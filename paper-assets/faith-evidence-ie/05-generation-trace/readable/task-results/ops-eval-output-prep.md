# ops eval output prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-output-prep_20260514T220250_result.json`
- **Structured JSON:** [`c98ec2ed435f875258e8.json`](../../sessions/c9/c98ec2ed435f875258e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

### Eval 输出格式

**两种入口**：
- `freige.eval.batch_eval` — GRPO checkpoint eval，内部调 inference.py，需 `--sft_adapter` merge SFT
- `freige.eval.inference` — 直接 eval（SFT baseline 用这个）

**输出文件**：每个 checkpoint 目录下 `metrics.json`（~1.3KB 全部指标）+ `predictions.json`（~4-8MB 逐文档详情）。batch_eval 额外在顶层写 `summary.json`（f1/ign_f1/evi_f1/edcr/format_ok_rate）。

**关键指标字段**：`f1`, `ign_f1`, `evi_f1`, `edcr`, `format_ok_rate`, `pred_count`, `n_truncated`

### 当前状态

- 4 个 eval 正在运行（ckpt-20/40/rp_ckpt20/sft_baseline），输出目录已创建但为空
- 无 sentinel/W&B 输出，判断完成的唯一方式：检查 `metrics.json` 是否存在且非空
- 预计每个 eval 耗时 85-110 分钟

### SFT baseline 确认

sft_eval_r3_results 与 sft_eval_results 数值完全一致：F1=0.4057, Evi-F1=0.7979, EDCR=0.7118。handoff 中的数字来源已确认。

---
