# ops m2 embed verify hang fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m2-embed-verify-hang-fix_20260513T062356_result.json`
- **Structured JSON:** [`543e1acc9cfc9c77e037.json`](../../sessions/54/543e1acc9cfc9c77e037.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练正常运行！**

`random_s42.log` 输出了第一个训练步日志：

```
step 50  loss=0.5669  lr=6.10e-06
```

## 总结

| 项目 | 值 |
|------|------|
| **诊断** | 原始进程 (PID 23729) 双重问题：(1) batch_size=8 + num_negatives=7 导致 50GB 显存占用过高；(2) Python stdout 通过 `tee` 管道 block-buffered，日志不可见 |
| **修复** | batch_size 8→4, num_negatives 7→5, 添加 `PYTHONUNBUFFERED=1` |
| **当前 PID** | 29302 (tmux session: m2_embed_verify) |
| **GPU 1 状态** | 95% util, 22GB VRAM（之前 50GB → 大幅下降） |
| **训练状态** | step 50, loss=0.5669, lr=6.10e-06，正常训练中 |
| **额外清理** | 杀掉了残留 wrapper 进程树 (PID 27797 及子进程)，之前 kill 单个 Python 进程后 wrapper 继续执行了后续 strategy |

---
