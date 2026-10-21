# deploy bjb2 40593 kill dup deploy k2mean

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-40593-kill-dup-deploy-k2mean_20260523T225813_result.json`
- **Structured JSON:** [`1c8e776822f682f4757c.json`](../../sessions/1c/1c8e776822f682f4757c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

| 操作 | 结果 |
|------|------|
| Kill PID 201029 (重复 adapt-s45) | force_killed, tmux session 已清理 |
| GPU 释放 | cuda:0 → 0 MiB |
| 部署 k2mean-s45 | PID 204339, tmux `eval-spatial-k2mean-s45`, 模型加载中 |
| Registry: `eval-supp-spatial-adapt-tau025-s45` | status=DONE, conclusion=killed |
| Registry: `eval-supp-spatial-k2mean-s45` | status=RUNNING, server=bjb2-40593, gpu=cuda:0 |

---
