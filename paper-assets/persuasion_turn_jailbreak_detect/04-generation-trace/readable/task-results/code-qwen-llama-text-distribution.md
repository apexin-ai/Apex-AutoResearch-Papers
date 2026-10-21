# code qwen llama text distribution

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen-llama-text-distribution_20260521T063004_result.json`
- **Structured JSON:** [`ad049dd7da27aae25057.json`](../../sessions/ad/ad049dd7da27aae25057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## Unigram KL Divergence
- **KL(Qwen || Llama) = 1.1387 bits**
- **KL(Llama || Qwen) = 1.0356 bits**
- **JSD = 0.2077 bits**

分布差异显著（JSD > 0.2）。

## Distinctive Vocabulary
**Top-5 Qwen-distinctive**: authenticator (516x), gun (464x), totp (419x), faucet (413x), bitwarden (352x)
**Top-5 Llama-distinctive**: chord (403x), investigators (349x), canyon (298x), maillard (261x), hydroponic (205x)

关键发现：**几乎全部是主题词（topic-specific nouns），不是风格标记（style markers）**。两个 LLM 被分配了不同的对话主题，导致词汇分布高度不重叠。

## Bigram Jaccard
- **Top-500 Jaccard = 0.2255**（仅 184/816 重叠）

极低的 bigram 重叠进一步印证主题驱动的分布差异。

## Type-Token Ratio
- Qwen TTR = 0.0228 (13,283 unique / 583,141 total)
- Llama TTR = 0.0222 (15,120 unique / 681,501 total)

**TTR 几乎一致**，说明两个 LLM 的词汇丰富度本身没有差异。

## 对 MLM Collapse 假设的支持

这些数据强有力地支持 Discussion 中的假设：

1. Qwen 和 Llama benign 文本的分布差异 **主要由话题差异驱动**，而非文体差异（TTR 一致、distinctive tokens 全是名词）
2. MLM DAPT 在这种数据上学到的是 **LLM-specific 的表面词汇模式**（哪个 LLM 讨论了什么主题），而不是跨 LLM 通用的风格特征
3. 这解释了为什么 MLM-DAPT 在 same-LLM 测试集上表现好但 cross-LLM transfer 时崩溃——它过拟合了源 LLM 的主题分布

结果已保存到 `results/qwen_llama_text_analysis.json`，脚本在 `scripts/analyze_qwen_llama_distribution.py`。

---
