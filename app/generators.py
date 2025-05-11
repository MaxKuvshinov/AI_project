import asyncio
from openai import AsyncOpenAI

# from config import API_KEY

client = AsyncOpenAI(api_key="")


async def gpt_text(req, model):
    completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": req}],
        model=model
    )
    print(completion.choices[0].message.content)

asyncio.run(gpt_text("Hello!", "gpt-4o"))