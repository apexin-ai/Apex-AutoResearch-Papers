# ops multi server status collect

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_multi-server-status-collect_20260521T032206_result.json`
- **Structured JSON:** [`25bbdf2084ade7b2fafc.json`](../../sessions/25/25bbdf2084ade7b2fafc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-27271
- **M128 eval (object, cuda:0)**: Task 1/10, Ep 2/50 — just started today 11:01, running normally
  - (vtconly_20k eval: dead — stuck at Task 0 Ep 3/50 since yesterday 16:02, no longer running)
- **M32 VTC train (cuda:1)**: step 40,650/100,000 (40.7%), loss ~2.5, 0.5 sps

## westd-41074
- **OpenVLA random k=0.5 eval (cuda:0)**: Task 1/10, Ep 30/50, SR=0/30 (0%) — very slow progress, 6.3 eps/min
- **M96 train (cuda:2)**: step 41,200/100,000 (41.2%), loss ~2.8-3.1, 0.5 sps
- **M64 v4 train (cuda:3)**: **CRASHED** at step 50,000/100,000 — `RuntimeError: PytorchStreamWriter failed writing file` during checkpoint save (disk write failure). GPU 3 still holds 27GB memory but 0% util (zombie process).

## westd-38929
- **random k=0.95 v2 (cuda:0)**: Task 10/10, Ep 10/50 — nearly done
  - Completed task SRs: [80%, 42%, 70%, 42%, 88%, 84%, 60%, 68%, 66%]
- **random k=0.7 v2 (cuda:1)**: Task 9/10, Ep 10/50
  - Completed task SRs: [72%, 20%, 56%, 38%, 64%, 52%, 20%, 24%]
- (cuda:2 和 cuda:3 也在跑东西，未查)

## cqa1
- **random k=0.9 (xvla, cuda:0)**: **已完成**, Overall SR=97.8% (489/500), CI=[96.1%, 98.8%]
  - per_task=[96%, 100%, 100%, 94%, 100%, 94%, 100%, 98%, 96%, 100%]
  - 耗时 50.4 min, GPU 0 已空闲

---

**需要关注**: westd-41074 上 M64 v4 训练在 step 50K 处 crash 了（磁盘写入失败），需要清理磁盘空间并 resume。

---
