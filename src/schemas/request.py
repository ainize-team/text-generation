from pydantic import BaseModel, Field


class GenerationParameters(BaseModel):
    max_new_tokens: int = Field(
        default=16,
        gt=0,
        le=1024,
        description="he maximum numbers of tokens to generate, ignore the current number of tokens.",
    )
    repetition_penalty: float = Field(
        default=2.0, gt=0.0, description="The parameter for repetition penalty. 1.0 means no penalty."
    )
    num_return_sequences: int = Field(
        default=1,
        ge=1,
        le=5,
        description="The number of independently computed returned sequences for each element in the batch.",
    )


class TextGenerationRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=4096,
        description="String value to generate completions for",
    )
    generation_paramters: GenerationParameters
