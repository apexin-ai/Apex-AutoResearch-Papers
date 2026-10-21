# ops check status westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_status_westb_20260516T091238_result.json`
- **Structured JSON:** [`0961dd72eac3f3db18f4.json`](../../sessions/09/0961dd72eac3f3db18f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

| 实验 | 状态 | 进度 | 当前 Accuracy |
|------|------|------|---------------|
| **eval_sft_rasp_25** (cuda:0) | 🟡 运行中 | 103/1319 (~8%) | 0.53 @100样本 |
| **eval_sft_standard_25** (cuda:1) | 🟡 运行中 | 550/1319 (~42%) | 0.5382 @550样本 |
| **eval_postprune_standard_25** (cuda:1) | ❌ 未启动 | — | — |

### 详情

**GPU 使用**:
- cuda:0: RTX PRO 6000, 28.9GB/97.9GB, 99% util, PID 602990 (eval_sft_rasp_25, 启动于 16:23)
- cuda:1: RTX PRO 6000, 28.5GB/97.9GB, 100% util, PID 598084 (eval_sft_standard_25, 启动于 15:05)

**进度估算**:
- eval_sft_standard_25: 已跑约 2h，平均 ~2-3s/it（含偶发长 generation），预计再需 ~3-4h 完成
- eval_sft_rasp_25: 已跑 ~50min，速度类似但有更多长 generation stall，预计需 ~8-10h 完成

**eval_postprune_standard_25**: 未找到任何相关进程或结果文件。cuda:1 目前被 sft_standard_25 占用，需等其完成后才能启动。

**磁盘**: 根分区 30G 用了 8.6G，剩余 22G，状态正常。

**结果文件输出路径**注意：实际输出到 `/root/autodl-tmp/recovery_aware_struct_prune/results/`，而非 `/root/recovery_aware_struct_prune/results/`。

---
