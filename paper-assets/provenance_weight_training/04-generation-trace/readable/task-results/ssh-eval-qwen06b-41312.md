# ssh eval qwen06b 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_qwen06b_41312_20260517T224228_result.json`
- **Structured JSON:** [`0319a9d39fec58298772.json`](../../sessions/03/0319a9d39fec58298772.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。汇报如下：

## 结果

| 项目 | 值 |
|------|-----|
| **Checkpoint 路径** | `/root/autodl-tmp/provenance_weight_training/output/models/qwen06b_uniform_seed42_v2/final` |
| **GPU 状态** | cuda:0 空闲（eval 前 0MiB），GPU 1-3 被其他训练占用 |
| **Perplexity** | **17.694** |
| **Loss** | 2.8733 |
| **Tokens 评估** | 4,077,068 |
| **耗时** | 137s |
| **状态** | 成功完成 |

PPL = 17.694，与预期 ≈ 17.694 完全吻合。

注意：实际路径是 `qwen06b_uniform_seed42_v2`（带 `_v2` 后缀），没有无后缀的 `qwen06b_uniform_seed42` 目录。结果已保存到 `/root/provenance_weight_training/output/eval_qwen06b_uniform_seed42.json`。

---
