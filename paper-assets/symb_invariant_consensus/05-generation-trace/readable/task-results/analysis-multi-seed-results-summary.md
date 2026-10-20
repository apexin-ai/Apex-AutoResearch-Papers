# analysis multi seed results summary

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi-seed-results-summary_20260523T175336_result.json`
- **Structured JSON:** [`29ec74f18c6df3a7a52f.json`](../../sessions/29/29ec74f18c6df3a7a52f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完成。Qwen3 多种子实验在两台服务器上都不存在，只有 seed42 baseline。

汇总如下：

## ProofWriter Depth-5 (n=600) 多种子实验结果

| Model | Seed | n | SC (%) | SICA (%) | Δ (pp) | McNemar p | Status | Server | Path |
|-------|------|---|--------|----------|--------|-----------|--------|--------|------|
| **Mistral-7B** | 42 | 600 | 40.00 | 36.67 | -3.33 | 0.0022** | ✅ 完成 | westd-16639 | multi_seed/mistral_pw_seed42 |
| Mistral-7B | 123 | 600 | 40.83 | 37.50 | -3.33 | 0.0091** | ✅ 完成 | westd-16639 | multi_seed/mistral_pw_seed123 |
| Mistral-7B | 456 | 600 | 39.83 | 38.67 | -1.17 | 0.3817 | ✅ 完成 | westd-16639 | multi_seed/mistral_pw_seed456 |
| Mistral-7B | 789 | 600 | 38.83 | 37.17 | -1.67 | 0.1742 | ✅ 完成 | westd-16639 | multi_seed/mistral_pw_seed789 |
| **LLaMA-3.1-8B** | 42 | 600 | 70.00 | 64.83 | -5.17 | 0.0002*** | ✅ 完成 | westd-16639 | exp048_llama8b_pw600 |
| LLaMA-3.1-8B | 123 | 600 | 71.33 | 64.17 | -7.17 | 0.000007*** | ✅ 完成 | westd-16639 | multi_seed/llama8b_pw_seed123 |
| LLaMA-3.1-8B | 456 | 520 | 71.92 | 65.96 | -5.96 | 0.0002*** | ⏳ 520/600 | westd-30973 | multi_seed/llama8b_pw_seed456_v2 |
| LLaMA-3.1-8B | 789 | 600 | 71.17 | 66.17 | -5.00 | 0.0003*** | ✅ 完成 | westd-16639 | multi_seed/llama8b_pw_seed789 |
| **Qwen2.5-14B** | 42 | 600 | 73.50 | 71.50 | -2.00 | 0.0501 | ✅ 完成 | westd-16639 | exp032_qwen25_14b_pw600 |
| Qwen2.5-14B | 123 | 600 | 72.33 | 71.17 | -1.17 | 0.3105 | ✅ 完成 | westd-16639 | multi_seed/qwen25_pw_seed123 |
| Qwen2.5-14B | 456 | 600 | 73.00 | 72.17 | -0.83 | 0.4421 | ✅ 完成 | westd-16639 | multi_seed/qwen25_pw_seed456 |
| **Qwen2.5-14B** | **789** | **600** | **73.67** | **71.67** | **-2.00** | **0.0428*** | **✅ 完成** | **westd-16639** | **multi_seed/qwen25_pw_seed789** |
| **Qwen3-14B** | 42 | 600 | 85.00 | 85.67 | +0.67 | 0.5034 | ✅ 完成 | westd-16639 | exp033_qwen3_14b_pw600_nonthinking |
| Qwen3-14B | 123 | — | — | — | — | — | ❌ 未跑 | — | — |
| Qwen3-14B | 456 | — | — | — | — | — | ❌ 未跑 | — | — |
| Qwen3-14B | 789 | — | — | — | — | — | ❌ 未跑 | — | — |

### 关键发现

**Qwen2.5-14B seed789 完整数据**（600/600，westd-16639）：SC=73.67%, SICA=71.67%, Δ=-2.00pp, McNemar p=0.0428 (显著)。

### 不完整实验

- **LLaMA-3.1-8B seed456**: 最佳版本是 westd-30973 的 v2 (520/600)，westd-16639 旧版仅 184/600
- **LLaMA-3.1-8B seed42**: multi_seed 目录版仅 223/600，但 exp048 baseline 有完整 600/600
- **Qwen3-14B seeds 123/456/789**: 两台服务器上均未找到，需要安排新实验

### 补充说明

westd-30973 还有 `qwen25_pw_seed789_v3` (339/600) 和 `llama8b_pw_seed789_v2` (357/600)，但 westd-16639 上对应的原版已有完整 600/600 结果，这些 v2/v3 无需使用。

---
