import requests
from django.conf import settings


class GiteaUserExistsError(Exception):
    pass


class GiteaCreateError(Exception):
    pass


def create_gitea_user(data: dict):
    url = f"{settings.GITEA_URL}/api/v1/admin/users"

    headers = {
        "Authorization": f"token {settings.GITEA_ADMIN_TOKEN}",
        "Content-Type": "application/json",
    }

    username = data.get("username")

    if not username:
        raise GiteaCreateError("Username is required")

    try:
        check_url = f"http://localhost:3000/api/v1/users/{username}"

        check_response = requests.get(check_url, headers=headers)

        if check_response.status_code == 200:
            raise GiteaUserExistsError(f"User '{username}' already exists in Gitea")

        response = requests.post(url, json=data, headers=headers)

        if response.status_code >= 400:
            try:
                error_detail = response.json()
            except Exception:
                error_detail = response.text

            raise GiteaCreateError(
                f"Gitea error {response.status_code}: {error_detail}"
            )

        return response.json()

    except requests.RequestException as e:
        raise GiteaCreateError(f"Request failed: {str(e)}")
    
def create_repository(data: dict):
    username = data.get("username")

    if not username:
        raise GiteaCreateError("Username is required")

    headers = {
        "Authorization": f"token {settings.GITEA_ADMIN_TOKEN}",
        "Content-Type": "application/json",
    }

    check_url = f"{settings.GITEA_URL}/api/v1/users/{username}"
    repo_url = f"{settings.GITEA_URL}/api/v1/admin/users/{username}/repos"

    try:
        check_response = requests.get(check_url, headers=headers)

        if check_response.status_code == 404:
            raise GiteaCreateError(f"User '{username}' not found")

        if check_response.status_code != 200:
            raise GiteaCreateError(
                f"Unable to verify user ({check_response.status_code})"
            )

        repo_data = data.copy()
        repo_data.pop("username", None)

        response = requests.post(
            repo_url,
            json=repo_data,
            headers=headers,
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:
        raise GiteaCreateError(str(e))
