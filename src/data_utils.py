
from pathlib import Path
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame with basic validation."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"CSV not found: {p}")
    df = pd.read_csv(p)
    if df.empty:
        raise ValueError("Loaded DataFrame is empty.")
    return df
