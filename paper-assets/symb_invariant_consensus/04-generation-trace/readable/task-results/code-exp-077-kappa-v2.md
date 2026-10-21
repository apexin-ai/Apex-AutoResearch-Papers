# code exp 077 kappa v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-077-kappa-v2_20260519T181014_result.json`
- **Structured JSON:** [`5fde6533d97727246a58.json`](../../sessions/5f/5fde6533d97727246a58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 3 题成功完成，无 crash。输出 JSON 格式正确。

结果摘要：
- 代码已部署到 `/root/symb_invariant_consensus/run_kappa_generalization.py`
- `--help` 参数验证通过
- 3 题 dry-run 完成（3.8 min），输出格式正确
- SC 的 n_questions=2（folio_2 不在 SC limit=3 的排序中，正式全量运行时 204 题不受影响）
- 3 题的 κ 值偏低是因为样本量太小，正式 204 题运行预计会更显著

正式运行命令：
```bash
python -u run_kappa_generalization.py \
  --mode vllm --api-base http://localhost:8002/v1 --model auto \
  --data data/folio_full.json \
  --sc-traces-dir results/exp033_mistral_7b_folio204 \
  --seed 42 \
  --output results/exp077_kappa_generalization/results.json \
  --save-intermediates
```

---
