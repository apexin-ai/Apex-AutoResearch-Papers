# prep plan006 prolog readiness

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan006-prolog-readiness_20260514T061712_result.json`
- **Structured JSON:** [`26692489d638652a000d.json`](../../sessions/26/26692489d638652a000d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。以下是就绪报告。

---

## plan006 Prolog GRPO 就绪报告

### ✅ 已就绪

| 项目 | 状态 | 路径/详情 |
|------|------|-----------|
| Prolog solver | ✅ | `src/solvers/prolog.py` → PrologSolver, dry-run 证明 `proved=True` |
| SWI-Prolog | ✅ | `/usr/bin/swipl` (8.4.2), `is_available()=True` |
| Prolog reward (full) | ✅ | `src/sta/prolog_reward.py` — `prolog_sta_reward` O(n), ISR=1.0 验证通过 |
| Prolog reward (fast) | ✅ | `fast_prolog_sta_reward` O(1), 验证通过 |
| 训练脚本 | ✅ | `scripts/train_grpo.py` — 支持 `--logic_type prolog`, 独立 prompt 模板 |
| 数据集构建 | ✅ | `build_prolog_dataset()` 从现有数据构建，无需 Prolog 专用数据 |
| 训练数据 | ✅ | `data/train_500_seed42.jsonl` — 500 条 (C001 合规) |
| 配置文件 | ✅ | `configs/grpo_prolog_exec_only.yaml`, `configs/grpo_prolog_exec_sta.yaml` |
| 模型 | ✅ | `/root/autodl-tmp/models/Qwen3-4B/` (7.6GB) |
| save_total_limit | ✅ | 代码硬编码 `save_total_limit=1` (C003 合规) |
| 磁盘 | ✅ | 数据盘 187G 可用，6 runs × ~8GB checkpoint = ~48GB 富余 |

### ⚠️ 需修改

1. **num_steps**: 两个 config 文件中 `num_steps: 100`，任务要求 **500**。需改 config 或用 CLI `--num_steps 500` 覆盖。
2. **no_wandb**: 两个 config 中 `no_wandb: true`。如需 wandb 跟踪需去掉或 CLI 覆盖 `--wandb_project solver-trace-ablation`。
3. **seed**: config 中固定 `seed: 42`，3 seeds 需要 CLI `--seed` 覆盖。

### 训练命令模板（3 seeds × 2 modes = 6 runs，两两并行）

```bash
# ── Round 1: seed=42 ──
# GPU 0: exec-only
export CUDA_VISIBLE_DEVICES=0
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_only.yaml \
  --num_steps 500 --seed 42 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_only_s42 \
  --wandb_project solver-trace-ablation \
  --wandb_run plan006_prolog_exec_only_s42 \
  > /root/autodl-tmp/outputs/plan006_exec_only_s42.log 2>&1 &

# GPU 1: exec+STA
export CUDA_VISIBLE_DEVICES=1
nohup python scripts/train_grpo.py \
  --config configs/grpo_prolog_exec_sta.yaml \
  --num_steps 500 --seed 42 \
  --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_sta_s42 \
  --wandb_project solver-trace-ablation \
  --wandb_run plan006_prolog_exec_sta_s42 \
  > /root/autodl-tmp/outputs/plan006_exec_sta_s42.log 2>&1 &

# ── Round 2: seed=123 (Round 1 完成后) ──
# 同上，替换 --seed 123, 输出目录/run 名中 s42→s123

# ── Round 3: seed=456 (Round 2 完成后) ──
# 同上，替换 --seed 456, 输出目录/run 名中 s42→s456
```

### 资源估算

- **显存**: Qwen3-4B + K=8 + batch=4 + max_len=512 → 预估 ~40-60GB/GPU (96GB RTX PRO 6000 充裕)
- **时间**: ~3-5h/round (基于 FOL 同配置参考，Prolog solver 比 Prover9 更快)
- **磁盘**: 每 run ~8GB checkpoint × save_total_limit=1 → 最多同时 16GB，总计 ~48GB

### 缺失项

无。代码、数据、依赖、配置均就绪，只需调整 config 中的 num_steps 和 wandb 设置。

---
