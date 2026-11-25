"""
Paginated Spotify Web API extraction with automatic token refresh.

Part of: Batch Data Ingestion from the Spotify API
Author : Faizan Saleem Siddiqui (https://github.com/FaizanSSDQ)
Built during the DeepLearning.AI & AWS Data Engineering Professional Certificate.
"""

from typing import Callable

import requests
from authentication import get_auth_header


def _refresh_headers(get_token: Callable, **kwargs) -> dict | None:
    """Request a new token and return fresh auth headers (None if refresh failed)."""
    token_response = get_token(**kwargs)
    if "access_token" in token_response:
        print("Token has been refreshed")
        return get_auth_header(access_token=token_response["access_token"])
    print("Failed to refresh token.")
    return None


def get_paginated_new_releases(base_url: str, access_token: str, get_token: Callable, **kwargs) -> list:
    """Follow the `next` links of the new-releases endpoint and collect every album.

    Args:
        base_url: Base URL for API requests
        access_token: Access token
        get_token: Function that requests a new access token (called on HTTP 401)

    Returns:
        List of album objects
    """
    headers = get_auth_header(access_token=access_token)
    request_url = base_url
    new_releases_data = []

    try:
        while request_url:
            print(f"Requesting to: {request_url}")
            response = requests.get(url=request_url, headers=headers, timeout=30)

            if response.status_code == 401:  # token expired
                headers = _refresh_headers(get_token, **kwargs)
                if headers is None:
                    return []
                continue  # retry the same page with the new token

            response.raise_for_status()
            response_json = response.json()
            new_releases_data.extend(response_json["albums"]["items"])
            request_url = response_json["albums"]["next"]

        return new_releases_data

    except Exception as err:
        print(f"Error occurred during request: {err}")
        return []


def get_paginated_album_tracks(
    base_url: str, access_token: str, album_id: str, get_token: Callable, **kwargs
) -> list:
    """Collect every track of one album from the /albums/{album_id}/tracks endpoint.

    Args:
        base_url: Base URL for endpoint requests
        access_token: Access token
        album_id: Id of the album to query
        get_token: Function that requests a new access token (called on HTTP 401)

    Returns:
        List of track objects
    """
    headers = get_auth_header(access_token=access_token)
    request_url = f"{base_url}/{album_id}/tracks"
    album_data = []

    try:
        while request_url:
            print(f"Requesting to: {request_url}")
            response = requests.get(url=request_url, headers=headers, timeout=30)

            if response.status_code == 401:  # token expired
                headers = _refresh_headers(get_token, **kwargs)
                if headers is None:
                    return []
                continue

            response.raise_for_status()
            response_json = response.json()
            album_data.extend(response_json["items"])
            request_url = response_json["next"]

        return album_data

    except Exception as err:
        print(f"Error occurred during request: {err}")
        return []
