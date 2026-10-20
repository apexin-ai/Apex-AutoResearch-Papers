# infra gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260514T001704_result.json`
- **Structured JSON:** [`02f311fedf62270a12ad.json`](../../sessions/02/02f311fedf62270a12ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### GPU 全景

| GPU | VRAM | Util | 实验 | 状态 |
|-----|------|------|------|------|
| **0** | 22001/24564 MiB | 84% | exp_001_sft_d100_05B (PID 235248) | 训练中，54% (2238/4159 steps)，~37min 剩余 |
| **1** | 3667/24564 MiB | 33% | exp_001_eval_05B_d000_s42 (PID 229375) | 评估中，GSM8K 65% (860/1319) |
| **2** | 3667/24564 MiB | 32% | exp_001_eval_05B_d000_s123 (PID 229521) | 评估中，GSM8K 63% (825/1319) |
| **3** | 0/24564 MiB | 0% | — | **空闲** |
| **4** | 10365/24564 MiB | 44% | exp_001_eval_15B_d000_s42 (PID 221376) | 评估中，已运行 ~2h47min，无日志文件 |
| **5** | 22007/24564 MiB | 93% | exp_001_sft_d005_05B_v3 (PID 239734) | 训练中，35% (1123/3177 steps)，~38min 剩余 |

### exp_001_sft_0pct_3B_s123

**已完成** — EXIT_CODE=0，完成时间 2026-05-14T00:15:04Z

- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter/`
- train_loss: **1.131**
- mean_token_accuracy: **0.751**
- entropy: 1.103
- epoch: 1.0（完整 1 epoch）
- 训练时长: 12787s (~3.55h)

### 进程健康状态

| 进程 | PID | 状态 |
|------|-----|------|
| exp_001_sft_d100_05B | 235243→235248 | ✅ 运行中 |
| exp_001_sft_d005_05B_v3 | 239729→239734 | ✅ 运行中 |
| exp_001_eval_15B_d000_s42 | 221376 | ✅ 运行中（eval_results 目录为空，尚未输出结果） |
| exp_001_eval_05B_d000_s42 | 229370→229375 | ✅ 运行中（GSM8K 阶段，后续还有其他 benchmark） |
| exp_001_eval_05B_d000_s123 | 229516→229521 | ✅ 运行中（GSM8K 阶段，后续还有其他 benchmark） |
| exp_001_sft_0pct_3B_s123 | — | ✅ 已完成 |

**注意**: eval_15B_d000_s42 是直接启动的（非 run 管理系统），没有日志文件在 `~/runs/` 下，且 eval_results 目录仍为空。GPU 3 完全空闲可用。

---
