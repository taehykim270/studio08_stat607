import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

PATH_TO_PICKLE_FILE = "results/raw/loss_vs_gamma.pkl"

def plot_loss_vs_gamma(df, ax, *, _n_sim, _gamma, _mse_hat, _mse_hat_standard_error, SNR = 5):
    """
    Plot the loss versus gamma
    """
    if df[_n_sim][0] < 20:
        alpha=0.3
    else:
        alpha=1

    FIT_COLOR = "blue"

    gamma = df[_gamma]
    mse = df[_mse_hat]
    mse_std_err = df[_mse_hat_standard_error]
    
    ax.errorbar(x=gamma, y=mse, yerr=mse_std_err, label="Monte Carlo Loss", alpha=alpha, color="blue")

    smoothed_fit_below_1 = sm.nonparametric.lowess(df.loc[df[gamma] <= 1][_mse_hat], df.loc[df[gamma] <= 1][_gamma], frac=0.1, it=0)
    smoothed_fit_above_1 = sm.nonparametric.lowess(df.loc[df[gamma] > 1][_mse_hat], df.loc[df[gamma] > 1][_gamma], frac=0.1, it=0)
    
    plt.plot(smoothed_fit_below_1[:, 0], smoothed_fit_below_1[:, 1], label="MC Risk", color=FIT_COLOR)
    plt.plot(smoothed_fit_above_1[:, 0], smoothed_fit_above_1[:, 1], color=FIT_COLOR)


    ax.set_ylabel("MSE Loss / Risk")
    ax.set_xlabel("$\\gamma$")
    ax.set_xscale("log")
    ax.set_xticks([0.1,0.2,0.5,1.0,2,5,10.0], labels=["0.1","0.2","0.5","1.0","2","5","10.0"])
    ax.set_yticks([0,2,4,6,8,10])

    ax.vlines([1],ymin=-0.2,ymax=10.2)
    ax.hlines(SNR, xmin=0.05,xmax=10.2)

    ax.set_ybound(lower=-0.2,upper=10.2)
    ax.set_xbound(lower=0.05,upper=10.2)


if __name__ == "__main__":
    # Load the DataFrame from the pickle file
    df = pd.read_pickle(PATH_TO_PICKLE_FILE)

    pd.DataFrame()["n_sim"]

    # Columns of DataFrame:
    _n_sim = "n_sim"
    _gamma = "gamma"
    _mse_hat = "mse_hat"
    _mse_hat_standard_error = "mse_hat_standard_error"

    n_sim = df["n_sim"].unique()


    fig, axs = plt.subplots((1,len(n_sim)))

    for i, n_sim in enumerate(n_sim):
        plot_loss_vs_gamma(df.loc[df[_n_sim] == n_sim], ax=axs[i], _n_sim=_n_sim, _gamma=_gamma, _mse_hat=_mse_hat, _mse_hat_standard_error=_mse_hat_standard_error)

    plt.savefig("results/figures/loss_vs_gamma.pdf")