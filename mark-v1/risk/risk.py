import polars as pl
import yfinance as yf
import jax.numpy as jnp

def calc_volatility_beta(ticker, market_symbol, start_date, end_date):
    # Download adjusted close prices
    stock_data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)['Adj Close']
    market_data = yf.download(market_symbol, start=start_date, end=end_date, auto_adjust=False)['Adj Close']

    # Create Polars DataFrames with consistent column names
    stock_df = pl.DataFrame({
        'Date': stock_data.index,
        'Stock': stock_data.values
    })
    market_df = pl.DataFrame({
        'Date': market_data.index,
        'Market': market_data.values
    })

    # Join DataFrames on 'Date'
    df = stock_df.join(market_df, on='Date', how='inner')

    # Calculate daily returns
    df = df.with_columns([
        (pl.col('Stock') / pl.col('Stock').shift(1)).log().alias('Stock_Returns'),
        (pl.col('Market') / pl.col('Market').shift(1)).log().alias('Market_Returns')
    ]).drop_nulls()

    # Convert returns to JAX arrays
    stock_returns = jnp.array(df['Stock_Returns'].to_numpy())
    market_returns = jnp.array(df['Market_Returns'].to_numpy())

    # Calculate annualized volatility
    volatility = jnp.std(stock_returns) * jnp.sqrt(252)

    # Calculate beta
    covariance_matrix = jnp.cov(jnp.stack([stock_returns, market_returns]))
    covariance = covariance_matrix[0, 1]
    market_variance = jnp.var(market_returns)
    beta = covariance / market_variance

    return {'Volatility': float(volatility), 'Beta': float(beta)}

# Example usage
result = calc_volatility_beta('AAPL', '^GSPC', '2022-01-01', '2023-01-01')
print(f"Annualized Volatility: {result['Volatility']:.2%}")
print(f"Beta: {result['Beta']:.4f}")
