import numpy as np
from scipy.stats import beta as dbeta
from scipy.special import beta
import matplotlib.pyplot as plt
from dbda2e_utilities import hdi_of_icdf


def bern_beta((a, b), data, hdi=0.95):

    if a < 0 or b < 0:
        raise Exception("prior beta a, b should be greater than 0")
    if not ((data == 0) | (data == 1)).all():
        raise Exception("Data values must be 0 or 1")

    z = sum(data)
    N = len(data)

    post_a = a + z
    post_b = b + N - z

    theta = np.linspace(0.001, 0.999, 1000)
    p_theta = dbeta.pdf(theta, a, b)
    p_data_given_theta = theta**z * (1-theta)**(N-z)
    p_theta_given_data = dbeta.pdf(theta, post_a, post_b)

    p_data = beta(z+a, N-z+b)/beta(a, b)

    (fig, (ax1, ax2, ax3)) = plt.subplots(3, 1, sharex=True)

    ax1.set_title("Prior (beta)")
    ax1.set_xlabel("$\\theta$")
    ax1.set_ylabel("$dbeta(\\theta^*|{0},{1})$".format(a, b))
    ax1.plot(theta, p_theta)
    x1, x2 = hdi_of_icdf(dbeta(a, b), hdi)
    ax1.plot([x1, x2], [0, 0], "k-", linewidth=4)

    ax2.set_title("Likelihood (Bernoulli)")
    ax2.set_xlabel("$\\theta$")
    ax2.set_ylabel("$p(D|\\theta)$")
    ax2.plot(theta, p_data_given_theta)

    ax3.set_title("Posterior (beta)")
    ax3.set_xlabel("$\\theta$")
    ax3.set_ylabel("$dbeta(\\theta^*|{0},{1})$".format(post_a, post_b))
    ax3.plot(theta, p_theta_given_data)
    x1, x2 = hdi_of_icdf(dbeta(post_a, post_b), hdi)
    ax3.plot([x1, x2], [0, 0], "k-", linewidth=4)

    return (post_a, post_b)
