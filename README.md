# Studio 08: Benign Overfitting --- Hastie et al. (2022)

Per the assignment outline, we aim to address the following:

### 1. Objective

1. Reproduce Figure 2 of Hastie et al. (2022), building on the code you wrote last week. This challenges the extensibility of the code you wrote. You can use the solution on canvas.
2. Explore three regimes for the number of simulation replications per scenario $n_{\text{sim}} \in\{1,50,1000\}$. For $n_{\text{sim}}=1$, we will model the target using nonparametric regression.

### 2. Experimental setup

Consider the following linear model

$$y = X\beta + \varepsilon,\quad X_{ij},\varepsilon_i \overset{\mathrm{iid}}{~} N(0,1),$$

where $X\in\mathbb{R}^{n\times p}$, $\varepsilon\in\mathbb{R}^n$ and $\beta=\sqrt{\frac{r^2}{p}}\mathbf{1}_p.$

- Fix $n=200$ and $r^{2}=5.$
- Set $p=[\gamma n]$, where we vary $\gamma\in(0.1,10).$


### 3. We estimate using ridgeless least squares regression

### 4. Output

We produce a figure that compares the MSE (risk) of the least squares estimator with gamma, the ratio p/n of the dimension of the space to the number of regression points.