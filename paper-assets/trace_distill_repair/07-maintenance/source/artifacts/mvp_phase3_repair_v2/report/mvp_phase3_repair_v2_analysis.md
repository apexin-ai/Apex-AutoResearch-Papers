# MVP Phase 3 Repair v2 — Experiment Analysis

## Experiment Summary

| Field | Value |
|-------|-------|
| exp_id | mvp_phase3_repair_v2 |
| Model | deepseek/deepseek-v4-pro |
| Server | rtx6000-diagprobe |
| Start | 2026-05-15 21:05 |
| End (last log write) | 2026-05-15 23:20 |
| Duration | ~2h15m |
| Target instances | 14 (Tier 1 clean subset) |
| Completed instances | **9/14** (process terminated during scrapy_7 API call) |
| Conditions | no_trace, full_trace, structural_filtered, line_filtered |
| Primary metric | test_execution pass rate |

## Completion Status: 9/14 (INCOMPLETE)

Process terminated silently during the 10th instance (scrapy_7). The log ends at an API call with no error message, suggesting an unhandled timeout or OOM. Last checkpoint: 9/14.

Completed instances: black_1, cookiecutter_1, cookiecutter_2, cookiecutter_3, fastapi_2, httpie_2, luigi_5, sanic_2, scrapy_2

Missing (5): scrapy_7 and 4 others from the 14-instance list.

## Oracle Baseline

| Instance | Oracle Pass | Method |
|----------|------------|--------|
| black_1 | False | test_execution |
| fastapi_1 | N/A | instance not found |
| fastapi_2 | False | test_execution |
| httpie_2 | **True** | test_execution |

Oracle pass rate: **1/4 = 25%**. Only httpie_2 has a working test harness for the oracle (ground-truth) fix. This severely limits the validity of test_execution as an evaluation metric.

## Aggregate Results

| Condition | n | test_pass | pass_rate | diff_apply | apply_rate | judge_mean | avg_tok_in | avg_tok_out |
|-----------|---|-----------|-----------|------------|------------|------------|------------|-------------|
| no_trace | 9 | 0 | **0.0%** | 3 | 33.3% | 0.333 | 7,226 | 3,357 |
| full_trace | 9 | 1 | 11.1% | 4 | 44.4% | 0.444 | 13,849 | 2,853 |
| structural_filtered | 9 | 0 | **0.0%** | 4 | 44.4% | 0.444 | 7,737 | 4,790 |
| line_filtered | 9 | 0 | **0.0%** | 5 | 55.6% | 0.556 | 7,854 | 3,618 |

### Key observations
- **test_pass = 0% for no_trace AND structural_filtered** — the primary metric shows zero signal
- The only test pass in the entire experiment is scrapy_2/full_trace (1/36 = 2.8%)
- Judge scores are binary (0 or 1) with means in 0.33–0.56 range — extremely low
- diff_apply rate is only 33–56% — more than a third of generated patches can't even apply

## Head-to-Head Comparisons

### structural_filtered vs no_trace (by judge score)

| Instance | no_trace | structural | Result |
|----------|----------|------------|--------|
| black_1 | 1 | 0 | LOSS |
| cookiecutter_1 | 1 | 1 | TIE |
| cookiecutter_2 | 1 | 0 | LOSS |
| cookiecutter_3 | 0 | 0 | TIE |
| fastapi_2 | 0 | 1 | WIN |
| httpie_2 | 0 | 0 | TIE |
| luigi_5 | 0 | 0 | TIE |
| sanic_2 | 0 | 1 | WIN |
| scrapy_2 | 0 | 1 | WIN |
| **Total** | | | **W3/T4/L2** |

### structural_filtered vs no_trace (by test_pass)
- **W0/T9/L0** — completely uninformative, both 0% everywhere

### structural_filtered vs line_filtered (by judge score)
- **W1/T5/L3** — line_filtered slightly outperforms structural_filtered

