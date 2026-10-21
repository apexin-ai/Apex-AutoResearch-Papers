# prep plan006 prolog readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan006-prolog-readiness_20260514T094538_result.json`
- **Structured JSON:** [`d2fd4da51f0460c8250b.json`](../../sessions/d2/d2fd4da51f0460c8250b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan006 Prolog 实验就绪状态

### ⚠️ 部分就绪

### ✅ 已就绪

| 检查项 | 状态 |
|--------|------|
| swipl (SWI-Prolog) | ✅ `/usr/bin/swipl` |
| PrologSolver (`src/solvers/prolog.py`) | ✅ factory 已注册 |
| Prolog STA reward (`src/sta/prolog_reward.py`) | ✅ `prolog_sta_reward` + `fast_prolog_sta_reward` |
| `train_grpo.py` Prolog 支持 | ✅ `logic_type=prolog` → Prolog prompts + dataset builder + reward dispatch |
| `eval_sta.py` Prolog 支持 | ✅ `--logic_type prolog` |
| 训练数据 | ✅ `data/train_500_seed42.jsonl`（500条，用 context+question 构造 Prolog prompt，符合 C001） |
| exec-only 配置 | ✅ `grpo_prolog_exec_only.yaml` 正确 |
| 磁盘空间 | ✅ 82GB 可用 |

### ❌ 需修复

**`grpo_prolog_exec_sta.yaml` 配置不匹配任务要求**：

| | 当前配置 | 任务要求 |
|--|---------|---------|
| reward_mode | `execution_sta`（线性组合） | `additive_bonus`（乘法 bonus） |
| 公式 | `0.5 * exec + 0.5 * ISR` | `exec * (1 + 0.1 * ISR)` |
| beta | 未设置 | `0.1` |

需要将 `grpo_prolog_exec_sta.yaml` 修改为：
```yaml
reward_mode: additive_bonus
beta: 0.1
```
并删除 `exec_weight` / `sta_weight`（additive_bonus 模式不使用这两个参数）。

### 训练命令（修正配置后）

**plan006-prolog-exec-s42**（可直接提交）：
```bash
export CUDA_VISIBLE_DEVICES=N
cd /root/solver-trace-ablation
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml > /root/autodl-tmp/outputs/grpo_prolog_exec_only/train.log 2>&1 &
```

**plan006-prolog-sta-s42**（需先修正配置）：
```bash
export CUDA_VISIBLE_DEVICES=M
cd /root/solver-trace-ablation
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml > /root/autodl-tmp/outputs/grpo_prolog_exec_sta/train.log 2>&1 &
```

（N/M 替换为实际空闲 GPU 编号，提交前 `nvidia-smi` 确认占用，遵守 C002/C005）

---
