
-- create from faker_users 
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Robin Snyder', 0, NOW(), NOW());
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Steven Bell', 0, NOW(), NOW());
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Jacob Wilson', 0, NOW(), NOW());
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Roger Mccoy', 0, NOW(), NOW());
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Janice Callahan', 0, NOW(), NOW());
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Heather Collins', 0, NOW(), NOW());
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Stacy Dodson', 0, NOW(), NOW());
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Lisa Oneill', 0, NOW(), NOW());
INSERT INTO users (name, followers_count, create_at, update_at) VALUES('Lori Gomez MD', 0, NOW(), NOW());

-- create from faker_tweets
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('Begin almost commercial air game office play rich. Always position television some hope.
Collection his firm buy arrive. Bill two management admit stock.', 1, True, NOW(), NOW());
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('Responsibility yetmajority effort role tree kitchen. Tv western party necessary get benefit. Tell again institution pretty source PM.', 2, False, NOW(), NOW());
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('Effort service machine its rest security.
Plan professor really floor part difference past. Dream relationship possible thus. Drug something with draw cell return share produce.', 3, False, NOW(), NOW());
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('Tree ten more clearly account marriage lay. Challenge worry that. Own I believe share agreement another common.', 4, True, NOW(), NOW());
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('Prove people create wait. Fast return impact road still staff his.
Audience address either parent nice machine. Fall follow public sign.', 5, True, NOW(), NOW());
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('From something layarticle under gun want. Break else agreement health speak respond positive. Everybody return debate nature.', 6, True, NOW(), NOW());
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('Put provide rich president ask join evening citizen. Herself car me game itself color already. Door authority card kindhuge despite eye.', 7, True, NOW(), NOW());
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('Charge item towardcost style. Toward next perform probably manage couple.
Magazine sea space quality. Blue trial north I. Space interview draw popular subject thing order over.', 8, True, NOW(), NOW());
INSERT INTO tweets (tweet_txt, user_id, is_delete, create_at, update_at) VALUES ('Trouble Democrat standard. Local past share great some. Argue he economic child least stand military.', 9, True, NOW(),NOW());

-- create from faker_favorites
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (6, 1, NOW());
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (5, 2, NOW());
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (1, 3, NOW());
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (2, 4, NOW());
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (4, 5, NOW());
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (5, 6, NOW());
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (1, 7, NOW());
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (2, 8, NOW());
INSERT INTO favorites (user_id, tweet_id, create_at) VALUES (6, 9, NOW());

-- create from faker_connections
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (1, 8, NOW());
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (2, 3, NOW());
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (3, 8, NOW());
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (4, 3, NOW());
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (5, 4, NOW());
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (6, 4, NOW());
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (7, 2, NOW());
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (8, 8, NOW());
INSERT INTO connections (follower_id, followee_id, create_at) VALUES (9, 9, NOW());

-- create from faker_reply
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (1, 3, 'Hard American blue attorney road stay. Tax effort play direction.
Pick probably organization meet best. Whatever with pick religious these.', NOW());
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (9, 3, 'Economic mentionavailable paper sister. Scientist quickly particular each with participant.', NOW());
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (8, 5, 'Though lay assume analysis. Budget month put wish game unit face.
Until north simply foot room history up.
Pretty size western than reduce expert wait avoid. Husband institution return.', NOW());
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (5, 6, 'Until important left avoid full. Government another year because official long audience unit.', NOW());
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (4, 9, 'Price piece never ago across. Organization side artist treatment peace blood. Fight method people good parent.
News read participant. Well traditional road look audience. Scientist turn expect dream.', NOW());
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (4, 4, 'Them account but use. Whether door skin experience though. Population give reach.', NOW());
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (1, 2, 'Hold should bar occur sense scientist a. Heart month probably forget environment wall.', NOW());
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (8, 6, 'International worry happen order fund seem trial. Information approach east. Successful each under once keep.', NOW());
INSERT INTO reply (user_id, tweet_id, reply_text, create_at) VALUES (2, 7, 'Glass perform audience see. Fly lead old future also shake popular nice. Effect hundred next next first population.', NOW());