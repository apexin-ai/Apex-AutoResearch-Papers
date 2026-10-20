# analysis dpo rebuilt 3ep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dpo_rebuilt_3ep_20260523T093841_result.json`
- **Structured JSON:** [`81c19892b5121b26d2ac.json`](../../sessions/81/81c19892b5121b26d2ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 数据未找到（可能未正确初始化）。基于训练日志的完整分析如下：

---

## DPO 3-epoch 训练结果分析

### 1. 训练概况

| 项目 | 值 |
|------|-----|
| 总步数 | 561 |
| 训练耗时 | 6135s (≈1h 42min) |
| 平均 train_loss | 0.4347 |
| 退出码 | 0 (正常完成) |
| 报错/异常 | 无 |

### 2. Checkpoint 结构

- `checkpoint-400` (~epoch 2.14)
- `checkpoint-500` (~epoch 2.67)
- `checkpoint-561` (final, epoch 3)
- **最终 adapter**: `/root/autodl-tmp/dpo_output_rebuilt_3ep/adapter_model.safetensors` (504MB)
- adapter_config.json ✓, ref/ 目录 ✓

### 3. 训练动态（逐 epoch 关键指标）

| 指标 | ~Ep 0.5 | ~Ep 1.0 | ~Ep 1.5 | ~Ep 2.0 | ~Ep 2.5 | ~Ep 3.0 |
|------|---------|---------|---------|---------|---------|---------|
| loss | 0.579 | 0.514 | 0.416 | 0.268 | 0.336 | 0.300 |
| accuracy | 0.694 | 0.719 | 0.831 | 0.919 | 0.888 | 0.869 |
| margin | 0.389 | 1.064 | 1.633 | 2.203 | 2.142 | 2.404 |
| entropy | 0.114 | 0.108 | 0.097 | 0.098 | 0.094 | 0.090 |
| logps/chosen | -39.9 | -63.3 | -52.4 | -67.6 | -61.5 | -58.2 |

### 4. 过拟合分析

**有明显过拟合迹象：**

1. **Accuracy 在 epoch 2 见顶 (0.919) 后回落至 epoch 3 的 0.869** — 典型的过拟合后训练不稳定模式。
2. **Entropy 持续下降 (0.114 → 0.090)** — 模型 policy 越来越确定，多样性损失。
3. **最终 summary 的 accuracy=1.0, margin=4.619** — 在最后一个 batch 上完美分离，过拟合信号。
4. **logps/chosen 从 -40 漂移到 -58~-68 范围** — 模型显著偏离 reference policy，chosen 的绝对概率在变差（DPO 在压低 rejected 的同时也拉低了 chosen）。
5. **Loss 在 epoch 2 之后不再持续下降**，在 0.27-0.36 之间振荡。

### 5. 3ep vs 1ep 对比

| 指标 | 1ep 位置 (~step 187) | 3ep 最终 (~step 561) |
|------|---------------------|---------------------|
| loss | ~0.51 | ~0.30 |
| accuracy | ~0.72 | ~0.87 |
| margin | ~1.06 | ~2.40 |
| 下游 ign_f1 | **0.32231** | **待 eval** |
| EDCR | **0.8123** | **待 eval** |

训练指标上 3ep 大幅优于 1ep（loss 降 41%, margin 翻倍），但这可能只反映了在训练集上的拟合程度而非泛化能力。accuracy 在 epoch 2 后的回落和 entropy 的持续下降是负面信号。

### 6. 初步判断

3ep DPO 训练在 **训练集** 上的区分能力显著强于 1ep，但存在 **过拟合风险**。关键判据在于下游 eval：
- 如果 ign_f1 > 0.32231 → 3ep 仍有收益，支撑 "gradual degradation" 假说（更多 epoch = 更好，或至少不大幅退化）
- 如果 ign_f1 < 0.32231 → 典型的 DPO 过拟合，epoch 2 可能是最优点，支撑在 checkpoint-400 处早停

### 7. 下一步

需要在 Re-DocRED test set 上跑 eval：
- 最终 checkpoint (`/root/autodl-tmp/dpo_output_rebuilt_3ep/`)
- 可选：中间 checkpoint-400 (~ep 2.14) 作为早停候选
- 对比 1ep baseline ign_f1=0.32231

是否现在提交 eval？

---
