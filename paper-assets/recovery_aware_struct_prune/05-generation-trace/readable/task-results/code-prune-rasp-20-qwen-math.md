# code prune rasp 20 qwen math

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prune_rasp_20_qwen_math_20260516T080223_result.json`
- **Structured JSON:** [`b76e19edb3fead746f50.json`](../../sessions/b7/b76e19edb3fead746f50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen2.5-Math-7B 剪枝已完成，两个实验均已在 registry 标记为 DONE。

**结果汇总：**

| | RASP (α=1.0) | Standard |
|---|---|---|
| 实际 sparsity | 18.99% | 19.28% |
| 参数 7.62B → | 6.17B | 6.15B |
| MLP groups pruned | 199 | 202 |
| Attn groups pruned | 0 | 0 |
| 输出路径 | `pruned_qwen_math_rasp_20/` | `pruned_qwen_math_standard_20/` |
| 服务器 | westd-11672 | westd-11672 |

注意：与 DeepSeek 模型类似，两种方法都只剪 MLP 通道，不剪 attention heads（Qwen2.5-Math-7B 只有 4 个 KV heads，GQA group 粒度较粗）。RASP 的非均匀 MLP 剪枝清晰可见——`per_layer_intermediate_size` 范围从 8128 到 18944（原始 18944），早期和最后层剪得最多，中间层保留更多通道。

---
