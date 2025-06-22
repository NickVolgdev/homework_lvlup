import logging
from yandex_search_api import YandexSearchAPIClient
from yandex_search_api.client import SearchType


def main():
    # Initialize client with your credentials
    client = YandexSearchAPIClient(
        folder_id="your_folder_id",
        oauth_token="your_oauth_token"
    )
    # How to get folder_id: https://yandex.cloud/en-ru/docs/resource-manager/operations/folder/get-id
    # How to get  oauth_token:  https://yandex.cloud/en-ru/docs/iam/concepts/authorization/oauth-token

    links = client.get_links(
        query_text="Python library for yandex search",
        search_type=SearchType.RUSSIAN,
        n_links=5
    )
    
    print("Search results:", links)

if __name__ == '__main__':
    main()
