import numpy as np
import matplotlib.pyplot as plt
from dbda2e_utilities import effective_sample_size, autocorr


def metropolis(prior, likelihood, traj_length=50000,
               start_position=0.01, proposal_sd=0.2):
    trajectory = np.repeat(0.0, traj_length+1)
    trajectory[0] = start_position

    for t in xrange(traj_length):
        current_position = trajectory[t]
        proposed_jump = np.random.normal(loc=0, scale=proposal_sd, size=1)
        proposed_position = current_position + proposed_jump
        current_prob = prior(current_position) * likelihood(current_position)
        proposed_prob = prior(proposed_position) * likelihood(proposed_position)
        prob_accept = min(1, proposed_prob/current_prob)
        if np.random.uniform(0, 1) < prob_accept:
            trajectory[t+1] = proposed_position
        else:
            trajectory[t+1] = current_position

    return trajectory


def plot_trajectory(trajectory):
    (fig, (ax1, ax2, ax3)) = plt.subplots(3, 1, sharex=True)

    ess = effective_sample_size(trajectory)
    ax1.set_title("Posterior, ess = {0}".format(ess))
    ax1.hist(trajectory, bins=100)
    ax1.set_xlabel("$\\theta$")
    ax1.set_xlim(0, 1)

    ax2.set_title("Beginning of Chain")
    ax2.set_xlabel("$\\theta$")
    ax2.set_ylabel("Step in Chain")
    ax2.set_xlim(0, 1)
    ax2.plot(trajectory[:100], range(100))

    ax3.set_title("End of Chain")
    ax3.set_xlabel("$\\theta$")
    ax3.set_ylabel("Step in Chain")
    traj_length = len(trajectory)
    ax3.plot(trajectory[-100:], range(traj_length-100, traj_length))


def plot_autocorrelation(trajectory, lag=10):
    fig = plt.figure()
    ac = autocorr(trajectory, lag)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("autocorrelation, lag = {0}, cor = {1}".format(lag, ac))
    ax.set_xlabel("tail")
    ax.set_ylabel("head")
    ax.plot(trajectory[:-lag], trajectory[lag:])
