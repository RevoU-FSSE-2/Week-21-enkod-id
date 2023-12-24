from typing import List
from core.tweet.models import TweetDomain
from infrastructure.db import db
from .ports import ITweetAccessor

class TweetAccessor(ITweetAccessor):

    def create(self, user_id: int, tweet: str, published_at: str) -> TweetDomain:
        new_tweet = TweetDomain(id=None, user_id=user_id, tweet=tweet, published_at=published_at)
        db.session.add(new_tweet)
        db.session.commit()
        return new_tweet

    def get_all(self) -> List[TweetDomain]:
        return TweetDomain.query.all()