# code openhands fewshot probe

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openhands-fewshot-probe_20260514T122155_result.json`
- **Structured JSON:** [`3fe59ecf35b5bff3156e.json`](../../sessions/3f/3fe59ecf35b5bff3156e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本 `finetune_cross_agent.py` 已写入服务器并通过 dry-run 验证。

**Dry-run 结果 (--epochs 1 --train_fraction 0.1)**：

| 指标 | Zero-shot | Fine-tuned (1 epoch) |
|------|-----------|---------------------|
| macro-F1 | 0.5284 | 0.4781 |
| accuracy | 0.7709 | 0.6366 |
| f1_stagnation | 0.1902 | 0.1905 |
| f1_progress | 0.8666 | 0.7657 |

1 epoch 尚未收敛（正常），完整训练 10 epoch 预期会明显提升。

**脚本功能**：
- 加载 SWE-agent 预训练 checkpoint，在 OpenHands 数据上 fine-tune
- 按 trajectory_id 做 70/15/15 split，test set 固定
- `--train_fraction` 按 trajectory 粒度 subsample（保持 trajectory 完整性）
- pos_weight 自动计算处理 6.6% stagnation 不平衡
- 输出 JSON 结果到 `results/finetune_cross_agent_{fraction}.json`
- 每个 fraction 保存 best checkpoint 到 `checkpoints_finetune_{fraction}/`

**运行示例**：
```bash
python finetune_cross_agent.py --train_fraction 0.1 --epochs 10
python finetune_cross_agent.py --train_fraction 0.2 --epochs 10
python finetune_cross_agent.py --train_fraction 0.5 --epochs 10
python finetune_cross_agent.py --train_fraction 1.0 --epochs 10
```

---
