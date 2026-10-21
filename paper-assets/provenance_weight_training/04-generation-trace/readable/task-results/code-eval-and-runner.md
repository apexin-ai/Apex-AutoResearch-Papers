# code eval and runner

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_and_runner_20260513T174428_result.json`
- **Structured JSON:** [`8ab7add20c2236b6b57a.json`](../../sessions/8a/8ab7add20c2236b6b57a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件已创建并验证：

| 文件 | 状态 |
|---|---|
| `evaluation/eval_pipeline.py` | 语法正确，含 perplexity（sliding window）、lm-eval-harness、生成质量（Self-BLEU + Distinct-n）三类评估 |
| `evaluation/compare_results.py` | argparse 正常，读取多方法 eval_results.json，输出对比表 + MVP pass 判定（adaptive ≥ 90% grid improvement） |
| `run_mvp.sh` | `--help` 正常，7步流程串联，支持中间步骤跳过恢复，`chmod +x` 已设置 |

---
