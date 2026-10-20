# code no think fix eval

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_no-think-fix-eval_20260514T082030_result.json`
- **Structured JSON:** [`6de0bb34828473f819e9.json`](../../sessions/6d/6de0bb34828473f819e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，汇总：

### Dry-run 结果
| Sample | think | probe | len |
|--------|-------|-------|-----|
| 0 | False | True | 324 |
| 1 | False | True | 339 |
| 2 | False | True | 225 |
| 3 | False | True | 243 |
| 4 | False | True | 194 |

5/5 通过，no-think 修复生效。

### 评估任务
| Job | GPU | tmux session | 状态 |
|-----|-----|-------------|------|
| eval-sft-v1 | cuda:0 | eval-sft-v1 | 模型已加载，正在评估 202 样本 |
| eval-base-v2 | cuda:1 | eval-base-v2 | 模型加载中 |

### GPU 显存
- GPU 0: 17.2 GB / 97.9 GB (68% util)
- GPU 1: 16.4 GB / 97.9 GB (71% util)

---
