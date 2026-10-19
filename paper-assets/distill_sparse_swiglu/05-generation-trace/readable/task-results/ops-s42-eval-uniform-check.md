# ops s42 eval uniform check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s42-eval-uniform-check_20260519T132100_result.json`
- **Structured JSON:** [`2da06e42e570420e0e40.json`](../../sessions/2d/2da06e42e570420e0e40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果**：`qwen14b_kl30_s42_eval_uniform` **失败**，已在 registry 标记。

| 指标 | 状态 |
|------|------|
| WikiText-2 PPL | 7.6318 (成功计算但未持久化) |
| arc_challenge | 未运行 |
| winogrande | 未运行 |
| hellaswag | 未运行 |
| piqa | 未运行 |
| mmlu | 未运行 |

**失败原因**：服务器网络中断 (`[Errno 101] Network is unreachable`)，lm-eval 无法从 HuggingFace 下载 arc_challenge 数据集。脚本在 lm-eval 阶段崩溃，results.json 未写入。

**重跑建议**：重跑前需确保 westd-34887 网络恢复，或提前将 lm-eval 所需数据集缓存到本地。

---
