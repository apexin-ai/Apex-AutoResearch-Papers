# ssh westd phase2 progress check v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-progress-check-v3_20260519T120039_result.json`
- **Structured JSON:** [`3cdfb25fdf99525a2e75.json`](../../sessions/3c/3cdfb25fdf99525a2e75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 2 状态总览 (20:01 CST)

### GPU 分配

| GPU | Util | Mem | 任务 |
|-----|------|-----|------|
| 0 | 95% | 31.7/97.9 GB | **phi4_d100** eval (PID 161497, since 19:49) |
| 1 | 94% | 32.7/97.9 GB | **qwen14b_d100** eval (PID 163254, since 19:56) |
| 2 | 90% | 16.7/97.9 GB | **olmo2_d100** eval (PID 162317, since 19:55) |
| 3 | **idle** | 0 MB | 空闲 |

### 25-cell 状态表

| Model | d000 | d005 | d025 | d050 | d100 |
|-------|------|------|------|------|------|
| **gemma2** | 0.6186 / 0.8601 | 0.6342 / 0.7782 | 0.6456 / 0.8737 | 0.6401 / 0.7108 | 0.6562 / 0.8481 |
| **phi4** | 0.7644 / 0.9206 | 0.7636 / 0.9181 | 0.7698 / 0.9232 | 0.7675 / 0.9241 | **RUNNING** (GPU0) |
| **qwen14b** | 0.6944 / 0.9104 | 0.6901 / 0.9036 | 0.6204 / 0.8891 | 0.5941 / 0.8763 | **RUNNING** (GPU1) |
| **qwen7b** | 0.6611 / 0.8788 | 0.6474 / 0.8609 | 0.6298 / 0.8404 | 0.6307 / 0.8456 | 0.6433 / 0.8498 |
| **olmo2** | MISSING | MISSING | MISSING | MISSING | **RUNNING** (GPU2) |

(格式: MMLU / ARC)

### 进展汇总

- **DONE**: 20/25 (上次 16/25, 新完成 4: phi4_d050, qwen14b_d050, qwen7b_d050, qwen7b_d100)
- **RUNNING**: 3/25 (phi4_d100, qwen14b_d100, olmo2_d100)
- **MISSING**: 4/25 (olmo2_d000/d005/d025/d050)
- **GPU 3 空闲**

### OLMo Monitor

- tmux sessions: `olmo2_gpu2` (19:55), `olmo2_monitor` (19:59)
- monitor 日志只有 1 轮 check (19:59:26)，GPU0/1 busy 所以未启动新任务，正在 sleep 120s
- olmo2_d100 已在 GPU2 上运行，monitor 在等 GPU0/1 空闲后启动 olmo2_d000~d050

### 下一步预期

phi4_d100 跑了 ~11min (19:49 start)，qwen14b_d100 ~5min (19:56 start)，olmo2_d100 ~6min (19:55 start)。根据前面 eval 耗时，预计各需 15-25 分钟。GPU0 最先释放后 monitor 应自动启动 olmo2 d000~d050 的 eval。

---
