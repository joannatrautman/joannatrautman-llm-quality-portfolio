"""
Prompt Evaluation (Demo)
Run: python prompt_evaluation.py
Creates: scored_responses.csv, summary_metrics.csv
"""
import pandas as pd, json, pathlib

base = pathlib.Path(__file__).parent
prompts = pd.read_csv(base / "sample_prompts.csv")
rubric = json.loads((base / "rubric.json").read_text())

# Simulate two response variants per prompt (replace with API responses in production)
rows = []
for _, row in prompts.iterrows():
    p = row["prompt"]
    rows.append({
        "prompt": p, "topic": row["topic"], "grade_level": row["grade_level"],
        "variant": "A",
        "response": "Concise, age-appropriate explanation with a simple example.",
        "accuracy": 5, "clarity": 5, "tone": 5, "instructional_alignment": 5
    })
    rows.append({
        "prompt": p, "topic": row["topic"], "grade_level": row["grade_level"],
        "variant": "B",
        "response": "Verbose explanation with some jargon; still mostly correct.",
        "accuracy": 4, "clarity": 3, "tone": 4, "instructional_alignment": 4
    })

df = pd.DataFrame(rows)
df["avg_score"] = df[["accuracy","clarity","tone","instructional_alignment"]].mean(axis=1)

# Aggregate summary (variant-level metrics)
summary = df.groupby(["variant"]).agg(
    avg_accuracy=("accuracy","mean"),
    avg_clarity=("clarity","mean"),
    avg_tone=("tone","mean"),
    avg_alignment=("instructional_alignment","mean"),
    n=("prompt","count")
).reset_index()

# Save for dashboards
df.to_csv(base / "scored_responses.csv", index=False)
summary.to_csv(base / "summary_metrics.csv", index=False)

print("Exported: scored_responses.csv, summary_metrics.csv")
print(summary)
