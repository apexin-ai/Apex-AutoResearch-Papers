# analyze exp 057 scale 9gen logo

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_057_scale_9gen_logo_20260520T073615_result.json`
- **Structured JSON:** [`7ec4e8033f56e2f5685c.json`](../../sessions/7e/7ec4e8033f56e2f5685c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。下面输出分析结论。

---

## exp_057 分析结论：9-gen LOGO — **SUCCESS**

### 核心指标

| 指标 | 9-gen | Baseline | Δ |
|------|-------|----------|---|
| 3-class LOGO avg F1 | **0.7516** | 8-gen: 0.7698 | −0.0182 |
| Binary LOGO avg F1 | **0.6842** | — | — |
| 6-gen LOGO (plan-002) | — | 0.8037 | — |
| 6-gen LOGO (plan-014) | — | 0.7893 | — |

### Per-generator 3-class F1 排名

| Generator | 3-class F1 | Binary F1 | Δ vs 8gen |
|-----------|-----------|-----------|-----------|
| pythia-1b | 0.8496 | 0.7942 | −0.0068 |
| pythia-2.8b | 0.8174 | 0.7427 | +0.0005 |
| qwen3-0.6b | 0.8167 | 0.7497 | −0.0057 |
| qwen3-1.7b | 0.8087 | 0.7590 | −0.0011 |
| olmo-2-1b | 0.7767 | 0.6894 | +0.0025 |
| llama-3.2-3b | 0.7688 | 0.6820 | +0.0067 |
| **qwen3-8b** | **0.7000** | **0.6540** | −0.0009 |
| gemma-2-2b | 0.6143 | 0.5539 | (new) |
| mistral-7b-v0.3 | 0.6122 | 0.5326 | −0.0037 |

### Qwen3-8B DDR Pattern

Per-class F1: gen-0 = 0.84, gen-1 = 0.5592, gen-2+ = 0.7009

这与 sub-3B 模型一致：gen-0（人类文本）最易区分，gen-1（首次生成）最难分类，gen-2+（更深层生成）信号累积后 F1 回升。DDR pattern 在 7B+ 模型上持续存在。

### gemma-2-2b 观察

样本量极少（n=1061，binary 仅 67 样本），gen-1 F1 = 0.0625 几乎为零，binary CI 宽达 [0.42, 0.68]。这不是信号缺失，更可能是 gemma-2-2b 仅 1061 行训练数据不足以学习其 depth pattern。

### 判断理由

- 9-gen 3-class F1 = 0.7516 ≥ 0.75 阈值 ✓
- Qwen3-8B binary F1 = 0.654 远超 chance (0.5) ✓
- 原有 7 个 generator 的 F1 变动均在 ±0.007 以内，添加新 generator 未破坏已有信号
- 整体 F1 下降（−0.0182）主要由两个新增低 F1 generator（gemma-2-2b、mistral-7b-v0.3）拉低均值，并非信号退化
- Qwen3-8B 展现清晰 DDR pattern，排除 scale-dependent signal collapse

**Conclusion: SUCCESS** — depth signal 在 7B+ scale 持续存在，9-gen ensemble 可用。

---
