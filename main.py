import logging
from typing import Optional

from fastapi import FastAPI
from google.cloud import aiplatform
from google.oauth2 import service_account
from pydantic import BaseModel, Field

from service.GeminiService import code_generate

# Initialize gcloud login
credentials = service_account.Credentials.from_service_account_file('joohanlee-playground-d64f38409fea.json')
aiplatform.init(
    project="joohanlee-playground",
    location="us-central1",
    credentials=credentials,
    service_account="vertex-api-user@joohanlee-playground.iam.gserviceaccount.com",
)

logging.basicConfig(level=logging.INFO)
app = FastAPI()


@app.get("/openai/chat")
async def openai_chat():
    pass


@app.get("/google/codeChat")
async def google_code_chat():
    pass


class CodeGenerationRequest(BaseModel):
    question: str = Field(min_length=1)


@app.get("/google/codegen")
async def google_code_generation(request: CodeGenerationRequest):
    response = await code_generate(text=request.question)
    return {"response": response.text}

class CodeCompletionRequest(BaseModel):
    question: str = Field(min_length=1)


@app.get("/google/codegen")
async def google_code_generation(request: CodeGenerationRequest):
    response = await code_generate(model=request.model, text=request.question)
    return {"response": response.text}


class CreateUserRequest(BaseModel):
    username: str
    email: str
    token: str
    first_name: str
    last_name: str


@app.post("/users")
async def create_user(request: CreateUserRequest):
    pass


@app.get("/ping")
async def ping():
    return "pong"
