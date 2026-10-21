# audit cqa1 deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1_deploy_20260527T104755_result.json`
- **Structured JSON:** [`033d0b939beb1716ff01.json`](../../sessions/03/033d0b939beb1716ff01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1 审计结果

| GPU | 实验 | PID | 进度 | 预计剩余 |
|-----|------|-----|------|----------|
| 0 | π0.5 Random k=0.7 strict v2 | 109152 | T5 done, 210/300=70.0%, 145min | ~2h |
| 1 | π0.5 Random k=0.5 strict | 118726 | T4 done, 163/250=65.2%, 131min | ~2.5h |
| 2 | π0.5 L2norm k=0.85 strict | 93525 | T7 进行中 (ep30), 273/350=78.0%, 157min | ~1.5h |
| 3 | π0.5 L2norm k=0.9 strict | 200112 | T0 ep40, 38/40=95%, 刚启动 | ~4-5h |

**结论：全部 4 GPU 在跑，无空闲 GPU。**

- GPU1 (Random k=0.5) 未完成，部署条件不满足
- GPU3 (L2norm k=0.9) 成功启动并在运行，部署条件不满足

**最早释放：GPU2 ~1.5h 后（约 UTC 20:15）**。GPU2 释放后可部署 L2norm k=0.75 strict；GPU0/GPU1 之后释放可部署 L2norm k=0.7 strict。

需要我设置定时轮询，GPU 释放后立即部署吗？

---
