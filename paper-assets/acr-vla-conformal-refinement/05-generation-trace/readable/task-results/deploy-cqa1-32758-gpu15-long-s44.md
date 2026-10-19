# deploy cqa1 32758 gpu15 long s44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-32758-gpu15-long-s44_20260523T144351_result.json`
- **Structured JSON:** [`bae0f4755e5a26bff757.json`](../../sessions/ba/bae0f4755e5a26bff757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

| 实验 | GPU | PID | tmux session | 状态 |
|------|-----|-----|-------------|------|
| `eval-supp-long-adapt-tau025-s44` | 1 | 291315 | eval-supp-long-adapt-tau025-s44 | RUNNING |
| `eval-supp-long-crm-norm005-s44` | 5 | 291523 | eval-supp-long-crm-norm005-s44 | RUNNING |

注意：任务给的命令用 `python evaluate.py`，实际路径是 `src/evaluate.py`，已修正。两个进程正在加载 SmolVLA 模型，预计几分钟后开始 rollout。

---
