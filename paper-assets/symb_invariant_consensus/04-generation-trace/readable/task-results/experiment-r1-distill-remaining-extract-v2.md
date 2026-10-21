# experiment r1 distill remaining extract v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r1-distill-remaining-extract-v2_20260521T155552_result.json`
- **Structured JSON:** [`7184e7535620a1172510.json`](../../sessions/71/7184e7535620a1172510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pipeline 进度：130/204，ETA ~70 分钟（约 01:08 UTC 完成）。**

汇总：
| 项目 | 状态 |
|------|------|
| R1-Distill vLLM (cuda:3, port 8003) | 运行中，PID 449110 |
| R1-Distill pipeline | 运行中，PID 451580，130/204，ETA ~70 min |
| Mistral (cuda:0, port 8000) | 运行中，PID 412714 |
| intermediates | 138/204 |
| per_trace_constraints_v2 | 93/204 已提取 |
| reextract_bpe_fix.py | 已修改，添加跳过已提取文件逻辑 |
| Mistral 模型路径 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3` |

**准备就绪，等 pipeline 跑完后执行：**
1. Kill R1-Distill vLLM + pipeline
2. 部署 Mistral on cuda:3 port 8004
3. 运行 `reextract_bpe_fix.py --api-base http://localhost:8004/v1` 补提取剩余 ~111 题

要我定时检查 pipeline 进度并自动执行后续步骤吗？

---
