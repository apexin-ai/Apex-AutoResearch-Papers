# code dpo train config r2

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-train-config-r2_20260513T162104_result.json`
- **Structured JSON:** [`d5edb742b1c3e9d0e9f4.json`](../../sessions/d5/d5edb742b1c3e9d0e9f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报：

---

**1. 脚本路径**: `/root/autodl-tmp/prov_grounded_uie/src/train_dpo.py`

**2. 关键超参选择**:

| 参数 | 值 | 理由 |
|---|---|---|
| `learning_rate` | 5e-7 | DPO 需要比 SFT (2e-4) 低 2-3 个数量级，防止 policy 偏移过大 |
| `beta` | 0.1 | 标准 DPO 起步值，控制 KL 惩罚强度 |
| `lora_rank` | 64, alpha=128 | 比 v1 (r=32) 更大，给 DPO 更多容量学习偏好信号 |
| `gradient_accumulation_steps` | 4 | 单卡有效 batch=8，足够稳定 |
| `max_length` | 2048 | 与候选生成时一致 |
| `max_prompt_length` | 1536 | 留 512 tokens 给 response |
| `num_train_epochs` | 1 | DPO 数据量小 (981 pairs)，多 epoch 易过拟合 |

**3. Dry-run 验证**: `--help` 正常，数据加载正确 (981 pairs, 3 列 prompt/chosen/rejected，格式匹配 TRL DPOTrainer)

**4. 单卡/双卡建议**:
- **单卡**: `python src/train_dpo.py` — model (~16GB bf16) + ref_model (~16GB) + LoRA + optimizer ≈ 40-50GB，96GB 单卡富余
- **双卡**: `accelerate launch --num_processes 2 src/train_dpo.py` — 有效 batch 翻倍到 16，训练更快。建议先单卡跑通确认 loss 正常下降，再切双卡

**vs v1 (`train_dpo.py`) 改进**: 多文件加载、wandb logging、margin 过滤、训练后自动 merge、lr 从 5e-6 降到 5e-7、LoRA rank 从 32 升到 64

---
