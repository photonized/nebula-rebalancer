import constants
import config

from bots.rebalance import create_then_redeem



cluster_address = constants.cluster_contracts[config.net][config.cluster]

create_then_redeem(config.total_capital, cluster_address, config.imbalance_threshold)
