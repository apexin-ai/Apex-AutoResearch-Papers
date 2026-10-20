# research lc scoring analysis

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lc_scoring_analysis_20260513T101642_result.json`
- **Structured JSON:** [`0f5dcd87c6880ffb310b.json`](../../sessions/0f/0f5dcd87c6880ffb310b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LC 动态范围分析报告

### 当前实现（第 56-69 行）

```python
def lexical_conformity(self, sample, corpus_subset=None, k=50):
    refs = random.sample(corpus_subset, min(k, len(corpus_subset)))
    for ref in refs:
        bleu = sacrebleu.sentence_bleu(sample, [ref])  # sentence-level BLEU-4, 单条参考
        bleu_scores.append(bleu.score / 100.0)
    return float(np.mean(bleu_scores))
```

对每个样本，随机取 k=50 条参考文本，逐条计算 sentence BLEU-4，取均值。

### 根因

BLEU-4 要求 **4-gram 精确匹配**。solver trace 是数学推理文本，词汇组合高度多样，单条样本与单条随机参考之间几乎不可能有 4-gram 重合。50 个近零值取均值仍然近零。这不是 bug，是 **BLEU-4 + 单参考 + 随机采样** 的组合天然导致的地板效应。

### 备选方案对比

| 方案 | 预期区分度 | 计算成本 | 理论合理性 |
|------|-----------|---------|-----------|
| **BLEU-1/2（降阶）** | 中等，unigram/bigram 匹配率高很多 | 同现有，无额外依赖 | 弱——低阶 n-gram 主要反映词频，区分度有限 |
| **ROUGE-L** | 较好，LCS 对长文本宽容 | 低，rouge-score 轻量 | 中——捕获序列结构但对词汇分布不敏感 |
| **chrF**（character n-gram F-score） | 较好，字符级天然更高 | 同 sacrebleu（内置） | 中——对拼写/形态变化鲁棒，但对语义词汇一致性间接 |
| **增大 k（200-500）** | 微弱改善，均值仍受 BLEU-4 地板限制 | 线性增长（×4-10） | 不解决根因 |
| **TF-IDF cosine** | **好**，连续分布在 [0,1]，区分度强 | 中等，需 fit vectorizer | **强**——直接衡量词汇分布相似性，正是 LC 的语义目标 |
| **Corpus BLEU（多参考）** | 中等，多参考提升匹配率 | 同现有 | 中——sacrebleu 支持多参考，但 50 条全传入开销大 |

### 推荐

**TF-IDF cosine similarity**。理由：

1. LC 的目标是衡量"合成样本在词汇层面与原始分布的一致性"，TF-IDF cosine 直接度量这个——将 gen-0 语料 fit 为词汇空间，每个样本算 cosine，天然分布在 [0,1] 且有区分度。
2. 计算成本低：`TfidfVectorizer.fit` 在 gen-0 上只跑一次，每个样本 `transform + cosine` 是 O(V) 稀疏运算。
3. 无需额外 GPU。

**代码改动位置**：`property_scorer.py` 第 56-69 行的 `lexical_conformity` 方法，以及 `__init__` 和 `set_reference_corpus` 中增加 TF-IDF vectorizer 的初始化和 fit。预期 LC 分布从 [0, 0.02] 扩展到 [0.05, 0.6] 区间。

---
