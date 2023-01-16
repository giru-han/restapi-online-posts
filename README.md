# REST API - JSON Posts

### The is solution repo for the test [Build a REST API](https://github.com/tribehired-devs/backend-test)

### Build Setup

1. Clone the repository to your local machine
2. navigate to the project directory in the command line
3. Run pip install `-r requirements.txt` to install all the necessary dependencies
4. Run python `application.py` to start the local server
5. The server will be running on http://localhost:5000/

### Usage

1. View list of Top Posts ordered by their number of Comments

    http://localhost:5000/top_posts

2. Filter the comments based on all the available fields. Endpoint must match full text

  ```
	- post_id
	- comment_id
	- comment_name
	- comment_email
	- comment_body
	- post_title
	- user_id
	- post_body
  ```

  http://localhost:5000/comment_filter?post_id={post_id}
  http://localhost:5000/comment_filter?post_title={post_title}
  
 3. Search the comments based on all the available fields. Endpoint can match any word or partial text.

  ```
  - comment_name
	- comment_email
	- comment_body
	- post_title
	- post_body
  ```

  http://localhost:5000/comment_search?post_id={post_id}
  
  *Note: This project is using a dummy jsonplaceholder api, so data will be same everytime you hit the endpoints.*
  
### Example
  Top Posts
  ![top_posts](https://user-images.githubusercontent.com/109772802/212638999-12bc0f15-9352-4a4c-8b56-f1e4cbf11a41.jpg)
  
  Comment Filter
  ![comment_filter](https://user-images.githubusercontent.com/109772802/212639108-16a46e09-0570-4629-8ec0-a2085c925a85.jpg)
  
  Rest API
  ![rest_api](https://user-images.githubusercontent.com/109772802/212639148-9fb31f4d-fc91-47f3-affc-ae1cf612e6f6.jpg)



