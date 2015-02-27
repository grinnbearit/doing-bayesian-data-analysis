import numpy as np


def hdi_of_icdf(dist, cred_mass=0.95):
    alpha = 1.0 - cred_mass
    l, u = dist.ppf(alpha/2), dist.ppf(1 - alpha/2)
    return (l, u)


def beta_ab_from_mean_kappa(mean, kappa):
    if mean <= 0 or mean >= 1:
       raise Exception("must have 0 < mean < 1")
    if kappa <= 0:
       raise Exception("kappa must be > 0")
    a = mean * kappa
    b = (1.0 - mean) * kappa
    return {"a": a, "b": b}


def beta_ab_from_mode_kappa(mode, kappa):
    if mode <= 0 or mode >= 1:
        raise Exception("must have 0 < mode < 1")
    if kappa <= 2:
        raise Exception("kappa must be > 2 for mode parameterization")
    a = mode * (kappa - 2) + 1
    b = (1.0 - mode) * (kappa - 2) + 1
    return {"a": a, "b": b}


def beta_ab_from_mean_sd(mean, sd):
    if mean <=0 or mean >=1:
        raise Exception("must have 0 < mean < 1")
    if sd <= 0:
        raise Exception("sd must be > 0")
    kappa = mean * (1.0 - mean)/(sd**2 - 1)
    if kappa <= 0:
        raise Exception("invalid combination of mean and sd")
    a = mean * kappa
    b = (1.0 - mean) * kappa
    return {"a": a, "b": b}


def autocorr(data, lag=1):
    """Autocorrelation function"""
    left_window = data[:-lag]
    right_window = data[lag:]
    corr_matrix = np.corrcoef(np.array([left_window, right_window]))
    return corr_matrix[0, 1]


def effective_sample_size(data, max_lag=1000, min_acf=0.05):
    N = len(data)
    sum_acf = autocorr(data)

    for lag in xrange(2, max_lag):
        sum_acf += autocorr(data, lag)
        if sum_acf < 0.05:
            break

    return N/(1 + 2*sum_acf)
