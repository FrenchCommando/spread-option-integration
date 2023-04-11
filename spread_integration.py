import numpy as np
from scipy.stats import norm
from scipy.integrate import quadrature


def spread_integration_function(
    s1, s2, rho,
    k1, k2, k,
):
    z1max1 = np.log(k1) / s1 + 0.5 * s1
    z1max2 = np.log(k2 - k) / s1 + 0.5 * s1
    z1max = min(z1max1, z1max2)
    z1min = -10

    def integrand(z):
        f12 = np.exp(-0.5 * rho * rho * s2 * s2 + rho * s2 * z)
        f11 = np.exp(-0.5 * s1 * s1 + s1 * z)
        s22 = np.sqrt(1 - rho * rho) * s2
        f11_plus_k = np.clip(f11 + k, a_min=1e-20, a_max=None)
        z_min = np.log(f11_plus_k / f12) / s22 + 0.5 * s22
        z_max = np.log(k2 / f12) / s22 + 0.5 * s22
        i = f12 * (norm.cdf(x=z_max - s22) - norm.cdf(x=z_min - s22)) \
            - (f11 + k) * (norm.cdf(x=z_max) - norm.cdf(x=z_min))
        return i * norm.pdf(x=z)
    return quadrature(integrand, a=z1min, b=z1max)[0]


def run_integration():
    integration_args = dict(
        s1=0.3,
        s2=0.2,
        rho=0.5,
        k1=1.1,
        k2=1.2,
        k=0.02,
    )
    out = spread_integration_function(**integration_args)
    print(out)


def main():
    run_integration()


if __name__ == '__main__':
    main()
