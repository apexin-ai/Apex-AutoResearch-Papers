# infra steering status and qwen prep

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_steering-status-and-qwen-prep_20260522T110418_result.json`
- **Structured JSON:** [`5b99de2fa6bccaf2d9e8.json`](../../sessions/5b/5b99de2fa6bccaf2d9e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Steering Llama v3 — 已完成

v3 运行成功（前两次 v1/v2 因 hook 维度 bug 崩溃，v3 修复后完整跑完）。

**配置**: Layer 28, probe acc 77.6%, n=136, position=last

**结果汇总**:

| Alpha | Steering Flips | Control Flips | p→c | c→p | Fisher p |
|------:|:--------------:|:-------------:|:---:|:---:|:--------:|
| -20 | 14.7% | 16.9% | 0 | 2 | 0.74 |
| -10 | 10.3% | 9.6% | 0 | 1 | 1.00 |
| -5 | 4.4% | 3.7% | 1 | 0 | 1.00 |
| -2 | 3.7% | 2.9% | 1 | 0 | 1.00 |
| -1 | 4.4% | 2.9% | 2 | 0 | 0.75 |
| +1 | 0.7% | 0.7% | 0 | 0 | 1.00 |
| +2 | 2.2% | 1.5% | 0 | 0 | 1.00 |
| +5 | 3.7% | 4.4% | 0 | 0 | 1.00 |
| +10 | 7.4% | 6.6% | 0 | 0 | 1.00 |
| +20 | 12.5% | 17.6% | 1 | 0 | 0.31 |

**结论**: Steering 对 Llama **完全无效**。所有 alpha 的 steering flip rate 与 control flip rate 无显著差异（所有 Fisher p >> 0.05）。大 alpha 只是增加了噪声 flip，但无方向性效果。

---

## Steering Qwen 准备情况

- **cuda:0**: 空闲（3 MiB, 0%）
- **模型**: `/root/models/Qwen3-8B-Instruct/` 已存在
- **数据**: `data/qwen3/en_conflict_{train,test}.jsonl` 已确认
- **Peak layer**: 24（EN→EN probe）
- **输出目录**: `data/qwen3/steering_results/`（尚不存在，脚本会创建）

**提交命令**:

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/clkc_mech_interp && \
CUDA_VISIBLE_DEVICES=0 nohup python -u src/steering_experiment.py \
  --model /root/models/Qwen3-8B-Instruct/ \
  --data_dir data/qwen3 \
  --output_dir data/qwen3/steering_results \
  --peak_layer 24 \
  > logs/steering_qwen.log 2>&1 &
```

是否现在提交运行？

---
