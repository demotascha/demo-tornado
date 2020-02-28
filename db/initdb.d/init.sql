
CREATE TABLE users (
    user_id integer generated always as identity primary key,
    name character varying(80),
	followers_count int,
	create_at date,
	update_at date
);
CREATE INDEX users_name_index ON users (name);

CREATE TABLE connections (
	follower_id int references users(user_id),
	followee_id int references users(user_id),
	create_at date
);
CREATE INDEX connections_follower_index ON connections (follower_id);
CREATE INDEX connections_followee_index ON connections (followee_id);

CREATE TABLE tweets (
	tweet_id integer generated always as identity primary key,
	tweet_txt text not null,
	user_id int references users(user_id),
	is_delete boolean,
	create_at date,
	update_at date,
	delete_at date
);
CREATE INDEX tweets_user_id_create_at_index ON tweets (user_id, create_at);

CREATE TABLE favorites (
	user_id int references users(user_id),
	tweet_id int references tweets(tweet_id),
	create_at date
);
CREATE INDEX favorites_user_id_index ON favorites (user_id);
CREATE INDEX favorites_tweet_id_index ON favorites (tweet_id);

CREATE TABLE reply (
	user_id int references users(user_id),
	tweet_id int references tweets(tweet_id),
	reply_text text not null,
	create_at date
);
CREATE INDEX reply_user_id_index ON reply (user_id);
CREATE INDEX reply_tweet_id_index ON reply (tweet_id);
CREATE INDEX reply_create_at_index ON reply (create_at);