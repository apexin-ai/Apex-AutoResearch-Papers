# ops verify m96 train completion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_m96_train_completion_20260518T041233_result.json`
- **Structured JSON:** [`ea62cff072ffbb0b2ce2.json`](../../sessions/ea/ea62cff072ffbb0b2ce2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 session 没有 cron job，可能是在之前的 session 中创建的，已经不存在了。

## 汇报

- **M=96 train: success** — 100K steps 完成，"Training complete"，checkpoint 1.5GB 已保存。final loss=0.055, eval/action_loss=0.064
- **M=16 train: success** — 100K steps 完成，"Training complete"，checkpoint 1.5GB 已保存。final loss=0.058, eval/action_loss=0.069
- **M=96 eval: running** — PID 689462, GPU 1, 3377MiB 占用
- **M=16 eval: running** — PID 689541, GPU 2, 3000MiB 占用

Registry 已将两个训练实验更新为 DONE(success)。Cron 在当前 session 不存在，无需删除。

---
