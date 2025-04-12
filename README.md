# Ctrl+Defeat - Domain 2: Quantitative Trading

## 🧠 Project Overview
We are Group Ctrl+Defeat, and our project focuses on **Quantitative Trading** under Domain 2 of UMHackathon 2025. Our objective is to design and implement a robust backtesting framework and predictive model to generate profitable trading signals using **volatility-based market assumptions** and **machine learning (HMM)** techniques.

## 🎯 Problem Statement
In highly dynamic financial markets—especially crypto markets—price movements often reflect hidden market sentiment and volatility. Our goal is to build a model that detects these patterns, calculates a **Signal Score**, and uses it to make informed trading decisions.

---

## 📌 Key Assumption: Volatility Reflects Market Regime

Our hypothesis is:
> **“Market volatility (high - low) reflects sentiment or risk, and can be used as a predictive feature for generating profitable signals.”**

We assume:
1. If a candle has a much bigger range than usual, it might mean a breakout or trend is starting.
2. If a market is moving a lot today, it will probably keep moving a lot tomorrow too.
3. if the shadows are large compared to the full candle, it means the market is unsure - price was pushed away from the highs/lows. That could mean a potential reversal.

---

## 🛠️ Methodology

### 1. Data Collection & Preprocessing
- Data Sources: CryptoQuant, Glassnode, Coinglass, etc. Cybotrade API
- Time Interval: ≤ 1 day (e.g., 4H, 10M)
- Preprocessing includes:
  - Cleaning & normalizing candle data
  - Extracting OHLC features (Candle model)
  - Converting data into regime-detectable formats

---

### 2. Volatility Feature Engineering
We construct volatility-based features such as:
- **RangeVol** = High - Low  
- **VolCluster** = Rolling standard deviation of close prices  
- **WickRatio** = (High - max(Open, Close) + min(Open, Close) - Low) / (High - Low + ε)

📈 These features are combined into a **Signal Score**:
Signal Score = w1 * RangeVol + w2 * VolCluster - w3 * WickRatio

---

### 3. Hidden Markov Model (HMM)
- We train an HMM to detect latent market regimes (bullish, bearish, sideways).
- The model outputs the most probable regime for each time point.
- This regime is combined with Signal Score to form a trading signal.

---

### 4. Trading Strategy Execution
We apply several trading strategies:
- **Momentum Strategy** – Follow trends detected by HMM + Signal Score
- **Mean Reversion** – Trade based on price deviations from rolling mean
- **Breakout & Trend Following** – Based on volatility surges and regime switches

Risk management:
- Stop-loss / trailing stop
- Incorporate transaction fees (0.06%)

---

### 5. Backtesting Framework
Our framework tests strategies over multiple years and validates using:
- **Sharpe Ratio** (≥ 1.8)
- **Max Drawdown** (≥ -40%)
- **Trade Frequency** (≥ 3% of data rows)
- Visualized results (P&L curve, regime charts, volatility overlays)

---

## ✅ Evaluation Metrics
- Sharpe Ratio
- Maximum Drawdown
- Trade Frequency
- Annualized Return
- Profit Factor
- Win Rate
- Cumulative Return

---

## 📦 Tech Stack
- Python (Pandas, NumPy, hmmlearn, Matplotlib, scikit-learn)
- Jupyter Notebook
- Data APIs (from CryptoQuant, Glassnode, Coinglass)
- Git for version control

---

## 🔚 Conclusion
We demonstrate that combining **volatility-based features** with **HMM market regime modeling** can produce actionable and interpretable trading signals. Our Signal Score framework captures implicit market behavior and supports quantitative strategies with measurable performance.

