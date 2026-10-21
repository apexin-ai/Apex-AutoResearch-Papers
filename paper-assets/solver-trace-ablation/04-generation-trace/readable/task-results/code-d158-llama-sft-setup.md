# code d158 llama sft setup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d158-llama-sft-setup_20260520T144202_result.json`
- **Structured JSON:** [`c89db98eedd7b8c86b81.json`](../../sessions/c8/c89db98eedd7b8c86b81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行：

- **总步数**: 189 步 (500 examples / 8 effective batch * 3 epochs)
- **速度**: ~1.07s/step → 预计 **~3.5 分钟**完成
- **显存**: 34.8 GB / 97.9 GB (cuda:0)
- **GPU 利用率**: 98%

## 汇总

| 项目 | 结果 |
|------|------|
| **模型** | `/root/autodl-tmp/models/Llama-3.2-3B` (base, 有 chat template) |
| **GPU** | cuda:0 (仅 1 张 RTX PRO 6000 97GB，无 cuda:1) |
| **SFT 脚本** | `scripts/train_sft.py` (已有，加了 cosine scheduler) |
| **数据** | `data/train_500_seed42.jsonl` (500 examples, C001 合规) |
| **Tokenizer** | FOL Unicode 符号 (∀, ∃, →, ∧, ¬) 全部正确 round-trip |
| **Dry-run** | Loss 2.0→1.35 (3步), token acc 62%→73%, 模型能学 |
| **训练配置** | 3 epochs, lr=2e-5, cosine, batch=4, grad_accum=2, bf16, seed=42 |
| **输出目录** | `/root/autodl-tmp/outputs/d158_llama_sft_s42/` |
| **W&B** | 服务器无 API key，已禁用 |
| **预计完成** | ~3.5 分钟 |

**注意**: 任务要求用 cuda:1，但服务器只有 1 张 GPU (cuda:0)。已改用 cuda:0。

---
