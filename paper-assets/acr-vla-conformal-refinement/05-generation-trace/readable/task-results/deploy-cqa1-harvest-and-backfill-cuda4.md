# deploy cqa1 harvest and backfill cuda4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-harvest-and-backfill-cuda4_20260523T183429_result.json`
- **Structured JSON:** [`3f5844a6ac3528658e98.json`](../../sessions/3f/3f5844a6ac3528658e98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 结果

| # | 项目 | 状态 |
|---|------|------|
| 1 | **Long K2mean s42** | SR = **0.57** (DONE) |
| 2 | **Long VLA-only s43** | SR = **0.595** (DONE) |
| 3 | **CRM checkpoint SCP** | 成功，MD5 = `4161c6403b8eb268864b99dd986be784` |
| 4 | **Object Reconvla s45** | PID **377316**, cuda:4 RUNNING, tmux session `eval-reconvla-obj-s45` |

## Registry 更新

- `eval-supp-long-k2mean-s42` → DONE, metrics={SR: 0.57}
- `eval-supp-long-vla-only-s43` → DONE, metrics={SR: 0.595}
- `eval-supp-reconvla-obj-s45` → RUNNING, cqa1-32758 cuda:4

---
