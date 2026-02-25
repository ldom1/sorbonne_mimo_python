import config
from fastapi import FastAPI
from scraping import Scraper
from summarizing import OpenAISummarizer

from pydantic import BaseModel


app = FastAPI()

config.logger.info("Starting Scrape and Summarize API...")


class ScrapeRequest(BaseModel):
    url: str


@app.get("/")
async def read_root():
    """Root endpoint that returns a welcome message.
    :return: A dictionary with a welcome message."""
    return {"message": "Welcome to the Scrape and Summarize API!"}


@app.get("/health")
async def health_check():
    """Health check endpoint to verify if the API is running.
    :return: A dictionary indicating the status of the API.
    """
    return {"status": "ok", "status_code": 200}


@app.post("/scrape_and_summarize")
async def scrape_and_summarize(request: ScrapeRequest):
    """
    Scrape the content of the given URL and summarize it.
    :param request: The request body containing the URL to scrape.
    :return: A dictionary containing the summary and file path.
    """
    url = request.url
    config.logger.info(f"Received request to scrape and summarize URL: {url}")
    if not url:
        return {"error": "URL is required", "status": "error", "status_code": 400}
    if not url.startswith("http"):
        return {"error": "Invalid URL format", "status": "error", "status_code": 400}

    try:
        # Scrape the content of the URL
        scraper = Scraper(url=url)
        file_path = scraper.run()
        summarizer = OpenAISummarizer(model="gpt-3.5-turbo-16k")

        config.logger.info(
            f"Scraping content from URL: {url}, using {summarizer.__str__()}"
        )

        response = summarizer.summarize(file_path=file_path)

        return {
            "summary": response,
            "file_path": file_path,
            "status": "success",
            "status_code": 200,
        }
    except Exception as e:
        config.logger.error(f"Error occurred while scraping and summarizing: {e}")
        return {"error": str(e), "status": "error", "status_code": 500}
