# ops bjb1 fix symlink and resubmit scienceworld

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_fix_symlink_and_resubmit_scienceworld_20260522T040821_result.json`
- **Structured JSON:** [`22d988f9b0f7d03198bc.json`](../../sessions/22/22d988f9b0f7d03198bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，正在加载模型 checkpoint。

### 产出汇总

| 项目 | 结果 |
|------|------|
| **Symlink** | `qwen3_scienceworld_sft -> scienceworld_sft` 创建成功 |
| **Config 更新** | `model_path` 已改为 `/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface` |
| **Dry-run** | 路径验证通过（12 files, safetensors OK, qwen in path OK） |
| **PID** | 386364（tmux session: `scienceworld_grpo_cell_c_v4`） |
| **启动日志** | Ray TaskRunner 启动正常，tokenizer 加载中，checkpoint shards 2/2 已加载。有 Mistral regex warning（无害） |
| **GPU 占用** | GPU 0: 1369 MiB, GPU 1: 1369 MiB（模型加载中，后续会增长） |

---
