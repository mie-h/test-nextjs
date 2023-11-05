import base64
import os
import requests
from get_api_key import get_api_key


def text2img(text: str) -> str:
    engine_id = "stable-diffusion-xl-1024-v1-0"
    api_host = os.getenv("API_HOST", "https://api.stability.ai")
    api_key = get_api_key(
        "text_to_nft/stability_api_key2"
    )  # os.getenv("STABILITY_API_KEY")
    work_dir = os.getenv("LAMBDA_WORK_DIR", "./tmp")

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={"text_prompts": [{"text": text}]},
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    generated_image_path = f"{work_dir}/txt2img_{text}.png"
    for i, image in enumerate(data["artifacts"]):
        with open(generated_image_path, "wb") as f:
            f.write(base64.b64decode(image["base64"]))
    return generated_image_path
