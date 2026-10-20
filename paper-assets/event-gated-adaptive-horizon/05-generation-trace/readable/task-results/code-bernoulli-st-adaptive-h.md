# code bernoulli st adaptive h

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bernoulli_st_adaptive_h_20260514T022231_result.json`
- **Structured JSON:** [`e36b75b93c6c50026f72.json`](../../sessions/e3/e36b75b93c6c50026f72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. 选择方案 b（物理时间预算掩码）

理由：
- 不改 `_imagine`（仍跑 `imag_horizon=15` 步），仅在 `_compute_target` 中根据物理时间掩码截断
- 优雅：discount 置零 → lambda return 自然在边界处 bootstrap → weights 自然归零
- 与论文叙事一致（"event-gated adaptive horizon"）
- 不引入可变长度 tensor，零额外复杂度

### 2. 具体改动

| 文件 | 行号 | 改动 |
|------|------|------|
| `configs.yaml` | L118 | 添加 `bernoulli_physical_horizon: 15` |
| `models.py` | L670-686 | `_compute_target` 中计算物理时间 `time_at`，生成 `horizon_mask`，乘入 `discount` |
| `models.py` | L703-704 | `weights *= horizon_mask`（确保无效步 loss 权重为零）|
| `models.py` | L563-577 | `_train` 中添加 `adaptive_horizon_{mean,min,max}` metrics |

### 3. Commit hash
`981ce19`

### 4. Dry-run 结果
- 初始化正常，eval 完成（`eval_return 41.5`）
- 训练正常运行到 120s timeout，无 crash/error
- `_compute_target` 中 adaptive horizon 代码和 metrics 代码均被执行

### 5. 完整启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa

python dreamer.py \
  --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_bernoulli_adaptive_h \
  --steps 500000 \
  --seed 1 \
  --compile False \
  --device cuda:1 \
  --gate_enabled True \
  --gate_type bernoulli_st \
  --bernoulli_physical_horizon 15
```

---
