# analysis mistral folio 789 harvest final

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral-folio-789-harvest-final_20260522T113235_result.json`
- **Structured JSON:** [`1228fedbef086cfc4f3c.json`](../../sessions/12/1228fedbef086cfc4f3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Mistral FOLIO seed=789（PID 576938）
**仍在运行**（elapsed 44min），vLLM port 8004 活跃（最后请求 19:33:11）。results.json 已有中间结果：

| 指标 | 值 |
|------|-----|
| 已完成 | **110/204** 题（~54%） |
| SC accuracy | **59.09%** (65/110) |
| SICA accuracy | **54.55%** (60/110) |
| Δ (SICA-SC) | **-4.55pp** |
| Wall time | 2626s (~44min) |

SICA 目前落后于 SC 4.55pp，最终结果需等全部 204 题跑完。

### 其他 GPU 实验（均已完成，有 results.json）

| GPU | 实验 | N | SC | SICA | Δ |
|-----|------|---|-----|------|---|
| cuda:0 | Qwen2.5 PW seed123 | 214 | **76.17%** | **75.70%** | -0.47pp |
| cuda:1 | LLaMA-8B FOLIO seed123 | 43 | **79.07%** | **79.07%** | 0.00pp |
| cuda:2 | Mistral PW seed123 | 375 | **40.80%** | **38.93%** | -1.87pp |

### cuda:3 vLLM 状态
**运行中**，port 8004 持续响应 HTTP 200。Mistral FOLIO seed=789 预计还需 ~40min 完成剩余 94 题。

---
