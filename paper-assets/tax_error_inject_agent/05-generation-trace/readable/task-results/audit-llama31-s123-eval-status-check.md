# audit llama31 s123 eval status check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_llama31-s123-eval-status-check_20260516T150700_result.json`
- **Structured JSON:** [`1b554bc00b5a1d8605ba.json`](../../sessions/1b/1b554bc00b5a1d8605ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Duplicate process (PID 293905) is already dead — no conflict. All 4 GPUs now fully loaded. Here's the full status:

---

## GPU 状态

| GPU | Memory | Utilization | Process |
|-----|--------|-------------|---------|
| 0 | 16837 MiB | 89% | taxei-s123 injected (PID 293496) |
| 1 | 16837 MiB | 88% | vanilla-s123 injected (PID 290182) |
| 2 | 16837 MiB | 88% | taxei-s123 clean (PID 291995) |
| 3 | 16837 MiB | 88% | random-s123 clean (PID 292353) |

## s123 Eval 汇总

| Eval | 文件状态 | 进程状态 | 结果 |
|------|---------|---------|------|
| vanilla-s123 clean | EXISTS (15840B) | DONE | **72.3%** |
| vanilla-s123 injected | MISSING (log only) | RUNNING PID 290182, 30/47 | ~60% done |
| taxei-s123 clean | MISSING | RUNNING PID 291995 | just started |
| taxei-s123 injected | MISSING | RUNNING PID 293496, 1/47 | just started |
| random-s123 clean | MISSING | RUNNING PID 292353 | just started |
| random-s123 injected | **MISSING** | **NOT RUNNING** | — |

## 问题

1. **`random-s123-injected` 未启动** — 没有进程、没有文件、没有 log。所有 4 张 GPU 已被占满，需要等当前某个 eval 完成后才能启动。
2. 已死的 screen session 进程 (PID 293905) 曾尝试重复写 `vanilla_s123_injected.json`，已自行退出（EXIT_CODE=137, OOM killed），不影响当前运行的 PID 290182。

## 预估进度

- `vanilla-s123 injected`: 30/47 episodes, 预计 ~10-15 min 内完成
- `taxei/random clean` + `taxei injected`: 刚启动，预计 ~25-40 min
- **`random-s123-injected` 需要手动启动**，最早在 vanilla-injected 完成释放 GPU 后

---
