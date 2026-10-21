# audit grid eval source

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_grid_eval_source_20260515T165250_result.json`
- **Structured JSON:** [`a507b7534dfb8a1d2251.json`](../../sessions/a5/a507b7534dfb8a1d2251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**审计结果：所有 18 组 grid_b 实验的 eval_ppl_holdout 均来自 eval_perplexity.py post-hoc eval，无需重跑。**

关键发现：
- 所有 grid 训练均未包含 `--eval_data_path`，无 inline eval
- `output/eval_results/` 下 18 个 eval JSON 文件格式统一（4077068 tokens, stride=1024, max_docs=5000, fp16），时间戳集中在 5月14-15日
- 抽查 13 组的 registry 数值与 eval 文件完全匹配
- `output/eval/` 下有少量早期 eval 痕迹（5004058 tokens），已被后续统一重跑覆盖，不影响当前 registry 值

报告已写入 `artifacts/grid_eval_source_audit.md`。

---
