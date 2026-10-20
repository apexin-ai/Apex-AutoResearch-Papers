# train sft mvp

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_sft-mvp_20260514T062107_result.json`
- **Structured JSON:** [`9d486fa2b183daba1b38.json`](../../sessions/9d/9d486fa2b183daba1b38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT 训练已完成。汇总：

## 同步文件
- **代码**: 8 个 .py 文件 (src/ 目录, 含额外发现的 validate_tests.py)
- **数据**: probes_train.jsonl (294 条), eval.jsonl (202 条) — 通过 scp 传输

## 模型路径
`/root/autodl-tmp/models/Qwen/Qwen3-8B`

## 训练结果
- **总步数**: 57 steps, 3 epochs
- **总耗时**: 176.6 秒 (~3 分钟)
- **GPU**: cuda:0, 56GB 显存使用 (RTX PRO 6000 Blackwell 94GB)

### Loss 曲线
| Step | Loss | Token Accuracy | Epoch |
|------|------|---------------|-------|
| 10 | 2.133 | 0.616 | 1.05 |
| 20 | 1.803 | 0.630 | 1.59 |
| 30 | 1.649 | 0.645 | 2.11 |
| 40 | 1.550 | 0.654 | 2.65 |
| **Avg** | **1.871** | **0.662** | **3.0** |

## Checkpoint
`/root/autodl-tmp/diagprobe/checkpoints/sft/` — LoRA adapter (174MB) + tokenizer

## 修复的问题
1. `eval.jsonl` 缺少 `good_probe` 字段 — 添加字段检查，跳过不兼容的 eval 数据
2. trl 1.1.0 的 `SFTConfig` 参数 `max_seq_length` → `max_length`
3. wandb 未登录 — 跳过 wandb logging

---
