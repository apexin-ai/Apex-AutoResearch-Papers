# writing methodology draft

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_writing_methodology_draft_20260512T162448.jsonl`
- **Structured JSON:** [`ac6e0c05dabf952a012a.json`](../../sessions/ac/ac6e0c05dabf952a012a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-12T16:28:15.749949+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T16:28:15.750246+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T16:28:15.750409+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "gen-depth-contamination",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-12T16:28:15.750580+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\", \"content\": \"# gen-depth-contamination — Research Dashboard\\n\\n> 最后更新: 2026-05-12 11:16 UTC | 更新原因: 修正模型型号 1.8B→1.5B-Instruct，更新进展状态\\n\\n## 核心方向\\n估计递归生成合成文本的代际深度（generational depth），构建首个 ordinal depth classifier，实现 depth-aware graduated filtering 替代 binary detection。核心科学量：判别饱和边界 K*。\\n\\n## 当前进展\\n- **阶段**: MVP 验证（执行中）\\n- **基础设施**: autodl-4090d（1×RTX 4090D 24GB, cuda:0）\\n- **实验**: mvp_pilot_sat_v1 PREPARING，Agent 在编写 pipeline 代码\\n\\n## MVP 验证方案\\n**核心假设**: 递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势。\\n\\n**方案**（对应 IDEA_BRIEF Phase 0 pilot saturation study）:\\n- 模型: **Qwen2.5-1.5B-Instruct**（Qwen2.5 系列无 1.8B；用 Instruct 更接近真实世界合成文本来源，full study 再对比 base vs Instruct）\\n- 种子数据: C4 子集 5K docs\\n- 深度链: depth 0(human) → depth 1-5（递归生成）\\n- 生成方式: **prompt-chain**（upper bound estimate，retrain-chain 留到 research 阶段）\\n- 解码策略: **nucleus sampling p=0.95, T=1.0**\\n- 特征（15 维）: surprisal 9 维 + vocab diversity 3 维 + tail-thinning 3 维\\n- 评估: pairwise depth AUC + JSD + LightGBM ordinal 分类\\n\\n**K* 操作性定义**: K* = max k s.t. AUC(depth k-1 vs k) > 0.60\\n\\n**Pass/Fail 标准**:\\n- ✅ Pass: K* ≥ 3 且 AUC(depth 0 vs 1) > 0.70\\n- ⚠️ Conditional Pass: K* = 2，但特征趋势清晰 → saturation characterization 路线\\n- ❌ Fail: K* ≤ 1 或特征无系统性趋势\\n\\n**预估资源**: 1×RTX 4090D，约 8-12 GPU 小时\\n\\n## 近期任务\\n- [x] GPU 服务器到位\\n- [x] 项目配置绑定\\n- [ ] Agent 完成 pipeline 代码 + 环境搭建\\n- [ ] 生成 depth chain（C4 5K × 6 depths）\\n- [ ] 特征提取 + pairwise AUC + JSD 分析\\n- [ ] 判定 K* → MVP gate 决策\\n\\n## GPU 预算\\n1×RTX 4090D 24GB @ autodl-4090d（cuda:0）\\n\\n## 关键风险\\n1. K* ≤ 2 → saturation characterization 路线仍可投\\n2. 方法论贡献薄弱 → 信道级联 + DPI 理论框架可补强\\n3. EMNLP ARR May 25 deadline 仅 13 天 → MVP 必须 2 天内完成\\n4. Reviewer SSH 不通，无法独立核实环境 → 需跟进修复\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-12 | MVP 初步结果 K*=2（边界），修复 right-padding 后重跑确认再锁路线 | mvp_p
…[truncated 186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T16:28:15.750749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/IDEA_BRIEF.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T16:28:15.751142+00:00_

1	# Idea Brief: How Deep Is Your Fake? Estimating Generational Depth of Recursive Synthetic Text for Quality-Aware Data Curation
2	
3	
4	- **Idea ID**: `idea_013`
5	- **Created**: 2026-05-12
6	- **Approved**: 2026-05-12
7	- **Source**: foreign:be-idea-gen-0509-4
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — primary target with compressed 10-day experiment plan and parallel writing, AAAI 2027 (abstract deadline July 25, 2026; paper deadline August 1, 2026) — fallback with additional time for full 100K corpus, extended cross-scale analysis, and polished writing, ICLR 2027 (expected submission deadline ~September 2026) — fallback allowing thorough cross-domain evaluation and larger-scale experiments
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.
14	
15	Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.
16	
17	Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.
21	2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experi
…[truncated 33176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T16:28:15.751326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/theory_framework.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/theory_framework.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T16:28:15.751525+00:00_

1	# 信道级联 + DPI 理论框架草案
2	
3	> 将递归生成建模为 iterated lossy channel，用 Data Processing Inequality 约束 depth-discriminability 的 fundamental limit。
4	
5	---
6	
7	## 1. 信道级联模型形式化
8	
9	### 基本设定
10	
11	设 X₀ 为人类撰写的文本（seed text），表示为某概率空间上的随机变量。LLM 的生成过程建模为一个随机信道：
12	
13	$$\mathcal{T}: \mathcal{X} \to \mathcal{X}$$
14	
15	将输入文本映射到输出文本。递归生成形成 Markov chain：
16	
17	$$X_0 \to X_1 \to X_2 \to \cdots \to X_k$$
18	
19	其中 $X_{i+1} = \mathcal{T}(X_i)$，即 depth-$(i+1)$ 的文本由 depth-$i$ 的文本经过一次 LLM 信道产生。
20	
21	**关键假设**：
22	
23	- **(A1) 时不变信道**：同一 LLM + 同一 decoding strategy 在每次迭代中使用相同的信道 $\mathcal{T}$。（prompt-chain 设定下成立；retrain-chain 需放宽为 $\mathcal{T}_i$）
24	- **(A2) Markov 性**：$X_{i+1}$ 仅依赖 $X_i$，不依赖 $X_0, \ldots, X_{i-1}$（prompt-chain 逐段独立生成时成立）
25	- **(A3) 有损信道**：$\mathcal{T}$ 是 non-invertible 的——生成过程丢失关于输入的信息（sampling 引入 noise，decoding 策略截断分布尾部）
26	
27	### 形式化表述
28	
29	$$X_0 \xrightarrow{\mathcal{T}} X_1 \xrightarrow{\mathcal{T}} X_2 \xrightarrow{\mathcal{T}} \cdots \xrightarrow{\mathcal{T}} X_k$$
30	
31	这是一个齐次 Markov chain（在假设 A1 下），其转移核由 LLM 的条件分布 $p_\theta(\cdot | x)$ 决定。
32	
33	---
34	
35	## 2. Data Processing Inequality 约束
36	
37	### DPI 基本形式
38	
39	对于 Markov chain $X_0 \to X_1 \to \cdots \to X_k$，DPI 给出：
40	
41	$$I(X_0; X_k) \leq I(X_0; X_{k-1}) \leq \cdots \leq I(X_0; X_1) \leq H(X_0)$$
42	
43	即 $I(X_0; X_k)$ 关于 $k$ 单调非递增。
44	
45	**直觉**：每经过一次 LLM 信道，关于原始人类文本 $X_0$ 的信息只会减少或不变，绝不增加。递归生成是不可逆的信息丢失过程。
46	
47	### 严格衰减条件
48	
49	当 $\mathcal{T}$ 是 strictly lossy channel（即 $I(X_i; X_{i+1}) < H(X_i)$ for all $i$）时，衰减是严格的：
50	
51	$$I(X_0; X_k) < I(X_0; X_{k-1}) \quad \forall k \geq 1$$
52	
53	这对应于 LLM 生成过程中 sampling noise 不可消除的事实——任何 temperature > 0 或 nucleus/top-k 截断都引入不可逆信息损失。
54	
55	### 与 Depth Discriminability 的联系
56	
57	两个不同深度 $k, k'$ 的文本 $X_k, X_{k'}$ 的可区分性取决于它们的分布差异。定义可区分性度量：
58	
59	$$D(k, k') = d(P_{X_k}, P_{X_{k'}})$$
60	
61	其中 $d$ 是某种分布距离（JSD、MMD、Total Variation 等）。
62	
63	**关键观察**：随着 $k$ 增大，$P_{X_k}$ 趋近于信道 $\mathcal{T}$ 的不动点分布 $P^*$（如果存在），相邻深度的分布差异趋于零：
64	
65	$$D(k, k+1) \to 0 \quad \t
…[truncated 5826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T16:28:15.751688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/claim_routes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/claim_routes.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T16:28:15.751882+00:00_

1	# 双路线 Claim 框架
2	
3	> 根据 MVP 结果 K* 的取值，准备两条论文叙事路线。
4	
5	---
6	
7	## 路线 A：K* ≥ 3（MVP Pass）
8	
9	### Core Claim
10	**Generational depth estimation is feasible and enables graduated filtering that outperforms binary detection for quality-aware data curation.**
11	
12	### Supporting Claims 拆解
13	
14	**C1: Depth signals exist and are ordinal-structured**
15	- 递归生成文本的统计特征（surprisal、vocabulary diversity、tail metrics）随 depth 呈系统性单调变化
16	- Ordinal regression（CORAL/CORN）显著优于 multinomial classification，证明 depth 的有序结构可被利用
17	- 证据：pairwise AUC matrix、ordinal vs. multinomial ablation、calibration curves
18	
19	**C2: K* characterization reveals linguistic degradation ordering**
20	- K* 是首次被系统量化的判别饱和边界
21	- Feature group ablation 揭示"降解序"：不同语言维度（vocabulary diversity → surprisal dynamics → tail metrics）在不同 depth 饱和
22	- Heatmap：feature group × depth → discriminative power
23	- 证据：per-feature saturation curves、cross-model K* comparison、decoding strategy 对 K* 的调控效应
24	
25	**C3: Graduated filtering > binary filtering**
26	- Depth-aware weighted filtering（weight ∝ quality(k)/quality(0)）在 MMLU/HellaSwag 等 data-quality-sensitive tasks 上显著优于 binary filtering 和 no filtering
27	- 理论动机：binary filtering 在 threshold 附近信息损失最大，ordinal signal 允许 soft weighting
28	- 证据：downstream benchmark results with bootstrap CIs + paired significance tests、contamination severity ablation（10%/30%/50%）
29	
30	**C4: Cross-model generalization**
31	- 在 model A 上训练的 depth classifier 可迁移到 model B 的生成文本
32	- Cross-scale probe（7B/14B）验证小模型训练的特征在更大模型生成文本上的迁移性
33	- 证据：cross-model transfer accuracy matrix、feature distribution MMD analysis
34	
35	### Story Arc
36	
37	```
38	Problem:  Web data 被未知深度的递归合成文本污染，binary detection 丢失 graded quality signal
39	Insight:  递归生成是 iterated lossy channel，depth-discriminative signals 系统性存在且可量化
40	          → 类比 JPEG 重压缩检测
41	Method:   (1) 15维特征 + ordinal regression → depth estimation
42	          (2) Depth-graduated curation: weight ∝ estimated quality decay
43	Results:  K*≥3 → fine-grain
…[truncated 6127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T16:28:15.752039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T16:28:15.752335+00:00_

1	"""
2	MVP Pilot Saturation Study — Complete Pipeline (Steps 2-5)
3	
4	Generates recursive depth chains from C4 seed data using Qwen2.5-1.5B,
5	extracts statistical features, and runs distinguishability analysis.
6	
7	Input:  C4 validation split (streamed from HuggingFace)
8	Output: data/depth_{0..K}.jsonl, data/features.csv, results/*.json + summary.txt
9	
10	Key deps: torch, transformers, datasets, scipy, lightgbm, sklearn, tqdm
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import math
17	import os
18	import sys
19	from collections import Counter
20	from pathlib import Path
21	
22	import numpy as np
23	import torch
24	from scipy import stats
25	from tqdm import tqdm
26	
27	logging.basicConfig(
28	    level=logging.INFO,
29	    format="%(asctime)s [%(levelname)s] %(message)s",
30	    datefmt="%H:%M:%S",
31	)
32	log = logging.getLogger(__name__)
33	
34	
35	# ---------------------------------------------------------------------------
36	# Utility: simple 4-gram BLEU (no nltk dependency)
37	# ---------------------------------------------------------------------------
38	
39	def ngrams(tokens, n):
40	    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
41	
42	
43	def simple_bleu(candidate_tokens, reference_tokens, max_n=4):
44	    """Compute sentence-level BLEU up to max_n grams with brevity penalty."""
45	    if len(candidate_tokens) == 0:
46	        return 0.0
47	    precisions = []
48	    for n in range(1, max_n + 1):
49	        cand_ngrams = ngrams(candidate_tokens, n)
50	        ref_ngrams = ngrams(reference_tokens, n)
51	        if not cand_ngrams:
52	            precisions.append(0.0)
53	            continue
54	        ref_counts = Counter(ref_ngrams)
55	        clipped = 0
56	        cand_counts = Counter(cand_ngrams)
57	        for ng, cnt in cand_counts.items():
58	            clipped += min(cnt, ref_counts.get(ng, 0))
59	        precisions.append(clipped / len(cand_ngrams))
60	    if any(p == 0 for p in precisions):

…[truncated 23751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T16:28:15.752575+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md",
  "content": "# 3. Methodology\n\n## 3.1 Multi-generation Corpus Construction\n\n### 问题形式化\n\n设 $X_0$ 为人类撰写的文本（seed text），建模为概率空间上的随机变量。LLM 的生成过程定义为随机信道 $\\mathcal{T}: \\mathcal{X} \\to \\mathcal{X}$，将输入文本映射到输出文本。递归生成形成 Markov chain：\n\n$$X_0 \\xrightarrow{\\mathcal{T}} X_1 \\xrightarrow{\\mathcal{T}} X_2 \\xrightarrow{\\mathcal{T}} \\cdots \\xrightarrow{\\mathcal{T}} X_K$$\n\n其中 depth-0 文本 $X_0$ 为人类原始文本，depth-$k$ 文本 $X_k = \\mathcal{T}(X_{k-1})$ 由 depth-$(k-1)$ 文本经过一次 LLM 信道产生。该形式化依赖两个关键假设：**(A1) 时不变信道**——同一 LLM 与 decoding strategy 在每次迭代中定义相同的信道 $\\mathcal{T}$；**(A2) Markov 性**——$X_{k+1}$ 仅依赖 $X_k$，不依赖更早的 $X_0, \\ldots, X_{k-1}$。这两个假设在 prompt-chain 设定下成立（每次生成仅以上一轮输出为输入），retrain-chain 场景需将 $\\mathcal{T}$ 放宽为 $\\mathcal{T}_k$。\n\n### Prompt-chain 实现\n\n我们采用 prompt-chain 方式构造 depth chain：每一轮将前一深度的文本嵌入固定的 rewrite prompt 模板，由模型生成同主题、同风格的新文本。具体 prompt 模板如下：\n\n> Below is a passage. Write a new passage of similar length on the same topic and in the same style.\n>\n> Original passage:\n> {prev\\_text}\n>\n> New passage:\n\n该模板要求模型保持主题与风格一致性，同时生成全新文本而非简单复述。这一设计的意图是模拟现实场景中合成文本被反复改写的过程——例如 AI 生成的内容被爬取后再次作为 LLM 的输入进行改写或续写。\n\nPrompt-chain 与 retrain-chain（在合成数据上重新训练模型再生成）的区别值得说明。Retrain-chain 更接近 Shumailov et al. [2024] 描述的 model collapse 真实路径，但 prompt-chain 提供了一个 **upper bound estimate**：如果在 prompt-chain（模型权重不变、仅输入文本退化）下特征已饱和，retrain-chain（模型本身也退化）下只会更快饱和。我们选择 prompt-chain 作为 MVP 方案以控制变量，retrain-chain 验证留作后续研究。\n\n### 模型选择\n\n我们选用 **Qwen2.5-1.5B-Instruct** [Qwen Team, 2024] 作为生成模型。选择理由如下：\n\n**Instruct 而非 base 模型**。现实世界中绝大多数合成文本（ChatGPT 输出、AI 写作工具、自动摘要等）均来自经过 instruction tuning 的模型。使用 Instruct 版本可确保生成文本的分布特征更接近实际污染数据。此外，Instruct 模型能更好地遵循 rewrite prompt 中的改写指令，生成主题一致但非直接复制的文本，而 base 模型可能简单延续原文或产生不相关内容。\n\n**1.5B 参数规模**。选择小规模模型基于以下考量：(1) 计算效率——在单块 RTX 4090D (24GB) 上可高效完成 5000 文档 × 5 个深度的生成任务；(2) model collapse 文献 [Shumailov et al., 2024; Drayson et al., 2025] 表明退化现象在小模型上更为显著，有利于在 pilot study 中观察清晰的深度信号；(3) Qwen2.5 系列在 1.5B 规模上已展现出 competitive 的语言能力 [需验证]，足以生成流畅且有意义的文本。Full study 阶段将扩展到多模型家族（Pythia-1.4B, OLMo-1B）及更大规模（Qwen2.5-7B/14B）进行 cross-model 和 cross-scale 验证。\n\n### 解码参数\n\n采用 **nucleus sampling** (top-$p$ sampling)，参数设定为 $p = 0.95$, temperature $T = 1.0$。这一配置的理由在于：\n\n(1) **接近真实世界配置**。主流 LLM 应用（ChatGPT、Claude、各类 API 调用）的默认或推荐生成参数通常处于 $T \\in [0.7, 1.0]$, $p \\in [0.9, 0.95]$ 的区间。$T=1.0, p=0.95$ 代表了一个 moderately stochastic 的生成配置，既保留了足够的随机性以反映真实合成文本的 diversity，又不至于因过高 temperature 产生不自然的噪声文本。\n\n(2) **信道噪声的理论考量**。在信道级联框架下，$T$ 和 $p$ 共同决定了信道 $\\mathcal{T}$ 的 contraction rate $\\rho$。Greedy decoding ($T \\to 0$) 使信道趋近确定性（$\\rho \\to 1$），信息衰减慢但 diversity 低；高 temperature 使信道趋近均匀随机（$\\rho \\to 0$），信息快速丢失。$T=1.0, p=0.95$ 处于中间区域，既保证可观测的深度信号，又不人为加速或延缓饱和。\n\n### 种子数据\n\n种子数据取自 **C4 (Colossal Clean Crawled Corpus)** [Raffel et al., 2020] 的 validation split。从中采样 **5,000 篇文档**，每篇文档经 tokenizer 截断至 **256 tokens** 后作为 depth-0 文本。\n\n选择 C4 的理由：(1) 作为广泛使用的预训练语料，C4 文本代表了典型的 web 文本分布；(2) validation split 保证不与常见模型的训练集重叠。5,000 篇文档的规模在 pilot study 中足以提供可靠的统计估计，同时控制计算成本。\n\n截断至 256 tokens 的考量：(1) 控制生成长度一致性——过长的 seed text 导致生成文本长度方差大，干扰特征提取；(2) 256 tokens 足以包含 1-2 个完整段落的语义信息，保留主题和风格特征；(3) 与模型的 max prompt length 配合——prompt 模板 + seed text 需要在 512 tokens 内完成。\n\n### Left-padding 技术考量\n\n在 batch 推理中，我们采用 **left-padding** (`tokenizer.padding_side = \"left\"`)。这一选择对 causal language model 的生成质量至关重要：\n\nRight-padding（将 pad token 追加到序列末尾）会导致模型在生成时\"看到\"大量无意义的 pad token，影响注意力分布和生成质量。Left-padding 将 pad token 置于序列左侧，真实 token 右对齐，使得模型在生成时只关注到有意义的上下文。对于 Qwen2.5 等基于 causal attention 的模型，left-padding 是 batch generation 的标准做法，可确保生成质量与单样本推理一致。\n\n## 3.2 Feature Extraction Pipeline\n\n我们设计了三组共 15 维统计特征，分别从 token-level surprisal dynamics、sequence-level vocabulary diversity 和 distributional-level tail structure 三个层面刻画文本的统计属性。这三组特征的设计动机来自递归生成的已知退化机制：surprisal 分布反映模型对文本的\"预期程度\"随深度偏移 [DivEye, 2026]；词汇多样性是 model collapse 文献中最广泛记录的退化信号 [Shumailov et al., 2024]；频率分布尾部结构则捕捉 Zipf 分布的系统性变形 [Shumailov et al., 2024]。\n\n### 3.2.1 Surprisal Features (9D)\n\nSurprisal 衡量模型对观测到的 token 的\"惊讶程度\"。给定文本序列 $\\mathbf{x} = (x_1, x_2, \\ldots, x_n)$ 和语言模型 $p_\\theta$，token $x_t$ 的 surprisal 定义为：\n\n$$s(x_t) = -\\log p_\\theta(x_t \\mid x_{&lt;t})$$\n\n其中 $x_{&lt;t} = (x_1, \\ldots, x_{t-1})$ 为前缀上下文。\n\n**动机**：递归生成的文本倾向于更\"符合预期\"——每经过一次 LLM 信道，输出文本的 token 分布趋近模型的先验偏好，surprisal 分布整体向低值偏移。这一趋势反映了信道级联中互信息 $I(X_0; X_k)$ 随深度单调衰减的理论预测。\n\n我们从 surprisal 序列 $\\{s(x_t)\\}_{t=2}^{n}$ 中提取以下统计量：\n\n**基础统计量 (4D)**：\n- $\\mu_s = \\frac{1}{n-1}\\sum_{t=2}^{n} s(x_t)$ — surprisal 均值，反映文本整体的可预测程度\n- $\\sigma_s = \\text{std}(\\{s(x_t)\\})$ — surprisal 标准差，反映 token 间可预测性的变异程度\n- $\\gamma_s = \\text{skewness}(\\{s(x_t)\\})$ — 偏度，捕捉 surprisal 分布的不对称性\n- $\\kappa_s = \\text{kurtosis}(\\{s(x_t)\\})$ — 峰度，捕捉 surprisal 分布的尾部厚度\n\n**一阶差分统计量 (3D)**：定义一阶差分 $\\Delta s_t = s(x_{t+1}) - s(x_t)$，反映相邻 token 间 surprisal 的局部变化动态。提取：\n- $\\mu_{\\Delta s}$ — 一阶差分均值\n- $\\sigma_{\\Delta s}$ — 一阶差分标准差\n- $\\gamma_{\\Delta s}$ — 一阶差分偏度（当 $|\\Delta s| \\geq 3$ 时计算，否则置为 0）\n\n**二阶差分统计量 (2D)**：定义二阶差分 $\\Delta^2 s_t = \\Delta s_{t+1} - \\Delta s_t$，捕捉 surprisal 变化的加速度。提取：\n- $\\mu_{\\Delta^2 s}$ — 二阶差分均值\n- $\\sigma_{\\Delta^2 s}$ — 二阶差分标准差\n\n一阶和二阶差分的引入受 DivEye [2026] 的启发——它们捕捉 surprisal 的 **temporal dynamics** 而非仅仅 distributional shape，能够反映递归生成文本中 token-level 可预测性的局部模式变化。\n\n**实现细节**：Surprisal 通过同一生成模型（Qwen2.5-1.5B-Instruct）计算。对于每个 token $x_t$，我们使用模型在前缀 $x_{&lt;t}$ 上的 logits 取 log-softmax 后的负对数概率。序列长度不足 3 个 token 的样本各维度置 0。计算采用 batch 推理（batch size = 8），使用 FP16 精度以控制显存占用。\n\n### 3.2.2 Vocabulary Diversity Features (3D)\n\n词汇多样性特征从 sequence level 衡量文本的词汇丰富度和重复模式。\n\n**Type-Token Ratio (TTR)**：\n\n$$\\text{TTR} = \\frac{|\\mathcal{V}(\\mathbf{x})|}{|\\mathbf{x}|}$$\n\n其中 $\\mathcal{V}(\\mathbf{x})$ 为文本 $\\mathbf{x}$ 中出现的不同词 (types) 的集合，$|\\mathbf{x}|$ 为总词数 (tokens)。TTR 越低，词汇重复度越高。\n\n**Hapax Ratio**：\n\n$$\\text{Hapax} = \\frac{|\\{w \\in \\mathcal{V}(\\mathbf{x}) : \\text{freq}(w) = 1\\}|}{|\\mathcal{V}(\\mathbf{x})|}$$\n\n即只出现一次的词 (hapax legomena) 占全部不同词的比例。Hapax ratio 对词频分布的尾部敏感——递归生成的尾部消失 (tail disappearance) 直接表现为 hapax ratio 下降。\n\n**Self-BLEU**：\n\n$$\\text{Self-BLEU}(\\mathbf{x}_i) = \\frac{1}{|R|} \\sum_{j \\in R} \\text{BLEU}_4(\\mathbf{x}_i, \\mathbf{x}_j)$$\n\n其中 $R$ 是从同一 depth 随机采样的参考文本集合（$|R| = 100$），$\\text{BLEU}_4$ 为标准的 4-gram BLEU score（含 brevity penalty）。Self-BLEU 衡量同一 depth 内不同文档间的 n-gram 重叠程度。\n\n**动机**：Self-BLEU 越高，说明同一深度的文本之间越相似——这正是递归生成导致的 progressive homogenization [Drayson et al., 2025] 的直接度量。与 TTR 和 Hapax ratio 关注单文档内部的多样性不同，Self-BLEU 捕捉的是同深度文档 **之间** 的多样性坍缩。\n\n**实现细节**：TTR 和 Hapax ratio 基于 whitespace tokenization（空格分词）在 word level 计算。Self-BLEU 的参考集从同深度文本中随机采样 100 篇（固定随机种子以保证可复现性），使用不依赖 NLTK 的轻量 4-gram BLEU 实现。\n\n### 3.2.3 Tail-thinning Features (3D)\n\n尾部稀疏特征从 distributional level 刻画文本词频分布的 Zipf 结构变化。\n\n**Frequency Kurtosis**：\n\n$$\\kappa_f = \\text{kurtosis}(\\{c_w : w \\in \\mathcal{V}(\\mathbf{x})\\})$$\n\n其中 $c_w = \\text{freq}(w, \\mathbf{x})$ 为词 $w$ 在文本 $\\mathbf{x}$ 中的出现次数。Kurtosis 衡量词频分布的尖峰和厚尾程度。当 unique types 不足 4 时置 0。\n\n**Frequency Entropy**：\n\n$$H_f = -\\sum_{w \\in \\mathcal{V}(\\mathbf{x})} \\hat{p}(w) \\log_2 \\hat{p}(w)$$\n\n其中 $\\hat{p}(w) = c_w / \\sum_{w'} c_{w'}$ 为 empirical unigram probability。Frequency entropy 衡量词频分布的均匀程度——entropy 越高，词频分布越接近均匀（diversity 越高）。\n\n**Low-frequency Ratio**：\n\n$$\\text{LFR} = \\frac{|\\{w \\in \\mathcal{V}(\\mathbf{x}) : c_w = 1\\}|}{|\\mathcal{V}(\\mathbf{x})|}$$\n\n即频次为 1 的词占所有 unique types 的比例。\n\n**动机**：Shumailov et al. [2024] 将 model collapse 分为三个阶段：tail disappearance → diversity loss → mode conflation。Tail-thinning features 直接刻画第一阶段——随着递归深度增加，词频分布的长尾逐渐消失，frequency kurtosis 下降（分布趋向扁平），frequency entropy 降低（分布集中于高频词），low-frequency ratio 减小（罕见词消失）。这些特征与 surprisal features 互补：surprisal 反映模型视角下的可预测性变化，而 tail-thinning 反映文本自身词频分布的结构性退化。\n\n**实现细节**：基于 whitespace tokenization 的词频统计。Entropy 计算中添加 $10^{-12}$ 的 smoothing 以避免 log(0)。\n\n### 特征总结\n\n| 特征组 | 维度 | 特征名 | 捕捉的退化信号 |\n|--------|------|--------|--------------|\n| Surprisal | 9 | surp\\_mean, surp\\_std, surp\\_skew, surp\\_kurt, surp\\_d1\\_mean, surp\\_d1\\_std, surp\\_d1\\_skew, surp\\_d2\\_mean, surp\\_d2\\_std | Token-level 可预测性偏移与动态变化 |\n| Vocab Diversity | 3 | ttr, hapax\\_ratio, self\\_bleu | 词汇丰富度衰减与文档间同质化 |\n| Tail-thinning | 3 | freq\\_kurtosis, freq\\_entropy, low\\_freq\\_ratio | Zipf 尾部消失与频率分布集中化 |\n\n全部 15 维特征均在 inference 时可计算（不依赖 paired original text 或跨深度信息），满足实际部署中仅有待检测文本可用的约束。\n\n## 3.3 Ordinal Depth Classifier\n\n### 分类器选择：LightGBM\n\n我们选用 **LightGBM** [Ke et al., 2017] 作为 depth classification 的 baseline 分类器。在 tabular features（低维手工特征）场景下，gradient boosted decision trees (GBDT) 通常优于或 comparable to 深度学习方法 [Grinsztajn et al., 2022, 需验证]，同时提供以下关键优势：\n\n(1) **可解释性**：LightGBM 原生提供 feature importance（基于 split gain 或 split count），使我们能够分析哪些特征对 depth discrimination 贡献最大，进而揭示递归生成的 linguistic degradation ordering。\n\n(2) **训练效率**：15 维特征 × 30,000 样本（5,000 docs × 6 depths）的规模下，LightGBM 训练仅需秒级时间，支持大量 ablation 实验和 cross-validation。\n\n(3) **对特征分布的鲁棒性**：GBDT 对特征缩放不敏感、能自然处理非线性关系和特征交互，无需额外的特征工程或归一化。\n\n### 任务设定\n\n我们在两个粒度上评估 depth discrimination 能力：\n\n**Pairwise Binary Classification**：对每对相邻深度 $(k-1, k)$，训练独立的二分类器。输入为 15 维特征向量，输出为 $\\{k-1, k\\}$ 的深度标签。pairwise AUC 是衡量相邻深度可区分性的核心指标，直接用于 $K^*$ 的计算。\n\n分类器参数：`n_estimators=200, max_depth=6, learning_rate=0.05, num_leaves=31`。\n\n**Ordinal Multi-class Classification**：将全部 6 个深度 (depth 0--5) 作为一个有序多分类问题。使用 LightGBM 的 `multiclass` objective，参数设为 `n_estimators=300, max_depth=8, num_leaves=63`。\n\n### 评估协议\n\n所有实验采用 **5-fold stratified cross-validation**。Stratified split 确保每个 fold 中各深度类别的比例一致。\n\n[TODO: grouped by doc\\_id 的实现——当前代码使用 StratifiedKFold 但未按 doc\\_id 分组。严格来说，同一 doc\\_id 在不同 depth 的文本应当被分配到同一 fold，以避免同源文档信息在训练集和测试集间泄露。这是一个需要在正式实验中修复的设计点。]\n\n### 评估指标\n\n- **Pairwise AUC**：每对相邻深度的 ROC-AUC，5-fold 均值和标准差。这是最核心的指标，直接反映每一步递归生成引入的 distributional shift 是否可被统计特征捕捉。\n\n- **MAE (Mean Absolute Error)**：ordinal classification 的预测深度与真实深度之差的均值。MAE 对 ordinal 结构敏感——将 depth-0 误分为 depth-1（MAE=1）比误分为 depth-5（MAE=5）惩罚更轻，符合\"相邻深度更难区分\"的直觉。\n\n- **Accuracy**：ordinal classification 的精确匹配准确率。\n\n- **Feature Importance**：LightGBM 的 split-based feature importance，按贡献排序，用于分析哪些特征组（surprisal / vocab diversity / tail-thinning）在 depth discrimination 中最为关键。\n\n## 3.4 Saturation Boundary $K^*$\n\n### 操作性定义\n\n我们定义 **判别饱和边界 (discriminability saturation boundary)** $K^*$ 为：\n\n$$K^* = \\max\\{k : \\text{AUC}(\\text{depth } k{-}1 \\text{ vs } k) > 0.60\\}$$\n\n即 $K^*$ 是满足相邻深度 pairwise AUC 大于 0.60 的最大深度。$K^*$ 之后（depth $> K^*$），相邻深度的文本在 15 维特征空间中不再具有可靠的统计可区分性。\n\n### 阈值选择理由\n\n选择 0.60 作为阈值基于以下考量：\n\n(1) **与 chance level 的间距**。二分类的 chance AUC = 0.50。阈值 0.60 对应 Cohen's $d$ [TODO: 计算对应效应量] 的 small-to-medium effect size，表示 \"微弱但可靠的可区分性\"。\n\n(2) **实践意义**。AUC = 0.60 意味着在随机抽取一对（depth $k{-}1$, depth $k$）样本时，分类器有 60% 的概率正确排序——略好于随机猜测，但已可为 downstream curation 提供有意义的信号。\n\n(3) **保守性**。相比更高阈值（如 0.70），0.60 允许更多深度被纳入\"可区分\"范围，使 $K^*$ 的估计偏向乐观。如果在此保守阈值下 $K^*$ 仍然较小，则更加确证了 depth discrimination 的 fundamental limit。\n\n### 与 DPI 理论的联系\n\n在信道级联框架下，$K^*$ 有明确的 information-theoretic 解释。由 Data Processing Inequality (DPI)，对 Markov chain $X_0 \\to X_1 \\to \\cdots \\to X_K$，有：\n\n$$I(X_0; X_k) \\leq I(X_0; X_{k-1}) \\leq \\cdots \\leq I(X_0; X_1) \\leq H(X_0)$$\n\n即关于原始人类文本 $X_0$ 的信息量随递归深度 **单调非递增**。每经过一次 LLM 信道 $\\mathcal{T}$（假设为 strictly lossy channel，即任何 temperature > 0 或 nucleus 截断都引入不可逆信息损失），互信息严格递减。\n\n$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度——不是分类器的能力上限，而是 **information-theoretic impossibility boundary**：任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已被信道噪声完全淹没。\n\n形式化地，若信道 $\\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（即 $d(\\mathcal{T}(P), \\mathcal{T}(Q)) \\leq \\rho \\cdot d(P, Q)$，$0 < \\rho < 1$），则 $P_{X_k}$ 以几何速率趋近不动点分布 $P^*$：\n\n$$d(P_{X_k}, P^*) \\leq \\rho^k \\cdot d(P_{X_0}, P^*)$$\n\n相邻深度的分布差异同样以几何速率趋零：\n\n$$D(k, k{+}1) \\leq (\\rho^k + \\rho^{k+1}) \\cdot d(P_{X_0}, P^*)$$\n\n从而 $K^*(\\epsilon)$ 对任意阈值 $\\epsilon > 0$ 必然有限，其粗略 scaling 为：\n\n$$K^* = O\\left(\\frac{\\log(d(P_{X_0}, P^*) / \\epsilon)}{\\log(1/\\rho)}\\right)$$\n\n这表明 $K^*$ 由信道的 contraction rate $\\rho$ 和 seed 文本分布到不动点的初始距离共同决定。\n\n### 经验验证方法\n\n我们使用 pairwise AUC 作为 discriminability 的 empirical proxy，配合 Jensen-Shannon Divergence (JSD) 作为 distributional distance 的 computationally tractable proxy：\n\n$$\\text{JSD}(P_{X_k} \\| P_{X_{k'}}) = \\frac{1}{2} D_{\\text{KL}}(P_{X_k} \\| M) + \\frac{1}{2} D_{\\text{KL}}(P_{X_{k'}} \\| M)$$\n\n其中 $M = \\frac{1}{2}(P_{X_k} + P_{X_{k'}})$。JSD 在 unigram level 上按 feature 维度分别计算（基于 50-bin 直方图估计），取均值作为综合度量。\n\n需要承认的局限：unigram-level JSD 忽略了序列结构（n-gram patterns、句法依赖等），不等价于真正的互信息 $I(X_0; X_k)$。但 DPI 的定性结论——单调衰减——在 JSD 框架下同样成立，因此作为 tracking metric 仍然有效。\n\n### $K^*$ 的科学意义\n\n$K^*$ 是本工作提出的首次被系统测量的科学量。此前关于递归生成退化的研究 [Shumailov et al., 2024; Drayson et al., 2025] 主要提供定性描述（\"early generations show most change\"），但从未给出精确的判别边界。$K^*$ 的测量具有直接的实践指导价值：\n\n- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。\n- **对 model collapse 研究**：$K^*$ 量化了 Shumailov et al. 描述的 \"early collapse\" 与 \"late collapse\" 之间的精确过渡边界。\n- **对 AI 生成文本检测**：$K^*$ 揭示了 depth estimation 作为检测范式的 fundamental resolution limit——无论特征工程或分类器如何改进，信息论约束决定了 $K^*$ 之外不可能做得更好。\n\n[TODO: 补充 MVP 实验中测得的 $K^*$ 实际值及其置信区间]\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md",
    "content": "# 3. Methodology\n\n## 3.1 Multi-generation Corpus Construction\n\n### 问题形式化\n\n设 $X_0$ 为人类撰写的文本（seed text），建模为概率空间上的随机变量。LLM 的生成过程定义为随机信道 $\\mathcal{T}: \\mathcal{X} \\to \\mathcal{X}$，将输入文本映射到输出文本。递归生成形成 Markov chain：\n\n$$X_0 \\xrightarrow{\\mathcal{T}} X_1 \\xrightarrow{\\mathcal{T}} X_2 \\xrightarrow{\\mathcal{T}} \\cdots \\xrightarrow{\\mathcal{T}} X_K$$\n\n其中 depth-0 文本 $X_0$ 为人类原始文本，depth-$k$ 文本 $X_k = \\mathcal{T}(X_{k-1})$ 由 depth-$(k-1)$ 文本经过一次 LLM 信道产生。该形式化依赖两个关键假设：**(A1) 时不变信道**——同一 LLM 与 decoding strategy 在每次迭代中定义相同的信道 $\\mathcal{T}$；**(A2) Markov 性**——$X_{k+1}$ 仅依赖 $X_k$，不依赖更早的 $X_0, \\ldots, X_{k-1}$。这两个假设在 prompt-chain 设定下成立（每次生成仅以上一轮输出为输入），retrain-chain 场景需将 $\\mathcal{T}$ 放宽为 $\\mathcal{T}_k$。\n\n### Prompt-chain 实现\n\n我们采用 prompt-chain 方式构造 depth chain：每一轮将前一深度的文本嵌入固定的 rewrite prompt 模板，由模型生成同主题、同风格的新文本。具体 prompt 模板如下：\n\n> Below is a passage. Write a new passage of similar length on the same topic and in the same style.\n>\n> Original passage:\n> {prev\\_text}\n>\n> New passage:\n\n该模板要求模型保持主题与风格一致性，同时生成全新文本而非简单复述。这一设计的意图是模拟现实场景中合成文本被反复改写的过程——例如 AI 生成的内容被爬取后再次作为 LLM 的输入进行改写或续写。\n\nPrompt-chain 与 retrain-chain（在合成数据上重新训练模型再生成）的区别值得说明。Retrain-chain 更接近 Shumailov et al. [2024] 描述的 model collapse 真实路径，但 prompt-chain 提供了一个 **upper bound estimate**：如果在 prompt-chain（模型权重不变、仅输入文本退化）下特征已饱和，retrain-chain（模型本身也退化）下只会更快饱和。我们选择 prompt-chain 作为 MVP 方案以控制变量，retrain-chain 验证留作后续研究。\n\n### 模型选择\n\n我们选用 **Qwen2.5-1.5B-Instruct** [Qwen Team, 2024] 作为生成模型。选择理由如下：\n\n**Instruct 而非 base 模型**。现实世界中绝大多数合成文本（ChatGPT 输出、AI 写作工具、自动摘要等）均来自经过 instruction tuning 的模型。使用 Instruct 版本可确保生成文本的分布特征更接近实际污染数据。此外，Instruct 模型能更好地遵循 rewrite prompt 中的改写指令，生成主题一致但非直接复制的文本，而 base 模型可能简单延续原文或产生不相关内容。\n\n**1.5B 参数规模**。选择小规模模型基于以下考量：(1) 计算效率——在单块 RTX 4090D (24GB) 上可高效完成 5000 文档 × 5 个深度的生成任务；(2) model collapse 文献 [Shumailov et al., 2024; Drayson et al., 2025] 表明退化现象在小模型上更为显著，有利于在 pilot study 中观察清晰的深度信号；(3) Qwen2.5 系列在 1.5B 规模上已展现出 competitive 的语言能力 [需验证]，足以生成流畅且有意义的文本。Full study 阶段将扩展到多模型家族（Pythia-1.4B, OLMo-1B）及更大规模（Qwen2.5-7B/14B）进行 cross-model 和 cross-scale 验证。\n\n### 解码参数\n\n采用 **nucleus sampling** (top-$p$ sampling)，参数设定为 $p = 0.95$, temperature $T = 1.0$。这一配置的理由在于：\n\n(1) **接近真实世界配置**。主流 LLM 应用（ChatGPT、Claude、各类 API 调用）的默认或推荐生成参数通常处于 $T \\in [0.7, 1.0]$, $p \\in [0.9, 0.95]$ 的区间。$T=1.0, p=0.95$ 代表了一个 moderately stochastic 的生成配置，既保留了足够的随机性以反映真实合成文本的 diversity，又不至于因过高 temperature 产生不自然的噪声文本。\n\n(2) **信道噪声的理论考量**。在信道级联框架下，$T$ 和 $p$ 共同决定了信道 $\\mathcal{T}$ 的 contraction rate $\\rho$。Greedy decoding ($T \\to 0$) 使信道趋近确定性（$\\rho \\to 1$），信息衰减慢但 diversity 低；高 temperature 使信道趋近均匀随机（$\\rho \\to 0$），信息快速丢失。$T=1.0, p=0.95$ 处于中间区域，既保证可观测的深度信号，又不人为加速或延缓饱和。\n\n### 种子数据\n\n种子数据取自 **C4 (Colossal Clean Crawled Corpus)** [Raffel et al., 2020] 的 validation split。从中采样 **5,000 篇文档**，每篇文档经 tokenizer 截断至 **256 tokens** 后作为 depth-0 文本。\n\n选择 C4 的理由：(1) 作为广泛使用的预训练语料，C4 文本代表了典型的 web 文本分布；(2) validation split 保证不与常见模型的训练集重叠。5,000 篇文档的规模在 pilot study 中足以提供可靠的统计估计，同时控制计算成本。\n\n截断至 256 tokens 的考量：(1) 控制生成长度一致性——过长的 seed text 导致生成文本长度方差大，干扰特征提取；(2) 256 tokens 足以包含 1-2 个完整段落的语义信息，保留主题和风格特征；(3) 与模型的 max prompt length 配合——prompt 模板 + seed text 需要在 512 tokens 内完成。\n\n### Left-padding 技术考量\n\n在 batch 推理中，我们采用 **left-padding** (`tokenizer.padding_side = \"left\"`)。这一选择对 causal language model 的生成质量至关重要：\n\nRight-padding（将 pad token 追加到序列末尾）会导致模型在生成时\"看到\"大量无意义的 pad token，影响注意力分布和生成质量。Left-padding 将 pad token 置于序列左侧，真实 token 右对齐，使得模型在生成时只关注到有意义的上下文。对于 Qwen2.5 等基于 causal attention 的模型，left-padding 是 batch generation 的标准做法，可确保生成质量与单样本推理一致。\n\n## 3.2 Feature Extraction Pipeline\n\n我们设计了三组共 15 维统计特征，分别从 token-level surprisal dynamics、sequence-level vocabulary diversity 和 distributional-level tail structure 三个层面刻画文本的统计属性。这三组特征的设计动机来自递归生成的已知退化机制：surprisal 分布反映模型对文本的\"预期程度\"随深度偏移 [DivEye, 2026]；词汇多样性是 model collapse 文献中最广泛记录的退化信号 [Shumailov et al., 2024]；频率分布尾部结构则捕捉 Zipf 分布的系统性变形 [Shumailov et al., 2024]。\n\n### 3.2.1 Surprisal Features (9D)\n\nSurprisal 衡量模型对观测到的 token 的\"惊讶程度\"。给定文本序列 $\\mathbf{x} = (x_1, x_2, \\ldots, x_n)$ 和语言模型 $p_\\theta$，token $x_t$ 的 surprisal 定义为：\n\n$$s(x_t) = -\\log p_\\theta(x_t \\mid x_{&lt;t})$$\n\n其中 $x_{&lt;t} = (x_1, \\ldots, x_{t-1})$ 为前缀上下文。\n\n**动机**：递归生成的文本倾向于更\"符合预期\"——每经过一次 LLM 信道，输出文本的 token 分布趋近模型的先验偏好，surprisal 分布整体向低值偏移。这一趋势反映了信道级联中互信息 $I(X_0; X_k)$ 随深度单调衰减的理论预测。\n\n我们从 surprisal 序列 $\\{s(x_t)\\}_{t=2}^{n}$ 中提取以下统计量：\n\n**基础统计量 (4D)**：\n- $\\mu_s = \\frac{1}{n-1}\\sum_{t=2}^{n} s(x_t)$ — surprisal 均值，反映文本整体的可预测程度\n- $\\sigma_s = \\text{std}(\\{s(x_t)\\})$ — surprisal 标准差，反映 token 间可预测性的变异程度\n- $\\gamma_s = \\text{skewness}(\\{s(x_t)\\})$ — 偏度，捕捉 surprisal 分布的不对称性\n- $\\kappa_s = \\text{kurtosis}(\\{s(x_t)\\})$ — 峰度，捕捉 surprisal 分布的尾部厚度\n\n**一阶差分统计量 (3D)**：定义一阶差分 $\\Delta s_t = s(x_{t+1}) - s(x_t)$，反映相邻 token 间 surprisal 的局部变化动态。提取：\n- $\\mu_{\\Delta s}$ — 一阶差分均值\n- $\\sigma_{\\Delta s}$ — 一阶差分标准差\n- $\\gamma_{\\Delta s}$ — 一阶差分偏度（当 $|\\Delta s| \\geq 3$ 时计算，否则置为 0）\n\n**二阶差分统计量 (2D)**：定义二阶差分 $\\Delta^2 s_t = \\Delta s_{t+1} - \\Delta s_t$，捕捉 surprisal 变化的加速度。提取：\n- $\\mu_{\\Delta^2 s}$ — 二阶差分均值\n- $\\sigma_{\\Delta^2 s}$ — 二阶差分标准差\n\n一阶和二阶差分的引入受 DivEye [2026] 的启发——它们捕捉 surprisal 的 **temporal dynamics** 而非仅仅 distributional shape，能够反映递归生成文本中 token-level 可预测性的局部模式变化。\n\n**实现细节**：Surprisal 通过同一生成模型（Qwen2.5-1.5B-Instruct）计算。对于每个 token $x_t$，我们使用模型在前缀 $x_{&lt;t}$ 上的 logits 取 log-softmax 后的负对数概率。序列长度不足 3 个 token 的样本各维度置 0。计算采用 batch 推理（batch size = 8），使用 FP16 精度以控制显存占用。\n\n### 3.2.2 Vocabulary Diversity Features (3D)\n\n词汇多样性特征从 sequence level 衡量文本的词汇丰富度和重复模式。\n\n**Type-Token Ratio (TTR)**：\n\n$$\\text{TTR} = \\frac{|\\mathcal{V}(\\mathbf{x})|}{|\\mathbf{x}|}$$\n\n其中 $\\mathcal{V}(\\mathbf{x})$ 为文本 $\\mathbf{x}$ 中出现的不同词 (types) 的集合，$|\\mathbf{x}|$ 为总词数 (tokens)。TTR 越低，词汇重复度越高。\n\n**Hapax Ratio**：\n\n$$\\text{Hapax} = \\frac{|\\{w \\in \\mathcal{V}(\\mathbf{x}) : \\text{freq}(w) = 1\\}|}{|\\mathcal{V}(\\mathbf{x})|}$$\n\n即只出现一次的词 (hapax legomena) 占全部不同词的比例。Hapax ratio 对词频分布的尾部敏感——递归生成的尾部消失 (tail disappearance) 直接表现为 hapax ratio 下降。\n\n**Self-BLEU**：\n\n$$\\text{Self-BLEU}(\\mathbf{x}_i) = \\frac{1}{|R|} \\sum_{j \\in R} \\text{BLEU}_4(\\mathbf{x}_i, \\mathbf{x}_j)$$\n\n其中 $R$ 是从同一 depth 随机采样的参考文本集合（$|R| = 100$），$\\text{BLEU}_4$ 为标准的 4-gram BLEU score（含 brevity penalty）。Self-BLEU 衡量同一 depth 内不同文档间的 n-gram 重叠程度。\n\n**动机**：Self-BLEU 越高，说明同一深度的文本之间越相似——这正是递归生成导致的 progressive homogenization [Drayson et al., 2025] 的直接度量。与 TTR 和 Hapax ratio 关注单文档内部的多样性不同，Self-BLEU 捕捉的是同深度文档 **之间** 的多样性坍缩。\n\n**实现细节**：TTR 和 Hapax ratio 基于 whitespace tokenization（空格分词）在 word level 计算。Self-BLEU 的参考集从同深度文本中随机采样 100 篇（固定随机种子以保证可复现性），使用不依赖 NLTK 的轻量 4-gram BLEU 实现。\n\n### 3.2.3 Tail-thinning Features (3D)\n\n尾部稀疏特征从 distributional level 刻画文本词频分布的 Zipf 结构变化。\n\n**Frequency Kurtosis**：\n\n$$\\kappa_f = \\text{kurtosis}(\\{c_w : w \\in \\mathcal{V}(\\mathbf{x})\\})$$\n\n其中 $c_w = \\text{freq}(w, \\mathbf{x})$ 为词 $w$ 在文本 $\\mathbf{x}$ 中的出现次数。Kurtosis 衡量词频分布的尖峰和厚尾程度。当 unique types 不足 4 时置 0。\n\n**Frequency Entropy**：\n\n$$H_f = -\\sum_{w \\in \\mathcal{V}(\\mathbf{x})} \\hat{p}(w) \\log_2 \\hat{p}(w)$$\n\n其中 $\\hat{p}(w) = c_w / \\sum_{w'} c_{w'}$ 为 empirical unigram probability。Frequency entropy 衡量词频分布的均匀程度——entropy 越高，词频分布越接近均匀（diversity 越高）。\n\n**Low-frequency Ratio**：\n\n$$\\text{LFR} = \\frac{|\\{w \\in \\mathcal{V}(\\mathbf{x}) : c_w = 1\\}|}{|\\mathcal{V}(\\mathbf{x})|}$$\n\n即频次为 1 的词占所有 unique types 的比例。\n\n**动机**：Shumailov et al. [2024] 将 model collapse 分为三个阶段：tail disappearance → diversity loss → mode conflation。Tail-thinning features 直接刻画第一阶段——随着递归深度增加，词频分布的长尾逐渐消失，frequency kurtosis 下降（分布趋向扁平），frequency entropy 降低（分布集中于高频词），low-frequency ratio 减小（罕见词消失）。这些特征与 surprisal features 互补：surprisal 反映模型视角下的可预测性变化，而 tail-thinning 反映文本自身词频分布的结构性退化。\n\n**实现细节**：基于 whitespace tokenization 的词频统计。Entropy 计算中添加 $10^{-12}$ 的 smoothing 以避免 log(0)。\n\n### 特征总结\n\n| 特征组 | 维度 | 特征名 | 捕捉的退化信号 |\n|--------|------|--------|--------------|\n| Surprisal | 9 | surp\\_mean, surp\\_std, surp\\_skew, surp\\_kurt, surp\\_d1\\_mean, surp\\_d1\\_std, surp\\_d1\\_skew, surp\\_d2\\_mean, surp\\_d2\\_std | Token-level 可预测性偏移与动态变化 |\n| Vocab Diversity | 3 | ttr, hapax\\_ratio, self\\_bleu | 词汇丰富度衰减与文档间同质化 |\n| Tail-thinning | 3 | freq\\_kurtosis, freq\\_entropy, low\\_freq\\_ratio | Zipf 尾部消失与频率分布集中化 |\n\n全部 15 维特征均在 inference 时可计算（不依赖 paired original text 或跨深度信息），满足实际部署中仅有待检测文本可用的约束。\n\n## 3.3 Ordinal Depth Classifier\n\n### 分类器选择：LightGBM\n\n我们选用 **LightGBM** [Ke et al., 2017] 作为 depth classification 的 baseline 分类器。在 tabular features（低维手工特征）场景下，gradient boosted decision trees (GBDT) 通常优于或 comparable to 深度学习方法 [Grinsztajn et al., 2022, 需验证]，同时提供以下关键优势：\n\n(1) **可解释性**：LightGBM 原生提供 feature importance（基于 split gain 或 split count），使我们能够分析哪些特征对 depth discrimination 贡献最大，进而揭示递归生成的 linguistic degradation ordering。\n\n(2) **训练效率**：15 维特征 × 30,000 样本（5,000 docs × 6 depths）的规模下，LightGBM 训练仅需秒级时间，支持大量 ablation 实验和 cross-validation。\n\n(3) **对特征分布的鲁棒性**：GBDT 对特征缩放不敏感、能自然处理非线性关系和特征交互，无需额外的特征工程或归一化。\n\n### 任务设定\n\n我们在两个粒度上评估 depth discrimination 能力：\n\n**Pairwise Binary Classification**：对每对相邻深度 $(k-1, k)$，训练独立的二分类器。输入为 15 维特征向量，输出为 $\\{k-1, k\\}$ 的深度标签。pairwise AUC 是衡量相邻深度可区分性的核心指标，直接用于 $K^*$ 的计算。\n\n分类器参数：`n_estimators=200, max_depth=6, learning_rate=0.05, num_leaves=31`。\n\n**Ordinal Multi-class Classification**：将全部 6 个深度 (depth 0--5) 作为一个有序多分类问题。使用 LightGBM 的 `multiclass` objective，参数设为 `n_estimators=300, max_depth=8, num_leaves=63`。\n\n### 评估协议\n\n所有实验采用 **5-fold stratified cross-validation**。Stratified split 确保每个 fold 中各深度类别的比例一致。\n\n[TODO: grouped by doc\\_id 的实现——当前代码使用 StratifiedKFold 但未按 doc\\_id 分组。严格来说，同一 doc\\_id 在不同 depth 的文本应当被分配到同一 fold，以避免同源文档信息在训练集和测试集间泄露。这是一个需要在正式实验中修复的设计点。]\n\n### 评估指标\n\n- **Pairwise AUC**：每对相邻深度的 ROC-AUC，5-fold 均值和标准差。这是最核心的指标，直接反映每一步递归生成引入的 distributional shift 是否可被统计特征捕捉。\n\n- **MAE (Mean Absolute Error)**：ordinal classification 的预测深度与真实深度之差的均值。MAE 对 ordinal 结构敏感——将 depth-0 误分为 depth-1（MAE=1）比误分为 depth-5（MAE=5）惩罚更轻，符合\"相邻深度更难区分\"的直觉。\n\n- **Accuracy**：ordinal classification 的精确匹配准确率。\n\n- **Feature Importance**：LightGBM 的 split-based feature importance，按贡献排序，用于分析哪些特征组（surprisal / vocab diversity / tail-thinning）在 depth discrimination 中最为关键。\n\n## 3.4 Saturation Boundary $K^*$\n\n### 操作性定义\n\n我们定义 **判别饱和边界 (discriminability saturation boundary)** $K^*$ 为：\n\n$$K^* = \\max\\{k : \\text{AUC}(\\text{depth } k{-}1 \\text{ vs } k) > 0.60\\}$$\n\n即 $K^*$ 是满足相邻深度 pairwise AUC 大于 0.60 的最大深度。$K^*$ 之后（depth $> K^*$），相邻深度的文本在 15 维特征空间中不再具有可靠的统计可区分性。\n\n### 阈值选择理由\n\n选择 0.60 作为阈值基于以下考量：\n\n(1) **与 chance level 的间距**。二分类的 chance AUC = 0.50。阈值 0.60 对应 Cohen's $d$ [TODO: 计算对应效应量] 的 small-to-medium effect size，表示 \"微弱但可靠的可区分性\"。\n\n(2) **实践意义**。AUC = 0.60 意味着在随机抽取一对（depth $k{-}1$, depth $k$）样本时，分类器有 60% 的概率正确排序——略好于随机猜测，但已可为 downstream curation 提供有意义的信号。\n\n(3) **保守性**。相比更高阈值（如 0.70），0.60 允许更多深度被纳入\"可区分\"范围，使 $K^*$ 的估计偏向乐观。如果在此保守阈值下 $K^*$ 仍然较小，则更加确证了 depth discrimination 的 fundamental limit。\n\n### 与 DPI 理论的联系\n\n在信道级联框架下，$K^*$ 有明确的 information-theoretic 解释。由 Data Processing Inequality (DPI)，对 Markov chain $X_0 \\to X_1 \\to \\cdots \\to X_K$，有：\n\n$$I(X_0; X_k) \\leq I(X_0; X_{k-1}) \\leq \\cdots \\leq I(X_0; X_1) \\leq H(X_0)$$\n\n即关于原始人类文本 $X_0$ 的信息量随递归深度 **单调非递增**。每经过一次 LLM 信道 $\\mathcal{T}$（假设为 strictly lossy channel，即任何 temperature > 0 或 nucleus 截断都引入不可逆信息损失），互信息严格递减。\n\n$K^*$ 对应于 $I(X_0; X_k)$ 降至 noise floor 的临界深度——不是分类器的能力上限，而是 **information-theoretic impossibility boundary**：任何方法（无论多复杂）都无法区分 depth $> K^*$ 的文本，因为原始人类文本的信息已被信道噪声完全淹没。\n\n形式化地，若信道 $\\mathcal{T}$ 关于某分布度量 $d$ 是 contractive 的（即 $d(\\mathcal{T}(P), \\mathcal{T}(Q)) \\leq \\rho \\cdot d(P, Q)$，$0 < \\rho < 1$），则 $P_{X_k}$ 以几何速率趋近不动点分布 $P^*$：\n\n$$d(P_{X_k}, P^*) \\leq \\rho^k \\cdot d(P_{X_0}, P^*)$$\n\n相邻深度的分布差异同样以几何速率趋零：\n\n$$D(k, k{+}1) \\leq (\\rho^k + \\rho^{k+1}) \\cdot d(P_{X_0}, P^*)$$\n\n从而 $K^*(\\epsilon)$ 对任意阈值 $\\epsilon > 0$ 必然有限，其粗略 scaling 为：\n\n$$K^* = O\\left(\\frac{\\log(d(P_{X_0}, P^*) / \\epsilon)}{\\log(1/\\rho)}\\right)$$\n\n这表明 $K^*$ 由信道的 contraction rate $\\rho$ 和 seed 文本分布到不动点的初始距离共同决定。\n\n### 经验验证方法\n\n我们使用 pairwise AUC 作为 discriminability 的 empirical proxy，配合 Jensen-Shannon Divergence (JSD) 作为 distributional distance 的 computationally tractable proxy：\n\n$$\\text{JSD}(P_{X_k} \\| P_{X_{k'}}) = \\frac{1}{2} D_{\\text{KL}}(P_{X_k} \\| M) + \\frac{1}{2} D_{\\text{KL}}(P_{X_{k'}} \\| M)$$\n\n其中 $M = \\frac{1}{2}(P_{X_k} + P_{X_{k'}})$。JSD 在 unigram level 上按 feature 维度分别计算（基于 50-bin 直方图估计），取均值作为综合度量。\n\n需要承认的局限：unigram-level JSD 忽略了序列结构（n-gram patterns、句法依赖等），不等价于真正的互信息 $I(X_0; X_k)$。但 DPI 的定性结论——单调衰减——在 JSD 框架下同样成立，因此作为 tracking metric 仍然有效。\n\n### $K^*$ 的科学意义\n\n$K^*$ 是本工作提出的首次被系统测量的科学量。此前关于递归生成退化的研究 [Shumailov et al., 2024; Drayson et al., 2025] 主要提供定性描述（\"early generations show most change\"），但从未给出精确的判别边界。$K^*$ 的测量具有直接的实践指导价值：\n\n- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。\n- **对 model collapse 研究**：$K^*$ 量化了 Shumailov et al. 描述的 \"early collapse\" 与 \"late collapse\" 之间的精确过渡边界。\n- **对 AI 生成文本检测**：$K^*$ 揭示了 depth estimation 作为检测范式的 fundamental resolution limit——无论特征工程或分类器如何改进，信息论约束决定了 $K^*$ 之外不可能做得更好。\n\n[TODO: 补充 MVP 实验中测得的 $K^*$ 实际值及其置信区间]\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T16:28:15.752949+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_methodology_draft_20260512T162448",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T16:28:15.753139+00:00_

Methodology 初稿已写入 `docs/methodology_draft.md`。

涵盖四个 subsection：
- **3.1** 形式化定义、prompt-chain 实现（含精确 prompt 模板）、模型选择理由、解码参数、种子数据、left-padding
- **3.2** 三组 15 维特征的精确公式——surprisal 9D（含一阶/二阶差分）、vocab diversity 3D（TTR/hapax/self-BLEU）、tail-thinning 3D（kurtosis/entropy/LFR），全部从 `run_pipeline.py` 提取
- **3.3** LightGBM 选择理由、pairwise + ordinal 两级评估、5-fold CV 协议、四项指标
- **3.4** $K^*$ 操作性定义（AUC > 0.60）、阈值理由、DPI 理论联系（含 contraction rate scaling）、JSD proxy 及其局限、科学意义

标注了 3 处 `[TODO]` 待补充实验数据，1 处 `[需验证]` 标注不确定的引用。还标注了 doc\_id grouped CV 的设计缺陷需在正式实验中修复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_methodology_draft_20260512T162448"
}
```

</details>

---
