# Reviewer 1 coordination — Part 3 of 4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/4b/4bf7b0cbf90edc59b291.json)

## Round 30

### Tool result

_source line 987 · 2026-05-21T01:21:17.498060+00:00_

1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 10.76 but MMLU already degrades to 35.5\% (vs.\ 40.7\% at 30\%); 30\% appears to be the lowest-degradation sparsity level for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	On Mistral-7B (3-seed), KL improves PPL ($-$17.3\%) and commonsense tasks (WG, HS, PIQA: all seeds win) but MMLU is tied (43.3\% vs.\ 43.5\%) and GSM8K reverses across all seeds (7.0--11.1\% vs.\ TEAL 15.9\%). ARC-c is seed-dependent (37.8--50.1\% vs.\ TEAL 41.1\%; $\sigma$=6.4pp vs.\ LLaMA-8B's 2.5pp), indicating reduced cross-architecture metric stability. Forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways.
6	The 30\% sparsity analysis is validated at 7--8B scale; at 14B, KL's MMLU decline ($-$2.79pp uniform, $-$8.1pp global) and GSM8K reversal ($-$20pp uniform; 32.1$\pm$5.2\% vs.\ TEAL's 52.1\%, 3-seed) reflect task-and-scale-dependent effects (\S\ref{sec:cross_arch}; Appendix~\ref{app:14b}): at 8B all methods collapse to $<$9\% GSM8K, so this reversal emerges only with sufficient base capacity. KL's high cross-seed GSM8K variance ($\sigma$=5.2pp) suggests minor training perturbations disrupt reasoning-critical pathways that magnitude pruning preserves more robustly. Scaling to 70B remains untested.
7	Training data is domain-homogeneous: all predictors are trained on WikiText-103 (English Wikipedia), a single-domain corpus.
8	Activation importance patterns may differ on code, multilingual, or dialogue data; the predictor could underperform on domains with substantially different neuron utilization profiles.
9	Out-of-distribution evaluation on C4 (Appendix~\ref{app:oo
…[truncated 1919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-21T01:21:17.498463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 989 · 2026-05-21T01:21:17.549007+00:00_

1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	SwiGLU's gated activation makes prediction challenging: importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
5	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
6	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
7	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
8	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
9	
10	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
11	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
12	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Gradient 
…[truncated 2507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 990 · 2026-05-21T01:21:23.378986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 991 · 2026-05-21T01:21:23.681684+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 28698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 992 · 2026-05-21T01:21:29.617814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-21T01:21:30.071030+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
16	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU 
…[truncated 4413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-21T01:21:30.222211+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-21T01:22:05.715270+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 50, \"total_citations\": 93, \"unique_cited_keys\": 49, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 44, \"online_not_found\": 1, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"de2024griffin\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2025spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and
…[truncated 40416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 35493
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-21T01:25:51.786523+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n### 审稿侧重：方法严谨性 + 实验验证\n\n---\n\n### 1. Summary\n\n本文提出用前向 KL 散度（替代 BCE）训练 SwiGLU LLM 的稀疏性预测器，配合 Gumbel-Sigmoid 松弛和自适应惩罚控制器。核心发现是 KL 的端到端耦合梯度发现了与 magnitude-based masks 偏离 46–68% 的 mask patterns，且这些 patterns 通过 target-swap ablation (C1) 被确认为推理阶段质量的近端驱动因素。实验在 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B 上进行，展示了一致的 PPL 改进但不一致的下游任务表现。\n\n### 2. Strengths\n\n**S1. C1 Target-swap ablation 设计精巧且有说服力。** Table 3 (§4.4) 通过将 KL 发现的 oracle masks 喂给标准 BCE predictor，成功解耦了 mask quality 与 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp（s42），30% 下多 seed 一致性 ≤1.70pp，提供了 mask quality 是推理质量近端驱动因素的有力证据。\n\n**S2. 消融覆盖面广且系统性强。** Table 4 系统对比了 divergence 类型（forward KL vs JSD vs reverse KL）、松弛方法（Gumbel vs STE）、loss function isolation（BCE+Gumbel vs BCE plain），Appendix 补充了 bottleneck sensitivity (Table 7)、temperature schedule (Table 8)、training convergence (Table 9)。\n\n**S3. 诚实的结果报告。** 论文明确报告了 KL 在 knowledge-intensive tasks 上的劣势（MMLU 40.7% vs TEAL 45.9%，Table 2；Qwen-14B GSM8K −20pp），50% 下游的 capacity cliff，以及跨架构的不一致性。\n\n**S4. 二维 taxonomy 有组织价值。** Table 1 沿 correction granularity × training signal coupling 两个轴清晰组织先前工作。\n\n**S5. Multi-seed 评估覆盖了关键结果。** 主要结论均为 3-seed 评估并报告标准差。\n\n### 3. Weaknesses\n\n**W1. [Critical] 无实际推理加速，动机与贡献脱节。** 论文的动机是推理效率，但 Appendix A (Table 6) 显示 KL pipeline 增加 6.4% 延迟开销，实际 wallclock 无加速。论文承认 \"net acceleration requires kernel-level sparse computation optimizations...beyond the scope of this work\"。在 activation sparsity 领域，若不能展示端到端加速，贡献主要停留在 prediction quality 的学术分析层面。建议至少提供 Triton block-sparse 的 prototype 实测数据，或将 framing 完全转向 \"understanding training objectives for sparsity prediction\"。\n\n**W2. [Major] MMLU/GSM8K 上的系统性劣势削弱了 \"quality improvement\" claim 的覆盖面。** Abstract 强调 PPL 和 commonsense reasoning 改进，但 MMLU 从 45.9% 降至 40.7%（−5.2pp），在 Qwen-14B 上 GSM8K −20pp。所有三个模型上，knowledge-intensive tasks 均无改进或退步。论文将 forward KL 的 mode-covering 特性作为假设性解释（§4.2），但缺少实验验证。\n\n**W3. [Major] 主要对比中 actual sparsity 不匹配未被充分解决。** Table 2 中 KL 30% actual=28.5%，TEAL 30% actual=29.3%。0.8pp 差异意味着 KL 保留了更多神经元。虽然正文提供了 matched sparsity 比较（14.5% at 28.5%），但 Table 2 的 headline 比较仍在不同 actual sparsity 下进行。建议在 Table 2 中增加 TEAL at 28.5% 的行。\n\n**W4. [Major] MSE baseline 的单 seed 报告掩盖了高方差。** Appendix G 承认 MSE with seed 123 仅达到 5.1% sparsity（PPL=15,789），是 \"failure mode\"。但 Table 2/4 中 MSE 均为 seed 42 单 seed。一个 seed 完全失败的情况下，单 seed 报告不能代表 MSE 方法的真实性能分布。\n\n**W5. [Major] \"Gradient coupling\" vs \"objective function\" 的因果解释未被完全解耦。** KL 和 BCE 的关键区别不仅是梯度耦合程度，更根本的是 target 定义不同。MSE baseline 使用 L2 on hidden states，而非 per-layer KL on output distributions，因此 MSE 的失败可能源于 L2 loss 不适合而非 per-layer coupling 本身的局限。缺少关键实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence）。\n\n**W6. [Minor] 14B scale 结果有限且令人担忧。** Qwen-14B 仅在 30% sparsity 下评估，KL 的 GSM8K 大幅退步（32.1±5.2% vs 52.1%），方法在 14B+ scale 的适用性存疑。\n\n**W7. [Minor] 训练数据同质性。** 所有 predictor 在 WikiText-103 上训练。OOD 评估显示 C4 上 cross-seed variance 显著增大（CV=6.3% vs in-domain 0.2%）。\n\n### 4. Questions\n\n**Q1.** C1 的 s42 oracle 来自 \"an earlier training run\"，而 s123/s456 使用 \"matched retrained oracles\"。统一使用 matched oracles 后 s42 的 gap 是否会缩小？\n\n**Q2.** 是否可以在 reverse KL predictor 上也报告下游 metrics，验证 mode-seeking 是否更好保留 knowledge pathways？\n\n**Q3.** Table 2 没有 BCE 30% uniform 的条目。可否提供？Table 4 的 BCE 30% PPL=15.71 是 uniform 吗？\n\n**Q4.** MSE seed 123 失败是 MSE + Gumbel-Sigmoid + Lagrangian 组合不稳定，还是 MSE 固有缺陷？KL 是否有类似失败？\n\n**Q5.** KL 训练成本约 2.6× BCE，且每个 sparsity target 需单独训练，对实际部署意味着什么？\n\n### 5. Missing References\n\n- CATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work 中提及但未实验比较。应与 TEAL 一起在 Table 2 中展示。\n- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖。\n\n### 6. Overall Assessment\n\n**Overall: 3.5** (Borderline Conference) | **Soundness: 3.5/5** | **Excitement: 3/5** | **Confidence: 4/5**\n\n本文是一篇执行质量较高的实证研究，C1 target-swap ablation 有创意，KL > BCE 的核心发现在 PPL 层面有充分支撑。三个核心短板：(1) 无实际推理加速削弱实用价值；(2) knowledge-intensive tasks 上系统性退步限制 quality improvement 主张覆盖面；(3) gradient coupling 的因果解释缺少 per-layer KL 关键对照实验。方法论新颖性有限，贡献主要在 empirical characterization。建议补充 per-layer KL ablation、MSE multi-seed、和至少一个 kernel-level speedup measurement。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n### 审稿侧重：方法严谨性 + 实验验证\n\n---\n\n### 1. Summary\n\n本文提出用前向 KL 散度（替代 BCE）训练 SwiGLU LLM 的稀疏性预测器，配合 Gumbel-Sigmoid 松弛和自适应惩罚控制器。核心发现是 KL 的端到端耦合梯度发现了与 magnitude-based masks 偏离 46–68% 的 mask patterns，且这些 patterns 通过 target-swap ablation (C1) 被确认为推理阶段质量的近端驱动因素。实验在 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B 上进行，展示了一致的 PPL 改进但不一致的下游任务表现。\n\n### 2. Strengths\n\n**S1. C1 Target-swap ablation 设计精巧且有说服力。** Table 3 (§4.4) 通过将 KL 发现的 oracle masks 喂给标准 BCE predictor，成功解耦了 mask quality 与 gradient coupling 的贡献。50% sparsity 下 max Δ≤0.79pp（s42），30% 下多 seed 一致性 ≤1.70pp，提供了 mask quality 是推理质量近端驱动因素的有力证据。\n\n**S2. 消融覆盖面广且系统性强。** Table 4 系统对比了 divergence 类型（forward KL vs JSD vs reverse KL）、松弛方法（Gumbel vs STE）、loss function isolation（BCE+Gumbel vs BCE plain），Appendix 补充了 bottleneck sensitivity (Table 7)、temperature schedule (Table 8)、training convergence (Table 9)。\n\n**S3. 诚实的结果报告。** 论文明确报告了 KL 在 knowledge-intensive tasks 上的劣势（MMLU 40.7% vs TEAL 45.9%，Table 2；Qwen-14B GSM8K −20pp），50% 下游的 capacity cliff，以及跨架构的不一致性。\n\n**S4. 二维 taxonomy 有组织价值。** Table 1 沿 correction granularity × training signal coupling 两个轴清晰组织先前工作。\n\n**S5. Multi-seed 评估覆盖了关键结果。** 主要结论均为 3-seed 评估并报告标准差。\n\n### 3. Weaknesses\n\n**W1. [Critical] 无实际推理加速，动机与贡献脱节。** 论文的动机是推理效率，但 Appendix A (Table 6) 显示 KL pipeline 增加 6.4% 延迟开销，实际 wallclock 无加速。论文承认 \"net acceleration requires kernel-level sparse computation optimizations...beyond the scope of this work\"。在 activation sparsity 领域，若不能展示端到端加速，贡献主要停留在 prediction quality 的学术分析层面。建议至少提供 Triton block-sparse 的 prototype 实测数据，或将 framing 完全转向 \"understanding training objectives for sparsity prediction\"。\n\n**W2. [Major] MMLU/GSM8K 上的系统性劣势削弱了 \"quality improvement\" claim 的覆盖面。** Abstract 强调 PPL 和 commonsense reasoning 改进，但 MMLU 从 45.9% 降至 40.7%（−5.2pp），在 Qwen-14B 上 GSM8K −20pp。所有三个模型上，knowledge-intensive tasks 均无改进或退步。论文将 forward KL 的 mode-covering 特性作为假设性解释（§4.2），但缺少实验验证。\n\n**W3. [Major] 主要对比中 actual sparsity 不匹配未被充分解决。** Table 2 中 KL 30% actual=28.5%，TEAL 30% actual=29.3%。0.8pp 差异意味着 KL 保留了更多神经元。虽然正文提供了 matched sparsity 比较（14.5% at 28.5%），但 Table 2 的 headline 比较仍在不同 actual sparsity 下进行。建议在 Table 2 中增加 TEAL at 28.5% 的行。\n\n**W4. [Major] MSE baseline 的单 seed 报告掩盖了高方差。** Appendix G 承认 MSE with seed 123 仅达到 5.1% sparsity（PPL=15,789），是 \"failure mode\"。但 Table 2/4 中 MSE 均为 seed 42 单 seed。一个 seed 完全失败的情况下，单 seed 报告不能代表 MSE 方法的真实性能分布。\n\n**W5. [Major] \"Gradient coupling\" vs \"objective function\" 的因果解释未被完全解耦。** KL 和 BCE 的关键区别不仅是梯度耦合程度，更根本的是 target 定义不同。MSE baseline 使用 L2 on hidden states，而非 per-layer KL on output distributions，因此 MSE 的失败可能源于 L2 loss 不适合而非 per-layer coupling 本身的局限。缺少关键实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence）。\n\n**W6. [Minor] 14B scale 结果有限且令人担忧。** Qwen-14B 仅在 30% sparsity 下评估，KL 的 GSM8K 大幅退步（32.1±5.2% vs 52.1%），方法在 14B+ scale 的适用性存疑。\n\n**W7. [Minor] 训练数据同质性。** 所有 predictor 在 WikiText-103 上训练。OOD 评估显示 C4 上 cross-seed variance 显著增大（CV=6.3% vs in-domain 0.2%）。\n\n### 4. Questions\n\n**Q1.** C1 的 s42 oracle 来自 \"an earlier training run\"，而 s123/s456 使用 \"matched retrained oracles\"。统一使用 matched oracles 后 s42 的 gap 是否会缩小？\n\n**Q2.** 是否可以在 reverse KL predictor 上也报告下游 metrics，验证 mode-seeking 是否更好保留 knowledge pathways？\n\n**Q3.** Table 2 没有 BCE 30% uniform 的条目。可否提供？Table 4 的 BCE 30% PPL=15.71 是 uniform 吗？\n\n**Q4.** MSE seed 123 失败是 MSE + Gumbel-Sigmoid + Lagrangian 组合不稳定，还是 MSE 固有缺陷？KL 是否有类似失败？\n\n**Q5.** KL 训练成本约 2.6× BCE，且每个 sparsity target 需单独训练，对实际部署意味着什么？\n\n### 5. Missing References\n\n- CATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work 中提及但未实验比较。应与 TEAL 一起在 Table 2 中展示。\n- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖。\n\n### 6. Overall Assessment\n\n**Overall: 3.5** (Borderline Conference) | **Soundness: 3.5/5** | **Excitement: 3/5** | **Confidence: 4/5**\n\n本文是一篇执行质量较高的实证研究，C1 target-swap ablation 有创意，KL > BCE 的核心发现在 PPL 层面有充分支撑。三个核心短板：(1) 无实际推理加速削弱实用价值；(2) knowledge-intensive tasks 上系统性退步限制 quality improvement 主张覆盖面；(3) gradient coupling 的因果解释缺少 per-layer KL 关键对照实验。方法论新颖性有限，贡献主要在 empirical characterization。建议补充 per-layer KL ablation、MSE multi-seed、和至少一个 kernel-level speedup measurement。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 997 · 2026-05-21T01:25:55.907076+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4120
}
```

</details>

---


### Assistant

_source line 998 · 2026-05-21T01:26:03.806634+00:00_

审稿意见已发送给 Review Director。

**审稿完成摘要：**

- **Overall: 3.5** (Borderline Conference)
- **Soundness: 3.5/5** | **Excitement: 3/5** | **Confidence: 4/5**

主要发现：
- **优势**：C1 target-swap ablation 设计精巧，消融覆盖全面，结果报告诚实
- **关键问题**：无实际推理加速（+6.4% overhead）、knowledge-intensive tasks 系统性退步（MMLU −5.2pp）、gradient coupling 因果解释缺少 per-layer KL 对照实验、MSE baseline 单 seed 掩盖高方差
- **建议补充**：per-layer KL ablation、MSE multi-seed、kernel-level speedup prototype

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 31

## Round 31

8 recorded events


### User

_source line 999 · 2026-05-21T01:28:00.786800+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 2 的完整审稿原文：

### Summary
本文提出用 KL divergence（而非传统 BCE）训练轻量 MLP 预测器，为 SwiGLU LLM 的 FFN 层生成 input-dependent activation sparsity masks。核心发现是 KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，在 PPL 指标上持续优于 BCE 和 training-free baselines。通过 target-swap ablation (C1) 确认 mask quality 驱动推理质量。评估覆盖 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B，自定位为 "primarily empirical study"。

### Strengths
**S1.** C1 Target-Swap Ablation 设计精巧。
**S2.** 实验覆盖全面，附录详尽（17 个 Appendix sections）。
**S3.** 诚实的自我定位。
**S4.** Taxonomy 有组织价值。
**S5.** 多架构验证。

### Weaknesses
**W1 [Major] — 与 MaskLLM 的方法论区分不足，novelty 有限。** 核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM 高度重合。论文声称三点区别（activation vs weight sparsity, dynamic vs static masks, predictor vs learnable params），但这些均为 application-level differences，非 methodological innovation。作为 empirical study，可能达 Findings bar，但对 main conference 缺乏方法论或理论新颖贡献。

**W2 [Major] — Downstream task 结果不一致，削弱核心 claim 的实用价值。** MMLU: KL 40.73 vs TEAL 45（−4.27pp at 30%）。论文在 §4.6 承认 task/scale-dependent effects 但未充分解释。如果 KL-discovered masks 更优，为何只在 PPL 和部分 reasoning tasks 上体现？

**W3 [Major] — "Gradient coupling" narrative 缺乏严格支撑。** §3.6 分析停留在直觉描述。"KL introduces a downstream Jacobian" 对任何 output-level loss 都成立，非 KL 独特性质。Gradient SNR 可能是不同 loss landscape 的 artifact。将此称为 "gradient coupling discovers mask patterns" 是 overclaiming。

**W4 [Minor] — Wall-clock speedup 缺失降低实用性论证。** 仅有 FLOPs 估算，无实际 wall-clock measurements。Unstructured masks 在现有硬件上通常无法转化为实际加速。

**W5 [Minor] — Abstract 信息密度过高。** ~200 词塞入过多数字，模糊核心 message。"coupled gradient discovers" 等措辞有 overclaiming 之嫌。

**W6 [Minor] — 训练数据单一性。** 仅 WikiText-103 训练。OOD C4 上 variance 增大。

### Questions
**Q1.** MaskLLM 的训练策略（directly learnable mask parameters + KL + Gumbel-Softmax）直接应用于 per-token activation sparsity prediction，结果是否与本文可比？
**Q2.** KL-derived masks 在不同 random seeds 之间的 Jaccard divergence 是多少？如果 seed-to-seed 变异也达到 40-60%，46-68% 的数字信息量将大打折扣。
**Q3.** MSE 也是 output-level objective（作用在 hidden states），为什么表现不如 TEAL？这与 "output-level coupling is the key" 叙事矛盾。
**Q4.** Table 4 中 Forward KL+Coupled 与 BCE+STE 差距仅 0.41 PPL，downstream 上是否有统计显著性？
**Q5.** 14B 模型多 GPU 部署时，predictor overhead 是否成为瓶颈？

### Missing References
- Mixture-of-Channels (MoC)：SwiGLU native gating + Top-K channel selection
- "A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering"

### 格式合规
全部通过（页数✅、模板✅、匿名✅、Limitations✅、Ethics✅、Checklist✅、引用✅）

### Overall Assessment
**Overall: 3.0 (Findings)** | **Soundness: 3.5/5** | **Excitement: 2.5/5** | **Confidence: 4/5**

升档路径（→3.5）: 形式化 gradient coupling 分析 + 解释 downstream inconsistency + proof-of-concept speedup。
降档风险（→2.5）: MaskLLM 策略直接迁移可复现结果 或 seed-level mask divergence 高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-21T01:28:41.885012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": "125",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "offset": "125",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1001 · 2026-05-21T01:28:42.337290+00:00_

125	\subsection{Ablation Studies}
126	
127	Table~\ref{tab:ablation} isolates the contribution of each design choice at 30\% and 50\% sparsity.
128	
129	\begin{table}[t]
130	\centering
131	\caption{Ablation on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol; uniform allocation at 30\%, global allocation at 50\%). $^\ddagger$STE achieved only 20.8\% model-level sparsity at 30\% target due to tied sigmoid scores in the threshold-based mask; excluded from 30\% comparison (see \S\ref{sec:ablation_ste}).}
132	\label{tab:ablation}
133	\resizebox{\columnwidth}{!}{
134	\begin{tabular}{lccc}
135	\toprule
136	Configuration & 30\% PPL$\downarrow$ & 50\% PPL$\downarrow$ & $\Delta_{50}$ \\
137	\midrule
138	\multicolumn{4}{l}{\textit{KL-based variants}} \\
139	Forward KL + Gumbel (Ours) & \textbf{8.82} & \textbf{11.79} & --- \\ % exp_id: kl30_ablation_s42, bench_kl50_global
140	JSD (symmetric) + Gumbel & 8.88 & 12.54 & +0.75 \\ % exp_id: jsd30_ablation_s42, jsd_ablation_s42
141	Reverse KL + Gumbel & 9.31 & 12.80 & +1.01 \\ % exp_id: rkl30_ablation_s42, reverse_kl_ablation_s42
142	Forward KL + STE & ---$^\ddagger$ & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
143	\midrule
144	\multicolumn{4}{l}{\textit{Per-layer coupling (intermediate)}} \\
145	Per-layer MSE & 20.43 & 229.26 & +217.47 \\ % exp_id: mse30_uniform_s42, mse50_uniform_s42
146	\midrule
147	\multicolumn{4}{l}{\textit{BCE-based variants}} \\
148	BCE (no compensation) & 15.71 & 27.97 & +16.18 \\ % exp_id: bce30_uniform_s42, eval_bce_v3_s42
149	BCE + Gumbel (no penalty) & --- & 32.22 & +20.43 \\ % exp_id: bce_gumbel_no_penalty_s42
150	BCE + Gumbel + Penalty & --- & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
151	BCE + STE & --- & 60.54 & +48.75 \\ % exp_id: bce_ste_s42
152	\bottomrule
153	\end{tabular}}
154	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-21T01:28:42.639007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
  "offset": "100",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
    "offset": "100",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-21T01:28:42.689722+00:00_

100	
101	\subsection{Gradient Analysis: BCE vs.\ KL}
102	\label{sec:method:gradient}
103	
104	To build intuition for how KL distillation discovers neuron importance patterns that diverge from magnitude-based masks (\S\ref{sec:mask_analysis}), we contrast the gradient structure of the two objectives. This analysis is suggestive; \S\ref{sec:mask_analysis} provides evidence that the coupled gradient discovers mask targets that yield lower perplexity, with mask quality driving inference-stage quality.
105	
106	Under BCE, the predictor trains against oracle masks $m_j^* = \mathbf{1}[|g_j| \geq \text{top-}k\text{ threshold}]$ derived from activation magnitudes.
107	The gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$; each neuron is trained independently with no inter-neuron coupling.
108	Under KL distillation, the chain rule introduces a downstream Jacobian $\partial \mathbf{z}_{\text{sparse}} / \partial \tilde{m}_j^{(\ell)}$ that couples neuron $j$'s gradient to all other retained neurons in layers $\ell$ through $L$, because the sparse hidden state propagates through subsequent attention and FFN operations.
109	This coupling allows KL to evaluate each neuron's importance in the context of the full sparse computation, rather than against a fixed magnitude target.
110	
111	Gradient SNR measurements\footnote{$\text{SNR}_\ell = \|\mathbb{E}[\nabla_{\theta_\ell} \mathcal{L}]\|_2^2 / \text{Var}[\nabla_{\theta_\ell} \mathcal{L}]$, expectation over mini-batches.} reveal that BCE maintains consistently higher SNR than KL throughout training ($2.3\times$ at convergence; Figure~\ref{fig:snr_trajectory}), indicating that KL's quality advantage does not arise from cleaner gradient signals.
112	Rather, KL's end-to-end coupled gradient serves as a \emph{search mechanism} that discovers compositionally superior mask patterns, even when the per-step signal is noisier than BCE's decomposed updates.
113	The target-swap ablation 
…[truncated 1683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1004 · 2026-05-21T01:30:24.222867+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 与 MaskLLM 方法论区分不足。** 核心训练配方确实与 MaskLLM 高度重合。论文自承 \"primarily an empirical study\"（Introduction §1）。但 per-token dynamic masks + global top-k allocation 产生的长距离依赖使 C1 ablation 和 allocation analysis 成为可能，application-level differences 不完全 trivial。方法论新颖性有限，empirical contributions 达 Findings bar 无争议，能否达 Conference 取决于评判标准。\n\n**[AGREE] R2-W2: Downstream inconsistency。** 完全同意，与我 R1-W2 一致。三个模型上 knowledge-intensive tasks 均系统性退步（Table 2 MMLU −5.2pp; Table 14 GSM8K −20pp），非边际效应。\n\n**[REBUT] R2-W3: Gradient coupling narrative。** 部分同意 narrative 不够严格，但 R2 说 \"任何 output-level loss 都成立\" 不构成否定——论文的贡献在于实证量化效果。§3.6 已标注 \"suggestive\"，因果证据在 C1 ablation。缺少 per-layer KL ablation 是真实 gap（与我 R1-W5 一致），但不应将整个叙事归为 overclaiming。\n\n**[REBUT] R2-W4: R2 称 \"仅有 FLOPs 估算，无 wall-clock\"——事实性错误。** Appendix A Table 6 有实际 wall-clock 测量（RTX PRO 6000, batch=1, seq=2048, fp16, 100 fwd passes）：Dense 119.11±0.57 ms, KL 126.78±0.31 ms。问题是 +6.4% overhead 而非加速，但数据确实存在。\n\n**[AGREE] R2-W5, W6。** 同意。\n\n### Questions 回应\n\n**[REBUT] R2-Q1:** MaskLLM 的 directly learnable mask parameters 无法泛化到未见过的 input（activation sparsity 的核心要求）。最接近的对照是 Table 4 \"BCE + Gumbel\"（PPL 32.22 at 50%），远不如 KL (11.79)。\n\n**[AGREE] R2-Q2: Seed-to-seed mask Jaccard 是关键缺口。** 如果 seed 间 mask divergence 也达 40-60%，46-68% 数字的信息量大打折扣。论文仅报告 PPL stability（CV=0.6%），未报告 mask-level 一致性。Appendix P 也承认这是 open question。我 R1 审稿遗漏了此点。\n\n**[REBUT] R2-Q3: MSE 不是 output-level objective。** MSE 作用于 per-layer hidden states，非 model output logits（§3.7 明确说明，Appendix G 确认 loss target 为 per-layer FFN reconstruction）。MSE 是 intermediate-level objective（Table 1 中间列），其失败支持而非矛盾 \"output-level coupling is key\"。\n\n**[REBUT] R2-Q4: 0.41 PPL 差距无法复现。** Table 4 实际数据：Forward KL 11.79 vs BCE+STE 60.54 (50%)，差距 48.75。30% 无 BCE+STE 数据。Forward KL vs Reverse KL at 30% = 0.49，Forward KL vs JSD at 30% = 0.06——无 0.41 对应。R2 可能存在数据引用错误。\n\n**[AGREE] R2-Q5:** 14B 多 GPU predictor overhead 未讨论，Appendix A 仅覆盖单 GPU。\n\n### 综合\n\nR2 审稿质量较高，W1/W2/Q2 关切有力。但 W4 事实性错误、Q3 前提错误、Q4 数据无法复现。Overall 3.0 可能略低——考虑 C1 ablation 质量和消融覆盖面，维持 3.5 (Borderline Conference)。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 的交叉回应\n\n### Weaknesses 回应\n\n**[AGREE] R2-W1: 与 MaskLLM 方法论区分不足。** 核心训练配方确实与 MaskLLM 高度重合。论文自承 \"primarily an empirical study\"（Introduction §1）。但 per-token dynamic masks + global top-k allocation 产生的长距离依赖使 C1 ablation 和 allocation analysis 成为可能，application-level differences 不完全 trivial。方法论新颖性有限，empirical contributions 达 Findings bar 无争议，能否达 Conference 取决于评判标准。\n\n**[AGREE] R2-W2: Downstream inconsistency。** 完全同意，与我 R1-W2 一致。三个模型上 knowledge-intensive tasks 均系统性退步（Table 2 MMLU −5.2pp; Table 14 GSM8K −20pp），非边际效应。\n\n**[REBUT] R2-W3: Gradient coupling narrative。** 部分同意 narrative 不够严格，但 R2 说 \"任何 output-level loss 都成立\" 不构成否定——论文的贡献在于实证量化效果。§3.6 已标注 \"suggestive\"，因果证据在 C1 ablation。缺少 per-layer KL ablation 是真实 gap（与我 R1-W5 一致），但不应将整个叙事归为 overclaiming。\n\n**[REBUT] R2-W4: R2 称 \"仅有 FLOPs 估算，无 wall-clock\"——事实性错误。** Appendix A Table 6 有实际 wall-clock 测量（RTX PRO 6000, batch=1, seq=2048, fp16, 100 fwd passes）：Dense 119.11±0.57 ms, KL 126.78±0.31 ms。问题是 +6.4% overhead 而非加速，但数据确实存在。\n\n**[AGREE] R2-W5, W6。** 同意。\n\n### Questions 回应\n\n**[REBUT] R2-Q1:** MaskLLM 的 directly learnable mask parameters 无法泛化到未见过的 input（activation sparsity 的核心要求）。最接近的对照是 Table 4 \"BCE + Gumbel\"（PPL 32.22 at 50%），远不如 KL (11.79)。\n\n**[AGREE] R2-Q2: Seed-to-seed mask Jaccard 是关键缺口。** 如果 seed 间 mask divergence 也达 40-60%，46-68% 数字的信息量大打折扣。论文仅报告 PPL stability（CV=0.6%），未报告 mask-level 一致性。Appendix P 也承认这是 open question。我 R1 审稿遗漏了此点。\n\n**[REBUT] R2-Q3: MSE 不是 output-level objective。** MSE 作用于 per-layer hidden states，非 model output logits（§3.7 明确说明，Appendix G 确认 loss target 为 per-layer FFN reconstruction）。MSE 是 intermediate-level objective（Table 1 中间列），其失败支持而非矛盾 \"output-level coupling is key\"。\n\n**[REBUT] R2-Q4: 0.41 PPL 差距无法复现。** Table 4 实际数据：Forward KL 11.79 vs BCE+STE 60.54 (50%)，差距 48.75。30% 无 BCE+STE 数据。Forward KL vs Reverse KL at 30% = 0.49，Forward KL vs JSD at 30% = 0.06——无 0.41 对应。R2 可能存在数据引用错误。\n\n**[AGREE] R2-Q5:** 14B 多 GPU predictor overhead 未讨论，Appendix A 仅覆盖单 GPU。\n\n### 综合\n\nR2 审稿质量较高，W1/W2/Q2 关切有力。但 W4 事实性错误、Q3 前提错误、Q4 数据无法复现。Overall 3.0 可能略低——考虑 C1 ablation 质量和消融覆盖面，维持 3.5 (Borderline Conference)。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-21T01:30:28.797610+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4574
}
```

</details>

---


### Assistant

_source line 1006 · 2026-05-21T01:30:36.447374+00:00_

交叉回应已提交给 Review Director。总结：

- 对 R2 的 6 个 Weakness 中，4 个 AGREE（W1 novelty, W2 downstream, W5 abstract, W6 data）、2 个 REBUT（W3 部分同意但 C1 ablation 的结论仍成立; W4 事实性错误——论文有 wall-clock 数据）
- 对 R2 的 5 个 Question 中，2 个 AGREE（Q2 seed mask divergence 是关键缺口、Q5 多 GPU overhead）、3 个 REBUT（Q1 MaskLLM 不可直接迁移、Q3 MSE 非 output-level、Q4 数据引用 0.41 无法复现）
- 维持 Overall 3.5 评分，认为 R2 的 3.0 略低

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 32

## Round 32

54 recorded events


### User

_source line 1007 · 2026-05-22T08:23:51.122621+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验评估**。

## 论文信息
- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
- 目标 venue: EMNLP 2026 (Long Paper, ARR May cycle)
- Deadline: 2026-05-25
- 格式: ACL review 模板, double-blind, 正文 ≤ 8页, 参考文献不限, Limitations/Ethics 不计入页数
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf

## 你的审查侧重

1. **方法论严谨性**:
   - KL distillation 框架的数学正确性（§3.4 KL loss, §3.3 Gumbel-Sigmoid, §3.5 Lagrangian）
   - Gradient analysis (§3.6): BCE vs KL 梯度结构对比是否准确，"suggestive" 标注是否足够 hedge overclaiming
   - Per-layer KL decomposition (§4.5): signal type vs coupling scope 的 2D 分解是否合理，97.5% 归因是否有 confound
   - Target-swap ablation (C1, §4.4): 是否充分隔离 mask quality vs gradient coupling

2. **实验评估**:
   - 多种子覆盖: 哪些结果有 3-seed 统计，哪些仅 single seed，是否有 cherry-picking 风险
   - Baseline 公平性: BCE 2700 steps vs KL 1000 steps 的 isocompute 比较是否合理
   - Actual sparsity 不匹配: KL 28.5% vs TEAL 29.3% at 30% target，对 headline comparison 的影响
   - MSE baseline: 3-seed 含 failed seed (PPL=15789) 的报告方式是否恰当
   - 14B scale 结果: 仅 30% sparsity, GSM8K 大幅退步 (32.1±5.2% vs dense 52.1%)，实验覆盖是否充分
   - Knowledge-intensive tasks 系统性退步: MMLU -5.2pp (8B), GSM8K -20pp (14B)

3. **技术细节**:
   - Compensation redundancy claim 是否有充分证据
   - OOD evaluation: C4 结果和 variance 增大 (CV 0.2%→6.3%)
   - 延迟分析: +6.4% overhead 但无 wall-clock speedup

请按 ARR reviewer guidelines 输出完整审稿意见，包含: Summary, Strengths (逐条), Weaknesses (逐条, 标注 Critical/Major/Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP guidelines)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-22T08:24:04.398810+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-22T08:24:04.449435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-22T08:24:07.321168+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1011 · 2026-05-22T08:24:09.581230+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
  "pages": "1-8",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
    "pages": "1-8",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1012 · 2026-05-22T08:24:14.594246+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I've found information about ACL ARR 2026 reviewer guidelines and review form criteria. Here are the key details:

## Review Form Criteria

For Main papers, review criteria include novelty, impact, and other factors, while for Findings papers, the main 
…[truncated 1134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7273
}
```

</details>

---


### Tool result

_source line 1013 · 2026-05-22T08:24:16.218298+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 561.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.1}], \"total_pages\": 19, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6637
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-22T08:24:41.794372+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-22T08:24:41.845089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1016 · 2026-05-22T08:24:42.850210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1017 · 2026-05-22T08:24:43.302214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1018 · 2026-05-22T08:24:43.705941+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1019 · 2026-05-22T08:24:43.756662+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1020 · 2026-05-22T08:24:44.712140+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 1021 · 2026-05-22T08:24:44.763637+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1022 · 2026-05-22T08:24:44.764113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1023 · 2026-05-22T08:24:45.216857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1024 · 2026-05-22T08:24:45.669496+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1025 · 2026-05-22T08:24:45.770311+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1026 · 2026-05-22T08:24:46.573901+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-22T08:24:46.575083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-22T08:24:46.625678+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1029 · 2026-05-22T08:24:46.928199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1030 · 2026-05-22T08:24:47.535362+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-22T08:24:47.787226+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-22T08:25:00.294053+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
  "pages": "9-19",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
    "pages": "9-19",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-22T08:25:02.605067+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.8}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 594.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.5}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p17.png\", \"wid
…[truncated 730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2311
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-22T08:25:02.705856+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions/criteria that reviewers must score, the scale for each dimension, and any instructions for how to score. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all dimensions/criteria that reviewers must score, the scale for each dimension, and any instructions for how to score. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 1035 · 2026-05-22T08:25:07.826295+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Scored Dimensions

**1. Soundness**
- Scale: 1-5 (with .5 increments)
- 5 = Excellent: "one of the most thorough I have seen"
- 4 = Strong: sufficient support for claims
- 3 = Acceptable: main claims supported with minor gaps
- 2 = Poor: major claims lack support
- 1 = Major Issues: insufficient for publication

**2. Excitement**
- Scale: 1-5 (with .5 increments)
- 5 = Highly Exciting: would recommend to others
- 4 = Exciting: would mention to others
- 3 = Interesting: might mention some points
- 2 = Potentially Interesting: doesn't resonate personally
- 1 = Not Exciting: lacks relevance to NLP community

**3. Overall Assessment**
- Scale: 1-5 (with .5 increments)
- 5 = Consider for Award: top 2.5% papers
- 4 = Conference acceptance
- 3 = Findings acceptance
- 2 = Resubmit next cycle
- 1 = Do not resubmit

**4. Reviewer Confidence**
- Scale: 1-5
- 5 = Very careful review; familiar with related work
- 3 = Adequate familiarity; some details unchecked
- 1 = Not expert area or unclear paper

**5. Reproducibility**
- Scale: 1-5
- 5 = Easily reproducible
- 3 = Reproducible with difficulty
- 1 = Cannot reproduce

**6. Datasets & Software Value**
- Scale: 1-5 each
- 5 = Enabling for future research
- 1 = None available

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5120
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-22T08:25:12.671543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1037 · 2026-05-22T08:25:13.628008+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-22T08:25:13.628503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1039 · 2026-05-22T08:25:14.186204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1040 · 2026-05-22T08:25:14.588770+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 1041 · 2026-05-22T08:25:14.690297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1042 · 2026-05-22T08:25:15.143863+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1043 · 2026-05-22T08:25:15.144329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1044 · 2026-05-22T08:25:16.160711+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1470
}
```

</details>

---


### Tool call

_source line 1045 · 2026-05-22T08:25:16.161183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1046 · 2026-05-22T08:25:16.617816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1473
}
```

</details>

---


### Tool call

_source line 1047 · 2026-05-22T08:25:16.618279+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-22T08:25:16.963649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-22T08:25:17.931964+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1770
}
```

</details>

---


### Tool call

_source line 1050 · 2026-05-22T08:25:17.932461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1051 · 2026-05-22T08:25:18.436599+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1818
}
```

</details>

---


### Tool result

_source line 1052 · 2026-05-22T08:25:18.438764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1475
}
```

</details>

---


### Tool call

_source line 1053 · 2026-05-22T08:25:18.439152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1054 · 2026-05-22T08:25:19.195080+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool result

_source line 1055 · 2026-05-22T08:25:19.197138+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 1056 · 2026-05-22T08:25:19.199114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1057 · 2026-05-22T08:25:19.250949+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1058 · 2026-05-22T08:30:27.252562+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n\n---\n\n## Summary\n\n本文提出用 forward KL divergence 替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的上下文稀疏性预测器。核心 insight 是：BCE 将每个神经元的激活视为独立二分类问题，梯度不跨层耦合；而 KL 在输出分布层面优化，通过完整前向传播产生耦合梯度，使预测器发现与 magnitude-based oracle 有 46–68% 差异的 mask patterns。在 LLaMA-3.1-8B 和 Qwen-2.5-14B 上，KL 在 30% 稀疏度下 PPL 优于 TEAL 14.5%（matched sparsity），并在多数下游任务上保持竞争力。论文通过 target-swap ablation (C1)、per-layer KL decomposition 等消融实验分析了 KL 优势的来源。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 KL 框架数学正确；但 97.5% signal-type 归因基于 PPL 而非下游指标，C1 ablation 存在循环论证，削弱了分析叙事的可信度 |\n| Excitement | 2.5/5 | 研究问题有意义（BCE 独立性限制），但无实际加速、knowledge-intensive 任务退步显著，实用影响有限 |\n| Reproducibility | 4/5 | 超参数详细、主实验有 3-seed 统计、训练细节完整；代码未提供但可根据描述复现 |\n| Overall Assessment | **3.0** (Findings) | 实证贡献扎实但分析叙事有关键缺口，且缺乏实际加速验证 |\n| Reviewer Confidence | 4/5 | 熟悉 contextual sparsity、知识蒸馏和 SwiGLU 架构相关工作 |\n\n---\n\n## 主要优势\n\n**S1. 研究问题清晰且有意义。** BCE 将每个神经元独立处理的局限性是 contextual sparsity 文献中一个被忽视的问题。用 output-distribution distillation 替代 per-neuron classification 是一个自然且有价值的研究方向。\n\n**S2. 消融设计系统且深入。** C1 target-swap ablation（§4.4）、per-layer KL decomposition（§4.5/§3.7）、4 种 loss 变体对比（Table 4）、relaxation 方法对比（Gumbel vs STE）形成了较完整的消融体系。\n\n**S3. 梯度分析的 hedging 恰当。** §3.6 将 BCE vs KL 梯度结构对比标注为\"suggestive\"，未过度声称理论因果关系，而是用实验（§4.4）提供支撑证据。这种诚实的表述值得肯定。\n\n**S4. 训练效率优势明确。** KL 在 1000 steps 达到的效果优于 BCE 2700 steps（§4.3, PPL 11.79 vs 28.13），且 wall-clock 时间相当（~45 min），这是一个有实用价值的发现。\n\n**S5. 附录内容充实。** 19 个附录覆盖了 inference latency（App A）、bottleneck sensitivity（App B）、temperature schedule（App B.1）、training convergence（App B.2）、penalty controller dynamics（App C）、OOD evaluation（App D）等，增强了可复现性。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **97.5% signal-type 归因与下游指标矛盾，叙事有误导风险**\n- 具体位置：§3.7（page 5）及 §4.5（page 8）\n- 问题：论文声称\"signal type accounts for 97.5% of the PPL gap\"（§3.7），但紧接着承认\"cross-layer coupling contributes downstream benefit (1–4pp on ARC-Challenge and WinoGrande)\"以及\"per-layer KL underperforms end-to-end KL by 5–8pp on commonsense tasks\"（§4.5）。这意味着 coupling scope 对下游任务的贡献远超 2.5%，但论文的主叙事（包括 abstract 和 conclusion）反复强调 97.5% 这个数字，可能给读者造成\"coupling 不重要\"的错误印象。\n- 为什么影响接收：论文的核心分析框架（signal type vs coupling scope 的 2D 分解）假设这两个因素可加性分解且 PPL 是充分代理指标。但下游指标显示非加性交互存在。这不是小的表述问题，而是分析叙事的核心主张与自身实验证据之间的不一致。\n- 建议修改方向：(1) 在 abstract/conclusion 中明确 97.5% 仅适用于 PPL，下游指标显示 coupling 贡献更大；(2) 补充下游指标的 2D 分解定量结果（不仅是 1–4pp 的定性描述）；(3) 讨论 PPL 作为代理指标的局限性。\n\n**N2** [critical] **C1 target-swap ablation 的循环论证未充分讨论**\n- 具体位置：§4.4（page 7）, Table 3\n- 问题：C1 将 KL 发现的 masks 交给 BCE 训练，结果 BCE 也能获得接近 KL 的 PPL。论文将此解释为\"mask quality is the proximate driver, not gradient coupling\"。但这些 masks 恰恰是由 KL 的耦合梯度发现的——如果没有 KL 训练，这些 mask targets 根本不存在。因此 C1 证明的是\"KL-derived masks transferable to BCE\"，而非\"coupling 不重要\"。\n- 为什么影响接收：这个 ablation 是论文因果分析链的关键环节。如果 C1 的解释存在循环（KL 的贡献被归结为 mask quality，但 mask quality 来自 KL 的 coupling），那么论文关于\"what matters\"的核心结论需要重新审视。\n- 建议修改方向：(1) 明确讨论这个循环性：C1 证明了 mask 的 transferability，但 KL 的 coupling 是发现这些 masks 的必要条件；(2) 补充反向实验——能否用其他方法（如 evolutionary search、random perturbation）找到同等质量的 masks？如果只有 KL 能发现，则 coupling 的贡献不可被 C1 消解。\n\n**N3** [critical] **无实际 wall-clock 加速，实用价值存疑**\n- 具体位置：§4.6（page 8）, Appendix A（page 13）, Limitations（page 9）\n- 问题：Table 5 显示 KL-sparse pipeline 增加 +6.4% latency overhead，但没有任何 wall-clock speedup 结果。论文承认\"wall-clock speedup requires sparse kernel support not yet implemented here\"（Limitations, page 9）。对于一篇 contextual sparsity 方法论文，缺乏实际加速验证是重大缺陷。\n- 为什么影响接收：Sparsity 的唯一目的是推理加速。即使论文自我定位为\"analytical understanding\"（Limitations），但 abstract 和 introduction 均以\"inference-free activation sparsity\"和\"lightweight predictor\"作为 motivation，暗示实用价值。如果无法展示加速，读者无法判断改进的 mask quality 是否有实际意义。\n- 建议修改方向：(1) 至少提供 Triton/cuSPARSE 的概念验证 speedup 数字，即使不完整；(2) 如果无法提供，在 abstract 和 introduction 中显著弱化 practical motivation，明确声明这是一项分析性研究。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] **14B 实验覆盖不足，GSM8K 退步严重且缺乏对比**\n- 具体位置：Table 13（page 16），§4.6（page 8）\n- 问题：14B（Qwen-2.5-14B）仅在 30% sparsity 下有完整下游评估。GSM8K 从 dense 52.1% 降至 32.1±5.2%（−20pp），高 seed variance（±5.2）暗示不稳定性。但论文未给出 TEAL 在 14B 上的 GSM8K 对比，无法判断这是 KL 方法的问题还是 contextual sparsity 的通病。Table 16（page 18）有 cross-architecture 结果但同样仅 30%。\n- 建议：(1) 补充 TEAL 在 14B 上的完整下游指标对比；(2) 补充 14B 50% sparsity 的下游结果（HellaSwag/PIQA 已有，缺其他指标）；(3) 讨论 GSM8K 高 variance 的原因。\n\n**W2** [major] **Knowledge-intensive 任务系统性退步缺乏机制解释**\n- 具体位置：Table 2（page 6），Limitations（page 9）\n- 问题：8B 30% sparsity 下 MMLU −5.2pp（Table 2, KL global vs dense），14B 30% GSM8K −20pp。论文在 Limitations 中承认\"KL's mass-covering property may preserve output quality at the expense of reasoning-critical pathways\"，但这是推测性的一句话，缺乏任何分析证据。\n- 建议：(1) 分析 knowledge-intensive tasks 上 per-layer mask 差异是否与 attention/FFN 的 knowledge storage 层相关；(2) 讨论 forward KL 的 mode-covering 特性是否系统性地牺牲了低频但重要的 knowledge patterns。\n\n**W3** [major] **MSE baseline 的 failed seed 报告方式不透明**\n- 具体位置：Table 4（page 7）\n- 问题：Per-layer MSE 在 50% sparsity 下达到 PPL 229.26（Table 4），远超正常范围。Appendix G 提到\"3-seed, with seed 123, ... random-level, indicating high sensitivity to initialization—a failure mode not observed with KL-based losses\"。如果 3 个 seeds 中有一个 catastrophic failure（如 PPL=15789 在某处提到），在 mean±std 中报告会严重扭曲统计。论文应明确每个 seed 的值并讨论 failure mode。\n- 建议：(1) Table 4 中标注哪些 entries 包含 failed seeds；(2) 分别报告 median 和 mean，或排除 failed seeds 后单独报告。\n\n**W4** [minor] **OOD variance 增大 (CV 0.2%→6.3%) 需更多讨论**\n- 具体位置：Appendix D（page 14）, Limitations（page 9）\n- 问题：C4 上 cross-seed PPL variance 的 coefficient of variation 从 in-domain 的 0.2% 增至 6.3%。虽然绝对 PPL（16.03）仍合理，但 30× 的 variance 增幅暗示 KL predictor 可能对 domain shift 敏感。论文仅简单提到\"the predictor partially overfits to training-domain activation patterns\"但未深入分析。\n- 建议：分析哪些层的 mask patterns 在 OOD 时变化最大，以及这是否与 per-layer allocation budget 的 non-monotonic behavior 相关。\n\n**W5** [minor] **Actual sparsity mismatch 的讨论虽在附录但不够显著**\n- 具体位置：Table 2 footnote（page 6），Appendix D（page 14）\n- 问题：KL 在 30% target 下实际只达到 28.5%（vs TEAL 29.3%）。虽然 Appendix D 有 matched-sparsity 对比，但主表（Table 2）的 headline comparison 使用了不同实际稀疏度下的数字。论文 abstract 的\"14.5% over TEAL\"使用了 matched-sparsity 数字，这一点没有在 abstract 中说明。\n- 建议：在 Table 2 中直接标注各方法的实际稀疏度，而非仅用脚注。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.4 Eq.(5): 符号 $p_{\\text{dense}}$ 和 $p_{\\text{sparse}}$ 在引入前建议先定义清楚，当前定义在 Eq.(5) 下方的段落中出现，但 Eq.(5) 本身先用了这些符号。\n- Figure 2（page 8）: y 轴标签\"PPL↓\"但图中值越高越差，建议标注为\"PPL\"（不加箭头）或使用 log scale 让差异更明显。\n- Table 1（page 5）: 该 taxonomy table 信息密度高，但\"Per-token × Coupled cell\"仅由本文占据，可能暗示 positioning 过于强调 novelty 而非实质差异。\n- Limitations 中提到\"scaling to 70B remains untested\"——建议明确这是由于计算资源限制还是方法论障碍。\n\n---\n\n## Questions for Authors\n\n**Q1.** 你们在 §4.5 的 2D 分解中能否提供下游指标（ARC, MMLU, WinoGrande）的定量分解结果？这对于评估 97.5% 归因的适用范围至关重要。\n\n**Q2.** C1 ablation 中，BCE 使用 KL-derived masks 作为 target 训练时，是否也使用了 Gumbel-Sigmoid relaxation？如果 C1 只用了 hard threshold，那么 C1 和 KL 之间的差异可能部分来自 relaxation method 而非 mask quality。\n\n**Q3.** 对于 14B 上 GSM8K 的 −20pp 退步和 ±5.2 的高 seed variance，你们是否分析过是哪些层的 masks 在不同 seeds 间差异最大？这可能揭示 reasoning 能力退化的机制。\n\n**Q4.** 是否有证据表明其他方法（如 evolutionary search 或 gradient-free optimization）能发现与 KL 类似质量的 masks？如果有，则 C1 的\"mask quality > coupling\"结论更强；如果没有，则说明 coupling 是 mask discovery 的必要条件。\n\n**Q5.** Compensation network 被声称为 redundant（+67.2M params），但在 capacity-limited regime（§4.6 提到的 ≤45% sparsity），compensation 是否可能变得必要？\n\n---\n\n## Missing References\n\n- **PowerInfer** (Song et al., 2024b) 已引用，但 **PowerInfer-2**（Xue et al., 2024）的 on-device sparsity work 可能相关。\n- **Wanda** (Sun et al., 2024) 的 structured pruning 方法与本文的 unstructured contextual sparsity 有方法论对比价值。\n- **ReLU-fication** literature（如 Mirzadeh et al., 2024 已引用）中关于 SwiGLU 到 ReLU 转换后天然 sparsity 的分析，可与本文\"SwiGLU 无天然稀疏性\"的假设对比。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n**一句话总结：** 论文提出了一个有价值的研究问题并提供了系统的实证分析，但核心归因框架（97.5% signal-type）与自身下游指标矛盾、C1 ablation 存在循环论证、且完全缺乏实际加速验证，使其分析叙事和实用贡献均有关键缺口。\n\n该论文的实证贡献——KL distillation 系统性优于 BCE 用于 sparsity prediction training——是可靠的，值得发表。但以下因素限制了其达到 Conference 水准：\n\n1. **分析叙事断裂**：97.5% 归因是论文最吸引人的 claim，但仅基于 PPL，与下游指标矛盾（5–8pp coupling 贡献被 97.5% 掩盖）。如果这个 claim 得到修正和扩展（补充下游指标的定量分解），论文会显著更强。\n\n2. **因果推断链有缺口**：C1 ablation 的循环论证（KL 发现的 masks → BCE 也能用 → 所以 mask quality 比 coupling 重要，但忽略了 KL 是发现这些 masks 的唯一途径）使得论文无法清晰回答\"what specifically does KL contribute\"。\n\n3. **实用价值未验证**：对于 sparsity 方法论文，缺乏任何 speedup 数据是硬伤。即使自我定位为 analytical study，也应至少提供 proof-of-concept。\n\n**推荐：Findings 接收**——实证发现有价值，但分析叙事需要实质性修正才能达到 Conference 水平。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n\n---\n\n## Summary\n\n本文提出用 forward KL divergence 替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的上下文稀疏性预测器。核心 insight 是：BCE 将每个神经元的激活视为独立二分类问题，梯度不跨层耦合；而 KL 在输出分布层面优化，通过完整前向传播产生耦合梯度，使预测器发现与 magnitude-based oracle 有 46–68% 差异的 mask patterns。在 LLaMA-3.1-8B 和 Qwen-2.5-14B 上，KL 在 30% 稀疏度下 PPL 优于 TEAL 14.5%（matched sparsity），并在多数下游任务上保持竞争力。论文通过 target-swap ablation (C1)、per-layer KL decomposition 等消融实验分析了 KL 优势的来源。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 KL 框架数学正确；但 97.5% signal-type 归因基于 PPL 而非下游指标，C1 ablation 存在循环论证，削弱了分析叙事的可信度 |\n| Excitement | 2.5/5 | 研究问题有意义（BCE 独立性限制），但无实际加速、knowledge-intensive 任务退步显著，实用影响有限 |\n| Reproducibility | 4/5 | 超参数详细、主实验有 3-seed 统计、训练细节完整；代码未提供但可根据描述复现 |\n| Overall Assessment | **3.0** (Findings) | 实证贡献扎实但分析叙事有关键缺口，且缺乏实际加速验证 |\n| Reviewer Confidence | 4/5 | 熟悉 contextual sparsity、知识蒸馏和 SwiGLU 架构相关工作 |\n\n---\n\n## 主要优势\n\n**S1. 研究问题清晰且有意义。** BCE 将每个神经元独立处理的局限性是 contextual sparsity 文献中一个被忽视的问题。用 output-distribution distillation 替代 per-neuron classification 是一个自然且有价值的研究方向。\n\n**S2. 消融设计系统且深入。** C1 target-swap ablation（§4.4）、per-layer KL decomposition（§4.5/§3.7）、4 种 loss 变体对比（Table 4）、relaxation 方法对比（Gumbel vs STE）形成了较完整的消融体系。\n\n**S3. 梯度分析的 hedging 恰当。** §3.6 将 BCE vs KL 梯度结构对比标注为\"suggestive\"，未过度声称理论因果关系，而是用实验（§4.4）提供支撑证据。这种诚实的表述值得肯定。\n\n**S4. 训练效率优势明确。** KL 在 1000 steps 达到的效果优于 BCE 2700 steps（§4.3, PPL 11.79 vs 28.13），且 wall-clock 时间相当（~45 min），这是一个有实用价值的发现。\n\n**S5. 附录内容充实。** 19 个附录覆盖了 inference latency（App A）、bottleneck sensitivity（App B）、temperature schedule（App B.1）、training convergence（App B.2）、penalty controller dynamics（App C）、OOD evaluation（App D）等，增强了可复现性。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **97.5% signal-type 归因与下游指标矛盾，叙事有误导风险**\n- 具体位置：§3.7（page 5）及 §4.5（page 8）\n- 问题：论文声称\"signal type accounts for 97.5% of the PPL gap\"（§3.7），但紧接着承认\"cross-layer coupling contributes downstream benefit (1–4pp on ARC-Challenge and WinoGrande)\"以及\"per-layer KL underperforms end-to-end KL by 5–8pp on commonsense tasks\"（§4.5）。这意味着 coupling scope 对下游任务的贡献远超 2.5%，但论文的主叙事（包括 abstract 和 conclusion）反复强调 97.5% 这个数字，可能给读者造成\"coupling 不重要\"的错误印象。\n- 为什么影响接收：论文的核心分析框架（signal type vs coupling scope 的 2D 分解）假设这两个因素可加性分解且 PPL 是充分代理指标。但下游指标显示非加性交互存在。这不是小的表述问题，而是分析叙事的核心主张与自身实验证据之间的不一致。\n- 建议修改方向：(1) 在 abstract/conclusion 中明确 97.5% 仅适用于 PPL，下游指标显示 coupling 贡献更大；(2) 补充下游指标的 2D 分解定量结果（不仅是 1–4pp 的定性描述）；(3) 讨论 PPL 作为代理指标的局限性。\n\n**N2** [critical] **C1 target-swap ablation 的循环论证未充分讨论**\n- 具体位置：§4.4（page 7）, Table 3\n- 问题：C1 将 KL 发现的 masks 交给 BCE 训练，结果 BCE 也能获得接近 KL 的 PPL。论文将此解释为\"mask quality is the proximate driver, not gradient coupling\"。但这些 masks 恰恰是由 KL 的耦合梯度发现的——如果没有 KL 训练，这些 mask targets 根本不存在。因此 C1 证明的是\"KL-derived masks transferable to BCE\"，而非\"coupling 不重要\"。\n- 为什么影响接收：这个 ablation 是论文因果分析链的关键环节。如果 C1 的解释存在循环（KL 的贡献被归结为 mask quality，但 mask quality 来自 KL 的 coupling），那么论文关于\"what matters\"的核心结论需要重新审视。\n- 建议修改方向：(1) 明确讨论这个循环性：C1 证明了 mask 的 transferability，但 KL 的 coupling 是发现这些 masks 的必要条件；(2) 补充反向实验——能否用其他方法（如 evolutionary search、random perturbation）找到同等质量的 masks？如果只有 KL 能发现，则 coupling 的贡献不可被 C1 消解。\n\n**N3** [critical] **无实际 wall-clock 加速，实用价值存疑**\n- 具体位置：§4.6（page 8）, Appendix A（page 13）, Limitations（page 9）\n- 问题：Table 5 显示 KL-sparse pipeline 增加 +6.4% latency overhead，但没有任何 wall-clock speedup 结果。论文承认\"wall-clock speedup requires sparse kernel support not yet implemented here\"（Limitations, page 9）。对于一篇 contextual sparsity 方法论文，缺乏实际加速验证是重大缺陷。\n- 为什么影响接收：Sparsity 的唯一目的是推理加速。即使论文自我定位为\"analytical understanding\"（Limitations），但 abstract 和 introduction 均以\"inference-free activation sparsity\"和\"lightweight predictor\"作为 motivation，暗示实用价值。如果无法展示加速，读者无法判断改进的 mask quality 是否有实际意义。\n- 建议修改方向：(1) 至少提供 Triton/cuSPARSE 的概念验证 speedup 数字，即使不完整；(2) 如果无法提供，在 abstract 和 introduction 中显著弱化 practical motivation，明确声明这是一项分析性研究。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] **14B 实验覆盖不足，GSM8K 退步严重且缺乏对比**\n- 具体位置：Table 13（page 16），§4.6（page 8）\n- 问题：14B（Qwen-2.5-14B）仅在 30% sparsity 下有完整下游评估。GSM8K 从 dense 52.1% 降至 32.1±5.2%（−20pp），高 seed variance（±5.2）暗示不稳定性。但论文未给出 TEAL 在 14B 上的 GSM8K 对比，无法判断这是 KL 方法的问题还是 contextual sparsity 的通病。Table 16（page 18）有 cross-architecture 结果但同样仅 30%。\n- 建议：(1) 补充 TEAL 在 14B 上的完整下游指标对比；(2) 补充 14B 50% sparsity 的下游结果（HellaSwag/PIQA 已有，缺其他指标）；(3) 讨论 GSM8K 高 variance 的原因。\n\n**W2** [major] **Knowledge-intensive 任务系统性退步缺乏机制解释**\n- 具体位置：Table 2（page 6），Limitations（page 9）\n- 问题：8B 30% sparsity 下 MMLU −5.2pp（Table 2, KL global vs dense），14B 30% GSM8K −20pp。论文在 Limitations 中承认\"KL's mass-covering property may preserve output quality at the expense of reasoning-critical pathways\"，但这是推测性的一句话，缺乏任何分析证据。\n- 建议：(1) 分析 knowledge-intensive tasks 上 per-layer mask 差异是否与 attention/FFN 的 knowledge storage 层相关；(2) 讨论 forward KL 的 mode-covering 特性是否系统性地牺牲了低频但重要的 knowledge patterns。\n\n**W3** [major] **MSE baseline 的 failed seed 报告方式不透明**\n- 具体位置：Table 4（page 7）\n- 问题：Per-layer MSE 在 50% sparsity 下达到 PPL 229.26（Table 4），远超正常范围。Appendix G 提到\"3-seed, with seed 123, ... random-level, indicating high sensitivity to initialization—a failure mode not observed with KL-based losses\"。如果 3 个 seeds 中有一个 catastrophic failure（如 PPL=15789 在某处提到），在 mean±std 中报告会严重扭曲统计。论文应明确每个 seed 的值并讨论 failure mode。\n- 建议：(1) Table 4 中标注哪些 entries 包含 failed seeds；(2) 分别报告 median 和 mean，或排除 failed seeds 后单独报告。\n\n**W4** [minor] **OOD variance 增大 (CV 0.2%→6.3%) 需更多讨论**\n- 具体位置：Appendix D（page 14）, Limitations（page 9）\n- 问题：C4 上 cross-seed PPL variance 的 coefficient of variation 从 in-domain 的 0.2% 增至 6.3%。虽然绝对 PPL（16.03）仍合理，但 30× 的 variance 增幅暗示 KL predictor 可能对 domain shift 敏感。论文仅简单提到\"the predictor partially overfits to training-domain activation patterns\"但未深入分析。\n- 建议：分析哪些层的 mask patterns 在 OOD 时变化最大，以及这是否与 per-layer allocation budget 的 non-monotonic behavior 相关。\n\n**W5** [minor] **Actual sparsity mismatch 的讨论虽在附录但不够显著**\n- 具体位置：Table 2 footnote（page 6），Appendix D（page 14）\n- 问题：KL 在 30% target 下实际只达到 28.5%（vs TEAL 29.3%）。虽然 Appendix D 有 matched-sparsity 对比，但主表（Table 2）的 headline comparison 使用了不同实际稀疏度下的数字。论文 abstract 的\"14.5% over TEAL\"使用了 matched-sparsity 数字，这一点没有在 abstract 中说明。\n- 建议：在 Table 2 中直接标注各方法的实际稀疏度，而非仅用脚注。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.4 Eq.(5): 符号 $p_{\\text{dense}}$ 和 $p_{\\text{sparse}}$ 在引入前建议先定义清楚，当前定义在 Eq.(5) 下方的段落中出现，但 Eq.(5) 本身先用了这些符号。\n- Figure 2（page 8）: y 轴标签\"PPL↓\"但图中值越高越差，建议标注为\"PPL\"（不加箭头）或使用 log scale 让差异更明显。\n- Table 1（page 5）: 该 taxonomy table 信息密度高，但\"Per-token × Coupled cell\"仅由本文占据，可能暗示 positioning 过于强调 novelty 而非实质差异。\n- Limitations 中提到\"scaling to 70B remains untested\"——建议明确这是由于计算资源限制还是方法论障碍。\n\n---\n\n## Questions for Authors\n\n**Q1.** 你们在 §4.5 的 2D 分解中能否提供下游指标（ARC, MMLU, WinoGrande）的定量分解结果？这对于评估 97.5% 归因的适用范围至关重要。\n\n**Q2.** C1 ablation 中，BCE 使用 KL-derived masks 作为 target 训练时，是否也使用了 Gumbel-Sigmoid relaxation？如果 C1 只用了 hard threshold，那么 C1 和 KL 之间的差异可能部分来自 relaxation method 而非 mask quality。\n\n**Q3.** 对于 14B 上 GSM8K 的 −20pp 退步和 ±5.2 的高 seed variance，你们是否分析过是哪些层的 masks 在不同 seeds 间差异最大？这可能揭示 reasoning 能力退化的机制。\n\n**Q4.** 是否有证据表明其他方法（如 evolutionary search 或 gradient-free optimization）能发现与 KL 类似质量的 masks？如果有，则 C1 的\"mask quality > coupling\"结论更强；如果没有，则说明 coupling 是 mask discovery 的必要条件。\n\n**Q5.** Compensation network 被声称为 redundant（+67.2M params），但在 capacity-limited regime（§4.6 提到的 ≤45% sparsity），compensation 是否可能变得必要？\n\n---\n\n## Missing References\n\n- **PowerInfer** (Song et al., 2024b) 已引用，但 **PowerInfer-2**（Xue et al., 2024）的 on-device sparsity work 可能相关。\n- **Wanda** (Sun et al., 2024) 的 structured pruning 方法与本文的 unstructured contextual sparsity 有方法论对比价值。\n- **ReLU-fication** literature（如 Mirzadeh et al., 2024 已引用）中关于 SwiGLU 到 ReLU 转换后天然 sparsity 的分析，可与本文\"SwiGLU 无天然稀疏性\"的假设对比。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n**一句话总结：** 论文提出了一个有价值的研究问题并提供了系统的实证分析，但核心归因框架（97.5% signal-type）与自身下游指标矛盾、C1 ablation 存在循环论证、且完全缺乏实际加速验证，使其分析叙事和实用贡献均有关键缺口。\n\n该论文的实证贡献——KL distillation 系统性优于 BCE 用于 sparsity prediction training——是可靠的，值得发表。但以下因素限制了其达到 Conference 水准：\n\n1. **分析叙事断裂**：97.5% 归因是论文最吸引人的 claim，但仅基于 PPL，与下游指标矛盾（5–8pp coupling 贡献被 97.5% 掩盖）。如果这个 claim 得到修正和扩展（补充下游指标的定量分解），论文会显著更强。\n\n2. **因果推断链有缺口**：C1 ablation 的循环论证（KL 发现的 masks → BCE 也能用 → 所以 mask quality 比 coupling 重要，但忽略了 KL 是发现这些 masks 的唯一途径）使得论文无法清晰回答\"what specifically does KL contribute\"。\n\n3. **实用价值未验证**：对于 sparsity 方法论文，缺乏任何 speedup 数据是硬伤。即使自我定位为 analytical study，也应至少提供 proof-of-concept。\n\n**推荐：Findings 接收**——实证发现有价值，但分析叙事需要实质性修正才能达到 Conference 水平。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-22T08:30:31.573843+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4321
}
```

</details>

---


### Assistant

_source line 1060 · 2026-05-22T08:30:40.717691+00:00_

审稿意见已提交给 Review Director。

**核心评价**：Overall 3.0 (Findings)。

三个 critical issues：
1. **97.5% signal-type 归因与下游指标矛盾** — coupling scope 对下游任务贡献远超 PPL 暗示的 2.5%，但论文叙事反复强调 97.5%
2. **C1 target-swap ablation 循环论证** — KL-derived masks 交给 BCE 也能用 ≠ coupling 不重要，因为这些 masks 只有 KL 的 coupled gradients 才能发现
3. **完全缺乏 wall-clock speedup** — 一篇 sparsity 方法论文没有任何加速数据

三个 major issues：14B 评估不足（GSM8K −20pp 且缺 TEAL 对比）、knowledge-intensive 退步缺机制解释、MSE failed seed 报告不透明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 33

## Round 33

4 recorded events


### User

_source line 1061 · 2026-05-22T08:31:36.211426+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/小问题，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

**Overall Assessment**: 3.0 (Findings)

### Must-Fix 问题

**N1** [Critical] 与 MaskLLM 的新颖性区分不足
- 核心配方 (frozen weights + learnable masks + KL divergence + Gumbel relaxation) 与 MaskLLM (Fang et al., 2024, NeurIPS) 完全一致。三点区分——(1) sparsity type (weight vs activation), (2) mask generation (direct params vs predictor network), (3) allocation (N:M vs global top-k)——都是 application-level adaptation。
- "KL 优于 BCE"这一核心 insight 已被 MaskLLM 的方法选择所暗示。论文的附加贡献（2D taxonomy、C1 ablation、coupling hierarchy）有价值但不足以独立撑起 main conference bar。

**N2** [Critical] Efficiency motivation 与实际无 wall-clock speedup 的叙事张力
- Introduction 第一段以 efficiency 为动机，但 Table 5 显示 +6.4% latency overhead。unstructured masks 无法实际加速推理。motivation 和 actual contribution 之间的 gap 太大。

### Should-Fix 问题

**W1** [Major] 14B 结果与核心叙事矛盾，但在 framing 中被淡化
- Qwen-2.5-14B: MMLU -2.79pp, GSM8K -20pp (32.1±5.2% vs TEAL 52.1%)。这些 negative results 与论文的核心 narrative（KL 优于 magnitude-based methods）直接矛盾。Limitations 中的解释过于笼统。

**W2** [Major] Target-swap ablation (C1) 存在 confound
- C1 同时改变了 mask 表征（hard vs soft）和 target（magnitude vs KL-derived）。soft-vs-hard confound 的排除实验只排除了 softness 有利于 BCE 的可能，没有排除 softness 与 KL targets 的 interaction。oracle masks 来自特定 KL training trajectory，trajectory dependence 是 open question。

**W3** [Major] "2D Taxonomy" / "Coupling Alignment Hierarchy" 叙事有 overclaim 风险
- Table 1 的 "2D taxonomy" 实质上是一个 2×3 分类表。称之为论文核心贡献之一有 overclaim。"Coupling alignment hierarchy" 本质上是实验排序，使用 "hierarchy" 一词过于宏大。

**W4** [Minor] 30% sparsity "sweet spot" 限制了实际影响
- 30% 下 KL 工作良好，但 40% 时 MMLU 降至 35.5%，50% 时 MMLU 崩溃。30% 稀疏度 + 无 speedup = 实际部署价值有限。

### 小问题
- Responsible NLP Research Checklist 出现在 PDF 中，应仅在 OpenReview form 中填写
- Table 2 caption footnote 过于密集
- Abstract 中 "post-hoc compensation becomes redundant" 可能误导

### Questions
1. 是否考虑将 MaskLLM 适配到 activation sparsity setting 直接对比？
2. 14B GSM8K 逆转的根因有更具体 evidence 吗？
3. 是否测试过多样化训练数据对 downstream 的影响？
4. Per-layer KL 的 train-inference distribution shift confound 有其他设计来控制吗？

### Missing References
- AWQ (Lin et al., 2024, MLSys) 的 activation-aware channel selection 可能相关

### 格式合规
- Responsible NLP Checklist 在 PDF 中 ❌ 未通过（应仅在 OpenReview form 中填写）
- 其他所有格式检查均通过

---

请对以上每个 Must-Fix、Should-Fix 和小问题逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-22T08:33:24.341780+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: 与 MaskLLM 的新颖性区分不足**\n\nR2 的核心主张——\"KL 优于 BCE 已被 MaskLLM 暗示\"——过度简化了两者的差异。\n\n1. **问题域本质不同**：MaskLLM 做的是 static weight sparsity（N:M structured，mask 在训练后固定），本文做的是 dynamic activation sparsity（mask 依赖 input，每个 token 不同）。这不是\"application-level adaptation\"——从 static mask optimization 到 input-conditioned predictor network 是一个非平凡的架构转变。MaskLLM 的直接可学习 mask 参数根本无法处理 unseen inputs，而本文的 predictor 必须泛化到 inference-time 的任意输入（§3.2, Eq. 3）。\n\n2. **核心贡献不是\"用 KL\"，而是\"分析 KL 为何有效\"**：MaskLLM 选择 KL 但未分析 BCE 为何不行。本文的贡献在于：(a) §3.6 的梯度结构对比（虽 suggestive）；(b) §4.5 的 signal-type vs coupling-scope 分解；(c) C1 target-swap ablation；(d) per-layer Jaccard divergence 分析（§4.4, Figure 7）。这些是独立的分析性贡献，不依赖于 MaskLLM 的存在。\n\n3. **但 R2 有部分道理**：论文确实应该更早、更显著地与 MaskLLM 对比（当前在 §2 Related Work 中提及但对比不够尖锐），明确说明\"MaskLLM 在 weight sparsity 中使用了相似配方，本文的贡献在于将此扩展到 activation sparsity 并提供了系统性的 ablation 分析\"。\n\n**总结**：不同意将其标记为 Critical/Must-Fix。新颖性不在配方本身而在分析框架。但同意需要更 sharp 的 MaskLLM 对比。建议降级为 Should-Fix。\n\n---\n\n**[AGREE] R2-N2: Efficiency motivation 与无 speedup 的叙事张力**\n\n完全同意，这与我的 N3 一致。论文 Introduction 第一段以\"large fraction of FFN neurons contribute negligibly to the output\"开篇暗示 efficiency gain，但全文无 wall-clock speedup 数据。Table 5 的 +6.4% overhead 进一步加剧了 motivation-contribution 的 gap。\n\n补充一点 R2 未提到的：即使 unstructured masks 目前无法用标准 CUDA kernel 加速，近期 Triton block-sparse（已在 Appendix A page 13 提到但未实际测试）和 cuSPARSE 的进展使得 proof-of-concept speedup 并非不可能。论文完全缺乏尝试是一个遗憾。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: 14B 结果与核心叙事矛盾**\n\n部分反驳 R2 的 framing。\n\n1. **R2 的对比对象有误**：\"GSM8K -20pp (32.1±5.2% vs TEAL 52.1%)\" 中的 52.1% 是 **dense baseline**，不是 TEAL。论文中 TEAL 在 14B 上的 GSM8K 数据实际上缺失（这正是我在 W1 中指出的问题）。如果 TEAL 在 14B GSM8K 上同样退步严重，则不能说 KL \"与核心叙事矛盾\"——而是说 contextual sparsity 方法在 reasoning tasks 上普遍有限制。\n\n2. **但核心关切成立**：无论 TEAL 表现如何，KL 在 14B 上 GSM8K −20pp、±5.2 高 variance 确实是严重的 negative result。论文将其淡化为 Limitations 中的一句话（\"reasoning decline…KL's mass-covering property may preserve output quality at the expense of reasoning-critical pathways\"，page 9）是不够的。\n\n3. **建议**：同意需要补充 TEAL 在 14B 上的完整对比，但不同意\"与核心叙事矛盾\"的 framing——在缺乏 baseline 对比的情况下，这是一个 coverage gap 而非 contradiction。\n\n---\n\n**[AGREE] R2-W2: C1 target-swap ablation 存在 confound**\n\n同意，但我的关切与 R2 不同，两者互补。\n\n- **R2 的关切（soft-vs-hard confound）**：C1 用 hard binary KL-derived masks 训练 BCE，而原始 KL 训练用 Gumbel-Sigmoid soft masks。soft representation 可能与 KL loss 有 interaction（例如 soft masks 允许 gradient flow 更平滑），C1 未控制这个变量。这是有效的方法论关切。\n\n- **我的关切（circularity，R1-N2）**：C1 的 KL-derived mask targets 本身就是 KL 耦合梯度的产物。\"mask quality > coupling\" 的结论因此有循环性——coupling 是发现这些高质量 masks 的必要条件。\n\n两个 confound 叠加使得 C1 的因果推断力显著减弱。建议作者同时回应两个关切。\n\n---\n\n**[REBUT] R2-W3: \"2D Taxonomy\" / \"Coupling Alignment Hierarchy\" overclaim**\n\n部分不同意。\n\n1. **Table 1 的 taxonomy 确实仅是分类表**：同意 R2 指出\"2D taxonomy\"作为论文贡献之一被高估了。Table 1 本身是一个 2×3 表格，信息量有限。\n\n2. **但 §4.5 的 2D 分解有实质分析价值**：将 signal type 和 coupling scope 正交分解，并用 4 个实验配置定量测量各自贡献（虽然我在 N1 中指出了 PPL vs downstream 的不一致），这不仅仅是命名。它提供了一个可被后续工作使用的分析框架。\n\n3. **\"Hierarchy\" 一词确实过于宏大**：用\"ranking\"或\"ordering\"更准确。\n\n**总结**：同意术语可以更谦逊（Minor 级别修改），但不同意 2D 分解本身缺乏实质——它是论文分析贡献的核心之一。建议从 Major 降级为 Minor。\n\n---\n\n**[AGREE] R2-W4: 30% sparsity \"sweet spot\" 限制实际影响**\n\n同意。论文在 Limitations（page 9）承认\"30% appears to be the lowest-degradation sparsity level for downstream fidelity\"。40% 时 MMLU 降至 35.5%（Table 15, page 18），50% 时多数 downstream tasks 大幅退化。结合无 wall-clock speedup，30% 的 sweet spot 确实限制了实用价值。\n\n---\n\n### 小问题\n\n**[AGREE] Responsible NLP Checklist 在 PDF 中**\n\n根据 EMNLP 2026/ARR 规定，Responsible NLP Research Checklist 应仅在 OpenReview submission form 中填写，不应出现在论文 PDF 中。Page 10 的 \"Responsible NLP Research Checklist\" section（A1–E1 条目）违反此规定。这是一个格式合规问题，应在提交前移除。\n\n**[AGREE] Table 2 caption footnote 过于密集**\n\n同意。Table 2 的 caption 包含多个关键信息（extended training budget、no compensation、actual sparsity mismatch、seed details），密度过高容易遗漏。建议将 actual sparsity 信息移入主表的单独列。\n\n**[REBUT] Abstract 中 \"post-hoc compensation becomes redundant\" 可能误导**\n\n部分不同意\"误导\"的判断。Abstract 原文是\"post-hoc compensation (+67.2M params) becomes redundant\"，这有 Table 4 和 §4.5 的实验支撑——在 KL 训练下移除 compensation 对 PPL 的影响确实很小。但 R2 的关切可能在于：(a) 在 capacity-limited regime（>45% sparsity）compensation 可能重新变得必要（§4.6 暗示了这一点）；(b) \"redundant\" 一词过于绝对。建议改为\"largely unnecessary at moderate sparsity levels\"，但不认为当前措辞构成误导。\n\n---\n\n### Questions 回应\n\n**Q1 (MaskLLM 直接适配对比)**: 有价值的实验建议。将 MaskLLM 适配到 activation sparsity（用 per-token learnable masks 替代 predictor network，或用 MaskLLM 的 N:M schedule 替代 global top-k）可以更清晰地隔离 predictor architecture 的贡献。我支持作者考虑此实验。\n\n**Q2 (14B GSM8K 根因)**: 与我的 Q3 一致。需要 per-layer mask stability 分析来定位 reasoning degradation 的来源。\n\n**Q3 (训练数据多样性)**: 有价值。当前仅用 WikiText-103 训练，可能导致 knowledge-intensive tasks 的系统性退步（与我的 W2 相关）。\n\n**Q4 (Per-layer KL train-inference distribution shift)**: 这是一个我未注意到的好问题。Per-layer KL 在训练时逐层优化，但推理时使用 TEAL 的 global allocation。训练和推理的 allocation strategy 不同可能引入 distribution shift confound，特别是对于 §4.5 中 per-layer KL 的实验结果解读。\n\n---\n\n### Missing References\n\n**[AGREE]** AWQ (Lin et al., 2024) 的 activation-aware channel selection 确实与本文的 activation-importance-based mask generation 有方法论联系，值得讨论。\n\n---\n\n### 总体评价\n\nR2 的审稿抓到了一些真问题（efficiency gap、14B coverage、C1 confound），但 N1（MaskLLM novelty）的严重性被高估了——weight sparsity 和 activation sparsity 的问题域差异不是 application-level adaptation，论文的核心贡献在分析框架而非 KL+Gumbel 配方本身。\n\n**我维持 Overall 3.0 (Findings)** 的评分。论文的实证贡献足够支撑 Findings，但 N2/N3（efficiency gap）和 N1（97.5% 归因矛盾）是阻碍 Conference 接收的主要因素。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: 与 MaskLLM 的新颖性区分不足**\n\nR2 的核心主张——\"KL 优于 BCE 已被 MaskLLM 暗示\"——过度简化了两者的差异。\n\n1. **问题域本质不同**：MaskLLM 做的是 static weight sparsity（N:M structured，mask 在训练后固定），本文做的是 dynamic activation sparsity（mask 依赖 input，每个 token 不同）。这不是\"application-level adaptation\"——从 static mask optimization 到 input-conditioned predictor network 是一个非平凡的架构转变。MaskLLM 的直接可学习 mask 参数根本无法处理 unseen inputs，而本文的 predictor 必须泛化到 inference-time 的任意输入（§3.2, Eq. 3）。\n\n2. **核心贡献不是\"用 KL\"，而是\"分析 KL 为何有效\"**：MaskLLM 选择 KL 但未分析 BCE 为何不行。本文的贡献在于：(a) §3.6 的梯度结构对比（虽 suggestive）；(b) §4.5 的 signal-type vs coupling-scope 分解；(c) C1 target-swap ablation；(d) per-layer Jaccard divergence 分析（§4.4, Figure 7）。这些是独立的分析性贡献，不依赖于 MaskLLM 的存在。\n\n3. **但 R2 有部分道理**：论文确实应该更早、更显著地与 MaskLLM 对比（当前在 §2 Related Work 中提及但对比不够尖锐），明确说明\"MaskLLM 在 weight sparsity 中使用了相似配方，本文的贡献在于将此扩展到 activation sparsity 并提供了系统性的 ablation 分析\"。\n\n**总结**：不同意将其标记为 Critical/Must-Fix。新颖性不在配方本身而在分析框架。但同意需要更 sharp 的 MaskLLM 对比。建议降级为 Should-Fix。\n\n---\n\n**[AGREE] R2-N2: Efficiency motivation 与无 speedup 的叙事张力**\n\n完全同意，这与我的 N3 一致。论文 Introduction 第一段以\"large fraction of FFN neurons contribute negligibly to the output\"开篇暗示 efficiency gain，但全文无 wall-clock speedup 数据。Table 5 的 +6.4% overhead 进一步加剧了 motivation-contribution 的 gap。\n\n补充一点 R2 未提到的：即使 unstructured masks 目前无法用标准 CUDA kernel 加速，近期 Triton block-sparse（已在 Appendix A page 13 提到但未实际测试）和 cuSPARSE 的进展使得 proof-of-concept speedup 并非不可能。论文完全缺乏尝试是一个遗憾。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: 14B 结果与核心叙事矛盾**\n\n部分反驳 R2 的 framing。\n\n1. **R2 的对比对象有误**：\"GSM8K -20pp (32.1±5.2% vs TEAL 52.1%)\" 中的 52.1% 是 **dense baseline**，不是 TEAL。论文中 TEAL 在 14B 上的 GSM8K 数据实际上缺失（这正是我在 W1 中指出的问题）。如果 TEAL 在 14B GSM8K 上同样退步严重，则不能说 KL \"与核心叙事矛盾\"——而是说 contextual sparsity 方法在 reasoning tasks 上普遍有限制。\n\n2. **但核心关切成立**：无论 TEAL 表现如何，KL 在 14B 上 GSM8K −20pp、±5.2 高 variance 确实是严重的 negative result。论文将其淡化为 Limitations 中的一句话（\"reasoning decline…KL's mass-covering property may preserve output quality at the expense of reasoning-critical pathways\"，page 9）是不够的。\n\n3. **建议**：同意需要补充 TEAL 在 14B 上的完整对比，但不同意\"与核心叙事矛盾\"的 framing——在缺乏 baseline 对比的情况下，这是一个 coverage gap 而非 contradiction。\n\n---\n\n**[AGREE] R2-W2: C1 target-swap ablation 存在 confound**\n\n同意，但我的关切与 R2 不同，两者互补。\n\n- **R2 的关切（soft-vs-hard confound）**：C1 用 hard binary KL-derived masks 训练 BCE，而原始 KL 训练用 Gumbel-Sigmoid soft masks。soft representation 可能与 KL loss 有 interaction（例如 soft masks 允许 gradient flow 更平滑），C1 未控制这个变量。这是有效的方法论关切。\n\n- **我的关切（circularity，R1-N2）**：C1 的 KL-derived mask targets 本身就是 KL 耦合梯度的产物。\"mask quality > coupling\" 的结论因此有循环性——coupling 是发现这些高质量 masks 的必要条件。\n\n两个 confound 叠加使得 C1 的因果推断力显著减弱。建议作者同时回应两个关切。\n\n---\n\n**[REBUT] R2-W3: \"2D Taxonomy\" / \"Coupling Alignment Hierarchy\" overclaim**\n\n部分不同意。\n\n1. **Table 1 的 taxonomy 确实仅是分类表**：同意 R2 指出\"2D taxonomy\"作为论文贡献之一被高估了。Table 1 本身是一个 2×3 表格，信息量有限。\n\n2. **但 §4.5 的 2D 分解有实质分析价值**：将 signal type 和 coupling scope 正交分解，并用 4 个实验配置定量测量各自贡献（虽然我在 N1 中指出了 PPL vs downstream 的不一致），这不仅仅是命名。它提供了一个可被后续工作使用的分析框架。\n\n3. **\"Hierarchy\" 一词确实过于宏大**：用\"ranking\"或\"ordering\"更准确。\n\n**总结**：同意术语可以更谦逊（Minor 级别修改），但不同意 2D 分解本身缺乏实质——它是论文分析贡献的核心之一。建议从 Major 降级为 Minor。\n\n---\n\n**[AGREE] R2-W4: 30% sparsity \"sweet spot\" 限制实际影响**\n\n同意。论文在 Limitations（page 9）承认\"30% appears to be the lowest-degradation sparsity level for downstream fidelity\"。40% 时 MMLU 降至 35.5%（Table 15, page 18），50% 时多数 downstream tasks 大幅退化。结合无 wall-clock speedup，30% 的 sweet spot 确实限制了实用价值。\n\n---\n\n### 小问题\n\n**[AGREE] Responsible NLP Checklist 在 PDF 中**\n\n根据 EMNLP 2026/ARR 规定，Responsible NLP Research Checklist 应仅在 OpenReview submission form 中填写，不应出现在论文 PDF 中。Page 10 的 \"Responsible NLP Research Checklist\" section（A1–E1 条目）违反此规定。这是一个格式合规问题，应在提交前移除。\n\n**[AGREE] Table 2 caption footnote 过于密集**\n\n同意。Table 2 的 caption 包含多个关键信息（extended training budget、no compensation、actual sparsity mismatch、seed details），密度过高容易遗漏。建议将 actual sparsity 信息移入主表的单独列。\n\n**[REBUT] Abstract 中 \"post-hoc compensation becomes redundant\" 可能误导**\n\n部分不同意\"误导\"的判断。Abstract 原文是\"post-hoc compensation (+67.2M params) becomes redundant\"，这有 Table 4 和 §4.5 的实验支撑——在 KL 训练下移除 compensation 对 PPL 的影响确实很小。但 R2 的关切可能在于：(a) 在 capacity-limited regime（>45% sparsity）compensation 可能重新变得必要（§4.6 暗示了这一点）；(b) \"redundant\" 一词过于绝对。建议改为\"largely unnecessary at moderate sparsity levels\"，但不认为当前措辞构成误导。\n\n---\n\n### Questions 回应\n\n**Q1 (MaskLLM 直接适配对比)**: 有价值的实验建议。将 MaskLLM 适配到 activation sparsity（用 per-token learnable masks 替代 predictor network，或用 MaskLLM 的 N:M schedule 替代 global top-k）可以更清晰地隔离 predictor architecture 的贡献。我支持作者考虑此实验。\n\n**Q2 (14B GSM8K 根因)**: 与我的 Q3 一致。需要 per-layer mask stability 分析来定位 reasoning degradation 的来源。\n\n**Q3 (训练数据多样性)**: 有价值。当前仅用 WikiText-103 训练，可能导致 knowledge-intensive tasks 的系统性退步（与我的 W2 相关）。\n\n**Q4 (Per-layer KL train-inference distribution shift)**: 这是一个我未注意到的好问题。Per-layer KL 在训练时逐层优化，但推理时使用 TEAL 的 global allocation。训练和推理的 allocation strategy 不同可能引入 distribution shift confound，特别是对于 §4.5 中 per-layer KL 的实验结果解读。\n\n---\n\n### Missing References\n\n**[AGREE]** AWQ (Lin et al., 2024) 的 activation-aware channel selection 确实与本文的 activation-importance-based mask generation 有方法论联系，值得讨论。\n\n---\n\n### 总体评价\n\nR2 的审稿抓到了一些真问题（efficiency gap、14B coverage、C1 confound），但 N1（MaskLLM novelty）的严重性被高估了——weight sparsity 和 activation sparsity 的问题域差异不是 application-level adaptation，论文的核心贡献在分析框架而非 KL+Gumbel 配方本身。\n\n**我维持 Overall 3.0 (Findings)** 的评分。论文的实证贡献足够支撑 Findings，但 N2/N3（efficiency gap）和 N1（97.5% 归因矛盾）是阻碍 Conference 接收的主要因素。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-22T08:33:28.257384+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Assistant

_source line 1064 · 2026-05-22T08:33:36.588449+00:00_

已完成对 Reviewer 2 全部意见的逐条回应，已提交给 Review Director。

总结：
- **N1 (MaskLLM novelty)**: [REBUT] — weight vs activation sparsity 是本质不同的问题域，核心贡献在分析框架不在配方。但同意需更 sharp 的 MaskLLM 对比。
- **N2 (no speedup)**: [AGREE] — 与我的 N3 一致。
- **W1 (14B contradiction)**: [REBUT framing] — R2 将 dense baseline 误标为 TEAL，但同意 coverage 不足。
- **W2 (C1 confound)**: [AGREE] — soft-vs-hard confound 与我的 circularity 关切互补。
- **W3 (taxonomy overclaim)**: [REBUT severity] — 术语可谦逊，但 2D 分解有实质价值，建议降级为 Minor。
- **W4 (30% sweet spot)**: [AGREE]。
- 小问题：Checklist 格式 [AGREE]，Table 2 density [AGREE]，"redundant" 措辞 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 34

## Round 34

62 recorded events


### User

_source line 1065 · 2026-05-22T09:35:08.184493+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。

## Venue 信息
- **目标会议**：EMNLP 2026 (Long Paper, ARR May 2026 cycle)
- **截止日期**：2026-05-25
- **格式要求**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数
- **模板**：ACL LaTeX template（已使用 `\usepackage[review]{acl}`）
- **匿名规则**：双盲审稿，无匿名期限制
- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit）

## 论文文件
- LaTeX 主文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf`

## 你的审查侧重

### 1. KL 蒸馏方法严谨性
- §3.6 的梯度分析（BCE vs KL gradient structure）是否数学正确？推导是否完整？
- Forward KL vs Reverse KL 的论证（mode-covering vs mode-seeking）是否站得住？
- Gumbel-Sigmoid relaxation 的使用是否合理？与 STE 的对比是否 fair？

### 2. C1 Target-Swap Ablation（§4.4）
- 这个 ablation 是否存在循环论证？（KL-derived masks 是由 coupling 发现的，用它们训练 BCE 是否能证明 "coupling 不重要"？）
- Soft-vs-hard confound：论文用 BCE+Gumbel (32.22) vs standard BCE (27.97) 排除 softness 效应，这个对照是否充分？
- C1 实验的因果推断力有多强？

### 3. Per-Layer KL 2D 分解（§4.5）
- "Signal type accounts for 98% of PPL gap" 这个归因是否方法论正确？
- Per-layer KL 的 train-inference mismatch（训练 mask 1 layer/step，inference 32 layers 同时）是否被充分讨论？
- Downstream 分解的定量方法是否 sound？

### 4. 实验方法论
- 训练仅用 WikiText-103，评估 WikiText-2：同分布问题
- Multi-seed 覆盖：哪些实验有 3-seed，哪些只有 seed 42？
- Actual sparsity mismatch（KL 28.5% vs TEAL 29.3% at 30% target）：是否影响公平对比？
- MSE baseline 在 50% 的 seed 失败（s123 PPL=15789）：是否充分报告？
- Compensation redundancy 的实验是否 conclusive？

### 5. 统计可靠性
- 3-seed evaluation 是否足够？领域标准是什么？
- OOD variance（CV 0.2% → 6.3%）的 implications
- Global allocation 30% MMLU σ=9.5pp 的极端 variance

请按以下结构输出审稿报告：
1. Summary（2-3 句）
2. Strengths（逐条）
3. Weaknesses（逐条，标注 Critical/Major/Minor + 置信度）
4. Questions（需要作者回答的）
5. Missing References
6. Overall Assessment（评分 + 置信度）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-22T09:35:18.671373+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-22T09:35:20.129042+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-22T09:35:20.531660+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-22T09:35:20.632558+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-22T09:35:30.885133+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 1071 · 2026-05-22T09:35:33.769712+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-22T09:35:34.122828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-22T09:35:39.350276+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Review Form Criteria

The main criteria for 
…[truncated 1182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8465
}
```

</details>

---


### Tool result

_source line 1074 · 2026-05-22T09:35:40.755667+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6985
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-22T09:35:40.756261+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6633
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-22T09:35:47.540793+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and descriptions. Include any guidance on what each score level means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and descriptions. Include any guidance on what each score level means."
  }
}
```

</details>

---


### Tool call

_source line 1077 · 2026-05-22T09:35:49.150489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1078 · 2026-05-22T09:35:50.458975+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool call

_source line 1079 · 2026-05-22T09:35:50.610888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-22T09:35:51.012820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1081 · 2026-05-22T09:35:51.315273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1082 · 2026-05-22T09:35:51.517374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 1083 · 2026-05-22T09:35:52.278932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1266
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-22T09:35:52.481321+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1166
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-22T09:35:54.389463+00:00_

# ARR Review Form: Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: top 2.5% papers"
- **4**: "Conference: could be accepted to an *ACL conference"
- **3**: "Findings: could be accepted to Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: has to be fully redone"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "Could easily reproduce the results"
- **4**: "Could mostly reproduce the results"
- **3**: "Could reproduce with some difficulty"
- **2**: "Would be hard pressed to reproduce the results"
- **1**: "Would not be able to reproduce the results"

## 6. **Datasets & Software**
Both scale 1-5:
…[truncated 107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6848
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-22T09:36:03.481184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1087 · 2026-05-22T09:36:03.886201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1088 · 2026-05-22T09:36:04.892972+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 1089 · 2026-05-22T09:36:04.893430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1090 · 2026-05-22T09:36:05.346822+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1460
}
```

</details>

---


### Tool call

_source line 1091 · 2026-05-22T09:36:05.548744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1092 · 2026-05-22T09:36:05.850945+00:00_

Image file is empty: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p7.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1093 · 2026-05-22T09:36:05.851375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1094 · 2026-05-22T09:36:05.952952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-22T09:36:06.507575+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-22T09:36:14.110471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1097 · 2026-05-22T09:36:14.413203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1098 · 2026-05-22T09:36:15.370117+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1259
}
```

</details>

---


### Tool result

_source line 1099 · 2026-05-22T09:36:15.370922+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1100 · 2026-05-22T09:36:15.371219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-22T09:36:15.471841+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Coupling alignment---optimizing through the output distribution---is the dominant design dimension for learned sparsity: signal type dominates PPL (98\% of the gap at 30\%), while coupling scope contributes 24--35\% on downstream tasks---a task-dependent spectrum where both dimensions carry independent value.
5	A predictor ($<$1\% of base) reduces TEAL's perplexity by 14.5\%, with KL-discovered masks (46--68\% divergent from magnitude) driving inference quality; however, downstream transfer is task- and scale-dependent. Future work: N:M sparsity and 70B+ scaling.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1102 · 2026-05-22T09:36:15.472376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-22T09:36:15.522818+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-22T09:36:22.653446+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-22T09:36:23.458812+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 30508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-22T09:36:23.459400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-22T09:36:24.464912+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity---a property exploitable for potential inference acceleration---but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\
…[truncated 2859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-22T09:36:24.816819+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-22T09:36:25.822134+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.7}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 217.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 91.3}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/rev
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-22T09:36:31.122351+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1111 · 2026-05-22T09:36:31.736585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1112 · 2026-05-22T09:36:32.440165+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1317
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-22T09:36:32.443351+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-22T09:36:32.443725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1115 · 2026-05-22T09:36:32.897230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1116 · 2026-05-22T09:36:33.404289+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 1117 · 2026-05-22T09:36:33.404753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1118 · 2026-05-22T09:36:33.963861+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1066
}
```

</details>

---


### Tool call

_source line 1119 · 2026-05-22T09:36:33.964359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1120 · 2026-05-22T09:36:34.468994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1064
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-22T09:36:34.821383+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-22T09:38:55.752488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-22T09:38:55.803168+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
16	Dhar et al.~\cite{dhar2025clustering} compress acti
…[truncated 5052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-22T09:42:11.716368+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**审查侧重：方法严谨性 + 实验设计**\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 系统性的实证研究揭示了 KL 蒸馏如何发现与 magnitude 显著不同的 mask 模式，但缺乏实际加速效果且下游知识任务一致性退化，限制了实际影响力。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有充分支撑，但 per-layer KL 分解存在训练-推理不匹配混淆变量，\"98% signal type\" 的归因方法论可商榷 |\n| Excitement | 3.0/5 | 对 sparsity prediction 社区有用的实证发现，但无实际加速且 MMLU/GSM8K 一致退化限制了影响力 |\n| Reproducibility | 4/5 | 详尽的超参数、多 seed 评估、完整附录；但 per-layer KL downstream 原始数值未在表格中呈现 |\n| Confidence | 4/5 | 仔细检查了关键技术点，对主要结论比较确信 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 无实际推理加速——方法增加 6.4% 延迟开销\n- 具体位置：Appendix A (Table 5), §5 Conclusion\n- 问题：论文动机是 contextual sparsity 的\"potential inference acceleration\"（§1），但 Table 5 显示完整 pipeline 增加 6.4% 延迟（126.78 vs 119.11 ms/fwd）。论文明确承认\"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support\"（Appendix A）。这意味着当前工作在实际部署层面不仅没有加速，反而变慢了。\n- 为什么影响接收：一篇关于 sparsity prediction 的论文如果无法展示任何加速效果，其实际贡献局限于 analytical insights。论文虽然诚实地 scope out 了这个问题，但 reviewer 和 AC 会质疑：如果 mask 无法转化为加速，发现更好的 mask 的价值有多大？\n- 建议修改方向：(a) 至少使用 Triton block-sparse 或 cuSPARSE 展示某个 sparsity level 的端到端加速；或 (b) 明确将论文重新定位为纯分析贡献（analysis paper），弱化 §1 中关于 acceleration 的动机表述。当前的定位介于两者之间，两头不讨好。\n- 置信度：高\n\n**N2** [critical] MMLU/GSM8K 在所有 scale 上一致退化——实用性存疑\n- 具体位置：Table 2 (30%: MMLU 40.7 vs TEAL 45.86, -5.2pp; GSM8K 7.5 vs 8.79), Table 13 (14B: GSM8K -20pp), Table 17 (Mistral: GSM8K -7.3pp), §Limitations\n- 问题：KL 蒸馏在 commonsense reasoning（ARC-c, WG, HellaSwag, PIQA）上一致优于 TEAL，但在 knowledge-intensive 任务（MMLU, GSM8K）上一致劣于 TEAL，且这种退化在 8B、7B、14B 三个 scale 上均成立。论文对此仅给出假设性解释：\"forward KL's mode-covering property may dilute task-specific knowledge pathways\"（§4.2），但未提供任何实验验证。\n- 为什么影响接收：这不是一个 edge case，而是系统性的 failure mode。MMLU 和 GSM8K 是 LLM 评估的核心任务。一个 sparsity prediction 方法如果系统性地损害了模型的知识保留和推理能力，其部署价值会受到严重质疑——即使 PPL 更低。\n- 建议修改方向：(a) 至少进行一组实验验证 mode-covering 假设（例如，分析 MMLU-relevant 层的 mask 差异）；(b) 设计 hybrid objective（对 knowledge-critical 层用 magnitude，其他层用 KL）并报告 MMLU 是否恢复；(c) 如果无法解决，需在 abstract/conclusion 更显著地标注此限制。\n- 置信度：高\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] Per-layer KL 的训练-推理不匹配严重混淆了 2D 分解的因果推断\n- 具体位置：§4.5 (Per-Layer KL), Table 4\n- 问题：Per-layer KL 的设计是\"mask one random layer per step and compute KL on the full model output\"。但在推理时，所有 32 层同时被 mask。这意味着 per-layer KL 的训练场景与推理场景存在根本性不匹配——训练时每步只有 1 层被稀疏化，其余 31 层保持 dense；推理时 32 层同时稀疏化。\n- 论文确实承认了这一点（§4.5 最后一句：\"A confound: training masks one layer per step while inference applies all 32; the downstream gap may partly reflect this train--inference shift.\"），但这个 confound 直接影响了论文最核心的定量结论之一。\n- 当 per-layer KL 在 30% 时下游任务表现不如 E2E KL，论文将差距归因于\"coupling scope contributes 30-35%\"。但这个差距的一部分（甚至大部分）可能来自训练-推理不匹配，而非缺乏 cross-layer coupling。\n- 50% 时 per-layer KL 退化到 34.85（vs E2E 11.92），退化幅度远超 30%。论文将此解释为\"coupling transitions from optional refinement to essential coordination as sparsity increases\"。但更 parsimonious 的解释是：50% sparsity 下 train-inference mismatch 更严重（训练时 1/32 层 50% sparse vs 推理时 32/32 层 50% sparse）。\n- 建议：(a) 训练 per-layer KL 时逐步增加每步 mask 的层数（如 1→4→16→32），观察性能曲线；(b) 至少讨论这个 confound 的量级估计。\n- 置信度：高\n\n**W2** [major] \"Signal type accounts for 98% of PPL gap\" 的归因方法论不严谨\n- 具体位置：§4.5\n- 问题：分解公式为 Total gap = (18.52 - 8.81) = 9.71; Signal type = (18.52 - 9.05) = 9.47 (97.5%); Coupling scope = (9.05 - 8.81) = 0.24 (2.5%)。这个分解隐含两个假设：(1) signal type 和 coupling scope 是正交的（无交互效应），(2) 分解是可加的。\n- 但实际上，\"signal type\" 在这里不是一个 clean 的单变量——从 MSE 切换到 KL，不仅改变了 loss target（中间层 vs 输出分布），也改变了 gradient flow 拓扑、优化景观、以及 loss surface 的曲率。论文在脚注中承认了这一点（\"this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled\"），但 98% 这个数字在正文中被当作主要结论反复引用（Abstract、§1、§4.5、§5），读者很容易将其理解为一个 clean 的因果归因。\n- 建议：(a) 在正文中更显著地注明这是 upper bound 估计而非精确归因；(b) 设计一个中间实验（如：per-layer KL on hidden states，即 per-layer scope + KL loss type on intermediate representations）来部分解耦 signal type 和 gradient flow topology。\n- 置信度：高\n\n**W3** [major] WikiText-103 训练 → WikiText-2 评估：同分布问题\n- 具体位置：§4.1 (Experimental Setup), Appendix D (OOD)\n- 问题：WikiText-103 和 WikiText-2 均来自 English Wikipedia 的 Good and Featured articles，本质上是同分布的不同 split。主表（Table 2）的所有 PPL 比较都基于这个 near-identical 分布，严格来说不能称为\"评估泛化能力\"。\n- C4 OOD 评估部分缓解了这个问题，但：(a) 30% 只有 2-seed（global）或 3-seed 但 CV=6.3%（uniform），远高于 in-domain 的 0.2%；(b) C4 PPL 的绝对值（16.03 global / 16.98 uniform）大幅偏离 dense baseline（9.21），说明 predictor 在 OOD 上的质量显著下降；(c) downstream robustness（Table 11）只报告了 seed 42，不是 multi-seed。\n- 建议：(a) C4 评估至少做 3-seed 一致性检查；(b) 在主表或 §4.2 中报告 C4 PPL 作为正式 metric，而非仅放在附录。\n- 置信度：高\n\n**W4** [major] C1 Target-Swap Ablation 的因果推断存在微妙的循环性\n- 具体位置：§4.4 (Table 3)\n- 问题：C1 的逻辑是：\"KL-derived masks 被提取 → BCE 在这些 masks 上训练 → BCE 匹配 KL → 结论：mask 质量驱动推理质量，而非 coupling 机制。\" 这个设计巧妙，但存在微妙问题：\n  - (a) KL-derived oracle masks 来自特定训练轨迹（optimizer state, data order, Gumbel noise），是一个 point estimate。虽然 3-seed 一致性（≤1.70pp）提供了部分鲁棒性证据，但 oracle mask 的质量仍然依赖于 KL 训练的具体收敛路径。Appendix P 承认了\"trajectory-dependent confounds\"但未量化。\n  - (b) 50% 只有 s42 一个 seed，且 s42 的 oracle 来自\"an earlier training run\"（Table 3 footnote），与 s123/s456 的 retrained oracles 条件不完全一致。\n  - (c) \"mask quality\" 本身是用 KL 定义的——KL-optimal masks 在 KL 评估下表现好，这有 tautological 成分。更有说服力的证据是 downstream 表现，但 C1 的 downstream 只在 30% 有 3-seed，50% 只有 s42。\n- 建议：(a) 50% C1 应补充 s123/s456 结果；(b) 报告 C1 downstream 的 full suite（包括 HellaSwag/PIQA）。\n- 置信度：中高\n\n**W5** [minor] MSE baseline 在 50% 的有效性存疑——实质上是 single-seed\n- 具体位置：Table 4, Appendix G\n- 问题：MSE 50% 的 s123 出现灾难性失败（PPL=15,789, 实际 sparsity 只有 5.1%）。论文在 Table 4 脚注标注了 $^\\S$，但主表只报告 s42 的 229.26。这意味着 MSE 在 50% 的对比本质上是 single-seed——这对一个用于支撑论文核心 claim 的 baseline 来说是不够的。\n- 此外，s123 的灾难性失败本身就是一个重要的负面结果（MSE 对初始化极其敏感），值得在正文中更显著地讨论，而非仅在附录中提及。\n- 建议：(a) 在 Table 4 中注明 MSE 50% 是 s42 only，或报告存活 seed 的均值；(b) 在正文 §4.5 中讨论 MSE 的初始化敏感性。\n- 置信度：高\n\n**W6** [minor] Actual sparsity mismatch (KL 28.5% vs TEAL 29.3% at 30% target) 对 downstream 对比的影响未量化\n- 具体位置：Table 2 footnote $^\\ddagger$, Appendix C, Appendix D\n- 问题：论文提供了 matched-sparsity PPL 对比（Appendix D: TEAL at 28.5% = 10.30 vs KL 8.81），但 downstream task 对比（Table 2: MMLU 40.7 vs 45.86）仍然是在不同 actual sparsity 下进行的。0.8pp 的 sparsity 差异在 PPL 上影响不大，但在 MMLU 这类对 capacity 敏感的任务上可能产生非对称影响——TEAL 比 KL 多保留 0.8pp 的神经元可能对 knowledge-intensive 任务更重要。\n- 建议：在 Appendix 中补充 TEAL at 28.5% actual sparsity 的 downstream 数字以排除这个 confound。\n- 置信度：中\n\n---\n\n## 小问题（不影响接收）\n\n1. **Multi-seed 覆盖不一致**：Table 2 中 KL 30%/50% 有 3-seed，但 TEAL 和 BCE 的部分配置只有 seed 42（尤其是 downstream tasks）。虽然 TEAL 是确定性的（不需要 multi-seed），但 BCE 30% global 只报告了单次结果。建议统一标准。\n\n2. **Per-layer KL downstream 数值缺失**：§4.5 引用了 per-layer KL 的 downstream 分解百分比（30.5% ARC-c, 35.2% WG, 24% MMLU 等），但 per-layer KL 的 downstream 原始数值既不在主表也不在附录表格中（仅在文字中隐含）。读者无法独立验证这些百分比。建议增加一个包含 per-layer KL downstream 数值的表格。\n\n3. **§3.6 梯度分析是定性的**：论文将 §3.6 定位为\"suggestive\"（合理），但正文和 abstract 中引用时有时暗示更强的因果关系。建议统一用语。\n\n4. **Forward KL vs Reverse KL 论证**：§3.4 中关于 mode-covering 对 sparsity prediction 重要性的论证（\"false negatives cascade... false positives merely waste capacity\"）是直觉性的但未经形式化证明。这在实证论文中可以接受，但需注意 §4.5 的 reverse KL 结果（30% 3-seed）显示 reverse KL 在 commonsense 任务上也优于 TEAL，削弱了 mode-seeking 的 \"missing critical neurons\" 论证。\n\n5. **Compensation redundancy**：仅在 30%（s42, s456）和 50%（s42）测试。如果声称 \"redundant at both tested sparsity levels\"（§1 contributions），至少应在两个 sparsity level 各有 2+ seed。\n\n---\n\n## 需要作者回答的问题\n\n**Q1**：Per-layer KL 在 30% 和 50% 的 downstream 原始数值是多少？请提供 ARC-c, WG, MMLU, GSM8K, HellaSwag, PIQA 的具体数字和 seed 信息（目前只有分解百分比但无法 verify）。\n\n**Q2**：Per-layer KL 训练时如果 mask K>1 层/步（如 K=8 或 K=32），性能如何变化？这能帮助量化训练-推理不匹配的贡献 vs coupling scope 的贡献。\n\n**Q3**：MMLU/GSM8K 退化是否与特定层的 mask divergence 相关？例如，late layers（论文显示 Jaccard divergence 最高的区域）是否恰好是存储 factual knowledge 的层？这可以通过比较 KL/magnitude masks 在 MMLU-relevant prompts 上的 per-layer divergence 来初步检验。\n\n**Q4**：MSE s123 在 50% 的灾难性失败——是 Lagrangian controller 未收敛还是 MSE 本身的优化景观问题？是否有 training curve 可以辅助诊断？\n\n**Q5**：如果用更多样化的训练数据（如 C4 或 RedPajama 的子集替代 WikiText-103），MMLU regression 是否会缓解？\n\n**Q6**：论文使用 $T=1$（无温度缩放）进行 KL 蒸馏，引用了 Hinton et al., 2015。是否尝试过 $T>1$？在标准知识蒸馏中，$T=2$-$4$ 通常优于 $T=1$。\n\n---\n\n## Missing References\n\n未发现关键缺失引用。Related work 覆盖了 training-free sparsity、predictor-based methods、static correction、activation engineering、weight pruning/distillation 和 MoE routing 等主要方向，引用充分。\n\n可考虑补充：\n- Alizadeh et al., 2024 (\"LLM in a Flash\") — 关于 flash memory 上的 sparse inference 部署，与本文的\"无加速\"讨论互补。\n- Wei et al., 2023 (Outlier Suppression+) — activation outlier 分布对 sparsity prediction 的影响。\n\n---\n\n## 主要优势\n\n1. **系统性实证设计**：5 种 loss function（Forward KL, Reverse KL, JSD, BCE, MSE）的完整对比，配合 Gumbel/STE relaxation 的交叉消融，构成了目前该方向最全面的实证研究。\n\n2. **C1 Target-Swap Ablation 设计巧妙**：通过将 KL-derived masks 作为 BCE 训练目标，解耦了\"发现 vs 利用\"，是一个有创意的因果推断实验。虽然存在 W4 所述的微妙问题，但整体设计思路值得肯定。\n\n3. **诚实的 limitation 报告**：论文没有回避负面结果（MMLU/GSM8K 退化、无加速、OOD variance、MSE seed 失败），均在正文或附录中明确报告。这种透明度值得赞赏。\n\n4. **多架构/多 scale 初步验证**：Mistral-7B（3-seed, Table 16-17）和 Qwen-2.5-14B（Table 13）的跨架构评估，虽然不是深入分析，但增强了结论的初步泛化性。\n\n5. **实用的分类框架**：Correction Granularity × Training Signal Coupling 的 2D taxonomy（Table 1）为后续工作提供了有用的概念工具，尽管部分 cell 为空。\n\n6. **详尽的附录**：18 页中有 10 页附录，涵盖 bottleneck sensitivity、temperature schedule、training convergence、penalty dynamics、OOD evaluation、mask visualization 等，可重现性高。\n\n---\n\n## 总结\n\n论文是一项扎实的实证分析，核心发现（KL 蒸馏发现与 magnitude 显著不同的 mask 模式，signal type 对 PPL 的贡献远大于 coupling scope）对 sparsity prediction 社区有参考价值。C1 ablation 和 5-way loss comparison 是主要亮点。\n\n但三个关键短板限制了论文的 impact：(1) 无实际推理加速（反而增加 6.4% 延迟）；(2) knowledge-intensive 任务一致退化，且缺乏解释；(3) per-layer KL 分解的 train-inference mismatch 混淆了论文最核心的定量结论。这些问题使论文更适合 Findings 而非主会议。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n**审查侧重：方法严谨性 + 实验设计**\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 系统性的实证研究揭示了 KL 蒸馏如何发现与 magnitude 显著不同的 mask 模式，但缺乏实际加速效果且下游知识任务一致性退化，限制了实际影响力。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有充分支撑，但 per-layer KL 分解存在训练-推理不匹配混淆变量，\"98% signal type\" 的归因方法论可商榷 |\n| Excitement | 3.0/5 | 对 sparsity prediction 社区有用的实证发现，但无实际加速且 MMLU/GSM8K 一致退化限制了影响力 |\n| Reproducibility | 4/5 | 详尽的超参数、多 seed 评估、完整附录；但 per-layer KL downstream 原始数值未在表格中呈现 |\n| Confidence | 4/5 | 仔细检查了关键技术点，对主要结论比较确信 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 无实际推理加速——方法增加 6.4% 延迟开销\n- 具体位置：Appendix A (Table 5), §5 Conclusion\n- 问题：论文动机是 contextual sparsity 的\"potential inference acceleration\"（§1），但 Table 5 显示完整 pipeline 增加 6.4% 延迟（126.78 vs 119.11 ms/fwd）。论文明确承认\"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support\"（Appendix A）。这意味着当前工作在实际部署层面不仅没有加速，反而变慢了。\n- 为什么影响接收：一篇关于 sparsity prediction 的论文如果无法展示任何加速效果，其实际贡献局限于 analytical insights。论文虽然诚实地 scope out 了这个问题，但 reviewer 和 AC 会质疑：如果 mask 无法转化为加速，发现更好的 mask 的价值有多大？\n- 建议修改方向：(a) 至少使用 Triton block-sparse 或 cuSPARSE 展示某个 sparsity level 的端到端加速；或 (b) 明确将论文重新定位为纯分析贡献（analysis paper），弱化 §1 中关于 acceleration 的动机表述。当前的定位介于两者之间，两头不讨好。\n- 置信度：高\n\n**N2** [critical] MMLU/GSM8K 在所有 scale 上一致退化——实用性存疑\n- 具体位置：Table 2 (30%: MMLU 40.7 vs TEAL 45.86, -5.2pp; GSM8K 7.5 vs 8.79), Table 13 (14B: GSM8K -20pp), Table 17 (Mistral: GSM8K -7.3pp), §Limitations\n- 问题：KL 蒸馏在 commonsense reasoning（ARC-c, WG, HellaSwag, PIQA）上一致优于 TEAL，但在 knowledge-intensive 任务（MMLU, GSM8K）上一致劣于 TEAL，且这种退化在 8B、7B、14B 三个 scale 上均成立。论文对此仅给出假设性解释：\"forward KL's mode-covering property may dilute task-specific knowledge pathways\"（§4.2），但未提供任何实验验证。\n- 为什么影响接收：这不是一个 edge case，而是系统性的 failure mode。MMLU 和 GSM8K 是 LLM 评估的核心任务。一个 sparsity prediction 方法如果系统性地损害了模型的知识保留和推理能力，其部署价值会受到严重质疑——即使 PPL 更低。\n- 建议修改方向：(a) 至少进行一组实验验证 mode-covering 假设（例如，分析 MMLU-relevant 层的 mask 差异）；(b) 设计 hybrid objective（对 knowledge-critical 层用 magnitude，其他层用 KL）并报告 MMLU 是否恢复；(c) 如果无法解决，需在 abstract/conclusion 更显著地标注此限制。\n- 置信度：高\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] Per-layer KL 的训练-推理不匹配严重混淆了 2D 分解的因果推断\n- 具体位置：§4.5 (Per-Layer KL), Table 4\n- 问题：Per-layer KL 的设计是\"mask one random layer per step and compute KL on the full model output\"。但在推理时，所有 32 层同时被 mask。这意味着 per-layer KL 的训练场景与推理场景存在根本性不匹配——训练时每步只有 1 层被稀疏化，其余 31 层保持 dense；推理时 32 层同时稀疏化。\n- 论文确实承认了这一点（§4.5 最后一句：\"A confound: training masks one layer per step while inference applies all 32; the downstream gap may partly reflect this train--inference shift.\"），但这个 confound 直接影响了论文最核心的定量结论之一。\n- 当 per-layer KL 在 30% 时下游任务表现不如 E2E KL，论文将差距归因于\"coupling scope contributes 30-35%\"。但这个差距的一部分（甚至大部分）可能来自训练-推理不匹配，而非缺乏 cross-layer coupling。\n- 50% 时 per-layer KL 退化到 34.85（vs E2E 11.92），退化幅度远超 30%。论文将此解释为\"coupling transitions from optional refinement to essential coordination as sparsity increases\"。但更 parsimonious 的解释是：50% sparsity 下 train-inference mismatch 更严重（训练时 1/32 层 50% sparse vs 推理时 32/32 层 50% sparse）。\n- 建议：(a) 训练 per-layer KL 时逐步增加每步 mask 的层数（如 1→4→16→32），观察性能曲线；(b) 至少讨论这个 confound 的量级估计。\n- 置信度：高\n\n**W2** [major] \"Signal type accounts for 98% of PPL gap\" 的归因方法论不严谨\n- 具体位置：§4.5\n- 问题：分解公式为 Total gap = (18.52 - 8.81) = 9.71; Signal type = (18.52 - 9.05) = 9.47 (97.5%); Coupling scope = (9.05 - 8.81) = 0.24 (2.5%)。这个分解隐含两个假设：(1) signal type 和 coupling scope 是正交的（无交互效应），(2) 分解是可加的。\n- 但实际上，\"signal type\" 在这里不是一个 clean 的单变量——从 MSE 切换到 KL，不仅改变了 loss target（中间层 vs 输出分布），也改变了 gradient flow 拓扑、优化景观、以及 loss surface 的曲率。论文在脚注中承认了这一点（\"this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled\"），但 98% 这个数字在正文中被当作主要结论反复引用（Abstract、§1、§4.5、§5），读者很容易将其理解为一个 clean 的因果归因。\n- 建议：(a) 在正文中更显著地注明这是 upper bound 估计而非精确归因；(b) 设计一个中间实验（如：per-layer KL on hidden states，即 per-layer scope + KL loss type on intermediate representations）来部分解耦 signal type 和 gradient flow topology。\n- 置信度：高\n\n**W3** [major] WikiText-103 训练 → WikiText-2 评估：同分布问题\n- 具体位置：§4.1 (Experimental Setup), Appendix D (OOD)\n- 问题：WikiText-103 和 WikiText-2 均来自 English Wikipedia 的 Good and Featured articles，本质上是同分布的不同 split。主表（Table 2）的所有 PPL 比较都基于这个 near-identical 分布，严格来说不能称为\"评估泛化能力\"。\n- C4 OOD 评估部分缓解了这个问题，但：(a) 30% 只有 2-seed（global）或 3-seed 但 CV=6.3%（uniform），远高于 in-domain 的 0.2%；(b) C4 PPL 的绝对值（16.03 global / 16.98 uniform）大幅偏离 dense baseline（9.21），说明 predictor 在 OOD 上的质量显著下降；(c) downstream robustness（Table 11）只报告了 seed 42，不是 multi-seed。\n- 建议：(a) C4 评估至少做 3-seed 一致性检查；(b) 在主表或 §4.2 中报告 C4 PPL 作为正式 metric，而非仅放在附录。\n- 置信度：高\n\n**W4** [major] C1 Target-Swap Ablation 的因果推断存在微妙的循环性\n- 具体位置：§4.4 (Table 3)\n- 问题：C1 的逻辑是：\"KL-derived masks 被提取 → BCE 在这些 masks 上训练 → BCE 匹配 KL → 结论：mask 质量驱动推理质量，而非 coupling 机制。\" 这个设计巧妙，但存在微妙问题：\n  - (a) KL-derived oracle masks 来自特定训练轨迹（optimizer state, data order, Gumbel noise），是一个 point estimate。虽然 3-seed 一致性（≤1.70pp）提供了部分鲁棒性证据，但 oracle mask 的质量仍然依赖于 KL 训练的具体收敛路径。Appendix P 承认了\"trajectory-dependent confounds\"但未量化。\n  - (b) 50% 只有 s42 一个 seed，且 s42 的 oracle 来自\"an earlier training run\"（Table 3 footnote），与 s123/s456 的 retrained oracles 条件不完全一致。\n  - (c) \"mask quality\" 本身是用 KL 定义的——KL-optimal masks 在 KL 评估下表现好，这有 tautological 成分。更有说服力的证据是 downstream 表现，但 C1 的 downstream 只在 30% 有 3-seed，50% 只有 s42。\n- 建议：(a) 50% C1 应补充 s123/s456 结果；(b) 报告 C1 downstream 的 full suite（包括 HellaSwag/PIQA）。\n- 置信度：中高\n\n**W5** [minor] MSE baseline 在 50% 的有效性存疑——实质上是 single-seed\n- 具体位置：Table 4, Appendix G\n- 问题：MSE 50% 的 s123 出现灾难性失败（PPL=15,789, 实际 sparsity 只有 5.1%）。论文在 Table 4 脚注标注了 $^\\S$，但主表只报告 s42 的 229.26。这意味着 MSE 在 50% 的对比本质上是 single-seed——这对一个用于支撑论文核心 claim 的 baseline 来说是不够的。\n- 此外，s123 的灾难性失败本身就是一个重要的负面结果（MSE 对初始化极其敏感），值得在正文中更显著地讨论，而非仅在附录中提及。\n- 建议：(a) 在 Table 4 中注明 MSE 50% 是 s42 only，或报告存活 seed 的均值；(b) 在正文 §4.5 中讨论 MSE 的初始化敏感性。\n- 置信度：高\n\n**W6** [minor] Actual sparsity mismatch (KL 28.5% vs TEAL 29.3% at 30% target) 对 downstream 对比的影响未量化\n- 具体位置：Table 2 footnote $^\\ddagger$, Appendix C, Appendix D\n- 问题：论文提供了 matched-sparsity PPL 对比（Appendix D: TEAL at 28.5% = 10.30 vs KL 8.81），但 downstream task 对比（Table 2: MMLU 40.7 vs 45.86）仍然是在不同 actual sparsity 下进行的。0.8pp 的 sparsity 差异在 PPL 上影响不大，但在 MMLU 这类对 capacity 敏感的任务上可能产生非对称影响——TEAL 比 KL 多保留 0.8pp 的神经元可能对 knowledge-intensive 任务更重要。\n- 建议：在 Appendix 中补充 TEAL at 28.5% actual sparsity 的 downstream 数字以排除这个 confound。\n- 置信度：中\n\n---\n\n## 小问题（不影响接收）\n\n1. **Multi-seed 覆盖不一致**：Table 2 中 KL 30%/50% 有 3-seed，但 TEAL 和 BCE 的部分配置只有 seed 42（尤其是 downstream tasks）。虽然 TEAL 是确定性的（不需要 multi-seed），但 BCE 30% global 只报告了单次结果。建议统一标准。\n\n2. **Per-layer KL downstream 数值缺失**：§4.5 引用了 per-layer KL 的 downstream 分解百分比（30.5% ARC-c, 35.2% WG, 24% MMLU 等），但 per-layer KL 的 downstream 原始数值既不在主表也不在附录表格中（仅在文字中隐含）。读者无法独立验证这些百分比。建议增加一个包含 per-layer KL downstream 数值的表格。\n\n3. **§3.6 梯度分析是定性的**：论文将 §3.6 定位为\"suggestive\"（合理），但正文和 abstract 中引用时有时暗示更强的因果关系。建议统一用语。\n\n4. **Forward KL vs Reverse KL 论证**：§3.4 中关于 mode-covering 对 sparsity prediction 重要性的论证（\"false negatives cascade... false positives merely waste capacity\"）是直觉性的但未经形式化证明。这在实证论文中可以接受，但需注意 §4.5 的 reverse KL 结果（30% 3-seed）显示 reverse KL 在 commonsense 任务上也优于 TEAL，削弱了 mode-seeking 的 \"missing critical neurons\" 论证。\n\n5. **Compensation redundancy**：仅在 30%（s42, s456）和 50%（s42）测试。如果声称 \"redundant at both tested sparsity levels\"（§1 contributions），至少应在两个 sparsity level 各有 2+ seed。\n\n---\n\n## 需要作者回答的问题\n\n**Q1**：Per-layer KL 在 30% 和 50% 的 downstream 原始数值是多少？请提供 ARC-c, WG, MMLU, GSM8K, HellaSwag, PIQA 的具体数字和 seed 信息（目前只有分解百分比但无法 verify）。\n\n**Q2**：Per-layer KL 训练时如果 mask K>1 层/步（如 K=8 或 K=32），性能如何变化？这能帮助量化训练-推理不匹配的贡献 vs coupling scope 的贡献。\n\n**Q3**：MMLU/GSM8K 退化是否与特定层的 mask divergence 相关？例如，late layers（论文显示 Jaccard divergence 最高的区域）是否恰好是存储 factual knowledge 的层？这可以通过比较 KL/magnitude masks 在 MMLU-relevant prompts 上的 per-layer divergence 来初步检验。\n\n**Q4**：MSE s123 在 50% 的灾难性失败——是 Lagrangian controller 未收敛还是 MSE 本身的优化景观问题？是否有 training curve 可以辅助诊断？\n\n**Q5**：如果用更多样化的训练数据（如 C4 或 RedPajama 的子集替代 WikiText-103），MMLU regression 是否会缓解？\n\n**Q6**：论文使用 $T=1$（无温度缩放）进行 KL 蒸馏，引用了 Hinton et al., 2015。是否尝试过 $T>1$？在标准知识蒸馏中，$T=2$-$4$ 通常优于 $T=1$。\n\n---\n\n## Missing References\n\n未发现关键缺失引用。Related work 覆盖了 training-free sparsity、predictor-based methods、static correction、activation engineering、weight pruning/distillation 和 MoE routing 等主要方向，引用充分。\n\n可考虑补充：\n- Alizadeh et al., 2024 (\"LLM in a Flash\") — 关于 flash memory 上的 sparse inference 部署，与本文的\"无加速\"讨论互补。\n- Wei et al., 2023 (Outlier Suppression+) — activation outlier 分布对 sparsity prediction 的影响。\n\n---\n\n## 主要优势\n\n1. **系统性实证设计**：5 种 loss function（Forward KL, Reverse KL, JSD, BCE, MSE）的完整对比，配合 Gumbel/STE relaxation 的交叉消融，构成了目前该方向最全面的实证研究。\n\n2. **C1 Target-Swap Ablation 设计巧妙**：通过将 KL-derived masks 作为 BCE 训练目标，解耦了\"发现 vs 利用\"，是一个有创意的因果推断实验。虽然存在 W4 所述的微妙问题，但整体设计思路值得肯定。\n\n3. **诚实的 limitation 报告**：论文没有回避负面结果（MMLU/GSM8K 退化、无加速、OOD variance、MSE seed 失败），均在正文或附录中明确报告。这种透明度值得赞赏。\n\n4. **多架构/多 scale 初步验证**：Mistral-7B（3-seed, Table 16-17）和 Qwen-2.5-14B（Table 13）的跨架构评估，虽然不是深入分析，但增强了结论的初步泛化性。\n\n5. **实用的分类框架**：Correction Granularity × Training Signal Coupling 的 2D taxonomy（Table 1）为后续工作提供了有用的概念工具，尽管部分 cell 为空。\n\n6. **详尽的附录**：18 页中有 10 页附录，涵盖 bottleneck sensitivity、temperature schedule、training convergence、penalty dynamics、OOD evaluation、mask visualization 等，可重现性高。\n\n---\n\n## 总结\n\n论文是一项扎实的实证分析，核心发现（KL 蒸馏发现与 magnitude 显著不同的 mask 模式，signal type 对 PPL 的贡献远大于 coupling scope）对 sparsity prediction 社区有参考价值。C1 ablation 和 5-way loss comparison 是主要亮点。\n\n但三个关键短板限制了论文的 impact：(1) 无实际推理加速（反而增加 6.4% 延迟）；(2) knowledge-intensive 任务一致退化，且缺乏解释；(3) per-layer KL 分解的 train-inference mismatch 混淆了论文最核心的定量结论。这些问题使论文更适合 Findings 而非主会议。\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-22T09:42:16.096144+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4379
}
```

</details>

---


### Assistant

_source line 1126 · 2026-05-22T09:42:28.879096+00:00_

审稿报告已提交给 Review Director。

**审稿结论概要：**

- **Overall: 3.0 (Findings)**，Soundness 3.5，Excitement 3.0，Confidence 4/5
- **2 个 Critical 问题**：无实际推理加速（+6.4% overhead）；MMLU/GSM8K 在所有 scale 上一致退化
- **6 个 Major/Minor 问题**：per-layer KL 训练-推理不匹配混淆了 2D 分解；"98% signal type" 归因方法论不严谨；WikiText 同分布评估；C1 ablation 50% 仅 single-seed；MSE 50% 实质 single-seed；sparsity mismatch 对 downstream 影响未量化
- **6 个 Questions**：per-layer KL downstream 原始数值、K>1 层训练、MMLU 退化与层级 mask divergence 的关系、MSE s123 失败诊断、训练数据多样性影响、KL 温度缩放
- **主要优势**：系统性 5-way loss 对比、巧妙的 C1 ablation、诚实的 limitation 报告、详尽附录

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 35

## Round 35

4 recorded events


### User

_source line 1127 · 2026-05-22T09:43:09.197601+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 2 审稿报告

**Overall**: 3.0 (Findings), Soundness 3/5, Excitement 2/5, Confidence 4/5

## Summary
本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor，使用 Gumbel-Sigmoid relaxation + frozen weights + learnable masks。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），并通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type 和 coupling scope 两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证。论文自我定位为 "primarily an empirical study"。

## Strengths
S1. 分析框架设计有新意（C1 + per-layer KL decomposition）
S2. 实验覆盖相对全面（5 loss configs, 3-seed, sensitivity sweeps, OOD, 跨架构）
S3. 诚实的自我定位（明确声明非 new architecture/algorithm）
S4. Related Work 非常全面（8/10）
S5. Compensation redundancy 是有实际价值的发现

## Must-Fix 问题

**N1** [Critical, Confidence 4/5] **与 MaskLLM 的新颖性区分不足**
核心配方——frozen weights + learnable masks + forward KL + Gumbel relaxation——与 MaskLLM (NeurIPS 2024 Spotlight) 完全一致。三点区分（sparsity type / mask generation / allocation）都是 application-level 差异而非 methodological innovation。论文自称贡献在 analysis framework，但 target-swap ablation 是实验设计而非方法，2D taxonomy 是分类表而非新框架。"output-distribution loss 比 per-neuron loss 好" 的 surprise factor 有限。

**N2** [Critical, Confidence 5/5] **无实际推理加速，实用价值存疑**
30% unstructured sparsity + 6.4% latency overhead = 净减速。对比 Polar Sparsity (NeurIPS 2025) 2.2× speedup, SVD-CSP 1.8× speedup。"prediction quality" 改进不能转化为实际收益则只是学术练习。

**N3** [Critical, Confidence 4/5] **知识密集型任务系统性退步未解释**
KL 在 MMLU/GSM8K 上跨三个架构一致劣于 TEAL（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp）。仅有假设性解释（"mode-covering may dilute knowledge pathways"），未验证。如果 coupling alignment 真的 dominant，为什么 knowledge tasks 上反而更差？

## Should-Fix 问题

**W1** [Major, Confidence 3/5] **C1 ablation 存在 confound**
(a) s42 oracle 来自 earlier training run（trajectory dependence）；(b) oracle masks 编码了 KL specific trajectory；(c) soft-vs-hard confound（BCE+Gumbel 32.22 vs standard BCE 27.97 说明 representation form 也 matters）。

**W2** [Major, Confidence 4/5] **"Coupling alignment dominance" 可能是 loss quality 而非 coupling 机制**
Per-layer KL 达 98% PPL gap → cross-layer coupling 几乎不重要 → 真正重要的是 signal type（output distribution vs intermediate activations）。Conclusion 中 "coupling alignment" conflates 了 signal type 和 coupling。

**W3** [Major, Confidence 4/5] **30% sparsity ceiling 过低**
即使在 30%，MMLU 65.27→40.7（-24.6pp），GSM8K 48.75→7.5（-41pp）。对比 Polar Sparsity 50% sparsity < 1% accuracy drop。

**W4** [Minor] **术语过度创造**
"coupling alignment ranking"、"signal type × coupling scope" 包装了相对简单的概念。

**W5** [Minor] **Batch size 限制未讨论**
Polar Sparsity 已证明 contextual sparsity 在 batched inference 下效果显著下降。

## Questions
Q1. Per-layer KL 达 98% PPL gap，为什么 "coupling" 是核心 selling point？
Q2. MaskLLM 在 activation sparsity 场景下表现如何？
Q3. 14B GSM8K -20pp 是否随 scale 增长？
Q4. C1 s42 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？
Q5. Abstract "14.5% PPL reduction" 是 matched sparsity 数字，为什么不用 nominal 18.6%？

## Missing References
Related work 已非常全面（8/10）。可补充 COTS (Zhang et al., 2025) 和 LazyLLM (Fu et al., 2024)。

## 小问题
- Abstract "universally use BCE" 不准确（ShadowLLM 用 MSE）
- Table 2 actual sparsity 差异应更显著标注
- MSE s123 catastrophic failure 应在主文更显著提及

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-22T09:45:10.318166+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: 与 MaskLLM 的新颖性区分不足**\n\nReviewer 2 称核心配方与 MaskLLM (NeurIPS 2024) \"完全一致\"，三点区分只是 \"application-level 差异\"。我认为这个批评过于简化。\n\n(1) **Mask generation 的差异不是 application-level 的**。MaskLLM 的 masks 是直接可学习参数（one per weight group），训练完成后固定。本文的 masks 由 predictor network 在推理时从 hidden states 生成，每个 token 不同。这是 architecture-level 的差异——前者是参数优化问题，后者是函数逼近问题。predictor 需要从 $\\mathbf{x}^{(\\ell)}$ 泛化到 unseen inputs（§3.2），MaskLLM 不需要。\n\n(2) **Global top-k allocation 创造了 MaskLLM 不存在的跨层依赖**。MaskLLM 在 fixed N:M groups 内优化（局部独立），本文的 masks 在全模型 global top-k 下竞争（§3.1, Eq. 2）——一个层的 mask 质量直接影响其他层获得的 neuron budget（Appendix E, Figure 4 per-layer retention 分析）。这是 per-layer KL 分解（§4.5）和 allocation strategy 分析（§4.6, Table 14）存在意义的前提。\n\n(3) 不过，我同意 Reviewer 2 关于 **analysis contribution 的定位需要更精确**。C1 target-swap ablation 确实是实验设计而非方法论创新，2D taxonomy 是分类而非理论框架。但 \"实验设计创新\" 在 empirical study 中是合理的贡献形式——论文明确自我定位为 \"primarily an empirical study\"（§1 倒数第二段）。\n\n**总结**：方法层面的新颖性确实有限（recipe-level overlap 真实存在），但三点差异中至少两点（predictor network、global allocation）具有非平凡的技术含义。R2 的批评在 \"surprise factor 有限\" 这一点上是成立的，但 \"完全一致\" 的措辞过强。\n\n---\n\n**[AGREE] R2-N2: 无实际推理加速**\n\n与我的 R1-N1 一致。论文 Appendix A (Table 5) 明确显示 +6.4% latency overhead。这是一个 critical limitation。不过我要补充一个 nuance：Reviewer 2 引用 Polar Sparsity (2.2× speedup) 和 SVD-CSP (1.8× speedup) 作为对比，但需注意 (a) Polar Sparsity 是 attention head sparsity（结构化），与本文的 FFN neuron sparsity（非结构化）不是同一类问题；(b) SVD-CSP 是 predictor compression 方法，与本文的 training objective 研究不直接可比。直接对比可能误导读者。但核心批评——无加速的 sparsity prediction 实用价值有限——完全成立。\n\n---\n\n**[AGREE] R2-N3: 知识密集型任务系统性退步**\n\n与我的 R1-N2 一致。Table 2（8B MMLU -5.2pp）、Table 13（14B MMLU -8.1pp, GSM8K -20pp）、Table 17（Mistral MMLU tied, GSM8K -7.3pp）构成了跨 scale 的一致证据。论文仅提供假设性解释（§4.2 \"mode-covering may dilute task-specific knowledge pathways\"），未进行任何验证实验（例如 per-layer mask divergence analysis on MMLU-relevant inputs）。Reviewer 2 提出的反问——\"如果 coupling alignment 真的 dominant，为什么 knowledge tasks 反而更差\"——有力地指出了论文 narrative 的内在张力。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: C1 ablation confounds**\n\n与我的 R1-W4 一致。具体补充：\n\n(a) **s42 oracle provenance**: Table 3 footnote 明确标注 s42 oracle 来自 \"earlier training run\"，而 s123/s456 使用 \"matched retrained oracles\"。s42 的 0.65pp PPL gap（9.45 vs 8.80）大于 retrained seeds 的 ≤0.02pp gap（如 s123: 8.84 vs 8.83），说明 oracle provenance 确实影响结论。\n\n(b) **soft-vs-hard confound**: BCE+Gumbel (32.22) 实际上比 standard BCE (27.97) 更差，这恰恰说明 Gumbel relaxation 与 BCE 的组合是有害的。但论文用此证明 \"softness alone does not explain KL's advantage\"（§4.4）——这个推理是正确的（Gumbel 对 BCE 有害但对 KL 有利，说明 loss function 才是关键变量），但需要更清晰地表述。\n\n(c) Reviewer 2 的 \"(b) oracle masks 编码了 KL specific trajectory\" 与 Appendix P 的承认一致。我认为 3-seed 一致性（≤1.70pp at 30%）提供了 partial 但非 conclusive 的鲁棒性证据。\n\n---\n\n**[AGREE] R2-W2: \"Coupling alignment\" 术语混淆 signal type 和 coupling**\n\n这是一个比我原始审稿中提出的更精确的批评。论文 §5 Conclusion: \"Coupling alignment---optimizing through the output distribution---is the dominant design dimension\"——但论文自己的 per-layer KL 实验（§4.5）显示 coupling scope 只贡献 PPL gap 的 2.5%！\"Coupling alignment\" 这个术语暗示 cross-layer coupling 是核心，但数据说明是 signal type（output distribution vs intermediate representation）才是核心。\n\nReviewer 2 正确指出了这个 conflation：如果 per-layer KL（无 cross-layer coupling 但有 output-distribution signal）已经达到 E2E KL 98% 的效果，那么 \"coupling\" 不应该是 selling point。论文应该用 \"output-distribution alignment\" 而非 \"coupling alignment\" 作为核心术语。\n\n---\n\n**[REBUT] R2-W3: 30% sparsity ceiling 过低（对比 Polar Sparsity 50% < 1% drop）**\n\n这个对比不公平，原因有三：\n\n(1) **Sparsity 类型不同**。Polar Sparsity 是 attention head sparsity（结构化、粗粒度），本文是 FFN neuron sparsity（非结构化、细粒度）。两者的 capacity-quality tradeoff 完全不同。移除一个 attention head 与移除单个 FFN neuron 的影响不可直接对比。\n\n(2) **模型基线不同**。Polar Sparsity 的 \"< 1% drop\" 通常报告在特定 benchmark 上的 best-case scenario。本文的 MMLU 65.27→40.7 确实是大幅退化，但这是 FFN activation sparsity 的 *所有* 方法都面临的问题——TEAL 也只有 45.86（-19.4pp），BCE 更差（36.3）。这是问题的固有难度，不是本文方法的特有缺陷。\n\n(3) **Dense baseline 的 capacity utilization 不同**。LLaMA-3.1-8B 在 MMLU 上只有 65.27%（远非完美），说明 FFN 的 capacity 已被高度利用。移除 30% 的 FFN neurons 必然导致显著退化。\n\n我同意 Reviewer 2 指出了 practical utility 的问题，但用 Polar Sparsity 的数字直接对比来论证 \"30% ceiling 过低\" 是不恰当的。\n\n---\n\n**[AGREE] R2-W4: 术语过度创造**\n\n同意这是一个 minor 但 valid 的风格问题。\"coupling alignment ranking\" 本质上就是 \"loss function comparison\"，\"signal type × coupling scope\" 就是 \"loss target × optimization scope\"。过度包装简单概念确实增加了阅读负担。但这不影响技术正确性。\n\n---\n\n**[AGREE] R2-W5: Batch size 限制未讨论**\n\n这是一个被论文完全忽略的实际问题。Per-token contextual sparsity 在 batched inference 下会遇到 \"mask union\" 问题——batch 内不同 token 需要不同 neurons，实际保留的 neuron set 可能接近 dense。Polar Sparsity（§2, Related Work 中已引用）的经验表明这个问题严重。论文应在 Limitations 中讨论 batch size 对 effective sparsity 的影响。\n\n---\n\n### Questions\n\n**R2-Q1: Per-layer KL 达 98% PPL gap，为什么 coupling 是核心 selling point？**\n\n[AGREE] 这与 W2 一致。论文的数据不支持 \"coupling\" 作为核心 selling point。如果将 framing 改为 \"output-distribution signal type 是 dominant dimension\"（而非 \"coupling alignment\"），narrative 会更诚实。\n\n**R2-Q2: MaskLLM 在 activation sparsity 场景下表现如何？**\n\n[AGREE] 这是一个合理的 baseline 请求。论文声称与 MaskLLM 有本质差异（§2），但未提供 MaskLLM 在 activation sparsity 上的实验。即使 MaskLLM 的 static N:M design 无法直接做 per-token activation sparsity，也应讨论为什么不能适配以及性能预期。\n\n**R2-Q3: 14B GSM8K -20pp 是否随 scale 增长？**\n\n[AGREE] 只有两个 scale（8B, 14B）无法确定趋势。但 8B GSM8K -1.3pp（7.5 vs 8.79）到 14B GSM8K -20pp 的跳跃确实令人担忧（Table 2, Table 13）。如果退化随 scale 增长，这会严重限制方法的 scalability。论文应至少讨论这个风险。\n\n**R2-Q4: C1 s42 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？**\n\n[AGREE] 如上 W1(a) 所述。s42 使用 earlier training run 的 oracle，gap 0.65pp；retrained oracles（s123, s456）gap ≤0.02pp。这个差异说明 oracle provenance 确实有影响，尽管影响量级（0.65pp）相对于 KL vs magnitude-BCE 的差距（11.79 vs 28.13）仍然很小。\n\n**R2-Q5: Abstract matched sparsity 数字**\n\n[REBUT] 使用 matched sparsity（14.5%）比 nominal（18.6%）更保守、更诚实。KL actual sparsity 28.5% vs TEAL 29.3% 存在 0.8pp 差异，用 matched sparsity 数字排除了这个 confound。论文在 §1 和 Appendix D 中都注明了这一点。如果用 nominal 18.6%，反而会因为 sparsity mismatch 而膨胀 advantage。Reviewer 2 的问题本身是合理的（读者可能困惑为什么不用更大的数字），但论文的选择是正确的。\n\n---\n\n### Missing References\n\n[AGREE] COTS (Zhang et al., 2025) 和 LazyLLM (Fu et al., 2024) 是合理的补充建议，分别涉及 token-level sparsity 和 lazy token processing，与本文的 contextual sparsity 方向相关。\n\n---\n\n### 小问题\n\n[AGREE] \"universally use BCE\" 确实不准确——ShadowLLM 用 MSE。建议改为 \"primarily rely on decomposed losses (BCE or per-layer MSE)\"。\n\n[AGREE] Table 2 actual sparsity 差异应更显著标注。\n\n[AGREE] MSE s123 catastrophic failure 应在正文更显著提及（与我的 R1-W5 一致）。\n\n---\n\n### 综合评价\n\nReviewer 2 的审稿质量较高，多数批评有据。我与 R2 在以下核心问题上达成共识：\n1. **无实际加速** (N2 = 我的 N1)\n2. **MMLU/GSM8K 系统退化未解释** (N3 = 我的 N2)\n3. **C1 confounds** (W1 ≈ 我的 W4)\n4. **术语混淆** (W2，R2 比我更精确地指出了 \"coupling alignment\" 术语问题)\n\n我与 R2 的主要分歧在：\n1. **MaskLLM 新颖性** (N1)：R2 认为 \"完全一致\"，我认为 predictor network 和 global allocation 是非平凡差异，但同意方法新颖性有限\n2. **30% ceiling 对比 Polar Sparsity** (W3)：R2 的对比不公平（不同 sparsity 类型），但指出的 practical utility 问题成立\n3. **Abstract matched sparsity 数字** (Q5)：R2 质疑用 14.5% 而非 18.6%，我认为论文选择更保守更正确\n\nOverall 评分，我同意 R2 的 3.0 (Findings)，但 Excitement 我给 3.0 vs R2 的 2.0——论文的 analysis contributions（C1 ablation, 5-way loss comparison）在 empirical study 类别中有中等价值，2.0 偏低。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: 与 MaskLLM 的新颖性区分不足**\n\nReviewer 2 称核心配方与 MaskLLM (NeurIPS 2024) \"完全一致\"，三点区分只是 \"application-level 差异\"。我认为这个批评过于简化。\n\n(1) **Mask generation 的差异不是 application-level 的**。MaskLLM 的 masks 是直接可学习参数（one per weight group），训练完成后固定。本文的 masks 由 predictor network 在推理时从 hidden states 生成，每个 token 不同。这是 architecture-level 的差异——前者是参数优化问题，后者是函数逼近问题。predictor 需要从 $\\mathbf{x}^{(\\ell)}$ 泛化到 unseen inputs（§3.2），MaskLLM 不需要。\n\n(2) **Global top-k allocation 创造了 MaskLLM 不存在的跨层依赖**。MaskLLM 在 fixed N:M groups 内优化（局部独立），本文的 masks 在全模型 global top-k 下竞争（§3.1, Eq. 2）——一个层的 mask 质量直接影响其他层获得的 neuron budget（Appendix E, Figure 4 per-layer retention 分析）。这是 per-layer KL 分解（§4.5）和 allocation strategy 分析（§4.6, Table 14）存在意义的前提。\n\n(3) 不过，我同意 Reviewer 2 关于 **analysis contribution 的定位需要更精确**。C1 target-swap ablation 确实是实验设计而非方法论创新，2D taxonomy 是分类而非理论框架。但 \"实验设计创新\" 在 empirical study 中是合理的贡献形式——论文明确自我定位为 \"primarily an empirical study\"（§1 倒数第二段）。\n\n**总结**：方法层面的新颖性确实有限（recipe-level overlap 真实存在），但三点差异中至少两点（predictor network、global allocation）具有非平凡的技术含义。R2 的批评在 \"surprise factor 有限\" 这一点上是成立的，但 \"完全一致\" 的措辞过强。\n\n---\n\n**[AGREE] R2-N2: 无实际推理加速**\n\n与我的 R1-N1 一致。论文 Appendix A (Table 5) 明确显示 +6.4% latency overhead。这是一个 critical limitation。不过我要补充一个 nuance：Reviewer 2 引用 Polar Sparsity (2.2× speedup) 和 SVD-CSP (1.8× speedup) 作为对比，但需注意 (a) Polar Sparsity 是 attention head sparsity（结构化），与本文的 FFN neuron sparsity（非结构化）不是同一类问题；(b) SVD-CSP 是 predictor compression 方法，与本文的 training objective 研究不直接可比。直接对比可能误导读者。但核心批评——无加速的 sparsity prediction 实用价值有限——完全成立。\n\n---\n\n**[AGREE] R2-N3: 知识密集型任务系统性退步**\n\n与我的 R1-N2 一致。Table 2（8B MMLU -5.2pp）、Table 13（14B MMLU -8.1pp, GSM8K -20pp）、Table 17（Mistral MMLU tied, GSM8K -7.3pp）构成了跨 scale 的一致证据。论文仅提供假设性解释（§4.2 \"mode-covering may dilute task-specific knowledge pathways\"），未进行任何验证实验（例如 per-layer mask divergence analysis on MMLU-relevant inputs）。Reviewer 2 提出的反问——\"如果 coupling alignment 真的 dominant，为什么 knowledge tasks 反而更差\"——有力地指出了论文 narrative 的内在张力。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: C1 ablation confounds**\n\n与我的 R1-W4 一致。具体补充：\n\n(a) **s42 oracle provenance**: Table 3 footnote 明确标注 s42 oracle 来自 \"earlier training run\"，而 s123/s456 使用 \"matched retrained oracles\"。s42 的 0.65pp PPL gap（9.45 vs 8.80）大于 retrained seeds 的 ≤0.02pp gap（如 s123: 8.84 vs 8.83），说明 oracle provenance 确实影响结论。\n\n(b) **soft-vs-hard confound**: BCE+Gumbel (32.22) 实际上比 standard BCE (27.97) 更差，这恰恰说明 Gumbel relaxation 与 BCE 的组合是有害的。但论文用此证明 \"softness alone does not explain KL's advantage\"（§4.4）——这个推理是正确的（Gumbel 对 BCE 有害但对 KL 有利，说明 loss function 才是关键变量），但需要更清晰地表述。\n\n(c) Reviewer 2 的 \"(b) oracle masks 编码了 KL specific trajectory\" 与 Appendix P 的承认一致。我认为 3-seed 一致性（≤1.70pp at 30%）提供了 partial 但非 conclusive 的鲁棒性证据。\n\n---\n\n**[AGREE] R2-W2: \"Coupling alignment\" 术语混淆 signal type 和 coupling**\n\n这是一个比我原始审稿中提出的更精确的批评。论文 §5 Conclusion: \"Coupling alignment---optimizing through the output distribution---is the dominant design dimension\"——但论文自己的 per-layer KL 实验（§4.5）显示 coupling scope 只贡献 PPL gap 的 2.5%！\"Coupling alignment\" 这个术语暗示 cross-layer coupling 是核心，但数据说明是 signal type（output distribution vs intermediate representation）才是核心。\n\nReviewer 2 正确指出了这个 conflation：如果 per-layer KL（无 cross-layer coupling 但有 output-distribution signal）已经达到 E2E KL 98% 的效果，那么 \"coupling\" 不应该是 selling point。论文应该用 \"output-distribution alignment\" 而非 \"coupling alignment\" 作为核心术语。\n\n---\n\n**[REBUT] R2-W3: 30% sparsity ceiling 过低（对比 Polar Sparsity 50% < 1% drop）**\n\n这个对比不公平，原因有三：\n\n(1) **Sparsity 类型不同**。Polar Sparsity 是 attention head sparsity（结构化、粗粒度），本文是 FFN neuron sparsity（非结构化、细粒度）。两者的 capacity-quality tradeoff 完全不同。移除一个 attention head 与移除单个 FFN neuron 的影响不可直接对比。\n\n(2) **模型基线不同**。Polar Sparsity 的 \"< 1% drop\" 通常报告在特定 benchmark 上的 best-case scenario。本文的 MMLU 65.27→40.7 确实是大幅退化，但这是 FFN activation sparsity 的 *所有* 方法都面临的问题——TEAL 也只有 45.86（-19.4pp），BCE 更差（36.3）。这是问题的固有难度，不是本文方法的特有缺陷。\n\n(3) **Dense baseline 的 capacity utilization 不同**。LLaMA-3.1-8B 在 MMLU 上只有 65.27%（远非完美），说明 FFN 的 capacity 已被高度利用。移除 30% 的 FFN neurons 必然导致显著退化。\n\n我同意 Reviewer 2 指出了 practical utility 的问题，但用 Polar Sparsity 的数字直接对比来论证 \"30% ceiling 过低\" 是不恰当的。\n\n---\n\n**[AGREE] R2-W4: 术语过度创造**\n\n同意这是一个 minor 但 valid 的风格问题。\"coupling alignment ranking\" 本质上就是 \"loss function comparison\"，\"signal type × coupling scope\" 就是 \"loss target × optimization scope\"。过度包装简单概念确实增加了阅读负担。但这不影响技术正确性。\n\n---\n\n**[AGREE] R2-W5: Batch size 限制未讨论**\n\n这是一个被论文完全忽略的实际问题。Per-token contextual sparsity 在 batched inference 下会遇到 \"mask union\" 问题——batch 内不同 token 需要不同 neurons，实际保留的 neuron set 可能接近 dense。Polar Sparsity（§2, Related Work 中已引用）的经验表明这个问题严重。论文应在 Limitations 中讨论 batch size 对 effective sparsity 的影响。\n\n---\n\n### Questions\n\n**R2-Q1: Per-layer KL 达 98% PPL gap，为什么 coupling 是核心 selling point？**\n\n[AGREE] 这与 W2 一致。论文的数据不支持 \"coupling\" 作为核心 selling point。如果将 framing 改为 \"output-distribution signal type 是 dominant dimension\"（而非 \"coupling alignment\"），narrative 会更诚实。\n\n**R2-Q2: MaskLLM 在 activation sparsity 场景下表现如何？**\n\n[AGREE] 这是一个合理的 baseline 请求。论文声称与 MaskLLM 有本质差异（§2），但未提供 MaskLLM 在 activation sparsity 上的实验。即使 MaskLLM 的 static N:M design 无法直接做 per-token activation sparsity，也应讨论为什么不能适配以及性能预期。\n\n**R2-Q3: 14B GSM8K -20pp 是否随 scale 增长？**\n\n[AGREE] 只有两个 scale（8B, 14B）无法确定趋势。但 8B GSM8K -1.3pp（7.5 vs 8.79）到 14B GSM8K -20pp 的跳跃确实令人担忧（Table 2, Table 13）。如果退化随 scale 增长，这会严重限制方法的 scalability。论文应至少讨论这个风险。\n\n**R2-Q4: C1 s42 的 0.65pp gap 是否说明结论对 oracle provenance 敏感？**\n\n[AGREE] 如上 W1(a) 所述。s42 使用 earlier training run 的 oracle，gap 0.65pp；retrained oracles（s123, s456）gap ≤0.02pp。这个差异说明 oracle provenance 确实有影响，尽管影响量级（0.65pp）相对于 KL vs magnitude-BCE 的差距（11.79 vs 28.13）仍然很小。\n\n**R2-Q5: Abstract matched sparsity 数字**\n\n[REBUT] 使用 matched sparsity（14.5%）比 nominal（18.6%）更保守、更诚实。KL actual sparsity 28.5% vs TEAL 29.3% 存在 0.8pp 差异，用 matched sparsity 数字排除了这个 confound。论文在 §1 和 Appendix D 中都注明了这一点。如果用 nominal 18.6%，反而会因为 sparsity mismatch 而膨胀 advantage。Reviewer 2 的问题本身是合理的（读者可能困惑为什么不用更大的数字），但论文的选择是正确的。\n\n---\n\n### Missing References\n\n[AGREE] COTS (Zhang et al., 2025) 和 LazyLLM (Fu et al., 2024) 是合理的补充建议，分别涉及 token-level sparsity 和 lazy token processing，与本文的 contextual sparsity 方向相关。\n\n---\n\n### 小问题\n\n[AGREE] \"universally use BCE\" 确实不准确——ShadowLLM 用 MSE。建议改为 \"primarily rely on decomposed losses (BCE or per-layer MSE)\"。\n\n[AGREE] Table 2 actual sparsity 差异应更显著标注。\n\n[AGREE] MSE s123 catastrophic failure 应在正文更显著提及（与我的 R1-W5 一致）。\n\n---\n\n### 综合评价\n\nReviewer 2 的审稿质量较高，多数批评有据。我与 R2 在以下核心问题上达成共识：\n1. **无实际加速** (N2 = 我的 N1)\n2. **MMLU/GSM8K 系统退化未解释** (N3 = 我的 N2)\n3. **C1 confounds** (W1 ≈ 我的 W4)\n4. **术语混淆** (W2，R2 比我更精确地指出了 \"coupling alignment\" 术语问题)\n\n我与 R2 的主要分歧在：\n1. **MaskLLM 新颖性** (N1)：R2 认为 \"完全一致\"，我认为 predictor network 和 global allocation 是非平凡差异，但同意方法新颖性有限\n2. **30% ceiling 对比 Polar Sparsity** (W3)：R2 的对比不公平（不同 sparsity 类型），但指出的 practical utility 问题成立\n3. **Abstract matched sparsity 数字** (Q5)：R2 质疑用 14.5% 而非 18.6%，我认为论文选择更保守更正确\n\nOverall 评分，我同意 R2 的 3.0 (Findings)，但 Excitement 我给 3.0 vs R2 的 2.0——论文的 analysis contributions（C1 ablation, 5-way loss comparison）在 empirical study 类别中有中等价值，2.0 偏低。\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-22T09:45:14.638407+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4320
}
```

</details>

---


### Assistant

_source line 1130 · 2026-05-22T09:45:19.409420+00:00_

已提交对 Reviewer 2 的逐条回应。核心共识：无加速(N2)、MMLU退化(N3)、C1 confounds(W1)、术语混淆(W2)。主要分歧：MaskLLM 新颖性(N1)我认为"完全一致"过强，Polar Sparsity 对比(W3)属于不同 sparsity 类型不可直接比较，Abstract matched sparsity 数字(Q5)论文选择更保守正确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 36

## Round 36

62 recorded events


### User

_source line 1131 · 2026-05-22T13:03:17.962949+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计有效性**。

## Venue 信息
- **EMNLP 2026** (ARR May cycle)，deadline 2026-05-25
- Long paper，正文 8 页限制，unlimited references
- ACL template (`\usepackage[review]{acl}`)，double-blind
- Mandatory Limitations section（不计页数）
- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文信息
- 文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf`
- 标题：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

## 你的审查侧重

重点审查以下维度，每个维度至少给出具体评价：

1. **方法合理性**：KL distillation + Gumbel-Sigmoid 框架是否 well-motivated？梯度分析（§3.6）是否严谨？自适应惩罚控制器（§3.5）是否有理论/经验支撑？
2. **实验设计**：对照实验是否充分？控制变量是否干净？baseline 选择是否公平？是否存在未控制的 confound？
3. **统计有效性**：多种子覆盖是否一致？哪些关键 claim 只有 single-seed 支撑？error bar 报告是否完整？
4. **Target-swap ablation（C1）**：因果推断链是否严密？是否存在循环论证或 trajectory confound？
5. **Per-layer KL 分解**：train-inference mismatch (K=1 训练 mask 1 层 / 推理 32 层) 是否 confounds 2D decomposition？K=4 pilot 是否足以解决？
6. **可复现性**：超参、训练细节、评估协议是否完整可复现？

请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Critical/Major/Minor/Info) → Questions → Missing References → Overall Assessment (score + confidence)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-22T13:03:25.912706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-22T13:03:27.267193+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1354
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-22T13:03:27.267593+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-22T13:03:27.318052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-22T13:03:35.482199+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 1137 · 2026-05-22T13:03:37.491117+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf",
  "pages": "1-10",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf",
    "pages": "1-10",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1138 · 2026-05-22T13:03:45.013529+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about the ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score

The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Meta-Review Scoring (as of February 2025)

The new options are: 5 = Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top
…[truncated 598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9531
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-22T13:03:46.731352+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9240
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-22T13:03:56.771746+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring form: all dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and detailed descriptions of each score level. Also extract any specific instructions about what constitutes a good vs bad review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring form: all dimensions (soundness, excitement, overall assessment, confidence, etc.), their scales, and detailed descriptions of each score level. Also extract any specific instructions about what constitutes a good vs bad review."
  }
}
```

</details>

---


### Tool call

_source line 1141 · 2026-05-22T13:03:57.674855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-22T13:03:58.179124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-22T13:03:58.581787+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1144 · 2026-05-22T13:03:58.582236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-22T13:03:59.537050+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 1146 · 2026-05-22T13:03:59.539942+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1147 · 2026-05-22T13:03:59.540558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-22T13:03:59.742231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-22T13:04:00.547551+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool result

_source line 1150 · 2026-05-22T13:04:00.699220+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-22T13:04:03.308207+00:00_

# ARR Reviewer Scoring Form and Guidelines

## Scoring Dimensions

Based on the ARR guidelines, reviewers provide **three main scores**:

### 1. **Soundness**
This assesses technical quality and validity. The guidelines state that "soundness scores must be justified by the text of the review." Low soundness ratings without documented flaws indicate an incomplete or biased assessment.

### 2. **Excitement**
This reflects personal interest level, described as "orthogonal to the assessment of the soundness of the paper." It captures subjective preference rather than objective quality.

### 3. **Overall Assessment**
This is "an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue." It integrates soundness, excitement, novelty, and potential impact considerations.

## Additional Scoring Elements

**Confidence Score**: Reviewers indicate their confidence level, particularly relevant when expertise doesn't fully cover all paper aspects.

**Reproducibility Score**: Justified separately, assessing whether sufficient implementation details exist for replication.

## Key Instructions for Quality Reviews

**Specificity**: Avoid vague criticisms. Instead of "X is unclear," explain "Y and Z are missing from X's description."

**Professional tone**: Reviews should be "professional and neutral, if not kind." Sarcasm and dismissiveness are discouraged.

**Justified scores**: All ratings must align with review content. Misaligned scores suggest unconscious bias or incomplete analysis.

**Avoid common heuristics**: Don't penalize papers for being "too simple," lacking SOTA results, using non-English data, or addressing niche topics if methodologically sound.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6536
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-22T13:04:11.040943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1153 · 2026-05-22T13:04:11.544439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1154 · 2026-05-22T13:04:12.602535+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1561
}
```

</details>

---


### Tool call

_source line 1155 · 2026-05-22T13:04:12.602981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-22T13:04:13.007758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1157 · 2026-05-22T13:04:13.462342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1158 · 2026-05-22T13:04:13.614854+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2070
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-22T13:04:15.360447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2757
}
```

</details>

---


### Tool result

_source line 1160 · 2026-05-22T13:04:15.865049+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2857
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-22T13:04:15.865812+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2403
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-22T13:04:24.187189+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf",
  "pages": "11-19",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf",
    "pages": "11-19",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-22T13:04:26.341882+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 575.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 319.0}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 0.0}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p19.png\", \"wid
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2154
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-22T13:04:30.970188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1165 · 2026-05-22T13:04:31.321316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1166 · 2026-05-22T13:04:32.278598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 1167 · 2026-05-22T13:04:32.279732+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-22T13:04:32.380455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1169 · 2026-05-22T13:04:32.782241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1170 · 2026-05-22T13:04:33.284944+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-22T13:04:33.285380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-22T13:04:34.191072+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-22T13:04:34.191529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-22T13:04:34.393133+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-22T13:04:34.393547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1176 · 2026-05-22T13:04:35.097012+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-22T13:04:35.099475+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-22T13:04:43.887356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-22T13:04:43.887715+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-22T13:04:50.264393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-22T13:04:50.265090+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-22T13:04:50.367337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-22T13:04:50.468464+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-22T13:04:58.649455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-22T13:04:59.503296+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 34205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-22T13:04:59.503664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-22T13:04:59.604461+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-22T13:04:59.655039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-22T13:04:59.705640+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment---optimizing through the model's final prediction---is the dominant design dimension for PPL (signal type: up to 97.5\% of the gap at 30\%); a $K{=}4$ mismatch pilot (single seed) reveals task-dependent downstream structure: PPL and BoolQ gaps are predominantly mismatch, while commonsense retains $\sim$60\% genuine coupling.
5	A predictor ($<$1\% of base) reduces TEAL's perplexity by 14.5\% via masks 46--68\% divergent from magnitude; downstream transfer is task- and scale-dependent.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-22T13:08:27.970206+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告（方法严谨性 + 实验设计 + 统计有效性）\n\n### 总体评分\n\n**Overall Assessment**: **3** (Findings)\n**Confidence**: 4/5\n**一句话总结**: 提出 KL 蒸馏替代 BCE 训练稀疏预测器的新视角，PPL 改进显著且消融充分，但缺乏实际加速收益、下游知识任务系统性退化、以及关键因果分解实验的 confound 削弱了核心 claim 的说服力。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心框架合理但 C1 ablation 有 trajectory confound，per-layer KL 的 97.5% signal-type claim 基于 confounded K=1 设置，K=4 pilot 仅 single-seed |\n| Excitement | 2.5/5 | 2D taxonomy 和 coupled-vs-decomposed 视角有学术价值，但无 wall-clock 加速（+6.4% overhead）且下游知识任务系统性退化 |\n| Reproducibility | 4/5 | 超参、架构、训练细节充分；单 GPU ~45min 门槛低；缺代码/checkpoint |\n| Confidence | 4/5 | 熟悉 contextual sparsity、KD、SwiGLU 相关文献 |\n\n### 主要优势\n\n**S1.** 新颖且 well-motivated 的问题框架——将稀疏预测从 per-neuron BCE 提升到 output-distribution KL，forward KL 的 mode-covering 性质在 false-negative 代价不对称的稀疏场景中有理论基础（§3.4）。2D taxonomy (Table 1) 为组织该领域提供了有用的思维框架。\n\n**S2.** 全面且诚实的消融实验——Table 4 覆盖 8 种配置（divergence × relaxation × coupling），发现不利结果（MMLU/GSM8K 退化）如实报告。\n\n**S3.** C1 target-swap ablation 设计有创意——用 KL-derived masks 作为 BCE 训练目标分离 mask quality 与 gradient coupling（§4.3, Table 3），3 种子覆盖 ≤1.70pp 一致性。\n\n**S4.** 跨架构验证——Mistral-7B（3-seed）和 Qwen-2.5-14B 上 PPL advantage ratio 一致（within 8%, Appendix N）。\n\n**S5.** 训练效率高——单 GPU ~45min，predictor <1% base model 参数。\n\n### Must-Fix 问题\n\n**N1** [Critical] 无 wall-clock 加速收益\n- 位置：Appendix A (Table 5), line 32-34\n- 论文承认 unstructured element-wise masks \"do not translate to wall-clock speedup\"，当前实现增加 6.4% 推理延迟。论文定位是 sparsity prediction for efficiency，但无实际加速数据，实践动机被根本削弱。\n\n**N2** [Critical] Per-layer KL 分解的 \"97.5% signal type\" claim 基于 confounded K=1 设置\n- 位置：§4.5 (experiments.tex line 162-163), Table 19\n- K=1 训练 mask 1/32 层 vs 推理 mask 32 层，train-inference mismatch 严重。K=4 pilot 仅 single-seed，且 MMLU K=4 超过 E2E KL（43.5 vs 40.7±1.3），GSM8K 负向 gap closure（-6.8%）——反常结果未能排除。\n\n**N3** [Major] 下游知识任务系统性退化，framing 偏重 PPL\n- 位置：Table 2, Table 14, Limitations\n- MMLU/GSM8K 退化跨 8B/14B 两个 scale，跨 LLaMA/Qwen 两个架构。Abstract/Introduction 以 PPL 改进为主叙事，下游 trade-off 仅在 Conclusion 以 \"task- and scale-dependent\" 一笔带过。\n\n### Should-Fix 问题\n\n**W1** [Major] C1 的 trajectory confound——oracle masks 从特定 KL trajectory 提取，s42 oracle 来自 earlier training run（Table 3 footnote）。C1 证明 masks 可 transfer，但未证明 KL 是发现好 masks 的唯一/最佳途径。\n\n**W2** [Major] 训练/评估域重叠——WikiText-103 训练 + WikiText-2 评估均来自 Wikipedia。C4 OOD 显示 31× 更高 cross-seed variance。\n\n**W3** [Minor] MSE baseline 可能未被公平调参——seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）表明配置不够稳健。\n\n**W4** [Minor] Global allocation 30% MMLU σ=9.5pp，结果不可解读。\n\n**W5** [Minor] 符号冲突——g^(ℓ) 在 Eq.(1) 为 gate activation，Eq.(4) 中 g1/g2 为 Gumbel noise。\n\n### Questions\n\nQ1. K=4 是否有多种子数据？MMLU 超过 E2E KL 是否为系统性现象？\nQ2. 有没有尝试 per-layer sparsity 约束来缓解 L22-L28 过度修剪？\nQ3. 补偿对 BCE predictor 的效果如何？\"compensation provides no benefit\" 可能仅因 KL 自带补偿。\nQ4. 更大/更多样训练集是否能缓解 OOD variance？\n\n### Missing References\n\n- Griffin et al., 2024 (Mixture of A Million Experts)\n- Mirzadeh et al., 2024 (ReLU-fication of LLMs)\n- Wanda (已引未对比讨论互补性)\n\n### 结论\n\n论文有学术价值（新视角、全面消融、诚实 limitation），但三个核心问题阻止 Conference-level：(1) 无实际推理加速；(2) 知识任务系统性退化无解决路径；(3) 核心分析 claim (97.5% signal type) 基于 confounded 实验。适合 Findings track。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告（方法严谨性 + 实验设计 + 统计有效性）\n\n### 总体评分\n\n**Overall Assessment**: **3** (Findings)\n**Confidence**: 4/5\n**一句话总结**: 提出 KL 蒸馏替代 BCE 训练稀疏预测器的新视角，PPL 改进显著且消融充分，但缺乏实际加速收益、下游知识任务系统性退化、以及关键因果分解实验的 confound 削弱了核心 claim 的说服力。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心框架合理但 C1 ablation 有 trajectory confound，per-layer KL 的 97.5% signal-type claim 基于 confounded K=1 设置，K=4 pilot 仅 single-seed |\n| Excitement | 2.5/5 | 2D taxonomy 和 coupled-vs-decomposed 视角有学术价值，但无 wall-clock 加速（+6.4% overhead）且下游知识任务系统性退化 |\n| Reproducibility | 4/5 | 超参、架构、训练细节充分；单 GPU ~45min 门槛低；缺代码/checkpoint |\n| Confidence | 4/5 | 熟悉 contextual sparsity、KD、SwiGLU 相关文献 |\n\n### 主要优势\n\n**S1.** 新颖且 well-motivated 的问题框架——将稀疏预测从 per-neuron BCE 提升到 output-distribution KL，forward KL 的 mode-covering 性质在 false-negative 代价不对称的稀疏场景中有理论基础（§3.4）。2D taxonomy (Table 1) 为组织该领域提供了有用的思维框架。\n\n**S2.** 全面且诚实的消融实验——Table 4 覆盖 8 种配置（divergence × relaxation × coupling），发现不利结果（MMLU/GSM8K 退化）如实报告。\n\n**S3.** C1 target-swap ablation 设计有创意——用 KL-derived masks 作为 BCE 训练目标分离 mask quality 与 gradient coupling（§4.3, Table 3），3 种子覆盖 ≤1.70pp 一致性。\n\n**S4.** 跨架构验证——Mistral-7B（3-seed）和 Qwen-2.5-14B 上 PPL advantage ratio 一致（within 8%, Appendix N）。\n\n**S5.** 训练效率高——单 GPU ~45min，predictor <1% base model 参数。\n\n### Must-Fix 问题\n\n**N1** [Critical] 无 wall-clock 加速收益\n- 位置：Appendix A (Table 5), line 32-34\n- 论文承认 unstructured element-wise masks \"do not translate to wall-clock speedup\"，当前实现增加 6.4% 推理延迟。论文定位是 sparsity prediction for efficiency，但无实际加速数据，实践动机被根本削弱。\n\n**N2** [Critical] Per-layer KL 分解的 \"97.5% signal type\" claim 基于 confounded K=1 设置\n- 位置：§4.5 (experiments.tex line 162-163), Table 19\n- K=1 训练 mask 1/32 层 vs 推理 mask 32 层，train-inference mismatch 严重。K=4 pilot 仅 single-seed，且 MMLU K=4 超过 E2E KL（43.5 vs 40.7±1.3），GSM8K 负向 gap closure（-6.8%）——反常结果未能排除。\n\n**N3** [Major] 下游知识任务系统性退化，framing 偏重 PPL\n- 位置：Table 2, Table 14, Limitations\n- MMLU/GSM8K 退化跨 8B/14B 两个 scale，跨 LLaMA/Qwen 两个架构。Abstract/Introduction 以 PPL 改进为主叙事，下游 trade-off 仅在 Conclusion 以 \"task- and scale-dependent\" 一笔带过。\n\n### Should-Fix 问题\n\n**W1** [Major] C1 的 trajectory confound——oracle masks 从特定 KL trajectory 提取，s42 oracle 来自 earlier training run（Table 3 footnote）。C1 证明 masks 可 transfer，但未证明 KL 是发现好 masks 的唯一/最佳途径。\n\n**W2** [Major] 训练/评估域重叠——WikiText-103 训练 + WikiText-2 评估均来自 Wikipedia。C4 OOD 显示 31× 更高 cross-seed variance。\n\n**W3** [Minor] MSE baseline 可能未被公平调参——seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）表明配置不够稳健。\n\n**W4** [Minor] Global allocation 30% MMLU σ=9.5pp，结果不可解读。\n\n**W5** [Minor] 符号冲突——g^(ℓ) 在 Eq.(1) 为 gate activation，Eq.(4) 中 g1/g2 为 Gumbel noise。\n\n### Questions\n\nQ1. K=4 是否有多种子数据？MMLU 超过 E2E KL 是否为系统性现象？\nQ2. 有没有尝试 per-layer sparsity 约束来缓解 L22-L28 过度修剪？\nQ3. 补偿对 BCE predictor 的效果如何？\"compensation provides no benefit\" 可能仅因 KL 自带补偿。\nQ4. 更大/更多样训练集是否能缓解 OOD variance？\n\n### Missing References\n\n- Griffin et al., 2024 (Mixture of A Million Experts)\n- Mirzadeh et al., 2024 (ReLU-fication of LLMs)\n- Wanda (已引未对比讨论互补性)\n\n### 结论\n\n论文有学术价值（新视角、全面消融、诚实 limitation），但三个核心问题阻止 Conference-level：(1) 无实际推理加速；(2) 知识任务系统性退化无解决路径；(3) 核心分析 claim (97.5% signal type) 基于 confounded 实验。适合 Findings track。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-22T13:08:31.685253+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3715
}
```

</details>

---


### Assistant

_source line 1192 · 2026-05-22T13:08:39.190223+00:00_

审稿报告已提交给 Review Director。

**评分总结：Overall 3 (Findings)，Confidence 4/5。**

三个核心问题：
1. **无 wall-clock 加速**（+6.4% overhead），实践动机薄弱
2. **Per-layer KL 分解的 97.5% signal-type claim** 基于 confounded K=1 设置，K=4 pilot 仅 single-seed 且有反常结果
3. **MMLU/GSM8K 系统性退化**跨模型跨架构，但论文 framing 偏重 PPL 改进

论文的消融设计和诚实的 limitation 讨论是优点，适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 37

## Round 37

4 recorded events


### User

_source line 1193 · 2026-05-22T13:10:19.916848+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿报告

**Overall**: 3.0 (Findings), Confidence 4/5

### 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（多 seed、cross-arch），但 97.5% signal type 上界基于非正交分解不可靠；K=4 pilot 单 seed；主表实际 sparsity 不匹配 |
| Excitement | 2.5/5 | KL+Gumbel+frozen model recipe 与 MaskLLM 高度重合；无实际 wall-clock 加速（反增 6.4%）；分析框架有价值但 insights 部分可预期 |
| Reproducibility | 4/5 | 详细的超参数、多 seed 评估、训练步数/温度/bottleneck 灵敏度分析；但未释放代码 |

### 主要优势
S1. Target-swap ablation (C1) 实验设计精巧。Table 3 在 3 个 seed (30%) 和 1 个 seed (50%) 上结果一致（max Δ≤1.70pp）。
S2. 多 seed 评估 + 诚实的混合结果报告。3-seed 贯穿全文，cross-seed variance 分析透明。
S3. 2D taxonomy 提供清晰的组织框架。
S4. 跨架构验证有说服力（Mistral-7B 3-seed, Qwen-2.5-14B）。
S5. 消融实验覆盖全面（Table 4, 8 种配置）。

### Must-Fix 问题
**N1** [critical] 与 MaskLLM 的 recipe 新颖性区分不足——KL+Gumbel+frozen model 组合在 MaskLLM 已建立，本文增量是从 static N:M weight sparsity 迁移到 dynamic activation sparsity。Related Work 承认 "shares the recipe-level principle" 但未实验量化差异。
**N2** [critical] 无实际推理加速——6.4% overhead，unstructured masks 无 wall-clock speedup。Introduction framing 暗示效率目标但无法兑现。

### Should-Fix 问题
**W1** [major] "97.5% signal type" 基于非正交分解，Abstract/Conclusion 中无 caveat。
**W2** [major] K=4 pilot 仅单 seed，MMLU 43.5 超过 E2E KL 40.7±1.3 可能为随机波动，但 Abstract/Conclusion hedging 不够。
**W3** [major] 主表 sparsity 不匹配（KL 28.5% vs TEAL 29.3%），Abstract 引用的 14.5% 来自 appendix matched 对比而非主表 19%。
**W4** [minor-to-major] 下游知识任务退步归因 late-layer over-pruning 但未验证因果链（如 layer-constrained sparsity 实验）。
**W5** [minor] Baseline 缺少 R-Sparse/CATS/FastForward 完整 pipeline 对比。

### 小问题
M1. Introduction disclaimer 放在括号里太隐蔽。
M2. Table 2 注释过长。
M3. Taxonomy table 信息含量有限。
M4. Figure 2 只展示 global allocation 但推荐 uniform。
M5. 格式合规 ✓。

### Missing References
CATS (已提及无对比), R-Sparse (已提及无对比), Griffin/Hawk (De et al., 2024), TurboSparse KL distillation 步骤。

### Questions
Q1. 在 activation sparsity 设定下实现 MaskLLM learnable-mask approach（去掉 predictor），PPL 如何？
Q2. Late-layer over-pruning 是否可通过 per-layer constraint 缓解？
Q3. 为什么没有 50% K=4 3-seed 数据？
Q4. 是否尝试更 diverse 训练数据降低 OOD variance？

---

请对以上每条 N/W/M/Q 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-22T13:12:34.632597+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Must-Fix\n\n[AGREE] R2-N1: MaskLLM recipe 重合。核心技术组件（KL+Gumbel+frozen model）确实与 MaskLLM 高度重合。论文更接近 empirical study（Introduction 自承），方法创新有限。\n\n[AGREE] R2-N2: 无 wall-clock 加速。与我的 N1 一致，+6.4% overhead 是最根本的实践性缺陷。\n\n### Should-Fix\n\n[AGREE] R2-W1: \"97.5% signal type\" 非正交分解。与我的 N2 一致，Abstract/Conclusion 缺乏 caveat。\n\n[AGREE] R2-W2: K=4 单 seed。与我的 N2 一致，MMLU 43.5 > E2E KL 40.7±1.3 的反常结果在单 seed 下无法排除随机波动。\n\n[REBUT] R2-W3: Sparsity mismatch。论文处理审慎——Table 2 脚注标注差异，Abstract 用 matched 14.5% 而非 main table 19%，Appendix C 补充了 TEAL@28.5% 的 PPL。0.8pp 差异不改变定性结论。但同意应在正文中更显著讨论。\n\n[AGREE] R2-W4: Late-layer over-pruning 归因缺因果验证。仅 correlational 证据，缺 per-layer sparsity constraint 的 interventional 实验。与我的 Q2 一致。\n\n[REBUT] R2-W5: 缺 R-Sparse/CATS/FastForward 完整 pipeline 对比。论文控制变量比较训练目标（KL vs BCE vs MSE），R-Sparse/CATS 架构不同会混淆变量。FastForward 补偿已在 §4.5 测试。但同意补充参考数字会增强 positioning。\n\n### 小问题\n\n[AGREE] M1, M2, M4。[REBUT] M3: taxonomy table 价值在概念框架而非信息密度。\n\n### Questions\n\n[AGREE] Q1-Q4 均为合理问题。\n\n### 两位 Reviewer 共识\n\n核心弱点：(1) 无 wall-clock 加速；(2) K=4 pilot underpowered 导致 97.5% claim 不可靠；(3) 知识任务退化归因缺因果验证。Overall 维持 3 (Findings)。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n### Must-Fix\n\n[AGREE] R2-N1: MaskLLM recipe 重合。核心技术组件（KL+Gumbel+frozen model）确实与 MaskLLM 高度重合。论文更接近 empirical study（Introduction 自承），方法创新有限。\n\n[AGREE] R2-N2: 无 wall-clock 加速。与我的 N1 一致，+6.4% overhead 是最根本的实践性缺陷。\n\n### Should-Fix\n\n[AGREE] R2-W1: \"97.5% signal type\" 非正交分解。与我的 N2 一致，Abstract/Conclusion 缺乏 caveat。\n\n[AGREE] R2-W2: K=4 单 seed。与我的 N2 一致，MMLU 43.5 > E2E KL 40.7±1.3 的反常结果在单 seed 下无法排除随机波动。\n\n[REBUT] R2-W3: Sparsity mismatch。论文处理审慎——Table 2 脚注标注差异，Abstract 用 matched 14.5% 而非 main table 19%，Appendix C 补充了 TEAL@28.5% 的 PPL。0.8pp 差异不改变定性结论。但同意应在正文中更显著讨论。\n\n[AGREE] R2-W4: Late-layer over-pruning 归因缺因果验证。仅 correlational 证据，缺 per-layer sparsity constraint 的 interventional 实验。与我的 Q2 一致。\n\n[REBUT] R2-W5: 缺 R-Sparse/CATS/FastForward 完整 pipeline 对比。论文控制变量比较训练目标（KL vs BCE vs MSE），R-Sparse/CATS 架构不同会混淆变量。FastForward 补偿已在 §4.5 测试。但同意补充参考数字会增强 positioning。\n\n### 小问题\n\n[AGREE] M1, M2, M4。[REBUT] M3: taxonomy table 价值在概念框架而非信息密度。\n\n### Questions\n\n[AGREE] Q1-Q4 均为合理问题。\n\n### 两位 Reviewer 共识\n\n核心弱点：(1) 无 wall-clock 加速；(2) K=4 pilot underpowered 导致 97.5% claim 不可靠；(3) 知识任务退化归因缺因果验证。Overall 维持 3 (Findings)。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-22T13:12:38.351173+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3718
}
```

</details>

---


### Assistant

_source line 1196 · 2026-05-22T13:12:44.820408+00:00_

交叉回应已提交。

与 R2 在多数关键问题上达成共识，在 2 条上提出部分反驳（W3 sparsity mismatch 处理合理、W5 baseline scope 有实验设计逻辑）。两位 reviewer 共同确认的核心弱点：无 wall-clock 加速、K=4 pilot 证据不足、知识任务退化归因缺因果验证。Overall 维持 3 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 38

## Round 38

68 recorded events


### User

_source line 1197 · 2026-05-22T17:12:33.242430+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查论文的**方法严谨性和实验设计**。

## 论文信息
- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
- **Venue**: EMNLP 2026 (通过 ARR May 2026 投稿)
- **截止日期**: 2026-05-25
- **页数限制**: Long paper, 正文 8 页, references 不限, Limitations 和 Ethics 不计入页数
- **模板**: ACL LaTeX (review mode)
- **匿名规则**: Double-blind
- **论文路径**: `projects/distill_sparse_swiglu/paper/main.tex`
- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf`

## 你的审查侧重

### 1. 方法严谨性
- KL distillation framework 的数学严谨性：forward KL 选择是否 well-motivated？gradient analysis (§3.6) 的论证是否严密？
- Gumbel-Sigmoid relaxation 的数学正确性和与 STE 的对比是否公平
- Adaptive penalty controller (§3.5) 是否有收敛保证或仅依赖经验
- 2D taxonomy (§3.7) 是否真正是有意义的框架，还是 post-hoc 组织

### 2. 实验设计与统计分析
- Baseline 选择是否公平（BCE 1000 steps vs KL 1000 steps, 但 BCE 2700 steps 也测了）
- 3-seed coverage 是否充分？哪些关键行缺少多种子？
- C1 target-swap ablation (§4.4) 的因果推断是否成立？circularity 和 soft-vs-hard confound 怎么评估？
- Per-layer KL decomposition (§4.5) 的 97.5% signal type 归因：K=1 的 train-inference mismatch confound 有多严重？K=4 的 3-seed 结果是否足够消解？MMLU anomaly 的解释可信度？
- Actual sparsity mismatch (KL 28.5% vs TEAL 29.3%) 对主要结论的影响
- MSE baseline 50% seed 123 catastrophic failure (PPL=15,789) 说明什么

### 3. 可复现性
- 所有超参数是否充分报告
- 训练和评估 protocol 是否清晰可复现

### 评分标准 (ARR Overall Assessment)
5 = Consider for Award (~top 2.5%), 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit

请严格、客观地评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → 评分建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-22T17:12:41.684695+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-22T17:12:41.685122+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-22T17:12:47.184512+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1201 · 2026-05-22T17:12:47.586376+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer form dimensions scoring 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer form dimensions scoring 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-22T17:12:49.794691+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-22T17:12:54.469629+00:00_

Web search results for query: "ACL Rolling Review reviewer form dimensions scoring 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here's what I found about ACL Rolling Review reviewer form dimensions and scoring for 2025-2026:

## Reviewer Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.


…[truncated 1116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6883
}
```

</details>

---


### Tool result

_source line 1204 · 2026-05-22T17:12:54.973137+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow a workflow: (1) read the paper and get the first impression, (2) search for related w
…[truncated 1460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7788
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-22T17:12:56.682440+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6887
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-22T17:13:02.051701+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-22T17:13:02.102223+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1208 · 2026-05-22T17:13:14.803958+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need the exact scoring options for Soundness, Excitement, Overall Assessment, and any other dimensions reviewers must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need the exact scoring options for Soundness, Excitement, Overall Assessment, and any other dimensions reviewers must fill in."
  }
}
```

</details>

---


### Tool call

_source line 1209 · 2026-05-22T17:13:15.458213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1210 · 2026-05-22T17:13:16.114305+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 1211 · 2026-05-22T17:13:16.114742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-22T17:13:16.618620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-22T17:13:17.628848+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1514
}
```

</details>

---


### Tool result

_source line 1214 · 2026-05-22T17:13:17.630618+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1011
}
```

</details>

---


### Tool call

_source line 1215 · 2026-05-22T17:13:17.835906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-22T17:13:18.689681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-22T17:13:20.446556+00:00_

# ACL Rolling Review Form: Scoring Dimensions

## Reviewer Confidence
Scale 1-5:
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with minor chance of missing details
- **3**: Pretty sure but may have missed something
- **2**: Willing to defend evaluation but likely missed details
- **1**: "Not my area, or paper is very hard to understand"

## Soundness
Scale 1-5 (with half-point options):
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Strong study with sufficient support
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: Poor with insufficient support for main claims
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale 1-5 (with half-point options):
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: Potentially interesting but doesn't resonate personally
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment
Scale 1-5 (with half-point options):
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5642
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-22T17:13:26.776188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1219 · 2026-05-22T17:13:27.330922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-22T17:13:27.683900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-22T17:13:28.440920+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1664
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-22T17:13:28.441381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-22T17:13:29.047514+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1716
}
```

</details>

---


### Tool result

_source line 1224 · 2026-05-22T17:13:29.402951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1719
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-22T17:13:29.604969+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1163
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-22T17:13:37.417367+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1227 · 2026-05-22T17:13:38.373608+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-22T17:13:38.374069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-22T17:13:39.378831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-22T17:13:39.780340+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1231 · 2026-05-22T17:13:40.833242+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 309.8}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 350.7}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p19.png\", \"w
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1052
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-22T17:13:44.346247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1233 · 2026-05-22T17:13:45.400636+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1234 · 2026-05-22T17:13:45.753672+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool call

_source line 1235 · 2026-05-22T17:13:45.754104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1236 · 2026-05-22T17:13:46.158777+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool call

_source line 1237 · 2026-05-22T17:13:46.159171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1238 · 2026-05-22T17:13:46.815423+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---


### Tool result

_source line 1239 · 2026-05-22T17:13:47.067219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-22T17:13:52.487777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1241 · 2026-05-22T17:13:52.839404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1242 · 2026-05-22T17:13:53.291961+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1243 · 2026-05-22T17:13:53.292423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1244 · 2026-05-22T17:13:54.499469+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1660
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-22T17:13:54.501705+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1209
}
```

</details>

---


### Tool call

_source line 1246 · 2026-05-22T17:13:54.504101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1247 · 2026-05-22T17:13:54.705325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1248 · 2026-05-22T17:13:55.359437+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-22T17:13:55.410685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-22T17:16:46.568461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-22T17:16:47.077153+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-22T17:16:47.118542+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-22T17:16:47.119271+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 16957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-22T17:16:54.078128+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-22T17:16:54.128823+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 3263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1256 · 2026-05-22T17:16:58.545803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-22T17:16:58.596780+00:00_

100	800 & 11.907 \\ % exp_id: training_steps_sweep
101	1000 & \textbf{11.906} \\ % exp_id: training_steps_sweep
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Training converges rapidly: 95\% of the quality gap closes by step 600, and performance saturates by step 800 ($\Delta < 0.001$ between 800 and 1000 steps).
107	Our default of 1000 steps provides a conservative margin.
108	
109	
110	\section{Adaptive Penalty Controller Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the adaptive penalty controller across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Penalty controller convergence across sparsity targets (multiplicative schedule, margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
119	\label{tab:lagrangian}
120	\small
121	\begin{tabular}{lccccc}
122	\toprule
123	Target $\rho$ & $\lambda_{\max}$ & Final $\lambda$ & Actual sparsity & Deviation \\
124	\midrule
125	30\% & 5000 & 5000 (cap) & 0.285 & 5.0\% \\ % exp_id: kl_30pct_s42
126	40\% & 5000 & 625 & 0.398 & 0.5\% \\ % exp_id: kl_40pct_s42
127	50\% & 1000 & 8 & 0.504 & 0.8\% \\ % exp_id: kl_50pct_s42
128	70\% & 1000 & 1000 (cap) & 0.688 & 1.7\% \\ % exp_id: kl_70pct_s42
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	At 50\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.
134	At 30\% and 70\%, the gap between the gate prior and target is larger, driving $\lambda$ to its respective caps.
135	The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation; this precision reflects a regime where the tar
…[truncated 12728 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1258 · 2026-05-22T17:17:05.596999+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "K.*=.*4.*downstream|k4_downstream|app:k4",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "output_mode": "content",
  "-C": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "K.*=.*4.*downstream|k4_downstream|app:k4",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "output_mode": "content",
    "-C": "5"
  }
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-22T17:17:05.748004+00:00_

496-The decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.
497-
498-\section{Per-Layer KL Downstream Decomposition}
499-\label{app:perlayer_downstream}
500-
501:Table~\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\ coupling scope decomposition at 30\% sparsity (\S\ref{sec:perlayer}). BoolQ's $\approx$100\% coupling is an upper bound confounded by high cross-seed variance ($\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.
502-
503-\begin{table}[h]
504-\centering
505-\caption{2D decomposition at 30\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \S\ref{sec:perlayer}).}
506-\label{tab:perlayer_downstream}
--
519-\bottomrule
520-\end{tabular}}
521-\end{table}
522-
523-\section{$K{=}4$ Mismatch Control}
524:\label{app:k4_downstream}
525-
526:Table~\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\% sparsity.
527-Training with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\ 1/32 layers masked during training, while inference applies all 32).
528-The gap closure column reports the fraction of the $K{=}1 \to$ E2E KL gap closed by $K{=}4$.
529-
530-\begin{table}[h]
531-\centering
532-\caption{3-seed $K{=}4$ mismatch control at 30\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \in \{42, 123, 456\}$). Actual sparsity 29.6\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\text{E2E} - K{=}1) \times 100$.}
533:\label{tab:k4_downstream}
534-\resizebox{\columnwidth}{!}{
535-\begin{tabular}{lcccc}
536-\toprule
537-& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\%) \\
538-\midrule
--
570-\end{table}
571-
572-Protecting late layers (
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-22T17:17:11.017714+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "523",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "523",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-22T17:17:11.069262+00:00_

523	\section{$K{=}4$ Mismatch Control}
524	\label{app:k4_downstream}
525	
526	Table~\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\% sparsity.
527	Training with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\ 1/32 layers masked during training, while inference applies all 32).
528	The gap closure column reports the fraction of the $K{=}1 \to$ E2E KL gap closed by $K{=}4$.
529	
530	\begin{table}[h]
531	\centering
532	\caption{3-seed $K{=}4$ mismatch control at 30\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \in \{42, 123, 456\}$). Actual sparsity 29.6\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\text{E2E} - K{=}1) \times 100$.}
533	\label{tab:k4_downstream}
534	\resizebox{\columnwidth}{!}{
535	\begin{tabular}{lcccc}
536	\toprule
537	& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\%) \\
538	\midrule
539	PPL$\downarrow$ & 8.89$\pm$0.01 & 9.05$\pm$0.02 & 8.81$\pm$0.02 & 66.7 \\
540	ARC-c & 40.0$\pm$1.3 & 39.9 & 43.7$\pm$2.5 & 2.6 \\
541	WG & 66.9$\pm$0.2 & 65.9 & 68.9$\pm$0.4 & 33.3 \\
542	MMLU$^\ast$ & 42.7$\pm$1.4 & 38.6 & 40.7$\pm$1.3 & $>$100 \\
543	GSM8K & 7.0$\pm$1.6 & 5.8 & 7.5$\pm$0.1 & 70.6 \\
544	BoolQ$^\dagger$ & 67.7$\pm$7.5 & 64.5$\pm$11.5 & 73.7 & 34.8 \\
545	\bottomrule
546	\end{tabular}}
547	\vspace{2pt}
548	{\footnotesize $^\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\% (Appendix~\ref{app:constraint}).
549	$^\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}
550	\end{table}
551	
552	\section{Per-Layer Sparsity Constraint Analysis}
553	\label{app:constraint}
554	
555	To test the causal role of the KL predictor's learned per-layer allocation, we evaluate
…[truncated 2022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-22T17:20:49.941298+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## 总体评分\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n**一句话总结**: 扎实的实证研究，KL 蒸馏优于 BCE 训练稀疏性预测器的核心发现可信且有价值，但两个关键因果分析声明（C1 ablation 和 97.5% signal-type decomposition）超出实验证据支撑范围，加之无实际推理加速、规模仅 7–14B，整体处于 Conference/Findings 边界。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心 KL distillation 方法数学正确、实验设计合理。但 C1 因果推断存在循环性，K=1 signal-type decomposition 受严重 train-inference mismatch 混淆，97.5% 精确数字给人虚假精确感。 |\n| Excitement | 3/5 | \"训练目标如何塑造 mask quality\" 的研究问题有意义，但技术组件（KL 蒸馏、Gumbel-Sigmoid、adaptive penalty）均为成熟工具的应用组合。无 wall-clock speedup 削弱实际影响力。 |\n| Confidence | 4/5 | 仔细阅读全文及全部 19 页附录，逐表核验了关键数字。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] C1 Target-Swap Ablation 的因果推断存在循环性，causal claim 过强\n\n- 具体位置：§4.4, Table 3, Abstract (\"the discovered patterns—not the training mechanism itself—as the proximate quality driver\")\n- 问题：C1 实验将 KL 训练发现的 mask 作为 BCE 的 oracle target，证明 BCE 在这些 target 上能达到接近 KL 的 PPL。但这些 mask 本身就是 KL 的 end-to-end gradient coupling 发现的产物。因此 C1 **不能**分离 \"mask pattern quality\" 和 \"the training dynamics that shaped those masks\"——它仅证明了 \"KL-derived masks are transferable to simpler training\"，而非 \"mask patterns alone, independent of discovery mechanism, drive quality\"。\n- 补充证据：\n  - s42 C1 使用了 \"earlier checkpoint\" 的 oracle (Table 3 footnote †)，PPL gap = 0.65pp；而 s123/s456 使用 matched retrained oracle 后 gap ≤0.03pp。两组结果的不一致性本身就说明 oracle 来源（即 KL 训练动态）影响 C1 质量。\n  - 下游任务方向不一致：s42 C1 在 MMLU (+1.7pp) 和 GSM8K (+0.23pp) 上优于 KL，但 s456 C1 在 MMLU (−0.96pp) 和 GSM8K (−0.98pp) 上劣于 KL。如果 mask pattern 是唯一质量驱动因素，下游方向应一致。\n- 为什么影响接收：这是论文三大 contribution 之一（Abstract bullet 3），因果声明的过强直接影响论文核心贡献的可信度。\n- 建议修改方向：将 claim 降级为 \"KL-discovered masks are transferable: BCE trained on KL-derived targets approaches KL-level PPL, suggesting mask patterns carry substantial quality information\"。删除 \"not the training mechanism itself\" 的排除性声明。\n\n**N2** [critical] Per-Layer KL Decomposition 的 \"97.5% signal type dominance\" 受严重混淆变量影响\n\n- 具体位置：§4.5 (Per-Layer KL: Decomposing Signal Type and Coupling Scope)\n- 问题：\n  1. **K=1 的 train-inference mismatch 极大**：训练时仅 mask 1/32 层，推理时 mask 全部 32 层。论文承认 \"The K=1 downstream gap conflates true coupling with train-inference mismatch\"，但仍在主文中使用 \"97.5%\" 作为 headline 数字。\n  2. **K=4 control 引入新的混淆变量**：K=4 的 MMLU 超过 E2E (42.7±1.4 vs 40.7±1.3，Table S in Appendix)，论文解释为 \"near-uniform allocation matching uniform inference\"（即 K=4 的 allocation pattern 恰好比 E2E 更适合 MMLU 的 uniform eval）。这说明 allocation strategy 本身就是一个混淆变量——K=4 改变了 coupling 的同时也改变了 learned allocation pattern。\n  3. **Gap closure 方向不一致**：ARC-c 仅 2.6% closure（\"coupling-dominated\"），WG 33.3%，PPL 66.7%，MMLU >100%（anomalous）。四个 metric 指向截然不同的结论，无法支持一个单一的 \"signal type dominates\" 叙事。\n  4. **论文自己在 footnote 5 中承认 \"signal type and coupling scope are not fully orthogonal\"**，但主文仍给出精确到小数点的 \"97.5%\" 上界，给读者虚假的分离精度。\n- 为什么影响接收：§4.5 是论文的核心分析贡献之一。如果 decomposition 不 clean，论文的分析深度优势大幅减弱。\n- 建议修改方向：\n  - 将 \"97.5%\" 替换为定性描述：\"signal type accounts for the majority of the PPL gap (upper bound; confounded by train-inference mismatch at K=1)\"\n  - 在主文而非 footnote 中明确讨论 orthogonality limitation\n  - 增加 K=4 在 50% sparsity 的实验（目前 50% 仅有 K=1，恰恰是 coupling 贡献最大的区间）\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 无实际推理加速，论文的效率动机与交付成果之间存在 gap\n\n- 具体位置：Appendix A (Table 5), §1 (Introduction)\n- 问题：Table 5 显示方法增加 6.4% 推理延迟 (126.78 vs 119.11 ms/fwd)。论文在 Introduction 中声明 \"we do not address latency optimization (Appendix A)\"，但论文的开篇叙事仍以 inference efficiency 为核心动机 (\"inference allocates budgets globally via top-k ranking\")。虽然论文定位为 empirical study，但缺乏实际 speedup 限制了实际影响力。\n- 建议：在 Introduction 或 Conclusion 主文中（而非仅 Appendix）更显著地讨论这个 gap，并给出 wall-clock speedup 所需的具体条件（什么稀疏核、什么硬件约束），让读者能评估实际可行性。\n\n**W2** [warning] 主表 (Table 2) 中 KL vs TEAL 在不匹配的实际稀疏度下比较\n\n- 具体位置：Table 2, footnote ‡\n- 问题：30% target 下 KL 实际稀疏度 28.5% vs TEAL 29.3%，相差 0.8pp。在 PPL 对稀疏度高度敏感的区间（见 Figure 2），这个差异非 negligible。论文在 Appendix C 中提供了 matched 28.5% 比较 (14.5%)，这比 Table 2 的 raw 数字 (18.6% = (10.82−8.81)/10.82) 低。Abstract 使用了更保守的 14.5%，这是好的，但 Table 2 给读者的第一印象是 18.6% improvement。\n- 建议：在 Table 2 中增加一行 \"TEAL at 28.5% actual sparsity\" 或在 caption 中更显著标注 matched comparison。\n\n**W3** [warning] 规模泛化不足\n\n- 具体位置：§4.6 (Cross-Architecture and Scale)\n- 问题：仅在 7–14B 模型上验证 (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B)。所有三个模型的 MMLU/GSM8K 均出现系统性下降（8B MMLU −5.2pp, 14B GSM8K −20pp），论文解释为 \"a systematic property of distribution-matching objectives\"。如果 KL 的 mode-covering 特性在更大规模下同样牺牲 reasoning 能力，该方法的适用性堪忧。\n- 建议：如无法补充 70B 实验，至少在 Limitations 中明确讨论 \"KL-based training may face a fundamental accuracy-fidelity trade-off on reasoning tasks that could worsen at scale\"。\n\n**W4** [warning] Table 2 中 KL global 50% 的下游评测不完整\n\n- 具体位置：Table 2, KL global (Ours) 50% 行\n- 问题：PPL 报告了 3-seed (11.84±0.15)，但 ARC-c (32.85)、WG (63.46)、MMLU (28.1)、GSM8K (1.29) 均无 ±，表明仅为 s42 单种子结果。同表中 KL uniform 50% 的 ARC-c 和 WG 都有 3-seed ±。这种不一致使读者无法评估 KL global 50% 下游的稳定性。\n- 建议：补充 KL global 50% 的 3-seed 下游评测，或明确标注哪些是单种子结果。\n\n**W5** [warning] K=4 decomposition 仅在 30% 做，50% 缺失\n\n- 具体位置：§4.5\n- 问题：50% 的 per-layer KL 仅有 K=1 结果 (PPL 34.85 vs E2E 11.92，gap 192%)。论文说 \"coupling's share rising from 2.5% to 10.6% (4×)\"，但这个 10.6% 完全来自 K=1，其中 train-inference mismatch 在 50% 处更严重（mask 50% 的神经元 vs 30%）。没有 K=4 的 50% 结果，无法判断 coupling 在高稀疏度下的真实贡献。\n- 建议：补充 K=4 在 50% 的 3-seed 实验，或将 50% 的 coupling 贡献数字标注为 \"confounded upper bound\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: §4.3 extended training 部分，BCE 2700 steps (46 min) 的 wall-clock match 声明值得质疑——KL 需要两次 forward pass (dense + sparse) 而 BCE 仅一次，但 KL 1000 步与 BCE 2700 步花费相同时间。这意味着 BCE 每步更快？如果是，应解释原因（batch size 差异？BCE 不需要 dense forward pass？）。\n- **M2**: Table 1 (Taxonomy) 中 SPON 被归入 \"Static × Coupled\"，但 SPON 是 per-layer bias，其 \"coupling\" 来自 KL loss 但 mask 不依赖 input。这个分类是否准确应在正文中讨论而非仅在 Appendix O。\n- **M3**: Eq. 6 中 penalty 函数使用 $\\text{clamp}(|\\bar{s} - (1-\\rho)| - \\epsilon, \\min=0)^2$——这是 squared hinge loss 形式，但论文称之为 \"adaptive penalty controller\"。实际的 \"adaptive\" 部分是 λ 的 geometric doubling，而非 penalty 函数本身。命名可能误导读者以为有更复杂的自适应机制。\n- **M4**: Limitations 中提到 \"Batched inference... may reduce effective sparsity\"，但未讨论 sequence length 的影响——较长序列可能改变 activation pattern，影响 predictor mask 质量。\n\n---\n\n## Questions to Authors\n\n1. **C1 circularity**: 如果在 magnitude-based masks 上训练 KL (而非 BCE)——即 \"reverse C1\"——结果会怎样？如果 KL coupling 在 magnitude targets 上也能达到好效果，这会进一步弱化 \"mask patterns are the driver\" 的声明。你们是否有这个实验？\n\n2. **K=4 at 50%**: 为什么没有做 50% 的 K=4 实验？这是最能体现 coupling 贡献的区间。是否存在训练不稳定问题？\n\n3. **MMLU 系统性下降**: 你们在三个架构上都观察到 MMLU 下降。这是否暗示 forward KL 的 mode-covering 特性系统性地损害了 reasoning-critical 的 neuron preservation？如果是，这对方法的适用范围有什么根本性限制？\n\n4. **Sparsity controller 在 30% 的 5% deviation**: Appendix C 显示 30% target 下 λ 达到 cap (5000) 但实际稀疏度仅 28.5%。这是否意味着 penalty controller 在低稀疏度下力度不足？如果 λ_max 设更高，实际稀疏度能否逼近 30%？\n\n---\n\n## 主要优势\n\n1. **研究问题有价值且定义清晰**：训练目标如何影响 learned sparsity predictor 的 mask quality 是一个 under-explored 但重要的问题，论文给出了系统性的实证分析。\n\n2. **实验覆盖面广、消融设计用心**：3 个架构、2 个稀疏度水平、6+ 个下游任务、5 个 baseline（TEAL/BCE/MSE/Uniform/STE）、C1 target-swap、K=1/K=4 decomposition、SNR 分析。总实验量远超一般 EMNLP 投稿。\n\n3. **梯度分析 (§3.6) 提供有用 insight**：BCE 梯度仅依赖 neuron j，KL 梯度通过下游 Jacobian 耦合所有层——这个 analysis 虽然是 standard chain rule，但在稀疏性预测场景下的应用是新颖的。配合 SNR 分析（KL 信号更噪但 mask 更好）构成了 \"search mechanism > gradient clarity\" 的有趣叙事。\n\n4. **诚实的局限性讨论**：论文对 MMLU/GSM8K 下降、sparsity mismatch、K=1 confound 等问题有坦诚的讨论（虽然部分问题被放在 footnote/appendix 中显著性不够）。\n\n5. **可复现性好**：所有超参数完整报告（lr、weight decay、τ schedule、batch size、steps、GPU 型号），exp_id 标注在 LaTeX 注释中，training 仅需 ~45 min 单卡。\n\n---\n\n**总结判断**: 论文的核心发现（KL > BCE for sparsity prediction）可信且有实验支撑。但两个关键因果分析（C1 和 signal-type decomposition）的 claim 强度超出实验证据，加之缺乏 wall-clock speedup 和规模泛化，建议评为 Borderline Conference (3.5)。如果 N1 和 N2 的 claim 调整为更审慎的措辞，本文有望进入 Conference (4.0) 档位。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## 总体评分\n\n**Overall**: 3.5/5 (Borderline Conference)\n\n**一句话总结**: 扎实的实证研究，KL 蒸馏优于 BCE 训练稀疏性预测器的核心发现可信且有价值，但两个关键因果分析声明（C1 ablation 和 97.5% signal-type decomposition）超出实验证据支撑范围，加之无实际推理加速、规模仅 7–14B，整体处于 Conference/Findings 边界。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心 KL distillation 方法数学正确、实验设计合理。但 C1 因果推断存在循环性，K=1 signal-type decomposition 受严重 train-inference mismatch 混淆，97.5% 精确数字给人虚假精确感。 |\n| Excitement | 3/5 | \"训练目标如何塑造 mask quality\" 的研究问题有意义，但技术组件（KL 蒸馏、Gumbel-Sigmoid、adaptive penalty）均为成熟工具的应用组合。无 wall-clock speedup 削弱实际影响力。 |\n| Confidence | 4/5 | 仔细阅读全文及全部 19 页附录，逐表核验了关键数字。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] C1 Target-Swap Ablation 的因果推断存在循环性，causal claim 过强\n\n- 具体位置：§4.4, Table 3, Abstract (\"the discovered patterns—not the training mechanism itself—as the proximate quality driver\")\n- 问题：C1 实验将 KL 训练发现的 mask 作为 BCE 的 oracle target，证明 BCE 在这些 target 上能达到接近 KL 的 PPL。但这些 mask 本身就是 KL 的 end-to-end gradient coupling 发现的产物。因此 C1 **不能**分离 \"mask pattern quality\" 和 \"the training dynamics that shaped those masks\"——它仅证明了 \"KL-derived masks are transferable to simpler training\"，而非 \"mask patterns alone, independent of discovery mechanism, drive quality\"。\n- 补充证据：\n  - s42 C1 使用了 \"earlier checkpoint\" 的 oracle (Table 3 footnote †)，PPL gap = 0.65pp；而 s123/s456 使用 matched retrained oracle 后 gap ≤0.03pp。两组结果的不一致性本身就说明 oracle 来源（即 KL 训练动态）影响 C1 质量。\n  - 下游任务方向不一致：s42 C1 在 MMLU (+1.7pp) 和 GSM8K (+0.23pp) 上优于 KL，但 s456 C1 在 MMLU (−0.96pp) 和 GSM8K (−0.98pp) 上劣于 KL。如果 mask pattern 是唯一质量驱动因素，下游方向应一致。\n- 为什么影响接收：这是论文三大 contribution 之一（Abstract bullet 3），因果声明的过强直接影响论文核心贡献的可信度。\n- 建议修改方向：将 claim 降级为 \"KL-discovered masks are transferable: BCE trained on KL-derived targets approaches KL-level PPL, suggesting mask patterns carry substantial quality information\"。删除 \"not the training mechanism itself\" 的排除性声明。\n\n**N2** [critical] Per-Layer KL Decomposition 的 \"97.5% signal type dominance\" 受严重混淆变量影响\n\n- 具体位置：§4.5 (Per-Layer KL: Decomposing Signal Type and Coupling Scope)\n- 问题：\n  1. **K=1 的 train-inference mismatch 极大**：训练时仅 mask 1/32 层，推理时 mask 全部 32 层。论文承认 \"The K=1 downstream gap conflates true coupling with train-inference mismatch\"，但仍在主文中使用 \"97.5%\" 作为 headline 数字。\n  2. **K=4 control 引入新的混淆变量**：K=4 的 MMLU 超过 E2E (42.7±1.4 vs 40.7±1.3，Table S in Appendix)，论文解释为 \"near-uniform allocation matching uniform inference\"（即 K=4 的 allocation pattern 恰好比 E2E 更适合 MMLU 的 uniform eval）。这说明 allocation strategy 本身就是一个混淆变量——K=4 改变了 coupling 的同时也改变了 learned allocation pattern。\n  3. **Gap closure 方向不一致**：ARC-c 仅 2.6% closure（\"coupling-dominated\"），WG 33.3%，PPL 66.7%，MMLU >100%（anomalous）。四个 metric 指向截然不同的结论，无法支持一个单一的 \"signal type dominates\" 叙事。\n  4. **论文自己在 footnote 5 中承认 \"signal type and coupling scope are not fully orthogonal\"**，但主文仍给出精确到小数点的 \"97.5%\" 上界，给读者虚假的分离精度。\n- 为什么影响接收：§4.5 是论文的核心分析贡献之一。如果 decomposition 不 clean，论文的分析深度优势大幅减弱。\n- 建议修改方向：\n  - 将 \"97.5%\" 替换为定性描述：\"signal type accounts for the majority of the PPL gap (upper bound; confounded by train-inference mismatch at K=1)\"\n  - 在主文而非 footnote 中明确讨论 orthogonality limitation\n  - 增加 K=4 在 50% sparsity 的实验（目前 50% 仅有 K=1，恰恰是 coupling 贡献最大的区间）\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 无实际推理加速，论文的效率动机与交付成果之间存在 gap\n\n- 具体位置：Appendix A (Table 5), §1 (Introduction)\n- 问题：Table 5 显示方法增加 6.4% 推理延迟 (126.78 vs 119.11 ms/fwd)。论文在 Introduction 中声明 \"we do not address latency optimization (Appendix A)\"，但论文的开篇叙事仍以 inference efficiency 为核心动机 (\"inference allocates budgets globally via top-k ranking\")。虽然论文定位为 empirical study，但缺乏实际 speedup 限制了实际影响力。\n- 建议：在 Introduction 或 Conclusion 主文中（而非仅 Appendix）更显著地讨论这个 gap，并给出 wall-clock speedup 所需的具体条件（什么稀疏核、什么硬件约束），让读者能评估实际可行性。\n\n**W2** [warning] 主表 (Table 2) 中 KL vs TEAL 在不匹配的实际稀疏度下比较\n\n- 具体位置：Table 2, footnote ‡\n- 问题：30% target 下 KL 实际稀疏度 28.5% vs TEAL 29.3%，相差 0.8pp。在 PPL 对稀疏度高度敏感的区间（见 Figure 2），这个差异非 negligible。论文在 Appendix C 中提供了 matched 28.5% 比较 (14.5%)，这比 Table 2 的 raw 数字 (18.6% = (10.82−8.81)/10.82) 低。Abstract 使用了更保守的 14.5%，这是好的，但 Table 2 给读者的第一印象是 18.6% improvement。\n- 建议：在 Table 2 中增加一行 \"TEAL at 28.5% actual sparsity\" 或在 caption 中更显著标注 matched comparison。\n\n**W3** [warning] 规模泛化不足\n\n- 具体位置：§4.6 (Cross-Architecture and Scale)\n- 问题：仅在 7–14B 模型上验证 (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B)。所有三个模型的 MMLU/GSM8K 均出现系统性下降（8B MMLU −5.2pp, 14B GSM8K −20pp），论文解释为 \"a systematic property of distribution-matching objectives\"。如果 KL 的 mode-covering 特性在更大规模下同样牺牲 reasoning 能力，该方法的适用性堪忧。\n- 建议：如无法补充 70B 实验，至少在 Limitations 中明确讨论 \"KL-based training may face a fundamental accuracy-fidelity trade-off on reasoning tasks that could worsen at scale\"。\n\n**W4** [warning] Table 2 中 KL global 50% 的下游评测不完整\n\n- 具体位置：Table 2, KL global (Ours) 50% 行\n- 问题：PPL 报告了 3-seed (11.84±0.15)，但 ARC-c (32.85)、WG (63.46)、MMLU (28.1)、GSM8K (1.29) 均无 ±，表明仅为 s42 单种子结果。同表中 KL uniform 50% 的 ARC-c 和 WG 都有 3-seed ±。这种不一致使读者无法评估 KL global 50% 下游的稳定性。\n- 建议：补充 KL global 50% 的 3-seed 下游评测，或明确标注哪些是单种子结果。\n\n**W5** [warning] K=4 decomposition 仅在 30% 做，50% 缺失\n\n- 具体位置：§4.5\n- 问题：50% 的 per-layer KL 仅有 K=1 结果 (PPL 34.85 vs E2E 11.92，gap 192%)。论文说 \"coupling's share rising from 2.5% to 10.6% (4×)\"，但这个 10.6% 完全来自 K=1，其中 train-inference mismatch 在 50% 处更严重（mask 50% 的神经元 vs 30%）。没有 K=4 的 50% 结果，无法判断 coupling 在高稀疏度下的真实贡献。\n- 建议：补充 K=4 在 50% 的 3-seed 实验，或将 50% 的 coupling 贡献数字标注为 \"confounded upper bound\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: §4.3 extended training 部分，BCE 2700 steps (46 min) 的 wall-clock match 声明值得质疑——KL 需要两次 forward pass (dense + sparse) 而 BCE 仅一次，但 KL 1000 步与 BCE 2700 步花费相同时间。这意味着 BCE 每步更快？如果是，应解释原因（batch size 差异？BCE 不需要 dense forward pass？）。\n- **M2**: Table 1 (Taxonomy) 中 SPON 被归入 \"Static × Coupled\"，但 SPON 是 per-layer bias，其 \"coupling\" 来自 KL loss 但 mask 不依赖 input。这个分类是否准确应在正文中讨论而非仅在 Appendix O。\n- **M3**: Eq. 6 中 penalty 函数使用 $\\text{clamp}(|\\bar{s} - (1-\\rho)| - \\epsilon, \\min=0)^2$——这是 squared hinge loss 形式，但论文称之为 \"adaptive penalty controller\"。实际的 \"adaptive\" 部分是 λ 的 geometric doubling，而非 penalty 函数本身。命名可能误导读者以为有更复杂的自适应机制。\n- **M4**: Limitations 中提到 \"Batched inference... may reduce effective sparsity\"，但未讨论 sequence length 的影响——较长序列可能改变 activation pattern，影响 predictor mask 质量。\n\n---\n\n## Questions to Authors\n\n1. **C1 circularity**: 如果在 magnitude-based masks 上训练 KL (而非 BCE)——即 \"reverse C1\"——结果会怎样？如果 KL coupling 在 magnitude targets 上也能达到好效果，这会进一步弱化 \"mask patterns are the driver\" 的声明。你们是否有这个实验？\n\n2. **K=4 at 50%**: 为什么没有做 50% 的 K=4 实验？这是最能体现 coupling 贡献的区间。是否存在训练不稳定问题？\n\n3. **MMLU 系统性下降**: 你们在三个架构上都观察到 MMLU 下降。这是否暗示 forward KL 的 mode-covering 特性系统性地损害了 reasoning-critical 的 neuron preservation？如果是，这对方法的适用范围有什么根本性限制？\n\n4. **Sparsity controller 在 30% 的 5% deviation**: Appendix C 显示 30% target 下 λ 达到 cap (5000) 但实际稀疏度仅 28.5%。这是否意味着 penalty controller 在低稀疏度下力度不足？如果 λ_max 设更高，实际稀疏度能否逼近 30%？\n\n---\n\n## 主要优势\n\n1. **研究问题有价值且定义清晰**：训练目标如何影响 learned sparsity predictor 的 mask quality 是一个 under-explored 但重要的问题，论文给出了系统性的实证分析。\n\n2. **实验覆盖面广、消融设计用心**：3 个架构、2 个稀疏度水平、6+ 个下游任务、5 个 baseline（TEAL/BCE/MSE/Uniform/STE）、C1 target-swap、K=1/K=4 decomposition、SNR 分析。总实验量远超一般 EMNLP 投稿。\n\n3. **梯度分析 (§3.6) 提供有用 insight**：BCE 梯度仅依赖 neuron j，KL 梯度通过下游 Jacobian 耦合所有层——这个 analysis 虽然是 standard chain rule，但在稀疏性预测场景下的应用是新颖的。配合 SNR 分析（KL 信号更噪但 mask 更好）构成了 \"search mechanism > gradient clarity\" 的有趣叙事。\n\n4. **诚实的局限性讨论**：论文对 MMLU/GSM8K 下降、sparsity mismatch、K=1 confound 等问题有坦诚的讨论（虽然部分问题被放在 footnote/appendix 中显著性不够）。\n\n5. **可复现性好**：所有超参数完整报告（lr、weight decay、τ schedule、batch size、steps、GPU 型号），exp_id 标注在 LaTeX 注释中，training 仅需 ~45 min 单卡。\n\n---\n\n**总结判断**: 论文的核心发现（KL > BCE for sparsity prediction）可信且有实验支撑。但两个关键因果分析（C1 和 signal-type decomposition）的 claim 强度超出实验证据，加之缺乏 wall-clock speedup 和规模泛化，建议评为 Borderline Conference (3.5)。如果 N1 和 N2 的 claim 调整为更审慎的措辞，本文有望进入 Conference (4.0) 档位。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-22T17:20:53.669704+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3728
}
```

</details>

---


### Assistant

_source line 1264 · 2026-05-22T17:21:04.810546+00:00_

审稿报告已提交给 Review Director。

**评审要点总结**：

- **Overall 3.5/5 (Borderline Conference)**，Soundness 3.5，Excitement 3.0
- **两个 Must-Fix**：(1) C1 target-swap ablation 的因果声明存在循环性——实验证明 mask 可转移但不能证明 "mask 是唯一质量驱动因素"；(2) 97.5% signal-type decomposition 受 K=1 train-inference mismatch 严重混淆，K=4 引入新的 allocation confound（MMLU anomaly），精确数字不可靠
- **五个 Should-Fix**：无实际推理加速、Table 2 sparsity mismatch 不显著标注、规模仅 7–14B、KL global 50% 下游缺 3-seed、K=4 在 50% 缺失
- **核心判断**：KL > BCE 的发现可信，但两个分析性 contribution 的 claim 需降级为更审慎的措辞后方可进入 Conference 档位

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 39

## Round 39

4 recorded events


### User

_source line 1265 · 2026-05-22T17:21:53.999878+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Round 1

以下是 **Reviewer 2** 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Questions，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并引用论文中的具体 Section/Table/Figure 作为证据。

---

**Reviewer 2 Overall**: 3.0 (Findings), Soundness 3.5, Excitement 2.5

### Must-Fix:

**N1** [critical] 缺乏 wall-clock speedup——方法实际增加 6.4% 延迟
- Appendix A (Table 5) 显示 126.78 vs 119.11 ms/forward (+6.4%)
- TEAL 原论文已展示 1.53×/1.8× wall-clock speedup
- 作为 efficiency-motivated 工作，无加速数据使贡献仅限分析层面

**N2** [critical] MMLU/GSM8K 系统性退化未充分解释
- Table 2: 30% MMLU 40.7 vs 45.86, GSM8K 7.5 vs 8.79
- Qwen-14B: GSM8K −20pp
- Remove Valley 实验（Appendix T）可恢复 MMLU +3.3pp 但未追踪此线索
- "distribution-matching objectives sacrifice reasoning pathways" 是描述非解释

**N3** [critical] 与 MaskLLM 区分度不足
- 核心 recipe 完全共享：frozen model + learnable masks + KL + Gumbel
- §2 列出的 3 个差异主要是应用场景差异，非方法论创新
- 2D taxonomy 是简单分类而非 intellectual contribution

### Should-Fix:

**W1** [warning] 缺少与 R-Sparse, CATS, DIP 等 training-free 方法的实验对比
**W2** [warning] Figure 2 仅展示 global allocation 但推荐 uniform——存在误导
**W3** [warning] Conclusion 过于密集且遗漏 limitation 信号；BoolQ 出现在 Conclusion 但不在 Table 2
**W4** [warning] C1 soft-vs-hard confound 未完全解耦
**W5** [warning] Abstract 信息密度过高，第5句约60词难以一遍理解

### Questions:
1. Remove Valley 可恢复 MMLU +3.3pp，为何不作为默认配置？
2. 能否提供 uniform allocation 下的 PPL scaling 数据？
3. "14.5% PPL reduction" 是 matched (28.5%) 还是 target (30%) sparsity？
4. WikiText-103 仅 1000 steps 训练是否足够？C4 CV=6.3% 暗示过拟合？
5. §3.6 gradient coupling 发现 68% divergent masks，但 C1 说 mask patterns 是 driver 而非 coupling——关系需要更清晰阐述。

### Missing References:
1. LaRoSA (2025, arXiv:2507.01299)
2. Geva et al. (2023) 已在 bib 中但正文未引用

### Minor: M1-M7（Table 2 注释过多、ε=0.02 无 justification、Jaccard vs random baseline、MMLU 方差讨论不足、FastForward 引用更新、d_ff 排版、Table 编号检查）

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-22T17:24:00.494775+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: 缺乏 wall-clock speedup**\n\nR2 将此列为 critical，我在自己的审稿中将其列为 Should-Fix (W1)。理由如下：\n\n1. 论文在 Introduction (§1, p.2) 明确声明：\"this paper is primarily an empirical study; we do not propose a new architecture or algorithm, but rather characterize how the training objective shapes sparsity prediction quality\"，并紧接着说 \"Wall-clock speedup requires sparse kernel support; we do not address latency optimization (Appendix A)\"。论文的自我定位是分析性工作，不是系统工作。\n\n2. R2 援引 TEAL 原论文展示了 1.53×/1.8× speedup，但 TEAL 使用了 Triton semi-structured kernel——这是一个 systems-level 贡献，与 mask quality（本文关注点）正交。本文的 predictor 产生的 mask 可以直接 plug into TEAL 的 kernel pipeline（§4.1 \"predictor-TEAL\" protocol），因此 TEAL 展示的加速原则上也适用于 KL-derived masks。\n\n3. 但我同意 R2 的一个隐含观点：**论文应在主文中更清晰说明 speedup 路径**，而非仅靠 Appendix A 一段话。这是我在 W1 中提出的相同建议。\n\n判断：应为 **Should-Fix** 而非 Must-Fix。论文的贡献在于 mask quality analysis，而非 system speedup。如果将此升级为 Must-Fix，大量分析性论文（如 pruning 方法比较、distillation 目标分析）都会因 \"无端到端系统集成\" 而被拒——这不是合理的 review standard。\n\n---\n\n**[AGREE] R2-N2: MMLU/GSM8K 系统性退化未充分解释**\n\n同意这是一个需要更深入处理的问题，但我认为严重程度介于 Should-Fix 和 Must-Fix 之间。\n\n1. 论文确实在 Table 2 中展示了 30% sparsity 下 MMLU 从 45.86 (TEAL) 降至 40.7 (KL uniform)，降幅 −5.2pp。且这不是随机波动——跨三个架构一致出现（§4.6: \"the consistent regression across scales (8B MMLU −5.2pp, 14B GSM8K −20pp) suggests a systematic property of distribution-matching objectives\"）。\n\n2. R2 指出 Remove Valley（Appendix T, Table 20）可恢复 MMLU +3.3pp（40.7→44.0），说明中间层保护是 MMLU 下降的直接原因。但论文承认这以 ARC-c −4.4pp 为代价——这是 task-dependent trade-off，不是 free lunch。**然而 R2 正确指出论文未追踪这个线索**：如果 remove valley 可以恢复 reasoning 而仅损失 commonsense，为什么不探索 task-aware allocation？\n\n3. R2 对 \"distribution-matching objectives sacrifice reasoning pathways\" 的批评有道理——这是描述而非解释。论文没有给出 mechanistic explanation 为什么 forward KL 的 mode-covering 会系统性损害 reasoning neurons。\n\n我的判断：**Should-Fix to borderline Must-Fix**。不同于 N1，这个问题直接影响方法的 soundness 判断——如果 KL training 在最重要的 benchmark 上系统性退化，方法的适用性存疑。\n\n---\n\n**[REBUT] R2-N3: 与 MaskLLM 区分度不足**\n\n不同意这是 critical issue。\n\n1. **核心区别是 contextual vs static masks，这不是 \"应用场景差异\" 而是 fundamental architectural choice**。MaskLLM（§2, p.3）学习 \"fixed per-input masks\" (static N:M patterns)——每层每 token 的 mask 固定，不依赖输入。本文的 predictor 根据 x^(ℓ)（attention 后的 hidden state）动态生成 per-token masks。这意味着：\n   - MaskLLM 的 mask 无法适应 unseen inputs（论文 §2: \"MaskLLM's masks are fixed per input... must be robust to distribution shift at inference\"）\n   - 本文的 predictor 为每个 token 生成不同 mask，可以 coordinate across layers through global top-k（§3.1 Eq. 2）\n\n2. **Cross-layer allocation 是本文独有的**。MaskLLM 没有 cross-layer budget distribution（论文 §2: \"no cross-layer allocation interaction\"）。本文通过 TEAL 的 global top-k 实现 cross-layer 预算分配，这直接影响了 §4.5 中 coupling scope 的分析。\n\n3. **2D taxonomy 的价值**：同意 R2 的判断——taxonomy 本身不是 intellectual contribution，我在自己的审稿中也未将其列为优势。但 taxonomy 确实组织了 Related Work 并引出了可测试的预测（coupled > intermediate > decomposed），论文在 §4.5 中验证了这个预测。\n\n4. **Recipe 层面的共享不等于方法论重叠**。\"frozen model + learnable masks + KL\" 也是 knowledge distillation 的标准 recipe——如果这构成区分度不足，那大量 distillation 工作都不可接受。关键是 what you train (contextual predictor vs static masks)、what you optimize through (per-layer vs cross-layer)、和 what you analyze (mask pattern quality, signal-type decomposition)。\n\n判断：应降级为 **Minor** 或至多 **Should-Fix**（需要在 §2 中更清晰对比 MaskLLM 的 contribution boundary）。将其列为 Must-Fix 不合理。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: 缺少与 R-Sparse, CATS, DIP 的实验对比**\n\n部分不同意。\n\n1. 这些方法与本文不在同一设计空间内：\n   - **R-Sparse**（Zhang et al., 2025b）从 rank-aware SVD projections 预测稀疏性——不同的 predictor architecture 和 scoring mechanism\n   - **CATS**（Lee et al., 2024）adapts per-layer thresholds for SiLU/SwiGLU activation——training-free 方法，与 learned predictor 不可直接比较训练目标\n   - **DIP**（Federici et al., 2024）combines dynamic input pruning with cache-aware masking——不同的 sparsity granularity\n\n2. 论文选择 TEAL 作为 primary baseline 是合理的：TEAL 是最接近的 training-free 方法（activation-magnitude scoring + global top-k），本文的 predictor 直接替换 TEAL 的 scoring（§4.1: \"predictor-TEAL\"）。BCE baseline 覆盖了 learned predictor 的比较。\n\n3. **但 R2 有一个 valid 点**：如果 CATS 或 R-Sparse 在 MMLU/GSM8K 上不像 TEAL 那样退化，这可能说明 KL training 的 reasoning degradation 不是稀疏性的固有代价。补充一个 training-free baseline（如 CATS）的数字会增强论文的 contextualization。\n\n判断：保持 Should-Fix 级别，建议补充 1-2 个 training-free 方法的数字作为 context。\n\n---\n\n**[AGREE] R2-W2: Figure 2 仅展示 global allocation 但推荐 uniform**\n\n同意。Figure 2 caption 标注 \"(global allocation)\"，但论文在 §4.6 和 Table 2 中推荐 uniform allocation（特别是 ≤30% 时）。读者自然会用 Figure 2 理解 PPL scaling 趋势，但实际推荐的 operating point 使用不同的 allocation。建议补充 uniform allocation 的 scaling curve 或在 caption 中明确说明。\n\n---\n\n**[AGREE] R2-W3: Conclusion 密度 + BoolQ 问题**\n\n同意。Conclusion (§5) 引用了 BoolQ 数据但 BoolQ 不在 Table 2 主表中（仅在 Appendix S Table K=4 中出现且 variance 极高: std=11.5）。在 conclusion 中引用一个仅在 appendix 出现且不可靠的 metric 是不审慎的。\n\n---\n\n**[AGREE] R2-W4: C1 soft-vs-hard confound 未完全解耦**\n\n同意，且这与我自己的 N1 一致。论文在 §4.4 讨论了 BCE+Gumbel (32.22) vs standard BCE (27.97) 来 argue softness 不是主要因素，但这个比较本身也有问题：BCE+Gumbel 加了 Gumbel noise 但没有正确的 sparsity target，所以 PPL 恶化可能来自 sparsity 偏移而非 softness 本身。论文将详细讨论推到 Appendix P，但主文的 claim 强度（\"softness alone does not explain\"）需要在 Appendix 有更严格的支撑。\n\n---\n\n**[AGREE] R2-W5: Abstract 信息密度过高**\n\n同意。Abstract 第 5 句 (\"Output-distribution optimization yields masks that diverge 46–68% from magnitude-based targets; a target-swap ablation suggests these discovered patterns—not the training mechanism itself—as the proximate quality driver.\") 约 30 词包含了两个独立 claim + 一个因果声明。建议拆分为两句。\n\n---\n\n### Questions\n\n**R2-Q1: Remove Valley 为何不作为默认配置？**\n\n好问题。Appendix T (Table 20) 显示 remove valley: MMLU +3.3pp, GSM8K +1.5pp, ARC-c −4.4pp。论文将此解读为 \"task-dependent trade-off\" 但未讨论为什么不提供 task-aware 配置选项。如果用户关心 MMLU 多于 ARC-c，remove valley 就是更好的默认。这值得在论文中讨论。\n\n**R2-Q2: Uniform allocation 下的 PPL scaling 数据？**\n\n同意这是有价值的补充。Figure 2 仅展示 global，uniform 的 scaling 行为可能不同。\n\n**R2-Q3: \"14.5% PPL reduction\" 是 matched 还是 target sparsity？**\n\n这个问题在论文中有明确回答。§4.2: \"reducing TEAL's perplexity by 19% (10.82 → 8.81; 14.5% at matched 28.5% sparsity, Appendix D)\"。Abstract 也使用 \"at matched sparsity\"。14.5% 是在 matched 28.5% actual sparsity 下计算的。R2 如果读到了 §4.2 这句应该不会有此疑问——但这也侧面说明 Table 2 的呈现方式不够清晰（呼应我的 W2 和 R2 的 Q3）。\n\n**R2-Q4: WikiText-103 1000 steps 是否足够？C4 CV=6.3%？**\n\n1. Appendix B.2 (Table 8) 显示 PPL 在 step 600 时已达 95% quality (12.046 vs final 11.906)，step 800 后 Δ < 0.001。1000 steps 提供 conservative margin。\n2. C4 CV=6.3% 主要来自 seed 42 的异常值 (18.22 vs s123/s456 的 16.37)。WikiText-2 的 CV=0.2% 说明 predictor 本身稳定。C4 上较高的 variance 更可能反映 **domain shift sensitivity**（不同种子学到的 mask pattern 在 OOD 下表现差异）而非 training insufficiency。但这确实暗示 generalization 有改进空间。\n\n**R2-Q5: §3.6 gradient coupling vs C1 的关系**\n\n同意这个关系需要更清晰阐述——这也是我自己 N1 的核心关切。当前叙事的矛盾是：§3.6 argue gradient coupling 是 KL 优势的来源（通过 downstream Jacobian 耦合），但 §4.4 C1 argue mask patterns（而非 coupling）是质量驱动因素。如果 coupling 的作用仅在于 **发现** 好的 mask（training-time effect），而非 **维持** 好的 mask（inference-time effect），论文应更清晰区分这两个层面。当前的措辞（\"not the training mechanism itself\"）过于绝对。\n\n---\n\n### Missing References\n\n**R2-Ref1: LaRoSA (2025, arXiv:2507.01299)**\n\n无法评估——我不确认这篇论文是否已在 ARR 提交截止日前（2026-05-25）公开。如果是，应引用。\n\n**R2-Ref2: Geva et al. (2023)**\n\n同意应在正文中引用，如果 bib 中已有但正文未 cite，这是一个遗漏。\n\n---\n\n### Minor Issues (M1-M7)\n\n简要回应：\n- **M1 (Table 2 注释过多)**: [AGREE] Table 2 有 5 个不同的 footnote symbols (*, †, ±, ‡, §)，确实增加认知负担。\n- **M2 (ε=0.02 无 justification)**: [AGREE] §3.5 仅说 \"ε = 0.02 is a deadzone margin\" 但未解释为何选 0.02 而非其他值。\n- **M3 (Jaccard vs random baseline)**: [REBUT] 论文在 Appendix F.1 中给出了 random baseline Jaccard distance = 0.462，且在 §4.4 中比较了 cross-seed divergence (36.3%) vs KL-vs-magnitude divergence (46-68%)。这个 context 已经提供。\n- **M4-M7**: [AGREE] 均为 valid editorial improvements。\n\n---\n\n### 总结\n\nR2 的 Overall 3.0 (Findings) 比我的 3.5 (Borderline Conference) 低 0.5 分。主要分歧在于：\n\n1. **Wall-clock speedup (R2-N1)**: R2 视为 critical，我视为 Should-Fix。论文明确定位为 analysis 而非 system work，降级为 Should-Fix 更合理。\n\n2. **MaskLLM 区分度 (R2-N3)**: R2 视为 critical，我认为应为 Minor/Should-Fix。Contextual vs static masks 是 fundamental difference，不是 \"应用场景差异\"。\n\n3. **MMLU 退化 (R2-N2)**: 我们基本一致——这是一个 real 问题，介于 Should-Fix 和 Must-Fix 之间。\n\n如果 N1 和 N3 降级为 Should-Fix（我认为有充分理由），R2 的评分应上调至 3.5 左右，与我的评估一致。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: 缺乏 wall-clock speedup**\n\nR2 将此列为 critical，我在自己的审稿中将其列为 Should-Fix (W1)。理由如下：\n\n1. 论文在 Introduction (§1, p.2) 明确声明：\"this paper is primarily an empirical study; we do not propose a new architecture or algorithm, but rather characterize how the training objective shapes sparsity prediction quality\"，并紧接着说 \"Wall-clock speedup requires sparse kernel support; we do not address latency optimization (Appendix A)\"。论文的自我定位是分析性工作，不是系统工作。\n\n2. R2 援引 TEAL 原论文展示了 1.53×/1.8× speedup，但 TEAL 使用了 Triton semi-structured kernel——这是一个 systems-level 贡献，与 mask quality（本文关注点）正交。本文的 predictor 产生的 mask 可以直接 plug into TEAL 的 kernel pipeline（§4.1 \"predictor-TEAL\" protocol），因此 TEAL 展示的加速原则上也适用于 KL-derived masks。\n\n3. 但我同意 R2 的一个隐含观点：**论文应在主文中更清晰说明 speedup 路径**，而非仅靠 Appendix A 一段话。这是我在 W1 中提出的相同建议。\n\n判断：应为 **Should-Fix** 而非 Must-Fix。论文的贡献在于 mask quality analysis，而非 system speedup。如果将此升级为 Must-Fix，大量分析性论文（如 pruning 方法比较、distillation 目标分析）都会因 \"无端到端系统集成\" 而被拒——这不是合理的 review standard。\n\n---\n\n**[AGREE] R2-N2: MMLU/GSM8K 系统性退化未充分解释**\n\n同意这是一个需要更深入处理的问题，但我认为严重程度介于 Should-Fix 和 Must-Fix 之间。\n\n1. 论文确实在 Table 2 中展示了 30% sparsity 下 MMLU 从 45.86 (TEAL) 降至 40.7 (KL uniform)，降幅 −5.2pp。且这不是随机波动——跨三个架构一致出现（§4.6: \"the consistent regression across scales (8B MMLU −5.2pp, 14B GSM8K −20pp) suggests a systematic property of distribution-matching objectives\"）。\n\n2. R2 指出 Remove Valley（Appendix T, Table 20）可恢复 MMLU +3.3pp（40.7→44.0），说明中间层保护是 MMLU 下降的直接原因。但论文承认这以 ARC-c −4.4pp 为代价——这是 task-dependent trade-off，不是 free lunch。**然而 R2 正确指出论文未追踪这个线索**：如果 remove valley 可以恢复 reasoning 而仅损失 commonsense，为什么不探索 task-aware allocation？\n\n3. R2 对 \"distribution-matching objectives sacrifice reasoning pathways\" 的批评有道理——这是描述而非解释。论文没有给出 mechanistic explanation 为什么 forward KL 的 mode-covering 会系统性损害 reasoning neurons。\n\n我的判断：**Should-Fix to borderline Must-Fix**。不同于 N1，这个问题直接影响方法的 soundness 判断——如果 KL training 在最重要的 benchmark 上系统性退化，方法的适用性存疑。\n\n---\n\n**[REBUT] R2-N3: 与 MaskLLM 区分度不足**\n\n不同意这是 critical issue。\n\n1. **核心区别是 contextual vs static masks，这不是 \"应用场景差异\" 而是 fundamental architectural choice**。MaskLLM（§2, p.3）学习 \"fixed per-input masks\" (static N:M patterns)——每层每 token 的 mask 固定，不依赖输入。本文的 predictor 根据 x^(ℓ)（attention 后的 hidden state）动态生成 per-token masks。这意味着：\n   - MaskLLM 的 mask 无法适应 unseen inputs（论文 §2: \"MaskLLM's masks are fixed per input... must be robust to distribution shift at inference\"）\n   - 本文的 predictor 为每个 token 生成不同 mask，可以 coordinate across layers through global top-k（§3.1 Eq. 2）\n\n2. **Cross-layer allocation 是本文独有的**。MaskLLM 没有 cross-layer budget distribution（论文 §2: \"no cross-layer allocation interaction\"）。本文通过 TEAL 的 global top-k 实现 cross-layer 预算分配，这直接影响了 §4.5 中 coupling scope 的分析。\n\n3. **2D taxonomy 的价值**：同意 R2 的判断——taxonomy 本身不是 intellectual contribution，我在自己的审稿中也未将其列为优势。但 taxonomy 确实组织了 Related Work 并引出了可测试的预测（coupled > intermediate > decomposed），论文在 §4.5 中验证了这个预测。\n\n4. **Recipe 层面的共享不等于方法论重叠**。\"frozen model + learnable masks + KL\" 也是 knowledge distillation 的标准 recipe——如果这构成区分度不足，那大量 distillation 工作都不可接受。关键是 what you train (contextual predictor vs static masks)、what you optimize through (per-layer vs cross-layer)、和 what you analyze (mask pattern quality, signal-type decomposition)。\n\n判断：应降级为 **Minor** 或至多 **Should-Fix**（需要在 §2 中更清晰对比 MaskLLM 的 contribution boundary）。将其列为 Must-Fix 不合理。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: 缺少与 R-Sparse, CATS, DIP 的实验对比**\n\n部分不同意。\n\n1. 这些方法与本文不在同一设计空间内：\n   - **R-Sparse**（Zhang et al., 2025b）从 rank-aware SVD projections 预测稀疏性——不同的 predictor architecture 和 scoring mechanism\n   - **CATS**（Lee et al., 2024）adapts per-layer thresholds for SiLU/SwiGLU activation——training-free 方法，与 learned predictor 不可直接比较训练目标\n   - **DIP**（Federici et al., 2024）combines dynamic input pruning with cache-aware masking——不同的 sparsity granularity\n\n2. 论文选择 TEAL 作为 primary baseline 是合理的：TEAL 是最接近的 training-free 方法（activation-magnitude scoring + global top-k），本文的 predictor 直接替换 TEAL 的 scoring（§4.1: \"predictor-TEAL\"）。BCE baseline 覆盖了 learned predictor 的比较。\n\n3. **但 R2 有一个 valid 点**：如果 CATS 或 R-Sparse 在 MMLU/GSM8K 上不像 TEAL 那样退化，这可能说明 KL training 的 reasoning degradation 不是稀疏性的固有代价。补充一个 training-free baseline（如 CATS）的数字会增强论文的 contextualization。\n\n判断：保持 Should-Fix 级别，建议补充 1-2 个 training-free 方法的数字作为 context。\n\n---\n\n**[AGREE] R2-W2: Figure 2 仅展示 global allocation 但推荐 uniform**\n\n同意。Figure 2 caption 标注 \"(global allocation)\"，但论文在 §4.6 和 Table 2 中推荐 uniform allocation（特别是 ≤30% 时）。读者自然会用 Figure 2 理解 PPL scaling 趋势，但实际推荐的 operating point 使用不同的 allocation。建议补充 uniform allocation 的 scaling curve 或在 caption 中明确说明。\n\n---\n\n**[AGREE] R2-W3: Conclusion 密度 + BoolQ 问题**\n\n同意。Conclusion (§5) 引用了 BoolQ 数据但 BoolQ 不在 Table 2 主表中（仅在 Appendix S Table K=4 中出现且 variance 极高: std=11.5）。在 conclusion 中引用一个仅在 appendix 出现且不可靠的 metric 是不审慎的。\n\n---\n\n**[AGREE] R2-W4: C1 soft-vs-hard confound 未完全解耦**\n\n同意，且这与我自己的 N1 一致。论文在 §4.4 讨论了 BCE+Gumbel (32.22) vs standard BCE (27.97) 来 argue softness 不是主要因素，但这个比较本身也有问题：BCE+Gumbel 加了 Gumbel noise 但没有正确的 sparsity target，所以 PPL 恶化可能来自 sparsity 偏移而非 softness 本身。论文将详细讨论推到 Appendix P，但主文的 claim 强度（\"softness alone does not explain\"）需要在 Appendix 有更严格的支撑。\n\n---\n\n**[AGREE] R2-W5: Abstract 信息密度过高**\n\n同意。Abstract 第 5 句 (\"Output-distribution optimization yields masks that diverge 46–68% from magnitude-based targets; a target-swap ablation suggests these discovered patterns—not the training mechanism itself—as the proximate quality driver.\") 约 30 词包含了两个独立 claim + 一个因果声明。建议拆分为两句。\n\n---\n\n### Questions\n\n**R2-Q1: Remove Valley 为何不作为默认配置？**\n\n好问题。Appendix T (Table 20) 显示 remove valley: MMLU +3.3pp, GSM8K +1.5pp, ARC-c −4.4pp。论文将此解读为 \"task-dependent trade-off\" 但未讨论为什么不提供 task-aware 配置选项。如果用户关心 MMLU 多于 ARC-c，remove valley 就是更好的默认。这值得在论文中讨论。\n\n**R2-Q2: Uniform allocation 下的 PPL scaling 数据？**\n\n同意这是有价值的补充。Figure 2 仅展示 global，uniform 的 scaling 行为可能不同。\n\n**R2-Q3: \"14.5% PPL reduction\" 是 matched 还是 target sparsity？**\n\n这个问题在论文中有明确回答。§4.2: \"reducing TEAL's perplexity by 19% (10.82 → 8.81; 14.5% at matched 28.5% sparsity, Appendix D)\"。Abstract 也使用 \"at matched sparsity\"。14.5% 是在 matched 28.5% actual sparsity 下计算的。R2 如果读到了 §4.2 这句应该不会有此疑问——但这也侧面说明 Table 2 的呈现方式不够清晰（呼应我的 W2 和 R2 的 Q3）。\n\n**R2-Q4: WikiText-103 1000 steps 是否足够？C4 CV=6.3%？**\n\n1. Appendix B.2 (Table 8) 显示 PPL 在 step 600 时已达 95% quality (12.046 vs final 11.906)，step 800 后 Δ < 0.001。1000 steps 提供 conservative margin。\n2. C4 CV=6.3% 主要来自 seed 42 的异常值 (18.22 vs s123/s456 的 16.37)。WikiText-2 的 CV=0.2% 说明 predictor 本身稳定。C4 上较高的 variance 更可能反映 **domain shift sensitivity**（不同种子学到的 mask pattern 在 OOD 下表现差异）而非 training insufficiency。但这确实暗示 generalization 有改进空间。\n\n**R2-Q5: §3.6 gradient coupling vs C1 的关系**\n\n同意这个关系需要更清晰阐述——这也是我自己 N1 的核心关切。当前叙事的矛盾是：§3.6 argue gradient coupling 是 KL 优势的来源（通过 downstream Jacobian 耦合），但 §4.4 C1 argue mask patterns（而非 coupling）是质量驱动因素。如果 coupling 的作用仅在于 **发现** 好的 mask（training-time effect），而非 **维持** 好的 mask（inference-time effect），论文应更清晰区分这两个层面。当前的措辞（\"not the training mechanism itself\"）过于绝对。\n\n---\n\n### Missing References\n\n**R2-Ref1: LaRoSA (2025, arXiv:2507.01299)**\n\n无法评估——我不确认这篇论文是否已在 ARR 提交截止日前（2026-05-25）公开。如果是，应引用。\n\n**R2-Ref2: Geva et al. (2023)**\n\n同意应在正文中引用，如果 bib 中已有但正文未 cite，这是一个遗漏。\n\n---\n\n### Minor Issues (M1-M7)\n\n简要回应：\n- **M1 (Table 2 注释过多)**: [AGREE] Table 2 有 5 个不同的 footnote symbols (*, †, ±, ‡, §)，确实增加认知负担。\n- **M2 (ε=0.02 无 justification)**: [AGREE] §3.5 仅说 \"ε = 0.02 is a deadzone margin\" 但未解释为何选 0.02 而非其他值。\n- **M3 (Jaccard vs random baseline)**: [REBUT] 论文在 Appendix F.1 中给出了 random baseline Jaccard distance = 0.462，且在 §4.4 中比较了 cross-seed divergence (36.3%) vs KL-vs-magnitude divergence (46-68%)。这个 context 已经提供。\n- **M4-M7**: [AGREE] 均为 valid editorial improvements。\n\n---\n\n### 总结\n\nR2 的 Overall 3.0 (Findings) 比我的 3.5 (Borderline Conference) 低 0.5 分。主要分歧在于：\n\n1. **Wall-clock speedup (R2-N1)**: R2 视为 critical，我视为 Should-Fix。论文明确定位为 analysis 而非 system work，降级为 Should-Fix 更合理。\n\n2. **MaskLLM 区分度 (R2-N3)**: R2 视为 critical，我认为应为 Minor/Should-Fix。Contextual vs static masks 是 fundamental difference，不是 \"应用场景差异\"。\n\n3. **MMLU 退化 (R2-N2)**: 我们基本一致——这是一个 real 问题，介于 Should-Fix 和 Must-Fix 之间。\n\n如果 N1 和 N3 降级为 Should-Fix（我认为有充分理由），R2 的评分应上调至 3.5 左右，与我的评估一致。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-22T17:24:05.114048+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4619
}
```

</details>

---


### Assistant

_source line 1268 · 2026-05-22T17:24:13.356481+00:00_

交叉回应已提交。核心分歧点：

1. **R2-N1 (wall-clock speedup)**: 我反驳其 critical 级别——论文明确定位为 empirical analysis 而非 system work，应为 Should-Fix
2. **R2-N3 (MaskLLM 区分度)**: 我反驳——contextual vs static masks 是 fundamental architectural difference，非 "应用场景差异"
3. **R2-N2 (MMLU 退化)**: 基本同意，认为介于 Should-Fix 和 Must-Fix 之间
4. 其余 Should-Fix 和 Questions 大部分同意 R2 的判断，特别是 W2 (Figure 2 误导)、W3 (Conclusion BoolQ)、W4 (C1 confound) 与我自己的审稿一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 40

## Round 40

70 recorded events


### User

_source line 1269 · 2026-05-22T23:39:24.941104+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查**方法严谨性和实验设计**。

## Venue 信息
- **目标**: EMNLP 2026 (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL template ([review] option), double-blind
- **页数限制**: 8 页正文 + unlimited references; Limitations/Ethics 不计页数
- **匿名规则**: double-blind（作者匿名为 "Anonymous"）

## 论文路径
- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf`

## 你的审查侧重

### 方法严谨性
1. **KL Distillation 框架**：Gumbel-Sigmoid 放松、forward KL 选择的理论/实验依据、geometric penalty schedule 的收敛性
2. **C1 Target-Swap Ablation**：实验设计是否足以支撑 "mask patterns carry most quality information" 的声明？oracle mask provenance（s42 早期 checkpoint vs s123/s456 matched retrained）是否引入 confound？
3. **Per-layer KL 2D 分解**：K=1 和 K=4 控制实验的 train-inference mismatch confound 处理是否充分？"signal type dominates PPL (upper bound)" 声明的强度是否合理？
4. **统计严谨性**：3-seed mean±std 的充分性、seed 选择偏差风险、高方差指标（ARC-c σ=3.6, BoolQ σ=11.5）的处理

### 实验设计
5. **Baselines 公平性**：BCE iso-compute 比较（1000 vs 2700 步）、MSE baseline 配置、TEAL comparison 的 actual sparsity mismatch
6. **评估覆盖度**：WikiText-2/C4 PPL + 6 下游任务是否足够？sequence length 2048 的限制性？缺少 batched inference 评估？
7. **跨架构泛化**：Mistral-7B 和 Qwen-14B 结果是否充分支持泛化声明？14B GSM8K -20pp 的系统性退步是否被充分讨论？
8. **Reproducibility**：实验细节是否完整（超参、硬件、数据处理）？

请按 ARR 标准给出：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，按严重性排列：Critical > Warning > Minor) → Questions → Missing References → Overall Assessment (1-5 分，参照 EMNLP 2026 ARR 评分标准)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-22T23:39:32.372546+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-22T23:39:32.372890+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-22T23:39:37.792189+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-22T23:39:37.892954+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-22T23:39:41.021579+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1275 · 2026-05-22T23:39:43.453884+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
  "pages": "1-8",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
    "pages": "1-8",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1276 · 2026-05-22T23:39:48.557620+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may al
…[truncated 1144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7536
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-22T23:39:49.664152+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.9}], \"total_pages\": 19, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6210
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-22T23:39:56.189676+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria including all scoring dimensions, their scales, and descriptions. I need the exact fields reviewers must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria including all scoring dimensions, their scales, and descriptions. I need the exact fields reviewers must fill in."
  }
}
```

</details>

---


### Tool call

_source line 1279 · 2026-05-22T23:39:56.692698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-22T23:39:57.601327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-22T23:39:58.055896+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-22T23:39:58.056486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1283 · 2026-05-22T23:39:58.560139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1284 · 2026-05-22T23:39:58.863230+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-22T23:39:59.570996+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1514
}
```

</details>

---


### Tool result

_source line 1286 · 2026-05-22T23:39:59.925671+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1365
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-22T23:40:08.416694+00:00_

# ACL Rolling Review Form - Complete Criteria

## Primary Review Dimensions

**1. Paper Summary**
Reviewers describe the paper's topic to clarify understanding and identify misinterpretations.

**2. Summary of Strengths**
Evaluators identify reasons for publication: "novel and useful methodology, insightful empirical results or theoretical analysis, clear organization."

**3. Summary of Weaknesses**
Concerns warranting deprioritization, numbered for author response, covering "correctness of the results or argumentation, limited perceived impact."

**4. Comments/Suggestions/Typos**
Additional improvement recommendations beyond addressing major concerns.

**5. Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; careful reading and familiarity with related work
- 1: Outside expertise area or paper difficult to understand

**6. Soundness** (1-5 scale, with half-point increments)
Assessment of scientific rigor, experimental validity, and adequate claim support. "This study provides sufficient support for all of its claims" rates as 4.

**7. Excitement** (1-5 scale, with half-point increments)
Subjective assessment of "transformational/innovative/surprising" qualities or community impact.

**8. Overall Assessment** (1-5 scale, with half-point increments)
Recommendation ranging from "Consider for Award" (5) to "Do not resubmit" (1).

## Additional Required Evaluations

- **Best Paper Justification** (conditional)
- **Limitations and Societal Impact**
- **Ethical Concerns**
- **Needs Ethics Review** (binary assessment)
- **Reproducibility** (1-5 scale)
- **Datasets** (1-5 scale, if applicable)
- **Software** (1-5 scale, if applicable)
- **Author Identity Knowledge** (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 12227
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-22T23:40:16.746725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1289 · 2026-05-22T23:40:17.354207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-22T23:40:17.682870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-22T23:40:19.343778+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2597
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-22T23:40:19.344236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-22T23:40:19.696812+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2013
}
```

</details>

---


### Tool result

_source line 1294 · 2026-05-22T23:40:20.202167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2847
}
```

</details>

---


### Tool call

_source line 1295 · 2026-05-22T23:40:20.353101+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
  "pages": "9-19",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
    "pages": "9-19",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1296 · 2026-05-22T23:40:20.707894+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-22T23:40:22.718777+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 560.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 597.7}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 594.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.1}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p17.png\", \"wid
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2365
}
```

</details>

---


### Tool call

_source line 1298 · 2026-05-22T23:40:27.084938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-22T23:40:28.038922+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-22T23:40:28.139822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-22T23:40:28.742944+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1302 · 2026-05-22T23:40:28.793520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1303 · 2026-05-22T23:40:29.144972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1304 · 2026-05-22T23:40:29.948084+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-22T23:40:29.949233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-22T23:40:29.949715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1307 · 2026-05-22T23:40:30.253624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1308 · 2026-05-22T23:40:31.111818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1162
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-22T23:40:31.817174+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1563
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-22T23:40:39.952999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1311 · 2026-05-22T23:40:40.506597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-22T23:40:41.160913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1313 · 2026-05-22T23:40:41.918841+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1965
}
```

</details>

---


### Tool call

_source line 1314 · 2026-05-22T23:40:42.172359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1315 · 2026-05-22T23:40:42.172768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1316 · 2026-05-22T23:40:42.427472+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1920
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-22T23:40:42.632783+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1471
}
```

</details>

---


### Tool result

_source line 1318 · 2026-05-22T23:40:44.098103+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1925
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-22T23:40:44.673919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2501
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-22T23:40:52.183135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-22T23:40:52.585100+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-22T23:40:52.585497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-22T23:40:52.636278+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-22T23:40:58.859792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-22T23:40:59.211475+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (max $\Delta$$\leq$0.79pp, 3-seed).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at 30\% (upper bound; not fully orthogonal with coupling scope).
6	Cross-layer coupling contributes 29--97\% on downstream tasks (3-seed $K{=}4$-corrected): coupling-dominated for commonsense (ARC-c 97\%, WG 67\%) and mismatch-dominated for reasoning (GSM8K 29\%).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-22T23:40:59.211853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-22T23:41:00.165753+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	While MaskLLM~\cite{fang2024maskllm} applies KL-based mask optimization, it targets static N:M weight sparsity; activation sparsity requires masks that generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation suggests that KL-discovered mask targets carry most of the quality information at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.2
…[truncated 2952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-22T23:41:00.166289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-22T23:41:00.216868+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the dominant design dimension for PPL (signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes 29--97\% on downstream tasks (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-22T23:41:00.769162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-22T23:41:00.819715+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-22T23:41:08.748621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-22T23:41:09.602245+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 36747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-22T23:41:09.602709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-22T23:41:09.703396+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-
…[truncated 5170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-22T23:46:46.652180+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿报告：方法严谨性与实验设计\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## Summary\n\n本文用 forward KL divergence + Gumbel-Sigmoid 松弛训练 SwiGLU FFN 稀疏预测器，替代传统 BCE per-neuron 独立目标。在 LLaMA-3.1-8B 上 30%/50% 稀疏度下相比 TEAL 和 BCE baseline 取得显著 PPL 优势，并通过 C1 target-swap ablation 和 per-layer KL 控制实验分解了信号类型（output-distribution vs. intermediate）和耦合范围对性能的贡献。论文定位为经验研究而非提出新架构，分析深度值得肯定，但几项关键分析存在未解决的 confound，知识密集型任务系统性退步限制了实用性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 KL vs BCE 对比可靠（效应量大、多 seed），但 per-layer 分解存在 train-inference mismatch confound，C1 ablation 有残余 confound |\n| Excitement | 2.5/5 | 无新方法/算法/架构（作者自述），KL+Gumbel-Sigmoid 均为已有技术；无 wall-clock 加速；核心发现（KL 优于 BCE）有价值但属预期范围 |\n| Reproducibility | 4.0/5 | 超参、架构、硬件细节完整，训练/评估协议清晰，但无代码/数据释放声明 |\n| Reviewer Confidence | 4/5 | 熟悉稀疏性预测、KD、SwiGLU 相关文献 |\n| **Overall Assessment** | **3.0** | **Findings 级别**：经验发现有价值，分析深度突出，但 per-layer 分解的 confound 削弱关键贡献，缺乏实际加速，知识任务系统性退步限制影响力 |\n\n---\n\n## Strengths\n\n**S1. 核心对比可靠且效应量大。**\nKL vs BCE 的 PPL 差距在 30%（8.81 vs 11.25）和 50%（11.84 vs 28.13）均超过 25%，3-seed 方差极低（KL σ=0.02 at 30%），跨架构（Mistral-7B -17.3%）一致。这不是边界效应，而是实质性差异。\n\n**S2. C1 target-swap ablation 是创造性的实验设计。**\n将 KL 发现的 mask 作为 BCE 训练目标（Table 3），分离 mask 质量 vs. 训练动态的贡献。s123/s456 的匹配实验（gap ≤0.03pp at 30%）令人信服。这一分析设计在稀疏性预测文献中是新颖的。\n\n**S3. 消融覆盖广泛且控制严格。**\nTable 4 系统比较 5 种 loss（forward KL, reverse KL, JSD, BCE, MSE）× 2 种松弛（Gumbel, STE），MSE baseline 除 loss 外完全一致（Appendix G 详述）。附录提供 d_b 敏感性（Appendix B）、温度 schedule（B.1）、训练收敛（B.2）、补偿网络冗余（J），形成完整的 hyperparameter robustness 图景。\n\n**S4. 论文对自身局限性的透明度高于平均水平。**\n明确标注 per-layer 分解为 \"upper bound\"（§4.5），承认 C1 的 s42 oracle 来自早期 checkpoint（Table 3 脚注），Limitations 逐条列出 seq length、batched inference、知识任务退步等。这种诚实度值得肯定。\n\n**S5. 2D taxonomy（Table 1）提供有用的组织框架。**\ncorrection granularity × training signal coupling 的分类法清晰定位了本文贡献，尽管框架本身较简单。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [Critical] Per-layer KL 分解存在根本性 confound，定量结论不可靠**\n\n- **具体位置**: §4.5, Table 4（ablation rows: per-layer KL K=1, K=4）, Abstract line 5-6, Conclusion line 1\n- **问题**: \n  (a) K=1 控制实验在训练时仅 mask 1/32 层，推理时 mask 全部 32 层，存在 32× 的 train-inference mismatch。论文承认这是 \"upper bound\"，但 Abstract 和 Conclusion 仍将 \"signal type accounts for the majority of the PPL gap\" 作为核心贡献之一呈现，未充分传达 upper bound 的资格限定。\n  (b) K=4 控制实验出现反常结果：50% 稀疏度下 K=4 (PPL 44.23) **显著差于** K=1 (PPL 34.85)，差距达 27%。更多训练上下文（4 层 vs 1 层 masked）反而导致更差性能，这与 \"K 越大越接近 E2E\" 的直觉相矛盾。论文仅描述现象（\"coupling scope dominates at high sparsity, reversing the 30% pattern\"），但未提供机制解释——为什么在 50% 时同时 mask 4 层会比 mask 1 层更差？\n  (c) K=4 在 30% 时 MMLU 超过 E2E（42.7 vs 40.7），论文归因于 allocation matching（Appendix S 注释），但这意味着 K=4 与 E2E 的差异中混入了 allocation 效应，进一步污染了 coupling scope 的估计。\n  (d) 缺少 K=8, K=16 等中间值。仅两个数据点（K=1, K=4）无法拟合 coupling scope 的单调趋势，更无法支撑 \"29-97% on downstream tasks\" 的精确分解数字。\n- **为什么影响接收**: 信号类型 vs 耦合范围的分解是论文三大贡献之一（Introduction bullet 1）。如果这一分解不可靠，论文的分析深度主张大幅削弱。\n- **建议修改方向**: (1) 在 Abstract/Conclusion 中明确标注 \"upper bound\" 限定，不应呈现为确定性结论；(2) 增加 K=8/K=16 实验或承认仅有两个数据点不足以做定量分解；(3) 对 50% K=4 < K=1 的反常提供假设性解释（如 gradient interference、sparsity compounding）。\n\n**N2 [Critical] 知识密集型任务系统性退步缺乏机制分析**\n\n- **具体位置**: Table 2（MMLU: KL 40.7 vs TEAL 45.86 at 30%），Table 14/Appendix K（Qwen-14B GSM8K -20pp），Limitations paragraph 2\n- **问题**: KL 在所有测试规模和架构上均系统性地低于 TEAL 的 MMLU/GSM8K 性能：\n  - 8B 30%: MMLU -5.2pp（40.7 vs 45.86）\n  - 8B 30% global: MMLU -10.2pp（35.7 vs 45.86），σ=9.5\n  - 14B 30% uniform: MMLU -2.8pp（63.55 vs 66.34），GSM8K -20.1pp（32.0 vs 52.1）\n  \n  论文推测 \"distribution-matching objectives systematically sacrifice reasoning-critical pathways\"，但这仅是事后叙事，无实验支撑。§4.4 的 per-layer sparsity 分析（L14-L18 protection valley）提供了一个数据点（Remove valley: MMLU +3.4pp, Table 20），但没有回答根本问题：为什么 KL 的 output-distribution 目标会学到一个牺牲知识路径的 allocation pattern？是 WikiText-103 训练数据的偏差？是 forward KL 的固有特性？还是 Gumbel-Sigmoid 的采样偏差？\n- **为什么影响接收**: MMLU 和 GSM8K 是 LLM 评估的核心指标。如果方法在这些指标上系统性退步，实际应用场景将严重受限。仅报告退步而不提供分析，对于定位为 \"characterize how the training objective shapes sparsity prediction quality\" 的论文来说是一个显著空白。\n- **建议修改方向**: (1) 分析 KL 和 TEAL 在知识密集型层（Meng et al., 2022 的知识神经元）上的 mask 差异；(2) 用不同训练数据（如包含更多 reasoning 内容的数据）测试退步是否缓解；(3) 至少在 Discussion 中提供更具体的假设和未来验证路径。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [Warning] C1 ablation 残余 confound 未完全控制**\n\n- **具体位置**: §4.4 \"Soft-vs-Hard Confound\" 段落, Table 3, Appendix P\n- **问题**: C1 同时改变了两个变量：(a) 训练目标（KL mask → BCE mask），(b) mask 表示（soft Gumbel → hard binary）。论文用 BCE+Gumbel（PPL 32.22）vs standard BCE（27.97）论证 softness 不解释 KL 优势，但这一对比使用的是 magnitude-based targets，不能直接推广到 KL-derived targets。此外，oracle mask 提取过程（从连续 Gumbel 分数到二值化 logits > 0）可能丢失排序信息，而这些信息在 TEAL global top-k 排序中可能有用。\n- **建议**: 明确讨论 oracle 提取时信息损失的可能性，或增加一个使用连续 KL 分数（非二值化）训练 BCE 的对比实验。\n\n**W2 [Warning] 无 wall-clock 加速，实际影响受限**\n\n- **具体位置**: Appendix A（Table 5: +6.4% overhead），Limitations\n- **问题**: Predictor 增加 6.4% 推理延迟，无稀疏内核支持。所有 PPL 改进在实际部署中不带来速度收益。论文定位为 empirical study 避开了这一点，但这意味着论文的直接实际价值有限——仅当未来有稀疏内核适配时才有价值。\n- **建议**: 至少在 Discussion 中讨论稀疏内核的可行性估算（如 Triton block-sparse 能否支持 unstructured element-wise masks？如果不能，需要 structured sparsity 适配，这又是一个未验证的步骤）。\n\n**W3 [Warning] 评估覆盖度存在关键空白**\n\n- **具体位置**: §4.1 Evaluation 段落, Limitations\n- **问题**: \n  (a) 所有下游任务均为 classification/multiple-choice 格式，无生成任务评估（MT-Bench, AlpacaEval 等）。稀疏预测对自回归生成质量的影响可能与 classification 不同。\n  (b) 序列长度固定 2048。现代 LLM 应用场景常用 8K-128K 上下文。稀疏 pattern 可能随序列长度变化（长序列中 attention pattern 变化可能影响 FFN 稀疏性）。\n  (c) Batched inference 未评估。实际部署中多序列需取 mask 交集，可能显著降低有效稀疏度。\n- **建议**: 补充至少一项生成任务评估，或明确讨论 classification-only 评估的局限性。\n\n**W4 [Warning] 高方差指标的统计可靠性不足**\n\n- **具体位置**: Table 2（ARC-c σ=3.6 at 30% global），Appendix R（BoolQ σ=11.5）\n- **问题**: ARC-c σ=3.6pp 意味着 95% CI 宽度约为 ±8.9pp（t 分布, df=2），BoolQ σ=11.5pp 更甚。在 3 seed 下，这些指标的均值差异基本不可解释。Table 4 (ablation) 多行仅有 s42 单 seed 数据（Per-layer KL K=1 50%: 34.85, BCE variants 50%: 27.97/32.22/38.02/60.54），无法评估可靠性。\n- **建议**: (1) 在正文中对高方差指标加注 \"differences not statistically significant\"；(2) ablation table 关键行补充 3-seed 数据，至少 forward KL + Gumbel 和 BCE 两行。\n\n**W5 [Warning] Geometric penalty schedule 在 30% 目标下偏差较大**\n\n- **具体位置**: Appendix C（Table 9: 30% target → 28.5% actual, 5% deviation），§3.5 Eq. 7\n- **问题**: ε=0.02 的 deadzone 设计意味着实际稀疏度 28.5%（retention 71.5%）距目标 30%（retention 70.0%）的偏差 |71.5%-70%|=1.5pp < ε=2pp，落入 deadzone 内，λ 不再增长。因此 30% 目标永远无法精确达到——这是 schedule 设计的固有限制而非收敛不足。论文在 Appendix C 处理了 matched sparsity comparison（TEAL at 28.5% → PPL 10.30 vs KL 8.96），但 main text Table 2 标注 \"30%\" 可能误导读者。\n- **建议**: Table 2 注释应更醒目地标注实际稀疏度（目前 ‡ 脚注存在但不够显眼）。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2 中 BCE 30% 使用 global allocation（脚注 †），但未提供 BCE 30% uniform 的对比，使读者无法在同一 allocation 策略下比较 BCE 与 KL。建议补充或说明省略原因。\n- §3.5 称 \"geometric penalty schedule\"，实际实现是 augmented penalty method with geometric λ update rule。术语不影响理解但不够精确。\n- Abstract 第 3 句 \"reduces perplexity by 14.5% over TEAL at matched sparsity\" 的 \"matched sparsity\" 指 28.5% 而非名义 30%，这一资格限定在 abstract 中容易被忽略。\n- Appendix G（MSE baseline）提到 seed 123 出现 catastrophic failure（PPL=15,789），但 MSE 的 3-seed 报告仍包含了可能在该 seed 上偏好的结果（仅排除了灾难 seed 后用剩余两个有效 seed）。MSE 3-seed mean 的计算方式应澄清。\n- 无代码/数据/模型释放声明。对于定位为 empirical study 的论文，reproducibility 需要代码可用。\n\n---\n\n## Questions for Authors\n\n**Q1.** Per-layer KL K=4 在 50% 时为何比 K=1 差？是否有 gradient interference 或 optimization landscape 方面的解释？增加 K 是否单调恶化，还是存在 sweet spot？\n\n**Q2.** 知识密集型退步是否与 WikiText-103 训练数据有关？如果用包含 Wikipedia + 数学/代码数据的混合语料训练，MMLU/GSM8K 退步是否缓解？\n\n**Q3.** C1 oracle 提取时使用 logits > 0 二值化。是否尝试过保留连续分数（如直接用 KL predictor 输出作为 BCE 回归目标）？信息损失是否可量化？\n\n**Q4.** STE 在 30% 仅达到 20.8% effective sparsity（§4.5 STE Failure 段落）。是否调整过 STE 的 learning rate 或 gradient scaling？如果 STE 达到了目标稀疏度，其 PPL 如何？\n\n**Q5.** Table 2 中 MSE 50% 报告 PPL=229.26（仅 s42），Appendix G 显示 s123 catastrophic（PPL=15,789）。MSE 30% 的 3-seed mean 18.52±1.68 是否包含了所有 3 个 seed，还是也排除了部分失败 seed？\n\n---\n\n## Missing References\n\n- Meng et al., 2022 \"Locating and Editing Factual Associations in GPT\" — 与知识密集型退步的讨论直接相关，可用于分析 KL masks 在知识存储层的行为。\n- Li et al., 2023 \"Inference with Reference: Lossless Acceleration of Large Language Models\" — 与 contextual sparsity prediction 路线相关但未讨论的加速方法。\n- 论文已引用的 MaskLLM (Fang et al., 2024) 仅在 Related Work 中讨论，未做实验对比。虽然 static N:M vs contextual sparsity 确有差异，但 KL+Gumbel 的共享方法论使得读者自然期待某种程度的对比或讨论。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n核心发现（KL 显著优于 BCE 用于稀疏预测训练）可靠且有价值，target-swap ablation 设计巧妙。但论文存在以下主要问题：(1) per-layer 分解是三大贡献之一，却因 train-inference mismatch confound 和 K=4 反常结果而不可靠；(2) 知识密集型任务系统性退步缺乏分析深度；(3) 无实际加速。论文分析详尽、写作透明，适合 Findings track；Conference 接收需解决 per-layer 分解的 confound 并提供知识退步的机制分析。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿报告：方法严谨性与实验设计\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May 2026)\n**审查侧重**: 方法严谨性 + 实验设计\n\n---\n\n## Summary\n\n本文用 forward KL divergence + Gumbel-Sigmoid 松弛训练 SwiGLU FFN 稀疏预测器，替代传统 BCE per-neuron 独立目标。在 LLaMA-3.1-8B 上 30%/50% 稀疏度下相比 TEAL 和 BCE baseline 取得显著 PPL 优势，并通过 C1 target-swap ablation 和 per-layer KL 控制实验分解了信号类型（output-distribution vs. intermediate）和耦合范围对性能的贡献。论文定位为经验研究而非提出新架构，分析深度值得肯定，但几项关键分析存在未解决的 confound，知识密集型任务系统性退步限制了实用性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 核心 KL vs BCE 对比可靠（效应量大、多 seed），但 per-layer 分解存在 train-inference mismatch confound，C1 ablation 有残余 confound |\n| Excitement | 2.5/5 | 无新方法/算法/架构（作者自述），KL+Gumbel-Sigmoid 均为已有技术；无 wall-clock 加速；核心发现（KL 优于 BCE）有价值但属预期范围 |\n| Reproducibility | 4.0/5 | 超参、架构、硬件细节完整，训练/评估协议清晰，但无代码/数据释放声明 |\n| Reviewer Confidence | 4/5 | 熟悉稀疏性预测、KD、SwiGLU 相关文献 |\n| **Overall Assessment** | **3.0** | **Findings 级别**：经验发现有价值，分析深度突出，但 per-layer 分解的 confound 削弱关键贡献，缺乏实际加速，知识任务系统性退步限制影响力 |\n\n---\n\n## Strengths\n\n**S1. 核心对比可靠且效应量大。**\nKL vs BCE 的 PPL 差距在 30%（8.81 vs 11.25）和 50%（11.84 vs 28.13）均超过 25%，3-seed 方差极低（KL σ=0.02 at 30%），跨架构（Mistral-7B -17.3%）一致。这不是边界效应，而是实质性差异。\n\n**S2. C1 target-swap ablation 是创造性的实验设计。**\n将 KL 发现的 mask 作为 BCE 训练目标（Table 3），分离 mask 质量 vs. 训练动态的贡献。s123/s456 的匹配实验（gap ≤0.03pp at 30%）令人信服。这一分析设计在稀疏性预测文献中是新颖的。\n\n**S3. 消融覆盖广泛且控制严格。**\nTable 4 系统比较 5 种 loss（forward KL, reverse KL, JSD, BCE, MSE）× 2 种松弛（Gumbel, STE），MSE baseline 除 loss 外完全一致（Appendix G 详述）。附录提供 d_b 敏感性（Appendix B）、温度 schedule（B.1）、训练收敛（B.2）、补偿网络冗余（J），形成完整的 hyperparameter robustness 图景。\n\n**S4. 论文对自身局限性的透明度高于平均水平。**\n明确标注 per-layer 分解为 \"upper bound\"（§4.5），承认 C1 的 s42 oracle 来自早期 checkpoint（Table 3 脚注），Limitations 逐条列出 seq length、batched inference、知识任务退步等。这种诚实度值得肯定。\n\n**S5. 2D taxonomy（Table 1）提供有用的组织框架。**\ncorrection granularity × training signal coupling 的分类法清晰定位了本文贡献，尽管框架本身较简单。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [Critical] Per-layer KL 分解存在根本性 confound，定量结论不可靠**\n\n- **具体位置**: §4.5, Table 4（ablation rows: per-layer KL K=1, K=4）, Abstract line 5-6, Conclusion line 1\n- **问题**: \n  (a) K=1 控制实验在训练时仅 mask 1/32 层，推理时 mask 全部 32 层，存在 32× 的 train-inference mismatch。论文承认这是 \"upper bound\"，但 Abstract 和 Conclusion 仍将 \"signal type accounts for the majority of the PPL gap\" 作为核心贡献之一呈现，未充分传达 upper bound 的资格限定。\n  (b) K=4 控制实验出现反常结果：50% 稀疏度下 K=4 (PPL 44.23) **显著差于** K=1 (PPL 34.85)，差距达 27%。更多训练上下文（4 层 vs 1 层 masked）反而导致更差性能，这与 \"K 越大越接近 E2E\" 的直觉相矛盾。论文仅描述现象（\"coupling scope dominates at high sparsity, reversing the 30% pattern\"），但未提供机制解释——为什么在 50% 时同时 mask 4 层会比 mask 1 层更差？\n  (c) K=4 在 30% 时 MMLU 超过 E2E（42.7 vs 40.7），论文归因于 allocation matching（Appendix S 注释），但这意味着 K=4 与 E2E 的差异中混入了 allocation 效应，进一步污染了 coupling scope 的估计。\n  (d) 缺少 K=8, K=16 等中间值。仅两个数据点（K=1, K=4）无法拟合 coupling scope 的单调趋势，更无法支撑 \"29-97% on downstream tasks\" 的精确分解数字。\n- **为什么影响接收**: 信号类型 vs 耦合范围的分解是论文三大贡献之一（Introduction bullet 1）。如果这一分解不可靠，论文的分析深度主张大幅削弱。\n- **建议修改方向**: (1) 在 Abstract/Conclusion 中明确标注 \"upper bound\" 限定，不应呈现为确定性结论；(2) 增加 K=8/K=16 实验或承认仅有两个数据点不足以做定量分解；(3) 对 50% K=4 < K=1 的反常提供假设性解释（如 gradient interference、sparsity compounding）。\n\n**N2 [Critical] 知识密集型任务系统性退步缺乏机制分析**\n\n- **具体位置**: Table 2（MMLU: KL 40.7 vs TEAL 45.86 at 30%），Table 14/Appendix K（Qwen-14B GSM8K -20pp），Limitations paragraph 2\n- **问题**: KL 在所有测试规模和架构上均系统性地低于 TEAL 的 MMLU/GSM8K 性能：\n  - 8B 30%: MMLU -5.2pp（40.7 vs 45.86）\n  - 8B 30% global: MMLU -10.2pp（35.7 vs 45.86），σ=9.5\n  - 14B 30% uniform: MMLU -2.8pp（63.55 vs 66.34），GSM8K -20.1pp（32.0 vs 52.1）\n  \n  论文推测 \"distribution-matching objectives systematically sacrifice reasoning-critical pathways\"，但这仅是事后叙事，无实验支撑。§4.4 的 per-layer sparsity 分析（L14-L18 protection valley）提供了一个数据点（Remove valley: MMLU +3.4pp, Table 20），但没有回答根本问题：为什么 KL 的 output-distribution 目标会学到一个牺牲知识路径的 allocation pattern？是 WikiText-103 训练数据的偏差？是 forward KL 的固有特性？还是 Gumbel-Sigmoid 的采样偏差？\n- **为什么影响接收**: MMLU 和 GSM8K 是 LLM 评估的核心指标。如果方法在这些指标上系统性退步，实际应用场景将严重受限。仅报告退步而不提供分析，对于定位为 \"characterize how the training objective shapes sparsity prediction quality\" 的论文来说是一个显著空白。\n- **建议修改方向**: (1) 分析 KL 和 TEAL 在知识密集型层（Meng et al., 2022 的知识神经元）上的 mask 差异；(2) 用不同训练数据（如包含更多 reasoning 内容的数据）测试退步是否缓解；(3) 至少在 Discussion 中提供更具体的假设和未来验证路径。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [Warning] C1 ablation 残余 confound 未完全控制**\n\n- **具体位置**: §4.4 \"Soft-vs-Hard Confound\" 段落, Table 3, Appendix P\n- **问题**: C1 同时改变了两个变量：(a) 训练目标（KL mask → BCE mask），(b) mask 表示（soft Gumbel → hard binary）。论文用 BCE+Gumbel（PPL 32.22）vs standard BCE（27.97）论证 softness 不解释 KL 优势，但这一对比使用的是 magnitude-based targets，不能直接推广到 KL-derived targets。此外，oracle mask 提取过程（从连续 Gumbel 分数到二值化 logits > 0）可能丢失排序信息，而这些信息在 TEAL global top-k 排序中可能有用。\n- **建议**: 明确讨论 oracle 提取时信息损失的可能性，或增加一个使用连续 KL 分数（非二值化）训练 BCE 的对比实验。\n\n**W2 [Warning] 无 wall-clock 加速，实际影响受限**\n\n- **具体位置**: Appendix A（Table 5: +6.4% overhead），Limitations\n- **问题**: Predictor 增加 6.4% 推理延迟，无稀疏内核支持。所有 PPL 改进在实际部署中不带来速度收益。论文定位为 empirical study 避开了这一点，但这意味着论文的直接实际价值有限——仅当未来有稀疏内核适配时才有价值。\n- **建议**: 至少在 Discussion 中讨论稀疏内核的可行性估算（如 Triton block-sparse 能否支持 unstructured element-wise masks？如果不能，需要 structured sparsity 适配，这又是一个未验证的步骤）。\n\n**W3 [Warning] 评估覆盖度存在关键空白**\n\n- **具体位置**: §4.1 Evaluation 段落, Limitations\n- **问题**: \n  (a) 所有下游任务均为 classification/multiple-choice 格式，无生成任务评估（MT-Bench, AlpacaEval 等）。稀疏预测对自回归生成质量的影响可能与 classification 不同。\n  (b) 序列长度固定 2048。现代 LLM 应用场景常用 8K-128K 上下文。稀疏 pattern 可能随序列长度变化（长序列中 attention pattern 变化可能影响 FFN 稀疏性）。\n  (c) Batched inference 未评估。实际部署中多序列需取 mask 交集，可能显著降低有效稀疏度。\n- **建议**: 补充至少一项生成任务评估，或明确讨论 classification-only 评估的局限性。\n\n**W4 [Warning] 高方差指标的统计可靠性不足**\n\n- **具体位置**: Table 2（ARC-c σ=3.6 at 30% global），Appendix R（BoolQ σ=11.5）\n- **问题**: ARC-c σ=3.6pp 意味着 95% CI 宽度约为 ±8.9pp（t 分布, df=2），BoolQ σ=11.5pp 更甚。在 3 seed 下，这些指标的均值差异基本不可解释。Table 4 (ablation) 多行仅有 s42 单 seed 数据（Per-layer KL K=1 50%: 34.85, BCE variants 50%: 27.97/32.22/38.02/60.54），无法评估可靠性。\n- **建议**: (1) 在正文中对高方差指标加注 \"differences not statistically significant\"；(2) ablation table 关键行补充 3-seed 数据，至少 forward KL + Gumbel 和 BCE 两行。\n\n**W5 [Warning] Geometric penalty schedule 在 30% 目标下偏差较大**\n\n- **具体位置**: Appendix C（Table 9: 30% target → 28.5% actual, 5% deviation），§3.5 Eq. 7\n- **问题**: ε=0.02 的 deadzone 设计意味着实际稀疏度 28.5%（retention 71.5%）距目标 30%（retention 70.0%）的偏差 |71.5%-70%|=1.5pp < ε=2pp，落入 deadzone 内，λ 不再增长。因此 30% 目标永远无法精确达到——这是 schedule 设计的固有限制而非收敛不足。论文在 Appendix C 处理了 matched sparsity comparison（TEAL at 28.5% → PPL 10.30 vs KL 8.96），但 main text Table 2 标注 \"30%\" 可能误导读者。\n- **建议**: Table 2 注释应更醒目地标注实际稀疏度（目前 ‡ 脚注存在但不够显眼）。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 2 中 BCE 30% 使用 global allocation（脚注 †），但未提供 BCE 30% uniform 的对比，使读者无法在同一 allocation 策略下比较 BCE 与 KL。建议补充或说明省略原因。\n- §3.5 称 \"geometric penalty schedule\"，实际实现是 augmented penalty method with geometric λ update rule。术语不影响理解但不够精确。\n- Abstract 第 3 句 \"reduces perplexity by 14.5% over TEAL at matched sparsity\" 的 \"matched sparsity\" 指 28.5% 而非名义 30%，这一资格限定在 abstract 中容易被忽略。\n- Appendix G（MSE baseline）提到 seed 123 出现 catastrophic failure（PPL=15,789），但 MSE 的 3-seed 报告仍包含了可能在该 seed 上偏好的结果（仅排除了灾难 seed 后用剩余两个有效 seed）。MSE 3-seed mean 的计算方式应澄清。\n- 无代码/数据/模型释放声明。对于定位为 empirical study 的论文，reproducibility 需要代码可用。\n\n---\n\n## Questions for Authors\n\n**Q1.** Per-layer KL K=4 在 50% 时为何比 K=1 差？是否有 gradient interference 或 optimization landscape 方面的解释？增加 K 是否单调恶化，还是存在 sweet spot？\n\n**Q2.** 知识密集型退步是否与 WikiText-103 训练数据有关？如果用包含 Wikipedia + 数学/代码数据的混合语料训练，MMLU/GSM8K 退步是否缓解？\n\n**Q3.** C1 oracle 提取时使用 logits > 0 二值化。是否尝试过保留连续分数（如直接用 KL predictor 输出作为 BCE 回归目标）？信息损失是否可量化？\n\n**Q4.** STE 在 30% 仅达到 20.8% effective sparsity（§4.5 STE Failure 段落）。是否调整过 STE 的 learning rate 或 gradient scaling？如果 STE 达到了目标稀疏度，其 PPL 如何？\n\n**Q5.** Table 2 中 MSE 50% 报告 PPL=229.26（仅 s42），Appendix G 显示 s123 catastrophic（PPL=15,789）。MSE 30% 的 3-seed mean 18.52±1.68 是否包含了所有 3 个 seed，还是也排除了部分失败 seed？\n\n---\n\n## Missing References\n\n- Meng et al., 2022 \"Locating and Editing Factual Associations in GPT\" — 与知识密集型退步的讨论直接相关，可用于分析 KL masks 在知识存储层的行为。\n- Li et al., 2023 \"Inference with Reference: Lossless Acceleration of Large Language Models\" — 与 contextual sparsity prediction 路线相关但未讨论的加速方法。\n- 论文已引用的 MaskLLM (Fang et al., 2024) 仅在 Related Work 中讨论，未做实验对比。虽然 static N:M vs contextual sparsity 确有差异，但 KL+Gumbel 的共享方法论使得读者自然期待某种程度的对比或讨论。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n核心发现（KL 显著优于 BCE 用于稀疏预测训练）可靠且有价值，target-swap ablation 设计巧妙。但论文存在以下主要问题：(1) per-layer 分解是三大贡献之一，却因 train-inference mismatch confound 和 K=4 反常结果而不可靠；(2) 知识密集型任务系统性退步缺乏分析深度；(3) 无实际加速。论文分析详尽、写作透明，适合 Findings track；Conference 接收需解决 per-layer 分解的 confound 并提供知识退步的机制分析。\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-22T23:46:50.328878+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3676
}
```

</details>

---


### Assistant

_source line 1338 · 2026-05-22T23:47:01.018085+00:00_

审稿报告已提交给 Review Director。

核心结论：**Overall 3.0（Findings 级别）**。

主要问题：
1. **Per-layer KL 分解的 confound**（N1 Critical）：K=1 有 32× train-inference mismatch，K=4 在 50% 时反常地差于 K=1（44.23 vs 34.85），仅两个 K 值不足以支撑定量分解。
2. **知识任务系统性退步无机制解释**（N2 Critical）：MMLU/GSM8K 在所有规模/架构上均退步（8B -5.2pp MMLU, 14B -20pp GSM8K），仅有事后推测。

核心优势：KL vs BCE 的效应量大且稳健（PPL 差 2-2.4×），C1 target-swap ablation 设计巧妙，消融覆盖广泛，论文对局限性高度透明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 41

## Round 41

8 recorded events


### User

_source line 1339 · 2026-05-22T23:47:36.869215+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿报告（新颖性与完整性）

**Overall**: 3.0 / 5 — Findings

### Must-Fix 问题

**N1** [critical] 核心贡献与 MaskLLM 的新颖性区分不充分
- MaskLLM (Fang et al., 2024, NeurIPS 2024 Spotlight) 已提出 KL divergence + Gumbel relaxation 训练可学习 sparsity masks 的范式。本文声称的区别是：(a) contextual vs. static masks, (b) activation sparsity vs. N:M weight sparsity, (c) cross-layer coupling analysis。但 (a) 和 (b) 属于 sparsity setting 的差异而非训练方法论的创新——核心 recipe（KL on output distributions + differentiable mask sampling）完全一致。论文 Section 2 仅用一句话提到 MaskLLM。

**N2** [critical] "Dominant design dimension" claim overclaimed
- 该 claim 仅基于两种 signal type 的对比：BCE vs forward KL。论文未测试 Reverse KL、JSD、MSE on logits/hidden states、cosine similarity 等。在仅比较两种方法的情况下声称 "dominant"，逻辑上不成立。此外 Table 3 中 BCE+Gumbel (32.22) vs standard BCE (27.97) 说明 Gumbel relaxation 本身也是重要因素。

**N3** [critical] 实验规模单一，削弱 generalizability claim
- 核心实验全部基于 LLaMA-3.1-8B；跨架构实验仅在 Appendix。Qwen-2.5-14B 无 C1 ablation 或 gradient SNR 分析。无 70B+ 模型实验。

### Should-Fix 问题

**W1** [warning] 无 wall-clock speedup 结果
**W2** [warning] 训练数据过于有限（WikiText-103, 1000 步）
**W3** [warning] 2D Taxonomy 贡献度有限——post-hoc 归类，未填充空白组合
**W4** [warning] Gumbel-Sigmoid relaxation 的贡献被低估/混淆——KL 方法同时使用 Gumbel，而 BCE baseline 使用 hard threshold，引入混淆变量

### 遗漏的相关工作
1. SparseInfer (Li et al., 2024)
2. GRASP (DAC 2025)
3. TurboSparse (Song et al., 2024)
4. Universal Properties of Activation Sparsity (2025)

### 主要优势
1. §3.6 梯度分析是真正的分析性贡献
2. C1 target-swap ablation 设计精巧
3. 实验覆盖面宽
4. 定位诚实
5. Predictor 设计高效

---

请对上述每个 N1-N3、W1-W4 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-22T23:48:20.904576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
  "offset": "0",
  "limit": "48"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
    "offset": "0",
    "limit": "48"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-22T23:48:21.356675+00:00_

0	\section{Related Work}
1	
2	\paragraph{Training-Free Activation Sparsity.}
3	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
4	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
5	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
6	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-p
…[truncated 5169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-22T23:48:21.407283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": "122",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "offset": "122",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1343 · 2026-05-22T23:48:21.457979+00:00_

122	\subsection{Ablation Studies}
123	
124	Table~\ref{tab:ablation} isolates the contribution of each design choice at 30\% and 50\% sparsity.
125	
126	\begin{table}[t]
127	\centering
128	\caption{Ablation on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$; uniform at 30\%, global at 50\%). $\pm$: 3-seed; unmarked: s42. $^\ddagger$STE: 20.8\% actual sparsity at 30\% target (\S\ref{sec:ablation_ste}). $^\S$MSE 50\%: s42 only; s123 catastrophic (PPL{=}15{,}789; Appendix~\ref{app:mse_config}).}
129	\label{tab:ablation}
130	\resizebox{\columnwidth}{!}{
131	\begin{tabular}{lccc}
132	\toprule
133	Configuration & 30\% PPL$\downarrow$ & 50\% PPL$\downarrow$ & $\Delta_{50}$ \\
134	\midrule
135	\multicolumn{4}{l}{\textit{KL-based variants}} \\
136	Forward KL + Gumbel (Ours) & \textbf{8.81$\pm$0.02} & \textbf{11.79} & --- \\ % exp_id: kl30_ablation_s42, bench_kl50_global
137	JSD (symmetric) + Gumbel & 8.90$\pm$0.02 & 12.54 & +0.75 \\ % exp_id: jsd30_ablation_s42, jsd_ablation_s42
138	Reverse KL + Gumbel & 9.26$\pm$0.07 & 12.80 & +1.01 \\ % exp_id: rkl30_ablation_s42, reverse_kl_ablation_s42
139	Forward KL + STE & ---$^\ddagger$ & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
140	\midrule
141	\multicolumn{4}{l}{\textit{Per-layer training}} \\
142	Per-layer MSE & 18.52$\pm$1.68 & 229.26$^\S$ & +217.47 \\ % exp_id: mse30_uniform_s42, mse50_uniform_s42
143	Per-layer KL ($K{=}1$) & 9.05$\pm$0.02 & 34.85 & +23.06 \\ % exp_id: perlayer_kl_30_3seed, perlayer_kl_50_s42
144	Per-layer KL ($K{=}4$) & 8.89$\pm$0.01 & 44.23 & +32.44 \\ % exp_id: perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42
145	\midrule
146	\multicolumn{4}{l}{\textit{BCE-based variants}} \\
147	BCE (no compensation) & 15.71 & 27.97 & +16.18 \\ % exp_id: bce30_uniform_s42, eval_bce_v3_s42
148	BCE + Gumbel (no penalty) & --- & 32.22 & +20.43 \\ % exp_id: bce_gumbel_no_penalty_s42
149	BCE + Gumbel + Penalty & --- & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
150	BCE + STE & --- & 60.54 & +48.75 \\ % exp_id: bce_ste_s42
15
…[truncated 3666 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-22T23:49:39.412081+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 的逐条回应\n\n---\n\n### N1: 核心贡献与 MaskLLM 的新颖性区分不充分\n\n**[REBUT]** R2 称 \"论文 Section 2 仅用一句话提到 MaskLLM\"——这与原文不符。Section 2 (Related Work) 用 **4 句话**（related_work.tex lines 19-23）详细讨论 MaskLLM，明确列出三个维度的差异：(a) static N:M vs per-token contextual masks, (b) 无 cross-layer allocation interaction vs TEAL global top-k coordination, (c) weight masks input-independent vs activation masks 需 distribution shift robustness。\n\n更重要的是，R2 低估了 contextual vs static 的差异。MaskLLM 学习 **固定的** N:M weight masks（每个 mask 是 Gumbel-Softmax 采样的 static pattern），不需要泛化到未见输入。本文的 predictor 必须从 $\\mathbf{x}^{(\\ell)}$ **实时预测** per-token masks 并在 OOD 数据上保持性能（Appendix D, Table 10: C4 下游 Δ≤1.1pp）。这不仅是 \"sparsity setting 的差异\"，而是根本不同的学习问题——one is parameter optimization, the other is function approximation。\n\n但我同意 R2 的一个隐含观点：论文应在 Introduction 中更早、更清晰地定位与 MaskLLM 的关系，而不是仅在 Related Work 中讨论。这是 framing 问题，不是 novelty 缺失。\n\n---\n\n### N2: \"Dominant design dimension\" claim overclaimed\n\n**[REBUT]** R2 声称 \"论文未测试 Reverse KL、JSD、MSE\"——这与原文 **直接矛盾**。Table 4 (§4.5 Ablation Studies) 明确对比了 **5 种 loss function**：\n\n| Loss | 30% PPL | 50% PPL |\n|------|---------|---------|\n| Forward KL + Gumbel | **8.81±0.02** | **11.79** |\n| JSD + Gumbel | 8.90±0.02 | 12.54 |\n| Reverse KL + Gumbel | 9.26±0.07 | 12.80 |\n| Per-layer MSE | 18.52±1.68 | 229.26 |\n| BCE | 15.71 | 27.97 |\n\nForward KL、Reverse KL、JSD（对称）、MSE（intermediate activations）、BCE（decomposed）——涵盖了 R2 要求的所有 divergence measure 类型。R2 的 \"仅比较两种方法\" 断言是事实性错误。\n\n关于 Gumbel confound：论文 §4.5 \"STE Failure and Loss-Relaxation Interaction\" 已精确量化——loss effect (ΔPPL=20.4) 是 relaxation effect (ΔPPL=3.98) 的 **5.1×**（experiments.tex line 168）。此外，MSE baseline 使用 **完全相同的** Gumbel-Sigmoid 松弛（Appendix G, appendix.tex line 239），因此 KL vs MSE 的对比完全控制了 relaxation 变量。\n\n不过，我在自己的审稿中指出（R1-N1），\"dominant\" 这一 claim 的定量基础（per-layer 分解的 signal type vs coupling scope 百分比）确实因 train-inference mismatch confound 而不够可靠。但 R2 给出的理由是错误的——不是因为缺少对比，而是因为分解方法学的 confound。\n\n---\n\n### N3: 实验规模单一，削弱 generalizability claim\n\n**[AGREE]** R2 的核心观点成立：跨架构证据是 preliminary 的。Mistral-7B 和 Qwen-14B 仅有 main results，无 C1 ablation、per-layer 分解或 SNR 分析。我在 R1 审稿中也指出了类似问题（R1-W3 评估覆盖度）。\n\n不过，两点补充：\n1. 论文明确自称 \"primarily an empirical study\"（Introduction, introduction.tex line 18），Conclusion 也标注 \"evaluation bounded at 7-14B\"。作者对这一局限是诚实的。\n2. 要求 70B+ 实验需考虑计算成本——论文使用单卡 RTX PRO 6000（96GB）训练，70B+ 模型的 predictor 训练可能超出合理的审稿修改范围。但至少应在 Discussion 中讨论 scaling 预期。\n\n这一不足是 **影响评分但非一票否决** 的问题——将 generalization claims 限定在已验证的 7-14B 范围内即可。升级到 critical 级别过于严格。\n\n---\n\n### W1: 无 wall-clock speedup 结果\n\n**[AGREE]** 与我的审稿意见 R1-W2 一致。Predictor 增加 6.4% latency overhead（Appendix A, Table 5），无稀疏内核支持。论文透明但影响力受限。\n\n---\n\n### W2: 训练数据过于有限（WikiText-103, 1000 步）\n\n**[REBUT]** R2 未充分考虑论文已提供的 OOD 证据：\n- Appendix D (Table 8): C4 validation PPL 保持 KL 优势（50%: 18.40 vs TEAL 38.75，与 WikiText-2 的 50% advantage 一致）\n- Appendix D (Table 10): 用 C4 text 生成 mask（OOD calibration），6 个下游任务 Δ≤1.1pp\n- Appendix B.2 (Table 7): 训练在 600 步即收敛 95%，1000 步提供保守余量\n\nWikiText-103 作为训练数据确实是限制（Limitations 段落 3 已承认，特别提到 cross-seed variance 在 C4 上升至 CV=6.3%），但 R2 的措辞 \"过于有限\" 忽略了已有的泛化验证。这是一个已被适当讨论的 limitation，不是 experimental oversight。\n\n---\n\n### W3: 2D Taxonomy 贡献度有限\n\n**[AGREE]** Taxonomy（Table 1）是 post-hoc 组织框架而非实验发现。论文也未声称它是 key contribution——Introduction 的 4 个 bullet points 未包含 taxonomy。这是一个 minor organizational contribution，R2 的评价合理。\n\n---\n\n### W4: Gumbel-Sigmoid relaxation 的贡献被低估/混淆\n\n**[REBUT]** 如 N2 回应所述，论文已显式控制了这一 confound：\n\n1. **BCE vs BCE+Gumbel**（Table 4）：BCE 27.97 → BCE+Gumbel 32.22，Gumbel 在 BCE 上反而 **恶化** 性能。这排除了 \"Gumbel 本身解释 KL 优势\" 的假说。\n2. **Forward KL+Gumbel vs Forward KL+STE**（Table 4）：11.79 vs 15.77，relaxation effect = ΔPPL 3.98。\n3. **Loss effect vs relaxation effect**：ΔPPL 20.4 vs 3.98，loss 是 relaxation 的 **5.1×**（§4.5）。\n4. **MSE 使用相同 Gumbel**（Appendix G, appendix.tex line 239）：KL vs MSE 完全控制了 relaxation 变量。\n\nR2 的 \"引入混淆变量\" 判断未考虑论文已提供的消融证据。这一 confound 被充分控制。\n\n---\n\n### R2 遗漏的相关工作评论\n\nR2 列出 4 篇遗漏引用，其中两篇论文 **已被引用**：\n- **SparseInfer** (Shin et al., 2025)：Section 2 line 4 已引用（related_work.tex: \"SparseInfer~\\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs\"）\n- **TurboSparse** (Song et al., 2024)：Section 2 line 31 已引用（related_work.tex: \"TurboSparse~\\cite{song2024turbosparse} and ProSparse~\\cite{song2025prosparse}\"）\n\nR2 可能未仔细阅读 Related Work section。GRASP (DAC 2025) 和 \"Universal Properties\" (2025) 可补充但非 critical omission。\n\n---\n\n### 总结\n\nR2 的 N2 和 W4 基于 **事实性错误**（遗漏 Table 4 的 5-loss 对比和 §4.5 的 confound 量化），应降级或撤回。N1 的 MaskLLM 讨论量也被低估（实际 4 句而非 1 句），但 Introduction framing 可改善。N3 和 W1 有效但严重性适中。W2 忽略了已有的 OOD 验证。W3 合理。\n\nR2 遗漏相关工作列表中两篇已被论文引用，反映了阅读不够仔细，可能影响其他判断的可靠性。\n",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 的逐条回应\n\n---\n\n### N1: 核心贡献与 MaskLLM 的新颖性区分不充分\n\n**[REBUT]** R2 称 \"论文 Section 2 仅用一句话提到 MaskLLM\"——这与原文不符。Section 2 (Related Work) 用 **4 句话**（related_work.tex lines 19-23）详细讨论 MaskLLM，明确列出三个维度的差异：(a) static N:M vs per-token contextual masks, (b) 无 cross-layer allocation interaction vs TEAL global top-k coordination, (c) weight masks input-independent vs activation masks 需 distribution shift robustness。\n\n更重要的是，R2 低估了 contextual vs static 的差异。MaskLLM 学习 **固定的** N:M weight masks（每个 mask 是 Gumbel-Softmax 采样的 static pattern），不需要泛化到未见输入。本文的 predictor 必须从 $\\mathbf{x}^{(\\ell)}$ **实时预测** per-token masks 并在 OOD 数据上保持性能（Appendix D, Table 10: C4 下游 Δ≤1.1pp）。这不仅是 \"sparsity setting 的差异\"，而是根本不同的学习问题——one is parameter optimization, the other is function approximation。\n\n但我同意 R2 的一个隐含观点：论文应在 Introduction 中更早、更清晰地定位与 MaskLLM 的关系，而不是仅在 Related Work 中讨论。这是 framing 问题，不是 novelty 缺失。\n\n---\n\n### N2: \"Dominant design dimension\" claim overclaimed\n\n**[REBUT]** R2 声称 \"论文未测试 Reverse KL、JSD、MSE\"——这与原文 **直接矛盾**。Table 4 (§4.5 Ablation Studies) 明确对比了 **5 种 loss function**：\n\n| Loss | 30% PPL | 50% PPL |\n|------|---------|---------|\n| Forward KL + Gumbel | **8.81±0.02** | **11.79** |\n| JSD + Gumbel | 8.90±0.02 | 12.54 |\n| Reverse KL + Gumbel | 9.26±0.07 | 12.80 |\n| Per-layer MSE | 18.52±1.68 | 229.26 |\n| BCE | 15.71 | 27.97 |\n\nForward KL、Reverse KL、JSD（对称）、MSE（intermediate activations）、BCE（decomposed）——涵盖了 R2 要求的所有 divergence measure 类型。R2 的 \"仅比较两种方法\" 断言是事实性错误。\n\n关于 Gumbel confound：论文 §4.5 \"STE Failure and Loss-Relaxation Interaction\" 已精确量化——loss effect (ΔPPL=20.4) 是 relaxation effect (ΔPPL=3.98) 的 **5.1×**（experiments.tex line 168）。此外，MSE baseline 使用 **完全相同的** Gumbel-Sigmoid 松弛（Appendix G, appendix.tex line 239），因此 KL vs MSE 的对比完全控制了 relaxation 变量。\n\n不过，我在自己的审稿中指出（R1-N1），\"dominant\" 这一 claim 的定量基础（per-layer 分解的 signal type vs coupling scope 百分比）确实因 train-inference mismatch confound 而不够可靠。但 R2 给出的理由是错误的——不是因为缺少对比，而是因为分解方法学的 confound。\n\n---\n\n### N3: 实验规模单一，削弱 generalizability claim\n\n**[AGREE]** R2 的核心观点成立：跨架构证据是 preliminary 的。Mistral-7B 和 Qwen-14B 仅有 main results，无 C1 ablation、per-layer 分解或 SNR 分析。我在 R1 审稿中也指出了类似问题（R1-W3 评估覆盖度）。\n\n不过，两点补充：\n1. 论文明确自称 \"primarily an empirical study\"（Introduction, introduction.tex line 18），Conclusion 也标注 \"evaluation bounded at 7-14B\"。作者对这一局限是诚实的。\n2. 要求 70B+ 实验需考虑计算成本——论文使用单卡 RTX PRO 6000（96GB）训练，70B+ 模型的 predictor 训练可能超出合理的审稿修改范围。但至少应在 Discussion 中讨论 scaling 预期。\n\n这一不足是 **影响评分但非一票否决** 的问题——将 generalization claims 限定在已验证的 7-14B 范围内即可。升级到 critical 级别过于严格。\n\n---\n\n### W1: 无 wall-clock speedup 结果\n\n**[AGREE]** 与我的审稿意见 R1-W2 一致。Predictor 增加 6.4% latency overhead（Appendix A, Table 5），无稀疏内核支持。论文透明但影响力受限。\n\n---\n\n### W2: 训练数据过于有限（WikiText-103, 1000 步）\n\n**[REBUT]** R2 未充分考虑论文已提供的 OOD 证据：\n- Appendix D (Table 8): C4 validation PPL 保持 KL 优势（50%: 18.40 vs TEAL 38.75，与 WikiText-2 的 50% advantage 一致）\n- Appendix D (Table 10): 用 C4 text 生成 mask（OOD calibration），6 个下游任务 Δ≤1.1pp\n- Appendix B.2 (Table 7): 训练在 600 步即收敛 95%，1000 步提供保守余量\n\nWikiText-103 作为训练数据确实是限制（Limitations 段落 3 已承认，特别提到 cross-seed variance 在 C4 上升至 CV=6.3%），但 R2 的措辞 \"过于有限\" 忽略了已有的泛化验证。这是一个已被适当讨论的 limitation，不是 experimental oversight。\n\n---\n\n### W3: 2D Taxonomy 贡献度有限\n\n**[AGREE]** Taxonomy（Table 1）是 post-hoc 组织框架而非实验发现。论文也未声称它是 key contribution——Introduction 的 4 个 bullet points 未包含 taxonomy。这是一个 minor organizational contribution，R2 的评价合理。\n\n---\n\n### W4: Gumbel-Sigmoid relaxation 的贡献被低估/混淆\n\n**[REBUT]** 如 N2 回应所述，论文已显式控制了这一 confound：\n\n1. **BCE vs BCE+Gumbel**（Table 4）：BCE 27.97 → BCE+Gumbel 32.22，Gumbel 在 BCE 上反而 **恶化** 性能。这排除了 \"Gumbel 本身解释 KL 优势\" 的假说。\n2. **Forward KL+Gumbel vs Forward KL+STE**（Table 4）：11.79 vs 15.77，relaxation effect = ΔPPL 3.98。\n3. **Loss effect vs relaxation effect**：ΔPPL 20.4 vs 3.98，loss 是 relaxation 的 **5.1×**（§4.5）。\n4. **MSE 使用相同 Gumbel**（Appendix G, appendix.tex line 239）：KL vs MSE 完全控制了 relaxation 变量。\n\nR2 的 \"引入混淆变量\" 判断未考虑论文已提供的消融证据。这一 confound 被充分控制。\n\n---\n\n### R2 遗漏的相关工作评论\n\nR2 列出 4 篇遗漏引用，其中两篇论文 **已被引用**：\n- **SparseInfer** (Shin et al., 2025)：Section 2 line 4 已引用（related_work.tex: \"SparseInfer~\\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs\"）\n- **TurboSparse** (Song et al., 2024)：Section 2 line 31 已引用（related_work.tex: \"TurboSparse~\\cite{song2024turbosparse} and ProSparse~\\cite{song2025prosparse}\"）\n\nR2 可能未仔细阅读 Related Work section。GRASP (DAC 2025) 和 \"Universal Properties\" (2025) 可补充但非 critical omission。\n\n---\n\n### 总结\n\nR2 的 N2 和 W4 基于 **事实性错误**（遗漏 Table 4 的 5-loss 对比和 §4.5 的 confound 量化），应降级或撤回。N1 的 MaskLLM 讨论量也被低估（实际 4 句而非 1 句），但 Introduction framing 可改善。N3 和 W1 有效但严重性适中。W2 忽略了已有的 OOD 验证。W3 合理。\n\nR2 遗漏相关工作列表中两篇已被论文引用，反映了阅读不够仔细，可能影响其他判断的可靠性。\n",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-22T23:49:42.925337+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3513
}
```

</details>

---


### Assistant

_source line 1346 · 2026-05-22T23:50:00.356948+00:00_

已向 Director 提交对 Reviewer 2 的逐条回应。主要结论：

- **N2、W4**：基于事实性错误（R2 遗漏了 Table 4 的 5-loss 对比和 §4.5 的 confound 量化），应降级或撤回
- **N1**：MaskLLM 讨论量被 R2 低估（4 句非 1 句），但 Introduction framing 确可改善
- **N3、W1**：有效但严重性适中
- **W2**：忽略了论文已有的 OOD 验证
- **W3**：合理

另外指出 R2 遗漏相关工作列表中 SparseInfer 和 TurboSparse 已被论文引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 42

## Round 42

72 recorded events


### User

_source line 1347 · 2026-05-23T00:34:03.887082+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**。

## Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: Long paper，8 页正文限制（不含 references/limitations/ethics），ACL 模板 (acl.sty)
- **匿名规则**: Double-blind
- **评分标准**: ARR Overall Assessment 1-5 分（4=Conference，3.5=Borderline Conference，3=Findings）

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- 各章节: 同目录下 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex

## 你的审查侧重

### 1. 方法论严谨性
- KL divergence 公式（forward KL 选择的理论依据是否充分）
- Gumbel-Sigmoid relaxation 的数学推导是否正确
- Geometric Penalty Schedule 是否是合理的 sparsity 控制方案
- §3.6 梯度分析——BCE vs KL 对比是否公正、严谨

### 2. 实验设计
- 控制变量是否充分（KL vs BCE vs MSE 的 fair comparison：同架构、同数据、同步数）
- 统计显著性：哪些结果是 3-seed，哪些仅 s42？confidence interval 是否足够窄？
- Per-layer KL 分解（§4.5 "Per-Layer KL: Decomposing Signal Type and Coupling Scope"）——K=1 的 32x train-inference mismatch confound 是否被充分讨论？K=4 是否真正 deconfound？
- C1 target-swap ablation（§4.3）——soft→hard 二值化是否引入了额外 confound？oracle mask 来自单一训练轨迹是否是问题？
- Cross-architecture（Mistral-7B, Qwen-14B）——14B 仅单 seed 是否足够？GSM8K -20pp 是否被充分分析？

### 3. 关键数字审计
- Table 1 main results：检查 PPL 和 downstream 数字是否自洽
- Table 3 C1 ablation：max Δ≤0.79pp 的声明是否被数据支持（注意 30% s42 gap=0.65pp 但使用了不同 checkpoint）
- Table 4 ablation：检查 Δ 列计算
- TEAL baseline 的公平性：TEAL 是 deterministic 的，但 actual sparsity 不同（28.5% vs 29.3%），matched comparison 是否充分

### 4. 可复现性
- 训练细节是否足够（lr, optimizer, batch size, seq_len 都有）
- 代码是否承诺释放？
- 硬件描述是否充分

请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-23T00:34:10.963537+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-23T00:34:12.372681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-23T00:34:17.040594+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1351 · 2026-05-23T00:34:19.249272+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1352 · 2026-05-23T00:34:33.828080+00:00_

Web search results for query: "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) reviewer guidelines and criteria for 2025-2026:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Reviewer Requirements and Guidelines

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## New Policies for 2025

Starting from May 2025, ACL introduces the awards policy for reviewers & chairs, where area chairs or senior area chairs may nominate great reviewers. Additionally, starting in May 2025, ARR adopts a new policy on 'highly irresponsible' (meta-)r
…[truncated 643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 16787
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-23T00:34:35.187294+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 15938
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-23T00:34:40.508576+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-23T00:34:40.659270+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-23T00:34:45.627854+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, review form dimensions, and scoring scales. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) with their exact scales and descriptions. 2) What reviewers are expected to evaluate. 3) Any specific guidance on how to assign scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, review form dimensions, and scoring scales. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) with their exact scales and descriptions. 2) What reviewers are expected to evaluate. 3) Any specific guidance on how to assign scores."
  }
}
```

</details>

---


### Tool call

_source line 1357 · 2026-05-23T00:34:46.682136+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-23T00:34:47.786392+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1359 · 2026-05-23T00:34:48.288389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-23T00:34:49.344659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1361 · 2026-05-23T00:34:49.796806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-23T00:34:50.249213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1363 · 2026-05-23T00:34:51.208602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-23T00:34:51.714382+00:00_

# ARR Reviewer Scoring Criteria

## Scoring Dimensions

Based on the guidelines, ARR uses **three primary scoring dimensions** (as of February 2025):

1. **Soundness** - Assesses technical validity and rigor
2. **Excitement** - Reflects personal interest and subjective appeal
3. **Overall Recommendation** - Composite assessment for venue suitability

## Scoring Expectations

### Soundness
Reviewers must justify low soundness scores with specific review content. The guidelines emphasize: *"low Soundness score without finding any major faults means your review is not a faithful explanation"* of the recommendation.

### Excitement
Described as orthogonal to soundness, this captures *"our personal taste"* separate from technical merit. A paper can be sound but personally unexciting.

### Overall Assessment
This composite score reflects *"soundness, excitement, and also other factors like novelty and impact."* Papers for main conferences must be "sufficiently sound and reproducible," but excitement need not be present—a resource or efficiency contribution may deserve acceptance despite lower personal interest.

## Evaluation Expectations

Reviewers assess:
- Technical correctness and methodology
- Clarity and specificity of claims
- Novelty and contribution significance
- Reproducibility details
- Appropriate scope and limitations
- Professional tone and constructive feedback

The guidelines note that all scores must align with the written review content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6086
}
```

</details>

---


### Tool call

_source line 1365 · 2026-05-23T00:34:51.714857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-23T00:34:52.267371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-23T00:34:52.923272+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 429.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 329.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 369.1}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p19.png\", \"w
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6241
}
```

</details>

---


### Tool result

_source line 1368 · 2026-05-23T00:34:57.003257+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8714
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-23T00:34:57.155520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7810
}
```

</details>

---


### Tool result

_source line 1370 · 2026-05-23T00:34:57.156647+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4889
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-23T00:34:57.258992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6050
}
```

</details>

---


### Tool result

_source line 1372 · 2026-05-23T00:34:57.262138+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 9475
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-23T00:34:57.263192+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5548
}
```

</details>

---


### Tool result

_source line 1374 · 2026-05-23T00:34:57.266245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7469
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-23T00:34:57.267385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7018
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-23T00:35:04.726195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1377 · 2026-05-23T00:35:05.230233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-23T00:35:05.631978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-23T00:35:06.639381+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1913
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-23T00:35:06.639848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1381 · 2026-05-23T00:35:07.495709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-23T00:35:07.547236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-23T00:35:08.859624+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3629
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-23T00:35:08.860097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1385 · 2026-05-23T00:35:09.716366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-23T00:35:09.716778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-23T00:35:10.423274+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4791
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-23T00:35:10.423684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1389 · 2026-05-23T00:35:11.077119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1390 · 2026-05-23T00:35:11.131468+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4491
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-23T00:35:13.093986+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5598
}
```

</details>

---


### Tool result

_source line 1392 · 2026-05-23T00:35:13.095169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5547
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-23T00:35:13.650182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3933
}
```

</details>

---


### Tool result

_source line 1394 · 2026-05-23T00:35:14.104404+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 5244
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-23T00:35:14.105225+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4388
}
```

</details>

---


### Tool result

_source line 1396 · 2026-05-23T00:35:14.107197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3030
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-23T00:35:14.208840+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3785
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-23T00:35:24.116827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-23T00:35:24.671792+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-23T00:35:24.672290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-23T00:35:26.230604+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1558
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-23T00:35:34.989180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-23T00:35:35.391412+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 36747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-23T00:35:35.391753+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-23T00:35:35.542527+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Our evaluation focuses on perplexity and multiple-choice benchmarks; open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-23T00:35:35.894142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1407 · 2026-05-23T00:35:36.346115+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (max $\Delta$$\leq$0.79pp, 3-seed).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at 30\% (upper bound; not fully orthogonal with coupling scope).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-23T00:35:36.346620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-23T00:35:36.898919+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation suggests that KL-discovered mask targets carry most of the quality information at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Cross-
…[truncated 2908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-23T00:35:36.950223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1411 · 2026-05-23T00:35:37.051069+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for PPL (signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes task-dependently---substantially for commonsense, marginally for reasoning (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	Code and trained predictors will be released upon acceptance.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-23T00:39:59.677260+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 3.5/5\n**Excitement**: 3/5\n**Confidence**: 4/5（仔细验证了所有关键数字和公式）\n\n**一句话总结**: 扎实的实证研究，证明了 output-distribution alignment（forward KL）显著优于 per-neuron BCE 来训练 sparsity predictor，C1 target-swap ablation 设计巧妙；但系统性的 knowledge-task regression、coupling decomposition 的 confounds、以及缺乏 wall-clock speedup 限制了贡献。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | KL 公式正确，Gumbel-Sigmoid 标准，ablation 设计巧妙。但 coupling decomposition 有未解决的 confounds（K=4 anomaly），sparsity controller 在 30% target 饱和未达目标 |\n| Excitement | 3/5 | 填补了 training objective for sparsity predictor 的文献空白，C1 ablation 有洞察力；但缺乏 wall-clock speedup 和系统性 knowledge regression 限制实际影响 |\n| Reproducibility | 4/5 | 训练细节充分（lr, optimizer, batch size, seq_len, hardware），承诺 release code；但 seed 覆盖不完整（14B 单 seed） |\n| Overall | 3.5/5 | 介于 Conference 和 Findings 之间；若能修复关键问题可达 Conference |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Per-layer KL K=4 在 50% sparsity 的反常行为削弱 coupling decomposition 的可信度\n\n- 具体位置：§4.5 (Table 4, Per-layer KL K=4 行)\n- 问题：K=4 per-layer KL 在 50% sparsity 的 PPL 为 44.23，**劣于** K=1 的 34.85，而 E2E KL 为 11.84。如果 coupling 是有益的，增加 masked layers 数量（K=1→K=4）应缩小与 E2E 的差距，但实际上差距扩大了（+23.06→+32.44）。论文给出的解释是 \"gradient interference\"（§4.5 倒数第二段），但这是纯粹的 speculation，没有任何实验验证。\n- 为什么影响接收：该反常行为直接动摇了 §4.5 signal type vs. coupling scope decomposition 的核心叙事。如果 K=4 的行为无法被解释，那么基于 K=1 和 K=4 的 decomposition percentages（如 \"PPL 67% closure\"）的可靠性也存疑。论文的一个主要 contribution 是这个 decomposition，但它在更高 sparsity 下失效。\n- 建议修改方向：(1) 增加 K=2, K=8, K=16 的实验以追踪 PPL 随 K 的变化趋势；(2) 或者限制 decomposition 分析仅在 30% sparsity 下声称有效，明确指出 50% 下 decomposition 失效；(3) 分析 K=4 at 50% 的 per-layer sparsity 分布，看是否存在 pathological allocation。\n\n**N2** [critical] MMLU K=4 超过 E2E 的 anomaly 暴露 decomposition confound\n\n- 具体位置：§4.5, Appendix S (Table in App S: MMLU K=4 = 42.7±1.4 vs E2E = 40.7±1.3)\n- 问题：K=4 在 MMLU 上系统性超过 E2E（所有 3 个 seed），论文解释为 K=4 的 near-uniform per-layer sparsity（std=0.003）匹配了 uniform inference protocol。但这说明 K=4 control 无法独立地隔离 coupling 效应——它同时改变了 allocation pattern。因此 signal type vs. coupling 的百分比分解（Table in Appendix R）混淆了 coupling effect 和 allocation effect。\n- 为什么影响接收：如果 decomposition 的两个维度不正交（论文自己承认 \"dimensions not fully orthogonal\"），那么 \"signal type accounts for the majority of the PPL gap\" 这一核心结论的 upper bound 性质需要更强的 caveat。目前论文在 abstract 和 conclusion 中反复强调此结论，但 caveat 仅在脚注中出现。\n- 建议修改方向：(1) 在 main text（非仅 appendix 脚注）中明确讨论 allocation confound 对 decomposition 的影响；(2) 考虑在 K=4 实验中强制使用与 E2E 相同的 per-layer allocation pattern（而非 K=4 自然学出的 near-uniform），以真正隔离 coupling effect。\n\n**N3** [critical] Qwen-2.5-14B 的 GSM8K -20pp regression 仅有单 seed 支撑\n\n- 具体位置：§4.6 (Table in Appendix K: Qwen-14B uniform KL GSM8K = 32.0±5.2 vs TEAL = 52.1)\n- 问题：GSM8K 从 52.1pp（TEAL）下降到 32.0pp（KL），降幅达 20pp，且标准差为 5.2pp（相对于均值 32.0 的 CV=16.3%）。论文在 §4.6 称这是 \"systematic property of distribution-matching\"，但 global allocation 行（Table in Appendix K）仅有 seed 42。3-seed 仅用于 uniform 的 GSM8K，而 global 的所有 6 个 metrics 均为单 seed。\n- 为什么影响接收：-20pp GSM8K 是论文最大的负面结果之一。如果这个结果是 seed-dependent 的（14B global 没有 multi-seed 验证），那么 \"knowledge-task regression scales with model size\" 的结论可能不成立。单 seed 不足以支撑如此强的跨规模趋势声明。\n- 建议修改方向：补充 Qwen-14B 至少 3-seed 评估，或者弱化跨规模趋势的措辞为 \"preliminary observation\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 系统性 knowledge-task regression 缺乏机制分析\n\n- 具体位置：§4.2 \"Knowledge-Task Regression: Hypothesis\" 段落\n- 问题：KL 在所有规模和架构上一致性地 underperform TEAL 在 MMLU 和 GSM8K 上：8B MMLU -5.2pp, 14B GSM8K -20pp, Mistral GSM8K -7.3pp。论文提出两个假说（WikiText-103 数据偏差和 forward KL 的 mode-covering 稀释 rare activations），但两者均 \"await validation via knowledge-neuron probing\"。\n- 建议：至少做一个简单验证：(1) 比较 KL 和 magnitude 在 knowledge-critical layers（如 L14-L18）的 neuron retention 差异；(2) 或者在 GSM8K 样本上计算 KL vs magnitude mask 的 per-layer Jaccard，看 divergence 是否在特定层更严重。Appendix T 的 constraint analysis（remove valley → MMLU +3.4pp）已经暗示了方向，可以更深入。\n\n**W2** [warning] C1 ablation s42 oracle 来自不同 checkpoint\n\n- 具体位置：Table 3 caption footnote \"†s42 oracle is from an earlier training run\"\n- 问题：s42 的 C1 在 30% 时 PPL = 9.45（vs KL 8.80, gap 0.65pp），而 s123 和 s456 使用 matched retrained oracles 后 gap 降至 ≤0.03pp。这表明 s42 的 0.65pp gap 主要来自 oracle provenance mismatch，而非 target-swap 本身的效应。但 s42 是 Table 3 中最显眼的第一行数据。\n- 建议：(1) 为 s42 补训 matched oracle 以消除 provenance confound；(2) 或在 Table 3 中将 s42 标记为 \"oracle mismatch\" 并优先展示 s123/s456 的结果。\n\n**W3** [warning] BCE 30% 仅报告 global allocation，缺少 uniform 对比\n\n- 具体位置：Table 1, BCE 30% 行标注 \"BCE global†\"\n- 问题：KL 30% 有 global（8.96）和 uniform（8.81）两个配置，但 BCE 30% 仅有 global（11.25）。由于 KL 的 best 在 uniform（8.81），但 BCE 没有 uniform 数据，无法直接对比相同 allocation strategy 下 KL vs BCE 的差异。\n- 建议：补充 BCE 30% uniform 数据，或解释为什么 BCE uniform 数据缺失。\n\n**W4** [warning] Sparsity controller 在 30% target 饱和（λ=5000 cap）\n\n- 具体位置：Appendix C, Table 9 第一行（30% target, λ_max=5000, Final λ=5000 cap, Actual sparsity=0.285）\n- 问题：λ 饱和在 cap 意味着 controller 已尽最大努力仍无法达到 30% target（实际 28.5%，偏差 5%）。这是 geometric penalty schedule 的失败模式。虽然论文在 Appendix C 末尾说明 TEAL at 28.5% PPL=10.30 仍远不如 KL 8.81，但 systematic under-sparsification 意味着 KL 的 PPL 优势部分来自更低的实际 sparsity。\n- 建议：(1) 在 main text 而非仅 appendix 中讨论这一偏差；(2) 为 main results 补充一个在 exactly matched actual sparsity 下的对比行。\n\n**W5** [warning] 无 wall-clock speedup 限制实际影响\n\n- 具体位置：Appendix A（6.4% latency overhead），§5 Conclusion\n- 问题：Sparse prediction 的最终目的是加速推理。论文在 Appendix A 说 \"Our contribution is prediction quality and inference simplification, not end-to-end latency reduction\"，并诚实地报告了 6.4% overhead。但对于 sparsity 领域的论文，缺乏 speedup 结果显著限制了贡献的实际意义。\n- 建议：(1) 至少在一层使用 Triton block-sparse 做 proof-of-concept speedup 实验；(2) 或更清晰地在 introduction 中 frame 论文为 \"training objective study\"，弱化 efficiency claim。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.2: \"reducing TEAL's perplexity by 19% (10.82 → 8.81)\" — 准确值为 18.6%，19% 是向上取整，建议用 \"~19%\" 或精确值。\n- Eq. 3: s_j 缺少层标 ℓ 的上标，与 Eq. 1-2 的 notation 不一致。\n- §3.4: \"No temperature scaling (T=1) is applied (Hinton et al., 2015)\" — 这里的 T 是 KL distillation 的 temperature，而 §3.3 的 τ 是 Gumbel-Sigmoid 的 temperature。两者使用不同符号很好，但可能让读者困惑是否两者相关。建议在首次出现 T 时加一句澄清。\n- Table 4: STE 在 30% 缺少 PPL 数据（标记为 \"---‡\"），footnote 解释 STE 仅达 20.8% effective sparsity。但这实际上意味着 STE 和 Gumbel 在不同 actual sparsity 下对比，公平性有限。\n- Limitations 段落：提到 \"scaling to 70B+ remains future work\"，但论文已经在 14B 上观察到 regression 加剧，这使得 70B+ 的前景更加不确定，建议提及。\n\n---\n\n## 主要优势\n\n1. **C1 target-swap ablation 设计巧妙**：将 \"what\"（mask target quality）和 \"how\"（gradient coupling mechanism）解耦，证明 KL 发现的 mask patterns 是质量优势的主要来源。这是论文最有洞察力的实验。\n\n2. **实验控制严格**：KL / BCE / MSE 使用完全相同的 architecture、data、optimizer、steps，仅改变 loss function。这种 controlled comparison 在 empirical ML 论文中并不常见。\n\n3. **诚实的 limitations**：论文明确承认无 wall-clock speedup、knowledge-task regression、training data homogeneity。Abstract 使用更保守的 14.5%（matched sparsity）而非 18.6%（nominal）。\n\n4. **丰富的 appendix**：从 bottleneck sensitivity 到 temperature schedule 到 training convergence 到 cross-seed mask consistency，appendix 覆盖了大部分可预见的 reviewer 问题。\n\n5. **2D taxonomy**（Table 1, §3.7）提供了一个有用的组织框架：correction granularity × training signal coupling，帮助定位论文贡献。\n\n6. **3-seed 评估**用于主要结果（8B），PPL 标准差极小（±0.02），增强了结果的可靠性。\n\n---\n\n## Questions for Authors\n\nQ1: K=4 at 50% 为什么比 K=1 差？你们是否有 K=2, K=8 的数据来追踪 PPL vs K 的趋势？\n\nQ2: 如果在 K=4 实验中强制使用 E2E KL 的 per-layer allocation pattern（而非 K=4 自然学出的），MMLU anomaly 是否消失？\n\nQ3: 你们是否尝试过在 GSM8K 或 math 数据上训练 predictor（而非 WikiText-103），以检验 knowledge-task regression 是否来自 training data bias？\n\nQ4: BCE 30% 为什么缺少 uniform allocation 数据？\n\nQ5: 在 Appendix T 的 remove-valley 实验中，MMLU +3.4pp 的代价是 ARC-c -1.5pp。是否存在一个 per-layer allocation 配置能同时改善两者？",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**Soundness**: 3.5/5\n**Excitement**: 3/5\n**Confidence**: 4/5（仔细验证了所有关键数字和公式）\n\n**一句话总结**: 扎实的实证研究，证明了 output-distribution alignment（forward KL）显著优于 per-neuron BCE 来训练 sparsity predictor，C1 target-swap ablation 设计巧妙；但系统性的 knowledge-task regression、coupling decomposition 的 confounds、以及缺乏 wall-clock speedup 限制了贡献。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | KL 公式正确，Gumbel-Sigmoid 标准，ablation 设计巧妙。但 coupling decomposition 有未解决的 confounds（K=4 anomaly），sparsity controller 在 30% target 饱和未达目标 |\n| Excitement | 3/5 | 填补了 training objective for sparsity predictor 的文献空白，C1 ablation 有洞察力；但缺乏 wall-clock speedup 和系统性 knowledge regression 限制实际影响 |\n| Reproducibility | 4/5 | 训练细节充分（lr, optimizer, batch size, seq_len, hardware），承诺 release code；但 seed 覆盖不完整（14B 单 seed） |\n| Overall | 3.5/5 | 介于 Conference 和 Findings 之间；若能修复关键问题可达 Conference |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Per-layer KL K=4 在 50% sparsity 的反常行为削弱 coupling decomposition 的可信度\n\n- 具体位置：§4.5 (Table 4, Per-layer KL K=4 行)\n- 问题：K=4 per-layer KL 在 50% sparsity 的 PPL 为 44.23，**劣于** K=1 的 34.85，而 E2E KL 为 11.84。如果 coupling 是有益的，增加 masked layers 数量（K=1→K=4）应缩小与 E2E 的差距，但实际上差距扩大了（+23.06→+32.44）。论文给出的解释是 \"gradient interference\"（§4.5 倒数第二段），但这是纯粹的 speculation，没有任何实验验证。\n- 为什么影响接收：该反常行为直接动摇了 §4.5 signal type vs. coupling scope decomposition 的核心叙事。如果 K=4 的行为无法被解释，那么基于 K=1 和 K=4 的 decomposition percentages（如 \"PPL 67% closure\"）的可靠性也存疑。论文的一个主要 contribution 是这个 decomposition，但它在更高 sparsity 下失效。\n- 建议修改方向：(1) 增加 K=2, K=8, K=16 的实验以追踪 PPL 随 K 的变化趋势；(2) 或者限制 decomposition 分析仅在 30% sparsity 下声称有效，明确指出 50% 下 decomposition 失效；(3) 分析 K=4 at 50% 的 per-layer sparsity 分布，看是否存在 pathological allocation。\n\n**N2** [critical] MMLU K=4 超过 E2E 的 anomaly 暴露 decomposition confound\n\n- 具体位置：§4.5, Appendix S (Table in App S: MMLU K=4 = 42.7±1.4 vs E2E = 40.7±1.3)\n- 问题：K=4 在 MMLU 上系统性超过 E2E（所有 3 个 seed），论文解释为 K=4 的 near-uniform per-layer sparsity（std=0.003）匹配了 uniform inference protocol。但这说明 K=4 control 无法独立地隔离 coupling 效应——它同时改变了 allocation pattern。因此 signal type vs. coupling 的百分比分解（Table in Appendix R）混淆了 coupling effect 和 allocation effect。\n- 为什么影响接收：如果 decomposition 的两个维度不正交（论文自己承认 \"dimensions not fully orthogonal\"），那么 \"signal type accounts for the majority of the PPL gap\" 这一核心结论的 upper bound 性质需要更强的 caveat。目前论文在 abstract 和 conclusion 中反复强调此结论，但 caveat 仅在脚注中出现。\n- 建议修改方向：(1) 在 main text（非仅 appendix 脚注）中明确讨论 allocation confound 对 decomposition 的影响；(2) 考虑在 K=4 实验中强制使用与 E2E 相同的 per-layer allocation pattern（而非 K=4 自然学出的 near-uniform），以真正隔离 coupling effect。\n\n**N3** [critical] Qwen-2.5-14B 的 GSM8K -20pp regression 仅有单 seed 支撑\n\n- 具体位置：§4.6 (Table in Appendix K: Qwen-14B uniform KL GSM8K = 32.0±5.2 vs TEAL = 52.1)\n- 问题：GSM8K 从 52.1pp（TEAL）下降到 32.0pp（KL），降幅达 20pp，且标准差为 5.2pp（相对于均值 32.0 的 CV=16.3%）。论文在 §4.6 称这是 \"systematic property of distribution-matching\"，但 global allocation 行（Table in Appendix K）仅有 seed 42。3-seed 仅用于 uniform 的 GSM8K，而 global 的所有 6 个 metrics 均为单 seed。\n- 为什么影响接收：-20pp GSM8K 是论文最大的负面结果之一。如果这个结果是 seed-dependent 的（14B global 没有 multi-seed 验证），那么 \"knowledge-task regression scales with model size\" 的结论可能不成立。单 seed 不足以支撑如此强的跨规模趋势声明。\n- 建议修改方向：补充 Qwen-14B 至少 3-seed 评估，或者弱化跨规模趋势的措辞为 \"preliminary observation\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 系统性 knowledge-task regression 缺乏机制分析\n\n- 具体位置：§4.2 \"Knowledge-Task Regression: Hypothesis\" 段落\n- 问题：KL 在所有规模和架构上一致性地 underperform TEAL 在 MMLU 和 GSM8K 上：8B MMLU -5.2pp, 14B GSM8K -20pp, Mistral GSM8K -7.3pp。论文提出两个假说（WikiText-103 数据偏差和 forward KL 的 mode-covering 稀释 rare activations），但两者均 \"await validation via knowledge-neuron probing\"。\n- 建议：至少做一个简单验证：(1) 比较 KL 和 magnitude 在 knowledge-critical layers（如 L14-L18）的 neuron retention 差异；(2) 或者在 GSM8K 样本上计算 KL vs magnitude mask 的 per-layer Jaccard，看 divergence 是否在特定层更严重。Appendix T 的 constraint analysis（remove valley → MMLU +3.4pp）已经暗示了方向，可以更深入。\n\n**W2** [warning] C1 ablation s42 oracle 来自不同 checkpoint\n\n- 具体位置：Table 3 caption footnote \"†s42 oracle is from an earlier training run\"\n- 问题：s42 的 C1 在 30% 时 PPL = 9.45（vs KL 8.80, gap 0.65pp），而 s123 和 s456 使用 matched retrained oracles 后 gap 降至 ≤0.03pp。这表明 s42 的 0.65pp gap 主要来自 oracle provenance mismatch，而非 target-swap 本身的效应。但 s42 是 Table 3 中最显眼的第一行数据。\n- 建议：(1) 为 s42 补训 matched oracle 以消除 provenance confound；(2) 或在 Table 3 中将 s42 标记为 \"oracle mismatch\" 并优先展示 s123/s456 的结果。\n\n**W3** [warning] BCE 30% 仅报告 global allocation，缺少 uniform 对比\n\n- 具体位置：Table 1, BCE 30% 行标注 \"BCE global†\"\n- 问题：KL 30% 有 global（8.96）和 uniform（8.81）两个配置，但 BCE 30% 仅有 global（11.25）。由于 KL 的 best 在 uniform（8.81），但 BCE 没有 uniform 数据，无法直接对比相同 allocation strategy 下 KL vs BCE 的差异。\n- 建议：补充 BCE 30% uniform 数据，或解释为什么 BCE uniform 数据缺失。\n\n**W4** [warning] Sparsity controller 在 30% target 饱和（λ=5000 cap）\n\n- 具体位置：Appendix C, Table 9 第一行（30% target, λ_max=5000, Final λ=5000 cap, Actual sparsity=0.285）\n- 问题：λ 饱和在 cap 意味着 controller 已尽最大努力仍无法达到 30% target（实际 28.5%，偏差 5%）。这是 geometric penalty schedule 的失败模式。虽然论文在 Appendix C 末尾说明 TEAL at 28.5% PPL=10.30 仍远不如 KL 8.81，但 systematic under-sparsification 意味着 KL 的 PPL 优势部分来自更低的实际 sparsity。\n- 建议：(1) 在 main text 而非仅 appendix 中讨论这一偏差；(2) 为 main results 补充一个在 exactly matched actual sparsity 下的对比行。\n\n**W5** [warning] 无 wall-clock speedup 限制实际影响\n\n- 具体位置：Appendix A（6.4% latency overhead），§5 Conclusion\n- 问题：Sparse prediction 的最终目的是加速推理。论文在 Appendix A 说 \"Our contribution is prediction quality and inference simplification, not end-to-end latency reduction\"，并诚实地报告了 6.4% overhead。但对于 sparsity 领域的论文，缺乏 speedup 结果显著限制了贡献的实际意义。\n- 建议：(1) 至少在一层使用 Triton block-sparse 做 proof-of-concept speedup 实验；(2) 或更清晰地在 introduction 中 frame 论文为 \"training objective study\"，弱化 efficiency claim。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.2: \"reducing TEAL's perplexity by 19% (10.82 → 8.81)\" — 准确值为 18.6%，19% 是向上取整，建议用 \"~19%\" 或精确值。\n- Eq. 3: s_j 缺少层标 ℓ 的上标，与 Eq. 1-2 的 notation 不一致。\n- §3.4: \"No temperature scaling (T=1) is applied (Hinton et al., 2015)\" — 这里的 T 是 KL distillation 的 temperature，而 §3.3 的 τ 是 Gumbel-Sigmoid 的 temperature。两者使用不同符号很好，但可能让读者困惑是否两者相关。建议在首次出现 T 时加一句澄清。\n- Table 4: STE 在 30% 缺少 PPL 数据（标记为 \"---‡\"），footnote 解释 STE 仅达 20.8% effective sparsity。但这实际上意味着 STE 和 Gumbel 在不同 actual sparsity 下对比，公平性有限。\n- Limitations 段落：提到 \"scaling to 70B+ remains future work\"，但论文已经在 14B 上观察到 regression 加剧，这使得 70B+ 的前景更加不确定，建议提及。\n\n---\n\n## 主要优势\n\n1. **C1 target-swap ablation 设计巧妙**：将 \"what\"（mask target quality）和 \"how\"（gradient coupling mechanism）解耦，证明 KL 发现的 mask patterns 是质量优势的主要来源。这是论文最有洞察力的实验。\n\n2. **实验控制严格**：KL / BCE / MSE 使用完全相同的 architecture、data、optimizer、steps，仅改变 loss function。这种 controlled comparison 在 empirical ML 论文中并不常见。\n\n3. **诚实的 limitations**：论文明确承认无 wall-clock speedup、knowledge-task regression、training data homogeneity。Abstract 使用更保守的 14.5%（matched sparsity）而非 18.6%（nominal）。\n\n4. **丰富的 appendix**：从 bottleneck sensitivity 到 temperature schedule 到 training convergence 到 cross-seed mask consistency，appendix 覆盖了大部分可预见的 reviewer 问题。\n\n5. **2D taxonomy**（Table 1, §3.7）提供了一个有用的组织框架：correction granularity × training signal coupling，帮助定位论文贡献。\n\n6. **3-seed 评估**用于主要结果（8B），PPL 标准差极小（±0.02），增强了结果的可靠性。\n\n---\n\n## Questions for Authors\n\nQ1: K=4 at 50% 为什么比 K=1 差？你们是否有 K=2, K=8 的数据来追踪 PPL vs K 的趋势？\n\nQ2: 如果在 K=4 实验中强制使用 E2E KL 的 per-layer allocation pattern（而非 K=4 自然学出的），MMLU anomaly 是否消失？\n\nQ3: 你们是否尝试过在 GSM8K 或 math 数据上训练 predictor（而非 WikiText-103），以检验 knowledge-task regression 是否来自 training data bias？\n\nQ4: BCE 30% 为什么缺少 uniform allocation 数据？\n\nQ5: 在 Appendix T 的 remove-valley 实验中，MMLU +3.4pp 的代价是 ARC-c -1.5pp。是否存在一个 per-layer allocation 配置能同时改善两者？",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-23T00:40:03.291012+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3613
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-23T00:40:09.022451+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-23T00:40:09.073125+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-23T00:40:13.039097+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1417 · 2026-05-23T00:40:13.089722+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1418 · 2026-05-23T00:40:23.537422+00:00_

审稿完成。总结：

- **Overall 3.5（Borderline Conference）**，Soundness 3.5，Excitement 3
- 3 个 Must-Fix：(1) K=4 at 50% 反常行为削弱 coupling decomposition 可信度；(2) MMLU K=4 > E2E anomaly 暴露 allocation confound；(3) Qwen-14B GSM8K -20pp 仅单 seed
- 5 个 Should-Fix：系统性 knowledge regression 缺机制分析、C1 s42 oracle provenance、BCE 30% 缺 uniform 对比、sparsity controller 30% 饱和、无 wall-clock speedup
- 主要优势：C1 target-swap ablation 巧妙、实验控制严格、limitations 诚实、appendix 丰富

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 43

## Round 43

4 recorded events


### User

_source line 1419 · 2026-05-23T00:43:31.664246+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

**Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4

### Must-Fix 问题

**N1** [critical] 知识密集型任务的系统性退化缺乏充分调查
- KL predictor 在所有测试规模上系统性地在 MMLU/GSM8K 上退化（8B: MMLU -5.2pp; Mistral: GSM8K 15.9→8.6; Qwen-14B: GSM8K -20pp, MMLU -8.1pp）。论文仅提出两个假设但没有做任何控制实验验证。
- 建议：至少执行一个控制实验——例如在 C4 或 RedPajama 子集上训练 predictor，或更突出 Appendix T 的 constraint analysis（remove-valley → MMLU +3.4pp）。

**N2** [critical] 方法新颖性的边界需要更清晰地论证
- 核心技术（KL distillation + Gumbel-Sigmoid + sparsity predictor 架构）每个组件都是成熟技术。MaskLLM 已将 KL + Gumbel-Softmax 用于可学习稀疏 mask。论文的三点区分更多来自应用场景不同（activation vs weight sparsity），而非方法论创新。
- 建议：更明确地定位为分析驱动的实证贡献，加强 C1 ablation 和 signal type/coupling scope 分解的 framing。

### Should-Fix 问题

**W1** Per-layer KL 分解在 50% sparsity 下失效（K=4 PPL 44.23 > K=1 34.85），abstract/conclusion 仍使用 30% 结论做 general claims
**W2** 无 wall-clock 加速，6.4% latency overhead
**W3** 缺少生成质量评估（MT-Bench, AlpacaEval）
**W4** Introduction 中 "19%" PPL 减少实际为 18.6%
**W5** MSE baseline 在 50% 仅 seed 42（seed 123 catastrophic failure PPL=15,789），single-seed 结论不可靠
**W6** C1 ablation s42 oracle provenance 问题（s42 gap 0.65pp vs s123/s456 ≤0.03pp）

### 小问题
- Table 2 BCE 30% global vs KL uniform 比较不公平
- Abstract 信息密度偏高（9 句）
- Conclusion 过于简洁，缺 future work
- 术语不一致："output-distribution alignment/distillation/objective" 交替使用
- Figure 2 caption 14.5% vs §4.1 "19%" 使用不同基准
- GPU 型号 "RTX PRO 6000 Blackwell Server Edition" double-blind 风险

### Missing References
- TurboSparse-Mistral 后续工作
- Mixtral-of-Experts 区分说明
- 2026 年 1-5 月新工作检索
- 总体 missing refs 不构成重大问题

### 主要优势
1. 实验设计严谨（3-seed, cross-arch, 18 个 appendix sections）
2. C1 target-swap ablation 巧妙
3. 诚实的 limitations 披露
4. Per-layer KL decomposition 有 insight
5. 写作有适当 hedging
6. Compensation redundancy finding 简化推理管线

### 评分
Soundness 3.5, Excitement 3, Overall 3.5, Confidence 4, Reproducibility 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1420 · 2026-05-23T00:45:19.083291+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 知识密集型任务的系统性退化缺乏充分调查**\n\n同意这是论文最大的弱点之一。我在自己的审稿中也将此列为 W1 (Should-Fix)。数据模式非常清晰且跨规模一致：\n\n- 8B: MMLU 40.7 vs TEAL 45.86 (-5.2pp)，GSM8K 7.5 vs 8.79 (-1.3pp)（Table 2）\n- Mistral-7B: GSM8K 8.6 vs TEAL 15.9 (-7.3pp)（Appendix N, Table 17）\n- Qwen-14B uniform: GSM8K 32.0 vs TEAL 52.1 (-20pp)（Appendix K, Table 13）\n\n论文在 §4.2 \"Knowledge-Task Regression: Hypothesis\" 段提出两个假设但明确说 \"await validation via knowledge-neuron probing\"。R2 建议的控制实验（C4/RedPajama 训练）合理。我补充一点：Appendix T 的 constraint analysis 已经显示 remove-valley → MMLU +3.4pp, GSM8K +1.6pp（Table in Appendix T），这暗示 regression 部分源于 learned allocation（而非 loss function 本身），但论文未将此线索发展为系统性分析。至少应将 Appendix T 的发现提升到 main text，并讨论 allocation-aware training 的可能。\n\n**[AGREE with nuance] R2-N2: 方法新颖性的边界**\n\n部分同意。R2 正确指出核心组件（KL + Gumbel-Sigmoid + predictor architecture）均为成熟技术。但我认为 R2 对 MaskLLM 的对比略有偏差：\n\n1. MaskLLM（Fang et al., 2024）处理的是 **static N:M weight masks**，mask 在部署后固定不变；本文处理的是 **contextual activation sparsity**，mask 随每个 token 变化，且需要 global top-k 跨层协调。这不仅是 \"应用场景不同\"，而是优化问题根本不同——MaskLLM 直接优化离散 mask 组合，本文需要 predictor 来泛化到未见输入。论文在 Introduction 第一段已做此区分。\n\n2. 论文自身定位为 \"primarily an empirical study\"（Abstract 末句, Introduction §1 末段）。其贡献不在方法组件的新颖性，而在 (a) C1 target-swap ablation 解耦了 \"what\" vs \"how\"，(b) signal type vs coupling scope decomposition，(c) 跨 5 种 loss 的系统对比。这些 **实验设计** 是新颖的。\n\n建议：论文应更早且更显著地承认组件层面的非新颖性（目前仅在 Related Work §2 的 MaskLLM 段提及），并在 Introduction 的 contribution list 中将 C1 ablation 和 decomposition 置于首位（目前第一条是 \"ranking across five losses\"，信息量不如 \"C1 + decomposition\"）。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Per-layer KL 分解在 50% sparsity 下失效**\n\n强烈同意。我在自己的审稿中将此列为 **N1 (Critical)**——K=4 at 50% PPL 44.23 > K=1 34.85 的反常行为是 coupling decomposition 可信度的核心威胁。论文在 §4.5 末段给出 \"gradient interference\" 假说但无实验支撑。Abstract (\"Signal type accounts for the majority of the PPL gap\") 和 Conclusion (\"signal type accounts for the majority of the PPL gap; upper bound\") 均基于 30% 结果做 general claim，但未注明此结论在 50% 下不成立。\n\n**[AGREE] R2-W2: 无 wall-clock 加速**\n\n同意。我也列为 W5。Appendix A 报告 6.4% overhead（126.78 vs 119.11 ms/fwd），无任何 sparse kernel 实验。论文诚实披露了这一点，但对 sparsity 论文而言这显著限制了实际影响。\n\n**[REBUT] R2-W3: 缺少生成质量评估（MT-Bench, AlpacaEval）**\n\n不完全同意这属于 Should-Fix。理由：\n\n1. 论文评估的是 **base model**（LLaMA-3.1-8B，非 Instruct），MT-Bench 和 AlpacaEval 需要 instruction-tuned model。在 base model 上跑这些 benchmark 没有意义。\n2. 论文的 Limitations 段已承认 \"open-ended generation quality (e.g., MT-Bench) remains untested\"，并将其列为 future work。\n3. 当前的 evaluation suite（PPL + 6 个 downstream tasks + OOD + cross-architecture）对于一篇 training objective 的 empirical study 已经相当充分。\n\n如果 R2 的意图是评估 fluency/coherence 而非 instruction-following，更合适的 benchmark 是 perplexity（已有）或 text completion quality。但我不认为缺少 MT-Bench 是一个需要修复的问题。\n\n**[AGREE] R2-W4: \"19%\" vs 18.6%**\n\n同意是不精确的取整。我在自己的小问题中也指出了这一点。(10.82-8.81)/10.82 = 18.58% ≈ 18.6%。应改为 \"~19%\" 或 \"18.6%\"。\n\n**[AGREE] R2-W5: MSE baseline at 50% single seed**\n\n同意。MSE 50% 仅 seed 42 有效（PPL=229.26），seed 123 灾难性失败（PPL=15,789，Appendix G）。Table 4 中 MSE 50% 标注了 \"§\" footnote 但仅在 caption 中提及。单 seed 的 229.26 可能不代表 MSE 的典型表现。不过，MSE 30% 有 3-seed（18.52±1.68），已经 1.7× 劣于 TEAL，所以 MSE 劣势的结论在 30% 是稳健的。建议在 50% 对比中弱化对 MSE 的 claim 或补充更多 seed。\n\n**[AGREE] R2-W6: C1 s42 oracle provenance**\n\n同意。我列为 W2。s42 的 oracle 来自 earlier checkpoint（PPL gap 0.65pp），而 s123/s456 使用 matched oracle 后 gap 降至 ≤0.03pp。这使 s42 成为 Table 3 中的 outlier。建议为 s42 补训 matched oracle 或调整展示顺序。\n\n---\n\n### 小问题\n\n**[AGREE] BCE 30% comparison fairness**: 我在 W3 中提出了同样的问题。Table 2 中 BCE 30% 仅有 global，KL 有 global+uniform，比较不完整。\n\n**[AGREE] Abstract 信息密度**: 9 句话包含 PPL 数字、C1 ablation 结论、decomposition 结论、cross-architecture 结论，确实偏密。但内容均有必要，可考虑拆分为两段。\n\n**[REBUT] Conclusion 过于简洁**: Conclusion 虽仅 4 句但覆盖了：(1) 核心发现（signal type 主导 PPL gap），(2) key result（14.5% PPL reduction, 46-68% divergence），(3) limitations summary，(4) code release。ARR 对 conclusion 格式无硬性要求。简洁但完整。Future work 在 Limitations 段中隐含（knowledge-task regression, wall-clock speedup, scaling to 70B+）。我不认为这需要修复。\n\n**[AGREE] 术语不一致**: 确实存在。\"output-distribution alignment\"（Introduction, Conclusion）、\"KL distillation\"（§3, §4）、\"output-distribution objective\"（Abstract）交替使用。建议统一为 \"output-distribution alignment\" 并在首次出现时定义。\n\n**[AGREE] Figure 2 caption vs §4.1 基准不一致**: Figure 2 caption 用 \"14.5% at 30%\" 而 §4.2 用 \"19%\"。前者是 matched sparsity（both at 28.5%），后者是 nominal TEAL 30%。两者都正确但对读者造成困惑。建议在 Figure 2 caption 中注明 \"(matched actual sparsity 28.5%)\"。\n\n**[REBUT] GPU 型号 double-blind 风险**: \"RTX PRO 6000 Blackwell Server Edition\" 是 2025 年发布的商用 GPU，全球数万个实验室可能拥有。这不比 \"A100 80GB\" 更具识别性。ARR 的 anonymity policy 允许报告具体硬件配置。不构成 de-anonymization 风险。\n\n---\n\n### Missing References\n\n**[AGREE with caveat]**: R2 提到的 TurboSparse-Mistral 和 2026 年新工作值得检查，但 R2 自己也说 \"总体 missing refs 不构成重大问题\"。论文的 Related Work（§2）已经相当全面，覆盖了 TEAL, CATS, R-Sparse, DejaVu, FastForward, ShadowLLM, D2DMoE, MaskLLM, SPON, PowerInfer, Deja Vu, LazyLLM 等。我同意可以补充但这不影响接收决定。\n\n---\n\n### 对 R2 优势评价的认同\n\n完全同意 R2 列出的 6 个优势。特别是：\n- **C1 target-swap ablation 的巧妙性** 是我和 R2 的共识\n- **诚实的 limitations 披露** 在 ML 论文中难能可贵\n- **Compensation redundancy finding** 确实简化了推理管线（去掉 67.2M 参数的 compensation network）\n\n---\n\n### 总结：与 R2 的分歧\n\n| R2 观点 | R1 立场 | 理由 |\n|---------|---------|------|\n| N2 新颖性不足 | 部分同意 | 组件非新颖，但实验设计（C1, decomposition）有新颖性；论文已自定位为 empirical study |\n| W3 缺 MT-Bench | 反驳 | Base model 不适用 instruction-following benchmarks |\n| Conclusion 太短 | 反驳 | 简洁但完整，ARR 无格式要求 |\n| GPU double-blind | 反驳 | 商用 GPU，不构成 de-anonymization |\n\n其余所有 Must-Fix 和 Should-Fix 均同意或基本同意。我和 R2 的核心共识是：**knowledge-task regression 的机制分析不足**和 **coupling decomposition 在高 sparsity 下失效**是论文两个最关键的弱点。\n\n**维持我的评分：Overall 3.5, Soundness 3.5, Excitement 3, Confidence 4。**",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 知识密集型任务的系统性退化缺乏充分调查**\n\n同意这是论文最大的弱点之一。我在自己的审稿中也将此列为 W1 (Should-Fix)。数据模式非常清晰且跨规模一致：\n\n- 8B: MMLU 40.7 vs TEAL 45.86 (-5.2pp)，GSM8K 7.5 vs 8.79 (-1.3pp)（Table 2）\n- Mistral-7B: GSM8K 8.6 vs TEAL 15.9 (-7.3pp)（Appendix N, Table 17）\n- Qwen-14B uniform: GSM8K 32.0 vs TEAL 52.1 (-20pp)（Appendix K, Table 13）\n\n论文在 §4.2 \"Knowledge-Task Regression: Hypothesis\" 段提出两个假设但明确说 \"await validation via knowledge-neuron probing\"。R2 建议的控制实验（C4/RedPajama 训练）合理。我补充一点：Appendix T 的 constraint analysis 已经显示 remove-valley → MMLU +3.4pp, GSM8K +1.6pp（Table in Appendix T），这暗示 regression 部分源于 learned allocation（而非 loss function 本身），但论文未将此线索发展为系统性分析。至少应将 Appendix T 的发现提升到 main text，并讨论 allocation-aware training 的可能。\n\n**[AGREE with nuance] R2-N2: 方法新颖性的边界**\n\n部分同意。R2 正确指出核心组件（KL + Gumbel-Sigmoid + predictor architecture）均为成熟技术。但我认为 R2 对 MaskLLM 的对比略有偏差：\n\n1. MaskLLM（Fang et al., 2024）处理的是 **static N:M weight masks**，mask 在部署后固定不变；本文处理的是 **contextual activation sparsity**，mask 随每个 token 变化，且需要 global top-k 跨层协调。这不仅是 \"应用场景不同\"，而是优化问题根本不同——MaskLLM 直接优化离散 mask 组合，本文需要 predictor 来泛化到未见输入。论文在 Introduction 第一段已做此区分。\n\n2. 论文自身定位为 \"primarily an empirical study\"（Abstract 末句, Introduction §1 末段）。其贡献不在方法组件的新颖性，而在 (a) C1 target-swap ablation 解耦了 \"what\" vs \"how\"，(b) signal type vs coupling scope decomposition，(c) 跨 5 种 loss 的系统对比。这些 **实验设计** 是新颖的。\n\n建议：论文应更早且更显著地承认组件层面的非新颖性（目前仅在 Related Work §2 的 MaskLLM 段提及），并在 Introduction 的 contribution list 中将 C1 ablation 和 decomposition 置于首位（目前第一条是 \"ranking across five losses\"，信息量不如 \"C1 + decomposition\"）。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Per-layer KL 分解在 50% sparsity 下失效**\n\n强烈同意。我在自己的审稿中将此列为 **N1 (Critical)**——K=4 at 50% PPL 44.23 > K=1 34.85 的反常行为是 coupling decomposition 可信度的核心威胁。论文在 §4.5 末段给出 \"gradient interference\" 假说但无实验支撑。Abstract (\"Signal type accounts for the majority of the PPL gap\") 和 Conclusion (\"signal type accounts for the majority of the PPL gap; upper bound\") 均基于 30% 结果做 general claim，但未注明此结论在 50% 下不成立。\n\n**[AGREE] R2-W2: 无 wall-clock 加速**\n\n同意。我也列为 W5。Appendix A 报告 6.4% overhead（126.78 vs 119.11 ms/fwd），无任何 sparse kernel 实验。论文诚实披露了这一点，但对 sparsity 论文而言这显著限制了实际影响。\n\n**[REBUT] R2-W3: 缺少生成质量评估（MT-Bench, AlpacaEval）**\n\n不完全同意这属于 Should-Fix。理由：\n\n1. 论文评估的是 **base model**（LLaMA-3.1-8B，非 Instruct），MT-Bench 和 AlpacaEval 需要 instruction-tuned model。在 base model 上跑这些 benchmark 没有意义。\n2. 论文的 Limitations 段已承认 \"open-ended generation quality (e.g., MT-Bench) remains untested\"，并将其列为 future work。\n3. 当前的 evaluation suite（PPL + 6 个 downstream tasks + OOD + cross-architecture）对于一篇 training objective 的 empirical study 已经相当充分。\n\n如果 R2 的意图是评估 fluency/coherence 而非 instruction-following，更合适的 benchmark 是 perplexity（已有）或 text completion quality。但我不认为缺少 MT-Bench 是一个需要修复的问题。\n\n**[AGREE] R2-W4: \"19%\" vs 18.6%**\n\n同意是不精确的取整。我在自己的小问题中也指出了这一点。(10.82-8.81)/10.82 = 18.58% ≈ 18.6%。应改为 \"~19%\" 或 \"18.6%\"。\n\n**[AGREE] R2-W5: MSE baseline at 50% single seed**\n\n同意。MSE 50% 仅 seed 42 有效（PPL=229.26），seed 123 灾难性失败（PPL=15,789，Appendix G）。Table 4 中 MSE 50% 标注了 \"§\" footnote 但仅在 caption 中提及。单 seed 的 229.26 可能不代表 MSE 的典型表现。不过，MSE 30% 有 3-seed（18.52±1.68），已经 1.7× 劣于 TEAL，所以 MSE 劣势的结论在 30% 是稳健的。建议在 50% 对比中弱化对 MSE 的 claim 或补充更多 seed。\n\n**[AGREE] R2-W6: C1 s42 oracle provenance**\n\n同意。我列为 W2。s42 的 oracle 来自 earlier checkpoint（PPL gap 0.65pp），而 s123/s456 使用 matched oracle 后 gap 降至 ≤0.03pp。这使 s42 成为 Table 3 中的 outlier。建议为 s42 补训 matched oracle 或调整展示顺序。\n\n---\n\n### 小问题\n\n**[AGREE] BCE 30% comparison fairness**: 我在 W3 中提出了同样的问题。Table 2 中 BCE 30% 仅有 global，KL 有 global+uniform，比较不完整。\n\n**[AGREE] Abstract 信息密度**: 9 句话包含 PPL 数字、C1 ablation 结论、decomposition 结论、cross-architecture 结论，确实偏密。但内容均有必要，可考虑拆分为两段。\n\n**[REBUT] Conclusion 过于简洁**: Conclusion 虽仅 4 句但覆盖了：(1) 核心发现（signal type 主导 PPL gap），(2) key result（14.5% PPL reduction, 46-68% divergence），(3) limitations summary，(4) code release。ARR 对 conclusion 格式无硬性要求。简洁但完整。Future work 在 Limitations 段中隐含（knowledge-task regression, wall-clock speedup, scaling to 70B+）。我不认为这需要修复。\n\n**[AGREE] 术语不一致**: 确实存在。\"output-distribution alignment\"（Introduction, Conclusion）、\"KL distillation\"（§3, §4）、\"output-distribution objective\"（Abstract）交替使用。建议统一为 \"output-distribution alignment\" 并在首次出现时定义。\n\n**[AGREE] Figure 2 caption vs §4.1 基准不一致**: Figure 2 caption 用 \"14.5% at 30%\" 而 §4.2 用 \"19%\"。前者是 matched sparsity（both at 28.5%），后者是 nominal TEAL 30%。两者都正确但对读者造成困惑。建议在 Figure 2 caption 中注明 \"(matched actual sparsity 28.5%)\"。\n\n**[REBUT] GPU 型号 double-blind 风险**: \"RTX PRO 6000 Blackwell Server Edition\" 是 2025 年发布的商用 GPU，全球数万个实验室可能拥有。这不比 \"A100 80GB\" 更具识别性。ARR 的 anonymity policy 允许报告具体硬件配置。不构成 de-anonymization 风险。\n\n---\n\n### Missing References\n\n**[AGREE with caveat]**: R2 提到的 TurboSparse-Mistral 和 2026 年新工作值得检查，但 R2 自己也说 \"总体 missing refs 不构成重大问题\"。论文的 Related Work（§2）已经相当全面，覆盖了 TEAL, CATS, R-Sparse, DejaVu, FastForward, ShadowLLM, D2DMoE, MaskLLM, SPON, PowerInfer, Deja Vu, LazyLLM 等。我同意可以补充但这不影响接收决定。\n\n---\n\n### 对 R2 优势评价的认同\n\n完全同意 R2 列出的 6 个优势。特别是：\n- **C1 target-swap ablation 的巧妙性** 是我和 R2 的共识\n- **诚实的 limitations 披露** 在 ML 论文中难能可贵\n- **Compensation redundancy finding** 确实简化了推理管线（去掉 67.2M 参数的 compensation network）\n\n---\n\n### 总结：与 R2 的分歧\n\n| R2 观点 | R1 立场 | 理由 |\n|---------|---------|------|\n| N2 新颖性不足 | 部分同意 | 组件非新颖，但实验设计（C1, decomposition）有新颖性；论文已自定位为 empirical study |\n| W3 缺 MT-Bench | 反驳 | Base model 不适用 instruction-following benchmarks |\n| Conclusion 太短 | 反驳 | 简洁但完整，ARR 无格式要求 |\n| GPU double-blind | 反驳 | 商用 GPU，不构成 de-anonymization |\n\n其余所有 Must-Fix 和 Should-Fix 均同意或基本同意。我和 R2 的核心共识是：**knowledge-task regression 的机制分析不足**和 **coupling decomposition 在高 sparsity 下失效**是论文两个最关键的弱点。\n\n**维持我的评分：Overall 3.5, Soundness 3.5, Excitement 3, Confidence 4。**",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1421 · 2026-05-23T00:45:22.698952+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---


### Assistant

_source line 1422 · 2026-05-23T00:45:28.755237+00:00_

已提交对 Reviewer 2 的逐条回应。

核心共识：knowledge-task regression 缺乏机制分析、coupling decomposition 在 50% sparsity 下失效是两个最关键的共同关注点。在 MT-Bench（base model 不适用）、Conclusion 长度、GPU double-blind 三点上持反对意见。维持 Overall 3.5 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 44

## Round 44

72 recorded events


### User

_source line 1423 · 2026-05-23T01:28:20.500124+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验有效性**的审查。

## Venue 信息
- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle
- **截止日期**：2026-05-25
- **正文页数限制**：8 页（ACL 模板）
- **匿名规则**：Double-blind
- **附录**：允许，审稿人可选择性参考

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf`

## 审查侧重

请重点审查以下方面，对每个方面给出具体发现：

### 1. 方法论严谨性
- §3.6 梯度分析（BCE vs KL gradient 对比）的论证是否充分？SNR 分析结论是否自洽？
- §3.3 Gumbel-Sigmoid relaxation 的使用和论证
- §3.5 Geometric penalty schedule 的收敛性论证
- KL distillation 的 forward vs reverse 选择是否有充分实验支撑？

### 2. 实验设计与统计可靠性
- 3-seed 评估是否足以支撑核心声明？高方差指标（ARC-c σ=3.6, MMLU 30% global σ=9.5）的统计力
- Table 2（主表）中不同方法间的比较是否公平？注意 allocation strategy 差异
- Table 3 C1 ablation 的实验设计是否能支撑其声明？s42 oracle provenance 问题
- Table 4 ablation 中哪些行是 3-seed、哪些是 single-seed？结论可靠性

### 3. Per-layer KL decomposition (§4.5)
- K=1 和 K=4 两个控制点能否支撑 signal type vs coupling scope 的分解？
- K=4 在 50% 下反常（PPL 44.23 > K=1 34.85）的假设性解释是否充分？
- 两个维度的正交性问题（K=4 改变 allocation pattern → allocation confound）

### 4. Cross-architecture 和 Scale 结果
- Mistral 和 Qwen-14B 的评估覆盖度
- MMLU/GSM8K 跨规模退步的机制分析是否充分？
- 6.4% latency overhead 的实际影响

### 5. 实验覆盖度空白
- 缺失的对比实验或 baseline
- 未评估的重要场景

请给出结构化审稿意见：Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-23T01:28:27.865384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-23T01:28:29.327846+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_1_772f066c.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1462
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-23T01:28:29.482207+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-23T01:28:29.532913+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-23T01:28:35.605997+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1429 · 2026-05-23T01:28:38.066005+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-23T01:28:38.919727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-23T01:28:43.105810+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about the ACL Rolling Review 2026 reviewer guidelines and review form. Here are the key details:

## Reviewer Guidelines

Reviewers are asked to follow a workflow of reading the paper and getting a first impression, then searching for related work. If you feel qualified to review only some aspects of the paper, you should state in the review which major parts you did not check, such as proofs.

Reviewers are provided with a checklist to flag problems that other people may have missed.

Cases of extre
…[truncated 991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7499
}
```

</details>

---


### Tool result

_source line 1432 · 2026-05-23T01:28:45.418433+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7352
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-23T01:28:45.418814+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 6499
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-23T01:28:55.251804+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Clarity, Confidence, and any other dimensions. List each dimension with its full scale description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Clarity, Confidence, and any other dimensions. List each dimension with its full scale description."
  }
}
```

</details>

---


### Tool call

_source line 1435 · 2026-05-23T01:28:55.302789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-23T01:28:55.354206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1437 · 2026-05-23T01:28:55.408175+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1438 · 2026-05-23T01:28:55.408644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1439 · 2026-05-23T01:28:55.810807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1440 · 2026-05-23T01:28:57.891557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2588
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-23T01:28:57.995523+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2641
}
```

</details>

---


### Tool result

_source line 1442 · 2026-05-23T01:28:58.207501+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2799
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-23T01:28:59.097012+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3688
}
```

</details>

---


### Tool result

_source line 1444 · 2026-05-23T01:28:59.435718+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3624
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-23T01:29:10.083005+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5 = "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4 = "Quite sure. I tried to check the important points carefully."
- 3 = "Pretty sure, but there's a chance I missed something."
- 2 = "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- 1 = "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (in 0.5 increments)
- 5 = Excellent study with thorough investigation
- 4 = Strong with sufficient support for claims
- 3 = Acceptable with support for main claims
- 2 = Poor with insufficient support for major claims
- 1 = Major issues, not sufficiently thorough

## 3. **Excitement**
Scale: 1-5 (in 0.5 increments)
- 5 = "Highly Exciting: I would recommend this paper to others"
- 4 = "Exciting: I would mention this paper to others"
- 3 = "Interesting: I might mention some points"
- 2 = "Potentially Interesting: does not resonate with me"
- 1 = "Not Exciting: does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (in 0.5 increments)
- 5 = Consider for Award
- 4 = Conference acceptance
- 3 = Findings track acceptance
- 2 = Resubmit next cycle
- 1 = Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- 5 = "They could easily reproduce the results."
- 4 = "They could mostly reproduce the results"
- 3 = "They could reproduce with some difficulty"
- 2 = "They would be hard pressed to reproduce"
- 1 = "They would not be able to reproduce"

## 6. **Datasets** (if applicable)
Scale: 1-5
- 5 = Enabling for future research
- 4 = Useful for researchers
- 3 = Potentially useful
- 2 = Documentary value only
- 1 = No usable datasets

## 7. **Software** (if applicable)
Scale: 1-5
- 5 = Enabling for future projects
- 4 = Useful for researchers
- 3 = Potentially useful
- 2 = Documentary value only
- 1 = No usable software

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 14831
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-23T01:29:17.718878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1447 · 2026-05-23T01:29:18.374757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1448 · 2026-05-23T01:29:18.932716+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1213
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-23T01:29:18.933193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1450 · 2026-05-23T01:29:19.688387+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---


### Tool call

_source line 1451 · 2026-05-23T01:29:19.688797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-23T01:29:19.889692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1453 · 2026-05-23T01:29:19.890853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool result

_source line 1454 · 2026-05-23T01:29:20.886012+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1197
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-23T01:29:21.087611+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1197
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-23T01:29:28.886374+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1457 · 2026-05-23T01:29:30.095225+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 335.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 362.0}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p19.png\", \"w
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1208
}
```

</details>

---


### Tool call

_source line 1458 · 2026-05-23T01:29:33.211321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1459 · 2026-05-23T01:29:33.666902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-23T01:29:34.623986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-23T01:29:35.177886+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1966
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-23T01:29:35.383206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1463 · 2026-05-23T01:29:35.384444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1717
}
```

</details>

---


### Tool call

_source line 1464 · 2026-05-23T01:29:35.391083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-23T01:29:36.347290+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1723
}
```

</details>

---


### Tool result

_source line 1466 · 2026-05-23T01:29:36.801201+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1417
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-23T01:29:36.852292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1461
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-23T01:29:42.173609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1469 · 2026-05-23T01:29:42.678327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1470 · 2026-05-23T01:29:43.536530+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-23T01:29:43.537962+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 1472 · 2026-05-23T01:29:43.688954+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1473 · 2026-05-23T01:29:43.842219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1474 · 2026-05-23T01:29:44.545596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 1475 · 2026-05-23T01:29:44.546870+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 1476 · 2026-05-23T01:29:53.679395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1477 · 2026-05-23T01:29:53.735446+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuro
…[truncated 9747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 56
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-23T01:29:53.735940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1479 · 2026-05-23T01:29:53.787551+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1480 · 2026-05-23T01:30:00.091864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1481 · 2026-05-23T01:30:00.444911+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at moderate sparsity (30\%) (upper bound; not fully orthogonal with coupling scope).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-23T01:30:00.445327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1483 · 2026-05-23T01:30:00.945101+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to PPL but m
…[truncated 3030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 499
}
```

</details>

---


### Tool call

_source line 1484 · 2026-05-23T01:30:00.982615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-23T01:30:01.271119+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for PPL at moderate sparsity (30\%; signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes task-dependently---substantially for commonsense, marginally for reasoning (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	Code and trained predictors will be released upon acceptance.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 288
}
```

</details>

---


### Tool call

_source line 1486 · 2026-05-23T01:30:01.332607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1487 · 2026-05-23T01:30:01.384353+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Our evaluation focuses on perplexity and multiple-choice benchmarks; open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity. The aggravation from 8B to 14B (GSM8K regression deepening from $-$1.3pp to $-$20.1pp) raises concern about scaling to 70B+; wall-clock speedup via sparse kernels also remains future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1488 · 2026-05-23T01:30:06.651313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 1489 · 2026-05-23T01:30:06.802192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1490 · 2026-05-23T01:30:06.852864+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
16	SVD-CSP~\cite{serbin2026svdcsp} compre
…[truncated 5041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1491 · 2026-05-23T01:30:06.954103+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 36747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-23T01:34:24.383860+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**Confidence**: 4 / 5 — Quite sure; I read the paper very carefully and am familiar with related work.\n**一句话总结**: 论文提出用 forward KL 替代 BCE 训练稀疏预测器，PPL 改善显著且实验设计诚实透明，但知识类任务系统性退化（随 scale 恶化）、缺乏实际加速、以及核心分解分析在 50% 稀疏度下失效，限制了贡献的深度和实用性。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法论合理，C1 ablation 设计精巧；但 per-layer KL decomposition 在 50% 处崩溃（K=4 比 K=1 更差），signal type vs coupling scope 两个维度存在 allocation confound，downstream claims 的统计力不足（3-seed MMLU σ=9.5） |\n| Excitement | 3.0/5 | KL > BCE 用于稀疏预测是有趣的实证发现，target-swap ablation 有新意；但缺乏实际推理加速（+6.4% overhead），且核心负面结果（知识任务退化随 scale 恶化）削弱了实用前景 |\n| Reproducibility | 4.0/5 | 实验细节充分（种子、步数、超参），附录完整（19页），承诺 release 代码；但部分关键行是 single-seed（Table 4 BCE 变体、MSE 50%），且 C1 s42 oracle 来自不同训练 run |\n| Clarity | 4.0/5 | 写作清晰，对局限性的披露非常诚实（罕见地在 abstract 里承认无加速、在正文持续标注 upper bound/confound）；但 Table 2 的 allocation 混用（BCE 30% 用 TEAL global，KL 用 uniform）需要读者仔细看脚注才能理解 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 知识类任务系统性退化随 scale 恶化，机制分析不充分\n- 具体位置：§4.2 Table 2, §4.6 Table 13 (Appendix K), Limitations\n- 问题：KL 在所有测试规模上一致地在 MMLU/GSM8K 上低于 TEAL——8B: MMLU -5.2pp, GSM8K -1.3pp (30%)；14B: MMLU -2.8pp, GSM8K **-20.1pp** (σ=5.2)。退化幅度从 8B 到 14B 恶化（GSM8K 从 -1.3pp 到 -20.1pp），暗示这不是可忽略的噪声而是系统性缺陷。论文提出两个假设（训练数据同质性、forward KL mode-covering 稀释稀有激活），但仅用 constraint experiment（remove valley, MMLU +3.4pp）部分验证了第一个因素，对第二个因素（mode-covering 导致 factual neuron 保护不足）没有任何实验支撑。\n- 为什么影响接收：一个声称改善稀疏预测质量的方法，如果在推理和知识任务上系统性退化且随规模恶化，其实用价值存疑。对于 EMNLP 会议级别的论文，应该至少有一个初步的消融来验证第二个假设（例如用 mixed domain 数据训练，或 probe knowledge neurons 的保留率），或者明确限定方法的适用场景。\n- 建议修改方向：(1) 在 WikiText-103 + 少量数学/代码数据上重新训练 predictor，测试 GSM8K 是否恢复；(2) 分析 KL vs magnitude masks 对已知 factual neurons（如 Meng et al., 2022 定位的）的保留率差异；(3) 如果无法修复，应将适用范围明确限定为\"以 PPL 和 commonsense 为目标的场景\"。\n\n**N2** [critical] Per-layer KL 分解在 50% 稀疏度下失效，削弱核心贡献之一\n- 具体位置：§4.5 (Per-Layer KL), Table 4\n- 问题：论文的核心贡献之一是将稀疏预测训练分解为 signal type（输出分布 vs 中间层）和 coupling scope（端到端 vs 逐层）。然而，在 50% 稀疏度下，K=4 per-layer KL（PPL 44.23）**比 K=1**（PPL 34.85）**更差**，而 E2E KL 为 11.84。论文对此的解释是\"partial coupling amplifies gradient interference\"，但这是纯粹假设性的，没有任何实验证据。此外，在 30% 处 K=4 的 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露了 allocation confound：K=4 产生 near-uniform allocation (std=0.003)，恰好匹配 uniform inference protocol，而 E2E KL 学到非均匀 allocation（protection valley）。这意味着 K=4 同时改变了两个维度（coupling 和 allocation），signal type 和 coupling scope **并非正交**。\n- 为什么影响接收：论文声称\"signal type accounts for the majority of the PPL gap\"（abstract, §4.5, conclusion），但这个 claim 标注为 upper bound，且仅在 30% 处可解释。如果这个分解是论文的核心分析贡献，它需要在关键操作点（50%）也成立，或者论文需要大幅降低这个 claim 的强度。\n- 建议修改方向：(1) 在 50% 处增加更多 K 值（K=2, K=8, K=16）以建立连续曲线，而非仅两个控制点；(2) 在 K=4 控制中强制使用与 E2E 相同的 allocation pattern（而非让 K=4 自行收敛到 near-uniform），消除 allocation confound；(3) 如果无法解决，将分解框架限定为\"30% moderate sparsity regime\"，并在 abstract/conclusion 中明确这一限制。\n\n**N3** [critical] 缺乏实际推理加速，实用贡献为零\n- 具体位置：§1 Introduction (最后一段), Appendix A (Table 5), Limitations\n- 问题：Predictor 增加 6.4% latency overhead（126.78 vs 119.11 ms/fwd），即使在 50% 稀疏度下也没有任何速度提升。论文使用的是 unstructured element-wise masks，不支持 sparse kernel 加速。论文坦诚地承认了这一点（\"This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here\"），但这意味着方法在当前形态下没有实用价值——它比 dense inference 更慢。\n- 为什么影响接收：对于一个稀疏预测方法，不能带来任何推理加速是一个严重的实用性缺陷。虽然论文定位为\"empirical study characterizing how the training objective shapes sparsity prediction quality\"，但 reviewer 和 AC 可能期望至少有 proof-of-concept 的加速实验。Related work 中的 LaRoSA、PowerInfer 等方法已经实现了 wall-clock speedup，没有与这些方法的对比使得贡献的 positioning 不够 convincing。\n- 建议修改方向：(1) 至少在一个 sparse kernel backend（Triton block-sparse / cuSPARSE）上展示 proof-of-concept 加速；(2) 如果不可行，增加与已有加速方法（LaRoSA 等）在 mask 质量层面的对比，证明 KL masks 在质量上的优势可以转化为更好的 quality-speedup tradeoff；(3) 讨论将 unstructured masks 转化为 structured（N:M / block-sparse）的路径和预期退化。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Downstream task 统计力不足：3 seeds 无法支撑细粒度比较\n- 具体位置：Table 2, §4.2\n- 问题：核心下游评估使用 3 seeds。对于 PPL（σ=0.02, CV=0.2%），3 seeds 完全足够。但对于下游任务，方差极高：MMLU 30% global σ=9.5（3-seed 95% CI 约 ±23.5pp），ARC-c 30% σ=3.6，Mistral ARC-c σ=6.4。论文正确指出\"95% confidence intervals for individual downstream tasks overlap\"，但仍在 abstract 和 conclusion 中做出下游比较的 claims（\"commonsense gains but knowledge-intensive decline\"）。这些 claims 的统计基础薄弱。\n- 建议：(1) 将下游比较的 claims 进一步弱化为\"directional trends\"而非 established findings；(2) 在有方差报告的指标上计算并报告 paired t-test 或 bootstrap p-value，让读者判断显著性；(3) 如果条件允许，增加到 5-10 seeds 以改善统计力。\n\n**W2** [warning] Table 2 Baseline 比较条件不统一\n- 具体位置：Table 2, 脚注 †\n- 问题：(1) BCE 30% 使用 TEAL global allocation（脚注说明 uniform 下 PPL=15.71），而 KL 30% 同时报告了 global 和 uniform——但 TEAL baseline 用的是 uniform。这使得横向比较需要在多个 allocation 间跳转。(2) BCE 50% 使用 2700 steps（2.71× KL 预算），而 KL 用 1000 steps。虽然 §4.3 解释了 iso-compute 动机，但这也意味着 Table 2 的 BCE 50% 结果对 BCE 是**有利**的（额外训练），KL 仍然大幅领先说明差距是本质的。(3) MSE 50% 只有 s42（s123 catastrophic PPL=15,789），单种子结果可靠性弱。\n- 建议：在 Table 2 中统一报告 KL/BCE/TEAL 在同一 allocation 下的结果，或者增加一个清晰的\"controlled comparison\"子表。当前的注释系统虽然信息完整但增加了阅读难度。\n\n**W3** [warning] C1 ablation 的 soft-vs-hard confound 未被完全解决\n- 具体位置：§4.4 \"Soft-vs-Hard Confound\" 段落\n- 问题：C1 把 KL predictor 的 soft logits 通过阈值（>0）二值化为 hard masks，然后用 BCE 训练新 predictor。但这改变了两件事：(1) 训练目标（KL→BCE），和 (2) mask 表示（soft ranking→binary）。论文承认了这个 confound 并报告了 BCE+Gumbel (32.22) vs standard BCE (27.97)，指出\"softness alone does not explain KL's advantage\"。但反过来说，C1 的 near-zero delta（≤0.79pp）可能部分来自于 KL masks 的 binary pattern 本身就足够好，而不是因为 BCE *training* on these targets 等价于 KL training。一个更干净的控制是：用 KL 训练但在推理时用 magnitude-based allocation（测试 KL 的 ranking 信息 vs pattern 信息）。\n- 建议：增加讨论这个 confound 的含义，或增加一个实验控制（例如冻结 KL predictor 的 binary mask patterns 但重新训练 ranking scores）。\n\n**W4** [warning] Qwen-14B 评估不完整\n- 具体位置：§4.6, Appendix K (Table 13)\n- 问题：Qwen-14B 的评估仅在 30% sparsity 下进行，且 GSM8K 在 uniform allocation 下只有 3-seed 均值（32.0±5.2），方差极高。没有 50% 的结果，没有 per-layer allocation 分析，也没有 C1 ablation。作为 cross-scale 证据，这不够有力——只有 PPL generalization 的 claim 是可靠的；downstream 的退化模式（GSM8K -20pp）需要更深入的分析。\n- 建议：至少增加 50% sparsity 的 PPL 结果以验证 scaling pattern；讨论 14B 上 GSM8K 退化加剧的可能机制（超越 §4.2 对 8B 的假设）。\n\n**W5** [warning] Forward KL vs Reverse KL 的实验论证依赖 30% 处的微小差距\n- 具体位置：Table 4, §4.5 \"Relaxation, Divergence, and SPON\"\n- 问题：在 30% 处，Forward KL (8.81) vs JSD (8.90) 差距仅 0.09 PPL（1.0%），Forward KL vs Reverse KL (9.26) 差距 0.45 PPL（5.1%）。论文引用 mode-covering 理论解释 forward KL 的优越性，但在这个差距水平下，理论叙事的支撑力度有限。只有在 50% 处差距才变得明显（+6.4% JSD, +8.6% RKL）。论文的叙事将 forward KL 选择呈现为一个重要的设计决策，但数据表明它更接近于 implementation detail（30% 差距小到可能被超参调整抹平）。\n- 建议：弱化 forward KL 选择的叙事权重；或增加在更多 sparsity levels 的 ablation 以建立更稳健的趋势。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.4 Eq. 5：$\\mathcal{L}_{\\text{KL}}$ 的求和是 over vocabulary $v$，但没有说明是否 applied at every token position 还是某种平均方式。附录 G 才提到\"summed over the vocabulary $v$ and averaged over sequence positions\"——这应该在正文中明确。\n- Table 2 脚注 ‡：\"Actual sparsity: KL 28.5% vs. TEAL 29.3% at 30%\"——由于 KL 的 Lagrangian 控制器使实际稀疏度偏离目标 5%（Appendix C），所有与 TEAL 的 PPL 比较都存在 0.8pp 的稀疏度差异。虽然 Appendix D 表明这个差异的 PPL 影响小（0.67），但正文应更明确地说明 matched-sparsity 比较。\n- Figure 1 (overview) 画得比较简单，没有展示训练阶段的 Gumbel relaxation 和 Lagrangian controller 的位置，对方法理解的帮助有限。\n- §2 Related Work：SPON 的讨论在 §2 和 §4.5 各出现一次，建议合并。\n- Appendix P \"Oracle Mask Provenance\"：s42 oracle 来自 earlier checkpoint 的问题应在正文 Table 3 caption 中更显著地标注（当前只有 † 号），因为这直接影响 C1 ablation 的可信度。\n\n---\n\n## 主要优势\n\n1. **Target-swap ablation (C1) 设计精巧**：将 KL-derived mask patterns 迁移到 BCE 训练，clean 地分离了 mask pattern quality 和 training objective coupling 的贡献。这是一个有创意且有信息量的控制实验。\n\n2. **对局限性的诚实披露极为罕见**：论文在 abstract 中就承认无加速、在正文中持续标注 \"upper bound\"/\"confound\"/\"not fully orthogonal\"、在 Limitations 中坦承所有负面发现。这种透明度在投稿论文中很少见，值得肯定。\n\n3. **PPL 改善显著且一致**：14.5% at 30%、50% at 50%，跨架构一致（LLaMA、Mistral、Qwen），且 3-seed PPL 的方差极低（CV=0.2%），说明 KL 训练方式确实学到了更好的 mask patterns。\n\n4. **实验覆盖面广**：5 种 loss 排名、3 个架构、6 个 sparsity levels、allocation 策略分析、sensitivity sweeps、OOD 评估、compensation redundancy——附录极为充分。\n\n5. **2D taxonomy (signal type × coupling scope) 为理解稀疏预测方法提供了有用框架**：即使分解不完美，这个分析视角对后续工作有价值。\n\n6. **训练成本极低**：1000 步、单 GPU、~45 分钟——方法的实用门槛非常低。\n\n---\n\n## Questions to Authors\n\nQ1: 是否尝试过在多样化数据（WikiText + 少量数学/代码文本）上训练 predictor？这是验证知识任务退化是否可修复的最直接实验。\n\nQ2: 在 K=4 控制中，如果强制使用 E2E KL 学到的非均匀 allocation（而非让 K=4 自行收敛到 near-uniform），MMLU 异常是否消失？这能直接测试 allocation confound 假设。\n\nQ3: Table 4 中 BCE+Gumbel+Penalty (38.02) 比 BCE+Gumbel-no-penalty (32.22) 更差——为什么添加 sparsity penalty 会让 BCE 表现恶化？这与 KL 方向上 penalty 的帮助形成反差。\n\nQ4: 论文报告 KL predictor 在 L14-L18 形成 protection valley（14-18% sparsity）。这个 pattern 在 Mistral 和 Qwen 上是否也出现？如果是，这可能揭示 SwiGLU 架构的通用属性。\n\nQ5: 考虑到 C1 ablation 显示 mask patterns 携带了大部分质量信息，一个自然的后续是：能否用 KL 训练一个 \"teacher predictor\"，然后用 BCE 训练一个更高效的 \"student predictor\" on KL-derived targets？这可能兼得 KL 的 mask quality 和 BCE 的 training stability。\n\n---\n\n## Missing References\n\n- **CATS** (Lee et al., 2024): §2 提到但 Table 2 未作为 baseline——考虑到 CATS 也是 per-layer adaptive threshold 方法且有 wall-clock speedup 数据，应该在实验中对比或至少讨论为何排除。\n- **MaskLLM** (Fang et al., 2024): §1 和 §2 讨论了与 MaskLLM 的区别（static N:M vs contextual），但没有实验对比——即使 setting 不同，PPL 层面的数字对比可以帮助读者校准结果。\n- **Mixture-of-Depths** (Raposo et al., 2024): §2 引用了但未讨论与 token-level sparsity prediction 的对比——本文的 per-token mask prediction 在概念上与 MoD 的 token routing 有对偶关系。\n\nSources:\n- [ACL Rolling Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**Confidence**: 4 / 5 — Quite sure; I read the paper very carefully and am familiar with related work.\n**一句话总结**: 论文提出用 forward KL 替代 BCE 训练稀疏预测器，PPL 改善显著且实验设计诚实透明，但知识类任务系统性退化（随 scale 恶化）、缺乏实际加速、以及核心分解分析在 50% 稀疏度下失效，限制了贡献的深度和实用性。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法论合理，C1 ablation 设计精巧；但 per-layer KL decomposition 在 50% 处崩溃（K=4 比 K=1 更差），signal type vs coupling scope 两个维度存在 allocation confound，downstream claims 的统计力不足（3-seed MMLU σ=9.5） |\n| Excitement | 3.0/5 | KL > BCE 用于稀疏预测是有趣的实证发现，target-swap ablation 有新意；但缺乏实际推理加速（+6.4% overhead），且核心负面结果（知识任务退化随 scale 恶化）削弱了实用前景 |\n| Reproducibility | 4.0/5 | 实验细节充分（种子、步数、超参），附录完整（19页），承诺 release 代码；但部分关键行是 single-seed（Table 4 BCE 变体、MSE 50%），且 C1 s42 oracle 来自不同训练 run |\n| Clarity | 4.0/5 | 写作清晰，对局限性的披露非常诚实（罕见地在 abstract 里承认无加速、在正文持续标注 upper bound/confound）；但 Table 2 的 allocation 混用（BCE 30% 用 TEAL global，KL 用 uniform）需要读者仔细看脚注才能理解 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 知识类任务系统性退化随 scale 恶化，机制分析不充分\n- 具体位置：§4.2 Table 2, §4.6 Table 13 (Appendix K), Limitations\n- 问题：KL 在所有测试规模上一致地在 MMLU/GSM8K 上低于 TEAL——8B: MMLU -5.2pp, GSM8K -1.3pp (30%)；14B: MMLU -2.8pp, GSM8K **-20.1pp** (σ=5.2)。退化幅度从 8B 到 14B 恶化（GSM8K 从 -1.3pp 到 -20.1pp），暗示这不是可忽略的噪声而是系统性缺陷。论文提出两个假设（训练数据同质性、forward KL mode-covering 稀释稀有激活），但仅用 constraint experiment（remove valley, MMLU +3.4pp）部分验证了第一个因素，对第二个因素（mode-covering 导致 factual neuron 保护不足）没有任何实验支撑。\n- 为什么影响接收：一个声称改善稀疏预测质量的方法，如果在推理和知识任务上系统性退化且随规模恶化，其实用价值存疑。对于 EMNLP 会议级别的论文，应该至少有一个初步的消融来验证第二个假设（例如用 mixed domain 数据训练，或 probe knowledge neurons 的保留率），或者明确限定方法的适用场景。\n- 建议修改方向：(1) 在 WikiText-103 + 少量数学/代码数据上重新训练 predictor，测试 GSM8K 是否恢复；(2) 分析 KL vs magnitude masks 对已知 factual neurons（如 Meng et al., 2022 定位的）的保留率差异；(3) 如果无法修复，应将适用范围明确限定为\"以 PPL 和 commonsense 为目标的场景\"。\n\n**N2** [critical] Per-layer KL 分解在 50% 稀疏度下失效，削弱核心贡献之一\n- 具体位置：§4.5 (Per-Layer KL), Table 4\n- 问题：论文的核心贡献之一是将稀疏预测训练分解为 signal type（输出分布 vs 中间层）和 coupling scope（端到端 vs 逐层）。然而，在 50% 稀疏度下，K=4 per-layer KL（PPL 44.23）**比 K=1**（PPL 34.85）**更差**，而 E2E KL 为 11.84。论文对此的解释是\"partial coupling amplifies gradient interference\"，但这是纯粹假设性的，没有任何实验证据。此外，在 30% 处 K=4 的 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露了 allocation confound：K=4 产生 near-uniform allocation (std=0.003)，恰好匹配 uniform inference protocol，而 E2E KL 学到非均匀 allocation（protection valley）。这意味着 K=4 同时改变了两个维度（coupling 和 allocation），signal type 和 coupling scope **并非正交**。\n- 为什么影响接收：论文声称\"signal type accounts for the majority of the PPL gap\"（abstract, §4.5, conclusion），但这个 claim 标注为 upper bound，且仅在 30% 处可解释。如果这个分解是论文的核心分析贡献，它需要在关键操作点（50%）也成立，或者论文需要大幅降低这个 claim 的强度。\n- 建议修改方向：(1) 在 50% 处增加更多 K 值（K=2, K=8, K=16）以建立连续曲线，而非仅两个控制点；(2) 在 K=4 控制中强制使用与 E2E 相同的 allocation pattern（而非让 K=4 自行收敛到 near-uniform），消除 allocation confound；(3) 如果无法解决，将分解框架限定为\"30% moderate sparsity regime\"，并在 abstract/conclusion 中明确这一限制。\n\n**N3** [critical] 缺乏实际推理加速，实用贡献为零\n- 具体位置：§1 Introduction (最后一段), Appendix A (Table 5), Limitations\n- 问题：Predictor 增加 6.4% latency overhead（126.78 vs 119.11 ms/fwd），即使在 50% 稀疏度下也没有任何速度提升。论文使用的是 unstructured element-wise masks，不支持 sparse kernel 加速。论文坦诚地承认了这一点（\"This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here\"），但这意味着方法在当前形态下没有实用价值——它比 dense inference 更慢。\n- 为什么影响接收：对于一个稀疏预测方法，不能带来任何推理加速是一个严重的实用性缺陷。虽然论文定位为\"empirical study characterizing how the training objective shapes sparsity prediction quality\"，但 reviewer 和 AC 可能期望至少有 proof-of-concept 的加速实验。Related work 中的 LaRoSA、PowerInfer 等方法已经实现了 wall-clock speedup，没有与这些方法的对比使得贡献的 positioning 不够 convincing。\n- 建议修改方向：(1) 至少在一个 sparse kernel backend（Triton block-sparse / cuSPARSE）上展示 proof-of-concept 加速；(2) 如果不可行，增加与已有加速方法（LaRoSA 等）在 mask 质量层面的对比，证明 KL masks 在质量上的优势可以转化为更好的 quality-speedup tradeoff；(3) 讨论将 unstructured masks 转化为 structured（N:M / block-sparse）的路径和预期退化。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Downstream task 统计力不足：3 seeds 无法支撑细粒度比较\n- 具体位置：Table 2, §4.2\n- 问题：核心下游评估使用 3 seeds。对于 PPL（σ=0.02, CV=0.2%），3 seeds 完全足够。但对于下游任务，方差极高：MMLU 30% global σ=9.5（3-seed 95% CI 约 ±23.5pp），ARC-c 30% σ=3.6，Mistral ARC-c σ=6.4。论文正确指出\"95% confidence intervals for individual downstream tasks overlap\"，但仍在 abstract 和 conclusion 中做出下游比较的 claims（\"commonsense gains but knowledge-intensive decline\"）。这些 claims 的统计基础薄弱。\n- 建议：(1) 将下游比较的 claims 进一步弱化为\"directional trends\"而非 established findings；(2) 在有方差报告的指标上计算并报告 paired t-test 或 bootstrap p-value，让读者判断显著性；(3) 如果条件允许，增加到 5-10 seeds 以改善统计力。\n\n**W2** [warning] Table 2 Baseline 比较条件不统一\n- 具体位置：Table 2, 脚注 †\n- 问题：(1) BCE 30% 使用 TEAL global allocation（脚注说明 uniform 下 PPL=15.71），而 KL 30% 同时报告了 global 和 uniform——但 TEAL baseline 用的是 uniform。这使得横向比较需要在多个 allocation 间跳转。(2) BCE 50% 使用 2700 steps（2.71× KL 预算），而 KL 用 1000 steps。虽然 §4.3 解释了 iso-compute 动机，但这也意味着 Table 2 的 BCE 50% 结果对 BCE 是**有利**的（额外训练），KL 仍然大幅领先说明差距是本质的。(3) MSE 50% 只有 s42（s123 catastrophic PPL=15,789），单种子结果可靠性弱。\n- 建议：在 Table 2 中统一报告 KL/BCE/TEAL 在同一 allocation 下的结果，或者增加一个清晰的\"controlled comparison\"子表。当前的注释系统虽然信息完整但增加了阅读难度。\n\n**W3** [warning] C1 ablation 的 soft-vs-hard confound 未被完全解决\n- 具体位置：§4.4 \"Soft-vs-Hard Confound\" 段落\n- 问题：C1 把 KL predictor 的 soft logits 通过阈值（>0）二值化为 hard masks，然后用 BCE 训练新 predictor。但这改变了两件事：(1) 训练目标（KL→BCE），和 (2) mask 表示（soft ranking→binary）。论文承认了这个 confound 并报告了 BCE+Gumbel (32.22) vs standard BCE (27.97)，指出\"softness alone does not explain KL's advantage\"。但反过来说，C1 的 near-zero delta（≤0.79pp）可能部分来自于 KL masks 的 binary pattern 本身就足够好，而不是因为 BCE *training* on these targets 等价于 KL training。一个更干净的控制是：用 KL 训练但在推理时用 magnitude-based allocation（测试 KL 的 ranking 信息 vs pattern 信息）。\n- 建议：增加讨论这个 confound 的含义，或增加一个实验控制（例如冻结 KL predictor 的 binary mask patterns 但重新训练 ranking scores）。\n\n**W4** [warning] Qwen-14B 评估不完整\n- 具体位置：§4.6, Appendix K (Table 13)\n- 问题：Qwen-14B 的评估仅在 30% sparsity 下进行，且 GSM8K 在 uniform allocation 下只有 3-seed 均值（32.0±5.2），方差极高。没有 50% 的结果，没有 per-layer allocation 分析，也没有 C1 ablation。作为 cross-scale 证据，这不够有力——只有 PPL generalization 的 claim 是可靠的；downstream 的退化模式（GSM8K -20pp）需要更深入的分析。\n- 建议：至少增加 50% sparsity 的 PPL 结果以验证 scaling pattern；讨论 14B 上 GSM8K 退化加剧的可能机制（超越 §4.2 对 8B 的假设）。\n\n**W5** [warning] Forward KL vs Reverse KL 的实验论证依赖 30% 处的微小差距\n- 具体位置：Table 4, §4.5 \"Relaxation, Divergence, and SPON\"\n- 问题：在 30% 处，Forward KL (8.81) vs JSD (8.90) 差距仅 0.09 PPL（1.0%），Forward KL vs Reverse KL (9.26) 差距 0.45 PPL（5.1%）。论文引用 mode-covering 理论解释 forward KL 的优越性，但在这个差距水平下，理论叙事的支撑力度有限。只有在 50% 处差距才变得明显（+6.4% JSD, +8.6% RKL）。论文的叙事将 forward KL 选择呈现为一个重要的设计决策，但数据表明它更接近于 implementation detail（30% 差距小到可能被超参调整抹平）。\n- 建议：弱化 forward KL 选择的叙事权重；或增加在更多 sparsity levels 的 ablation 以建立更稳健的趋势。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.4 Eq. 5：$\\mathcal{L}_{\\text{KL}}$ 的求和是 over vocabulary $v$，但没有说明是否 applied at every token position 还是某种平均方式。附录 G 才提到\"summed over the vocabulary $v$ and averaged over sequence positions\"——这应该在正文中明确。\n- Table 2 脚注 ‡：\"Actual sparsity: KL 28.5% vs. TEAL 29.3% at 30%\"——由于 KL 的 Lagrangian 控制器使实际稀疏度偏离目标 5%（Appendix C），所有与 TEAL 的 PPL 比较都存在 0.8pp 的稀疏度差异。虽然 Appendix D 表明这个差异的 PPL 影响小（0.67），但正文应更明确地说明 matched-sparsity 比较。\n- Figure 1 (overview) 画得比较简单，没有展示训练阶段的 Gumbel relaxation 和 Lagrangian controller 的位置，对方法理解的帮助有限。\n- §2 Related Work：SPON 的讨论在 §2 和 §4.5 各出现一次，建议合并。\n- Appendix P \"Oracle Mask Provenance\"：s42 oracle 来自 earlier checkpoint 的问题应在正文 Table 3 caption 中更显著地标注（当前只有 † 号），因为这直接影响 C1 ablation 的可信度。\n\n---\n\n## 主要优势\n\n1. **Target-swap ablation (C1) 设计精巧**：将 KL-derived mask patterns 迁移到 BCE 训练，clean 地分离了 mask pattern quality 和 training objective coupling 的贡献。这是一个有创意且有信息量的控制实验。\n\n2. **对局限性的诚实披露极为罕见**：论文在 abstract 中就承认无加速、在正文中持续标注 \"upper bound\"/\"confound\"/\"not fully orthogonal\"、在 Limitations 中坦承所有负面发现。这种透明度在投稿论文中很少见，值得肯定。\n\n3. **PPL 改善显著且一致**：14.5% at 30%、50% at 50%，跨架构一致（LLaMA、Mistral、Qwen），且 3-seed PPL 的方差极低（CV=0.2%），说明 KL 训练方式确实学到了更好的 mask patterns。\n\n4. **实验覆盖面广**：5 种 loss 排名、3 个架构、6 个 sparsity levels、allocation 策略分析、sensitivity sweeps、OOD 评估、compensation redundancy——附录极为充分。\n\n5. **2D taxonomy (signal type × coupling scope) 为理解稀疏预测方法提供了有用框架**：即使分解不完美，这个分析视角对后续工作有价值。\n\n6. **训练成本极低**：1000 步、单 GPU、~45 分钟——方法的实用门槛非常低。\n\n---\n\n## Questions to Authors\n\nQ1: 是否尝试过在多样化数据（WikiText + 少量数学/代码文本）上训练 predictor？这是验证知识任务退化是否可修复的最直接实验。\n\nQ2: 在 K=4 控制中，如果强制使用 E2E KL 学到的非均匀 allocation（而非让 K=4 自行收敛到 near-uniform），MMLU 异常是否消失？这能直接测试 allocation confound 假设。\n\nQ3: Table 4 中 BCE+Gumbel+Penalty (38.02) 比 BCE+Gumbel-no-penalty (32.22) 更差——为什么添加 sparsity penalty 会让 BCE 表现恶化？这与 KL 方向上 penalty 的帮助形成反差。\n\nQ4: 论文报告 KL predictor 在 L14-L18 形成 protection valley（14-18% sparsity）。这个 pattern 在 Mistral 和 Qwen 上是否也出现？如果是，这可能揭示 SwiGLU 架构的通用属性。\n\nQ5: 考虑到 C1 ablation 显示 mask patterns 携带了大部分质量信息，一个自然的后续是：能否用 KL 训练一个 \"teacher predictor\"，然后用 BCE 训练一个更高效的 \"student predictor\" on KL-derived targets？这可能兼得 KL 的 mask quality 和 BCE 的 training stability。\n\n---\n\n## Missing References\n\n- **CATS** (Lee et al., 2024): §2 提到但 Table 2 未作为 baseline——考虑到 CATS 也是 per-layer adaptive threshold 方法且有 wall-clock speedup 数据，应该在实验中对比或至少讨论为何排除。\n- **MaskLLM** (Fang et al., 2024): §1 和 §2 讨论了与 MaskLLM 的区别（static N:M vs contextual），但没有实验对比——即使 setting 不同，PPL 层面的数字对比可以帮助读者校准结果。\n- **Mixture-of-Depths** (Raposo et al., 2024): §2 引用了但未讨论与 token-level sparsity prediction 的对比——本文的 per-token mask prediction 在概念上与 MoD 的 token routing 有对偶关系。\n\nSources:\n- [ACL Rolling Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-23T01:34:28.096820+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3712
}
```

</details>

---


### Assistant

_source line 1494 · 2026-05-23T01:34:41.025115+00:00_

审稿意见已提交给 Review Director。

**审稿总结**：Overall 3.5（Borderline Conference），置信度 4/5。

核心发现：
- **3 个 Must-Fix**：(1) 知识任务退化随 scale 恶化（14B GSM8K -20pp），机制分析不足；(2) per-layer KL 分解在 50% 稀疏度失效（K=4 比 K=1 更差），signal type vs coupling scope 不正交；(3) 无实际推理加速（+6.4% overhead）
- **5 个 Should-Fix**：downstream 统计力不足（3-seed MMLU σ=9.5）、Table 2 baseline 条件不统一、C1 soft-vs-hard confound、Qwen-14B 评估不完整、forward vs reverse KL 差距在 30% 处微小
- **主要优势**：C1 target-swap ablation 设计精巧、PPL 改善显著一致（14.5%/50%）、对局限性的诚实披露极罕见、实验覆盖面广

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 45

## Round 45

14 recorded events


### User

_source line 1495 · 2026-05-23T01:36:12.012001+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（引用论文中的 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

### Overall: 3.5 (Borderline Conference), Confidence 4/5

### Must-Fix 问题

**N1** [critical] Signal type vs coupling scope 分解存在不可消除的混淆变量
- K=1 per-layer KL 同时改变：(1) 移除 cross-layer gradient coupling, (2) 引入 train-inference mismatch（训练 1/32 layers，推理全部 32）。K=4 仅部分缓解，在 50% 下 K=4 (44.23) 比 K=1 (34.85) 更差，论文自身承认分解"unreliable under the current design"。但 Abstract 和 Conclusion 仍将此作为核心结论。建议限定为"at 30% moderate sparsity, subject to train-inference mismatch confound"，或设计 stop-gradient 实验更干净地隔离 coupling。

**N2** [critical] 知识任务系统性退步与"primary design dimension"强 claim 矛盾
- 8B MMLU −5.2pp, 14B GSM8K −20.1pp, Mistral GSM8K −7.3pp。Abstract 仅说"commonsense gains but knowledge-intensive decline"未量化。Conclusion 归入一句 Limitations。§4.2 的两个假设仅推测无实验验证。"primary design dimension" 只对 PPL 和 commonsense 成立，对知识任务是 inferior。建议限定适用范围并在 Abstract 量化退步幅度。

### Should-Fix 问题

**W1** [warning] 与 MaskLLM 区分需加强，Table 1 遗漏 MaskLLM
- MaskLLM（NeurIPS 2024）共享 frozen weights + learnable masks + KL + Gumbel recipe。三点区分合理但无实验验证。Table 1 Static × Coupled 格仅列 SPON，应纳入 MaskLLM。

**W2** [warning] 14.5% PPL improvement 的引用基准不一致
- Abstract 用 matched sparsity 数字（8.81 vs 10.30, 来自 Appendix），Table 2 中 TEAL uniform 30% 是 10.82。按 Table 2 改进是 18.6%。一级读者验证 Table 2 会发现数字对不上。

**W3** [warning] 缺少 ActTail (arXiv:2603.12272, March 2026)
- 基于 HT-SR 理论的全局 activation sparsity allocation，与本文 per-layer allocation 分析直接相关。

**W4** [warning] 标题/framing 可能产生效率误导
- 标题暗示推理效率贡献，但方法增加 6.4% overhead。论文诚实披露但 framing 可能误导匆忙读者。

**W5** [warning] C1 ablation soft-vs-hard confound 未完全解决
- 二值化 KL logits (>0) 同时改变 target source 和 mask representation。BCE+Gumbel (32.22) vs standard BCE (27.97) 不足以排除 confound（它们用的是 magnitude targets 而非 KL targets）。

### 小问题
- M1: Intro 中 8.6%/6.4% 未标注 sparsity level（来自 50%，30% 差距小得多）
- M2: 术语不一致（output-distribution alignment/objective/coupled objective/KL distillation）
- M3: Table 2 注脚标记过密
- M4: "stable downstream (MMLU 40.7±1.3%)" 相对 dense 65.27% 降 24.5pp，"stable" 指跨 seed 稳定性应澄清
- M5: 页数合规性——Conclusion 可能溢出第 8 页
- M6: 68% divergence 和 32% Jaccard 同句出现易混淆
- M7: 14B GSM8K 退步剧增（-1.3pp → -20.1pp）未深入分析

### 主要优势
1. 系统且诚实的实证框架（5 种 loss, 3 架构, 多 sparsity, 3-seed, OOD, cross-seed consistency）
2. C1 target-swap ablation 设计巧妙
3. PPL 改进显著且跨架构一致
4. Compensation 冗余性发现实用
5. 写作质量整体高，2D taxonomy 有用

### Questions
Q1: stop-gradient 实验能否更干净地隔离 coupling scope？
Q2: Qwen-2.5-14B d_ff=18944 vs LLaMA 14336 的架构差异是否导致 predictor 不匹配？
Q3: 为何 Abstract 用 Appendix matched-sparsity 数字而非 main table？
Q4: K=4 50% PPL=44.23 反常的 gradient interference hypothesis 有无进一步实验支持？

### Missing References
- ActTail (arXiv:2603.12272, March 2026)
- MaskLLM 应在 Table 1 taxonomy 中体现位置

---

请逐条回应以上所有 Must-Fix、Should-Fix 和主要 Questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-23T01:36:57.680725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": "155",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "offset": "155",
    "limit": "35"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-23T01:36:58.192513+00:00_

155	At 30\%, forward KL (8.81) and JSD (8.90) are near-identical, both outperforming reverse KL (9.26) and MSE (18.52$\pm$1.68). % exp_id: kl30_ablation_s42, jsd30_ablation_s42, rkl30_ablation_s42, mse30_uniform_s42, mse30_3seed
156	The near-equivalence of KL and JSD suggests the divergence measure matters less than whether the loss optimizes through the output distribution; cross-layer scope provides additional downstream benefits (\S\ref{sec:perlayer}). % exp_id: bce30_uniform_s42, rkl30_downstream_3seed
157	\paragraph{Per-Layer KL: Decomposing Signal Type and Coupling Scope.}
158	\label{sec:perlayer}
159	To isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.
160	At $K{=}1$, per-layer KL achieves 9.05$\pm$0.02, within 2.7\% of end-to-end KL (8.81$\pm$0.02), while per-layer MSE degrades to 18.52$\pm$1.68 ($2.05\times$ worse). For PPL, signal type\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} accounts for the majority of the gap---an upper bound, as the $K{=}1$ control conflates coupling removal with train--inference mismatch (training 1/32 layers; inference all 32). A 3-seed $K{=}4$ control\footnote{Actual sparsity 29.6\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds this (Appendix~\ref{app:k4_downstream}): \emph{coupling-dominated}---ARC-c (97\% residual gap) and WG (67\%) indicate genuine cross-layer benefits for commonsense; \emph{mismatch-dominated}---PPL (67\% closure) and GSM8K (71\%) gaps largely close; \emph{anomalous}---MMLU exceeds E2E across all seeds (42.7$\pm$1.4 vs.\ 40.7$\pm$1.3), explained by $K{=}4$'s near-uniform allocation matching uni
…[truncated 2902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 511
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-23T01:36:58.243214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1499 · 2026-05-23T01:36:58.343974+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at moderate sparsity (30\%) (upper bound; not fully orthogonal with coupling scope).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1500 · 2026-05-23T01:36:58.394760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1501 · 2026-05-23T01:36:58.445308+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for PPL at moderate sparsity (30\%; signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes task-dependently---substantially for commonsense, marginally for reasoning (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	Code and trained predictors will be released upon acceptance.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-23T01:37:05.068380+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
  "offset": "1",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
    "offset": "1",
    "limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 1503 · 2026-05-23T01:37:05.533906+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to PPL but m
…[truncated 1732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 465
}
```

</details>

---


### Tool call

_source line 1504 · 2026-05-23T01:37:05.652065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
  "offset": "78",
  "limit": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
    "offset": "78",
    "limit": "7"
  }
}
```

</details>

---


### Tool result

_source line 1505 · 2026-05-23T01:37:05.696737+00:00_

78	
79	We use forward KL (mass-covering) rather than reverse KL, as the goal is to preserve the dense model's primary predictions rather than explore alternative modes.
80	In sparsity prediction, mode-covering is critical: false negatives (omitting a rarely but critically active neuron) cascade through downstream layers under global allocation, whereas false positives merely waste capacity; reverse KL's mode-seeking concentrates on high-probability neurons and risks missing compositionally important activations~\cite{wu2025rethinking}.
81	\S\ref{sec:experiments} validates this choice empirically: forward KL outperforms reverse KL by 8.6\% and JSD by 6.4\% (Table~\ref{tab:ablation}).
82	No temperature scaling ($T{=}1$) is applied~\cite{hinton2015distilling}; we distinguish $T$ from the Gumbel temperature $\tau$ (\S\ref{sec:method:gumbel}), which controls mask sharpness rather than logit scaling.
83	
84	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 44
}
```

</details>

---


### Tool call

_source line 1506 · 2026-05-23T01:39:39.159475+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Signal type vs coupling scope 分解存在不可消除的混淆变量**\n\n同意这是论文的核心弱点之一（与我的 N2 一致）。具体证据：\n\n1. §4.5 脚注明确承认 K=1 的 confound：\"the K=1 control conflates coupling removal with train-inference mismatch (training 1/32 layers; inference all 32)\"。\n2. K=4 在 50% 下 PPL=44.23 比 K=1 的 34.85 更差（Table 4），论文自己说\"the signal-type/coupling decomposition unreliable under the current design\"（§4.5 最后一句）。\n3. K=4 在 30% 的 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）被论文归因为 allocation confound（Appendix T），进一步证实两个维度不正交。\n\n但我注意到 Abstract 已加了 qualifier：\"(upper bound; not fully orthogonal with coupling scope)\"，Conclusion 也标注了\"upper bound\"。问题是这些 qualifiers 是否足够——\"accounts for the majority\"仍然是一个较强的表述。\n\n**R2 建议的 stop-gradient 实验**（在 KL 反传时对 downstream Jacobian 做 stop-gradient，保留 output-distribution 目标但切断跨层梯度耦合）比 K=1/K=4 设计更干净，我赞同这是一个有建设性的修改方向。不过这需要对训练代码做 non-trivial 的修改，作为 revision 任务的合理性需评估。\n\n---\n\n**[AGREE] R2-N2: 知识任务系统性退步与\"primary design dimension\"强 claim 矛盾**\n\n同意（与我的 N1 一致）。补充 R2 未详细展开的证据：\n\n1. 退步的**跨 scale 恶化趋势**：8B GSM8K -1.3pp → 14B GSM8K -20.1pp（Table 2 vs Table 13, Appendix K），退步幅度增长 15 倍，这不是噪声可解释的。\n2. Abstract 的表述\"commonsense gains but knowledge-intensive decline\"确实过于轻描淡写——未量化，读者无法从 abstract 判断退步程度。对比：Introduction 第 17 行明确给出了 14B 数字\"GSM8K −20.1pp, σ=5.2pp; MMLU −2.8pp\"，但 abstract 回避了这些。\n3. \"primary design dimension\"这个 claim 严格来说对 PPL 是成立的（PPL 改善一致、跨架构、3-seed 方差极低）。但论文将此 claim 作为标题级别的主要结论呈现，而在 PPL 之外的维度上方法是 inferior，这构成 overclaim。\n\nR2 建议\"限定适用范围并在 Abstract 量化退步幅度\"是合理且可操作的。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 与 MaskLLM 区分需加强，Table 1 遗漏 MaskLLM**\n\n同意。Table 1（taxonomy, §3.7）的 Static × Coupled 格中仅列 SPON，但 MaskLLM 也属于此格（static N:M masks + KL training）。§2 Related Work 虽然讨论了 MaskLLM 并给出三点区分（static vs contextual, N:M vs unstructured, input-independent vs input-dependent），但这些区分均无实验验证。将 MaskLLM 纳入 Table 1 是一个简单且应该做的修正。\n\n不过我补充一点：MaskLLM 的 setting 差异（static weight masks vs contextual activation masks）确实足够大，不要求在 Table 2 中做 baseline 对比。两者的核心区别在于 MaskLLM 的 mask 不随输入变化，这在 contextual sparsity 场景下是根本性不同。Table 1 加注即可。\n\n---\n\n**[AGREE] R2-W2: 14.5% PPL improvement 的引用基准不一致**\n\n同意，这是一个呈现清晰度问题。\n\n- Abstract 使用 matched-sparsity 对比：8.81 vs 10.30（both at 28.5%），数字来自 Appendix D 和 Figure 2 caption。\n- Table 2 中 TEAL uniform 30% = 10.82（名义 30% 稀疏度），按此计算改进是 18.6%。\n- Introduction 第 14 行也用 matched-sparsity 数字：\"reduces TEAL's perplexity by 14.5% at matched sparsity (8.81 vs. 10.30, both at 28.5%)\"。\n\n论文选择 matched-sparsity 对比在方法论上是合理的（KL 实际稀疏度 28.5% ≠ 名义 30%，Appendix C Table 9），但 **primary claim 引用 appendix 而非 main table 的数字确实容易让读者困惑**。一级读者查 Table 2 找不到 10.30 这个数字。建议在 Table 2 caption 或正文中明确标注 matched-sparsity 对比的来源。\n\n---\n\n**[REBUT] R2-W3: 缺少 ActTail (arXiv:2603.12272, March 2026)**\n\n我无法验证这篇论文的存在性和内容。arXiv ID 2603.12272 的格式对应 2026 年 3 月，距投稿仅 2 个月。如果这篇论文确实提出了基于 HT-SR 理论的全局 activation sparsity allocation，它与本文的 per-layer allocation 分析（§4.6, Appendix L）相关，应在 Related Work §2 \"Training-Free Activation Sparsity\" 段落中引用。\n\n但我认为这不应作为 Should-Fix——遗漏一篇 2 个月前的 arXiv 预印本（非 peer-reviewed）不构成重大缺陷。降为 Minor 更合适。\n\n---\n\n**[AGREE] R2-W4: 标题/framing 可能产生效率误导**\n\n部分同意。标题\"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"本身不直接承诺效率，但\"Sparsity Prediction\"在 LLM 语境下强烈暗示推理加速。论文在 Introduction 最后一段和 Appendix A 中诚实地披露了 +6.4% overhead（这一点我在自己的审稿中也肯定了），但标题和 abstract 确实可能误导快速浏览的读者。\n\n不过，我认为这更接近 framing 调整而非 substantive 问题。论文的核心贡献是 analytical（理解训练目标如何影响稀疏预测质量），而非 practical efficiency。如果论文更明确地在 abstract 开头就定位为 analytical study（类似 Introduction 第 18 行\"This paper is primarily an empirical study...\"），这个 concern 就会消解。\n\n---\n\n**[AGREE] R2-W5: C1 ablation soft-vs-hard confound 未完全解决**\n\n同意（与我的 W3 一致）。R2 正确指出 BCE+Gumbel (32.22) vs standard BCE (27.97) 的对比使用的是 **magnitude targets**，而非 KL targets。这意味着该控制实验测试的是\"softness 对 magnitude-based masks 有无帮助\"，而非\"softness 对 KL-derived masks 有无帮助\"。要完整控制 soft-vs-hard confound，需要的是：BCE+Gumbel **on KL-derived targets** vs BCE hard **on KL-derived targets**。\n\n但我补充：C1 的核心 claim 是\"KL-discovered mask patterns transfer to simpler training\"（§4.4），而非\"training objective doesn't matter\"。即使存在 soft-vs-hard confound，C1 的 ≤0.79pp gap（Table 3, 50% s42）已经建立了 mask pattern transferability 的强证据。confound 影响的是对 *why* transfer works 的解释，而非 transfer *whether* works 的结论。\n\n---\n\n### 小问题\n\n**[AGREE] R2-M1: §3.4 中 8.6%/6.4% 未标注 sparsity level**\n\n同意。§3.4 第 81 行：\"forward KL outperforms reverse KL by 8.6% and JSD by 6.4% (Table 4)\"——这些数字来自 Table 4 的 50% 列（11.79 vs 12.80=8.6%, 11.79 vs 12.54=6.4%）。在 30%，Forward KL vs JSD 差距仅 1.0%（8.81 vs 8.90），vs RKL 仅 5.1%（8.81 vs 9.26）。不标注 sparsity level 会让读者高估 forward KL 在 moderate sparsity 下的优势。\n\n小修正：R2 定位为\"Intro 中\"，实际出现在 §3.4 Method 中。但实质性观点正确。\n\n---\n\n**[AGREE] R2-M2: 术语不一致**\n\n同意。论文交替使用 output-distribution alignment / output-distribution objective / coupled objective / KL distillation / end-to-end KL 指代同一概念，增加了阅读认知负担。建议统一为 \"output-distribution KL\" 或 \"end-to-end KL distillation\"。\n\n---\n\n**[AGREE] R2-M3: Table 2 注脚标记过密**\n\n同意。Table 2 有 †, ‡, ±, * 四种标注加上 caption 中大量说明文字，视觉负担重。但信息本身是必要的——问题在于呈现方式而非内容。\n\n---\n\n**[AGREE] R2-M4: \"stable downstream\" 用词模糊**\n\n同意。Introduction 第 14 行\"stable downstream (MMLU 40.7±1.3%)\"——MMLU 相对 dense 65.27% 下降了 24.5pp，这里的\"stable\"指跨 seed 稳定性（σ=1.3），不是指性能保持。应改为\"reproducible across seeds\"或\"low cross-seed variance\"以避免误读。\n\n---\n\n**[REBUT] R2-M5: 页数合规性——Conclusion 可能溢出第 8 页**\n\n查看 PDF：第 8 页底部是 §5 Conclusion 的开头，第 9 页顶部有 Conclusion 最后 1-2 行溢出，随后是 Limitations。按 EMNLP 2026 规则，main text（含 Conclusion）限 8 页，Limitations 不计入。如果 Conclusion 确实溢出到第 9 页，这是**格式违规**，需要修复。\n\n但我将此定级为 Minor 而非 Should-Fix——这是一个通过微调排版即可修复的问题（压缩 Table 2 间距或缩短 Conclusion 即可）。不影响内容评判。\n\n实际上仔细看 PDF 第 8 页，Conclusion 部分占了大约 6 行正文，第 9 页顶部可能有约 1-2 行溢出。这确实是违规的，但属于 camera-ready 级别的修复。R2 的 concern 有效，但不改变评分。\n\n---\n\n**[AGREE] R2-M6: 68% divergence 和 32% Jaccard 同句出现易混淆**\n\n同意。Introduction 第 10 行：\"patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)\"——68% = Jaccard distance, 32% = Jaccard similarity = 1 - 0.68。同一句用两种互补度量确实造成混淆。建议统一使用 Jaccard distance 或明确注明\"Jaccard similarity 32% (distance 68%)\"。\n\n---\n\n**[AGREE] R2-M7: 14B GSM8K 退步剧增未深入分析**\n\n同意（与我的 W4 一致）。§4.6 对 14B 退步的讨论仅一句：\"suggests a systematic property of distribution-matching\"。8B→14B GSM8K 退步从 -1.3pp 飙升到 -20.1pp，这个 15 倍的恶化缺乏任何机制分析。可能的因素包括：(1) 14B 的 d_ff=18944（vs 8B 的 14336）导致 predictor 瓶颈 d_b=128 的压缩比更大；(2) 14B 上数学推理能力更强，被稀疏化破坏的绝对量更大。论文应至少讨论这些可能性。\n\n---\n\n### Questions 回应\n\n**R2-Q1 (stop-gradient 实验)**: 同意这是一个比 K=1/K=4 更干净的隔离方案。具体实现：在 KL loss 反传时，对 $\\partial \\mathbf{z}_{\\text{sparse}} / \\partial \\tilde{m}_j^{(\\ell)}$ 中来自 $\\ell' > \\ell$ 层的梯度做 detach，保留本层 mask→output 的梯度路径但切断跨层耦合。这保持了 output-distribution 目标（signal type 不变）同时移除 coupling。\n\n**R2-Q2 (Qwen d_ff=18944 vs LLaMA 14336)**: 这是一个有效的 concern。Predictor 结构 Linear(4096→128→d_ff) 中，d_ff=18944 时第二层参数量增加 32%（128×18944=2.42M vs 128×14336=1.84M per layer）。论文 Appendix K 的 Table 13 caption 没有说明是否调整了 d_b。如果使用相同的 d_b=128，压缩比从 4096:128:14336 变为 5120:128:18944（假设 Qwen 的 d_model=5120），bottleneck 压力更大。这可能部分解释 14B 上的退化。\n\n**R2-Q3 (Abstract 用 Appendix 数字)**: 同意 R2 的 concern，如我在 W2 回应中所述。\n\n**R2-Q4 (K=4 50% gradient interference hypothesis)**: 论文没有提供任何实验支持（我在自己的 N2 中也指出了这一点）。这是一个纯粹假设性的解释。要验证需要：(1) 在训练过程中测量 K=4 vs E2E 的 layer-wise gradient conflict（例如 cosine similarity between layer groups 的梯度），(2) 尝试 K=8, K=16 看是否有单调趋势。\n\n---\n\n### 总结\n\nR2 与我的审稿在核心问题上高度一致：**per-layer KL 分解的 confound（R2-N1 ≈ 我的 N2）**和**知识任务退步（R2-N2 ≈ 我的 N1）**是两个最重要的 Must-Fix。R2 额外指出的 **baseline 引用不一致（W2）**和 **MaskLLM taxonomy 遗漏（W1）**是合理的 Should-Fix。我对 R2 的 W3（ActTail 引用）持保留意见——2 个月前的 arXiv 预印本不应作为 Should-Fix。\n\n两份审稿的核心分歧不大，但侧重点不同：我更强调缺乏实际加速（我的 N3），R2 更关注分解框架的 claim 强度和呈现一致性。综合来看，论文需要：(1) 弱化 signal type/coupling decomposition 的 claim 强度，(2) 量化知识任务退步并限定方法适用范围，(3) 修复 baseline 引用和 taxonomy 遗漏。如果这些修改完成，Findings 级别接收是合理的。",
  "reviewer_id": "1",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Signal type vs coupling scope 分解存在不可消除的混淆变量**\n\n同意这是论文的核心弱点之一（与我的 N2 一致）。具体证据：\n\n1. §4.5 脚注明确承认 K=1 的 confound：\"the K=1 control conflates coupling removal with train-inference mismatch (training 1/32 layers; inference all 32)\"。\n2. K=4 在 50% 下 PPL=44.23 比 K=1 的 34.85 更差（Table 4），论文自己说\"the signal-type/coupling decomposition unreliable under the current design\"（§4.5 最后一句）。\n3. K=4 在 30% 的 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）被论文归因为 allocation confound（Appendix T），进一步证实两个维度不正交。\n\n但我注意到 Abstract 已加了 qualifier：\"(upper bound; not fully orthogonal with coupling scope)\"，Conclusion 也标注了\"upper bound\"。问题是这些 qualifiers 是否足够——\"accounts for the majority\"仍然是一个较强的表述。\n\n**R2 建议的 stop-gradient 实验**（在 KL 反传时对 downstream Jacobian 做 stop-gradient，保留 output-distribution 目标但切断跨层梯度耦合）比 K=1/K=4 设计更干净，我赞同这是一个有建设性的修改方向。不过这需要对训练代码做 non-trivial 的修改，作为 revision 任务的合理性需评估。\n\n---\n\n**[AGREE] R2-N2: 知识任务系统性退步与\"primary design dimension\"强 claim 矛盾**\n\n同意（与我的 N1 一致）。补充 R2 未详细展开的证据：\n\n1. 退步的**跨 scale 恶化趋势**：8B GSM8K -1.3pp → 14B GSM8K -20.1pp（Table 2 vs Table 13, Appendix K），退步幅度增长 15 倍，这不是噪声可解释的。\n2. Abstract 的表述\"commonsense gains but knowledge-intensive decline\"确实过于轻描淡写——未量化，读者无法从 abstract 判断退步程度。对比：Introduction 第 17 行明确给出了 14B 数字\"GSM8K −20.1pp, σ=5.2pp; MMLU −2.8pp\"，但 abstract 回避了这些。\n3. \"primary design dimension\"这个 claim 严格来说对 PPL 是成立的（PPL 改善一致、跨架构、3-seed 方差极低）。但论文将此 claim 作为标题级别的主要结论呈现，而在 PPL 之外的维度上方法是 inferior，这构成 overclaim。\n\nR2 建议\"限定适用范围并在 Abstract 量化退步幅度\"是合理且可操作的。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 与 MaskLLM 区分需加强，Table 1 遗漏 MaskLLM**\n\n同意。Table 1（taxonomy, §3.7）的 Static × Coupled 格中仅列 SPON，但 MaskLLM 也属于此格（static N:M masks + KL training）。§2 Related Work 虽然讨论了 MaskLLM 并给出三点区分（static vs contextual, N:M vs unstructured, input-independent vs input-dependent），但这些区分均无实验验证。将 MaskLLM 纳入 Table 1 是一个简单且应该做的修正。\n\n不过我补充一点：MaskLLM 的 setting 差异（static weight masks vs contextual activation masks）确实足够大，不要求在 Table 2 中做 baseline 对比。两者的核心区别在于 MaskLLM 的 mask 不随输入变化，这在 contextual sparsity 场景下是根本性不同。Table 1 加注即可。\n\n---\n\n**[AGREE] R2-W2: 14.5% PPL improvement 的引用基准不一致**\n\n同意，这是一个呈现清晰度问题。\n\n- Abstract 使用 matched-sparsity 对比：8.81 vs 10.30（both at 28.5%），数字来自 Appendix D 和 Figure 2 caption。\n- Table 2 中 TEAL uniform 30% = 10.82（名义 30% 稀疏度），按此计算改进是 18.6%。\n- Introduction 第 14 行也用 matched-sparsity 数字：\"reduces TEAL's perplexity by 14.5% at matched sparsity (8.81 vs. 10.30, both at 28.5%)\"。\n\n论文选择 matched-sparsity 对比在方法论上是合理的（KL 实际稀疏度 28.5% ≠ 名义 30%，Appendix C Table 9），但 **primary claim 引用 appendix 而非 main table 的数字确实容易让读者困惑**。一级读者查 Table 2 找不到 10.30 这个数字。建议在 Table 2 caption 或正文中明确标注 matched-sparsity 对比的来源。\n\n---\n\n**[REBUT] R2-W3: 缺少 ActTail (arXiv:2603.12272, March 2026)**\n\n我无法验证这篇论文的存在性和内容。arXiv ID 2603.12272 的格式对应 2026 年 3 月，距投稿仅 2 个月。如果这篇论文确实提出了基于 HT-SR 理论的全局 activation sparsity allocation，它与本文的 per-layer allocation 分析（§4.6, Appendix L）相关，应在 Related Work §2 \"Training-Free Activation Sparsity\" 段落中引用。\n\n但我认为这不应作为 Should-Fix——遗漏一篇 2 个月前的 arXiv 预印本（非 peer-reviewed）不构成重大缺陷。降为 Minor 更合适。\n\n---\n\n**[AGREE] R2-W4: 标题/framing 可能产生效率误导**\n\n部分同意。标题\"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"本身不直接承诺效率，但\"Sparsity Prediction\"在 LLM 语境下强烈暗示推理加速。论文在 Introduction 最后一段和 Appendix A 中诚实地披露了 +6.4% overhead（这一点我在自己的审稿中也肯定了），但标题和 abstract 确实可能误导快速浏览的读者。\n\n不过，我认为这更接近 framing 调整而非 substantive 问题。论文的核心贡献是 analytical（理解训练目标如何影响稀疏预测质量），而非 practical efficiency。如果论文更明确地在 abstract 开头就定位为 analytical study（类似 Introduction 第 18 行\"This paper is primarily an empirical study...\"），这个 concern 就会消解。\n\n---\n\n**[AGREE] R2-W5: C1 ablation soft-vs-hard confound 未完全解决**\n\n同意（与我的 W3 一致）。R2 正确指出 BCE+Gumbel (32.22) vs standard BCE (27.97) 的对比使用的是 **magnitude targets**，而非 KL targets。这意味着该控制实验测试的是\"softness 对 magnitude-based masks 有无帮助\"，而非\"softness 对 KL-derived masks 有无帮助\"。要完整控制 soft-vs-hard confound，需要的是：BCE+Gumbel **on KL-derived targets** vs BCE hard **on KL-derived targets**。\n\n但我补充：C1 的核心 claim 是\"KL-discovered mask patterns transfer to simpler training\"（§4.4），而非\"training objective doesn't matter\"。即使存在 soft-vs-hard confound，C1 的 ≤0.79pp gap（Table 3, 50% s42）已经建立了 mask pattern transferability 的强证据。confound 影响的是对 *why* transfer works 的解释，而非 transfer *whether* works 的结论。\n\n---\n\n### 小问题\n\n**[AGREE] R2-M1: §3.4 中 8.6%/6.4% 未标注 sparsity level**\n\n同意。§3.4 第 81 行：\"forward KL outperforms reverse KL by 8.6% and JSD by 6.4% (Table 4)\"——这些数字来自 Table 4 的 50% 列（11.79 vs 12.80=8.6%, 11.79 vs 12.54=6.4%）。在 30%，Forward KL vs JSD 差距仅 1.0%（8.81 vs 8.90），vs RKL 仅 5.1%（8.81 vs 9.26）。不标注 sparsity level 会让读者高估 forward KL 在 moderate sparsity 下的优势。\n\n小修正：R2 定位为\"Intro 中\"，实际出现在 §3.4 Method 中。但实质性观点正确。\n\n---\n\n**[AGREE] R2-M2: 术语不一致**\n\n同意。论文交替使用 output-distribution alignment / output-distribution objective / coupled objective / KL distillation / end-to-end KL 指代同一概念，增加了阅读认知负担。建议统一为 \"output-distribution KL\" 或 \"end-to-end KL distillation\"。\n\n---\n\n**[AGREE] R2-M3: Table 2 注脚标记过密**\n\n同意。Table 2 有 †, ‡, ±, * 四种标注加上 caption 中大量说明文字，视觉负担重。但信息本身是必要的——问题在于呈现方式而非内容。\n\n---\n\n**[AGREE] R2-M4: \"stable downstream\" 用词模糊**\n\n同意。Introduction 第 14 行\"stable downstream (MMLU 40.7±1.3%)\"——MMLU 相对 dense 65.27% 下降了 24.5pp，这里的\"stable\"指跨 seed 稳定性（σ=1.3），不是指性能保持。应改为\"reproducible across seeds\"或\"low cross-seed variance\"以避免误读。\n\n---\n\n**[REBUT] R2-M5: 页数合规性——Conclusion 可能溢出第 8 页**\n\n查看 PDF：第 8 页底部是 §5 Conclusion 的开头，第 9 页顶部有 Conclusion 最后 1-2 行溢出，随后是 Limitations。按 EMNLP 2026 规则，main text（含 Conclusion）限 8 页，Limitations 不计入。如果 Conclusion 确实溢出到第 9 页，这是**格式违规**，需要修复。\n\n但我将此定级为 Minor 而非 Should-Fix——这是一个通过微调排版即可修复的问题（压缩 Table 2 间距或缩短 Conclusion 即可）。不影响内容评判。\n\n实际上仔细看 PDF 第 8 页，Conclusion 部分占了大约 6 行正文，第 9 页顶部可能有约 1-2 行溢出。这确实是违规的，但属于 camera-ready 级别的修复。R2 的 concern 有效，但不改变评分。\n\n---\n\n**[AGREE] R2-M6: 68% divergence 和 32% Jaccard 同句出现易混淆**\n\n同意。Introduction 第 10 行：\"patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)\"——68% = Jaccard distance, 32% = Jaccard similarity = 1 - 0.68。同一句用两种互补度量确实造成混淆。建议统一使用 Jaccard distance 或明确注明\"Jaccard similarity 32% (distance 68%)\"。\n\n---\n\n**[AGREE] R2-M7: 14B GSM8K 退步剧增未深入分析**\n\n同意（与我的 W4 一致）。§4.6 对 14B 退步的讨论仅一句：\"suggests a systematic property of distribution-matching\"。8B→14B GSM8K 退步从 -1.3pp 飙升到 -20.1pp，这个 15 倍的恶化缺乏任何机制分析。可能的因素包括：(1) 14B 的 d_ff=18944（vs 8B 的 14336）导致 predictor 瓶颈 d_b=128 的压缩比更大；(2) 14B 上数学推理能力更强，被稀疏化破坏的绝对量更大。论文应至少讨论这些可能性。\n\n---\n\n### Questions 回应\n\n**R2-Q1 (stop-gradient 实验)**: 同意这是一个比 K=1/K=4 更干净的隔离方案。具体实现：在 KL loss 反传时，对 $\\partial \\mathbf{z}_{\\text{sparse}} / \\partial \\tilde{m}_j^{(\\ell)}$ 中来自 $\\ell' > \\ell$ 层的梯度做 detach，保留本层 mask→output 的梯度路径但切断跨层耦合。这保持了 output-distribution 目标（signal type 不变）同时移除 coupling。\n\n**R2-Q2 (Qwen d_ff=18944 vs LLaMA 14336)**: 这是一个有效的 concern。Predictor 结构 Linear(4096→128→d_ff) 中，d_ff=18944 时第二层参数量增加 32%（128×18944=2.42M vs 128×14336=1.84M per layer）。论文 Appendix K 的 Table 13 caption 没有说明是否调整了 d_b。如果使用相同的 d_b=128，压缩比从 4096:128:14336 变为 5120:128:18944（假设 Qwen 的 d_model=5120），bottleneck 压力更大。这可能部分解释 14B 上的退化。\n\n**R2-Q3 (Abstract 用 Appendix 数字)**: 同意 R2 的 concern，如我在 W2 回应中所述。\n\n**R2-Q4 (K=4 50% gradient interference hypothesis)**: 论文没有提供任何实验支持（我在自己的 N2 中也指出了这一点）。这是一个纯粹假设性的解释。要验证需要：(1) 在训练过程中测量 K=4 vs E2E 的 layer-wise gradient conflict（例如 cosine similarity between layer groups 的梯度），(2) 尝试 K=8, K=16 看是否有单调趋势。\n\n---\n\n### 总结\n\nR2 与我的审稿在核心问题上高度一致：**per-layer KL 分解的 confound（R2-N1 ≈ 我的 N2）**和**知识任务退步（R2-N2 ≈ 我的 N1）**是两个最重要的 Must-Fix。R2 额外指出的 **baseline 引用不一致（W2）**和 **MaskLLM taxonomy 遗漏（W1）**是合理的 Should-Fix。我对 R2 的 W3（ActTail 引用）持保留意见——2 个月前的 arXiv 预印本不应作为 Should-Fix。\n\n两份审稿的核心分歧不大，但侧重点不同：我更强调缺乏实际加速（我的 N3），R2 更关注分解框架的 claim 强度和呈现一致性。综合来看，论文需要：(1) 弱化 signal type/coupling decomposition 的 claim 强度，(2) 量化知识任务退步并限定方法适用范围，(3) 修复 baseline 引用和 taxonomy 遗漏。如果这些修改完成，Findings 级别接收是合理的。",
    "reviewer_id": "1",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1507 · 2026-05-23T01:39:42.926695+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3767
}
```

</details>

---


### Assistant

_source line 1508 · 2026-05-23T01:39:53.044095+00:00_

交叉回应已提交。

要点概括：
- R2 的两个 Must-Fix（N1 分解 confound、N2 知识任务退步）与我的 N2、N1 高度一致，均标注 [AGREE]
- 5 个 Should-Fix 中 4 个 [AGREE]（MaskLLM taxonomy、baseline 引用不一致、标题 framing、C1 soft-hard confound），1 个 [REBUT]（ActTail 引用——2 个月前的 arXiv 预印本不应作为 Should-Fix）
- 7 个 Minor 中 6 个 [AGREE]，1 个 [REBUT]（M5 页数溢出实质上是格式微调问题，不影响评分）
- 两份审稿核心判断一致：论文 PPL 贡献扎实，但 decomposition claim 需弱化、知识退步需量化限定、Findings 级别接收合理

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1"
}
```

</details>

---


## Round 46

## Round 46

62 recorded events


### User

_source line 1509 · 2026-05-23T07:19:13.936092+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查论文的 **方法严谨性 + 实验设计**。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）
- **截止日期**: 2026-05-25
- **格式要求**: ACL 模板，Long Paper 正文上限 8 页（不含 references 和 limitations/ethics）
- **匿名规则**: Double-blind
- **评分标准**: ARR Overall Assessment (1-5 scale)，其中 4 = Conference（可被主会议接收），3 = Findings

## 论文文件
- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf`
- 图表目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/figures/paper/`

## 你的审查侧重

**核心关注点**：
1. **Per-layer KL 分解的实验有效性**：K=1 的 train-inference mismatch (1/32 vs 32/32) 是否污染了 "signal type accounts for majority" 的结论？K=4 correction 是否充分？K-curve 数据（多数 single-seed）的统计可靠性。
2. **C1 target-swap ablation 的 confound 控制**：soft→hard mask binarization 是否引入 representation confound？s42 oracle 来自 earlier checkpoint 的影响。BCE+Gumbel(32.22) vs BCE(27.97) 的解释是否充分？
3. **统计严谨性**：3-seed 下游指标的置信区间是否足以支撑方向性结论（MMLU 30% global σ=9.5）？PPL 作为 primary metric 的合理性论证。
4. **Table 2 对比公平性**：BCE 30% uniform vs KL 的对比条件是否充分控制（steps、allocation）？BCE 50% 用 2700 steps 的 iso-compute 论证。
5. **Knowledge-task regression 的机制分析**：跨架构/跨 scale 一致退步（8B MMLU -5.2pp, 14B GSM8K -20pp）的解释是否充分？C4 控制实验的结论是否 over-interpreted？
6. **实验覆盖度**：缺少生成任务评估、seq_len 固定 2048、无 batched inference。Limitations 覆盖是否充分？

**输出格式**：
- Strengths（逐条，带证据）
- Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级，引用具体 Section/Table/Figure）
- Questions（需要作者回答的问题）
- Missing References（如有）
- Overall Assessment（1-5 ARR scale + 简短理由）
- Confidence（1-5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-23T07:19:21.167461+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1511 · 2026-05-23T07:19:21.217992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1512 · 2026-05-23T07:19:25.635322+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1513 · 2026-05-23T07:19:25.685871+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-23T07:19:29.709161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 1515 · 2026-05-23T07:19:31.768512+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
  "pages": "1-10",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
    "pages": "1-10",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1516 · 2026-05-23T07:19:37.203839+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I found comprehensive information about ACL ARR 2026 reviewer guidelines and scoring criteria. Here are the key details:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Assessment Score

The Overall assessm
…[truncated 1155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7494
}
```

</details>

---


### Tool result

_source line 1517 · 2026-05-23T07:19:38.562311+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6793
}
```

</details>

---


### Tool call

_source line 1518 · 2026-05-23T07:19:46.148181+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. Focus on: soundness, excitement, overall assessment scales, confidence scale, and any other scoring dimensions. List each dimension with its full scale description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring dimensions, and their scales. Focus on: soundness, excitement, overall assessment scales, confidence scale, and any other scoring dimensions. List each dimension with its full scale description."
  }
}
```

</details>

---


### Tool call

_source line 1519 · 2026-05-23T07:19:47.503576+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
  "pages": "11-20",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
    "pages": "11-20",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-23T07:19:48.058419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1521 · 2026-05-23T07:19:48.560141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-23T07:19:49.563366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1523 · 2026-05-23T07:19:50.065476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-23T07:19:50.366717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1525 · 2026-05-23T07:19:51.319978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1526 · 2026-05-23T07:19:51.771725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---
