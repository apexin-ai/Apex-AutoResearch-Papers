# research baseline verification

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline-verification_20260525T201615_result.json`
- **Structured JSON:** [`994a2d88c6b05da90ec5.json`](../../sessions/99/994a2d88c6b05da90ec5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

**结果: 4/5 通过，1 个错误**

- **ATLOP / EIDER / SAIS / DREEAM**: 全部匹配原论文数字（DocRED dev, RoBERTa-large）。✓
- **AutoRE**: ❌ related_work.tex 中引用的 52.14 来自 RelPrior 论文 Table 2 的 **RE-DocRED dev** 列，不是 DocRED dev。在 DocRED dev 上，AutoRE_LLaMA3-8B 实际为 45.22，RelPrior 为 47.70。当前写法 "our RSFT model (54.33) outperforms AutoRE (52.14) and is slightly below RelPrior (−1.17pp)" 是跨数据集比较（我们的 54.33 是 DocRED dev，对方的 52.14/55.50 都是 RE-DocRED dev）。

**修复方案**：用 DocRED dev 数字（AutoRE=45.22, RelPrior=47.70），此时我们 +9.11pp / +6.63pp 大幅领先。或者在 Re-DocRED dev 上跑我们的 8B 模型做公平比较。

---
