import os
import sys

from dotenv import find_dotenv, load_dotenv
from loguru import logger

# Environment variables
load_dotenv(find_dotenv())

# Logger
logger.remove()
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> |<red> PID {process}</red> | <level>{level: <8}</level>| <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
logger.add(
    sys.stdout,
    format=LOG_FORMAT,
    level=os.environ.get("LOG_LEVEL", "INFO"),
)

# HuggingFace API key
HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OUTPUT_FOLDER = "output"
