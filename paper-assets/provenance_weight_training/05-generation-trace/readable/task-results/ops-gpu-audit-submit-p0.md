# ops gpu audit submit p0

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_audit_submit_p0_20260521T134738_result.json`
- **Structured JSON:** [`6f80ad53a73b21623319.json`](../../sessions/6f/6f80ad53a73b21623319.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dr_epoch_matched 已在 registry 中（PPL=18.78）。现在分析 GPU 冲突情况。

## 产出报告

### 1. GPU 当前状态

| GPU | 显存占用 | 利用率 | 正在运行 | 进度 | 预估剩余 |
|-----|---------|--------|---------|------|---------|
| 0 | 45.6/97.9 GB | 100% | `detect_remove_q05_seed42` (训练) | 4016/6103 (66%) | ~1h13m |
| 1 | 90.2/97.9 GB | 100% | `bs16_adaptive_tau07_seed42` (训练) | 未查 | — |
| 2 | 14.3/97.9 GB | 100% | `uniform_epoch_matched_indep_lr_seed42` eval (2个eval进程) | 接近完成 | 数分钟 |
| 3 | 45.6/97.9 GB | 97% | `random_reweight_baseline_seed42` (训练，但数据是 scored_data_**random_shuffle**.jsonl + **adaptive**) | 3229/6103 (53%) | ~1h51m |

### 2. dr_epoch_matched_indep_lr_seed42 结果

- **Status**: DONE (success), 已在 registry
- **Checkpoint**: `/root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_indep_lr_seed42/final`
- **Metrics**:
  - holdout PPL = **18.78**, loss = 2.93
  - OOD OWT PPL = 19.24, OOD Wiki PPL = 15.96
  - train_loss_final = 5.833, total_steps = 2533

### 3. uniform_epoch_matched_indep_lr_seed42 进度

训练已完成（2533/2533, train_loss=8.058）。Eval 正在 GPU 2 上运行（holdout + wiki），预计几分钟内完成。

### 4. 提交冲突

**cuda:0 — detect-remove baseline**: GPU 0 已在跑 `detect_remove_q05_seed42`（同一数据 scored_data_filtered_q05.jsonl + uniform + 6103 steps）。这实质上**就是**要提交的实验，只是 output_dir 名称不含 "baseline"。当前进度 66%，约 1h13m 后完成。

**cuda:3 — random-reweight baseline**: GPU 3 正在跑名为 `random_reweight_baseline_seed42` 的实验，但参数**完全不同**：
- 在跑的：`scored_data_random_shuffle.jsonl` + `weighting_method=adaptive`（打乱 q-score 顺序 + adaptive 加权）
- 要求的：`scored_data.jsonl` + `weighting_method=random`（原始数据 + 随机权重）

两个目标 GPU 均被占用，无法立即提交。选项：
1. **等 GPU 2 eval 完成后**，在 cuda:2 提交 random-reweight baseline（需要改 GPU 分配）
2. **等 GPU 0/3 当前任务结束**后再提交

需要你决定如何处理。

---
