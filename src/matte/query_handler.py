from api_manager import call_api
from local_fs_manager import lookup_local


def api_lookup(api_job):
    print(f"[Query Handler] Looking up API: {api_job}.")
    endpoint = f"placeholder made with: {api_job}."
    call_api(endpoint)
    return {}


def local_lookup(local_job):
    print(f"[Query Handler] Looking up local files: {local_job}.")
    filepath = f"placeholder made with: {local_job}."
    lookup_local(filepath)
    return {}


def handle_query(query):
    print(f"[Query Handler] Handling user query: {query}.")

    # Define data that needs to go into lookup handlers
    api_job = "placeholder"
    local_job = "placeholder"

    # Look up data in sources
    api_json = api_lookup(api_job)
    local_json = local_lookup(local_job)

    combo_json = api_json.update(local_json)
    return combo_json
