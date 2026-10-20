# ops eval queue prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-queue-prep_20260514T210747_result.json`
- **Structured JSON:** [`48c83fb3cac51cbd07ca.json`](../../sessions/48/48c83fb3cac51cbd07ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

kl001 multi-eval 已完全停止。

**汇总：**

| 项目 | 状态 |
|------|------|
| **脚本 1** | `/root/autodl-tmp/scripts/eval_lr5e6_rp_ckpt20.sh` ✓ |
| **脚本 2** | `/root/autodl-tmp/scripts/eval_lr5e6_ckpt40.sh` ✓ |
| **Watcher** | PID 100154，已完成执行。额外手动 kill 了孤儿进程 PID 99616（kl001 ckpt-40 inference） |
| **rp_r2 当前 step** | **27/200**（~1:01:08 elapsed，约 112s/step） |
| **P0 ckpt-40** | **EXISTS** ✓ |

当前 GPU 占用：
- **cuda:0** — rp_r2 训练（PID 94758，step 27/200）
- **cuda:1** — P0 ckpt-20 eval 正在运行（PID 96500）
- **cuda:2** — 空闲（kl001 已被停止）
- **cuda:3** — 空闲

---
