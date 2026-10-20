# ops check gpu2 pid553256 alive

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu2-pid553256-alive_20260515T122536_result.json`
- **Structured JSON:** [`e9822fe716b4b5ef900c.json`](../../sessions/e9/e9822fe716b4b5ef900c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
PID 553256 (0.5B base eval v2): ALIVE — 运行 54m55s, cuda:2 占用 3612 MiB
PID 555931 (3B d005 s123 SFT):  ALIVE — 运行 27m27s, CUDA_VISIBLE_DEVICES=2, 子进程 555936 占用 19316 MiB
PID 556011 (3B d025 s123 SFT):  ALIVE — 运行 27m25s, CUDA_VISIBLE_DEVICES=4, 子进程 556016 占用 19280 MiB
```

**cuda:2 进程列表：**
| PID | 显存 | 任务 |
|-----|------|------|
| 553256 | 3612 MiB | 0.5B base pretrained eval v2 |
| 555936 | 19316 MiB | 3B d005 s123 SFT (父进程 555931) |

**cuda:4 进程列表：**
| PID | 显存 | 任务 |
|-----|------|------|
| 556016 | 19280 MiB | 3B d025 s123 SFT (父进程 556011) |

**结论：cuda:2 存在冲突。** 两个任务共享 cuda:2，合计占用约 22.9 GB 显存。这是 C001 违规——3B SFT 提交前未检查 cuda:2 上已有 0.5B eval 在跑。Director 命令禁止 kill PID 553256，所以需要决策：kill 3B SFT (555931) 并重新调度到空闲 GPU，还是等 0.5B eval 自然结束。

---
