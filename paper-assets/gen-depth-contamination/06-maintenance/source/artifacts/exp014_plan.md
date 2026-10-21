# exp-014: Naturalistic Validation — Experiment Plan

## 目标

对 Common Crawl 衍生的自然 web 文本做 OBD depth 预测，与独立质量指标做 correlation 分析，验证 depth signal 在 wild data 上的 ecological validity。

**Rebuttal 价值**：直接回应 Reviewer concern #6（"Prompt-chain 不代表真实世界递归污染"）。如果 OBD predicted depth 与独立质量指标相关，说明实验室构造的 depth signal 确实捕获了自然文本中的退化模式。

---

## 1. 数据获取

### 1.1 数据源选择：FineWeb（推荐）

**不直接用 raw Common Crawl**，改用 HuggingFace 的 FineWeb 数据集：
- 覆盖 114 个 CC snapshots，最新到 CC-MAIN-2025-26
- 已做 trafilatura 文本提取 + URL/line/doc 过滤 + MinHash 去重 + English 过滤
- 避免自己处理 HTML 清洗、语言检测、去重等 pipeline 噪声
- 论文可写 "sampled from FineWeb (Li et al., 2024), a curated English corpus derived from Common Crawl snapshots through 2025"

**Snapshot 选择**：`CC-MAIN-2025-26`（2025年6月），理由：
1. 足够新——大量 AI 生成内容已渗入 web
2. FineWeb 已覆盖，无需自己抓 CC
3. 2025 年中的 snapshot 包含 ChatGPT/Claude/Gemini 普及后的 web 内容

**备选（如需最新 2026 数据）**：直接下载 CC-MAIN-2026-17 的 WET segment，但需要自行做语言过滤和质量过滤，工作量大得多。

### 1.2 采样策略

```python
from datasets import load_dataset
import itertools

ds = load_dataset(
    "HuggingFaceFW/fineweb",
    name="CC-MAIN-2025-26",
    split="train",
    streaming=True
)

# 采样 50K 文档，长度过滤
docs = []
for row in ds:
    text = row["text"]
    word_count = len(text.split())
    if 50 <= word_count <= 1000:  # 过滤过短/过长
        docs.append({"text": text, "doc_id": len(docs), "url": row.get("url", "")})
    if len(docs) >= 50000:
        break
```

**采样参数**：
| 参数 | 值 | 理由 |
|------|-----|------|
| 目标文档数 | 50,000 | 足够做 correlation + 分层分析，GPU 成本可控 |
| 最小词数 | 50 | 排除导航碎片、列表页 |
| 最大词数 | 1,000 | 与 depth chain 实验的文本长度范围一致（C4 truncate 256 tokens ≈ 200 words） |
| 语言 | English（FineWeb 已过滤） | — |
| 去重 | FineWeb 已做 MinHash 去重 | 无需额外处理 |

**领域多样性**：FineWeb 从完整 CC snapshot 采样，天然覆盖新闻、博客、商业、教育、技术等多种 web 页面类型。不做额外的领域平衡采样——我们要的就是 "wild web text" 的自然分布。

### 1.3 预处理

FineWeb 已完成主要清洗。额外处理：
1. 截断到前 256 tokens（与 C4 depth chain 实验对齐）
2. 去除前/后空白
3. 跳过含 >30% 非 ASCII 字符的文档（残留 HTML/代码）
4. 保存为 `cc_sample.jsonl`，schema: `{"doc_id": int, "text": str, "url": str}`

---

## 2. Depth 预测

### 2.1 Feature Extraction

复用 `scripts/run_pipeline.py` 中的三个特征提取函数：

```python
from run_pipeline import (
    compute_surprisal_features,  # 9D surprisal statistics
    compute_vocab_diversity,     # 3D: TTR, hapax_ratio, self_bleu
    compute_tail_features,       # 3D: freq_kurtosis, freq_entropy, low_freq_ratio
)
```

