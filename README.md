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




