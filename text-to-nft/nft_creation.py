import os
import json
from solana.rpc.api import Client
from solders.pubkey import Pubkey as PublicKey
from cryptography.fernet import Fernet
from api.metaplex_api import MetaplexAPI


PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")

cfg = {
    "PRIVATE_KEY": PRIVATE_KEY,
    "PUBLIC_KEY": PUBLIC_KEY,
    "DECRYPTION_KEY": Fernet.generate_key().decode("ascii"),
}
api_endpoint = "https://api.testnet.solana.com/"
# get SOL on account A
# response = Client(api_endpoint).request_airdrop(
#     PublicKey.from_string(PUBLIC_KEY), int(1e10)
# )

# Create API
metaplex_api = MetaplexAPI(cfg)

# Deploy
print("About to deploy")
response = metaplex_api.deploy(api_endpoint, "A" * 32, "A" * 10, 0)
print(f"Deploy response: {response}")
contract = json.loads(response)["contract"]

# Topup - The base58 encoded public key of the destination address
# topup_response = json.loads(metaplex_api.topup(api_endpoint, PUBLIC_KEY))
# print(f"Topup {PUBLIC_KEY} response:", topup_response)
# if topup_response["status"] != 200:
#     raise Exception("Non-200 response: " + str(topup_response))

RECEIVER_PUBLIC_KEY = "By3RECZEGmkfkqd5FqeJAEAJBsV3ko8qbvMxQRck8uzy"

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
        RECEIVER_PUBLIC_KEY,
        "https://ipfs.io/ipfs/bafkreidr5cnmualj2eh7g6bpe2iztglbfvottfceamswqevlye7negmkcq",
    )
)
print(f"Mint response: {mint_response}")
if mint_response["status"] != 200:
    raise Exception("Non-200 response: " + str(mint_response))

# Send
# print("About to send")
# """
# contract_key: (str) The base58 encoded public key of the mint address
# sender_key: (str) The base58 encoded public key of the source address (from which the contract will be transferred)
# dest_key: (str) The base58 encoded public key of the destinaion address (to where the contract will be transferred)
# encrypted_private_key: (bytes) The encrypted private key of the sender
# """
# encrypted_key = metaplex_api.cipher.encrypt(
#     bytes(
#         [
#             95,
#             46,
#             174,
#             145,
#             248,
#             101,
#             108,
#             111,
#             128,
#             44,
#             41,
#             212,
#             118,
#             145,
#             42,
#             242,
#             84,
#             6,
#             31,
#             115,
#             18,
#             126,
#             47,
#             230,
#             103,
#             202,
#             46,
#             7,
#             194,
#             149,
#             42,
#             213,
#         ]
#     )
# )
# send_response = json.loads(
#     metaplex_api.send(
#         api_endpoint,
#         contract,
#         PUBLIC_KEY,
#         RECEIVER_PUBLIC_KEY,
#         encrypted_key,
#     )
# )

# print(f"Send response: {send_response}")
# if send_response["status"] != 200:
#     raise Exception("Non-200 response: " + str(send_response))

print("Success!")
