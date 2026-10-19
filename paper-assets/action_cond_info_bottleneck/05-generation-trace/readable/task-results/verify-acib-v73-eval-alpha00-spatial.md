# verify acib v73 eval alpha00 spatial

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_acib_v73_eval_alpha00_spatial_20260518T022650_result.json`
- **Structured JSON:** [`01046ef320b8188160bf.json`](../../sessions/01/01046ef320b8188160bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PASS** — 三项全部通过。

| 检查项 | 结果 |
|---|---|
| GPU 0 显存 | 5443 MiB 占用，PID 844027（eval 子进程）在 GPU 0 运行 |
| 日志 | 无 traceback/error。10 个 libero_spatial env 已构建完成，模型权重加载完毕（489/489），正在进入 eval |
| PID 844017 | 存活，wrapper bash 进程正常，实际 python 子进程 PID 844027 也在运行（CPU 564%） |

注意：GPU 1 上 PID 759167 是之前的 connector_only eval（α=0.0, 全 suite），仍在运行，互不冲突。

---