### full_trace vs no_trace (by judge score)
- W3/T2/L4 — no clear advantage for full_trace either

## Per-Instance Detail

| Instance | Condition | test_pass | diff_apply | judge | tokens_in | tokens_out |
|----------|-----------|-----------|------------|-------|-----------|------------|
| black_1 | no_trace | False | True | 1 | 33,314 | 1,207 |
| black_1 | full_trace | False | False | 0 | 36,003 | 2,347 |
| black_1 | structural | False | False | 0 | 34,175 | 4,212 |
| black_1 | line | False | False | 1 | 33,546 | 3,484 |
| cookiecutter_1 | no_trace | False | False | 1 | 3,415 | 4,146 |
| cookiecutter_1 | full_trace | False | True | 0 | 5,859 | 3,428 |
| cookiecutter_1 | structural | False | True | 1 | 3,747 | 3,044 |
| cookiecutter_1 | line | False | True | 1 | 4,094 | 2,155 |
| cookiecutter_2 | no_trace | False | True | 1 | 1,194 | 977 |
| cookiecutter_2 | full_trace | False | True | 1 | 3,637 | 163 |
| cookiecutter_2 | structural | False | True | 0 | 1,522 | 5,267 |
| cookiecutter_2 | line | False | True | 0 | 1,772 | 3,711 |
| cookiecutter_3 | no_trace | False | False | 0 | 1,957 | 4,566 |
| cookiecutter_3 | full_trace | False | True | 1 | 2,978 | 1,309 |
| cookiecutter_3 | structural | False | False | 0 | 2,861 | 4,468 |
| cookiecutter_3 | line | False | False | 1 | 2,616 | 6,581 |
| fastapi_2 | no_trace | False | True | 0 | 8,903 | 2,215 |
| fastapi_2 | full_trace | False | False | 1 | 28,654 | 4,432 |
| fastapi_2 | structural | False | True | 1 | 9,126 | 2,931 |
| fastapi_2 | line | False | True | 0 | 10,615 | 4,812 |
| httpie_2 | no_trace | False | False | 0 | 2,709 | 2,241 |
| httpie_2 | full_trace | False | False | 1 | 4,845 | 1,702 |
| httpie_2 | structural | False | False | 0 | 2,709 | 4,972 |
| httpie_2 | line | False | True | 1 | 2,709 | 4,230 |
| luigi_5 | no_trace | False | False | 0 | 3,525 | 6,702 |
| luigi_5 | full_trace | False | False | 0 | 27,036 | 2,718 |
| luigi_5 | structural | False | False | 0 | 3,644 | 7,147 |
| luigi_5 | line | False | True | 0 | 4,500 | 1,801 |
| sanic_2 | no_trace | False | False | 0 | 7,480 | 2,350 |
| sanic_2 | full_trace | False | False | 0 | 9,063 | 3,823 |
| sanic_2 | structural | False | False | 1 | 8,621 | 4,604 |
| sanic_2 | line | False | False | 1 | 7,872 | 5,649 |
| scrapy_2 | no_trace | False | False | 0 | 2,541 | 5,805 |
| scrapy_2 | full_trace | **True** | True | 0 | 6,563 | 5,757 |
| scrapy_2 | structural | False | True | 1 | 3,225 | 6,464 |
| scrapy_2 | line | False | True | 1 | 2,966 | 143 |

## Token Usage Comparison

| Condition | avg_input_tokens | avg_output_tokens | avg_total |
|-----------|-----------------|-------------------|-----------|
| no_trace | 7,226 | 3,357 | 10,583 |
| full_trace | 13,849 | 2,853 | 16,702 |
| structural_filtered | 7,737 | 4,790 | 12,527 |
| line_filtered | 7,854 | 3,618 | 11,472 |

full_trace uses ~1.9x input tokens vs no_trace due to trace content. structural and line are comparable to no_trace in input but produce slightly longer output.