**Scorer model**: Qwen2.5-1.5B（路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B`），与主实验一致。

**self_bleu 处理**：原 pipeline 按 depth 分组计算 self-BLEU（100 random refs from same depth）。CC 数据无 depth 标签，改为从全部 CC 样本中随机抽 100 篇作 reference（`depth=0` 模式，所有文档视为同一 pool）。

**输出**：`cc_features.csv`，15D features + doc_id。

### 2.2 OBD Classifier 训练与推断

**训练数据**：exp-017（Qwen-1.5B-Instruct continuation mode on C4）的 `features.csv`。选择理由：
1. Continuation mode 是论文的 canonical condition
2. Qwen-1.5B 同时是 generator 和 scorer，与 CC feature extraction 用同一 scorer
3. C4 web text 与 CC 文本域最接近

**训练流程**（复用 `exp_D_obd_n500_v2.py` 的 OBD 逻辑）：
1. 加载 exp-017 的 features.csv（depths 0-5, N=30,000）
2. 训练 K-1=5 个 binary LightGBM classifiers（P(Y>k), k=0..4）
3. **注意**：这里用全量训练（不做 CV），因为目标是 inference on CC，不是评估 OBD 本身

**推断**：
1. 加载 cc_features.csv
2. 对每篇文档预测 P(Y=0), ..., P(Y=5)
3. 取 argmax 作为 predicted depth
4. 同时保存概率分布（用于 soft analysis）

**输出**：`cc_predictions.csv`，columns: `doc_id, predicted_depth, prob_d0, ..., prob_d5`

**备选方案**：如 exp-017 的 features 有问题（如 Qwen-cont 1v2 CI 极边缘），可改用 exp-001（Pythia C4 continuation）重新用 Qwen scorer 提取特征后训练。

### 2.3 预期 Depth 分布

| Predicted Depth | 预期占比 | 理由 |
|-----------------|---------|------|
| 0（human） | 60-80% | 大部分 web 文本仍是人类写的 |
| 1 | 15-30% | AI 辅助/生成的内容，一次性 generation |
| 2 | 3-8% | 部分可能是 AI 重写 AI 文本 |
| 3+ | <2% | 极少自然出现的多轮递归 |

如果分布严重偏离（例如 >50% predicted depth ≥ 2），需检查 OBD 泛化性——可能是 domain shift 导致的 miscalibration。

---

## 3. 独立质量指标（Correlation Targets）

### 3.1 AlignScore — 不适用，不纳入

**调研结论**：AlignScore（Zha et al., ACL 2023）测量两段文本之间的 factual consistency（context → claim alignment），需要 source-claim pair 输入。我们的 CC 文本是独立的——没有 source document 可以对照。AlignScore 不是通用文本质量指标，不适用于此实验。

### 3.2 采用的指标（5 类，覆盖不同质量维度）

#### A. Perplexity（文本自然度 / 流畅度）

**指标**：GPT-2 Large perplexity（per-token cross-entropy loss 的 exp）

**实现**：
```python
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import torch

model = GPT2LMHeadModel.from_pretrained("gpt2-large").eval().cuda()
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2-large")

def compute_ppl(text, max_length=512):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length).to("cuda")
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
    return torch.exp(outputs.loss).item()
```

**为什么用 GPT-2 而非 LLaMA/Qwen**：
- GPT-2 是独立于我们 pipeline 的外部模型，避免 scorer overlap
- GPT-2 perplexity 是 NLG 评估的标准 baseline
- 轻量（774M params），不需额外下载大模型

**GPU 需求**：GPT-2 Large ~3GB VRAM，可与 Qwen-1.5B 分时使用。

**预期**：AI 生成文本的 GPT-2 perplexity 通常更低（更"平滑"），predicted depth 越高 → perplexity 越低 → 负相关。

#### B. Vocabulary Richness（词汇多样性）

4 个子指标，全部 CPU 计算：

| 指标 | 计算方法 | 库 | 预期与 depth 的关系 |
|------|---------|-----|-------------------|
| **TTR** | unique_types / total_tokens | 内置 | 负相关（AI 文本词汇更窄） |
| **MTLD** | Measure of Textual Lexical Diversity | `lexical_diversity` | 负相关 |
| **vocd-D** | 随机采样 TTR 曲线拟合 | `lexical_diversity` | 负相关 |
| **Hapax Legomenon Ratio** | count(freq=1) / unique_types | 内置 | 负相关 |

```bash
pip install lexical-diversity
```

```python
from lexical_diversity import lex_div as ld

def compute_vocab_richness(text):
    tokens = ld.flemmatize(text)  # lemmatize
    return {
        "ttr": ld.ttr(tokens),
        "mtld": ld.mtld(tokens),
        "vocd_d": ld.hdd(tokens),  # HD-D approximation of vocd-D
        "hapax_ratio": ld.hapax_legomena(tokens) / max(len(set(tokens)), 1)
    }
