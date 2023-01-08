# venv\Scripts\activate.bat
import pandas as pd
import requests
from flask import Flask, request


# Consume Data (comments list)
all_comments = requests.get('https://jsonplaceholder.typicode.com/comments')
comments_df = pd.DataFrame(all_comments.json())
comments_df.rename(columns={'postId':'post_id',
                            'id':'comment_id',
                            'name':'comment_name',
                            'email':'comment_email',
                            'body':'comment_body'},
                   inplace=True)
comments_df.columns

# Consume Data (posts list)
all_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
posts_df = pd.DataFrame(all_posts.json())
posts_df.rename(columns={'userId':'user_id',
                         'id':'post_id',
                         'title':'post_title',
                         'body':'post_body'},
                inplace=True)
posts_df.set_index('post_id', inplace=True)
# posts_df['user_id'].dtype = int(5)
posts_df = posts_df.assign(total_number_of_comments = lambda x: comments_df['post_id'].value_counts().loc[x.index])
posts_df.reset_index(inplace=True)
posts_df.columns

# Merge Data both df
all_df = pd.merge(posts_df, comments_df, on='post_id', how='outer')
# all_df['comment_count'] = all_df.groupby('post_id')['post_id'].transform('count')
# all_df.columns
all_df[all_df['comment_body'].str.contains('expedita maiores', case=False)]

# Set up Flask
app = Flask(__name__)

# Set up route/endpoint
@app.route('/')
def index():
    return 'hello test'

@app.route('/top_posts')
def get_top_post():
    return posts_df.sort_values(by='total_number_of_comments', ascending=False).to_dict('records')

# Route to filter comments by any field (Must match full content)
@app.route('/comment_filter')
def filter_comment():

    pid   = request.args.get('post_id', type=int)
    cid   = request.args.get('comment_id', type=int)
    cname = request.args.get('comment_name', type=str)
    cmail = request.args.get('comment_email', type=str)
    cbody = request.args.get('comment_body', type=str)
    ptle  = request.args.get('post_title', type=str)
    uid   = request.args.get('user_id', type=int)
    pbody = request.args.get('post_body', type=str)

    field_ls = ['post_id', 'comment_id', 'comment_name', 'comment_email', 'comment_body', 'post_title', 'user_id', 'post_body']
    field_vs =[pid, cid, cname, cmail, cbody, ptle, uid, pbody]
    field_cs =['post_id', 'comment_id', 'comment_name', 'comment_email', 'comment_body', 'post_title', 'user_id', 'post_body']
    output_df = all_df

    for fi,val,col in zip(field_ls, field_vs, field_cs):
        if val:
            output_df = output_df[output_df[col] == val]
    return output_df.to_dict('records')

# Route to Search comments by any field (Must match full content for ids and partial text for strings)
@app.route('/comment_search')
def search_comment():

    pid = request.args.get('post_id', type=int)
    cid = request.args.get('comment_id', type=int)
    cname = request.args.get('comment_name', type=str)
    cmail = request.args.get('comment_email', type=str)
    cbody = request.args.get('comment_body', type=str)
    ptle = request.args.get('post_title', type=str)
    uid = request.args.get('user_id', type=int)
    pbody = request.args.get('post_body', type=str)

    field_ls = ['post_id', 'comment_id', 'comment_name', 'comment_email', 'comment_body', 'post_title', 'user_id', 'post_body']
    field_vs = [pid, cid, cname, cmail, cbody, ptle, uid, pbody]
    field_cs = ['post_id', 'comment_id', 'comment_name', 'comment_email', 'comment_body', 'post_title', 'user_id', 'post_body']
    output_df = all_df
    for fi,val,col in zip(field_ls, field_vs, field_cs):
        if val:
            if isinstance(val, str):
                output_df = output_df[output_df[col].str.contains(val, case=False)]
            else:
                output_df = output_df[output_df[col] == val]
    return output_df.to_dict('records')

# Run Server
if __name__ == "__main__":
    app.run(debug=False)
