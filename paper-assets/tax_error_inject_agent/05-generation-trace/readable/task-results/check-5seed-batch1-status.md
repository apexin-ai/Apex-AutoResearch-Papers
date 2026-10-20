# check 5seed batch1 status

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_5seed-batch1-status_20260515T134602_result.json`
- **Structured JSON:** [`84ea47edbab6677dd40a.json`](../../sessions/84/84ea47edbab6677dd40a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Batch 1 训练状态报告

### 进程状态：4/4 全部运行中

| 任务 | PID | GPU | 运行时间 | 当前步数 | 总步数 | 进度 | 最新 loss | 预计剩余 |
|------|-----|-----|---------|---------|--------|------|----------|---------|
| v4-vanilla-seed1 | 154589 | cuda:0 | 6h16m | 167/1635 | 1635 | 10% | 0.585 | ~53min |
| v4-vanilla-seed7 | 154666 | cuda:1 | 6h14m | 166/1635 | 1635 | 10% | 0.580 | ~53min |
| v4-taxei-seed1 | 154937 | cuda:2 | 6h11m | 183/3387 | 3387 | 5% | 0.591 | ~1h42min |
| v4-taxei-seed7 | 155145 | cuda:3 | 6h08m | 180/3387 | 3387 | 5% | 0.591 | ~1h41min |

### GPU 占用

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 18,399 MiB | 94% |
| cuda:1 | 18,399 MiB | 95% |
| cuda:2 | 19,537 MiB | 91% |
| cuda:3 | 19,537 MiB | 93% |

### 训练细节
- 进程已运行 ~6h，但训练实际只跑了 ~6min（前 ~5h54m 为模型加载/数据预处理）
- 训练速度: vanilla ~2.14s/step, taxei ~1.92s/step
- **尚无 checkpoint**（save_strategy=epoch，epoch 1 未完成）
- TaxEI 数据集约为 Vanilla 的 2 倍（3387 vs 1635 总步数）

### Recovery Eval 文件（seed0 & seed123）
已存在 4 个文件：
- `v4_taxei_recovery_eval_s0.json` (562KB)
- `v4_taxei_recovery_eval_s123.json` (467KB)
- `v4_vanilla_recovery_eval_s0.json` (477KB)
- `v4_vanilla_recovery_eval_s123.json` (460KB)

### Random seed1/7 训练
**不存在。** `mini_random_sft_v4_seed1/` 和 `mini_random_sft_v4_seed7/` 目录均未创建，需要后续提交。

### 预计完成时间
- **Vanilla (seed1 & seed7)**: ~1h 后完成
- **TaxEI (seed1 & seed7)**: ~1h45min 后完成

---
