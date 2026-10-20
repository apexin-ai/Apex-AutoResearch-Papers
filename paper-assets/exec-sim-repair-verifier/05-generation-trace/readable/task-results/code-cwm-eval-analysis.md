# code cwm eval analysis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm-eval-analysis_20260514T151900_result.json`
- **Structured JSON:** [`7ceb6ce80f0a36e922eb.json`](../../sessions/7c/7ceb6ce80f0a36e922eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

majority baseline 现在是 72.96%，与 eval_repo_cwm.json 一致。

脚本已就绪：
- **`/home/sonny/exec-sim-repair-verifier/analyze_cwm_eval.py`** 已部署到 home 服务器
- 本地副本在 `projects/exec-sim-repair-verifier/analyze_cwm_eval.py`
- 用 CWM v10 (9784 samples) 验证通过，metrics 与 eval_repo_cwm.json 完全匹配

CWM v12 / seed123 eval 完成后的用法：
```bash
python3 analyze_cwm_eval.py \
  --predictions_path /root/autodl-tmp/results/repo_cwm_v12_conda_eval/eval_repo_cwm_predictions.jsonl \
  --output_path /root/autodl-tmp/results/repo_cwm_v12_conda_eval/cwm_analysis.json
```

---
