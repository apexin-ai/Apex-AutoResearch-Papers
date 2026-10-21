# diagnose cqa1 gpu012 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1-gpu012-status_20260525T195118_result.json`
- **Structured JSON:** [`2ae98ca2be9ebf1702bd.json`](../../sessions/2a/2ae98ca2be9ebf1702bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**服务器状态：cqa1-33015 → westd-27271**
- **只有 2 张 GPU**（不是 4 张），型号 NVIDIA RTX PRO 6000 Blackwell (98GB)
- **GPU0**: 运行 OpenVLA baseline eval（libero_goal, seed43），已跑 1h39m
- **GPU1**: 运行 OpenVLA random_prune k=0.9 eval（libero_goal, seed43），已跑 1h39m
- **两张 GPU 都在占用中**，无法提交新实验

**脚本兼容性问题：**
- `eval_pi05_pruning_libero.py` 的 `--prune_mode` 只支持 3 种：`none`、`random`、`l2norm`
- 任务要求的 `zero_mask_random` 和 `zero_mask_l2norm` 模式**不存在**，需要先扩展脚本才能提交实验 A 和 C

**结论：3 个实验都无法提交。**
1. GPU 全部被 OpenVLA eval 占用，没有空闲 GPU
2. 脚本不支持 `zero_mask_random` / `zero_mask_l2norm` 两种 prune mode（实验 A、C），只有实验 B（l2norm k=0.925）的模式是现有支持的
3. 即使模式支持，也没有可用 GPU

需要等当前 OpenVLA 实验跑完（或确认是否可以在其他服务器提交），以及决定是否扩展脚本支持 zero_mask 系列模式。

---
