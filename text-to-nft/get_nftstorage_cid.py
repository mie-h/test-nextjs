import os
import nft_storage
from nft_storage.api import nft_storage_api
from get_api_key import get_api_key

# from nft_storage.model.error_response import ErrorResponse
# from nft_storage.model.upload_response import UploadResponse
# from nft_storage.model.unauthorized_error_response import UnauthorizedErrorResponse
# from nft_storage.model.forbidden_error_response import ForbiddenErrorResponse


def get_nftstorage_cid(generated_image_path: str) -> str:
    # Configure Bearer authorization (JWT): bearerAuth
    # TODO: learn what JWT is
    access_token = get_api_key(
        "text_to_nft/nft_storage_api_key"
    )  # os.getenv("NFT_STORAGE_API_KEY")
    print(access_token)
    configuration = nft_storage.Configuration(access_token=access_token)

    # Enter a context with an instance of the API client
    with nft_storage.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = nft_storage_api.NFTStorageAPI(api_client)

        body = open(generated_image_path, "rb")
        try:
            api_response = api_instance.store(body, _check_return_type=False)

            print(api_response)
            if api_response["ok"] == False:
                raise Exception("Non-200 response: " + str(api_response))
            cid = api_response["value"]["cid"]
        except nft_storage.ApiException as e:
            print("Exception when calling NFTStorageAPI->store: %s\n" % e)
            return
    return cid
