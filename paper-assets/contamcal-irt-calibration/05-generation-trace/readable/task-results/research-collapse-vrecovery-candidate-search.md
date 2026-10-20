# research collapse vrecovery candidate search

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_collapse-vrecovery-candidate-search_20260522T035408_result.json`
- **Structured JSON:** [`f6481be63bebc6ff4081.json`](../../sessions/f6/f6481be63bebc6ff4081.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

## 候选模型 MMLU Baseline

| 模型 | MMLU 5-shot | 来源 | 在 65-70%? | HF 可用? | 备注 |
|------|------------|------|-----------|---------|------|
| Mistral-7B-v0.3 | 63.5% | [Mistral AI blog](https://mistral.ai/news/announcing-mistral-7b) | ❌ (偏低) | ✅ `mistralai/Mistral-7B-v0.3` | 7B, base+instruct 都有 |
| Yi-1.5-9B | 76.3% | [01-ai/Yi GitHub](https://github.com/01-ai/Yi) | ❌ (偏高) | ✅ `01-ai/Yi-1.5-9B` | 9B, 远超 vulnerability band |
| InternLM2.5-7B | 71.6% | [InternLM GitHub](https://github.com/InternLM/InternLM/blob/main/model_cards/internlm2.5_7b.md) | ❌ (略高) | ✅ `internlm/internlm2_5-7b` | 7B, 比上限高 1.6pp |
| **Falcon3-7B-Base** | **67.4%** | [HF model card](https://huggingface.co/tiiuae/Falcon3-7B-Base) | **✅** | ✅ `tiiuae/Falcon3-7B-Base` | 7B, TII 家族, 无 gating |
| **Mistral-Nemo-12B-Base** | **68.0%** | [HF nvidia/Mistral-NeMo-12B-Base](https://huggingface.co/nvidia/Mistral-NeMo-12B-Base) | **✅** | ✅ `mistralai/Mistral-Nemo-Base-2407` | 12B, Mistral 家族, 128k context |

## 推荐

**首选：Falcon3-7B-Base (67.4%)**

理由：
1. MMLU 67.4% 正好落在 vulnerability band 中心
2. TII（Technology Innovation Institute）家族，与 Qwen/Phi/OLMo/Gemma/LLaMA 完全无血缘关系，跨家族复现说服力最强
3. 7B 参数量，与现有 Qwen-7B 实验直接可比
4. HF 开放下载，无 gating
5. 有 Instruct 版本做对照但我们用 base

**备选：Mistral-Nemo-12B-Base (68.0%)**

如果需要第二个验证点或 Falcon3 训练出问题可切换。但注意 Mistral-Nemo 仍属 Mistral 家族（与候选列表中 Mistral-7B 同源），跨家族论证力度不如 Falcon3。

---
