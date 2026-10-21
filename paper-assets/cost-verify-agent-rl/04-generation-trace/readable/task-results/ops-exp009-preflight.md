# ops exp009 preflight

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp009_preflight_20260514T033649_result.json`
- **Structured JSON:** [`e6107a3432569750172a.json`](../../sessions/e6/e6107a3432569750172a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp009 启动前检查报告

| 检查项 | 结果 | 状态 |
|--------|------|------|
| **1. 清理 checkpoint-150** | 已删除，剩余: checkpoint-75, checkpoint-225, final | ✅ |
| **2. SFT checkpoint 精度** | 全部 `torch.bfloat16` | ✅ |
| **3a. save_freq** | `save_freq: 5` | ✅ |
| **3b. model_path** | `model_path: /root/autodl-tmp/checkpoints/exp008_sft/final` | ✅ |
| **3c. RAY_TMPDIR** | `export RAY_TMPDIR=/root/autodl-tmp/ray_tmp` (在 .bashrc 中) | ✅ |
| **4. eval 进程** | **PID 193931 仍在运行** (`eval_sft_model.py`，占用 cuda:1, 33065MiB) | ❌ |
| **5. GPU 状态** | cuda:0 空闲 (0MiB, 0%) / cuda:1 被占用 (33065MiB, 56%) | ❌ |
| **6. 磁盘** | 30G 总量, 7.6G 已用, 23G 可用 (26%) | ✅ |

### 结论：**不能安全启动 exp009**

cuda:1 上 `eval_sft_model.py` (PID 193931) 仍在运行。需要先 kill 该进程释放 GPU 才能启动 GRPO。

是否 kill PID 193931？

---
