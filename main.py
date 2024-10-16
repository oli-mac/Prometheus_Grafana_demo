
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import time
import os
import logging

app = FastAPI()

# Initialize Prometheus metrics
Instrumentator().instrument(app).expose(app)

# Configure logging to file (so Promtail can scrape logs)
log_file_path = 'logs/fastapi.log'  # Ensure this directory exists
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger("uvicorn")

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db/textdb")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TextEntry(Base):
    __tablename__ = "text_entries"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

# Retry logic for database connection
def init_db(retries=5):
    for attempt in range(retries):
        try:
            Base.metadata.create_all(bind=engine)
            logger.info("Database initialized successfully")
            return
        except Exception as e:
            logger.error(f"Attempt {attempt + 1} failed: {e}")
            if attempt + 1 == retries:
                logger.critical("Failed to initialize database after multiple attempts")
                raise
            time.sleep(5)

init_db()

class TextItem(BaseModel):
    content: str

@app.post("/text/")
def create_text(text_item: TextItem):
    db = SessionLocal()
    try:
        db_text = TextEntry(content=text_item.content)
        db.add(db_text)
        db.commit()
        db.refresh(db_text)
        logger.info(f"Text created with ID {db_text.id}")
        return {"id": db_text.id, "content": db_text.content}
    except Exception as e:
        logger.error(f"Error creating text entry: {e}")
        db.rollback()
        raise
    finally:
        db.close()

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
