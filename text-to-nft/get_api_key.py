import json
import boto3
from botocore.exceptions import ClientError

key_map = {
    "text_to_nft/stability_api_key": "STABILITY_API_KEY",
    "text_to_nft/nft_storage_api_key": "NFT_STORAGE_API_KEY"
}


def get_api_key(secret_name: str) -> str:
    region_name = "us-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = json.loads(get_secret_value_response["SecretString"])
    key_name = key_map.get(secret_name, "key")
    return secret[key_name]
