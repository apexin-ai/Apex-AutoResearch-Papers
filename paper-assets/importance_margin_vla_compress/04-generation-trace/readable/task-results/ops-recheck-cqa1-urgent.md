# ops recheck cqa1 urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_recheck-cqa1-urgent_20260520T150718_result.json`
- **Structured JSON:** [`9adfc4208fdc4ed973da.json`](../../sessions/9a/9adfc4208fdc4ed973da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

## GPU 状态

| GPU | 显存 | 利用率 | 进程 | 状态 |
|-----|------|--------|------|------|
| **0** | 486MiB/24G | 1% | PID 132420 残留(type G) | **空闲** — k=0.7 seed44 已完成，115960 已退出 |
| **1** | 4540MiB/24G | 26% | PID 346216 (k=0.3 seed44) | **运行中**，33min |
| **2** | 4055MiB/24G | 0% | PID 132420 (k=0.5 seed44) | **运行中**，1h38m，进程状态 Rl |
| **3** | 4540MiB/24G | 49% | PID 344867 (k=0.3 seed43) | **运行中**，33min |

## 已完成实验

**k=0.7 seed44** — SR=**56.4%** (282/500), 95% CI [52.0%, 60.7%]
- 完成于 22:54，PID 115960 已退出，JSON 已写入

## 运行中实验（均无崩溃）

- **k=0.5 seed44** (GPU 2, PID 132420): 运行 1h38m，进程 Rl 状态正常。GPU util 瞬时 0% 可能是 episode 间歇。无 /tmp 日志（直接前台启动），无输出 JSON 说明尚未完成。
- **k=0.3 seed43** (GPU 3, PID 344867): 运行 33min，日志显示当前 task 在 Ep 25/50，FAIL 较多。
- **k=0.3 seed44** (GPU 1, PID 346216): 运行 33min，日志显示当前 task 在 Ep 24/50。

## 空闲 GPU

**GPU 0** — 可立即使用（仅有 PID 132420 的 473MiB 残留显存，不影响）。

---
