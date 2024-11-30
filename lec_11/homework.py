"""
Use https://jsonplaceholder.typicode.com/ server and make GET POST PUT DELETE calls to the allowed endpoints.

For the GET calls iterate over the result and filter out titles that contain more than 6 words.
For the GET calls filter out that results which body contains more than 3 lines of description( \n )
"""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_filtered_results():
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        filtered_results = [
            post for post in data
            if len(post['title'].split()) <= 6 and post['body'].count('\n') <= 3
        ]
        if filtered_results:
            print("\n--- Filtered GET Results ---")
            for post in filtered_results:
                print(f"ID: {post['id']}, Title: {post['title']}")
        else:
            print("No posts found that match the filters.")
        return filtered_results
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

def create_post():
    payload = {
        "title": "Sample Title",
        "body": "This is a sample body for testing POST request.",
        "userId": 1
    }
    try:
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        response.raise_for_status()  # Raise error for failed request
        created_post = response.json()
        print("\n--- Created Post ---")
        print(f"ID: {created_post['id']}, Title: {created_post['title']}")
        return created_post
    except requests.exceptions.RequestException as e:
        print(f"Error creating post: {e}")
        return None

def update_post(post_id):
    payload = {
        "id": post_id,
        "title": "Updated Title",
        "body": "This is an updated body for testing PUT request.",
        "userId": 1
    }
    try:
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
        response.raise_for_status()
        updated_post = response.json()
        print("\n--- Updated Post ---")
        print(f"ID: {updated_post['id']}, Title: {updated_post['title']}")
        return updated_post
    except requests.exceptions.RequestException as e:
        print(f"Error updating post with ID {post_id}: {e}")
        return None

def delete_post(post_id):
    try:
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        print(f"\n--- DELETE Request ---")
        print(f"Post with ID {post_id} successfully deleted.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error deleting post with ID {post_id}: {e}")
        return False

if __name__ == "__main__":
    print("\n--- GET Request with Filtering ---")
    filtered_posts = get_filtered_results()
    
    print("\n--- POST Request ---")
    created_post = create_post()

    print("\n--- PUT Request ---")
    if created_post:
        updated_post = update_post(created_post['id'])

    print("\n--- DELETE Request ---")
    if created_post:
        delete_status = delete_post(created_post['id'])
