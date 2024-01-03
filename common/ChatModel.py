from enum import StrEnum, unique


@unique
class ChatModel(StrEnum):
    GPT4 = "gpt4"
    GPT3_5 = "gpt3.5"
    GEMINI = "gemini"

