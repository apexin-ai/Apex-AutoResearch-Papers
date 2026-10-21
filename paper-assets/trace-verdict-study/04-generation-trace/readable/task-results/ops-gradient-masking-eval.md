# ops gradient masking eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gradient_masking_eval_20260522T094230_result.json`
- **Structured JSON:** [`a9c5a4d5f4837b585f65.json`](../../sessions/a9/a9c5a4d5f4837b585f65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. Gradient Masking 结果

**训练完成**，3 epochs / 444 steps，耗时 ~1h15m。

| 指标 | 值 |
|------|-----|
| eval_loss | **0.0533** |
| train_loss (final) | 0.34–0.40 |
| condition | `exception_only` + `--gradient_mask_ratio` |
| checkpoints | checkpoint-148, 296, 444, final |

**没有准确率指标** — 训练只记录了 eval_loss，未计算 accuracy。需要用 evaluate.py 跑一次：

```bash
cd /root/trace-verdict-study && /root/miniconda3/bin/python eval/evaluate.py \
  --condition exception_only \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed42/final \
  --gpu 1 --save_predictions
```

eval_loss=0.053 非常低，预期准确率应该不错。

---

### 2. exc_type_only 训练

**问题：`exc_type_only` 不在 train_sft.py 的 `--condition` 枚举里。** 需要先在 `train_sft.py` 和 `evaluate.py` 的 argparse choices 中添加 `exc_type_only`，否则命令会报错。

数据已就绪：
- train: 4720 samples ✓
- test: 1190 samples ✓

添加 condition 后，训练命令：
```bash
cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py \
  --condition exc_type_only \
  --data_dir /root/autodl-tmp/trace-verdict-study-data/exc_subcomponent/ \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exc_type_only_seed42 \
  --gpu 1 --seed 42 --gradient_checkpointing
```

**cuda:1 完全空闲**（0 MiB / 97887 MiB，0% 利用率）✓

---

### 3. cuda:0 诊断

| 项目 | 结果 |
|------|------|
| 显存占用 | 49175 MiB / 97887 MiB |
| GPU 利用率 | 0% |
| 运行进程 | **无**（nvidia-smi Processes 列表为空） |
| fuser /dev/nvidia0 | `/dev/nvidia0` 不存在（容器只暴露 nvidia1, nvidia3） |
| lsof | 未安装 |

**结论：这是训练完成后的残留显存泄漏**（进程已退出但 GPU memory 未释放）。两个 GPU 都是 NVIDIA RTX PRO 6000 Blackwell (96GB)。可以尝试 `nvidia-smi --gpu-reset -i 0` 释放，或者直接用 cuda:1 跑 exc_type_only，不受影响。

---

**下一步建议的优先级：**
1. 修改 train_sft.py / evaluate.py 添加 `exc_type_only` condition → 立即提交训练
2. 同时在 cuda:1 上跑 gradient_masking 的 evaluate.py 拿准确率

---
