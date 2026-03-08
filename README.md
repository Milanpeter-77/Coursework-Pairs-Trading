# Statistical Arbitrage — Pairs Trading

This project explores **statistical arbitrage through pairs trading**, using cointegration techniques to identify mean-reverting relationships between stocks.
The analysis scans the **Dow Jones Global Titans 50** universe and identifies candidate pairs whose price relationships exhibit statistical evidence of equilibrium behavior.

The repository demonstrates the full workflow of a simple quantitative trading pipeline:

* data preparation
* cointegration testing
* spread construction
* signal generation
* strategy backtesting

## Project Motivation

Pairs trading is one of the most commonly taught strategies in quantitative finance because it introduces several fundamental concepts:

* statistical modeling of financial time series
* cointegration and stationarity testing
* relative value trading
* market-neutral portfolio construction
* algorithmic signal generation

Instead of forecasting the direction of individual assets, the strategy trades **relative mispricings between two assets**.

If two price series share a long-run equilibrium relationship, deviations from this equilibrium may provide trading opportunities.

## Data

The project uses constituents of the **Dow Jones Global Titans 50**, a large-cap global equity index.

Data includes:

* Daily stock prices
* Company metadata (sector, country)

Prices are converted to **log prices** to stabilize variance and make relationships more linear for regression.

## Methodology

The analysis follows the **Engle–Granger two-step cointegration framework**.

### Step 1 — Linear Relationship Estimation

For each pair of stocks:

$$
Y_t = α + β X_t + ε_t
$$

The regression estimates the **hedge ratio β** and produces residuals representing the spread.

### Step 2 — Stationarity Testing

The spread is tested for stationarity using:

* **Augmented Dickey–Fuller test (ADF)**
* **Phillips–Perron test (PP)**

If the residual series is stationary, the pair is considered **cointegrated**.

### Pair Ranking

All possible stock combinations are evaluated and ranked according to the average p-value of the ADF and PP tests.

Pairs with lower p-values exhibit stronger statistical evidence of mean reversion.

## Example Pair Diagnostics

The project generates diagnostic plots for candidate pairs showing:

* observed vs fitted log prices
* residual spread dynamics
* cointegration test results

Insert the figure here:

<img width="1043" height="868" alt="0-pairs-JPM-on-TTE" src="https://github.com/user-attachments/assets/f130730e-437a-40c3-b43b-bdda94a07091" />

This example (JPM vs TotalEnergies) shows **weak evidence of cointegration**, with high p-values in both unit root tests.


### Stronger Cointegration Example

The pair **Philip Morris (PM)** and **Royal Bank of Canada (RY)** shows much stronger statistical evidence of mean reversion.

Insert the figure here:

<img width="1043" height="868" alt="313-pairs-PM-on-RY" src="https://github.com/user-attachments/assets/b77c43bd-a912-4a7a-9f37-43f758d5564e" />

Interestingly, the companies belong to completely different industries:

* Tobacco
* Banking

This highlights an important aspect of statistical arbitrage: relationships are **statistical rather than economic**, and results should always be interpreted carefully.


## Trading Strategy

Once a cointegrated pair is identified, the spread is modeled as a **mean-reverting process**.

The strategy works as follows:

1. Estimate spread mean and standard deviation in a **training period (2019-2023)**
2. Monitor spread deviations in the **test period (2024)**
3. Generate signals when the spread crosses statistical thresholds

Example rule:

- Enter trade when |spread| > 1σ
- Exit trade when |spread| < 0.5σ


## Strategy Example

The following figure shows the trading strategy applied to the **PM–RY pair**:

<img width="1390" height="1000" alt="pairs-trading-strat-PM-on-RY" src="https://github.com/user-attachments/assets/bb231f38-af68-472b-a2a5-4be72e8a675e" />


The chart illustrates:

* spread dynamics
* trading signals
* cumulative strategy P&L

## Key Concepts Demonstrated

This project demonstrates several important quantitative finance concepts:

* cointegration testing
* statistical arbitrage
* mean-reverting processes
* market-neutral trading
* algorithmic signal generation
* backtesting methodology

## Future Extensions

Possible improvements include:

* Johansen multivariate cointegration testing
* dynamic hedge ratios
* transaction cost modeling
* portfolio-level stat-arb strategies
* machine learning for pair selection
