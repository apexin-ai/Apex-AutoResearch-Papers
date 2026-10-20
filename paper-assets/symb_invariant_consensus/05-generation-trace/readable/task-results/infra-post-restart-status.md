# infra post restart status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_post-restart-status_20260522T020854_result.json`
- **Structured JSON:** [`96155d45568b808c6b94.json`](../../sessions/96/96155d45568b808c6b94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16639 状态汇报

### FOLIO 2×2 Master Script (PID 495418, 运行 ~2h30m)

**Phase 1 — 完成** (10:11)
| 任务 | 进度 | 状态 |
|------|------|------|
| Cell A (Mistral→Mistral) | 204/204 | done (08:10 完成) |
| Qwen3 traces (k=12) | 204/204 | done (traces 08:38 完成, mvp 进程 10:11 退出) |

注意：mvp 进程在 traces 全部完成后又多跑了 ~1.5h 才退出（可能在做 constraint 聚合），导致 Phase 1 到 10:11 才结束。

**Phase 2 — 刚启动** (10:11)
| Cell | 方向 | PID | 进度 |
|------|------|-----|------|
| Cell B | Mistral gen → Qwen3 ext | 504508 | 0/204 (刚开始) |
| Cell C | Qwen3 gen → Mistral ext | 504509 | 0/204 (刚开始) |
| Cell D | Qwen3 gen → Qwen3 ext | — | 等待 B+C 完成 |
| Metrics | — | — | 等待 B+C+D 完成 |

### Qwen3-14B 单模型结果 (已出)
- **SICA accuracy: 84.8%** (173/204)
- **SC accuracy: 83.3%** (170/204)
- k=12, wall time ~3h

### GPU 状态
| GPU | 显存 | 利用率 | 用途 |
|-----|------|--------|------|
| 0 | 90207 MiB | 97% | Qwen3-14B vLLM (port 8001) |
| 1 | 0 MiB | 0% | 空闲 |
| 2 | 0 MiB | 0% | 空闲 |
| 3 | 89811 MiB | 0% | Mistral-7B vLLM (port 8004) |

### westd-25068
**连接失败** — Authentication failed。服务器重启后 SSH 端口大概率已变更，需去 AutoDL 控制台查看新端口并更新 `~/.ssh/config`。

---
