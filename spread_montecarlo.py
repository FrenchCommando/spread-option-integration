import numpy as np


def spread_mc(
    s1, s2, rho,
    k1, k2, k,
    n_mc,
):
    mu = [-0.5 * s1 * s1, -0.5 * s2 * s2]
    sigma = [[s1 * s1, rho * s1 * s2], [rho * s1 * s2, s2 * s2]]
    normals = np.random.multivariate_normal(
        mean=mu,
        cov=sigma,
        size=n_mc,
    )
    r = np.exp(normals)
    spread = r[:, 1] - r[:, 0] - k
    call_spread = np.clip(spread, a_min=0, a_max=None)
    i1 = r[:, 0] < k1
    i2 = r[:, 1] < k2
    i = i1 & i2
    option = call_spread * i
    price = np.mean(option)
    return price


def run_montecarlo():
    mc_args = dict(
        s1=0.3,
        s2=0.2,
        rho=0.5,
        k1=1.1,
        k2=1.2,
        k=0.02,
        n_mc=100000,
    )
    spread_mc(**mc_args)


def main():
    run_montecarlo()


if __name__ == '__main__':
    main()
