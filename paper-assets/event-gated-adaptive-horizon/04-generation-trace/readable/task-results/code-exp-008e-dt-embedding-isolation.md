# code exp 008e dt embedding isolation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_008e_dt_embedding_isolation_20260514T032449_result.json`
- **Structured JSON:** [`53fa7a0484f3e59ef01e.json`](../../sessions/53/53fa7a0484f3e59ef01e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 清理完成。现在记录完整产出。

---

## 产出汇总

### 1. 代码差异分析

| 差异点 | 详情 | 影响 |
|--------|------|------|
| **RSSM dt_embedding** | `gate_enabled=True` → RSSM `max_dt=8` → `Embedding(8,32)` 注入 GRU 输入，+32维 | **结构性差异**。dt=1 时是常量向量，但改变了 GRU 输入维度 |
| event_gate 模块 | 存在但 `gate_fixed_dt>0` 时不训练（无梯度） | 死参数，不影响训练动态 |
| lambda_return 路径 | 使用 `lambda_return_variable_dt(dt=1)` → `pcont^1 = pcont` | **数学等价**，无影响 |
| subsample_variable_dt | `effective_max_dt=1` 早返回，data 不变 | **无影响**，dt_labels 全 1 |

**结论**：`gate_enabled=True, gate_fixed_dt=1, gate_subsample_max_dt=1` **不完全等价于** baseline（`gate_enabled=False`），唯一实质差异是 RSSM 的 dt_embedding(0) 常量向量。但这个差异对训练效果的影响正是 008e 要验证的。

### 2. 008e 完整启动命令

与 008a/c/d 保持一致的参数模板（`--configs defaults dmc_proprio`, `--steps 105000`, `--seed 1`, `--compile False`）：

```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && \
export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && \
CUDA_VISIBLE_DEVICES=&lt;GPU> python dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_008e_dt1_no_subsample_h15 \
  --steps 105000 --seed 1 --compile False --device cuda:0 \
  --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 1 \
  --imag_horizon 15
```

对比 008a 命令的唯一差异：`--gate_fixed_dt 2` → `--gate_fixed_dt 1`

### 3. Dry-run 验证结果

- 配置解析正确，模型初始化成功
- 训练循环正常运行，metrics 正常写入
- gate metrics 正确：`gate_dt_mean=1.0`, `gate_dt_1_frac=1.0`
- 无 crash、无 error

### 实验解读预期

- 008e ≈ baseline（~400）→ gate 基础设施 + dt_embedding(0) 常量对训练无影响，008a 的提升来自 dt=2 imagination
- 008e ≫ baseline → dt_embedding 本身有正面效果（额外 32 维表示容量），需要进一步隔离
- 008e ≪ baseline → gate 代码路径引入了意外负面影响

---
