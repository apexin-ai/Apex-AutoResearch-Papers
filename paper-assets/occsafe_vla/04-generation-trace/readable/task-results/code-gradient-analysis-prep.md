# code gradient analysis prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient_analysis_prep_20260527T041505_result.json`
- **Structured JSON:** [`ee3b1913285ff7bae381.json`](../../sessions/ee/ee3b1913285ff7bae381.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有了完整的调研信息。下面是总结。

---

## 调研报告：v2 梯度分析脚本准备

### 1. 现有脚本情况

**没有现成的梯度分析脚本。** `analysis/` 目录下只有evaluation层面的消融诊断脚本：
- `ablation_diagnostic.py` — 比较 CAR/TSR 指标的消融矩阵
- `bootstrap_ci.py`, `per_task_comparison.py`, `seed_instability.py` — 统计分析

**需要从头写梯度分析脚本。**

### 2. 代码架构理解

**Loss 计算流（`finetune.py:481-490`）：**
```
total_loss = action_loss + occ_weight * occ_loss
```

**梯度流路径：**
- **共享参数**（backbone + LLM + projector）：同时被 action_loss 和 occ_loss（Cell 1/2 不 detach 时）的梯度更新
- **Action head**（`L1RegressionActionHead`，2层 MLP ResNet）：仅 action_loss 梯度
- **OCC head**（`BEVOccupancyHead`，ConvTranspose decoder）：仅 occ_loss 梯度
- `_cached_patch_features`（`modeling_prismatic.py:447`）：OCC head 从此获取 backbone 特征
- `occ_detach=True` 时：`patch_features = patch_features.detach()`，切断 occ_loss 对 backbone 的梯度

**关键：梯度分析应聚焦共享 backbone/LLM 参数，而非 action head 自身参数。**

### 3. 可用 v2 Checkpoints

| 条件 | 服务器 | Checkpoint 路径 | Step |
|------|--------|----------------|------|
| Cell 1 (Full OCC BN) | westd-34685 | `/root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/...-50000_chkpt` | 50k ✓ |
| Cell 2 (Full OCC LN) | westd-10894 | `/root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/...-50000_chkpt` | 50k ✓ |
| Cell 3 (Detach BN) | westd-34685 | `/root/autodl-tmp/checkpoints/detach_bn_v2_s0/...-50000_chkpt` | 50k ✓ |
| Cell 4 (Detach LN) | westd-34685 | `/root/autodl-tmp/checkpoints/detach_ln_v2_s1/...-10000_chkpt` | 10k (可能仍在训练) |
| Vanilla | westd-34685 | `/root/autodl-tmp/checkpoints/vanilla_v2_s1/...-50000_chkpt` | 50k ✓ |

Cell 4 只有 10k checkpoint，可能正在训练中（8/8 GPU 满载，RTX PRO 6000 96GB）。

### 4. 脚本设计方案

**需要写的脚本：`gradient_analysis_v2.py`**

核心逻辑：
```python
# 对每个 checkpoint:
# 1. 加载模型 + checkpoint（含 LoRA adapter + action_head + occ_head）
# 2. 加载同一批 data（固定 seed 保证跨条件可比）
# 3. 前向传播得到 action_loss 和 occ_loss（分别计算）
# 4. action_loss.backward(retain_graph=True) → 收集共享参数梯度 → 保存 → zero_grad
# 5. occ_loss.backward() → 收集共享参数梯度
# 6. 计算:
#    - cosine similarity（action_grad vs occ_grad）逐层 + 全局
#    - L2 norm ratio（occ_grad_norm / action_grad_norm）
#    - 梯度方差（跨 batch 的方差不对称性）
# Vanilla 无 OCC head，只计算 action gradient baseline
```

**需要从 `finetune.py` 借用的部分：**
- `FinetuneConfig` dataclass 及模型加载逻辑（~L1000-1050）
- `run_forward_pass()` 需要拆分成分别返回 action_loss 和 occ_loss 的版本
- 数据加载：`RLDSDataset` + `RLDSBatchTransform` + collator

**Checkpoint 加载需要的文件：**
每个 checkpoint 目录包含：`action_head--*_checkpoint.pt`, `occ_head--*_checkpoint.pt`, `lora_adapter/`, `config.json`, `model-*.safetensors`

### 5. 运行计划

| 步骤 | 内容 | GPU 需求 | 预估时间 |
|------|------|----------|---------|
| 编写脚本 | 本地或远程 | 无 | ~1h |
| 跑 Cell 1 | 加载 checkpoint + 100 batch forward/backward | 1 GPU, ~30GB | ~15min |
| 跑 Cell 2 | 同上 | 1 GPU | ~15min |
| 跑 Cell 3 | 同上 | 1 GPU | ~15min |
| 跑 Cell 4 | 同上 | 1 GPU | ~15min |
| 跑 Vanilla | 同上（只有 action grad） | 1 GPU | ~10min |
| 汇总出图 | 无 GPU，生成 cosine/norm 对比图 | CPU | ~5min |

**总 GPU 时间：~70min（1 GPU）。**

**约束：** 当前 8/8 GPU 全部满载。需要等待某个训练完成后腾出 GPU，或等所有训练在 DDL (2026-05-28 12:00 UTC) 前完成后再跑。考虑到 CoRL DDL，建议：
1. 先把脚本写好（不需要 GPU）
2. 一旦有 GPU 空出，立刻 5 条件串行跑完（~70min）
3. 或者用 2 张 GPU 并行跑（~35min）

---
