# infra check training progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-training-progress_20260514T145637_result.json`
- **Structured JSON:** [`c3c10250cd2a1c4c5ebf.json`](../../sessions/c3/c3c10250cd2a1c4c5ebf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`save_total_limit=1` 和 `log_completions=False` 已硬编码在脚本中，符合 C003 约束。

---

## 报告

### 1. 训练进度

| 实验 | GPU | Step | 进度 | 剩余时间 | 预计完成 |
|------|-----|------|------|----------|---------|
| plan006-prolog-exec-s44 | cuda:0 | 347/500 | 69% | ~21 min | ~23:17 |
| plan006-prolog-exec-s43-r3 | cuda:1 | 259/500 | 52% | ~1h08m | ~00:05 |

**s44 关键指标** (step 347): reward=1.0, prove_rate=1.0, isr=0.480, loss=0.0 — 模型已收敛饱和
**s43-r3 关键指标** (step 259): reward=0.875, prove_rate=0.875, isr=0.023 — 仍在训练中，step_time ~16s（比 s44 慢）

### 2. 资源状态

| 资源 | 状态 |
|------|------|
| 磁盘 | 120G/250G (48%) — 131G 可用，健康 |
| cuda:0 | 80189/97887 MiB (82%), util 0%* |
| cuda:1 | 81009/97887 MiB (83%), util 92% |

*cuda:0 util=0% 是快照瞬时值，内存占用确认模型已加载，训练正常运行。

### 3. 下批实验准备状态

所有前置条件已满足：
- `configs/grpo_additive_random.yaml` ✅
- `configs/grpo_prolog_exec_sta.yaml` ✅
- `data/train_500_seed42.jsonl` ✅ (C001)
- `save_total_limit=1`, `log_completions=False` 硬编码 ✅ (C003)
- output_dir 无冲突（plan006_prolog_sta_s43/s44 存在但为空，plan018 目录不存在会自动创建）

### 草拟提交命令

**优先级 1 — plan018-additive-random-b01-s43-r2**（cuda:0 释放后）
```bash
bash -c "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --beta 0.1 --seed 43 --num_steps 500 --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2"
```

**优先级 2 — plan006-prolog-sta-s43**（cuda:1 释放后）
```bash
bash -c "export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --seed 43 --num_steps 500 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43"
```

**优先级 3 — plan006-prolog-sta-s44**（等上面任一完成后接替该 GPU）
```bash
bash -c "export CUDA_VISIBLE_DEVICES={0或1} && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --seed 44 --num_steps 500 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s44"
```

### GPU 分配时间线

1. **~23:17** — cuda:0 空闲 → 提交 plan018-additive-random-b01-s43-r2
2. **~00:05** — cuda:1 空闲 → 提交 plan006-prolog-sta-s43
3. plan006-prolog-sta-s44 需等 #1 或 #2 完成（预计 ~2h 后有 GPU 空出）

---
