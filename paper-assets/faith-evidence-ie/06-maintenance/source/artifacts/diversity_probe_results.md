# SFT 模型输出多样性探测 (Diversity Probe)

- Base model: `Qwen3-4B`
- Adapter: `sft_output` (QLoRA, r=64, merge & unload)
- N generations per sample: 8
- Temperatures: 0.7, 1.0
- top_p: 0.9
- max_new_tokens: 1024
- GPU: RTX 5090 (cuda:2, shared)

## 实验样本

| # | Doc ID | Gold Triples | Sentences | 复杂度 |
|---|--------|-------------|-----------|--------|
| 1 | Academia Mexicana de la Lengua | 5 | 5 | 低 |
| 2 | Nops (spider) | 9 | 6 | 中 |
| 3 | Kina Konova | 12 | 7 | 高（被截断） |

## 核心结果

### Sample 1: Academia Mexicana (5 triples, 5 sents)

| Metric | T=0.7 | T=1.0 |
|--------|-------|-------|
| Format OK | **7/8** | 5/8 |
| F1 mean±std | 0.000±0.000 | 0.019±0.054 |
| Jaccard similarity | 0.240±0.179 | 0.100±0.115 |
| Unique triple-sets | **8/8** | **8/8** |
| Elapsed | 119.3s | 145.6s |

### Sample 2: Nops spider (9 triples, 6 sents)

| Metric | T=0.7 | T=1.0 |
|--------|-------|-------|
| Format OK | 1/8 | 2/8 |
| F1 mean±std | 0.000±0.000 | 0.000±0.000 |
| Jaccard similarity | 0.099±0.294 | 0.002±0.013 |
| Unique triple-sets | 6/8 | **8/8** |
| Elapsed | 149.6s | 160.5s |

### Sample 3: Kina Konova (12 triples, 7 sents) — 截断

所有生成均触顶 1024 tokens (format=0.10，即被截断的 JSON)。12 triples 需要 ~2048 tokens 才能完整输出，max_new_tokens=1024 不够。

**注意**: rsft_generate.py 使用 max_new_tokens=2048，RSFT 实际运行不会有此问题。

## 关键发现

### 1. 多样性充足 — RSFT 可行

| 指标 | T=0.7 avg | T=1.0 avg | 判断 |
|------|-----------|-----------|------|
| Unique triple-sets | 7.0/8 | 8.0/8 | 足够多样 |
| Jaccard similarity | 0.170 | 0.051 | 低相似度 = 高多样性 |

**结论: SFT 模型输出多样性完全充足。** 8 个候选输出中几乎每个都产生不同的三元组集合。reviewer 担心的"8 个输出几乎一样"的风险不存在。

T=1.0 多样性更高（jaccard 0.051 vs 0.170），但代价是格式合规率下降。

### 2. 格式合规率是主要风险

| 指标 | T=0.7 | T=1.0 |
|------|-------|-------|
| Format OK rate (sample 1) | 87.5% | 62.5% |
| Format OK rate (sample 2) | 12.5% | 25.0% |
| **Average** | **50.0%** | **43.8%** |

格式失败的两个原因（从 DEBUG 日志分析）：

**a) 字段名不稳定**: 模型交替使用 `head`/`head_entity`, `evidence`/`sentence_ids`/`evidence_sentence_ids`。format_reward 严格要求 `head`+`tail`+`relation`+`evidence`，任何变体都判 0。

**b) 关系名与 gold 不匹配**: 模型输出 "founded"/"located in"，gold 是 "inception"/"country"。这导致 F1=0，但实际上模型提取的信息是正确的（head-tail 对正确）。

### 3. F1=0 是测量问题，不是模型问题

F1 reward 基于精确字符串匹配。DEBUG 显示：

```
pred: ('academia mexicana de la lengua', 'founded', '11 september 1875')
gold: ('academia mexicana de la lengua', 'inception', '11 september 1875')
→ 同一事实，不同关系名，F1 判为不匹配
```

**这意味着 f1_reward 不适合用作 RSFT 的 reward signal**。应使用 CED reward（基于 NLI 语义匹配，不依赖精确字符串）。

## 建议

### RSFT 配置建议

| 参数 | 推荐值 | 理由 |
|------|--------|------|
| temperature | **0.7** | 多样性已充足（7/8 unique sets），格式合规率更高 |
| num_generations | 8 | 足够产生 6-8 个不同候选 |
| max_new_tokens | **2048** | 1024 导致复杂文档截断 |
| top_p | 0.9 | 保持当前设定 |

### 必须在 RSFT 前修复的问题

1. **统一输出格式**: SFT 模型的字段名不稳定（`head` vs `head_entity` 等）。建议：
   - 在 rsft_generate.py 的解析中容忍变体字段名（`head_entity`→`head`, `sentence_ids`→`evidence`）
   - 或在 SFT 训练数据中强化格式约束

2. **使用 CED reward 而非 f1_reward**: 关系名的措辞差异使 f1_reward 失效。CED reward 基于 NLI 模型，能正确评估语义等价的三元组。

3. **RSFT scoring pipeline**: rsft_score_filter.py 应使用 CED reward 作为主 reward signal，format_reward 作为 gating signal（format_ok 才有资格被选中）。

### 如果格式问题无法修复

如果格式合规率持续低于 50%，RSFT 的有效候选数（format_ok 且 high reward）可能不足。替代方案：
1. 回退到 GRPO（在线 RL，不需要预生成候选）
2. 在 SFT 上多训练几个 epoch 提升格式稳定性
3. 在 RSFT 生成时将 num_generations 提高到 16，保证至少有 4-8 个格式合规候选
