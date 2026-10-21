# prep plan004 sta o1 vs on

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan004-sta-o1-vs-on_20260514T114424_result.json`
- **Structured JSON:** [`c24f1f3b865ccc243351.json`](../../sessions/c2/c24f1f3b865ccc243351.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verification complete. Here's the summary:

---

## plan004 代码就绪状态: **READY**

### 验证结果

| 检查项 | 状态 |
|--------|------|
| 配置文件 `configs/grpo_fast_isr_ablation.yaml` | 存在，参数正确 |
| `reward_mode: execution_fast_sta` 代码路径 | train_grpo.py:211 → `fast_sta_reward()` |
| `fast_sta_reward` (src/sta/reward.py:157) | 调用 `fast_isr_fol` (O(1) binary ISR) |
| `fast_isr_fol` (src/sta/isr.py:100) | 存在 |
| 数据文件 `data/train_500_seed42.jsonl` | 存在 (C001 ✓) |
| `save_total_limit=1`, `log_completions=False` | 已设置 (C003 ✓) |
| 输出目录冲突 | 无，目录不存在 |
| 磁盘空间 | 199G 可用，充足 |

### GPU 状态

两张 RTX PRO 6000 (96GB) 都在使用中：
- GPU 0: 96.6G/97.9G used (98% util) — 满载
- GPU 1: 49.3G/97.9G used (100% util) — 正在训练

**当前无可用 GPU，需等释放。**

### 提交命令

```bash
cd /root/solver-trace-ablation && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export CUDA_VISIBLE_DEVICES=&lt;GPU_ID> && \
nohup python scripts/train_grpo.py \
  --config configs/grpo_fast_isr_ablation.yaml \
  > /root/autodl-tmp/outputs/plan004_fast_isr_s42.log 2>&1 &
```

配置 YAML 已包含所有参数：
- `reward_mode: execution_fast_sta` (O(1) binary ISR)
- `num_steps: 500`, `seed: 42`, `num_generations: 8` (K=8)
- `exec_weight: 0.5`, `sta_weight: 0.5`
- `output_dir: /root/autodl-tmp/outputs/plan004_fast_isr_ablation_s42`
- `wandb_run: plan004_fast_isr_s42`

### 预计 GPU 时间

500 步，K=8，参照同配置实验（plan001/plan005 等 500 步约 3-5 小时），预计 **3-5 小时**。O(1) ISR 比 O(N) 快，可能偏下限。

### 对比实验说明

| 实验 | reward_mode | ISR 类型 | 步数 | 作用 |
|------|------------|---------|------|------|
| **plan004** (本次) | `execution_fast_sta` | O(1) binary | 500 | 验证 O(1) ISR 在长训练下无效 |
| plan001-exec-only-s42 | `execution_only` | 无 | 500 | baseline，无 STA 信号 |
| plan005-sta-low-s42 | `execution_sta` | O(N) continuous | 500 | full STA，预期优于 plan004 |

plan004 的预期结果：性能接近 exec-only（plan001），显著弱于 full STA（plan005），证明 O(1) binary ISR 信号不足以驱动学习。

---