## v1 vs v2 Comparison

| Metric | v1 (invalidated) | v2 |
|--------|-------------------|-----|
| Instances completed | 3/14 | 9/14 |
| no_trace judge_mean | 1.06 | 0.333 |
| structural judge_mean | 0.76 | 0.444 |
| test_pass (any condition) | 0/12 | 1/36 |
| diff_apply rate | not recorded | 44.4% |
| Confounds | get_buggy_code fail, prompt degradation, output truncation | Oracle baseline failure (1/4), process incomplete |

### What v2 fixed from v1
- Correct buggy_code retrieval (was using wrong code in v1)
- Proper diff output format (was truncated in v1)
- max_tokens=8192 (was insufficient in v1)
- Expanded from 3 to 9 completed instances

### What v2 did NOT fix
- Judge scores are **worse** than v1 (0.33 vs 1.06 for no_trace) — likely because v1's inflated scores were artifacts of the confounded pipeline
- test_pass remains at ~0% — the fundamental task is too hard for deepseek-v4-pro on BugsInPy

## Confound / Data Quality Issues

1. **Incomplete run (9/14)**: Process terminated without summary. Results based on 9 instances only.
2. **Oracle baseline failure**: Only 1/4 oracle baselines pass test execution. This means test infra is broken for most instances — even the ground-truth fix can't pass tests. test_execution is not a reliable metric for these instances.
3. **Binary judge scores**: All judge scores are 0 or 1 (no intermediate values). This collapses the scale and reduces discriminative power. Could indicate judge prompt issues or genuinely terrible fixes.
4. **Low diff_apply rate (44.4%)**: The model frequently generates malformed patches. When diff doesn't apply, test_pass is automatically False and judge gets "parse_error" → score 0. This confounds the comparison.
5. **scrapy_2/full_trace anomaly**: The only test_pass=True in the entire experiment, but judge=0 ("parse_error"). The fix is structurally correct (adds `if self.limit is not None` guard) but the judge couldn't parse the output. This is a data quality issue.

## Kill Criteria C001 Evaluation

> 强模型消歧实验 kill criteria：
> (1) no_trace judge ≥ 3.0
> (2) structural > no_trace (p<0.15)
> (3) ≥1 条件 test pass > 0%
> 三条同时满足=PASS，否则 MVP FAIL。

| Criterion | Required | Actual | Status |
|-----------|----------|--------|--------|
| no_trace judge ≥ 3.0 | ≥ 3.0 | **0.333** | **FAIL** (scale issue: scores are 0-1 binary) |
| structural > no_trace (p<0.15) | p < 0.15 | W3/T4/L2, no significance | **FAIL** |
| ≥1 condition test pass > 0% | > 0% | full_trace: 11.1% | PASS (marginal) |
| **Combined** | All 3 PASS | 1/3 PASS | **MVP FAIL** |

## Conclusion: NEGATIVE

**The experiment produces a clear negative result.** Trace information (structural_filtered, line_filtered, or full_trace) does not meaningfully improve bug repair quality over the no_trace baseline when evaluated on BugsInPy with deepseek-v4-pro.

### Root causes of failure:
1. **The repair task itself is too hard**: deepseek-v4-pro generates low-quality patches regardless of trace input. Judge mean across all conditions is 0.42 (0–1 scale). The model cannot reliably produce valid diffs, let alone correct fixes.
2. **Test infrastructure is unreliable**: Oracle baseline pass rate of 25% means test_execution cannot differentiate conditions even if patches were correct.
3. **No trace signal**: Adding trace information does not help because the bottleneck is basic code generation quality, not diagnostic insight. The trace is potentially useful information given to a model that cannot use it.

### Implication per C001:
This was the "last disambiguation opportunity" per constraint C001. The kill criteria are not met. **The trace_distill_repair MVP should be declared FAILED.**
