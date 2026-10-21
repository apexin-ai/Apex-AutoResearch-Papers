# Re-Repair Downstream Experiment Design

## Objective

Demonstrate that CLS per-test diagnostic granularity (Claim 2) has practical downstream value: providing predicted per-test pass/fail information to a repair LLM improves patch repair success rate compared to a no-diagnostic baseline.

## Experimental Setup

### Data Source

**Population**: SWE-bench Verified instances with T_f2p ≥ 2 (≥2 FAIL_TO_PASS tests).
- Total SWE-bench Verified: 500 instances
- T≥2 subset: ~155 instances (31.3%)
- Rationale: With T=1, per-test info degenerates to "the patch failed" — no diagnostic gain.

**Incorrect Patches** (repair targets):

| Source | Method | Expected yield |
|--------|--------|---------------|
| Public agent predictions | SWE-bench leaderboard `.jsonl` files (SWE-agent, AutoCodeRover, Moatless, OpenHands, Agentless) | ~3-8 incorrect patches/instance |
| Synthetic mutations | Gold patch + operator_swap/off_by_one/boundary_removal | 3-4 per instance |
| LLM-generated | Qwen3-8B zero-shot repair (intentionally weak) | 1-2 per instance |

Target: ≥5 incorrect patches per T≥2 instance → ≥775 (instance, incorrect_patch) pairs.

Filter: only patches that fail at least 1 but not all F2P tests (partial failures are most informative for diagnostic guidance). Patches that fail ALL tests provide no diagnostic signal either.

### Conditions (3 + 1 oracle)

| Condition | Prompt content | Purpose |
|-----------|---------------|---------|
| **control** | "This patch does not fully resolve the issue. Please fix it." + patch + problem statement | Baseline: no diagnostic info |
| **cls-diag** | Control + "The patch fails the following tests: {CLS-predicted FAIL test names}" | Treatment: CLS-predicted diagnostics |
| **oracle-diag** | Control + "The patch fails the following tests: {ground-truth FAIL test names}" | Upper bound: perfect diagnostics |
| **random-diag** | Control + "The patch fails the following tests: {random subset of test names}" | Noise control: is ANY test-name info helpful regardless of accuracy? |

**Single variable**: only the diagnostic section of the prompt differs across conditions. Everything else (problem description, patch, system prompt, LLM, decoding params) is identical.

### CLS Model

Use the trained CLS 8B model (seed42, ckpt-3600, test accuracy 84.48%).

For each (incorrect_patch, test_i):
- Input: patch diff + modified file context + test code
- Output: predicted pass/fail

CLS predictions are generated once and cached. All conditions use the same CLS predictions (treatment uses them in the prompt; oracle ignores them).

### Repair LLM

**Primary**: Qwen3-8B-Instruct via vLLM on 4×5090
- Fits in single GPU (16-bit) or 2 GPUs
- ~1-2 samples/sec with 4K context
- Temperature 0.6, top_p 0.95, max_tokens 2048

**Optional API**: Claude Sonnet 4 / GPT-4o for comparison (higher ceiling, shows if diagnostic value scales with repair model capability).

**Sampling**: K=10 completions per (instance, patch, condition) for pass@1 and pass@5 computation.

### Verification

Ground-truth Docker execution via SWE-bench harness:
- Apply generated repair patch to the repo
- Run full test suite (F2P + P2P)
- Record per-test pass/fail
- Instance resolved = all F2P tests pass AND no P2P regressions

## Prompt Template

```
System: You are a software engineer. You are given a code patch that was intended
to fix an issue but does not fully work. Your task is to produce a corrected patch.

User:
## Issue Description
{problem_statement}

## Current (Incorrect) Patch
{incorrect_patch_diff}

## Relevant Source Files
{modified_file_contents}

{DIAGNOSTIC_SECTION}

Please produce a corrected patch in unified diff format that resolves the issue.
Output ONLY the diff, enclosed in ```diff ... ``` tags.
```

Where `DIAGNOSTIC_SECTION` varies by condition:

- **control**: *(empty)*
- **cls-diag**: `## Test Diagnostic\nThe current patch fails the following tests:\n{bullet list of CLS-predicted FAIL test names}\nThe following tests pass correctly:\n{bullet list of CLS-predicted PASS test names}`
- **oracle-diag**: Same format, ground-truth test results
- **random-diag**: Same format, random assignment

## Metrics

### Primary

| Metric | Definition |
|--------|-----------|
| **Resolve rate (pass@1)** | Fraction of (instance, patch) pairs where the best-of-1 repair resolves the instance |
| **Resolve rate (pass@5)** | Fraction where at least 1 of 5 repairs resolves |
| **Δ resolve rate** | cls-diag − control (primary effect size) |

### Secondary

| Metric | Definition |
|--------|-----------|
| **Per-test fix rate** | Of the originally-failing tests, what fraction now pass after repair? |
| **Regression rate** | Fraction of P2P tests that regress (pass→fail) after repair |
| **Oracle gap** | oracle-diag − cls-diag (how much room for CLS improvement) |
| **Noise gap** | random-diag − control (is test name info helpful even if random?) |

