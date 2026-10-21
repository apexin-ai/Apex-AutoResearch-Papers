# prep plan006 prolog sta batch

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan006-prolog-sta-batch_20260514T122642_result.json`
- **Structured JSON:** [`360cc7ff789bf9c575e0.json`](../../sessions/36/360cc7ff789bf9c575e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

准备完毕。汇总报告：

---

## plan006-prolog-sta-s43/s44 准备报告

### 配置确认
| 项目 | 状态 |
|------|------|
| Config | `grpo_prolog_exec_sta.yaml` ✅ (exec_weight=0.5, sta_weight=0.5, reward_mode=execution_sta) |
| 数据 | `data/train_500_seed42.jsonl` ✅ (484KB, C001 compliant) |
| 模型 | `/root/autodl-tmp/models/Qwen3-4B` ✅ |
| 磁盘 | `/root/autodl-tmp/` **148G 可用** ✅ (~10-20GB/实验，充足) |
| C003 | 脚本硬编码 `save_total_limit=1` + `log_completions=False` ✅ |
| 输出目录 | `plan006_prolog_sta_s43/s44` 已创建 ✅ |
| Registry | 两条目已更新 notes ✅ |

### 提交命令模板

**s43:**
```bash
bash -c "export CUDA_VISIBLE_DEVICES=X && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43 --warmup_ratio 0.1"
```

**s44:**
```bash
bash -c "export CUDA_VISIBLE_DEVICES=X && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s44 --warmup_ratio 0.1"
```

`X` = 等 GPU 释放后替换为可用卡号。

### ⚠️ warmup_ratio 不一致

sta-s42 使用默认 `warmup_ratio=0.0`，s43/s44 模板用 `0.1`。这与 exec-only 系列一致（exec-s42 无 warmup，exec-s43 有 0.1）。3-seed 对比中 s42 与 s43/s44 存在 warmup 配置差异——如需严格控制变量，应统一为 0.0 或 0.1。

### GPU 状态
两卡满载（cuda:0=plan018, cuda:1=plan006-exec-s43），需等释放后提交。Dry-run 跳过。

---
