import pandas as pd


def main() -> None:
    df = pd.read_csv("DJGT_raw.csv")

    if "PERMNO" in df.columns:
        df = df.drop(columns=["PERMNO"])

    if "date" in df.columns:
        df = df.rename(columns={"date": "DATE"})

    df_pivot = df.pivot(index="DATE", columns="TICKER", values="PRC")
    df_pivot.to_csv("DJGT_prices.csv")


if __name__ == "__main__":
    main()