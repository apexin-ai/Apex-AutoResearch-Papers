# code threshold q07 script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_threshold_q07_script_20260516T054958_result.json`
- **Structured JSON:** [`ca91cf593cf51f280a35.json`](../../sessions/ca/ca91cf593cf51f280a35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出：**
- 过滤数据：`data/scored_data_filtered_q07.jsonl` — **184,908 样本**（原始 371,499 的 49.8%，过滤掉 50.2% contamination_score > 0.7 的样本）
- 脚本：`scripts/run_threshold_q07_seed42.sh` — 已写入并 chmod +x
- Dry-run：2 step 成功，参数解析、数据加载、前向传播均正常

**预计训练时长：** 200M tokens / (batch_size 4 × grad_accum 4 × max_length 2048) ≈ 6,104 steps。参考 q03 同配置，预计 ~4-5 小时（4 卡空闲时）。当前 4 卡被 q03 训练占用，需等其结束后启动。

---
