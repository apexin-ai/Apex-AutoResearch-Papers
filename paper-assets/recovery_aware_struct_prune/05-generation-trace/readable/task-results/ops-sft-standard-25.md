# ops sft standard 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sft-standard-25_20260516T051939_result.json`
- **Structured JSON:** [`3da03fc739e026d33055.json`](../../sessions/3d/3da03fc739e026d33055.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活，GPU 已分配 13GB 显存。模型加载 + 数据集准备中，这对 7B 模型正常需要 1-2 分钟。

**训练已成功启动：**

| 项目 | 值 |
|------|-----|
| exp_id | sft_standard_25 |
| PID | 587865 |
| 服务器 | westb-23072, cuda:1 |
| 模型 | pruned_standard_25 (Standard 25% sparsity) |
| 输出 | /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 |
| 日志 | ~/runs/recovery_aware_struct_prune/sft_standard_25.log |

**训练参数**（与 20% SFT 完全一致）：
- epochs: 2, lr: 2e-5, batch_size: 1, grad_accum: 8
- max_seq_length: 2048, seed: 42
- 数据：GSM8K train (7473 samples)
- total_steps: 7473/8 × 2 = 1868 steps

**预估时间**：参考 20% SFT (~33 min for 1870 steps)，25% 模型更小，预计 **25-30 分钟**完成。

---
