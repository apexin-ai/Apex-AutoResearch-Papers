# ops sync eval and verify 4way

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_eval_and_verify_4way_20260519T110356_result.json`
- **Structured JSON:** [`8cbf17b68fdce5a69415.json`](../../sessions/8c/8cbf17b68fdce5a69415.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成，汇总：

**eval 脚本同步** — 远程 `eval_phase2_gar.py` 已更新，语法 OK，`compute_conversation_ppl` 和 `avg_ppl` 字段均存在。

**四路 eval 脚本** (`run_4way_eval.sh`) — 8 个 eval 配置（4 条件 × 2 GAR variant），已使用 `--conversations-path ultrachat_eval_sample.json`，路径正确。

**Checkpoint 路径验证**:
- TG v7: `lora/` ✓, `gate_params.pt` (3.4MB) ✓
- UG: `lora/` ✓, `gate_params.pt` (3.4MB) ✓
- eval 数据: `ultrachat_eval_sample.json` (447KB) ✓
- LoRA-only: 训练中，跳过路径验证

**LoRA-only 训练进度**: Step 7750, L_NTP≈1.0, Gate=1.0 (符合 gate-type=none 预期)。GPU 利用率 99%，显存 91.3GB，训练正常进行中。

---
