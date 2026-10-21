# prep seed123 8b val sweep plan

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_seed123-8b-val-sweep-plan_20260515T021451_result.json`
- **Structured JSON:** [`5e394bca973a49fb417d.json`](../../sessions/5e/5e394bca973a49fb417d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 训练进度
- **当前 step**: 5458 / 6633 (82%)
- **已运行**: 8h31m
- **速度**: ~8.3s/step
- **剩余**: 1175 steps × 8.3s ≈ **2h43m**
- **最近指标**: train_loss=0.2422 (step 5450), eval_loss=0.3489 (step 5400, epoch 2.44)

### 已有 Checkpoints
| Checkpoint | 时间 | 大小 |
|---|---|---|
| checkpoint-200 | May 14 14:35 | ~176M |
| checkpoint-4800 | May 15 08:01 | ~176M |
| checkpoint-5000 | May 15 08:43 | ~176M |
| checkpoint-5200 | May 15 09:25 | ~176M |
| checkpoint-5400 | May 15 10:07 | ~176M |

配置: `save_steps=200, save_total_limit=5, eval_steps=200`

### 训练结束时预计保留的 Checkpoints

save_total_limit=5，后续还会产出 checkpoint-5600/5800/6000/6200/6400/6600。旧的会被逐步淘汰。训练结束时预计保留：

- checkpoint-200（可能被保留——疑似 resume 前遗留或 best model）
- checkpoint-6000, 6200, 6400, 6600（最后4个）

如果 checkpoint-200 被淘汰，则保留最后5个: **5800, 6000, 6200, 6400, 6600**。

### Val Sweep 计划

**策略**: 全量评估（≤ 6 个 checkpoint，无需抽样）

每个 checkpoint eval 参数：
```bash
python /home/sonny/exec-sim-repair-verifier/eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-XXXX \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --split val \
  --device cuda:3 \
  --batch_size 1 \
  --max_seq_length 8192 \
  --output_dir /root/autodl-tmp/eval_results_8b_seed123/
```

- **每个 checkpoint**: ~35 min
- **5-6 个 checkpoint**: ~175-210 min (3-3.5h)
- 按 val loss / F1 选 best checkpoint

### 磁盘空间
- `/root/autodl-tmp/`: 111GB 可用 (56% used)，充足

### Eval 脚本验证
- `eval_repo_cls.py` 存在，支持 `--split val`、`--checkpoint_dir`、`--model_name`、`--batch_size`、`--max_seq_length`、`--output_dir` 等参数，可直接使用

---
