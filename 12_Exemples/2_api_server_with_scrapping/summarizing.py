import abc
import openai


class Summarizer(abc.ABC):
    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"Summarizer(model={self.model})"

    def get_model(self):
        return self.model

    def write_summary(self, file_path: str, summary: str):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(summary)

    @abc.abstractmethod
    def summarize(self, file_path: str):
        raise NotImplementedError("Subclasses must implement this method.")


class OpenAISummarizer(Summarizer):
    def __init__(self, model):
        super().__init__(model)

    def summarize(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Reduce number of tokens to summarize
        if len(content) > 50_000:
            content = content[:50_000]

        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """You are a helpful assistant that summarizes text.""",
                },
                {
                    "role": "user",
                    "content": f"""
                    INSTRUCTIONS:
                    - Provide a concise summary of the main points
                    - Focus on the key information and avoid unnecessary details
                    - Do not point out that it is HTML or other type of content
                    - Follow the language of the content
                    ACTION:
                    Summarize the following content:\n\n{content}\n\nSummary:
                    """,
                },
            ],
            max_tokens=500,
        )

        content = response.choices[0].message.content
        return content.strip() if content is not None else ""
