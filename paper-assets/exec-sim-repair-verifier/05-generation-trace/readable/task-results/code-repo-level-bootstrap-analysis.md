# code repo level bootstrap analysis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repo-level-bootstrap-analysis_20260514T172708_result.json`
- **Structured JSON:** [`b13089426312a1dcd48e.json`](../../sessions/b1/b13089426312a1dcd48e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署到 westd `/home/sonny/exec-sim-repair-verifier/repo_level_bootstrap.py`，dry-run 通过。

用法示例（CWM eval 完成后）：
```bash
python repo_level_bootstrap.py \
  --cls_pred results/repo_cls_v5_conda_eval/eval_repo_cls_predictions.jsonl \
  --cwm_pred results/&lt;cwm_dir>/eval_repo_cls_predictions.jsonl \
  --output results/bootstrap_cls_vs_cwm.json
```

输出 JSON 包含：`cls_accuracy`, `cwm_accuracy`, `gap_pp`（百分点差）, `ci_lower_pp`, `ci_upper_pp`（95% CI）, `p_value`（单侧 H0: CLS ≤ CWM）, `n_samples`, `significant_at_005`。

---
