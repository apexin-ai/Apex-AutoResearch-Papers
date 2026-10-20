# code prep hybrid posthoc eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_hybrid-posthoc-eval_20260516T155609_result.json`
- **Structured JSON:** [`16e2f3481b03d29d87b8.json`](../../sessions/16/16e2f3481b03d29d87b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**完成。** 两个脚本已就绪：

```
scripts/eval_hybrid_rho04_seed42.sh
scripts/eval_hybrid_rho06_seed42.sh
```

**验证结果**：
- `bash -n` 语法检查 ✓
- `data/human/eval_holdout.jsonl` 存在 (227MB) ✓
- `CUDA_VISIBLE_DEVICES` 默认 -1 ✓
- 训练进行中（当前两个实验都到了 checkpoint-2000），完成后会生成 `final/` 目录

**训练完成后执行**：
```bash
bash scripts/eval_hybrid_rho04_seed42.sh 2   # GPU 2
bash scripts/eval_hybrid_rho06_seed42.sh 3   # GPU 3
```

结果输出到 `output/eval_results/hybrid_rho0X_seed42_eval.json`。

---
