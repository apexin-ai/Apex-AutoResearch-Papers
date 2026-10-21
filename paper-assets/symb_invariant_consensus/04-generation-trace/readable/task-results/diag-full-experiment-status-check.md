# diag full experiment status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full-experiment-status-check_20260519T115730_result.json`
- **Structured JSON:** [`54a2a0a188d26b64d715.json`](../../sessions/54/54a2a0a188d26b64d715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。汇总如下：

---

## 实验状态汇总（2026-05-19 20:00 UTC）

### westd-25068

| Exp | Model / Dataset | 进度 | SC% | SICA% | Δ(pp) | ETA | 状态 |
|-----|----------------|------|-----|-------|-------|-----|------|
| exp-062 | Gemma-27B / FOLIO-204 | 100/204 | 82.0% | 82.0% | +0.0 | ~185 min (~3.1h) | 运行中 |
| exp-065 | Qwen2.5-7B / PW-600 | 331/600 | 72.8% | 66.2% | -6.6 | ~154 min (~2.6h) | 运行中 |
| exp-069 | Mistral-7B / LogiQA-200 | 24/200 | 45.8% | 45.8% | +0.0 | ~76 min (~1.3h) | 运行中 |
| exp-070 | Qwen2.5-7B / LogiQA-200 | 12/200 | 58.3% | 58.3% | +0.0 | ~54 min (~0.9h) | 运行中 |

GPU: 0=96% / 1=0%* / 2=97% / 3=96%
*GPU1 显存占满(87969 MiB)但 utilization 0%，exp-069 vllm 已加载模型，推理进程在跑，可能是采样间隙。

### westd-16639

| Exp | Model / Dataset | 进度 | SC% | SICA% | Δ(pp) | ETA | 状态 |
|-----|----------------|------|-----|-------|-------|-----|------|
| exp-048 | LLaMA-8B / PW-600 | 447/600 | 70.9% | 65.3% | -5.6 | ~198 min (~3.3h) | 运行中 |
| exp-064 | DeepSeek-R1-8B / FOLIO-204 | 67/204 | 82.1% | 82.1% | +0.0 | ~372 min (~6.2h) | 运行中 |
| exp-068 | Qwen3-14B / LogiQA-200 | 83/200 | 81.9% | 83.1% | +1.2 | ~63 min (~1.1h) | 运行中 |

GPU: 全部 4 卡 96-97%，满载运行。

### 关键发现

1. **exp-064 extraction rate 仍然很低：40.7%**（67 个问题中提取了 1790 constraints，但只有 1392 unique）。SICA=SC=82.1%（Δ=0），低 extraction rate 导致 SICA 退化为接近 SC 的行为。

2. **exp-065 和 exp-048（PW-600）都出现 SICA < SC**：exp-065 Δ=-6.6pp，exp-048 Δ=-5.6pp。PW-600 上 SICA 在多个模型上都表现负增益。

3. **exp-069/070（LogiQA）样本量还太小**（24/12），指标不稳定，需等待更多数据。

4. **exp-068 Qwen3-14B LogiQA 是目前唯一 SICA > SC 的实验**（+1.2pp），83.1% SICA vs 81.9% SC。

---
