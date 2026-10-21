# analyze d030 kl50 uniform v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d030_kl50_uniform_v2_20260516T050932_result.json`
- **Structured JSON:** [`ac46a8437b2a1feaea46.json`](../../sessions/ac/ac46a8437b2a1feaea46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d030_kl50_uniform 评测结果

### 原始指标

| 指标 | 值 |
|------|------|
| wikitext2_ppl | **11.9631** |
| arc_challenge acc | 0.2833 |
| arc_challenge acc_norm | **0.3276** |
| winogrande acc | **0.6290** |
| mmlu acc | **0.2777** |
| gsm8k exact_match_strict | 0.0197 |
| gsm8k exact_match_flexible | **0.0212** |

### 对比表

| 指标 | Dense | KL50 global top-k | KL30 uniform | **KL50 uniform** | KL50 uniform vs top-k |
|------|-------|-------------------|--------------|-------------------|----------------------|
| ARC-c norm | 0.5819 | 0.3771 | 0.4078 | **0.3276** | **-0.0495** |
| WinoGrande | 0.7814 | 0.6156 | 0.6859 | **0.6290** | **+0.0134** |
| MMLU | 0.6532 | 0.2591 | 0.4061 | **0.2777** | **+0.0186** |
| GSM8K | 0.5004 | 0.0121 | 0.0735 | **0.0212** | **+0.0091** |

### 分析

KL50 uniform 相比 KL50 global top-k：
- WinoGrande、MMLU、GSM8K 小幅提升（+1~2pp）
- **ARC-c norm 显著下降**（-5pp，0.3771→0.3276）
- 整体 uniform 分配在 50% 稀疏度下未带来一致性提升

KL50 uniform 相比 KL30 uniform：
- 所有指标全面大幅退化（ARC-c -8pp, WinoGrande -5.7pp, MMLU -12.8pp, GSM8K -5.2pp）
- 50% 稀疏度对 uniform 分配冲击很大，30% uniform 明显优于 50% uniform

---
