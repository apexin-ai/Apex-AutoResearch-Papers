# exp plan 015 dolma supplement

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_015_dolma_supplement_20260515T214713_result.json`
- **Structured JSON:** [`f44fc254130aea712c7e.json`](../../sessions/f4/f44fc254130aea712c7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册 (`art_20260515_1db0aa`)。

**plan_015 C4 supplement 实验完成。核心发现：**

- **C4 d0 prediction rate: 79.8%** — 在 5000 条 C4 web-crawl 验证集段落中，约 20% 被 RF 分类器错误预测为 d1+
- **WikiText-103 d0 rate: 100%** — 546 条学术百科文本全部正确识别为 d0
- **Controlled data accuracy: 99.9%+** — 在受控数据上 d0-d3 分类几乎完美
- **5-fold CV: 0.7878 ± 0.0056**

**d1+ 误分类分析 (1012/5000 passages)**：
- 误分类段落的关键特征差异：rep_4gram 高 74.7%，rep_3gram 高 37.0%，p90_ppl 高 39.6%
- 样本文本大多是广告、产品描述、SEO 模板化内容 — 这类文本重复率高、词汇多样性低，统计特征天然接近 LLM 生成文本

这说明 RF 分类器在编辑型文本（WikiText）上 FPR=0%，但在包含模板化/低质量内容的 web 文本上 FPR≈20%。对于论文来说，这是一个有意义的生态效度结果：分类器的 false positive 主要来源于可解释的文本特性（高重复率+低多样性），而非随机噪声。

---
