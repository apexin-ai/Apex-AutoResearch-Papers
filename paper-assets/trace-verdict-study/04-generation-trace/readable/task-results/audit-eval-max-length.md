# audit eval max length

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_eval_max_length_20260520T050347_result.json`
- **Structured JSON:** [`fd170f677dde1b03ef9c.json`](../../sessions/fd/fd170f677dde1b03ef9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键发现：seed42 的 maxlen2048 re-eval（May 16）得 16%，但 seed123（May 20）同样 maxlen=2048 得 99.16%。说明问题不在 evaluate.py 版本，而在 seed42 模型本身。

## Eval Max Length 审计结果

### 默认值
- `evaluate.py` 默认 max_length = **2048**，truncation_side = **right**
- `train_sft.py` 硬编码 max_length = **2048**

### 已确认问题

**1. deepseek_vota_seed42** — **严重**
- Registry accuracy = 84.45% ← 来自 **max_length=16384** 的 re-eval
- 原始 eval（默认 2048）= **15.97%**（eval_results.json / original_backup.json）
- Re-eval with fixed script (2048) = **16%**
- 同条件 seed123 (2048) = 99.16%, seed456 (2048) = 99.33%
- **Registry 指标不可信：记录的是非标准 eval 结果。** seed42 模型在标准 2048 eval 下表现灾难性（16%），与 seed123/456（99%+）差距巨大，说明 seed42 训练本身出了问题。
- Notes 中已记录："84.45% confirmed with max_length=16384"

**2. deepseek_full_trace_seed42_v3** — 已解决但磁盘文件不一致
- Registry accuracy = 79.16% ← 来自 max_length=2048 re-eval ✓
- 磁盘 eval_results.json = 28.49%（stale，来自 max_length=16384）
- eval_results_maxlen2048.json = 79.16% ✓
- Registry 标记 `reeval_discrepancy.status = "RESOLVED"`

### 可疑但不确定

| exp_id | accuracy | 同condition参考 | 说明 |
|--------|----------|----------------|------|
| full_trace_seed42 | 28.4% | v5=81.8% | 最早期实验（May 14），可能用了不同版本 evaluate.py |
| full_trace_seed42_v2 | 28.4% | v5=81.8% | 同上 |
| vota_seed42_v4 | 95.63% | v3=99.2%, v5=99.4% | 低 3-4pp，可能是早期训练参数不同 |
| deepseek_full_trace(无后缀) | eval_results.json=28.49%, eval_results_fixed.json=10.59% | v3=79.16% | 磁盘有两个不同结果 |

### 无问题

- **121/126 个实验** eval 命令使用 max_length=2048（显式或默认），无非标准 max_length
- 只有 5 个实验显式指定 `--max_length 2048`：deepseek_ae_only_seed42, deepseek_loop_only_seed123, deepseek_vota_seed123, deepseek_vota_seed456, vota_seed456
- 其余 53 个有 eval 命令的实验使用默认值 2048
- 68 个实验的 eval 在 spec.command 中无独立 eval 步骤（由 hook 或外部触发）
- 4 个 full_trace_tail 实验显式使用 `--truncation_side left`（符合预期）

### 建议行动
1. **deepseek_vota_seed42** 需要用当前 evaluate.py + max_length=2048 重新训练或标记为废弃（seed42 模型本身有问题，16% accuracy 不可用）
2. 清理 deepseek_full_trace_seed42_v3 磁盘上的 stale eval_results.json
3. 早期实验（full_trace_seed42/v2）如果仍在论文中引用，需要用当前 evaluate.py 重新 eval

---
