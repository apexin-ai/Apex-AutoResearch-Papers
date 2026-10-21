# check qwen25 7b selfref 001 progress

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen25_7b_selfref_001_progress_20260522T151718_result.json`
- **Structured JSON:** [`3a6c936a2183e68405b3.json`](../../sessions/3a/3a6c936a2183e68405b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## qwen25_7b_selfref_001 训练进度

| 项目 | 状态 |
|------|------|
| **当前 Phase** | Phase 3.1a — LoRA finetune d0 |
| **数据生成** | depth_0: 5000/5000 ✓ · depth_1~3: 未开始 |
| **LoRA 训练 d0** | 59/939 steps (6.3%) |
| **Checkpoint** | `lora_depth_0/` 目录已创建，尚无文件 |
| **GPU** | 利用率 100%, 显存 20.2GB / 95.6GB |
| **进程** | grep 未匹配（进程名可能不含关键词），但日志在持续写入、GPU 满载，训练在跑 |

**速度**: ~1.33s/step，剩余 880 steps ≈ **19 分钟**完成 d0 finetune。

**整体进度**: 实验共 4 个 depth（每个 depth = 生成数据 + LoRA finetune），当前在 d0 finetune 阶段。粗估整体完成约 **15-20%**，预计总剩余时间 **2-3 小时**（取决于后续 depth 的生成速度）。

---
