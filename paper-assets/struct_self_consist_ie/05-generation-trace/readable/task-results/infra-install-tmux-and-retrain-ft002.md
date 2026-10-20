# infra install tmux and retrain ft002

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_install_tmux_and_retrain_ft002_20260514T080436_result.json`
- **Structured JSON:** [`fb7311cc2bbaf250c46d.json`](../../sessions/fb/fb7311cc2bbaf250c46d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。报告如下：

| 项目 | 状态 |
|------|------|
| **tmux** | 已安装，版本 3.2a |
| **v2 checkpoint** | 已清理，checkpoints/ 下仅剩 `ft_001_train.log`、`qwen3-8b-scierc-lora`、`qwen3-8b-scierc-merged` |
| **GPU** | 4× 32GB（5090），GPU 0/1/2 空闲（0% util, 2MiB used），GPU 3 utilization 100% 但显存仅 2MiB |

**train_config_v2.yaml 摘要：**
- 模型：Qwen3-8B，LoRA (rank=32, alpha=64, target=all)
- 数据：scierc_uie_train / scierc_uie_dev
- 训练：batch=4, grad_accum=4, lr=2e-4, 5 epochs, cosine scheduler, bf16
- 输出：`checkpoints/qwen3-8b-scierc-lora-v2`

GPU cuda:1 空闲可用，可以提交训练。

---