### Stratification Analyses

1. **By CLS accuracy on that instance**: Split instances into CLS-accurate (≥90% per-test correct) vs CLS-inaccurate (<90%). Does accurate CLS help more?
2. **By T (number of F2P tests)**: T=2, T=3-5, T≥6. Does diagnostic value increase with T?
3. **By partial-fail pattern**: How many F2P tests does the incorrect patch pass? More partial = more diagnostic signal.
4. **CLS error mode analysis**: When CLS misguides (wrong per-test prediction), does repair degrade below control?

## Statistical Analysis

### Sample Size & Power

- ~155 T≥2 instances × ~5 patches = ~775 paired observations
- Paired comparison: same (instance, patch) under different conditions
- McNemar's test for paired binary outcomes (resolved/not)
- With n=775 pairs, power ≥0.80 for detecting Δ=5pp resolve rate difference (α=0.05)
- Bootstrap confidence intervals (10000 resamples, instance-clustered) for all metrics

### Significance Testing

```python
# Primary: McNemar's test
# H0: P(cls-diag resolves & control doesn't) = P(control resolves & cls-diag doesn't)
from statsmodels.stats.contingency_tables import mcnemar
# result = mcnemar(table, exact=True)

# Secondary: Clustered bootstrap CI
# Cluster by instance_id (patches within same instance are correlated)
# 10000 bootstrap resamples, report 95% CI for Δ resolve rate
```

## Handling CLS Prediction Errors

CLS accuracy is ~84%, meaning ~16% of per-test predictions are wrong. This creates two failure modes:

1. **False FAIL (CLS says fail, actually passes)**: Repair LLM may "fix" something that wasn't broken → introduce regression
2. **Missed FAIL (CLS says pass, actually fails)**: Repair LLM won't know about this failing test → won't fix it

**Analysis plan**:
- Compute CLS confusion matrix on the exact test subset used in re-repair
- Correlate CLS precision/recall on each instance with repair success
- If cls-diag < control on instances where CLS accuracy < X%, report the accuracy threshold

**Robustness check**: Vary CLS prediction quality by injecting noise into oracle predictions (flip X% of labels) and measure repair success curve as function of diagnostic accuracy. This traces the accuracy-utility frontier.

## Compute Budget

| Phase | GPU hours | Wall-clock (4×5090) | Notes |
|-------|-----------|-------------------|-------|
| CLS inference | 4h | 1h | 775 patches × ~10 tests × 0.1s/sample |
| Repair generation | 80h | 20h | 775 × 4 conditions × 10 samples × ~2.5s |
| Docker verification | 0 (CPU) | 48-96h (4 parallel) | ~31K repairs × ~5 min/verification |
| **Total** | ~84h GPU | ~70-120h wall | Docker is bottleneck |

Optimization: run verification only on unique patches (many K=10 samples will be identical or near-identical after dedup).

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| CLS predictions hurt repair (cls-diag < control) | Oracle condition proves diagnostic value exists; report CLS accuracy threshold |
| Insufficient incorrect patches | Fall back to synthetic mutations; lower threshold to T≥1 for sample size |
| Repair LLM too weak (resolve rate ~0% across all conditions) | Switch to stronger API model; reduce problem difficulty to recent/simpler instances |
| Docker verification too slow | Subsample: run 50 instances for quick signal, full 155 if positive |
| Repair patches unparseable (not valid diffs) | Structured output enforcement; regex extraction; retry once |

## Implementation Phases

### Phase 0: Quick Feasibility (Day 1, ~4h)
- Select 10 T≥2 instances
- Collect 3 incorrect patches each (from public predictions)
- Run CLS + control/cls-diag repair on 30 pairs
- Verify via Docker
- **Go/no-go**: if resolve rate is >0 in at least one condition, proceed

### Phase 1: Data Preparation (Day 2-3)
- Download public agent predictions for SWE-bench Verified
- Filter to T≥2 instances, select incorrect patches
- Run CLS model on all (patch, test) pairs
- Run Docker to get ground-truth per-test results
- Build repair prompt dataset

### Phase 2: Repair Generation (Day 4-5)
- Deploy Qwen3-8B on vLLM
- Generate repairs for all 4 conditions × K=10
- Parse and dedup generated patches

### Phase 3: Verification (Day 5-8)
- Docker execution of all unique repair patches
- Compute resolve rates

### Phase 4: Analysis (Day 9)
- Statistical tests
- Stratification analyses
- Generate paper figures
- Write results section

## Output Artifacts

| Artifact | Path | Format |
|----------|------|--------|
| CLS per-test predictions | `artifacts/re_repair/cls_predictions.jsonl` | JSONL |
| Repair prompts | `artifacts/re_repair/repair_prompts.jsonl` | JSONL |
| Generated repairs | `artifacts/re_repair/generated_repairs.jsonl` | JSONL |
| Verification results | `artifacts/re_repair/verification_results.jsonl` | JSONL |
| Summary metrics | `artifacts/re_repair/metrics_summary.json` | JSON |
| Paper figure (resolve rate bar chart) | `artifacts/re_repair/fig_resolve_rate.pdf` | PDF |
