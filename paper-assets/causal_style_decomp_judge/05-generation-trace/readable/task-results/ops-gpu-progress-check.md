# ops gpu progress check

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_progress_check_20260521T005741_result.json`
- **Structured JSON:** [`e98ba3b9630dbee172a9.json`](../../sessions/e9/e98ba3b9630dbee172a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 100% | 88.3/97.9 GB |
| 1 | 100% | 88.4/97.9 GB |
| 2 | 0% | 空闲 |
| 3 | 100% | 0 MB（无进程，可能是驱动残留） |

### 任务进度

**1. Register CF gen (GPU 0, port 8000)**
- 进程运行中 (PID 86609, 08:50 启动)
- 进度：**35/100** (最后处理 mvp_0034)
- 速度 ~4.4 样本/min，预计还需 ~15 min

**2. AlpacaEval benchmark CF gen (GPU 1, port 8001)**
- 进程运行中 (PID 86702, 08:51 启动)
- 进度：**32/100** (最后处理 alpacaeval_030，formal axis)
- 速度 ~4.6 样本/min，预计还需 ~15 min

**3. Exp-013 NLI validation (共用 GPU 1 的 vLLM)**
- 进程运行中 (PID 87285, 08:54 启动)
- 进度：**84/100** (mvp_0083)
- 绝大多数 NLI pass (>0.95)，偶有 DISAGREE (如 mvp_0066 nli=0.1085)
- 预计 ~1-2 min 完成

**注意**：GPU 2 完全空闲，三个任务只用了 GPU 0 和 GPU 1。Exp-013 和 AlpacaEval CF gen 共享同一个 vLLM server (port 8001)，可能互相影响吞吐。

---
