import os
import json
from cryptography.fernet import Fernet
from api.metaplex_api import MetaplexAPI
from get_api_key import get_api_key


def create_nft(name, symbol, receiver_public_key: str, link: str) -> None:
    PRIVATE_KEY = get_api_key("text_to_nft/private_key") # os.getenv("PRIVATE_KEY")
    PUBLIC_KEY = get_api_key("text_to_nft/public_key") # os.getenv("PUBLIC_KEY")

    cfg = {
        "PRIVATE_KEY": PRIVATE_KEY,
        "PUBLIC_KEY": PUBLIC_KEY,
        "DECRYPTION_KEY": Fernet.generate_key().decode("ascii"),
    }
    api_endpoint = "https://api.testnet.solana.com/"

    # Create API
    metaplex_api = MetaplexAPI(cfg)

    # Deploy
    print("About to deploy")
    deploy_response = json.loads(metaplex_api.deploy(api_endpoint, name, symbol, 0))
    print(f"Deploy response: {deploy_response}")
    if deploy_response["status"] != 200:
        raise Exception("Non-200 response: " + str(deploy_response))
    contract = deploy_response.get("contract")
    if not contract:
        raise Exception("No contract in response")

    # Mint
    print("About to mint")
    """
    contract_key: (str) The base58 encoded public key of the mint address
    dest_key: (str) The base58 encoded public key of the destinaion address (where the contract will be minted)
    link: (str) The link to the content of the the NFT
    """
    mint_response = json.loads(
        metaplex_api.mint(
            api_endpoint,
            contract,
            receiver_public_key,
            link,
        )
    )
    print(f"Mint response: {mint_response}")
    if mint_response["status"] != 200:
        raise Exception("Non-200 response: " + str(mint_response))

    print("Success!")
