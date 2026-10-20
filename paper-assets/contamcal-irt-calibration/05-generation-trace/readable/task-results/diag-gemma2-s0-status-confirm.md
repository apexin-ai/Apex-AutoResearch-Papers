# diag gemma2 s0 status confirm

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2-s0-status-confirm_20260520T143159_result.json`
- **Structured JSON:** [`678063c1b7ffe607efa2.json`](../../sessions/67/678063c1b7ffe607efa2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemma-2 s0 Sweep 状态 (westd-29999, cuda:1)

**进程**: 存活。父 shell PID **314024**（非 314029），GPU 进程 PID **342346**。`CUDA_VISIBLE_DEVICES=1` 已显式设置。

**GPU 1**: 98% 利用率，94,877 / 97,887 MiB（97% 显存占用）

**当前训练**: **d005_s0**，step 2685/3177（**84%**），epoch 0.7555，已运行 ~2h05m，预计 ~24min 完成当前 dosage 训练

**LoRA 配置**: r=16, alpha=32, lr=5e-5（合规，非黑名单 alpha=16）

### Dosage 完成进度

| Dosage | TRAIN | EVAL | 备注 |
|--------|-------|------|------|
| d000_s0 | **DONE** | **DONE** | .done marker 存在，eval_results_v2 有 4 个结果文件 |
| d005_s0 | **84%** (进行中) | 待开始 | lora_adapter 子目录已创建 |
| d025_s0 | 未开始 | 未开始 | 空目录（预创建） |
| d050_s0 | 未开始 | 未开始 | 空目录（预创建） |
| d100_s0 | 未开始 | 未开始 | 目录不存在 |

**剩余时间估算**: 每个 dosage ~2.5h 训练 + ~12min eval。d005 剩余 ~24min，之后 d025/d050/d100 共需 ~8.2h。全部完成预计约 **明早 07:00 CST**。

---
