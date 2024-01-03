from typing import Optional

from repo.gemini import code_generation, code_completion


async def code_generate(text: str):
    return await code_generation(text=text)


async def code_complete(prefix: str, suffix: Optional[str]):
    return await code_completion(prefix= prefix, suffix=suffix)

