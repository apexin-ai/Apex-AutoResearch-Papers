# code plan006 prolog readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-prolog-readiness_20260514T094707_result.json`
- **Structured JSON:** [`d8cd9974b5b295924e52.json`](../../sessions/d8/d8cd9974b5b295924e52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：plan006 Prolog 实验就绪状态

### 1. Prolog 数据
- **路径**: `data/train_500_seed42.jsonl` — 500 条（符合 C001）
- 数据原为 FOL 格式（含 `context`, `question`, `answer`），无 `prolog_premises`/`prolog_query` 字段
- **不阻塞**: `build_prolog_dataset` 用空默认值处理；Prolog prompt 仅使用 `context`/`question`（NL）；STA reward 从模型生成的 Prolog 代码自身计算，不依赖 gold reference

### 2. 配置文件
| 实验 | 配置 | reward_mode | exec_weight | sta_weight | solver |
|------|------|-------------|-------------|------------|--------|
| exec-only | `configs/grpo_prolog_exec_only.yaml` | execution_only | 1.0 | 0.0 | prolog |
| exec+STA | `configs/grpo_prolog_exec_sta.yaml` | execution_sta | 0.5 | 0.5 | prolog |

### 3. 代码支持确认
- `train_grpo.py`: 完整支持 `--logic_type prolog`，含 `build_prolog_dataset`、Prolog system prompt、prolog solver/reward 调度
- `src/sta/prolog_reward.py`: 存在
- `src/solvers/factory.py`: 注册 `"prolog"` → `PrologSolver`
- SWI-Prolog: `/usr/bin/swipl` (8.4.2) 已确认

### 4. Config merge 陷阱
argparse 有非 None 默认值的参数 **不会被 config YAML 覆盖**。必须 CLI 显式传递：
- `--num_steps 500`（argparse 默认 100）
- `--num_generations 8`（argparse 默认 4）

### 5. 两个实验的完整训练命令

**plan006-prolog-exec-s42** (exec-only, 物理 GPU 0):
```bash
bash -c "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --num_generations 8 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42"
```

**plan006-prolog-sta-s42** (exec+STA, 物理 GPU 1):
```bash
bash -c "export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --num_generations 8 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42"
```

### 6. Dry-run 结果
**OOM** — 训练需要 ~80GB/GPU，但 eval_sta.py 进程各占 ~16GB 导致不足。

### 7. 磁盘空间
`/root/autodl-tmp`: 82G 可用 (68%) — 充足

### 8. 阻塞问题
**GPU 被 eval 进程占用**:
- PID 504301 (GPU 0): `eval_sta.py --model_path plan002_additive_b01_s43/checkpoint-500`
- PID 504987 (GPU 1): `eval_sta.py --model_path plan002_additive_b01_s43`
- 各占 ~16GB，约 17:45 启动，尚未完成（无 eval_results.json 输出）
- **需等 eval 完成后方可提交训练**

---
