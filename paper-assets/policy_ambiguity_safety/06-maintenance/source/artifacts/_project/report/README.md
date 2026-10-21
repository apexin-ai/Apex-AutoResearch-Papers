# Policy Ambiguity Safety — Experiment Pipeline

Three-module pipeline: agent execution → LLM judge evaluation → statistical analysis.

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=[REDACTED]
export OPENAI_API_KEY=[REDACTED]
```

## Clauses JSON Format

Input `clauses.json` schema:

```json
[
  {
    "clause_id": "S01",
    "ambiguity_type": "scopal",
    "ambiguous_clause": "Every agent may approve two exceptions...",
    "unambiguous_clause": "Each agent may independently approve up to two...",
    "user_scenario": "I'd like to request an exception to the return window...",
    "tools": [],
    "stripped_tool_desc": []
  }
]
```

## Module 1: Agent Execution Harness

Runs LLM agents against each clause (ambiguous + unambiguous) and records trajectories.

```bash
python harness.py \
  --clauses clauses.json \
  --models claude-sonnet-4-5,gpt-5.4 \
  --output results/ \
  --concurrency 10 \
  --resume
```

Output: `results/episodes.jsonl` — one JSON line per episode with full trajectory.

## Module 2: LLM-as-Judge Evaluation

Evaluates each episode for policy violations against the ground-truth (unambiguous) clause.

```bash
python judge.py \
  --results results/ \
  --clauses clauses.json \
  --output judgments/ \
  --judge-model claude-sonnet-4-5 \
  --concurrency 5
```

Output: `judgments/judgments.jsonl` — violation level (critical/moderate/minor/none) per episode.

Includes automatic bias check: warns if scopal violation rate is lower than expected (H1 predicts highest).

## Module 3: Statistical Analysis

Dual-track analysis with automatic pass/fail judgment.

```bash
python analyze.py \
  --judgments judgments/ \
  --clauses clauses.json \
  --output analysis/ \
  --alpha 0.05 \
  --min-v 0.20
```

**Primary analysis** — ambiguous-only cross-type comparison:
- χ² omnibus test (3 ambiguity types × violation levels)
- Pairwise Fisher exact tests + Bonferroni correction
- Cramér's V effect size per pair

**Secondary analysis** — matched-pair within-type:
- McNemar test (ambiguous vs unambiguous, paired binary)
- Wilcoxon signed-rank (paired ordinal)

**Pass criterion**: omnibus p < α AND at least one pairwise Cramér's V ≥ min_v.

Output files:
- `analysis/results_summary.csv` — per-clause violation rates
- `analysis/statistics_report.json` — all test statistics
- `analysis/pass_fail_judgment.json` — PASS/FAIL + reasons
