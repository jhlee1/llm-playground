import logging
from typing import Optional

from vertexai.language_models import CodeGenerationModel

logger = logging.getLogger(__name__)


async def code_generation(text: str,
                          model: str = "code-bison",
                          temperature: float = 0.5,
                          max_output_tokens: int = 164) -> object:
    return await code_completion(prefix=text, model=model, temperature=temperature, max_output_tokens=max_output_tokens)


# The model attempts to fill in the code in between the prefix and suffix.
async def code_completion(prefix: str,
                          suffix: Optional[str] = None,
                          model: str = "code-gecko",
                          temperature: float = 0.2,
                          max_output_tokens=1024) -> object:
    parameters = {
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
    }

    code_generation_model = CodeGenerationModel.from_pretrained(model)
    response = code_generation_model.predict(
        prefix=prefix,
        suffix=suffix,
        **parameters
    )

    logger.info(f"Response from Model: {response.text}")

    return response