```

**注意**：TTR 和 hapax_ratio 已经是 15D 特征的一部分（但 MTLD 和 vocd-D 不是），可以做 partial independence 分析。

#### C. Repetition Metrics（重复度）

| 指标 | 计算方法 | 预期 |
|------|---------|------|
| **n-gram repetition rate** | 重复 n-gram 数 / 总 n-gram 数 (n=2,3,4) | 正相关（AI 文本更重复） |
| **self-BLEU**（intra-doc） | 将文档分成段落/句子，计算段落间 BLEU | 正相关 |

```python
from collections import Counter

def ngram_repetition(text, n=3):
    tokens = text.split()
    ngrams = [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
    if not ngrams:
        return 0.0
    freq = Counter(ngrams)
    repeated = sum(c - 1 for c in freq.values() if c > 1)
    return repeated / len(ngrams)
```

**GPU 需求**：无。纯 CPU。

#### D. MAUVE（分布级 human-likeness）

**用途**：不做 per-document 评分，而是按 predicted depth bin 分组后与 depth-0 组做 MAUVE 对比。

```python
import mauve

# 将 CC texts 按 predicted depth 分组
for depth_bin in [0, 1, 2, "3+"]:
    texts_in_bin = [t for t, d in zip(cc_texts, predicted_depths) if bin_match(d, depth_bin)]
    result = mauve.compute_mauve(
        p_text=texts_depth0[:5000],  # human baseline = predicted depth 0
        q_text=texts_in_bin[:5000],
        device_id=0,
        max_text_length=256,
        verbose=False
    )
    print(f"Depth {depth_bin}: MAUVE = {result.mauve:.4f}")
```

**预期**：predicted depth 越高 → MAUVE 越低（与 depth-0 的分布差距越大）。

**GPU 需求**：MAUVE 内部用 GPT-2 embedding，~3GB VRAM。每组 ~2-5 min。

**安装**：
```bash
pip install mauve-text
```

#### E. Zipf 系数（词频分布形态）

**原理**：人类语言符合 Zipf 定律（rank-frequency 幂律关系）。AI 生成文本的 Zipf 系数可能偏离。

```python
import numpy as np
from scipy.optimize import curve_fit

def zipf_coefficient(text):
    tokens = text.lower().split()
    freq = Counter(tokens)
    counts = sorted(freq.values(), reverse=True)
    ranks = np.arange(1, len(counts) + 1, dtype=float)
    counts = np.array(counts, dtype=float)
    # fit log(freq) = -alpha * log(rank) + C
    log_r = np.log(ranks)
    log_f = np.log(counts)
    alpha, _ = np.polyfit(log_r, log_f, 1)
    return -alpha  # Zipf exponent (human text ≈ 1.0)
```

**预期**：AI 文本 Zipf 系数偏离 1.0（通常偏低，词频分布更均匀）。

**GPU 需求**：无。

### 3.3 指标汇总

| 指标 | 维度 | GPU | 计算量 (50K docs) | 与 depth 预期相关方向 |
|------|------|-----|-------------------|---------------------|
| GPT-2 PPL | 流畅度 | 是（3GB） | ~2h | 负相关 |
| TTR | 词汇多样性 | 否 | <5min | 负相关 |
| MTLD | 词汇多样性 | 否 | ~10min | 负相关 |
| vocd-D (HD-D) | 词汇多样性 | 否 | ~15min | 负相关 |
| Hapax ratio | 词汇多样性 | 否 | <5min | 负相关 |
| 3-gram rep rate | 重复度 | 否 | <5min | 正相关 |
| 4-gram rep rate | 重复度 | 否 | <5min | 正相关 |
| MAUVE (per bin) | 分布距离 | 是（3GB） | ~20min | 负相关 |
| Zipf coefficient | 词频形态 | 否 | <5min | 偏离 1.0 |

---

## 4. 分析计划

### 4.1 Correlation Analysis

```python
from scipy.stats import spearmanr, kendalltau

metrics = ["gpt2_ppl", "ttr", "mtld", "vocd_d", "hapax_ratio",
           "rep_3gram", "rep_4gram", "zipf_coeff"]

for metric in metrics:
    rho, p_spearman = spearmanr(predicted_depth, quality_scores[metric])
    tau, p_kendall = kendalltau(predicted_depth, quality_scores[metric])
    print(f"{metric}: Spearman ρ={rho:.4f} (p={p_spearman:.2e}), Kendall τ={tau:.4f} (p={p_kendall:.2e})")
```

**多重比较校正**：Bonferroni 或 Benjamini-Hochberg FDR（9 个指标，α=0.05）。

### 4.2 Stratified Analysis（按 predicted depth 分组）

将 50K 文档按 predicted_depth 分组：
- Bin 0: predicted depth = 0
- Bin 1: predicted depth = 1
- Bin 2: predicted depth = 2
- Bin 3+: predicted depth ≥ 3

对每组计算各质量指标的 mean, median, std, IQR。

**统计检验**：
- Kruskal-Wallis H-test（各组间差异）
- Mann-Whitney U-test（pairwise: Bin 0 vs Bin 1, Bin 1 vs Bin 2, etc.）
- Effect size: Cliff's delta

### 4.3 可视化

**Figure 1: Violin plot** — 每个 predicted depth bin 的各质量指标分布
```
x-axis: predicted depth (0, 1, 2, 3+)
y-axis: metric value
一张 figure 含 3x3 subplot grid（9 个指标）
```

**Figure 2: Scatter plot with trend line** — predicted depth (jittered) vs 代表性指标（GPT-2 PPL, MTLD）
```
x-axis: predicted depth (jittered for visibility)
y-axis: metric value
overlay: LOWESS trend line + Spearman ρ annotation
```

**Figure 3: Depth distribution histogram** — CC 文本的 predicted depth 分布
```
x-axis: predicted depth (0-5)
y-axis: fraction of documents
annotate: N per bin
```

**Figure 4: MAUVE by depth bin** — bar chart with error bars

### 4.4 Robustness Checks

1. **Length-controlled analysis**: 按文本长度分 quartile，每个 quartile 内单独做 correlation（排除长度 confound）
2. **Domain-stratified**: 如果 URL 信息可用，粗分几个域（news, blog, edu, tech）分别做 correlation
3. **Classifier calibration check**: 对 predicted depth 分布做 chi-squared test 与训练集深度分布对比，检查是否有明显偏移
4. **Bootstrap CI for correlations**: 1000 次 bootstrap，报告 Spearman ρ 的 95% CI

---

## 5. 预期结果与 Rebuttal 价值

### 5.1 理想结果（强 ecological validity）

| 发现 | Rebuttal 论点 |
|------|-------------|
| 60-80% CC 文本 predicted depth = 0 | 符合预期，OBD 不是把所有文本都标为 "contaminated" |
| predicted depth 与 vocab richness (MTLD, vocd-D) 显著负相关 | Depth signal 捕获了真实的词汇退化 |
| predicted depth 与 GPT-2 PPL 显著负相关 | 高 depth 文本更"机械"/"平滑" |
| predicted depth 与 repetition 显著正相关 | 高 depth 文本更重复，与 model collapse 理论一致 |
| MAUVE 随 depth bin 单调递减 | 分布层面的验证 |

### 5.2 可接受的混合结果

- 部分指标相关不显著（如 Zipf coefficient）→ 说明某些质量维度不被 depth signal 捕获，是合理的
- Depth 2+ 样本太少 (<500) 导致统计 power 不足 → 报告 effect size，noting power limitation

### 5.3 需要解释的负面结果

- 所有相关均不显著 → OBD 在 wild data 上泛化差，可能是 domain shift（C4 训练 → CC 推断）
- 大量文本 predicted depth ≥ 2 (>20%) → OBD 过度预测，calibration 问题
- 相关方向与预期相反 → 需深入 debug，可能是特征提取 pipeline 不一致

### 5.4 Rebuttal 段落模板

> "To assess ecological validity, we applied our trained OBD classifier to 50K documents sampled from FineWeb (CC-MAIN-2025-26). The predicted depth distribution shows XX% at depth 0, XX% at depth 1, and XX% at depth ≥2, consistent with the expected prevalence of AI-generated content in contemporary web text. Crucially, predicted depth shows significant rank correlation with independent quality metrics not used in OBD training: [MTLD (ρ=−X.XX, p<0.001), GPT-2 perplexity (ρ=−X.XX, p<0.001), 3-gram repetition rate (ρ=+X.XX, p<0.001)]. This confirms that the depth signal captured by our 15D features reflects genuine text quality degradation patterns observable in naturally occurring web text, not merely artifacts of our experimental generation pipeline."

---

## 6. 资源估计

### 6.1 GPU

| 阶段 | 模型 | VRAM | 耗时估计 |
|------|------|------|---------|
| Feature extraction (surprisal) | Qwen-1.5B | ~6GB | ~3-4h (50K docs, batch=8) |
| GPT-2 PPL 计算 | GPT-2 Large | ~3GB | ~2h |
| MAUVE 计算 | GPT-2 (internal) | ~3GB | ~20min |
| **总计** | | 单卡 ≤10GB | ~6h |

可在 cqa1-22115 单卡完成（该服务器有 GPU）。Feature extraction 和 GPT-2 计算分时执行（不需同时加载两个模型）。

### 6.2 磁盘

| 文件 | 大小估计 |
|------|---------|
| cc_sample.jsonl (50K docs) | ~200-500MB |
| cc_features.csv | ~15MB |
| cc_predictions.csv | ~5MB |
| cc_quality_metrics.csv | ~10MB |
| 模型缓存 (GPT-2 Large) | ~3GB |
| **总计** | ~4GB |

### 6.3 依赖包

```bash
# 在 cqa1-22115 上安装（项目 venv/conda 内）
pip install lexical-diversity mauve-text datasets

# 已有（不需安装）：
# torch, transformers, lightgbm, scikit-learn, scipy, numpy, pandas
```

GPT-2 Large 模型需下载（~1.5GB），首次运行时 HuggingFace 自动下载。

---

## 7. 执行步骤（Worker Checklist）

### Phase 1: 数据准备
1. [ ] 连接 cqa1-22115，探测环境
2. [ ] 安装依赖：`pip install lexical-diversity mauve-text datasets`
3. [ ] 下载 GPT-2 Large：`python -c "from transformers import GPT2LMHeadModel; GPT2LMHeadModel.from_pretrained('gpt2-large')"`
4. [ ] 编写 `scripts/exp014_cc_sample.py`：从 FineWeb CC-MAIN-2025-26 streaming 采样 50K docs，保存为 `/root/autodl-tmp/gen-depth-contamination/data_exp014/cc_sample.jsonl`
5. [ ] 运行采样脚本，验证输出格式和数量

### Phase 2: Feature Extraction & Depth Prediction
6. [ ] 编写 `scripts/exp014_features.py`：加载 Qwen-1.5B scorer，对 cc_sample.jsonl 提取 15D features，保存 `cc_features.csv`
7. [ ] 编写 `scripts/exp014_predict.py`：加载 exp-017 的 features.csv 训练 OBD（全量训练，非 CV），对 cc_features.csv 做 depth prediction，保存 `cc_predictions.csv`
8. [ ] 运行并验证 predicted depth 分布合理性

### Phase 3: Quality Metrics
9. [ ] 编写 `scripts/exp014_quality.py`：计算 9 个质量指标（GPT-2 PPL, TTR, MTLD, vocd-D, hapax ratio, 3-gram rep, 4-gram rep, Zipf, intra-doc self-BLEU），保存 `cc_quality_metrics.csv`
10. [ ] 运行并 spot-check 指标值合理性

### Phase 4: Analysis & Visualization
11. [ ] 编写 `scripts/exp014_analysis.py`：correlation analysis, stratified analysis, statistical tests, 生成 4 张 figure + results JSON
12. [ ] 运行分析，结果保存到 `artifacts/exp-014/`
13. [ ] 将关键数字汇报给 Director

### Phase 5: 备用——如果 exp-017 features 不可用
14. [ ] 用 `run_pipeline.py --skip_generation` 对 exp-001 (Pythia C4) 数据重新用 Qwen scorer 提取 features
15. [ ] 用新 features 训练 OBD

---

## 8. 注意事项

1. **AutoDL 网络**：下载 FineWeb 和 GPT-2 前必须 `source /etc/network_turbo`，设置 `HF_HUB_DISABLE_XET=1`，`REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`
2. **self-BLEU 一致性**：CC 数据的 self-BLEU 计算方式与训练数据不同（全 pool vs 同 depth），这是一个已知的 feature mismatch。如果 OBD 性能明显异常，可尝试去掉 self_bleu 用 14D features 重跑
3. **TTR/hapax overlap**：TTR 和 hapax_ratio 同时是 OBD 特征和独立质量指标。在 correlation 分析中应注意标注哪些指标与 OBD 特征有 overlap，哪些是完全独立的（MTLD, vocd-D, GPT-2 PPL, rep rate, MAUVE, Zipf 是完全独立的）
4. **文本截断一致性**：CC 文本必须截断到与训练数据相同的 token 长度（256 tokens），否则 surprisal 特征统计量会因长度差异系统性偏移
5. **HF_HOME**：确保设为 `/root/autodl-tmp/.hf_cache`，GPT-2 Large 下载到数据盘
