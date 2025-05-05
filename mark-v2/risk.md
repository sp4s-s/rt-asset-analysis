# 📊 Financial Risk Measures: Formulas, Purposes, and Components
## 1. Standard Deviation (Volatility)

**Purpose:**Measures the dispersion of returns around the mean, indicating the asset's volatility

**Formula:**
\[
\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (R_i - \bar{R})^2}
\]

- \( R_i \):Return in period \( i \
- \( \bar{R} \):Average retur
- \( N \):Number of period

**Sub-components:**

- **Mean Return (\( \bar{R} \))**:Average of all returns
- **Variance**:Average of squared deviations from the mean

---

## 2. Value at Risk (VaR)

**Purpose:**Estimates the potential loss in value of a risky asset or portfolio over a defined period for a given confidence interval

**Formula (Parametric VaR):**
\[
\text{VaR}_{\alpha} = \mu + z_{\alpha} \cdot \sigma
\]

- \( \mu \):Expected retur
- \( z_{\alpha} \):Z-score corresponding to the confidence level \( \alpha \
- \( \sigma \):Standard deviation of return

**Sub-components:**

- **Confidence Level (\( \alpha \))**:Probability that the loss will not exceed VaR
- **Time Horizon**:Period over which VaR is calculated

---

## 3. Conditional Value at Risk (CVaR)

**Purpose:**Provides the expected loss exceeding the VaR, offering insight into tail risk

**Formula:**
\[
\text{CVaR}_{\alpha} = \mathbb{E}[-R \mid R \leq -\text{VaR}_{\alpha}]
\]

- \( \mathbb{E} \):Expected valu
- \( R \):Retur

**Sub-components:**

- **Tail Distribution**:Focuses on the worst-case losses beyond the VaR threshold

---

## 4. Beta (β)

**Purpose:**Measures an asset's sensitivity to market movements, indicating systematic risk

**Formula:**
\[
\beta = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}
\]

- \( R_i \):Return of the asse
- \( R_m \):Return of the marke

**Sub-components:**

- **Covariance**:Measures how two variables move together
- **Market Variance**:Variance of the market returns

---

## 5. Sharpe Ratio

**Purpose:**Evaluates risk-adjusted return, indicating how much excess return is received for the extra volatility endured

**Formula:**
\[
\text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}
\]

- \( R_p \):Portfolio retur
- \( R_f \):Risk-free rat
- \( \sigma_p \):Standard deviation of the portfolio's excess retur

**Sub-components:**

- **Excess Return**:Difference between portfolio return and risk-free rate
- **Portfolio Volatility**:Standard deviation of portfolio returns

---

## 6. Drawdown

**Purpose:**Measures the decline from a historical peak in investment value, indicating downside risk

**Formula:**
\[
\text{Drawdown}_t = \frac{P_t - P_{\text{peak}}}{P_{\text{peak}}}
\]

- \( P_t \):Portfolio value at time \( t \
- \( P_{\text{peak}} \):Historical peak portfolio valu

**Sub-components:**

- **Peak Value**:Maximum historical value before the drawdown
- **Trough Value**:Lowest value following the peak

---

## 7. Risk-Free Rate (\( R_f \))

**Purpose:**Represents the return on an investment with zero risk, serving as a benchmark for evaluating other investments

**Calculation:**

- **Nominal Risk-Free Rate**:Yield on government securities (e.g., 10-year government bonds)
- **Real Risk-Free Rate**:Adjusts the nominal rate for inflation

**Formula:**
\[
\text{Real } R_f = \frac{1 + \text{Nominal } R_f}{1 + \text{Inflation Rate}} - 1
\]

**India Context:**

-The 10-year Indian government bond yield is commonly used as the risk-free rate

**Sub-components:**

- **Government Bond Yield**:Return on sovereign debt instruments
- **Inflation Rate**:Rate at which the general price level of goods and services is rising

---

## 8. Equity Risk Premium (ERP)

**Purpose:**Represents the excess return that investing in the stock market provides over a risk-free rate

**Formula:**
\[
\text{ERP} = \text{Expected Market Return} - R_f
\]

**Sub-components:**

- **Expected Market Return**:Anticipated return from the market portfolio
- **Risk-Free Rate (\( R_f \))**:Return on risk-free investments

---

## 9. Capital Asset Pricing Model (CAPM)

**Purpose:**Determines the expected return on an asset based on its beta and the equity risk premium

**Formula:**
\[
\text{Expected Return} 


## 📉 Risk-Free Rate (Rf)

### 🔹 Definition
The **Risk-Free Rate (Rf)** is the theoretical rate of return of an investment with **zero risk**. It represents the interest an investor would expect from a **completely risk-free investment** over a specified period of time.

In most financial models, the **yield on government securities** (such as treasury bonds or bills) is used as a proxy for the risk-free rate, since these are backed by the government and considered virtually free of default risk.

---

### 🔹 Formula (Real Risk-Free Rate)

\[
\text{Real } R_f = \frac{1 + \text{Nominal } R_f}{1 + \text{Inflation Rate}} - 1
\]

Where:
- \( \text{Nominal } R_f \) = yield on a government bond
- \( \text{Inflation Rate} \) = expected annual inflation

---

### 🔹 Common Use Cases
- **Sharpe Ratio**:
  \[
  \text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}
  \]
- **CAPM**:
  \[
  E(R_i) = R_f + \beta_i (E(R_m) - R_f)
  \]
- **Equity Risk Premium (ERP)**:
  \[
  \text{ERP} = E(R_m) - R_f
  \]

---

### 🔹 In Practice (Example for India 🇮🇳)
In the Indian context, the **10-year Indian government bond yield** is often used as the risk-free rate.

> 💡 Example: If the 10-year government bond yield is **7.1%**, and expected inflation is **5.2%**, then the **real risk-free rate** is:
>
> \[
> \frac{1 + 0.071}{1 + 0.052} - 1 \approx 1.8\%
> \]

---

### 🔹 Key Considerations
- Risk-free rate is **time-dependent** (short-term vs long-term securities).
- Must be **currency-matched** with the investment.
- Real vs Nominal rate matters in inflation-adjusted models.

---
