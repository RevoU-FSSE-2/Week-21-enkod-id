from dataclasses import dataclass 

@dataclass
class TweetDomain:
    id: int
    user_id: int
    tweet: str
    published_at: str
    likes: int = 0  # new field
    retweets: int = 0  # new field