from gym.envs.registration import register

from trading_gym.envs.market_maker import MarketMaker
from trading_gym.envs.trend_following import TrendFollowing

register(
    id=TrendFollowing.id,
    entry_point='trading_gym.envs:TrendFollowing',
    max_episode_steps=1000000,
    nondeterministic=False
)

register(
    id=MarketMaker.id,
    entry_point='trading_gym.envs:MarketMaker',
    max_episode_steps=1000000,
    nondeterministic=False
)
