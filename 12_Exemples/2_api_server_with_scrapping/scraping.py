import requests
from bs4 import BeautifulSoup
from config import OUTPUT_FOLDER
import os
import re


class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape(self) -> BeautifulSoup:
        """Scrape the content of the page at self.url and return a BeautifulSoup object."""
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {self.url}")
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    def clean_content(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Clean the scraped content by removing unnecessary tags."""
        for script in soup(["script", "style"]):
            script.decompose()
        common_tags = [
            "head",
            "title",
            "meta",
            "style",
            "noscript",
            "svg",
            "canvas",
            "iframe",
            "object",
            "embed",
        ]
        for tag in soup.find_all(common_tags):
            tag.decompose()
        return soup

    def get_filename(self) -> str:
        """
        Generate a safe filename from the URL.
        Handles edge cases such as trailing slashes, query strings, and root URLs.
        """
        # Remove protocol
        url = re.sub(r"^https?://", "", self.url)
        # Remove query and fragment
        url = url.split("?", 1)[0].split("#", 1)[0]
        # Remove trailing slash
        url = url.rstrip("/")
        # If nothing left, use 'index'
        if not url:
            return "index.html"
        # Replace slashes and illegal filename chars
        filename = re.sub(r"[^a-zA-Z0-9_\-\.]", "_", url)
        # Ensure .html extension
        if not filename.endswith(".html"):
            filename += ".html"
        return filename

    @staticmethod
    def save_to_file(content: str, file_path: str):
        """Save the given content to a file."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    def run(self):
        """Run the scraper and save the content to a file."""
        filename = self.get_filename()
        file_path = os.path.join(OUTPUT_FOLDER, filename)

        # Get the scraped content
        soup = self.scrape()

        # Clean the content
        cleaned_soup = self.clean_content(soup)

        # Convert cleaned soup to string
        content = cleaned_soup.prettify()
        if not isinstance(content, str):
            content = str(content)

        # Ensure the output directory exists
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        # Save the content to a file
        self.save_to_file(content, file_path)
        print(f"Content saved to {file_path}")
        return file_path
