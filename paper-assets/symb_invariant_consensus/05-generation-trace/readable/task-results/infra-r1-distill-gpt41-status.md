# infra r1 distill gpt41 status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_r1-distill-gpt41-status_20260521T145512_result.json`
- **Structured JSON:** [`e8ede443bc90b5e56ec7.json`](../../sessions/e8/e8ede443bc90b5e56ec7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. R1-Distill 修复状态 ✅ 已修复

- **旧 PID 441147**: 已消失
- **新 vLLM (PID 449110)**: cuda:3 上运行，端口 8003，模型 `DeepSeek-R1-Distill-Llama-8B`，**已正常响应**
  - 吞吐: avg gen 707.7 tokens/s, 11 reqs running, KV cache 1.3%, prefix cache hit 85.8%
- **GPU 3**: 17555/97887 MiB (模型较小，正常)
- **Extraction 进程 (PID 442112)**: 正在运行，**196/204** intermediates 已完成，正常推进中

## 2. Frontier SCB 进度 (D135)

| 模型 | 完成 | 总量 | 并发 |
|------|------|------|------|
| **gpt-4.1** | **120/204** | 204 | 12 |
| **gpt-5.5** | 30/204 | 204 | 4 |
| **o3** | 30/204 | 204 | 4 |

三个进程 (PID 444433/444813/444814) 均在运行。gpt-4.1 进度最快（并发12）。

## 3. Gemini 状态

**无 gemini 进程在运行**，未找到相关结果文件。

## 4. 其他实验快照

| 实验 | PID | 运行时间 | 进度 |
|------|-----|---------|------|
| **70B SICA** | 436077 (python 436084) | 2h15m | **7/204** intermediates (port 8002, 较慢) |
| **Cross-model SICA** | 414515 | 6h15m | **100/204** problems, 各 extraction 目录 ~100 files |

**GPU 总览**:
| GPU | VRAM | Util |
|-----|------|------|
| 0 | 84225/97887 MiB | 0% |
| 1 | 83565/97887 MiB | 100% |
| 2 | 88115/97887 MiB | 100% |
| 3 | 17555/97887 MiB | 98% |

GPU 0 utilization 0% 但 VRAM 高占用——可能是 cross-model 使用的 vLLM server 处于空闲等待状态。

---
