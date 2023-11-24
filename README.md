## Assignment Database Design

User
- id (primary key)
- username (string, 20)
- password (string - hashed, bcrypt)
- bio (string, 150)


Tweet
- id (primary key)
- user_id (FK user.id)
- tweet
- published_at (datetime, default=utcnow)


Following (association table)
- id (primary key)
- user_id (FK user.id)
- following_user_id (FK user.id)



```


4. User Profile API
```
User.query.get(user_id)

Tweet.query.filter_by(user_id=user_id).order_by(Tweet.published_at.desc()).limit(10).all()

following = Following.query.filter(user_id=user_id).count()

follower = Following.query.filter(following_user_id=user_id).count()
```

5. Post a Tweet API
```
Tweet(user_id=user_id, tweet=tweet)
db.session.add()
```
