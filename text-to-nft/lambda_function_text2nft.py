from create_nft import create_nft
from text2img import text2img
from get_nftstorage_cid import get_nftstorage_cid
from upload_json_nftstorage import upload_json_nftstorage


def lambda_handler(event, context):
    text = event.get("text")
    if not text:
        raise Exception("text not found in event")
    name = event.get("name")
    if not name:
        raise Exception("name not found in event")
    symbol = event.get("symbol")
    if not symbol:
        raise Exception("symbol not found in event")
    receiver_public_key = event.get("receiver_public_key")
    if not receiver_public_key:
        raise Exception("receiver_public_key not found in event")

    generated_image_path = text2img(text)
    # generated_image_path = "./tmp/txt2img_zen temple.png"
    print(f"generated_image_path: {generated_image_path}")
    cid = get_nftstorage_cid(generated_image_path)
    imgURI = f"https://ipfs.io/ipfs/{cid}"
    description = f"Created by Stability AI using the text: {text}"
    print(f"imgURI: {imgURI}")
    upload_json_nftstorage(name, description, symbol, imgURI)

    # create_nft(name, symbol, receiver_public_key, imgURI)


if __name__ == "__main__":
    event = {
        "text": "pumpkin spice latte",
        "name": "name",
        "symbol": "symbol",
        "receiver_public_key": "2sUsc2GiqB3NM17DeBFb28UrsNwfbMJE9ZEYm4dnYipf",
    }
    lambda_handler(
        event,
        None,
    )
