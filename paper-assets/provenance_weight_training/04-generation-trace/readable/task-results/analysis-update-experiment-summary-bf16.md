# analysis update experiment summary bf16

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_update_experiment_summary_bf16_20260515T100302_result.json`
- **Structured JSON:** [`c613730ad31b9a050f57.json`](../../sessions/c6/c613730ad31b9a050f57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。主要变更：

- **Table 1** 重命名为 "Full Record"，填入 seed456 b=2.0/3.0/5.0 的 PPL 值并标注 †，添加 Seeds 列，Mean/Std 仅用 seed42+seed123 计算（与之前一致），脚注说明 fp32→bf16 偏差
- **Table 1a** 新增 "Paper View"，只展示用于论文的 mean±std 和 seed 数
- **Source Experiment IDs** 三个 seed456 实验状态改为 DONE，conclusion 标注 checkpoint resume artifact
- Table 2/3/4 不受影响，保持不变

---
