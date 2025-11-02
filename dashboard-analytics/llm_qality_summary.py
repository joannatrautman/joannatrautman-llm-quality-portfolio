"""
LLM Quality Summary (Demo)
Run AFTER prompt_evaluation.py
Usage: python llm_quality_summary.py
"""
import pandas as pd
from pathlib import Path

prompt_eval_dir = Path(__file__).parent.parent / "prompt-evaluation"
df = pd.read_csv(prompt_eval_dir / "scored_responses.csv")

summary = df.groupby(["variant"]).agg(
    avg_accuracy=("accuracy","mean"),
    avg_clarity=("clarity","mean"),
    avg_tone=("tone","mean"),
    avg_alignment=("instructional_alignment","mean"),
    n=("prompt","count")
).reset_index()

print(summary)

# Optional: quick plot (comment out if running headless)
try:
    import matplotlib.pyplot as plt
    summary.set_index("variant")[["avg_accuracy","avg_clarity","avg_tone","avg_alignment"]].plot(kind="bar", title="LLM Quality by Variant")
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("Plot skipped:", e)
