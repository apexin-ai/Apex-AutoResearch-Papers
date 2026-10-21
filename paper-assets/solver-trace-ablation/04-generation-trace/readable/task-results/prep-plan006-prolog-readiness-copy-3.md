# prep plan006 prolog readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan006-prolog-readiness_20260514T081243_result.json`
- **Structured JSON:** [`f53d8287caea0274def1.json`](../../sessions/f5/f53d8287caea0274def1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。以下是 readiness report。

---

## Plan006 Prolog Exec-Only GRPO — Readiness Report

### 1. 环境就绪状态

| 组件 | 状态 | 详情 |
|------|------|------|
| SWI-Prolog | ✅ | 8.4.2, `/usr/bin/swipl` |
| Prolog STA 测试 | ✅ | 5/5 passed，rule ablation 正确工作 |
| 磁盘空间 | ✅ | `/root/autodl-tmp` 142GB 可用（44% 已用） |

### 2. 代码就绪状态

| 模块 | 状态 | 文件 |
|------|------|------|
| Prolog Solver | ✅ | `src/solvers/prolog.py` — PrologSolver 调 swipl 子进程 |
| Solver Factory | ✅ | `src/solvers/factory.py` — `get_solver("prolog")` 已注册 |
| Prolog STA Reward | ✅ | `src/sta/prolog_reward.py` — rule ablation ISR + fast O(1) 版本 |
| 训练脚本 Prolog 支持 | ✅ | `scripts/train_grpo.py` — `--logic_type prolog --solver prolog` |
| Prolog Prompt | ✅ | `PROLOG_SYSTEM_PROMPT` + `PROLOG_USER_TEMPLATE` 已定义 |
| `build_prolog_dataset()` | ✅ | 使用 context/question 字段构建 Prolog prompt |
| `make_reward_fn` Prolog 分支 | ✅ | `logic_type == "prolog"` 时用 `prolog_sta_reward` / `fast_prolog_sta_reward` |
| eval_sta.py Prolog 支持 | ✅ | `--logic_type prolog` 已实现，用 `prolog_sta_reward` |
| Config 文件 | ✅ | `configs/grpo_prolog_exec_only.yaml` 已存在 |

### 3. 数据就绪状态

| 数据 | 状态 | 详情 |
|------|------|------|
| 训练数据 | ✅ | `data/train_500_seed42.jsonl`，500 条。数据与 FOL 共用同一 NL 数据（context + question），Prolog 训练时模型生成 Prolog 形式化而非 FOL |

符合 C001 约束：使用同一数据文件，seed 仅控制模型初始化。

### 4. 缺失项清单

**无缺失项。** 所有代码、数据、环境均已就绪，可直接启动训练。

### 5. 建议训练命令（3-seed）

基于 FOL exec-only 命令和 config 改写，遵守 C002（export 显式设 GPU）、C003（save_total_limit=1）、C005（显式 CUDA_VISIBLE_DEVICES）：

**Seed 42 (GPU 0):**
```bash
bash -c "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan006-prolog-exec-only-s42 --reward_mode execution_only --logic_type prolog --solver prolog --num_steps 500 --seed 42 --num_generations 8 --save_total_limit 1 --no_wandb --log_completions False"
```

**Seed 43 (GPU 1):**
```bash
bash -c "export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan006-prolog-exec-only-s43 --reward_mode execution_only --logic_type prolog --solver prolog --num_steps 500 --seed 43 --num_generations 8 --save_total_limit 1 --no_wandb --log_completions False"
```

**Seed 44（等前两个跑完后再跑）:**
```bash
bash -c "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan006-prolog-exec-only-s44 --reward_mode execution_only --logic_type prolog --solver prolog --num_steps 500 --seed 44 --num_generations 8 --save_total_limit 1 --no_wandb --log_completions False"
```

注意：两张 GPU 可并行跑 s42 + s43，s44 等其中一个完成后接着跑。每次训练模型权重约 16GB，3 runs 共 ~48GB，当前 142GB 可用空间充足。

---
