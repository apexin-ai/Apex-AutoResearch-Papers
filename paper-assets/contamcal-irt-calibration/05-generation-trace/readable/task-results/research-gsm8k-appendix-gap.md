# research gsm8k appendix gap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_gsm8k-appendix-gap_20260521T110638_result.json`
- **Structured JSON:** [`10aaf1c851b6f5361f7c.json`](../../sessions/10/10aaf1c851b6f5361f7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the output:

---

## 1. GSM8K Appendix 数据完整性表（s0 seed, 37775 evaluate.py — D206）

| Family | d000 | d005 | d025 | d050 | d100 | 状态 |
|--------|------|------|------|------|------|------|
| **Qwen-7B** | 73.31% ✅ | 78.32% ✅ | 78.24% ✅ | 79.38% ✅ | 81.20% ✅ | **完整 5-dose** |
| **Qwen-14B** | 74.98% ✅ | 71.19% ✅ | 79.30% ✅ | **GAP** (PREPARING) | 82.41% ✅ | **4/5** |
| **Phi-4** | 84.46% ✅ | — | — | — | **GAP** | **1/5** |
| OLMo-2 | ❌ 排除 (D204: evaluate.py 版本不一致) | — | — | — | — | **排除** |
| Gemma-2 | 17.82% ⚠️ CoT 崩塌 | — | — | — | — | **排除** |

**Gaps:**
- **Qwen-14B d050 GSM8K s0**: 模型存在（retrain_qwen14b_d050_s0 DONE），MMLU/ARC eval 已完成，但 GSM8K eval 仍 PREPARING
- **Phi-4 d100 GSM8K s0**: 无 s0 数据。s123 数据存在（83.85%, gsm8k_phi4_s123_westd），s42 仍 PREPARING

注：ROADMAP 标 Qwen-14B "✅ 完整 5-dose" 与 registry 矛盾（d050 PREPARING）。需确认 d050 是否已完成但未注册。

## 2. Phi-4 d100 GSM8K 状态确认

**s0: 无数据（GAP）。s123: 83.85%（Δ = -0.46pp vs d000=84.31%）。s42: PREPARING。**

如果 appendix 统一用 s0（D206），Phi-4 d100 是必须补的 gap。但 s123 数据显示 Phi-4 GSM8K 基本 immune（-0.46pp），与 MMLU pattern 一致。

## 3. LLaMA-3 结果预计写入的论文章节

LLaMA-3.1-8B Base 当前状态：SFT 训练中（sft_llama3_d000_s0 / d025 / d100 均 RUNNING），eval 尚未开始。

预计写入章节：

| 章节 | 内容 | 优先级 |
|------|------|--------|
| **§4 Results / Claim 1 Characterization** | 主表添加第 6 行（LLaMA-3 dose-response pattern 分类）| 核心——直接回应 W3 |
| **§4 Vulnerability gradient 讨论** | LLaMA-3.1-8B Base 的 baseline MMLU 决定它在 gradient 上的位置 | 核心 |
| **Table 1（主结果表）** | 5→6 families，添加 d000/d100 Δ | 核心 |
| **§5 Discussion / Generalizability** | "6 independent families" 替代 "5 families"，增强泛化论证 | 重要 |
| **Appendix: GSM8K Cross-Benchmark** | 如果时间允许跑 LLaMA-3 GSM8K eval | 可选 |
| **Limitations** | family count 从 5→6 可弱化 "limited families" caveat | 次要 |

---
