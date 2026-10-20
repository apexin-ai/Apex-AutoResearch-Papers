# ops westd disk cleanup qwen25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526_result.json`
- **Structured JSON:** [`67f438445687f2b1a3f7.json`](../../sessions/67/67f438445687f2b1a3f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 清理结果
- 已删除 `pruned_graspune_20` + `sft_graspune_20`
- 数据盘剩余 **4.2GB** (99%)，两个新剪枝模型各占 ~11GB

## Qwen Math 25% 剪枝统计

| | RASP 25% | Standard 25% |
|---|---|---|
| MLP groups pruned | 252 / 784 | 251 / 784 |
| Attn GQA groups pruned | 0 / 112 | 0 / 112 |
| Target sparsity | 25.00% | 25.00% |
| **Actual sparsity** | **24.05%** | **23.96%** |
| Pruned params | 5,783,991,808 | ~5,790M |
| 输出路径 | `pruned_rasp_25_qwen_math` | `pruned_standard_25_qwen_math` |

两个模型均通过 forward pass validation，包含 `model.safetensors` + tokenizer + config。

⚠️ 数据盘仅剩 4.2GB，后续 SFT 训练前需要清理更多空间。

---
