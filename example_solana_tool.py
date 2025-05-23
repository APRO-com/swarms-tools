import json
from swarms_tools.finance.unified_solana_coin_api import (
    fetch_solana_coin_info,
)


if __name__ == "__main__":

    result = fetch_solana_coin_info(
        ids="74SBV4zDXxTRgv1pEMoECskKBkZHc2yGPnc7GYVepump",  # Example token address
        show_extra_info=True,
    )

    print(json.dumps(result, indent=4))
