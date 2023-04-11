import matplotlib.pyplot as plt
import numpy as np

from spread_montecarlo import spread_mc
from spread_integration import spread_integration_function


def main():
    common_args = dict(
        s1=0.3,
        s2=0.2,
        rho=0.5,
        k1=1.1,
        k2=1.2,
    )
    strike_range = [
        -0.25 + 0.01 * x for x in range(60)
    ]
    spread_mc_range = [
        spread_mc(**dict(**common_args, k=strike_value, n_mc=100000))
        for strike_value in strike_range
    ]
    spread_integration_range = [
        spread_integration_function(**dict(**common_args, k=strike_value))
        for strike_value in strike_range
    ]
    plt.figure('SpreadOption vs Strike')
    plt.plot(strike_range, spread_mc_range, label="MC")
    plt.plot(
        strike_range, spread_integration_range, label="Integration",
        linestyle='dashed', dashes=(4, 1), linewidth=1
    )
    plt.legend()
    plt.xlabel("Strike")
    plt.ylabel("SpreadOption")
    plt.title(f"Spread vs Strike {common_args}")
    plt.grid(visible=True)
    plt.savefig("SpreadVsStrike.png")

    plt.figure('SpreadOption vs Strike - Diff')
    plt.plot(
        strike_range,
        np.array(spread_mc_range) - np.array(spread_integration_range)
    )
    plt.xlabel("Strike")
    plt.ylabel("SpreadOption - Diff")
    plt.title(f"Spread vs Strike - Diff {common_args}")
    plt.grid(visible=True)
    plt.savefig("SpreadVsStrikeDiff.png")
    plt.show()


if __name__ == '__main__':
    main()
