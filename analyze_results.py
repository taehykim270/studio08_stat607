import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import os

PATH_TO_PICKLE_FILE = "results/raw/simulation_results.pkl"

def plot_loss_vs_gamma(df,
                       ax,
                       *,
                       _n_sim,
                       _gamma,
                       _mse_hat,
                       _mse_hat_standard_error,
                       SNR = 5,
                       alpha = 0.8,
                       write_y_axis_title = True):
    """
    Plot the loss versus gamma
    """
    # if df[_n_sim].iloc[0] < 20:
    #     alpha=0.3
    # else:
    #     alpha=

    FIT_COLOR = "black"
    TRUE_RISK_COLOR = "green"

    gamma = df[_gamma]
    mse = df[_mse_hat]
    mse_std_err = df[_mse_hat_standard_error]

    if mse_std_err.iloc[0] > 0:
        ax.errorbar(x=gamma,
                    y=mse,
                    yerr=mse_std_err,
                    label="Monte Carlo Loss",
                    alpha=alpha,
                    color="blue",
                    fmt='o',
                    markerfacecolor='blue',
                    markersize=1 if df[_n_sim].iloc[0]==1 else 4,
                    capsize=3,
                    zorder=1)
    else:
        ax.scatter(x=gamma,
                   y=mse,
                   label="Monte Carlo Loss",
                   alpha=alpha,
                   s=3,
                   zorder=1)

    smoothed_fit_below_1 = sm.nonparametric.lowess(df.loc[df[_gamma] <= 1][_mse_hat], df.loc[df[_gamma] <= 1][_gamma], frac=0.1, it=0)
    smoothed_fit_above_1 = sm.nonparametric.lowess(df.loc[df[_gamma] > 1][_mse_hat], df.loc[df[_gamma] > 1][_gamma], frac=0.1, it=0)
    
    ax.plot(smoothed_fit_below_1[:, 0], smoothed_fit_below_1[:, 1], label="MC Risk", color=FIT_COLOR)
    ax.plot(smoothed_fit_above_1[:, 0], smoothed_fit_above_1[:, 1], color=FIT_COLOR)

    gamma_grid_lower = np.linspace(0.1,0.99,50)
    asymptotic_risk_lower = gamma_grid_lower / (1 - gamma_grid_lower)

    gamma_grid_upper = np.linspace(1.01,10,50)
    asymptotic_risk_upper = SNR * (1 - 1 / gamma_grid_upper) + 1 / (gamma_grid_upper - 1)

    ax.plot(gamma_grid_lower, asymptotic_risk_lower, label="Asymptotic Risk", color=TRUE_RISK_COLOR)
    ax.plot(gamma_grid_upper, asymptotic_risk_upper, color=TRUE_RISK_COLOR)


    if write_y_axis_title:
        ax.set_ylabel("MSE Loss / Risk")
    ax.set_xlabel("$\\gamma$")
    ax.set_xscale("log")
    ax.set_xticks([0.1,0.2,0.5,1.0,2,5,10.0], labels=["0.1","0.2","0.5","1.0","2","5","10.0"])
    ax.set_yticks([0,2,4,6,8,10])

    ax.vlines([1],ymin=-0.2,ymax=10.2,linestyle='--')
    ax.hlines(SNR, xmin=0.05,xmax=10.2,linestyle='--')

    ax.set_ybound(lower=-0.2,upper=10.2)
    ax.set_xbound(lower=0.05,upper=10.2)

    ax.legend()

if __name__ == "__main__":
    # Load the DataFrame from the pickle file
    df = pd.read_pickle(PATH_TO_PICKLE_FILE)

    # pd.DataFrame()["n_sim"]

    # Columns of DataFrame:
    _n_sim = "_n_sim"
    _gamma = "_gamma"
    _mse_hat = "_mse_hat"
    _mse_hat_standard_error = "_mse_hat_standard_error"

    n_sim_values = df[_n_sim].unique()
    # print(n_sim_values)
    # print(df.head(10))


    fig, axs = plt.subplots(1,len(n_sim_values), figsize=(10,4), sharey=True)

    for i, n_sim in enumerate(n_sim_values):
        plot_loss_vs_gamma(df.loc[df[_n_sim] == n_sim],
                           ax=axs[i],
                           _n_sim=_n_sim,
                           _gamma=_gamma,
                           _mse_hat=_mse_hat,
                           _mse_hat_standard_error=_mse_hat_standard_error,
                           alpha = 0.1 if n_sim==1 else 0.5,
                           write_y_axis_title = (i == 0))

    os.makedirs("results/figures", exist_ok=True)
    fig.savefig("results/figures/figure.pdf")