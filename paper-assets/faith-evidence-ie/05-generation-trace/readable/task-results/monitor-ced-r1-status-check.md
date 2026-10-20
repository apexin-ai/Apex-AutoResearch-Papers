# monitor ced r1 status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_ced-r1-status-check_20260514T095843_result.json`
- **Structured JSON:** [`899b4e4b80c4d705e740.json`](../../sessions/89/899b4e4b80c4d705e740.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练正在运行中 — step 56/189 (30%)**

| 指标 | Step 45 | Step 50 | Step 55 |
|------|---------|---------|---------|
| loss | 0.0258→0.2115 | 0.2971 | 0.2607 |
| format_reward | 0.927 | 0.623 | 0.617 |
| f1_reward | 0.042 | 0.030 | 0.012 |
| ced_reward | 0.645 | 0.426 | 0.467 |
| **total reward** | **1.613** | **1.079** | **1.096** |
| clipped_ratio | 0.078 | 0.416 | 0.403 |
| step_time | ~110s | ~124s | ~123s |

**GPU 状态**: 4 卡均有显存占用（17-24GB），GPU 0-1 利用率 100%，GPU 2-3 利用率 0%（DeepSpeed ZeRO offload 模式正常）。

**Checkpoint**: `/root/autodl-tmp/grpo_s3/` 目前为空，尚未保存 checkpoint。

**预计剩余时间**: 133 steps × ~123s/step ≈ **4.5 小时**，预计 ~22:30 完成。

**值得注意的趋势**: step 45 之后 format_reward 从 0.93 骤降至 0.62，clipped_ratio 从 0.08 飙升至 0.40+，说明大量生成被截断到 max_length，模型输出变冗长导致格式合规率和 CED reward 同步下滑。总 reward 从 1.61 降至 ~1.10。

---
