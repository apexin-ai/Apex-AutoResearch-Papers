# ops verify eval gpu status

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-eval-gpu-status_20260516T061507_result.json`
- **Structured JSON:** [`c059dcb97e9881e41e0c.json`](../../sessions/c0/c059dcb97e9881e41e0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**4 个 eval 全部存在且正常运行，无需重启。**

| Session | GPU | PID | 进度 | 状态 |
|---------|-----|-----|------|------|
| eval-rp-s0 | cuda:1 | 240920 | 25/47 (53%) | 运行中，CPU 115% |
| eval-rp-s123 | cuda:2 | 241056 | 29/47 (62%) | 运行中，CPU 113% |
| eval-rp-s1 | cuda:3 | 241193 | 26/47 (55%) | 运行中，CPU 119% |
| eval-rp-s42 | cuda:0 | — | 未开始 | 等待 PID 239377 (`analyze_failure_modes_5seed.py --condition vanilla`) 完成后自动启动 |

**GPU 使用**：
| GPU | Util | 显存占用 |
|-----|------|---------|
| 0 | 87% | 17091/32607 MiB（failure analysis 脚本） |
| 1 | 65% | 17091/32607 MiB（eval-rp-s0） |
| 2 | 84% | 17091/32607 MiB（eval-rp-s123） |
| 3 | 0%* | 17091/32607 MiB（eval-rp-s1） |

*GPU 3 utilization 瞬时为 0%，但进程在跑（119% CPU），属正常波动。

**eval-rp-s42** 的 tmux session 里有 wait loop（`while kill -0 239377; do sleep 10; done`），一旦 GPU 0 上的 failure analysis 跑完就会自动启动 eval。无需人工干预。

---
