"""
Defines constants and objects used in PortfolioStrategy App.
"""

from enum import Enum
from vnpy.trader.translate import tr


APP_NAME = "PortfolioStrategy"


class EngineType(Enum):
    LIVE = tr("LIVE", "实盘")
    BACKTESTING = tr("BACKTESTING", "回测")


EVENT_PORTFOLIO_LOG = "ePortfolioLog"
EVENT_PORTFOLIO_STRATEGY = "ePortfolioStrategy"
