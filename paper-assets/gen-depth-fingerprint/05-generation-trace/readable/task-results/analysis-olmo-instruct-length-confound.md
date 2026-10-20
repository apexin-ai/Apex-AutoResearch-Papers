# analysis olmo instruct length confound

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_olmo-instruct-length-confound_20260515T180847_result.json`
- **Structured JSON:** [`d6fc1154eb3c60488aae.json`](../../sessions/d6/d6fc1154eb3c60488aae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OLMo-Instruct length confound 分析完成。结果已追加到 `instruct_length_confound.json` 并更新 registry。

**关键发现（OLMo-2-0425-1B-Instruct）：**

| 指标 | 值 |
|------|-----|
| length-depth Spearman ρ | **-0.3701**（确认 length confound） |
| **entropy_mean** original → partial ρ | 0.4822 → **0.3640**（控制长度后仍显著，reversal survives） |
| **ttr** original → partial ρ | 0.0057 → **-0.2407**（原本就几乎无相关，控制后反转为负） |
| **hapax_ratio** original → partial ρ | 0.0253 → **-0.1979**（同上） |
| surface reversal survives | **NO** |
| entropy reversal survives | **YES** |
| depth signal after control | **partially_survives** |
| binary LOGO F1 (held-out) | **0.3506** |

与 Qwen instruct 模型的区别：OLMo-Instruct 的 surface 特征（ttr/hapax）原始 ρ 就接近零（不像 Qwen 的 ~0.5），所以不存在 "surface reversal"。但 entropy ρ sign reversal（base 约 -0.64 → instruct +0.48）在控制长度后仍保留（partial ρ = 0.364），说明 **entropy 方向反转不是纯粹的长度伪相关**。

---
