# code pre verify preparing exps

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pre-verify-preparing-exps_20260515T154921_result.json`
- **Structured JSON:** [`50e1444dcb667d7441de.json`](../../sessions/50/50e1444dcb667d7441de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

| 实验 | 就绪 | 问题 |
|------|------|------|
| plan002-additive-b01-s43-r2 | **NO** | 配置文件名错误 |
| plan018-additive-random-b01-s44-r2 | YES | — |
| plan018-additive-random-b01-s43-r3 | YES | — |

### 阻塞问题：plan002 配置文件不存在

`configs/grpo_additive_b01.yaml` 不存在。实际文件是 **`configs/grpo_additive_bonus_b01.yaml`**，其 `reward_mode: additive_bonus`。

修正后的提交命令：
```bash
python3 scripts/train_grpo.py \
  --config configs/grpo_additive_bonus_b01.yaml \
  --data_path data/train_500_seed42.jsonl \
  --num_steps 500 --seed 43 --beta 0.1 \
  --reward_mode additive_bonus \
  --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43_r2
```

### 通过项

- **磁盘**：root 21GB / data 204GB，充足
- **Python 环境**：torch=2.10.0+cu128, transformers=4.57.6, trl=1.1.0
- **基座模型**：Qwen3-4B 存在
- **数据文件**：train_500_seed42.jsonl 500 行
- **输出目录**：3 个均不存在，无冲突
- **当前训练**：PID 363692 (GPU0) 和 363840 (GPU1) 均在运行，已跑约 2 小时

---
