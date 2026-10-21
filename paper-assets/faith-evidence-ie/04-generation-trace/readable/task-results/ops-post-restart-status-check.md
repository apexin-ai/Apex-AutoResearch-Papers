# ops post restart status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post_restart_status_check_20260519T174019_result.json`
- **Structured JSON:** [`a031c1c208d64e3fef4d.json`](../../sessions/a0/a031c1c208d64e3fef4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个进程全部存活：

| 实验 | PID | GPU | 运行时长 | 状态 |
|------|-----|-----|---------|------|
| plan017_14b_rsft_generate | 712685 | cuda:0+cuda:2 | 6m46s | **ALIVE** |
| d112_rsft_no_evidence_eval_r3 | 706326 | cuda:1 | 1h53m | **ALIVE** |
| plan019_1_7b_rsft_no_evidence_eval_2048 | 702837 | cuda:3 | 2h51m | **ALIVE** |

GPU 显存占用与预期一致：GPU0 16GB、GPU1 11GB、GPU2 18GB、GPU3 7GB，均在工作中。服务重启未影响任何实验进程。

---
