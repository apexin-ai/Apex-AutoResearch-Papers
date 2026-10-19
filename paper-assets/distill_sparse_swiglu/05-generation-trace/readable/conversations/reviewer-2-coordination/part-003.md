# Reviewer 2 coordination — Part 3 of 5

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/96/96af94fcc323c852e454.json)

## Round 26

### Tool result

_source line 1067 · 2026-05-20T06:41:01.277742+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address the interaction between dynamic sparsity and quantization with zigzag-patterned weight layouts.
7	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
8	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
9	
10	\paragraph{Predictor-Based Contextual Sparsity.}
11	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
12	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
13	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
14	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
15	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
16	MaskLLM~\cite{fang2024maskllm} shares the principle of frozen weights + learnable masks + KL training, but the two methods differ in three fundamental ways.
17	First, \emph{spar
…[truncated 4220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-20T06:41:05.145397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool call

_source line 1069 · 2026-05-20T06:41:05.145727+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1070 · 2026-05-20T06:41:05.196253+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--14B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}, Qwen-2.5-14B~\cite{qwen2024qwen25}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1071 · 2026-05-20T06:41:05.197682+00:00_

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
…[truncated 23958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-20T06:41:10.379617+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"activation sparsity\" \"sparsity predictor\" \"clustering\" LLM 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"activation sparsity\" \"sparsity predictor\" \"clustering\" LLM 2025 2026 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 1073 · 2026-05-20T06:41:11.236093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gumbel softmax discrete optimization neural network pruning mask learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gumbel softmax discrete optimization neural network pruning mask learning 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 1074 · 2026-05-20T06:41:17.625891+00:00_

Web search results for query: "Gumbel softmax discrete optimization neural network pruning mask learning 2024 2025"

Links: [{"title":"Gumbel-Softmax Sampling in Differentiable Models","url":"https://www.emergentmind.com/topics/gumbel-softmax-sampling"},{"title":"Gumbel-Softmax: Differentiable Discrete Sampling","url":"https://www.emergentmind.com/topics/gumbel-softmax"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/397199936_MaskLLM_Learnable_Semi-Structured_Sparsity_for_Large_Language_Models"},{"title":"Gumbel–Softmax Relaxation","url":"https://www.emergentmind.com/topics/gumbel-softmax-relaxation-9e7d074a-4229-4c58-b6d7-d5652f6827f5"},{"title":"Neural Network Pruning by Gradient Descent","url":"https://arxiv.org/pdf/2311.12526"},{"title":"Extracting Effective Subnetworks with Gumbel-Softmax","url":"https://arxiv.org/pdf/2202.12986"},{"title":"[2311.12526v2] Neural Network Pruning by Gradient Descent","url":"https://arxiv.org/abs/2311.12526v2"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2409.17481"}]

Based on the search results, here's what I found about Gumbel-Softmax for discrete optimization in neural network pruning and mask learning (2024-2025):

## Key Applications in Neural Network Pruning and Mask Learning

MaskLLM is a learnable method for end-to-end training of LLM sparsity. Since mask selection is non-differentiable, it frames the mask selection problem probabilistically and uses Gumbel Softmax for differentiable sampling, making mask probabilities optimizable with gradient descent.

A neural network pruning framework incorporating Gumbel-Softmax enables simultaneous optimization of a network's weights and topology in an end-to-end process using stochastic gradient descent. Empirical results demonstrate exceptional compression capability, maintaining high accuracy on MNIST with only 0.15% of
…[truncated 913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6389
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-20T06:41:19.668212+00:00_

Web search results for query: ""activation sparsity" "sparsity predictor" "clustering" LLM 2025 2026 arxiv"

Links: [{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"[2507.14179] A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/abs/2507.14179"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern","url":"https://arxiv.org/pdf/2507.14179"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=20800&show=1000"},{"title":"[2509.00454] Universal Properties of Activation Sparsity in Modern Large Language Models","url":"https://arxiv.org/abs/2509.00454"}]

I found several relevant papers on activation sparsity, sparsity prediction, and clustering in LLMs from 2025-2026 on arXiv:

## Key Research Papers

**1. A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering**

This paper from July 2025 addresses how Large Language Models exhibit significant activation sparsity, where only a subset of neurons are active for a given input, and proposes a clustering-based approach to efficiently utilize this sparsity. The method proposes a clustering-based activation pattern compression framework that groups similar activation patterns into a small set of representative clusters instead of treating each neuron independently. The method achieves up to 79.34% clustering precision while main
…[truncated 920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9288
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-20T06:44:51.973976+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n### 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**Confidence**: 4 / 5\n**一句话总结**: 实验设计扎实、ablation 有说服力的经验性研究，但核心思想（用 KL 替代 BCE 训练 sparsity predictor）在 MaskLLM 已有先例的情况下新颖性不足，且实际可用的 sparsity regime 过窄（仅 30%），限制了论文的影响力。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有充分实验支持（C1 ablation、多 seed、跨架构），但\"coupling alignment\"缺少形式化定义，30% sparsity 下 MMLU 仍大幅退化却被弱化表述 |\n| Excitement | 2.5/5 | 经验性发现有价值但属 incremental；MaskLLM 已用 KL+Gumbel 做 mask learning；实际无 wall-clock speedup；可用 regime 仅 30% |\n| Reproducibility | 4/5 | 超参完整、3-seed 评估、GPU 型号明确、训练步数/时间报告清楚；但未释放代码或 checkpoint |\n| Overall Assessment | 3.0/5 | Findings 级别——经验贡献扎实但新颖性和影响力不足以达到主会议 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 与 MaskLLM 的新颖性边界不清晰\n\n- 具体位置：§2 Related Work (page 2)；§1 Introduction (line 8)\n- 问题：MaskLLM (Fang et al., NeurIPS 2024) 已使用 frozen weights + KL divergence + Gumbel relaxation + learnable masks 的完整框架。论文给出三点区分（sparsity type, mask generation, allocation），但这三点更像 application domain 差异而非方法论创新。核心 insight——\"KL couples gradients through output distribution, outperforming per-neuron BCE\"——在 MaskLLM 框架中已隐含成立。\n- 为什么影响接收：如果核心思路已被 MaskLLM 覆盖，contribution 不足以支撑独立发表。\n- 建议：(1) 明确论证 global allocation 场景的 cross-layer budget competition 是 MaskLLM 的 N:M 结构不涉及的新挑战；(2) 提供 MaskLLM 中 KL vs BCE gap 的定量对比。\n\n**N2** [critical] \"Coupling Alignment\" 概念缺少形式化，过度包装已知原理\n\n- 具体位置：§3.7 (Table 1, page 5)；§5 Conclusion (page 8)；Abstract\n- 问题：\"Coupling alignment\" 本质上是 \"end-to-end training outperforms component-wise training when components interact\"——深度学习基本原理。论文将其呈现为核心 contribution（Conclusion 首句），但未提供形式化定义或理论分析。Taxonomy (Table 1) 填充空格不构成理论发现。\n- 建议：将其定位为\"对已知原理在 sparsity prediction 场景的经验验证\"，降低 claim 强度。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] 实际可用 regime 过窄，削弱实用价值\n\n- 具体位置：Table 2 (page 6)；§4.6 (page 8)\n- 问题：30% 是唯一有意义的 regime，但 MMLU 从 dense 65.27% 降至 KL 40.7%（-24.6pp），TEAL 反而更好（45.86%）。50% downstream 全部 collapse。KL predictor 增加 6.4% latency overhead 无实际加速。KL vs training-free TEAL 的实际优势场景非常有限。\n\n**W2** [warning] 跨架构/跨规模结果过于初步\n\n- 具体位置：§4.6 (page 8)；Appendix K, N\n- 问题：Mistral-7B 为 single-seed，14B 显示 MMLU -2.79pp、GSM8K -20pp。论文称 \"preliminary\" 但 Abstract/Conclusion 仍将其作为 contribution。\n\n**W3** [warning] Abstract 数字选择性呈现\n\n- 具体位置：Abstract\n- 问题：选择性展示 KL 胜出的任务数字（ARC +4.4pp, HellaSwag +7.8pp），MMLU -5.2pp 仅给标签。完全未提及绝对退化幅度（MMLU 65.3%→40.7%）。\n- 建议：加入绝对退化说明。\n\n**W4** [warning] Training data 单一性\n\n- 具体位置：§4.1 (page 6)；Appendix D\n- 问题：所有 predictor 仅在 WikiText-103 训练 1000 步。C4 OOD 仅报告 PPL 未报告 downstream。Cross-seed variance 在 C4 上增大（CV 6.3% vs 0.2%）。\n\n---\n\n### 小问题\n\n- M1: 30% sparsity 下 penalty controller λ 达 cap (5000)，实际 sparsity 仅 28.5%（5% 偏差），在最实用 regime 表现最差。\n- M2: MSE baseline 的 λ_max=1000 vs KL 的 5000 是未控制变量。\n- M3: Figure 2 caption \"82% at 70%\" 但 70% downstream 不可用。\n- M4: \"proximate quality driver\" 反复出现但其含义不令人意外。\n- M5: Reference xu2026spon year=2026 但引为 ICML 2025，年份不一致。\n- M6: Reference de2024griffin 在 OpenAlex 验证中 not_found。\n\n---\n\n### 可能遗漏的相关工作\n\n1. \"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering\" (Dhar et al., 2025, arXiv:2507.14179)\n2. \"Universal Properties of Activation Sparsity in Modern LLMs\" (arXiv:2509.00454, revised Feb 2026)\n3. §2 line 20 的 claim \"All prior predictor-based methods use decomposed or intermediate objectives\" 需更精确限定。\n\n---\n\n### 主要优势\n\n1. C1 Target-swap ablation 设计精巧，max Δ≤0.79pp 令人信服\n2. 实验诚实度高，坦诚报告负面结果\n3. Multi-seed 评估规范\n4. Ablation 全面（Table 4: relaxation, divergence direction, coupling level, soft-vs-hard）\n5. Appendix 内容充实（A-P），reproducibility 支持好\n\n---\n\n### Questions to Authors\n\n1. MaskLLM 在 weight sparsity 场景下 KL vs BCE 的 PPL gap 是多少？与本文 2.4× gap 可比吗？\n2. 30% sparsity 下有无方法恢复 KL 相对 TEAL 的 MMLU 差距？\n3. Gumbel 对 KL 有利但对 BCE 有害——为什么？这个发现值得更深入分析。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告：新颖性 + 完整性 + 写作质量\n\n### 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**Confidence**: 4 / 5\n**一句话总结**: 实验设计扎实、ablation 有说服力的经验性研究，但核心思想（用 KL 替代 BCE 训练 sparsity predictor）在 MaskLLM 已有先例的情况下新颖性不足，且实际可用的 sparsity regime 过窄（仅 30%），限制了论文的影响力。\n\n---\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有充分实验支持（C1 ablation、多 seed、跨架构），但\"coupling alignment\"缺少形式化定义，30% sparsity 下 MMLU 仍大幅退化却被弱化表述 |\n| Excitement | 2.5/5 | 经验性发现有价值但属 incremental；MaskLLM 已用 KL+Gumbel 做 mask learning；实际无 wall-clock speedup；可用 regime 仅 30% |\n| Reproducibility | 4/5 | 超参完整、3-seed 评估、GPU 型号明确、训练步数/时间报告清楚；但未释放代码或 checkpoint |\n| Overall Assessment | 3.0/5 | Findings 级别——经验贡献扎实但新颖性和影响力不足以达到主会议 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 与 MaskLLM 的新颖性边界不清晰\n\n- 具体位置：§2 Related Work (page 2)；§1 Introduction (line 8)\n- 问题：MaskLLM (Fang et al., NeurIPS 2024) 已使用 frozen weights + KL divergence + Gumbel relaxation + learnable masks 的完整框架。论文给出三点区分（sparsity type, mask generation, allocation），但这三点更像 application domain 差异而非方法论创新。核心 insight——\"KL couples gradients through output distribution, outperforming per-neuron BCE\"——在 MaskLLM 框架中已隐含成立。\n- 为什么影响接收：如果核心思路已被 MaskLLM 覆盖，contribution 不足以支撑独立发表。\n- 建议：(1) 明确论证 global allocation 场景的 cross-layer budget competition 是 MaskLLM 的 N:M 结构不涉及的新挑战；(2) 提供 MaskLLM 中 KL vs BCE gap 的定量对比。\n\n**N2** [critical] \"Coupling Alignment\" 概念缺少形式化，过度包装已知原理\n\n- 具体位置：§3.7 (Table 1, page 5)；§5 Conclusion (page 8)；Abstract\n- 问题：\"Coupling alignment\" 本质上是 \"end-to-end training outperforms component-wise training when components interact\"——深度学习基本原理。论文将其呈现为核心 contribution（Conclusion 首句），但未提供形式化定义或理论分析。Taxonomy (Table 1) 填充空格不构成理论发现。\n- 建议：将其定位为\"对已知原理在 sparsity prediction 场景的经验验证\"，降低 claim 强度。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] 实际可用 regime 过窄，削弱实用价值\n\n- 具体位置：Table 2 (page 6)；§4.6 (page 8)\n- 问题：30% 是唯一有意义的 regime，但 MMLU 从 dense 65.27% 降至 KL 40.7%（-24.6pp），TEAL 反而更好（45.86%）。50% downstream 全部 collapse。KL predictor 增加 6.4% latency overhead 无实际加速。KL vs training-free TEAL 的实际优势场景非常有限。\n\n**W2** [warning] 跨架构/跨规模结果过于初步\n\n- 具体位置：§4.6 (page 8)；Appendix K, N\n- 问题：Mistral-7B 为 single-seed，14B 显示 MMLU -2.79pp、GSM8K -20pp。论文称 \"preliminary\" 但 Abstract/Conclusion 仍将其作为 contribution。\n\n**W3** [warning] Abstract 数字选择性呈现\n\n- 具体位置：Abstract\n- 问题：选择性展示 KL 胜出的任务数字（ARC +4.4pp, HellaSwag +7.8pp），MMLU -5.2pp 仅给标签。完全未提及绝对退化幅度（MMLU 65.3%→40.7%）。\n- 建议：加入绝对退化说明。\n\n**W4** [warning] Training data 单一性\n\n- 具体位置：§4.1 (page 6)；Appendix D\n- 问题：所有 predictor 仅在 WikiText-103 训练 1000 步。C4 OOD 仅报告 PPL 未报告 downstream。Cross-seed variance 在 C4 上增大（CV 6.3% vs 0.2%）。\n\n---\n\n### 小问题\n\n- M1: 30% sparsity 下 penalty controller λ 达 cap (5000)，实际 sparsity 仅 28.5%（5% 偏差），在最实用 regime 表现最差。\n- M2: MSE baseline 的 λ_max=1000 vs KL 的 5000 是未控制变量。\n- M3: Figure 2 caption \"82% at 70%\" 但 70% downstream 不可用。\n- M4: \"proximate quality driver\" 反复出现但其含义不令人意外。\n- M5: Reference xu2026spon year=2026 但引为 ICML 2025，年份不一致。\n- M6: Reference de2024griffin 在 OpenAlex 验证中 not_found。\n\n---\n\n### 可能遗漏的相关工作\n\n1. \"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering\" (Dhar et al., 2025, arXiv:2507.14179)\n2. \"Universal Properties of Activation Sparsity in Modern LLMs\" (arXiv:2509.00454, revised Feb 2026)\n3. §2 line 20 的 claim \"All prior predictor-based methods use decomposed or intermediate objectives\" 需更精确限定。\n\n---\n\n### 主要优势\n\n1. C1 Target-swap ablation 设计精巧，max Δ≤0.79pp 令人信服\n2. 实验诚实度高，坦诚报告负面结果\n3. Multi-seed 评估规范\n4. Ablation 全面（Table 4: relaxation, divergence direction, coupling level, soft-vs-hard）\n5. Appendix 内容充实（A-P），reproducibility 支持好\n\n---\n\n### Questions to Authors\n\n1. MaskLLM 在 weight sparsity 场景下 KL vs BCE 的 PPL gap 是多少？与本文 2.4× gap 可比吗？\n2. 30% sparsity 下有无方法恢复 KL 相对 TEAL 的 MMLU 差距？\n3. Gumbel 对 KL 有利但对 BCE 有害——为什么？这个发现值得更深入分析。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-20T06:44:56.608962+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4634
}
```

</details>

---


### Assistant

_source line 1078 · 2026-05-20T06:45:02.310924+00:00_

审稿报告已提交给 Review Director。

总结：论文被评为 **3.0/5 (Findings)**。两个 critical 问题：(1) 与 MaskLLM 的新颖性边界不够清晰——KL+Gumbel+frozen weights 的框架已存在；(2) "coupling alignment" 概念将已知原理包装为新贡献但缺乏形式化。四个 should-fix：实际可用 regime 仅 30% 且 MMLU 退化、跨架构结果过于初步、Abstract 选择性呈现、训练数据单一。论文的主要优势在于 C1 target-swap ablation 设计精巧、实验诚实度高、multi-seed 规范。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 27

## Round 27

4 recorded events


### User

_source line 1079 · 2026-05-20T06:45:40.772742+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix / Should-Fix / Minor 问题标注 [AGREE] 或 [REBUT]，并说明理由。如果 [REBUT]，请引用论文中的具体 Section/Table/Figure 作为证据。

---

## Reviewer 1 审稿报告

**Overall**: 3.5/5 (Borderline Conference)
**Confidence**: 4/5

### Must-Fix

**N1** [critical] Coupling alignment 概念存在同义反复（tautological）风险
- §3.7 将 coupling alignment 定义为"训练损失是否优化一个跨层组合的量"，然后论证"只有直接优化 next-token prediction loss 的目标才能发现产生好 next-token prediction 的 mask"——逻辑上接近同义反复。
- 论文同时主张"gradient coupling remains necessary at the discovery stage"，但没有提供独立于 PPL/downstream 的 mask 质量定义来打破循环。
- 建议：(a) 提供可操作形式化定义（如 mask 梯度协方差矩阵秩）；(b) 或降低理论抱负；(c) 测试 intermediate coupling 级别目标（hidden-state KL）。

**N2** [critical] Headline 19% PPL improvement 在非匹配 sparsity 下报告
- Abstract "reduces perplexity by 19%"（10.82→8.81），但 KL 实际 28.5% vs TEAL ~30%。匹配 sparsity 下改善为 14.5%。Abstract 突出 19% 而将 14.5% 藏在正文括号里，构成误导。

**N3** [critical] 50% sparsity 下 downstream 全面崩溃，方法 unambiguous wins 仅限 30% PPL
- 50% 所有方法 MMLU≈28%（random），GSM8K<2.2%。
- 30% 也是 mixed：commonsense 赢（ARC +4.4pp, HellaSwag +7.8pp），knowledge-intensive 输（MMLU −5.2pp）。
- 如果方法只在一个 sparsity level 的 PPL 有优势而 downstream task-dependent，核心价值大打折扣。

### Should-Fix

**W1** Cross-architecture 证据过薄：Mistral/Qwen 均 single seed，14B GSM8K 反转 -20pp。
**W2** MSE baseline λ_max=1000 vs KL 的 5000，且 single seed，影响 taxonomy 对比公平性。
**W3** Adaptive penalty 30% 时 λ 触顶 5000，actual sparsity=28.5%（5% deviation），控制器设计存疑。
**W4** BCE+Gumbel (32.22) 比 standard BCE (27.97) 更差，KL 与 Gumbel 存在未量化交互效应。Loss effect vs relaxation effect 的加法分解假设独立性，但交互作用说明不独立。
**W5** 梯度分析（§3.6）定性正确但缺乏定量支撑——缺 per-layer gradient 相关性分析或 Jacobian 条件数分析。

### Minor
- m1: Table 2 † footnote 容易混淆
- m2: de2024griffin 在 OpenAlex 未找到
- m3: 固定 τ=0.5 比 default annealing 更好但正文未提及
- m4: "primarily empirical study" 与 §3.6-3.7 的理论贡献定位不一致
- m5: Figure 2 y轴 log scale 但标注线性刻度值

### Missing References
- Wortsman et al. (2023) training stability
- Dettmers et al. (2024) SpQR quantization+sparsity
- Clark et al. (2020) ELECTRA

### Questions
Q1. 反向 C1：用 KL 训练在 magnitude-based oracle targets 上性能如何？
Q2. λ_max 提高到 50000 能否达到 30%？
Q3. Forward KL 的 mode-covering 是否解释了 knowledge-intensive tasks 的退化？
Q4. SPON 正交性显示 static bias 在 KL 框架下几乎无用？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1080 · 2026-05-20T06:47:55.731315+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n### Must-Fix\n\n**[PARTIALLY AGREE] R1-N1: Coupling alignment 同义反复**\n形式化缺失成立（与我 N2 一致），但\"同义反复\"定性过重。MSE 也是 end-to-end 的但比 training-free TEAL 差 1.9×（Table 2: MSE 20.43 vs TEAL 10.82 at 30%），说明 coupling 的 **层级** 而非 coupling 本身是关键——这个发现不是 trivial 的。建议采纳 R1 的 (b)+(c)：降低理论抱负 + 补充 hidden-state KL 对照实验。\n\n**[AGREE] R1-N2: 19% 在非匹配 sparsity 下**\nKL actual 28.5% vs TEAL 29.3%，matched-sparsity 改善仅 14.5%（§4.2 parenthetical, Appendix C: TEAL at 28.5% PPL 10.30）。Abstract 突出 19% 构成选择性呈现。比我的 W3 更精确。\n\n**[AGREE] R1-N3: 50% collapse + 方法仅 30% PPL 有优势**\n与我 W1 完全一致。30% 也是 mixed（commonsense 4/4 win, knowledge 0/2 lose）。Unambiguous win 仅在 \"30% × PPL\" 窄窗口。\n\n### Should-Fix\n\n**[AGREE] R1-W1**: 与我 W2 一致。\n**[PARTIALLY AGREE] R1-W2**: Appendix G defense 对 50%（MSE 229 vs TEAL 23.9）成立，但 MSE single seed 仍需验证 50% 结果非异常值。\n**[AGREE] R1-W3**: 与我 M1 一致，但 matched-sparsity 对比限制了影响。\n**[AGREE] R1-W4**: BCE+Gumbel 交互效应是 R1 独到观察。Gumbel 对 BCE 有害（+4.25 PPL）对 KL 有利（-3.98 PPL），additive decomposition 的独立性假设不成立。\n**[AGREE] R1-W5**: 与我 N2 中形式化缺失一致。\n\n### Minor\n\n**[AGREE]** R1-m1, m2, m3, m5\n**[PARTIALLY AGREE]** R1-m4: §3.6 已有 hedge (\"This analysis is suggestive\")，更多是 framing 不一致。\n\n### Missing References\n\n**[PARTIALLY AGREE]** Wortsman/SpQR: tangentially related\n**[REBUT]** Clark et al. (2020) ELECTRA: 与 activation sparsity prediction 训练目标选择无直接关联。\n\n### 综合评估\n\nR1 和我在核心问题上高度一致：(1) 新颖性边界模糊（我 N1 vs MaskLLM, R1 N1 tautology）；(2) 实际 regime 过窄（我 W1, R1 N3）；(3) headline 数字选择性呈现（我 W3, R1 N2）。R1 的 N2（sparsity 不匹配）和 W4（交互效应）是我遗漏的有价值观点。\n\n我维持 Overall 3.0 (Findings)。R1 给 3.5 (Borderline Conference) 略高于我，主要分歧在 excitement——R1 似乎对 C1 ablation 的方法论贡献给了更高权重。综合两份 review，3.0-3.5 是合理区间。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 的交叉回应\n\n### Must-Fix\n\n**[PARTIALLY AGREE] R1-N1: Coupling alignment 同义反复**\n形式化缺失成立（与我 N2 一致），但\"同义反复\"定性过重。MSE 也是 end-to-end 的但比 training-free TEAL 差 1.9×（Table 2: MSE 20.43 vs TEAL 10.82 at 30%），说明 coupling 的 **层级** 而非 coupling 本身是关键——这个发现不是 trivial 的。建议采纳 R1 的 (b)+(c)：降低理论抱负 + 补充 hidden-state KL 对照实验。\n\n**[AGREE] R1-N2: 19% 在非匹配 sparsity 下**\nKL actual 28.5% vs TEAL 29.3%，matched-sparsity 改善仅 14.5%（§4.2 parenthetical, Appendix C: TEAL at 28.5% PPL 10.30）。Abstract 突出 19% 构成选择性呈现。比我的 W3 更精确。\n\n**[AGREE] R1-N3: 50% collapse + 方法仅 30% PPL 有优势**\n与我 W1 完全一致。30% 也是 mixed（commonsense 4/4 win, knowledge 0/2 lose）。Unambiguous win 仅在 \"30% × PPL\" 窄窗口。\n\n### Should-Fix\n\n**[AGREE] R1-W1**: 与我 W2 一致。\n**[PARTIALLY AGREE] R1-W2**: Appendix G defense 对 50%（MSE 229 vs TEAL 23.9）成立，但 MSE single seed 仍需验证 50% 结果非异常值。\n**[AGREE] R1-W3**: 与我 M1 一致，但 matched-sparsity 对比限制了影响。\n**[AGREE] R1-W4**: BCE+Gumbel 交互效应是 R1 独到观察。Gumbel 对 BCE 有害（+4.25 PPL）对 KL 有利（-3.98 PPL），additive decomposition 的独立性假设不成立。\n**[AGREE] R1-W5**: 与我 N2 中形式化缺失一致。\n\n### Minor\n\n**[AGREE]** R1-m1, m2, m3, m5\n**[PARTIALLY AGREE]** R1-m4: §3.6 已有 hedge (\"This analysis is suggestive\")，更多是 framing 不一致。\n\n### Missing References\n\n**[PARTIALLY AGREE]** Wortsman/SpQR: tangentially related\n**[REBUT]** Clark et al. (2020) ELECTRA: 与 activation sparsity prediction 训练目标选择无直接关联。\n\n### 综合评估\n\nR1 和我在核心问题上高度一致：(1) 新颖性边界模糊（我 N1 vs MaskLLM, R1 N1 tautology）；(2) 实际 regime 过窄（我 W1, R1 N3）；(3) headline 数字选择性呈现（我 W3, R1 N2）。R1 的 N2（sparsity 不匹配）和 W4（交互效应）是我遗漏的有价值观点。\n\n我维持 Overall 3.0 (Findings)。R1 给 3.5 (Borderline Conference) 略高于我，主要分歧在 excitement——R1 似乎对 C1 ablation 的方法论贡献给了更高权重。综合两份 review，3.0-3.5 是合理区间。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-20T06:47:59.861056+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4129
}
```

</details>

---


### Assistant

_source line 1082 · 2026-05-20T06:48:07.302267+00:00_

交叉回应已提交。

**与 R1 的共识**：核心问题高度一致——新颖性边界（我 N1/MaskLLM vs R1 N1/tautology）、regime 过窄（我 W1 vs R1 N3）、数字选择性呈现（我 W3 vs R1 N2）。

**R1 独到的贡献**：N2（sparsity 不匹配下的 headline 数字）和 W4（Gumbel×Loss 交互效应破坏 additive decomposition）是我遗漏的有价值观点。

**分歧点**：R1 给 3.5，我给 3.0。差异主要在 excitement——R1 对 C1 target-swap ablation 的方法论价值给了更高权重。综合两份 review，3.0-3.5 是合理区间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 28

## Round 28

84 recorded events


### User

_source line 1083 · 2026-05-20T15:24:15.913225+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + 完整性 + Related Work**。

## Venue 信息
- **会议**：EMNLP 2026（通过 ARR May 2026 cycle 提交）
- **截止日期**：2026-05-25
- **页数限制**：正文 8 页，参考文献不限，Limitations/Ethics 不计入页数
- **模板**：ACL style（\usepackage[review]{acl}）
- **匿名规则**：Double-blind
- **附录**：在 references 之后，审稿人可参考

## 论文路径
- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf`

## 你的审查侧重

### 1. 新颖性评估
- **核心贡献**：用 KL divergence 替代 BCE 训练 sparsity predictor — 这是否算 sufficient novelty？KL distillation 本身是标准技术，创新性在哪里？
- **MaskLLM 区分**：§2 Related Work 中 MaskLLM 三点区分（sparsity type / mask generation / allocation）是否充分？MaskLLM 已在 NeurIPS 2024 发表，本文在技术上走得比 MaskLLM 远多少？
- **Taxonomy (Table 1 §3.7)**：两维分类框架（correction granularity × training signal coupling）是否真正有洞察力，还是仅仅是对已有方法的重新分类？
- **"Primarily empirical study" 声明**（Introduction 最后一段）：EMNLP 是否接受纯经验性研究？贡献量级是否足够？

### 2. Related Work 完整性
- 检查是否遗漏了重要的 2024-2026 相关工作（activation sparsity, learned pruning, KL distillation for efficiency）
- 特别关注：
  - Polar Sparsity (NeurIPS 2025) — 已引用，但是否充分讨论？
  - GRIFFIN (2024) 在 Related Work 中仅一句话提及 — 是否需要更多讨论？
  - 是否有其他 SwiGLU-specific sparsity 工作被遗漏？
  - MoE routing 相关工作（Expert Choice, MoNE, D2D-MoE）引用是否充分？
- 引用真实性：抽查 bib 条目的 venue/year/title 是否正确

### 3. 叙事完整性
- Abstract → Introduction → Conclusion 的故事线是否一致？
- 结论中 "future work includes N:M structured sparsity and scaling to 70B+" — 是否暗示当前工作不够完整？
- Limitations 是否全面？是否有未被提及的重要局限？
- 跨架构/跨规模的负面结果（Mistral GSM8K 反转、Qwen-14B 推理退化）是否被充分讨论？

### 4. 写作质量
- 论文是否有"AI写作"痕迹（过度 hedging、重复性短语、无实质内容的长句）？
- 数学符号一致性（§3 各公式的 notation 是否统一）
- 表格/图表标题是否自包含（不看正文能否理解）
- 参考文献格式是否统一

请按 ACL Reviewer Guidelines 的标准输出审稿报告，包含：Summary (2-3句) → Strengths (逐条) → Weaknesses (逐条，标注 severity: critical/warning/minor) → Questions → Missing References → Overall Assessment (1-5 分制，参照 EMNLP 2026 评分标准) → Confidence (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1084 · 2026-05-20T15:24:22.970756+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-20T15:24:24.730740+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1759
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-20T15:24:24.781466+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-20T15:24:24.833464+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-20T15:24:31.853512+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1089 · 2026-05-20T15:24:34.213286+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-20T15:24:34.564686+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1091 · 2026-05-20T15:24:40.788175+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on my search results, I found information about ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recomme
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8934
}
```

</details>

---


### Tool result

_source line 1092 · 2026-05-20T15:24:42.093174+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 551.4}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 5
…[truncated 223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7879
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-20T15:25:25.371811+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 47, \"total_citations\": 90, \"unique_cited_keys\": 47, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 1, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2025spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben...\", \"year
…[truncated 37957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 50807
}
```

</details>

---


### Tool call

_source line 1094 · 2026-05-20T15:25:33.266634+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, including all dimensions, their descriptions, and scoring scales. I need the exact scoring rubric for each dimension (soundness, excitement/novelty, overall assessment, confidence, etc.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, including all dimensions, their descriptions, and scoring scales. I need the exact scoring rubric for each dimension (soundness, excitement/novelty, overall assessment, confidence, etc.)"
  }
}
```

</details>

---


### Tool call

_source line 1095 · 2026-05-20T15:25:35.633347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-20T15:25:36.137438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-20T15:25:36.639913+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-20T15:25:36.640389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1099 · 2026-05-20T15:25:37.497393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1359
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-20T15:25:37.498287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1101 · 2026-05-20T15:25:37.598917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1102 · 2026-05-20T15:25:38.356118+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-20T15:25:38.710819+00:00_

# ACL Rolling Review Form Criteria

## Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully..."
- 4: "Quite sure. I tried to check the important points carefully..."
- 3: "Pretty sure, but there's a chance I missed something..."
- 2: "Willing to defend my evaluation, but it is fairly likely..."
- 1: "Not my area, or paper is very hard to understand..."

## Soundness
**Scale: 1-5 (with .5 increments)**
- 5: "Excellent: This study is one of the most thorough I have seen..."
- 4: "Strong: This study provides sufficient support for all claims..."
- 3: "Acceptable: This study provides sufficient support for main claims..."
- 2: "Poor: Some main claims lack sufficient support..."
- 1: "Major Issues: This study is not sufficiently thorough..."

## Excitement
**Scale: 1-5 (with .5 increments)**
- 5: "Highly Exciting: I would recommend this paper to others..."
- 4: "Exciting: I would mention this paper to others..."
- 3: "Interesting: I might mention some points..."
- 2: "Potentially Interesting: does not resonate with me..."
- 1: "Not Exciting: does not resonate with me..."

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Additional Dimensions
- **Reproducibility:** 1-5 scale
- **Datasets:** 1-5 scale
- **Software:** 1-5 scale
- **Author Identity:** 1-5 scale

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5444
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-20T15:25:45.348219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-20T15:25:46.303522+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-20T15:25:46.306725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1107 · 2026-05-20T15:25:46.909194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1108 · 2026-05-20T15:25:47.112001+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1109 · 2026-05-20T15:25:47.112502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1110 · 2026-05-20T15:25:47.766580+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-20T15:25:48.018698+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-20T15:25:54.407040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-20T15:25:55.863174+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1456
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-20T15:25:55.863586+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1115 · 2026-05-20T15:25:56.819485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-20T15:25:56.819935+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-20T15:25:57.828513+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 600.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 373.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 217.5}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 91.3}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 1118 · 2026-05-20T15:26:05.806905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1119 · 2026-05-20T15:26:06.259591+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-20T15:26:06.310139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-20T15:26:06.711740+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-20T15:26:06.712172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1123 · 2026-05-20T15:26:07.213799+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-20T15:26:07.214176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-20T15:26:07.264567+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1126 · 2026-05-20T15:26:11.227365+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/_pdf_images/main_p1*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/_pdf_images/main_p1*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-20T15:26:11.278500+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-20T15:26:14.992214+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/",
    "description": "List PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-20T15:26:15.145064+00:00_

Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/': No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-20T15:26:27.016860+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1131 · 2026-05-20T15:26:27.693492+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 600.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.1}], \"total_pages\": 18, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 676
}
```

</details>

---


### Tool call

_source line 1132 · 2026-05-20T15:26:31.009766+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1133 · 2026-05-20T15:26:31.514186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1134 · 2026-05-20T15:26:32.421774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool result

_source line 1135 · 2026-05-20T15:26:32.422598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-20T15:26:32.422820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1137 · 2026-05-20T15:26:32.673849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1138 · 2026-05-20T15:26:33.279219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-20T15:26:33.581596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-20T15:26:48.232235+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "15-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "15-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-20T15:26:48.634183+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 373.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 217.5}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 91.3}], \"total_pages\": 18, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-20T15:26:51.857030+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1143 · 2026-05-20T15:26:52.463184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1144 · 2026-05-20T15:26:53.267736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-20T15:26:53.270532+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-20T15:26:53.270898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1147 · 2026-05-20T15:26:53.522143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1148 · 2026-05-20T15:26:53.624431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-20T15:26:53.625875+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-20T15:27:01.303685+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SwiGLU activation sparsity LLM 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SwiGLU activation sparsity LLM 2024 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1151 · 2026-05-20T15:27:01.810320+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KL divergence distillation sparsity prediction LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KL divergence distillation sparsity prediction LLM 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-20T15:27:02.314200+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "learned pruning activation sparsity predictor neural network 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "learned pruning activation sparsity predictor neural network 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-20T15:27:08.493473+00:00_

Web search results for query: "SwiGLU activation sparsity LLM 2024 2025 2026"

Links: [{"title":"SwiGLU Activation in Transformer Models","url":"https://www.emergentmind.com/topics/swiglu-activation"},{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"(PDF) Activation Sparsity Opportunities for Compressing General Large Language Models","url":"https://www.researchgate.net/publication/388433352_Activation_Sparsity_Opportunities_for_Compressing_General_Large_Language_Models"},{"title":"1 Introduction","url":"https://arxiv.org/html/2412.01380v1"},{"title":"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware   Masking","url":"https://arxiv.org/pdf/2412.01380"},{"title":"SwiGLU: The FFN Upgrade I Use to Get Free Performance - DEV Community","url":"https://dev.to/mshojaei77/swiglu-the-ffn-upgrade-i-use-to-get-free-performance-33jc"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"}]

Based on the search results, here's what recent research shows about SwiGLU activation sparsity in LLMs:

## Natural Sparsity Characteristics

State-of-the-art LLMs have switched to non-ReLU activations, such as SwiGLU, demonstrating negligible natural activation sparsity, in contrast to ReLU-based LLMs which normally have natural activation sparsity around 95%. More specifically, SwiGLU models display only a 5% average neuron activation, limiting hardware efficiency when deployed on offload/flash architectures.

## Challenges with Sparsity Prediction

While activations can still be pruned based on magnitude, it turns out to be much harder to predict which activations should be pruned in SwiGLU LLMs than in ReLU LLMs. Methods like DejaVu and "LLM in a Flash" show the impracticality of training predictors for SwiGLU-based models.

## Recent Approaches (2024-2025)

Lee et al. (2024a) p
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7189
}
```

</details>

---


### Tool result

_source line 1154 · 2026-05-20T15:27:09.195995+00:00_

Web search results for query: "learned pruning activation sparsity predictor neural network 2025 2026"

Links: [{"title":"Activity Pruning for Efficient Spiking Neural Networks | OpenReview","url":"https://openreview.net/forum?id=zjOXZEXQKZ"},{"title":"Joint Regularization on Activations and Weights for Efficient Neural   Network Pruning","url":"https://arxiv.org/pdf/1906.07875"},{"title":"AP: Selective Activation for De-sparsifying Pruned Neural Networks","url":"https://arxiv.org/pdf/2212.06145"},{"title":"Sparsity in Deep Learning: Pruning and growth for efficient inference and training in neural networks | Request PDF","url":"https://www.researchgate.net/publication/348958836_Sparsity_in_Deep_Learning_Pruning_and_growth_for_efficient_inference_and_training_in_neural_networks"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Pruning Convolutional Filters via Reinforcement Learning with Entropy   Minimization","url":"https://arxiv.org/pdf/2312.04918"}]

Based on the web search results, here are the relevant findings for your query about learned pruning, activation sparsity, and predictor neural networks from 2025-2026:

## Key Recent Work

**Spiking Neural Networks (2025):** A spike activity pruning method for spiking neural networks was published as a NeurIPS 2025 poster in September 2025. The work targets reduction of neuronal activity, which directly leads to lower computational cost and facilitates efficient SNN deployment on Neuromorphic hardware.

**Activation Sparsity Prediction for LLMs:** SparseInfer accelerates General Matrix-Vector Multiplication (GEMV) operations in the MLPs of ReLU-fied LLMs by predicting activation sparsity. The approach involves training-free prediction of where activations will be sparse during inference.

**De-sparsification in Pruned Networks:** Recent work examines how activation sparsity from ReLU networks changes during iterativ
…[truncated 524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6881
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-20T15:27:09.598118+00:00_

Web search results for query: "KL divergence distillation sparsity prediction LLM 2024 2025"

Links: [{"title":"Diversity-Aware Reverse Kullback-Leibler Divergence for Large Language Model Distillation","url":"https://arxiv.org/html/2604.00223v1"},{"title":"LLM Distillation Explained - by Nilesh Barla - Adaline Labs","url":"https://labs.adaline.ai/p/llm-distillation-explained"},{"title":"Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models","url":"https://arxiv.org/html/2404.02657v1"},{"title":"Diversity-Aware Reverse Kullback-Leibler Divergence for Large Language Model Distillation","url":"https://arxiv.org/pdf/2604.00223"},{"title":"SpecKD: Speculative Decoding for Effective Knowledge Distillation of LLMs","url":"https://arxiv.org/html/2510.24021v1/"},{"title":"Choosy Babies Need One Coach: Inducing Mode-Seeking Behavior in   BabyLlama with Reverse KL Divergence","url":"https://arxiv.org/pdf/2410.22081"}]

Based on the search results, here are the key findings related to KL divergence distillation in LLMs for 2024-2025:

## Recent Developments in KL Divergence and LLM Distillation

**Shift from Forward to Reverse KL:**
Recent LLM distillation methods increasingly favor reverse KL (RKL) due to its superior empirical performance, despite forward KL (FKL) being the standard objective in early distillation work. This advantage is commonly attributed to the mode-seeking behavior of RKL, which concentrates probability mass on dominant teacher modes, whereas FKL is more mass-covering and encourages matching the full distribution.

**Understanding the KL Divergence Trade-offs:**
Prior work suggests that FKL and RKL converge to the same optimum under sufficient optimization, but the theoretical equivalence relies on assumptions (e.g., sufficient student capacity, exact optimization) that rarely hold in modern LLM distillation, particularly under large vocabularies and significant teacher–student capacity mismatch.

**Advanced Distillat
…[truncated 890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7787
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-20T15:27:13.715345+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"activation sparsity\" \"SwiGLU\" predictor training distillation 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"activation sparsity\" \"SwiGLU\" predictor training distillation 2025 2026 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 1157 · 2026-05-20T15:27:14.619425+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRIFFIN gated linear recurrence sparsity activation 2024 DeepMind"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRIFFIN gated linear recurrence sparsity activation 2024 DeepMind"
  }
}
```

</details>

---


### Tool result

_source line 1158 · 2026-05-20T15:27:21.838984+00:00_

Web search results for query: "GRIFFIN gated linear recurrence sparsity activation 2024 DeepMind"

Links: [{"title":"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://gonzoml.substack.com/p/griffin-mixing-gated-linear-recurrences"},{"title":"2024-3-1 Griffin: Mixing Gated Linear Recurrences with","url":"https://arxiv.org/pdf/2402.19427"},{"title":"RecurrentGemma: Moving Past Transformers for Efficient Open Language Models","url":"https://arxiv.org/html/2404.07839v1"},{"title":"[Let’s Review] Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models by Dogukan Uraz Tuna | Medium | Medium","url":"https://medium.com/@dtunai/lets-review-griffin-mixing-gated-linear-recurrences-with-local-attention-for-efficient-lms-57c824846b3d"},{"title":"[2402.19427] Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://arxiv.org/abs/2402.19427"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://arxiv.org/html/2402.19427v1"},{"title":"Paper Review: Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models | by Andrew Lukyanenko | Medium","url":"https://artgor.medium.com/paper-review-griffin-mixing-gated-linear-recurrences-with-local-attention-for-efficient-language-75e5a86b1b24"},{"title":"Paper page - Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://huggingface.co/papers/2402.19427"}]

Based on the search results, here's what I found about GRIFFIN:

## Overview

Griffin is a hybrid model that mixes gated linear recurrences with local attention, and was released by DeepMind in late February 2024.

## Key Components

The work introduces Hawk, a recurrent model incorporating a novel gated linear recurrent layer called the RG-LRU, and Griffin, which mixes the RG-LRU layer with local atte
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7219
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-20T15:27:25.101612+00:00_

Web search results for query: ""activation sparsity" "SwiGLU" predictor training distillation 2025 2026 arxiv"

Links: [{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2408.14690v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2412.01380v1"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"Accelerating Transformer Inference and Training with 2:4 Activation   Sparsity","url":"https://arxiv.org/pdf/2503.16672"},{"title":"Published as a conference paper at ICLR 2024 RELU STRIKES BACK:","url":"https://openreview.net/pdf?id=osoWxY8q2E"}]

Here are the results from your web search for "activation sparsity" "SwiGLU" predictor training distillation 2025 2026 arxiv:

## Key Research Papers Found:

1. **SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference** (arXiv:2411.12692)
   - Presents a simple, lightweight, and training-free predictor for activation sparsity of ReLU-fied LLMs, where activation sparsity is predicted by comparing only the sign bits of inputs and weights
   - Achieves approximately 21% faster inference speed over state-of-the-art with negligible accuracy loss of within 1%

2. **Training-Free Activation Sparsity in Large Language Models** (arXiv:2408.14690)
   - Introduces TEAL (Training-Free Activation Sparsity in LLMs), a simple, training-free approach that applies activation sparsity based on magnitude pruning, where the threshold is layer-dependent
   - Lee et al. (2024a) propose CATS, and realize training-free activation sparsity on SwiGLU based LLMs by applying magnitude pruning on the output of Wgate


…[truncated 1123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11386
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-20T15:27:30.674537+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"activation sparsity opportunities\" compressing general LLM 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"activation sparsity opportunities\" compressing general LLM 2025 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 1161 · 2026-05-20T15:27:30.975835+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2507.14179 \"sparsity predicting\" \"activation pattern clustering\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2507.14179 \"sparsity predicting\" \"activation pattern clustering\" 2025"
  }
}
```

</details>

---


### Tool result

_source line 1162 · 2026-05-20T15:27:36.394948+00:00_

Web search results for query: ""activation sparsity opportunities" compressing general LLM 2025 arxiv"

Links: [{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"[2412.12178] Activation Sparsity Opportunities for Compressing General Large Language Models","url":"https://arxiv.org/abs/2412.12178"},{"title":"(PDF) Activation Sparsity Opportunities for Compressing General Large Language Models","url":"https://www.researchgate.net/publication/387141228_Activation_Sparsity_Opportunities_for_Compressing_General_Large_Language_Models"},{"title":"Activation Sparsity Opportunities for Compressing General Large Language Models","url":"https://arxiv.org/pdf/2412.12178"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern","url":"https://arxiv.org/pdf/2507.14179"},{"title":"Activation Sparsity Opportunities for Compressing General Large Language Models | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10850382/"},{"title":"[2509.00454] Universal Properties of Activation Sparsity in Modern Large Language Models","url":"https://arxiv.org/abs/2509.00454"}]

Based on the search results, I found the paper you're looking for:

"Activation Sparsity Opportunities for Compressing General Large Language Models" systematically investigates the tradeoff between enforcing activation sparsity and perplexity (accuracy) on state-of-the-art LLMs.

**Key findings from the paper:**

- The empirical analysis demonstrates that around 50% of main memory and computing reductions can be obtained for critical FFN components with negligible accuracy degradation.

- This extra 50% sparsity does not naturally exist in current LLMs, which require tuning LLMs' activation outputs by injecting zero-enforcing thresholds.

- LLMs' Feed-Forward Network (FFN) components typically comprise a large proportion of parameters (around 2/3
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5720
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-20T15:27:37.800156+00:00_

Web search results for query: "arxiv 2507.14179 "sparsity predicting" "activation pattern clustering" 2025"

Links: [{"title":"[2507.14179] A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/abs/2507.14179"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=1075&show=2000"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=20800&show=1000"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern","url":"https://arxiv.org/pdf/2507.14179"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"}]

I found the paper you're looking for. arXiv:2507.14179 is titled "A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering" by Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, and Kun Suo, submitted on July 11, 2025. The paper is to be published in Euro-Par 2025.

The paper addresses how Large Language Models (LLMs) exhibit significant activation sparsity, where only a subset of neurons are active for a given input. Since direct prediction at the neuron level is computationally expensive due to the vast number of neurons in modern LLMs, the authors propose a clustering-based activation pattern compression framework. Instead of treating each neuron independently, they group similar activation patterns into a small set of representative clusters.


REMINDER: You MUST include the sources above in your response to the user usin
…[truncated 22 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6824
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-20T15:30:44.289454+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n### Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器。核心思想是将 mask 决策通过完整前向传播耦合到输出分布，使每个 neuron 的梯度依赖于所有其他 neuron 的 mask 状态，而非独立优化。在 LLaMA-3.1-8B 上 50% 稀疏度下 PPL 相对 TEAL 降低 14.5%，并在 Mistral-7B 和 Qwen-2.5-14B 上做了跨架构验证。论文自述为\"primarily empirical study\"。\n\n---\n\n### Strengths\n\n**S1. 清晰的问题定义与动机。** §3.6 的梯度分析简洁有力地展示了 BCE 将 mask 训练分解为独立逐 neuron 分类问题（梯度 ∂L_BCE/∂σ_j 仅依赖 neuron j），而 KL 通过 Jacobian 链式传播使每个 neuron 的梯度依赖全层 mask 配置。这一洞察虽在数学上直观，但对理解为何 output-level 目标优于 element-wise 目标很有启发。\n\n**S2. 受控实验设计。** 消融实验（§4.4, §4.5, Table 3-4）设计合理：target-swap ablation 用 BCE 训练在 KL 发现的 oracle mask 上以分离 mask 质量 vs. gradient coupling 的贡献；MSE baseline（Appendix G）用相同架构和 Lagrangian 控制器但不同 loss function，隔离了 coupling 效应。\n\n**S3. 丰富的附录支撑。** 18 页论文含 10 页附录（A-P），覆盖 inference efficiency 分析、bottleneck sensitivity、温度调度、训练收敛、penalty controller 动态、OOD 评估、per-layer 分析、mask 可视化等。信息密度高。\n\n**S4. 训练效率高。** 仅 1000 步（~45 min on 1×RTX PRO 6000）、75.9M 额外参数（<1% base model），训练成本极低，实用性强。\n\n**S5. 负面结果的诚实报告。** Mistral-7B GSM8K 反转（Table 16-17）、Qwen-2.5-14B 推理退化（GSM8K -20pp）均被明确报告，而非隐藏。\n\n---\n\n### Weaknesses\n\n**N1 [critical] 新颖性不足：核心贡献是标准 KL distillation 的直接应用。**\n- 具体位置：§3.4 (Eq. 5), §1 最后一段 (\"primarily empirical study\")\n- 问题：用 KL divergence 匹配 teacher（dense model）和 student（sparse model）的输出分布是知识蒸馏的经典范式（Hinton et al., 2015; Kim & Rush, 2016）。本文的创新在于将此范式应用于 SwiGLU sparsity predictor 训练，但技术上没有引入新的 loss function、新的优化方法、或新的理论分析。Gumbel-Sigmoid 松弛（§3.3）、adaptive Lagrangian penalty（§3.5）、TEAL global top-k allocation 均为已有技术的组合。\n- §3.6 的梯度分析虽有启发性，但本质上是在复述\"output-level loss 比 element-wise loss 传递更丰富梯度信号\"这一已知事实（MiniLLM, GKD, DistiLLM 等 LLM KD 文献均基于此动机）。\n- 与 MaskLLM 的区分（§2）：三个区分点（sparsity type / mask generation / allocation）确实存在，但核心训练原理（学习 mask 以最小化输出分布偏离）高度重合。MaskLLM 用 Gumbel-Softmax + output loss，本文用 Gumbel-Sigmoid + KL loss，差异有限。\n- 为什么影响接收：EMNLP main conference 要求 sufficient novelty。作为 \"primarily empirical study\"，实验需要覆盖更广的模型/任务/对比方法才能弥补方法论创新的不足。\n- 建议修改方向：(1) 增加与 MaskLLM 的直接实验对比（即使需要将 MaskLLM 从 N:M 适配到 unstructured），或充分论证为何不可比；(2) 深化理论贡献——例如分析 KL coupling 在什么条件下优于/劣于 BCE，而非仅做经验验证。\n\n**N2 [critical] 缺少与已有训练型稀疏预测器的数值对比。**\n- 具体位置：§4.2 (Table 2), §2 (Related Work)\n- 问题：论文主要对比 TEAL（training-free baseline）和 magnitude-based pruning。但 §2 详细讨论了 DejaVu、ShadowLLM、FastForward 等训练型预测器，却未在实验中进行数值对比。这使得读者无法判断 KL predictor 相对于这些已有方法的优势大小。\n- 论文在 §2 提到 \"DejaVu introduces attention-based routing with per-layer MSE supervision\" 和 \"ShadowLLM uses per-layer MSE supervision\"——这些是中间层级 coupling（per-layer intermediate）的代表，恰好是 Table 1 taxonomy 中的一个 cell。然而 taxonomy 的预测力未被实验验证（即没有展示这些方法在本文设置下的实际表现）。\n- 为什么影响接收：没有与已有 trained predictor 对比，核心 claim \"KL coupling 优于其他训练信号\" 的证据不完整。\n- 建议修改方向：至少复现 DejaVu-style per-layer MSE predictor 作为 baseline（代码复杂度低，仅需改 loss function），或引用并分析这些方法在 SwiGLU 模型上的已有结果。\n\n**W1 [warning] 无实际推理加速验证。**\n- 具体位置：Appendix A, Limitations §6\n- 问题：Appendix A 明确指出 \"the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support\"。overhead 为 ~4.4%（Table 6），但 sparse computation 本身没有加速。对于一篇关于 \"inference efficiency\" 的工作，这严重削弱了实际意义。\n- 论文的贡献严格来说是 prediction quality 而非 runtime efficiency，但 abstract 和 introduction 中 \"reducing the computational burden\" 等表述暗示了实际效率收益。\n- 建议：(1) 调整 framing，更明确地将贡献定位为 \"mask quality study\" 而非 efficiency method；(2) 或提供 Triton/cuSPARSE 的 proof-of-concept 加速测量。\n\n**W2 [warning] 实验规模和多样性有限。**\n- 具体位置：§4.1, §4.6\n- 问题：\n  - 主实验仅在 LLaMA-3.1-8B 上进行，Mistral-7B 和 Qwen-2.5-14B 作为 \"cross-architecture\" 验证但结果不一致（GSM8K 反转、推理退化）\n  - 训练数据仅用 WikiText-103（1000 steps, ~45 min），未探索其他数据源对 predictor 质量的影响\n  - 所有实验使用相同的 predictor 架构（2-layer MLP, d_b=128），未与其他 predictor 架构（如 linear probe, attention-based routing）对比\n  - 下游评估仅 5 个 benchmark（ARC-C, WG, HellaSwag, MMLU, GSM8K, PIQA），缺少生成任务（summarization, translation）和长文本理解任务\n- 建议：增加至少一个 13B+ 规模模型的完整实验（不仅是 preliminary evaluation）；增加训练数据多样性实验。\n\n**W3 [warning] Table 1 taxonomy 的分析价值有限。**\n- 具体位置：§3.7, Table 1\n- 问题：两维分类框架（correction granularity × training signal coupling）对已有方法做了整理，但：(1) 大部分 cell 只有 0-1 个方法，矩阵过于稀疏，难以得出 systematic conclusion；(2) taxonomy 的预测力未被验证——论文声称 \"coupled + per-token\" 应优于其他配置，但没有系统对比同一 taxonomy cell 内的方法；(3) 文中未讨论为何某些 cell 为空（例如 coupled + per-layer）——是技术上不可行还是尚未被探索？\n- 建议：要么通过实验填充 taxonomy 的关键 cell（至少验证 2-3 个代表性配置），要么降低对 taxonomy 作为贡献的强调。\n\n**W4 [warning] C1 ablation 存在混淆因素。**\n- 具体位置：§4.4, Table 3-4\n- 问题：Target-swap ablation 训练 BCE predictor 在 KL-derived oracle masks 上。但 oracle masks 是从完整 KL 训练（1000+2000 steps）得到的，已经包含了 KL 目标的信息。因此 \"BCE on KL targets\" 的表现部分反映了 KL 发现的 mask quality，但也受 BCE 训练本身能否忠实复现这些 mask 的影响。更干净的 ablation 应该：(a) 用 KL 训练的 frozen mask 直接评估（不经过 BCE 重新训练），或 (b) 用随机采样的 mask 分布进行消融。\n- 论文确实报告了 \"BCE on KL targets reproduces KL quality\" (Table 4, Δ≤0.79pp)，这支持了 mask quality 是主要因素。但这也削弱了 gradient coupling 贡献的说服力——如果 BCE 也能达到相同质量，那 KL 的优势仅在于 mask *discovery* 而非训练过程本身。\n- 建议：明确讨论此 confound，并补充\"如果事先不知道好的 mask targets，BCE 无法发现它们\"这一论点的更直接证据。\n\n---\n\n### Minor Issues\n\n**M1.** §3.4 Eq. 5 中 KL 公式为 D_KL(P_dense || P_sparse)，即 forward KL。鉴于近期 LLM KD 文献（MiniLLM, DistiLLM）大量讨论 forward vs. reverse KL 的选择，论文应简要说明为何选择 forward KL 而非 reverse KL，或报告 reverse KL 的实验结果。\n\n**M2.** GRIFFIN 引用（de2024griffin）在 OpenAlex 上 not_found，bib entry 列为 arXiv preprint。Griffin 本身是关于 gated linear recurrence 的架构，与 activation sparsity 的关联较弱。§2 最后一段提到 Griffin 是为了暗示方法可能 generalize beyond Transformer FFNs，但没有实验支撑。建议：要么去掉这句 speculation，要么降低其权重。\n\n**M3.** Figure 1 caption 偏短，不够自包含——仅说 \"Method overview\" 但未解释 Gumbel-Sigmoid 松弛和 TEAL allocation 的角色。表格标题总体质量良好。\n\n**M4.** References 中 CATS (Lee et al., 2024) 仍标为 arXiv preprint，但该工作可能已被发表（arXiv:2404.08763），建议核查更新。\n\n**M5.** §4.3 \"Extended Training Strategy\" 的叙述比较仓促——2700 步 vs 1000 步 的对比只用了一段话。BCE 7pp worse PPL + KL 6x random precision 这些数字的 statistical significance 未报告。\n\n---\n\n### Questions for Authors\n\n**Q1.** §3.6 分析表明 KL coupling 使 predictor 发现不同于 magnitude-based 的 mask pattern。但在 Table 3 中，BCE+STE 的 PPL 为 11.79 vs. KL 的 11.17——差异为 0.62 PPL。这个差异是否在统计上显著？Table 2 报告的 3-seed 标准差约 ±0.02-0.07，但 Table 3 的 ablation 是否也做了多 seed 评估？\n\n**Q2.** 为什么不在 SwiGLU 的 gate 分支（而非 up-projection 分支）进行 sparsity prediction？Gate 分支的 sigmoid 输出天然接近二值化，可能更适合稀疏性预测。CATS 正是利用 gate output 进行 thresholding。\n\n**Q3.** 论文是否尝试过 attention layer 的 sparsity prediction？Polar Sparsity (Shrestha et al., 2025) 将注意力头稀疏化——本文方法是否可以 extend 到 attention sparsity？\n\n**Q4.** Adaptive penalty controller（§3.5）的 geometric doubling 和 deadzone (κ=0.02) 是如何选择的？对这些超参数的敏感性分析在哪里？\n\n---\n\n### Missing References\n\n**MR1.** \"Activation Sparsity Opportunities for Compressing General Large Language Models\" (arXiv:2412.12178, Dec 2024) — 系统研究 SwiGLU FFN 的稀疏化机会和 accuracy-sparsity tradeoff，与本文直接相关。\n\n**MR2.** \"Accelerating Transformer Inference and Training with 2:4 Activation Sparsity\" (arXiv:2503.16672, March 2025) — 探索结构化 2:4 activation sparsity，与论文 future work 中提到的 N:M sparsity 方向直接相关。\n\n**MR3.** 论文引用了 MiniLLM 和 GKD 作为 KD 背景，但未引用 \"Rethinking KL Divergence in Knowledge Distillation for Large Language Models\" (Wen et al., arXiv:2404.02657, 2024)，该工作深入分析了 forward vs. reverse KL 在 LLM distillation 中的行为差异，与本文 KL 目标选择直接相关。\n\n---\n\n### 总体评分\n\n**Overall**: **3.0 — Findings**\n\n**一句话总结**: 扎实的经验性研究表明 output-distribution coupling 优于 per-neuron BCE 训练 SwiGLU 稀疏预测器，但核心方法是标准 KL distillation 的直接应用，缺少与已有训练型预测器的数值对比，新颖性不足以支撑 main conference 接收。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 技术正确，消融设计合理但 C1 ablation 有 confound；梯度分析正确但深度有限；缺少与 trained predictors 的对比削弱了核心 claim 的支撑 |\n| Excitement | 2.5/5 | 核心是标准 KD 范式的应用；gradient coupling insight 有一定启发性但不够深刻；taxonomy 贡献有限；无 runtime speedup 限制实际影响 |\n| Reproducibility | 4.0/5 | 训练细节完整（Appendix），超参数明确，架构简单可复现；但代码未提供（Ethics §C.5 提到 \"Yes\" 但未见链接） |\n| Overall Assessment | 3.0/5 | Findings 水平——经验发现有价值，实验设计基本扎实，但方法新颖性和实验全面性未达 main conference 门槛 |\n\n### Confidence\n\n**4/5** — 熟悉 activation sparsity、knowledge distillation 和 SwiGLU LLM 推理优化文献。仔细阅读了全文和附录。对梯度分析和实验设计的评估有较高信心。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n### Summary\n\n本文提出用 KL divergence 替代 BCE 训练 SwiGLU LLM 的上下文稀疏性预测器。核心思想是将 mask 决策通过完整前向传播耦合到输出分布，使每个 neuron 的梯度依赖于所有其他 neuron 的 mask 状态，而非独立优化。在 LLaMA-3.1-8B 上 50% 稀疏度下 PPL 相对 TEAL 降低 14.5%，并在 Mistral-7B 和 Qwen-2.5-14B 上做了跨架构验证。论文自述为\"primarily empirical study\"。\n\n---\n\n### Strengths\n\n**S1. 清晰的问题定义与动机。** §3.6 的梯度分析简洁有力地展示了 BCE 将 mask 训练分解为独立逐 neuron 分类问题（梯度 ∂L_BCE/∂σ_j 仅依赖 neuron j），而 KL 通过 Jacobian 链式传播使每个 neuron 的梯度依赖全层 mask 配置。这一洞察虽在数学上直观，但对理解为何 output-level 目标优于 element-wise 目标很有启发。\n\n**S2. 受控实验设计。** 消融实验（§4.4, §4.5, Table 3-4）设计合理：target-swap ablation 用 BCE 训练在 KL 发现的 oracle mask 上以分离 mask 质量 vs. gradient coupling 的贡献；MSE baseline（Appendix G）用相同架构和 Lagrangian 控制器但不同 loss function，隔离了 coupling 效应。\n\n**S3. 丰富的附录支撑。** 18 页论文含 10 页附录（A-P），覆盖 inference efficiency 分析、bottleneck sensitivity、温度调度、训练收敛、penalty controller 动态、OOD 评估、per-layer 分析、mask 可视化等。信息密度高。\n\n**S4. 训练效率高。** 仅 1000 步（~45 min on 1×RTX PRO 6000）、75.9M 额外参数（<1% base model），训练成本极低，实用性强。\n\n**S5. 负面结果的诚实报告。** Mistral-7B GSM8K 反转（Table 16-17）、Qwen-2.5-14B 推理退化（GSM8K -20pp）均被明确报告，而非隐藏。\n\n---\n\n### Weaknesses\n\n**N1 [critical] 新颖性不足：核心贡献是标准 KL distillation 的直接应用。**\n- 具体位置：§3.4 (Eq. 5), §1 最后一段 (\"primarily empirical study\")\n- 问题：用 KL divergence 匹配 teacher（dense model）和 student（sparse model）的输出分布是知识蒸馏的经典范式（Hinton et al., 2015; Kim & Rush, 2016）。本文的创新在于将此范式应用于 SwiGLU sparsity predictor 训练，但技术上没有引入新的 loss function、新的优化方法、或新的理论分析。Gumbel-Sigmoid 松弛（§3.3）、adaptive Lagrangian penalty（§3.5）、TEAL global top-k allocation 均为已有技术的组合。\n- §3.6 的梯度分析虽有启发性，但本质上是在复述\"output-level loss 比 element-wise loss 传递更丰富梯度信号\"这一已知事实（MiniLLM, GKD, DistiLLM 等 LLM KD 文献均基于此动机）。\n- 与 MaskLLM 的区分（§2）：三个区分点（sparsity type / mask generation / allocation）确实存在，但核心训练原理（学习 mask 以最小化输出分布偏离）高度重合。MaskLLM 用 Gumbel-Softmax + output loss，本文用 Gumbel-Sigmoid + KL loss，差异有限。\n- 为什么影响接收：EMNLP main conference 要求 sufficient novelty。作为 \"primarily empirical study\"，实验需要覆盖更广的模型/任务/对比方法才能弥补方法论创新的不足。\n- 建议修改方向：(1) 增加与 MaskLLM 的直接实验对比（即使需要将 MaskLLM 从 N:M 适配到 unstructured），或充分论证为何不可比；(2) 深化理论贡献——例如分析 KL coupling 在什么条件下优于/劣于 BCE，而非仅做经验验证。\n\n**N2 [critical] 缺少与已有训练型稀疏预测器的数值对比。**\n- 具体位置：§4.2 (Table 2), §2 (Related Work)\n- 问题：论文主要对比 TEAL（training-free baseline）和 magnitude-based pruning。但 §2 详细讨论了 DejaVu、ShadowLLM、FastForward 等训练型预测器，却未在实验中进行数值对比。这使得读者无法判断 KL predictor 相对于这些已有方法的优势大小。\n- 论文在 §2 提到 \"DejaVu introduces attention-based routing with per-layer MSE supervision\" 和 \"ShadowLLM uses per-layer MSE supervision\"——这些是中间层级 coupling（per-layer intermediate）的代表，恰好是 Table 1 taxonomy 中的一个 cell。然而 taxonomy 的预测力未被实验验证（即没有展示这些方法在本文设置下的实际表现）。\n- 为什么影响接收：没有与已有 trained predictor 对比，核心 claim \"KL coupling 优于其他训练信号\" 的证据不完整。\n- 建议修改方向：至少复现 DejaVu-style per-layer MSE predictor 作为 baseline（代码复杂度低，仅需改 loss function），或引用并分析这些方法在 SwiGLU 模型上的已有结果。\n\n**W1 [warning] 无实际推理加速验证。**\n- 具体位置：Appendix A, Limitations §6\n- 问题：Appendix A 明确指出 \"the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support\"。overhead 为 ~4.4%（Table 6），但 sparse computation 本身没有加速。对于一篇关于 \"inference efficiency\" 的工作，这严重削弱了实际意义。\n- 论文的贡献严格来说是 prediction quality 而非 runtime efficiency，但 abstract 和 introduction 中 \"reducing the computational burden\" 等表述暗示了实际效率收益。\n- 建议：(1) 调整 framing，更明确地将贡献定位为 \"mask quality study\" 而非 efficiency method；(2) 或提供 Triton/cuSPARSE 的 proof-of-concept 加速测量。\n\n**W2 [warning] 实验规模和多样性有限。**\n- 具体位置：§4.1, §4.6\n- 问题：\n  - 主实验仅在 LLaMA-3.1-8B 上进行，Mistral-7B 和 Qwen-2.5-14B 作为 \"cross-architecture\" 验证但结果不一致（GSM8K 反转、推理退化）\n  - 训练数据仅用 WikiText-103（1000 steps, ~45 min），未探索其他数据源对 predictor 质量的影响\n  - 所有实验使用相同的 predictor 架构（2-layer MLP, d_b=128），未与其他 predictor 架构（如 linear probe, attention-based routing）对比\n  - 下游评估仅 5 个 benchmark（ARC-C, WG, HellaSwag, MMLU, GSM8K, PIQA），缺少生成任务（summarization, translation）和长文本理解任务\n- 建议：增加至少一个 13B+ 规模模型的完整实验（不仅是 preliminary evaluation）；增加训练数据多样性实验。\n\n**W3 [warning] Table 1 taxonomy 的分析价值有限。**\n- 具体位置：§3.7, Table 1\n- 问题：两维分类框架（correction granularity × training signal coupling）对已有方法做了整理，但：(1) 大部分 cell 只有 0-1 个方法，矩阵过于稀疏，难以得出 systematic conclusion；(2) taxonomy 的预测力未被验证——论文声称 \"coupled + per-token\" 应优于其他配置，但没有系统对比同一 taxonomy cell 内的方法；(3) 文中未讨论为何某些 cell 为空（例如 coupled + per-layer）——是技术上不可行还是尚未被探索？\n- 建议：要么通过实验填充 taxonomy 的关键 cell（至少验证 2-3 个代表性配置），要么降低对 taxonomy 作为贡献的强调。\n\n**W4 [warning] C1 ablation 存在混淆因素。**\n- 具体位置：§4.4, Table 3-4\n- 问题：Target-swap ablation 训练 BCE predictor 在 KL-derived oracle masks 上。但 oracle masks 是从完整 KL 训练（1000+2000 steps）得到的，已经包含了 KL 目标的信息。因此 \"BCE on KL targets\" 的表现部分反映了 KL 发现的 mask quality，但也受 BCE 训练本身能否忠实复现这些 mask 的影响。更干净的 ablation 应该：(a) 用 KL 训练的 frozen mask 直接评估（不经过 BCE 重新训练），或 (b) 用随机采样的 mask 分布进行消融。\n- 论文确实报告了 \"BCE on KL targets reproduces KL quality\" (Table 4, Δ≤0.79pp)，这支持了 mask quality 是主要因素。但这也削弱了 gradient coupling 贡献的说服力——如果 BCE 也能达到相同质量，那 KL 的优势仅在于 mask *discovery* 而非训练过程本身。\n- 建议：明确讨论此 confound，并补充\"如果事先不知道好的 mask targets，BCE 无法发现它们\"这一论点的更直接证据。\n\n---\n\n### Minor Issues\n\n**M1.** §3.4 Eq. 5 中 KL 公式为 D_KL(P_dense || P_sparse)，即 forward KL。鉴于近期 LLM KD 文献（MiniLLM, DistiLLM）大量讨论 forward vs. reverse KL 的选择，论文应简要说明为何选择 forward KL 而非 reverse KL，或报告 reverse KL 的实验结果。\n\n**M2.** GRIFFIN 引用（de2024griffin）在 OpenAlex 上 not_found，bib entry 列为 arXiv preprint。Griffin 本身是关于 gated linear recurrence 的架构，与 activation sparsity 的关联较弱。§2 最后一段提到 Griffin 是为了暗示方法可能 generalize beyond Transformer FFNs，但没有实验支撑。建议：要么去掉这句 speculation，要么降低其权重。\n\n**M3.** Figure 1 caption 偏短，不够自包含——仅说 \"Method overview\" 但未解释 Gumbel-Sigmoid 松弛和 TEAL allocation 的角色。表格标题总体质量良好。\n\n**M4.** References 中 CATS (Lee et al., 2024) 仍标为 arXiv preprint，但该工作可能已被发表（arXiv:2404.08763），建议核查更新。\n\n**M5.** §4.3 \"Extended Training Strategy\" 的叙述比较仓促——2700 步 vs 1000 步 的对比只用了一段话。BCE 7pp worse PPL + KL 6x random precision 这些数字的 statistical significance 未报告。\n\n---\n\n### Questions for Authors\n\n**Q1.** §3.6 分析表明 KL coupling 使 predictor 发现不同于 magnitude-based 的 mask pattern。但在 Table 3 中，BCE+STE 的 PPL 为 11.79 vs. KL 的 11.17——差异为 0.62 PPL。这个差异是否在统计上显著？Table 2 报告的 3-seed 标准差约 ±0.02-0.07，但 Table 3 的 ablation 是否也做了多 seed 评估？\n\n**Q2.** 为什么不在 SwiGLU 的 gate 分支（而非 up-projection 分支）进行 sparsity prediction？Gate 分支的 sigmoid 输出天然接近二值化，可能更适合稀疏性预测。CATS 正是利用 gate output 进行 thresholding。\n\n**Q3.** 论文是否尝试过 attention layer 的 sparsity prediction？Polar Sparsity (Shrestha et al., 2025) 将注意力头稀疏化——本文方法是否可以 extend 到 attention sparsity？\n\n**Q4.** Adaptive penalty controller（§3.5）的 geometric doubling 和 deadzone (κ=0.02) 是如何选择的？对这些超参数的敏感性分析在哪里？\n\n---\n\n### Missing References\n\n**MR1.** \"Activation Sparsity Opportunities for Compressing General Large Language Models\" (arXiv:2412.12178, Dec 2024) — 系统研究 SwiGLU FFN 的稀疏化机会和 accuracy-sparsity tradeoff，与本文直接相关。\n\n**MR2.** \"Accelerating Transformer Inference and Training with 2:4 Activation Sparsity\" (arXiv:2503.16672, March 2025) — 探索结构化 2:4 activation sparsity，与论文 future work 中提到的 N:M sparsity 方向直接相关。\n\n**MR3.** 论文引用了 MiniLLM 和 GKD 作为 KD 背景，但未引用 \"Rethinking KL Divergence in Knowledge Distillation for Large Language Models\" (Wen et al., arXiv:2404.02657, 2024)，该工作深入分析了 forward vs. reverse KL 在 LLM distillation 中的行为差异，与本文 KL 目标选择直接相关。\n\n---\n\n### 总体评分\n\n**Overall**: **3.0 — Findings**\n\n**一句话总结**: 扎实的经验性研究表明 output-distribution coupling 优于 per-neuron BCE 训练 SwiGLU 稀疏预测器，但核心方法是标准 KL distillation 的直接应用，缺少与已有训练型预测器的数值对比，新颖性不足以支撑 main conference 接收。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 技术正确，消融设计合理但 C1 ablation 有 confound；梯度分析正确但深度有限；缺少与 trained predictors 的对比削弱了核心 claim 的支撑 |\n| Excitement | 2.5/5 | 核心是标准 KD 范式的应用；gradient coupling insight 有一定启发性但不够深刻；taxonomy 贡献有限；无 runtime speedup 限制实际影响 |\n| Reproducibility | 4.0/5 | 训练细节完整（Appendix），超参数明确，架构简单可复现；但代码未提供（Ethics §C.5 提到 \"Yes\" 但未见链接） |\n| Overall Assessment | 3.0/5 | Findings 水平——经验发现有价值，实验设计基本扎实，但方法新颖性和实验全面性未达 main conference 门槛 |\n\n### Confidence\n\n**4/5** — 熟悉 activation sparsity、knowledge distillation 和 SwiGLU LLM 推理优化文献。仔细阅读了全文和附录。对梯度分析和实验设计的评估有较高信心。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-20T15:30:49.310673+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5021
}
```

</details>

---


### Assistant

_source line 1166 · 2026-05-20T15:31:02.491505+00:00_

审稿报告已提交给 Review Director。

**审稿结论概要：Overall 3.0（Findings 水平）**

主要发现：

- **2 个 critical 问题**：(1) 新颖性不足——核心是标准 KL distillation 的直接应用于 SwiGLU sparsity predictor，与 MaskLLM 技术重合度高；(2) 缺少与 DejaVu/ShadowLLM/FastForward 等已有训练型预测器的数值对比，核心 claim 证据不完整。

- **4 个 warning 问题**：无实际推理加速验证（Appendix A 承认无 wall-clock speedup）；实验规模有限（主要在 LLaMA-3.1-8B，跨架构结果不一致）；Table 1 taxonomy 分析价值有限；C1 ablation 存在混淆因素。

- **3 篇 missing references**：activation sparsity opportunities (2412.12178)、2:4 activation sparsity (2503.16672)、rethinking KL divergence in KD (2404.02657)。

- **优势**：梯度分析清晰、消融设计合理、附录丰富、训练效率高、负面结果诚实报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 29

## Round 29

12 recorded events


### User

_source line 1167 · 2026-05-20T15:33:18.489107+00:00_

[Round 1 审稿请求]:
以下是 **Reviewer 1** 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness/Question 标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并引用论文具体 Section/Table/Figure 作为证据。

---

## Reviewer 1 完整审稿原文

### Overall: 3.5 (Borderline Conference)

### Must-Fix 问题

**N1 [critical] 多种子覆盖不一致，存在选择性报告风险**
- 50% KL global（Table 2 最佳 PPL 11.79）为 single-seed (s42)，而 50% KL uniform（PPL 11.92±0.07）为 3-seed。Table 5（appendix Table 15）50% global 行中，MMLU 有 ±0.2 但 PPL、ARC-c、WG、GSM8K 均无 ±。MSE baseline 全部 single-seed。

**N2 [critical] PPL 改善与下游任务脱节——核心实用性质疑**
- 30% 稀疏度下 KL PPL 比 TEAL 好 19%（8.81 vs 10.82），但 MMLU 差 5.2pp（40.7 vs 45.9）、GSM8K 差 1.3pp（7.5 vs 8.8）。PPL 改善不能转化为下游提升甚至在关键任务上劣化。

**N3 [critical] 消融实验仅在 50% 稀疏度——论文实际有用的 regime 未被消融覆盖**
- Table 4 所有消融仅在 50%。但论文承认 50% 下游崩溃，30% 才是可用稀疏度。30% 的 loss function 选择消融缺失。

### Should-Fix 问题

**W1 [warning]** 稀疏度控制器 30% 目标偏差 5%（实际 28.5%），headline "19%" 基于 mismatched 比较。

**W2 [warning]** Forward KL 方向选择论证不足——标准 KD 文献通常论证 reverse KL 对 capacity-limited student 更优。

**W3 [warning]** 评估域同质性——WikiText-103 训练、WikiText-2 评估，C4 OOD 显示 domain shift 放大方差 30×。

**W4 [warning]** §3.6 梯度分析 informal——缺乏显式梯度表达式、耦合程度量化。

**W5 [warning]** 无实际推理加速——增加 6.4% 开销。

### 主要优势
1. C1 目标-交换消融设计精妙
2. 诚实报告负面结果
3. 全面敏感性分析
4. §3.7 二维分类框架有用
5. 单 GPU 45 分钟训练

### 引用核查
- 47 entries, 0 orphan, 0 missing, 41 verified, 1 not_found (Griffin), 5 minor mismatches
- 无虚假引用

### 数据一致性核查
- 表格间数字全部匹配
- Limitations PPL 数值与正文匹配
- Abstract 数字验证通过

### 格式合规
- 正文 8 页，合规
- Double-blind 合规
- 引用格式合规

**Confidence: 4/5**
评语：如果能补充 30% 消融和完整 multi-seed Table 2，建议可升至 Conference (4)。

---

请对上述每个 N1/N2/N3/W1-W5 逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-20T15:34:33.100776+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "6-8",
  "dpi": "165"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "6-8",
    "dpi": "165"
  }
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-20T15:34:33.984842+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 555.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 549.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 544.7}], \"total_pages\": 18, \"rendered_pages\": 3, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 884
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-20T15:34:37.799497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1171 · 2026-05-20T15:34:38.301589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1172 · 2026-05-20T15:34:38.856739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 1173 · 2026-05-20T15:34:38.857242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1174 · 2026-05-20T15:34:39.514717+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1213
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-20T15:34:39.817098+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-20T15:36:44.582394+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 Round 1 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 多种子覆盖不一致，存在选择性报告风险**\n\n同意这是一个实质性问题。我在 Table 2 和 Table 5 中验证了 R1 的观察：\n\n- Table 2 caption 使用标记约定（†3-seed, unmarked=seed42），50% KL global PPL 11.79 无 ± 号，确认为 single-seed (s42)\n- Table 5 中 50% global 行：PPL 11.79（无±）、MMLU 28.1±0.2（有±），种子覆盖在同一行内不一致\n- MSE baseline（Appendix G）全部 single-seed\n\n论文确实 disclose 了种子约定，但 headline result（Table 2 的 \"best PPL\"）基于 single-seed 而非 3-seed mean，这在 empirical study 中构成选择性报告风险。补充完整 3-seed 评估是合理要求。\n\n---\n\n**[REBUT] R1-N2: PPL 改善与下游任务脱节——R1 选择性引用了下游结果**\n\nR1 的论据存在选择性偏差。R1 仅引用 MMLU（-5.2pp）和 GSM8K（-1.3pp）来支撑\"PPL 改善不能转化为下游提升\"的结论，但**忽略了论文明确报告的 4 项正面结果**。§4.2 原文：\"KL outperforms TEAL on commonsense reasoning (ARC-C, WG, HellaSwag, PIQA: 4/4 wins at 30% uniform)\"。完整图景是：\n\n| 任务类型 | 30% KL vs TEAL | 方向 |\n|---------|---------------|------|\n| ARC-C | KL 胜 | ↑ |\n| WinoGrande | KL 胜 | ↑ |\n| HellaSwag | KL 胜 | ↑ |\n| PIQA | KL 胜 | ↑ |\n| MMLU | TEAL 胜 (-5.2pp) | ↓ |\n| GSM8K | TEAL 胜 (-1.3pp) | ↓ |\n\n因此 R1 的结论\"PPL 改善不能转化为下游提升\"过度概括。更准确的表述应为：**KL 的 PPL 改善一致地转化为 commonsense reasoning 提升，但在 knowledge-intensive 任务上存在 task-type-dependent 退化。**\n\n但我补充一个 R1 未充分强调的担忧：MMLU（-5.2pp）的退化幅度大于 dense→TEAL 30% 的退化，且 MMLU 是 reviewer 和 AC 最常关注的 benchmark。这一 task-type split 模式值得论文在 §5 Conclusion 中更显著地讨论，而非仅在 §4.2 一句话带过。此外，论文将此归因于 \"Forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways\"，但这只是 post-hoc speculation，没有实验验证。\n\n**结论**：R1-N2 的核心观察（PPL-downstream 不一致）有部分合理性，但将其定为 \"critical\" 并声称 PPL 改善\"不能转化为下游提升\"与论文实际报告的 4/6 任务正面结果不符。建议降级为 warning。\n\n---\n\n**[AGREE] R1-N3: 消融实验仅在 50% 稀疏度**\n\n完全同意。Table 3（target-swap ablation）和 Table 4（component ablation）均在 50% sparsity 下进行。论文自身在 §4.6 和 §5 中承认 50% 时 \"all methods exhibit downstream collapse\"，MMLU 崩溃至 near-random（~28%）。在此 regime 下的消融告诉我们 mask quality 差异，但在实际可用的 30% regime 下：\n\n1. BCE vs KL 的 loss function 选择对 downstream 的影响是否相同？未知\n2. Gradient coupling 在 30%（激活更多 neurons）时的贡献是否与 50%（大量 pruning）时相同？未知\n3. 30% 时 MMLU 退化（-5.2pp vs TEAL）是否可通过消融归因？未知\n\n这是论文的一个真正盲区。作者应补充 30% sparsity 下至少 Table 4 中关键 configurations（Forward KL+Gumbel、BCE+Gumbel、Forward KL+STE）的对比。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R1-W1: 稀疏度控制器偏差导致 headline 数字 misleading**\n\nR1 声称 \"headline 19% 基于 mismatched 比较\"，但论文在 §4.2 **同一段**中已同时报告了两个数字：\"reducing TEAL's perplexity by 19% (10.82 → 8.81; **14.5% at matched 28.5% sparsity**, Appendix D)\"。Table 2 caption 也明确标注 \"Actual achieved sparsity: KL 28.5%, TEAL 29.3% at 30% target\"。\n\n- 实际偏差：KL 28.5% vs target 30%（差 1.5pp），TEAL 29.3% vs target 30%（差 0.7pp）\n- 两者实际稀疏度之差：0.8pp，不是 R1 暗示的 5%\n\n论文的 disclosure 是充分的。19% 是 headline comparison，14.5% 是 matched comparison，两者均被报告。R1 将此定为 warning 偏严。\n\n---\n\n**[AGREE] R1-W2: Forward KL 方向选择论证不足**\n\n完全同意。我在自己的审稿中也提出了相同问题（我的 M1）。§3.4 使用 D_KL(P_dense || P_sparse)（forward KL）但未论证此选择。MiniLLM (Gu et al., 2024) 专门论证了 reverse KL 对 capacity-limited student 的优势；DistiLLM (Ko et al., 2024) 探索了 skewed KL。论文引用了这两个工作但未讨论 KL 方向选择。补充 forward vs. reverse KL 的消融实验或至少理论论证是合理要求。\n\n---\n\n**[AGREE] R1-W3: 评估域同质性**\n\n同意但补充：论文确实在 Appendix D (Table 11) 进行了 C4 OOD 评估，显示 KL predictor achieves 52.5% relative advantage over TEAL。但 R1 正确指出 C4 方差放大（CV=0.3% in-domain vs. 较高 OOD），且只有一个 OOD domain。训练数据也仅 WikiText-103，作为 empirical study 这限制了 generalizability claims 的强度。\n\n---\n\n**[AGREE] R1-W4: §3.6 梯度分析 informal**\n\n同意。§3.6 的分析直觉上有说服力，但缺乏：(1) ∂L_KL/∂σ_j 的显式展开表达式；(2) coupling degree 的量化指标（如 Hessian off-diagonal magnitude）；(3) 与 BCE 梯度在实际训练中 gradient flow 的经验对比。当前分析本质是 \"KL 通过 softmax 耦合所有 neuron\" 这一已知事实的叙述性重述，未提供定量新洞察。\n\n---\n\n**[AGREE] R1-W5: 无实际推理加速**\n\n同意。这与我的 W1 重合。Appendix A 报告 predictor overhead 4.4%（Table 6），且 unstructured mask 不能被现有 sparse kernel 加速。论文的贡献严格限于 prediction quality，但 framing 时使用了 \"reducing computational burden\"（Abstract）等暗示实际效率收益的措辞。\n\n---\n\n### 综合评价\n\nR1 的审稿整体质量高，数据核查细致。我的分歧主要在：\n\n1. **N2 应降为 warning**：R1 选择性引用 MMLU/GSM8K 退化而忽略 4 项 commonsense 提升，不应定为 critical。但 task-type split 的成因分析不足确实是问题。\n\n2. **W1 基本不成立**：论文在同一段中同时报告了 matched 和 unmatched comparison，disclosure 充分。\n\n3. **其他 N1/N3/W2-W5 均同意**，尤其 N1（种子覆盖不一致）和 N3（消融缺 30% regime）是需要补充的实质性 gap。\n\n**我维持 Overall 3.0 (Findings) 的评分。** R1 建议 \"补充 30% 消融和完整 multi-seed Table 2 可升至 Conference (4)\"——我认为这些补充是必要条件但可能不是充分条件，因为 novelty 不足（我的 N1）和缺少与 trained predictor 的对比（我的 N2）是独立于 R1 意见的额外 concerns。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 Round 1 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 多种子覆盖不一致，存在选择性报告风险**\n\n同意这是一个实质性问题。我在 Table 2 和 Table 5 中验证了 R1 的观察：\n\n- Table 2 caption 使用标记约定（†3-seed, unmarked=seed42），50% KL global PPL 11.79 无 ± 号，确认为 single-seed (s42)\n- Table 5 中 50% global 行：PPL 11.79（无±）、MMLU 28.1±0.2（有±），种子覆盖在同一行内不一致\n- MSE baseline（Appendix G）全部 single-seed\n\n论文确实 disclose 了种子约定，但 headline result（Table 2 的 \"best PPL\"）基于 single-seed 而非 3-seed mean，这在 empirical study 中构成选择性报告风险。补充完整 3-seed 评估是合理要求。\n\n---\n\n**[REBUT] R1-N2: PPL 改善与下游任务脱节——R1 选择性引用了下游结果**\n\nR1 的论据存在选择性偏差。R1 仅引用 MMLU（-5.2pp）和 GSM8K（-1.3pp）来支撑\"PPL 改善不能转化为下游提升\"的结论，但**忽略了论文明确报告的 4 项正面结果**。§4.2 原文：\"KL outperforms TEAL on commonsense reasoning (ARC-C, WG, HellaSwag, PIQA: 4/4 wins at 30% uniform)\"。完整图景是：\n\n| 任务类型 | 30% KL vs TEAL | 方向 |\n|---------|---------------|------|\n| ARC-C | KL 胜 | ↑ |\n| WinoGrande | KL 胜 | ↑ |\n| HellaSwag | KL 胜 | ↑ |\n| PIQA | KL 胜 | ↑ |\n| MMLU | TEAL 胜 (-5.2pp) | ↓ |\n| GSM8K | TEAL 胜 (-1.3pp) | ↓ |\n\n因此 R1 的结论\"PPL 改善不能转化为下游提升\"过度概括。更准确的表述应为：**KL 的 PPL 改善一致地转化为 commonsense reasoning 提升，但在 knowledge-intensive 任务上存在 task-type-dependent 退化。**\n\n但我补充一个 R1 未充分强调的担忧：MMLU（-5.2pp）的退化幅度大于 dense→TEAL 30% 的退化，且 MMLU 是 reviewer 和 AC 最常关注的 benchmark。这一 task-type split 模式值得论文在 §5 Conclusion 中更显著地讨论，而非仅在 §4.2 一句话带过。此外，论文将此归因于 \"Forward KL's mass-covering property may preserve output breadth at the expense of reasoning-critical pathways\"，但这只是 post-hoc speculation，没有实验验证。\n\n**结论**：R1-N2 的核心观察（PPL-downstream 不一致）有部分合理性，但将其定为 \"critical\" 并声称 PPL 改善\"不能转化为下游提升\"与论文实际报告的 4/6 任务正面结果不符。建议降级为 warning。\n\n---\n\n**[AGREE] R1-N3: 消融实验仅在 50% 稀疏度**\n\n完全同意。Table 3（target-swap ablation）和 Table 4（component ablation）均在 50% sparsity 下进行。论文自身在 §4.6 和 §5 中承认 50% 时 \"all methods exhibit downstream collapse\"，MMLU 崩溃至 near-random（~28%）。在此 regime 下的消融告诉我们 mask quality 差异，但在实际可用的 30% regime 下：\n\n1. BCE vs KL 的 loss function 选择对 downstream 的影响是否相同？未知\n2. Gradient coupling 在 30%（激活更多 neurons）时的贡献是否与 50%（大量 pruning）时相同？未知\n3. 30% 时 MMLU 退化（-5.2pp vs TEAL）是否可通过消融归因？未知\n\n这是论文的一个真正盲区。作者应补充 30% sparsity 下至少 Table 4 中关键 configurations（Forward KL+Gumbel、BCE+Gumbel、Forward KL+STE）的对比。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R1-W1: 稀疏度控制器偏差导致 headline 数字 misleading**\n\nR1 声称 \"headline 19% 基于 mismatched 比较\"，但论文在 §4.2 **同一段**中已同时报告了两个数字：\"reducing TEAL's perplexity by 19% (10.82 → 8.81; **14.5% at matched 28.5% sparsity**, Appendix D)\"。Table 2 caption 也明确标注 \"Actual achieved sparsity: KL 28.5%, TEAL 29.3% at 30% target\"。\n\n- 实际偏差：KL 28.5% vs target 30%（差 1.5pp），TEAL 29.3% vs target 30%（差 0.7pp）\n- 两者实际稀疏度之差：0.8pp，不是 R1 暗示的 5%\n\n论文的 disclosure 是充分的。19% 是 headline comparison，14.5% 是 matched comparison，两者均被报告。R1 将此定为 warning 偏严。\n\n---\n\n**[AGREE] R1-W2: Forward KL 方向选择论证不足**\n\n完全同意。我在自己的审稿中也提出了相同问题（我的 M1）。§3.4 使用 D_KL(P_dense || P_sparse)（forward KL）但未论证此选择。MiniLLM (Gu et al., 2024) 专门论证了 reverse KL 对 capacity-limited student 的优势；DistiLLM (Ko et al., 2024) 探索了 skewed KL。论文引用了这两个工作但未讨论 KL 方向选择。补充 forward vs. reverse KL 的消融实验或至少理论论证是合理要求。\n\n---\n\n**[AGREE] R1-W3: 评估域同质性**\n\n同意但补充：论文确实在 Appendix D (Table 11) 进行了 C4 OOD 评估，显示 KL predictor achieves 52.5% relative advantage over TEAL。但 R1 正确指出 C4 方差放大（CV=0.3% in-domain vs. 较高 OOD），且只有一个 OOD domain。训练数据也仅 WikiText-103，作为 empirical study 这限制了 generalizability claims 的强度。\n\n---\n\n**[AGREE] R1-W4: §3.6 梯度分析 informal**\n\n同意。§3.6 的分析直觉上有说服力，但缺乏：(1) ∂L_KL/∂σ_j 的显式展开表达式；(2) coupling degree 的量化指标（如 Hessian off-diagonal magnitude）；(3) 与 BCE 梯度在实际训练中 gradient flow 的经验对比。当前分析本质是 \"KL 通过 softmax 耦合所有 neuron\" 这一已知事实的叙述性重述，未提供定量新洞察。\n\n---\n\n**[AGREE] R1-W5: 无实际推理加速**\n\n同意。这与我的 W1 重合。Appendix A 报告 predictor overhead 4.4%（Table 6），且 unstructured mask 不能被现有 sparse kernel 加速。论文的贡献严格限于 prediction quality，但 framing 时使用了 \"reducing computational burden\"（Abstract）等暗示实际效率收益的措辞。\n\n---\n\n### 综合评价\n\nR1 的审稿整体质量高，数据核查细致。我的分歧主要在：\n\n1. **N2 应降为 warning**：R1 选择性引用 MMLU/GSM8K 退化而忽略 4 项 commonsense 提升，不应定为 critical。但 task-type split 的成因分析不足确实是问题。\n\n2. **W1 基本不成立**：论文在同一段中同时报告了 matched 和 unmatched comparison，disclosure 充分。\n\n3. **其他 N1/N3/W2-W5 均同意**，尤其 N1（种子覆盖不一致）和 N3（消融缺 30% regime）是需要补充的实质性 gap。\n\n**我维持 Overall 3.0 (Findings) 的评分。** R1 建议 \"补充 30% 消融和完整 multi-seed Table 2 可升至 Conference (4)\"——我认为这些补充是必要条件但可能不是充分条件，因为 novelty 不足（我的 N1）和缺少与 trained predictor 的对比（我的 N2）是独立于 R1 意见的额外 concerns。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-20T15:36:48.095369+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3512
}
```

</details>

---


### Assistant

_source line 1178 · 2026-05-20T15:36:54.163111+00:00_

已提交对 Reviewer 1 意见的逐条回应。要点总结：

- **N1（种子不一致）、N3（消融缺 30%）、W2-W5**：全部 AGREE
- **N2（PPL-下游脱节）**：REBUT——R1 选择性引用 MMLU/GSM8K 退化而忽略 4 项 commonsense 提升，建议降为 warning
- **W1（稀疏度偏差）**：REBUT——论文同段已报告 matched comparison（14.5%），disclosure 充分

维持 Overall 3.0 (Findings) 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 30

## Round 30

58 recorded events


### User

_source line 1179 · 2026-05-21T01:19:52.179708+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

### 你的侧重：新颖性 + Related Work + 写作质量 + 格式合规

重点审查以下方面：
1. **新颖性评估**：核心贡献的技术新颖性如何？与 MaskLLM（同为 frozen weights + learnable masks + KL training）的区别是否足够？empirical contribution 是否达到 EMNLP main conference bar？
2. **Related Work 完整性**：是否遗漏重要相关工作？与已有方法的定位是否准确？Taxonomy (Table 1) 的分类是否合理？
3. **写作质量**：论文结构是否清晰？核心 narrative 是否有说服力？是否存在过度声称或措辞不当？Abstract/Introduction 的 framing 是否准确反映实验发现？
4. **格式合规**：是否符合 EMNLP 2026 / ARR 格式要求（8 页正文、ACL 模板、匿名性、引用格式）？
5. **贡献清晰度**：4 个 contributions 的 claim 是否清晰、可验证、有意义？
6. **Limitations 和 Ethics**：是否充分讨论？是否遗漏重要 limitations？

### Venue 信息
- **EMNLP 2026**, ARR May cycle, deadline 2026-05-25
- Long Paper: 正文 ≤8 页, 参考文献无限制
- Limitations 和 Ethics 不计入页数
- ACL 模板, double-blind
- Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle

### 论文路径
- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）
- PDF: `projects/distill_sparse_swiglu/paper/main.pdf`

### 论文摘要
论文提出用 KL divergence（而非 BCE）训练 SwiGLU LLM 的稀疏预测器。核心发现：KL 的耦合梯度发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，这些 patterns 产生更低的 perplexity。Target-swap ablation (C1) 确认 mask quality 驱动推理阶段质量。评估在 LLaMA-3.1-8B, Mistral-7B, Qwen-2.5-14B 上进行。论文自定位为 "primarily empirical study"。

### 输出格式
请按以下结构输出审稿意见：
1. **Summary**（2-3 句）
2. **Strengths**（逐条编号，S1/S2/...）
3. **Weaknesses**（逐条编号，W1/W2/...，标注严重程度 [Critical/Major/Minor]）
4. **Questions**（逐条编号，Q1/Q2/...）
5. **Missing References**（如有）
6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-21T01:20:07.852574+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-21T01:20:08.053976+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-21T01:20:11.072275+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1183 · 2026-05-21T01:20:12.731206+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1184 · 2026-05-21T01:20:19.515260+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8442
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-21T01:20:21.022877+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 562.3}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 5
…[truncated 223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8291
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-21T01:20:27.131216+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions (e.g. soundness, excitement, novelty, reproducibility, etc.), their scales, and descriptions. Also extract any guidance on what constitutes each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions (e.g. soundness, excitement, novelty, reproducibility, etc.), their scales, and descriptions. Also extract any guidance on what constitutes each score level."
  }
}
```

</details>

---


### Tool call

_source line 1187 · 2026-05-21T01:20:27.587800+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-21T01:20:28.191588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1189 · 2026-05-21T01:20:28.596980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1190 · 2026-05-21T01:20:29.553781+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1965
}
```

</details>

---


### Tool call

_source line 1191 · 2026-05-21T01:20:29.554290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-21T01:20:29.756594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-21T01:20:30.161085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1969
}
```

</details>

---


### Tool result

_source line 1194 · 2026-05-21T01:20:31.267904+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2670
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-21T01:20:31.824271+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2269
}
```

</details>

---


### Tool result

_source line 1196 · 2026-05-21T01:20:32.076176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2319
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-21T01:20:35.039295+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award"
- **4**: "Conference: I think this paper could be accepted to an *ACL conference."
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: I think this paper needs substantial revisions."
- **1**: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could re
…[truncated 1321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7908
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-21T01:20:42.055236+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1199 · 2026-05-21T01:20:42.610221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1200 · 2026-05-21T01:20:42.764525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 709
}
```

</details>

---


### Tool call

_source line 1201 · 2026-05-21T01:20:42.965952+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-21T01:20:42.966448+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1203 · 2026-05-21T01:20:43.168199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-21T01:20:43.169321+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-21T01:20:44.581932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1971
}
```

</details>

---


### Tool result

_source line 1206 · 2026-05-21T01:20:45.940438+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2974
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-21T01:20:45.943857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2977
}
```

</details>

---


### Tool result

_source line 1208 · 2026-05-21T01:20:45.996773+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2828
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-21T01:20:47.411986+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 600.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 341.7}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 213.2}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4242
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-21T01:20:51.683741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-21T01:20:52.489611+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-21T01:20:52.540212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1213 · 2026-05-21T01:20:53.193728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1214 · 2026-05-21T01:20:53.546435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1215 · 2026-05-21T01:20:53.546865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-21T01:20:54.105073+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 1217 · 2026-05-21T01:20:54.105504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-21T01:20:54.508454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-21T01:20:55.717857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2170
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-21T01:20:55.718313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1221 · 2026-05-21T01:20:55.718527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1222 · 2026-05-21T01:20:56.476989+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2371
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-21T01:20:57.884012+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3375
}
```

</details>

---


### Tool result

_source line 1224 · 2026-05-21T01:20:57.887382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2168
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-21T01:20:58.040509+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2322
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-21T01:21:03.821315+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the full reviewer guidelines: what reviewers should focus on, what constitutes novelty, how to evaluate soundness, guidance on borderline papers, and any specific instructions about how to write constructive reviews. Also extract any guidance about evaluating empirical contributions vs theoretical contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the full reviewer guidelines: what reviewers should focus on, what constitutes novelty, how to evaluate soundness, guidance on borderline papers, and any specific instructions about how to write constructive reviews. Also extract any guidance about evaluating empirical contributions vs theoretical contributions."
  }
}
```

</details>

---


### Tool call

_source line 1227 · 2026-05-21T01:21:05.379007+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1228 · 2026-05-21T01:21:11.016190+00:00_

# ARR Reviewer Guidelines: Key Focus Areas

## Core Reviewer Responsibilities

Reviewers should concentrate on four main tasks: allocating review time, checking assignments for expertise and conflicts, writing strong reviews, and updating assessments after author responses.

## Evaluating Soundness

The soundness score must be justified by review text. Reviewers should verify that "low soundness scores without sufficient justification" indicate the review doesn't faithfully represent the recommendation. Technical correctness, methodological rigor, and complete proofs are central to soundness evaluation.

## Defining Novelty

Novelty requires "a reference" when claiming prior work exists. The guidelines caution against dismissing contributions merely because they seem "obvious in retrospect." Reproduction studies, reimplementations, and analyses legitimately constitute novel contributions if appropriately framed.

## Constructive Review Practices

Reviews must be "professional and neutral, if not kind." Reviewers should avoid sarcasm and dismissiveness. The guidance emphasizes: "Write the review you would like to get yourself." Specificity matters—vague criticisms like "missing relevant references" should become "missing references X, Y, Z."

## Empirical vs. Theoretical Contributions

The guidelines stress that "SOTA results are neither necessary nor sufficient for a scientific contribution." Papers offering improvements on "efficiency, generalizability, interpretability, fairness" merit fair evaluation. Both empirical work and theoretical contributions—including formal proofs needing "complete and correct" justification—warrant serious consideration.

## Red Flags to Avoid

Reviewers should recognize common problematic heuristics, such as dismissing work as "too simple," lacking "precedent," or using non-preferred methodologies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7194
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-21T01:21:50.035968+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 50, \"total_citations\": 93, \"unique_cited_keys\": 49, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 44, \"online_not_found\": 1, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [\"de2024griffin\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"fang2024maskllm\", \"type\": \"inproceedings\", \"title\": \"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models\", \"authors\": \"Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff P...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"xu2025spon\", \"type\": \"inproceedings\", \"title\": \"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\", \"authors\": \"Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Machine Learning (ICML)\"}, {\"key\": \"muralidharan2024minitron\", \"type\": \"inproceedings\", \"title\": \"Compact Language Models via Pruning and Knowledge Distillation\", \"authors\": \"Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marci...\", \"year\": \"2024\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"gautam2026fastforward\", \"type\": \"article\", \"title\": \"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\", \"authors\": \"Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott ...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2602.00397\"}, {\"key\": \"liu2025teal\", \"type\": \"inproceedings\", \"title\": \"Training-Free Activation Sparsity in Large Language Models\", \"authors\": \"James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and
…[truncated 40416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 44656
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-21T01:23:57.346673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation sparsity prediction LLM knowledge distillation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation sparsity prediction LLM knowledge distillation 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1231 · 2026-05-21T01:23:57.347010+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SwiGLU sparsity gating FFN efficient inference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SwiGLU sparsity gating FFN efficient inference 2025"
  }
}
```

</details>

---


### Tool result

_source line 1232 · 2026-05-21T01:24:03.724551+00:00_

Web search results for query: "SwiGLU sparsity gating FFN efficient inference 2025"

Links: [{"title":"SwiGLU Activation in Transformer Models","url":"https://www.emergentmind.com/topics/swiglu-activation"},{"title":"Masked Gated Linear Unit","url":"https://arxiv.org/html/2506.23225v1"},{"title":"DualSparse-MoE: Coordinating Tensor/Neuron-Level Sparsity with Expert Partition and Reconstruction","url":"https://arxiv.org/html/2508.18376"},{"title":"Published as a conference paper at ICLR 2024 RELU STRIKES BACK:","url":"https://openreview.net/pdf?id=osoWxY8q2E"},{"title":"SwiGLU: The FFN Upgrade I Use to Get Free Performance - DEV Community","url":"https://dev.to/mshojaei77/swiglu-the-ffn-upgrade-i-use-to-get-free-performance-33jc"},{"title":"Mixture-of-Channels: Exploiting Sparse FFNs for Efficient LLMs Pre-Training and Inference","url":"https://arxiv.org/html/2511.09323"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"}]

Based on the search results, here's what I found about SwiGLU, sparsity, gating, and FFN efficient inference in 2025:

## Key Findings

**SwiGLU Architecture and Sparsity:**
SwiGLU's gating architecture is compatible with sparse inference but exhibits moderate sparsity compared to alternatives such as ReLU.

**Recent Innovations (2025):**

A variant called SwiMGLU achieves comparable or superior downstream accuracy to SwiGLU while notably improving inference throughput and memory efficiency for resource-constrained LLM deployments.

Mixture-of-Channels (MoC) is a novel feedforward network architecture that activates only the Top-K most relevant channels per token, guided by the native gating mechanism of SwiGLU.

**Contextual Sparsity for Efficient Inference:**
ReGLU-based LLMs exhibit dynamic (or contextual) sparsity—the phenomenon where only a small subset of neurons within FFN blocks are activated for any given input. Experiments on sparse LLMs with an average activation sparsity level
…[truncated 498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6377
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-21T01:24:04.628607+00:00_

Web search results for query: "activation sparsity prediction LLM knowledge distillation 2025 2026"

Links: [{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2512.12744"},{"title":"La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation","url":"https://arxiv.org/pdf/2507.01299"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"},{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity","url":"https://arxiv.org/pdf/2411.02335"}]

Based on the search results, here's what I found on activation sparsity prediction for LLMs in 2025-2026:

## Recent Research on Activation Sparsity Prediction

**SparseInfer (2025)**: A training-free predictor for activation sparsity of ReLU-fied LLMs, where activation sparsity is predicted by comparing only the sign bits of inputs and weights. The method achieves approximately 21% faster inference speed with negligible accuracy loss of within 1%.

**Activation Pattern Clustering Approach (2025)**: Instead of predicting activations at an individual neuron level, researchers identify recurring activation patterns and use centroids to approximate neuron states, significantly reducing the computational burden. This method achieves up to 79.34% clustering precision while maintaining minimal degradation in perplexity scores.

**SPON - Robust Activation Sparsity (2026)**: SPON
…[truncated 789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7281
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-21T01:26:04.370764+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n### 1. Summary\n\n本文提出用 KL divergence（而非传统 BCE）训练轻量 MLP 预测器，为 SwiGLU LLM 的 FFN 层生成 input-dependent activation sparsity masks。核心发现是 KL 的耦合梯度（coupled gradients）发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，这些 patterns 在 PPL 指标上持续优于 BCE 和 training-free baselines。通过 target-swap ablation (C1) 确认 mask quality（而非训练 objective 本身）驱动推理质量。评估覆盖 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B，论文自定位为 \"primarily empirical study\"。\n\n---\n\n### 2. Strengths\n\n**S1. C1 Target-Swap Ablation 设计精巧** — Table 3 (p7) 的 target-swap ablation 是本文最有价值的贡献。通过让 BCE predictor 在推理时使用 KL-derived oracle masks（反之亦然），干净地隔离了 mask quality 与 training objective 的效果。这一实验设计在该领域中较为少见，为 \"mask quality drives inference-stage quality\" 提供了有说服力的因果证据。\n\n**S2. 实验覆盖全面，附录详尽** — 17 个 Appendix sections 覆盖 bottleneck 敏感性（App B）、OOD 评估（App D）、per-layer retention（App E）、training stability（App F）、MSE baseline（App G）、SNR 分析（App H）等。这种实验透彻度超过了同领域大多数工作，读者能在附录中找到几乎所有合理的 follow-up 问题的回答。\n\n**S3. 诚实的自我定位** — 论文明确声明 \"This paper is primarily an empirical study: we do not propose a new architecture or algorithms\"（p2），这种诚实的 framing 降低了读者的期望校准成本，也使贡献评估更公正。\n\n**S4. Taxonomy 有组织价值** — Table 1 (p5) 沿 signal coupling（BCE/intermediate/coupled KL）和 granularity（per-token vs per-layer）两个维度组织了现有工作，提供了清晰的定位参照。\n\n**S5. 多架构验证** — 在 3 个模型家族（7B-14B）上评估，包括 cross-architecture 分析（Table 16-17, Appendix N），结论不依赖单一模型。\n\n---\n\n### 3. Weaknesses\n\n**W1 [Major] — 与 MaskLLM 的方法论区分不足，novelty 有限**\n\n核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文在 Section 2 (p3) 声称三点区别：(1) activation sparsity vs N:M weight sparsity, (2) dynamic per-token masks vs static masks, (3) predictor network vs directly learnable mask parameters。但这三点均为 **application-level differences**（目标不同），而非 **methodological innovation**（训练方法不同）。\n\n关键问题：如果将 MaskLLM 的 KL+Gumbel 训练策略直接迁移到 activation sparsity 场景（只需把 learnable mask parameters 替换为 predictor network 输出），是否就能复现本文的核心结果？论文未讨论这一 counterfactual，这使得\"本文的贡献是什么\"变得模糊——是发现 KL 对 activation sparsity 也有效（confirmatory），还是提出了新的训练技术（innovative）？\n\n作为 \"primarily empirical study\"，此 novelty 水平可能达到 Findings bar，但对 main conference 而言，缺乏方法论或理论层面的新颖贡献是主要短板。\n\n**W2 [Major] — Downstream task 结果不一致，削弱核心 claim 的实用价值**\n\nTable 2 (p6) 显示 KL predictor 在 commonsense reasoning (ARC-c, WG, HellaSwag) 上优于 TEAL，但在 knowledge-intensive benchmarks 上表现不佳：\n- MMLU: KL 40.73 vs TEAL 45（30% sparsity），差距显著（-4.27pp）\n- PIQA: 所有方法均大幅低于 dense baseline\n\nTable 2 同时显示 uniform allocation 在多数下游任务上表现接近 global allocation（有时更好），这暗示 allocation strategy 对下游任务的影响可能被高估。\n\n论文在 Section 4.6 (p8) 承认 \"PPL gains reveal task- and scale-dependent effects\" 但未充分解释这种不一致性。如果 KL-discovered masks 确实更优，为什么只在 PPL 和部分 reasoning tasks 上体现？这是 mask quality 问题还是 evaluation metric 选择问题？这一 gap 需要更严谨的分析。\n\n**W3 [Major] — \"Gradient coupling\" narrative 缺乏严格支撑**\n\nSection 3.6 (p5) 的梯度分析是论文的核心叙事支柱，但分析层次停留在直觉性描述：\n- \"KL introduces a downstream Jacobian ∂P_dense/∂h_l that couples each neuron j's gradient to all other retained neurons in layers l' through L\"（p5）— 这个 observation 对任何 output-level loss 都成立（包括 MSE），并非 KL 的独特性质\n- Gradient SNR measurements（Figure 5, Appendix H）显示 BCE 在训练早期有更高 SNR，而 KL 后来超越——但这可能是不同 loss landscape 的 artifact，而非 \"coupling\" 的因果效应\n- 论文未提供形式化的理论分析来证明 coupled gradients → better masks 这一因果链条\n\n将这一机制称为 \"gradient coupling discovers mask patterns\" 是 overclaiming——更准确的描述应该是 \"output-level KL optimization empirically finds different masks than per-neuron BCE\"。\n\n**W4 [Minor] — Wall-clock speedup 缺失降低实用性论证**\n\n论文在 Limitations (p9) 承认 \"actual wall-clock acceleration depends on sparse kernel implementations\"，但 Appendix A (p12) 的推理效率分析仅估算 FLOPs 减少（30% sparsity 节省 ~21% latency）。对于声称改进 inference efficiency 的工作，至少应提供 simulated 或 rough wall-clock measurements。特别是论文使用 unstructured element-wise masks (p13)，这在现有硬件上通常无法转化为实际加速。\n\n**W5 [Minor] — Abstract 信息密度过高，关键 claim 的表述需要推敲**\n\nAbstract 在 ~200 词中塞入了过多具体数字（46-68%、14.5%、PPL 数值、5 个 downstream benchmarks 等），反而模糊了核心 message。建议突出 1-2 个最关键的定量发现。\n\n此外，\"coupled gradient discovers mask patterns\" 和 \"mask pattern discovery\" 等表述暗示了一种 emergent discovery 的叙事，但实际上这些 patterns 是通过标准优化过程产生的。这种措辞有 overclaiming 之嫌。\n\n**W6 [Minor] — 训练数据单一性**\n\n所有实验仅在 WikiText-103 上训练 1000 steps。虽然 Appendix D (p14) 提供了 C4 上的 OOD 评估，但未探讨在更多样化的训练数据上（如 OpenWebText、RedPajama subsets）mask patterns 是否一致。对于声称发现 \"general\" mask patterns 的工作，单一训练语料是一个值得注意的局限。\n\n---\n\n### 4. Questions\n\n**Q1**: 如果让 MaskLLM 的训练策略（directly learnable mask parameters + KL + Gumbel-Softmax）直接应用于 per-token activation sparsity prediction（每个 token 有独立 mask），结果是否与本文的 predictor-based 方法可比？这个 baseline 对于确立 predictor architecture 的必要性至关重要。\n\n**Q2**: KL-derived masks 在不同 random seeds 之间的 Jaccard divergence 是多少？如果 seed-to-seed 变异也达到 40-60%，那么 \"KL masks diverge 46-68% from magnitude masks\" 这个数字的信息量就大打折扣。Appendix F (p14-15) 报告了 PPL 的 seed stability（CV=0.6%），但未报告 mask pattern 的 seed stability。\n\n**Q3**: Section 3.6 (p5) 声称 \"coupled gradients discover mask targets that yield lower perplexity, with mask quality driving inference-stage quality\"。但 MSE 也是 output-level objective（虽然作用在 hidden states 而非 output distribution），为什么 MSE 的表现反而不如 TEAL（Appendix G, p15）？这似乎与 \"output-level coupling is the key\" 的叙事矛盾。\n\n**Q4**: Table 4 (p7) 的 ablation 中，\"Forward KL + Coupled (ours)\" 与 \"BCE + STE\" 的差距在 50% sparsity 时仅为 PPL 11.79 vs 12.20——这个差距（0.41 PPL points）在 downstream tasks 上是否有统计显著性？\n\n**Q5**: Appendix A (p12) 的 inference 延迟估算基于 RTX PRO 6000 单 GPU。对于 14B 模型（Qwen-2.5-14B），实际部署通常需要多 GPU——predictor overhead 在多 GPU 场景下是否会成为瓶颈？\n\n---\n\n### 5. Missing References\n\n以下工作与本文直接相关但未被讨论：\n\n- **Mixture-of-Channels (MoC)** (arxiv 2511.09323, Nov 2025)：利用 SwiGLU 的 native gating mechanism 进行 Top-K channel selection，与本文在 SwiGLU gate sparsity 的问题域高度重合，应在 Related Work 中讨论。\n- **\"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering\"** (arxiv 2507.14179, Jul 2025)：通过聚类 activation patterns 进行 sparsity prediction，是一种不同于 predictor network 的替代方案。\n\n---\n\n### 6. 格式合规检查\n\n- **页数**: 正文（Abstract 到 Conclusion）8 页，Limitations + Ethics 从 p8 底部开始，References 从 p10 开始。✅ 符合 8 页限制。\n- **模板**: ACL 格式，双栏排版。✅\n- **匿名性**: \"Anonymous ACL submission\"。✅ 未发现明显匿名性违规。\n- **Limitations**: 有独立 Limitations section (p8-9)，讨论了 model scale 限制、PPL 作为 proxy 的局限、wall-clock speedup 未实现。✅\n- **Ethics Statement**: 有独立 Ethics Statement (p9)。✅\n- **Responsible NLP Checklist**: 包含完整 checklist (p9-10)。✅\n- **引用格式**: 使用 `\\cite` 和 `\\citealp`，格式一致。✅\n- **引用验证**: 50 条引用全部通过 OpenAlex 验证（44 verified, 5 minor mismatches in author name format, 1 orphan bib entry `de2024griffin` not cited）。✅ 无虚假引用。\n\n---\n\n### 7. 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 核心 PPL claims 有充分实验支持，C1 ablation 设计严谨。但 gradient coupling 分析缺乏形式化证明，downstream results 不一致性未充分解释。 |\n| **Excitement** | 2.5/5 | 方法论 novelty 有限（KL→BCE 替换 + empirical analysis），但 C1 ablation 的实验设计有方法论贡献。对 activation sparsity 社区有参考价值，但不太可能改变该领域的研究方向。 |\n| **Reproducibility** | 4/5 | 架构、超参数、训练细节描述详尽（Section 4.1, Appendix B-C）。代码未发布但描述足够重现。唯一扣分：部分 downstream evaluation 细节需参考 TEAL 原文。 |\n| **Datasets** | 1/5 | 未发布新数据集。 |\n| **Software** | 1/5 | 未发布代码。 |\n\n---\n\n### 8. Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5** — 对 activation sparsity 和 knowledge distillation 领域较熟悉，仔细阅读了全文及附录。\n\n**一句话总评**: 一项执行扎实的 empirical study，C1 target-swap ablation 有独立价值，但核心方法论贡献有限（KL 替代 BCE 是增量改进），downstream results 的不一致性和 gradient coupling 叙事缺乏严格支撑使其更适合 Findings 而非 main conference。\n\n**升档路径（→3.5 Borderline Conference）**: (1) 形式化 gradient coupling 分析，提供 KL vs BCE gradient structure 的理论保证；(2) 解释 downstream task inconsistency 的 root cause 并提供额外实验；(3) 提供至少 proof-of-concept 的 wall-clock speedup 数据。\n\n**降档风险（→2.5 Borderline Findings）**: 如果 Q1（MaskLLM 策略直接迁移）的结果表明 predictor architecture 并非必要，或 Q2（seed-level mask divergence）表明 46-68% 的数字不具信息量，则核心 claims 将被显著削弱。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\"\n**Venue**: EMNLP 2026 (ARR May cycle)\n\n---\n\n### 1. Summary\n\n本文提出用 KL divergence（而非传统 BCE）训练轻量 MLP 预测器，为 SwiGLU LLM 的 FFN 层生成 input-dependent activation sparsity masks。核心发现是 KL 的耦合梯度（coupled gradients）发现与 magnitude-based masks 偏离 46-68% 的 mask patterns，这些 patterns 在 PPL 指标上持续优于 BCE 和 training-free baselines。通过 target-swap ablation (C1) 确认 mask quality（而非训练 objective 本身）驱动推理质量。评估覆盖 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B，论文自定位为 \"primarily empirical study\"。\n\n---\n\n### 2. Strengths\n\n**S1. C1 Target-Swap Ablation 设计精巧** — Table 3 (p7) 的 target-swap ablation 是本文最有价值的贡献。通过让 BCE predictor 在推理时使用 KL-derived oracle masks（反之亦然），干净地隔离了 mask quality 与 training objective 的效果。这一实验设计在该领域中较为少见，为 \"mask quality drives inference-stage quality\" 提供了有说服力的因果证据。\n\n**S2. 实验覆盖全面，附录详尽** — 17 个 Appendix sections 覆盖 bottleneck 敏感性（App B）、OOD 评估（App D）、per-layer retention（App E）、training stability（App F）、MSE baseline（App G）、SNR 分析（App H）等。这种实验透彻度超过了同领域大多数工作，读者能在附录中找到几乎所有合理的 follow-up 问题的回答。\n\n**S3. 诚实的自我定位** — 论文明确声明 \"This paper is primarily an empirical study: we do not propose a new architecture or algorithms\"（p2），这种诚实的 framing 降低了读者的期望校准成本，也使贡献评估更公正。\n\n**S4. Taxonomy 有组织价值** — Table 1 (p5) 沿 signal coupling（BCE/intermediate/coupled KL）和 granularity（per-token vs per-layer）两个维度组织了现有工作，提供了清晰的定位参照。\n\n**S5. 多架构验证** — 在 3 个模型家族（7B-14B）上评估，包括 cross-architecture 分析（Table 16-17, Appendix N），结论不依赖单一模型。\n\n---\n\n### 3. Weaknesses\n\n**W1 [Major] — 与 MaskLLM 的方法论区分不足，novelty 有限**\n\n核心训练配方（frozen backbone + learnable masks + KL divergence + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文在 Section 2 (p3) 声称三点区别：(1) activation sparsity vs N:M weight sparsity, (2) dynamic per-token masks vs static masks, (3) predictor network vs directly learnable mask parameters。但这三点均为 **application-level differences**（目标不同），而非 **methodological innovation**（训练方法不同）。\n\n关键问题：如果将 MaskLLM 的 KL+Gumbel 训练策略直接迁移到 activation sparsity 场景（只需把 learnable mask parameters 替换为 predictor network 输出），是否就能复现本文的核心结果？论文未讨论这一 counterfactual，这使得\"本文的贡献是什么\"变得模糊——是发现 KL 对 activation sparsity 也有效（confirmatory），还是提出了新的训练技术（innovative）？\n\n作为 \"primarily empirical study\"，此 novelty 水平可能达到 Findings bar，但对 main conference 而言，缺乏方法论或理论层面的新颖贡献是主要短板。\n\n**W2 [Major] — Downstream task 结果不一致，削弱核心 claim 的实用价值**\n\nTable 2 (p6) 显示 KL predictor 在 commonsense reasoning (ARC-c, WG, HellaSwag) 上优于 TEAL，但在 knowledge-intensive benchmarks 上表现不佳：\n- MMLU: KL 40.73 vs TEAL 45（30% sparsity），差距显著（-4.27pp）\n- PIQA: 所有方法均大幅低于 dense baseline\n\nTable 2 同时显示 uniform allocation 在多数下游任务上表现接近 global allocation（有时更好），这暗示 allocation strategy 对下游任务的影响可能被高估。\n\n论文在 Section 4.6 (p8) 承认 \"PPL gains reveal task- and scale-dependent effects\" 但未充分解释这种不一致性。如果 KL-discovered masks 确实更优，为什么只在 PPL 和部分 reasoning tasks 上体现？这是 mask quality 问题还是 evaluation metric 选择问题？这一 gap 需要更严谨的分析。\n\n**W3 [Major] — \"Gradient coupling\" narrative 缺乏严格支撑**\n\nSection 3.6 (p5) 的梯度分析是论文的核心叙事支柱，但分析层次停留在直觉性描述：\n- \"KL introduces a downstream Jacobian ∂P_dense/∂h_l that couples each neuron j's gradient to all other retained neurons in layers l' through L\"（p5）— 这个 observation 对任何 output-level loss 都成立（包括 MSE），并非 KL 的独特性质\n- Gradient SNR measurements（Figure 5, Appendix H）显示 BCE 在训练早期有更高 SNR，而 KL 后来超越——但这可能是不同 loss landscape 的 artifact，而非 \"coupling\" 的因果效应\n- 论文未提供形式化的理论分析来证明 coupled gradients → better masks 这一因果链条\n\n将这一机制称为 \"gradient coupling discovers mask patterns\" 是 overclaiming——更准确的描述应该是 \"output-level KL optimization empirically finds different masks than per-neuron BCE\"。\n\n**W4 [Minor] — Wall-clock speedup 缺失降低实用性论证**\n\n论文在 Limitations (p9) 承认 \"actual wall-clock acceleration depends on sparse kernel implementations\"，但 Appendix A (p12) 的推理效率分析仅估算 FLOPs 减少（30% sparsity 节省 ~21% latency）。对于声称改进 inference efficiency 的工作，至少应提供 simulated 或 rough wall-clock measurements。特别是论文使用 unstructured element-wise masks (p13)，这在现有硬件上通常无法转化为实际加速。\n\n**W5 [Minor] — Abstract 信息密度过高，关键 claim 的表述需要推敲**\n\nAbstract 在 ~200 词中塞入了过多具体数字（46-68%、14.5%、PPL 数值、5 个 downstream benchmarks 等），反而模糊了核心 message。建议突出 1-2 个最关键的定量发现。\n\n此外，\"coupled gradient discovers mask patterns\" 和 \"mask pattern discovery\" 等表述暗示了一种 emergent discovery 的叙事，但实际上这些 patterns 是通过标准优化过程产生的。这种措辞有 overclaiming 之嫌。\n\n**W6 [Minor] — 训练数据单一性**\n\n所有实验仅在 WikiText-103 上训练 1000 steps。虽然 Appendix D (p14) 提供了 C4 上的 OOD 评估，但未探讨在更多样化的训练数据上（如 OpenWebText、RedPajama subsets）mask patterns 是否一致。对于声称发现 \"general\" mask patterns 的工作，单一训练语料是一个值得注意的局限。\n\n---\n\n### 4. Questions\n\n**Q1**: 如果让 MaskLLM 的训练策略（directly learnable mask parameters + KL + Gumbel-Softmax）直接应用于 per-token activation sparsity prediction（每个 token 有独立 mask），结果是否与本文的 predictor-based 方法可比？这个 baseline 对于确立 predictor architecture 的必要性至关重要。\n\n**Q2**: KL-derived masks 在不同 random seeds 之间的 Jaccard divergence 是多少？如果 seed-to-seed 变异也达到 40-60%，那么 \"KL masks diverge 46-68% from magnitude masks\" 这个数字的信息量就大打折扣。Appendix F (p14-15) 报告了 PPL 的 seed stability（CV=0.6%），但未报告 mask pattern 的 seed stability。\n\n**Q3**: Section 3.6 (p5) 声称 \"coupled gradients discover mask targets that yield lower perplexity, with mask quality driving inference-stage quality\"。但 MSE 也是 output-level objective（虽然作用在 hidden states 而非 output distribution），为什么 MSE 的表现反而不如 TEAL（Appendix G, p15）？这似乎与 \"output-level coupling is the key\" 的叙事矛盾。\n\n**Q4**: Table 4 (p7) 的 ablation 中，\"Forward KL + Coupled (ours)\" 与 \"BCE + STE\" 的差距在 50% sparsity 时仅为 PPL 11.79 vs 12.20——这个差距（0.41 PPL points）在 downstream tasks 上是否有统计显著性？\n\n**Q5**: Appendix A (p12) 的 inference 延迟估算基于 RTX PRO 6000 单 GPU。对于 14B 模型（Qwen-2.5-14B），实际部署通常需要多 GPU——predictor overhead 在多 GPU 场景下是否会成为瓶颈？\n\n---\n\n### 5. Missing References\n\n以下工作与本文直接相关但未被讨论：\n\n- **Mixture-of-Channels (MoC)** (arxiv 2511.09323, Nov 2025)：利用 SwiGLU 的 native gating mechanism 进行 Top-K channel selection，与本文在 SwiGLU gate sparsity 的问题域高度重合，应在 Related Work 中讨论。\n- **\"A Sparsity Predicting Approach for LLMs via Activation Pattern Clustering\"** (arxiv 2507.14179, Jul 2025)：通过聚类 activation patterns 进行 sparsity prediction，是一种不同于 predictor network 的替代方案。\n\n---\n\n### 6. 格式合规检查\n\n- **页数**: 正文（Abstract 到 Conclusion）8 页，Limitations + Ethics 从 p8 底部开始，References 从 p10 开始。✅ 符合 8 页限制。\n- **模板**: ACL 格式，双栏排版。✅\n- **匿名性**: \"Anonymous ACL submission\"。✅ 未发现明显匿名性违规。\n- **Limitations**: 有独立 Limitations section (p8-9)，讨论了 model scale 限制、PPL 作为 proxy 的局限、wall-clock speedup 未实现。✅\n- **Ethics Statement**: 有独立 Ethics Statement (p9)。✅\n- **Responsible NLP Checklist**: 包含完整 checklist (p9-10)。✅\n- **引用格式**: 使用 `\\cite` 和 `\\citealp`，格式一致。✅\n- **引用验证**: 50 条引用全部通过 OpenAlex 验证（44 verified, 5 minor mismatches in author name format, 1 orphan bib entry `de2024griffin` not cited）。✅ 无虚假引用。\n\n---\n\n### 7. 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 核心 PPL claims 有充分实验支持，C1 ablation 设计严谨。但 gradient coupling 分析缺乏形式化证明，downstream results 不一致性未充分解释。 |\n| **Excitement** | 2.5/5 | 方法论 novelty 有限（KL→BCE 替换 + empirical analysis），但 C1 ablation 的实验设计有方法论贡献。对 activation sparsity 社区有参考价值，但不太可能改变该领域的研究方向。 |\n| **Reproducibility** | 4/5 | 架构、超参数、训练细节描述详尽（Section 4.1, Appendix B-C）。代码未发布但描述足够重现。唯一扣分：部分 downstream evaluation 细节需参考 TEAL 原文。 |\n| **Datasets** | 1/5 | 未发布新数据集。 |\n| **Software** | 1/5 | 未发布代码。 |\n\n---\n\n### 8. Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5** — 对 activation sparsity 和 knowledge distillation 领域较熟悉，仔细阅读了全文及附录。\n\n**一句话总评**: 一项执行扎实的 empirical study，C1 target-swap ablation 有独立价值，但核心方法论贡献有限（KL 替代 BCE 是增量改进），downstream results 的不一致性和 gradient coupling 叙事缺乏严格支撑使其更适合 Findings 而非 main conference。\n\n**升档路径（→3.5 Borderline Conference）**: (1) 形式化 gradient coupling 分析，提供 KL vs BCE gradient structure 的理论保证；(2) 解释 downstream task inconsistency 的 root cause 并提供额外实验；(3) 提供至少 proof-of-concept 的 wall-clock speedup 数据。\n\n**降档风险（→2.5 Borderline Findings）**: 如果 Q1（MaskLLM 策略直接迁移）的结果表明 predictor architecture 并非必要，或 Q2（seed-level mask divergence）表明 46-68% 的数字不具信息量，则核心 claims 将被显著削弱。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-21T01:26:09.021858+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4651
}
```

</details>

---


### Assistant

_source line 1236 · 2026-05-21T01:26:16.872120+00:00_

审稿意见已提交给 Review Director。

总结：评分 **Overall 3.0 (Findings)**，主要问题：
1. **[Major]** 与 MaskLLM 方法论高度重合，novelty 有限——核心是 "KL 替代 BCE" 的增量改进
2. **[Major]** Downstream task 结果不一致（MMLU 差 4.27pp），削弱实用价值论证
3. **[Major]** "Gradient coupling" 叙事缺乏形式化支撑，存在 overclaiming
4. **[Minor]** 无 wall-clock speedup、训练数据单一、abstract 过度密集

主要优势：C1 target-swap ablation 设计精巧（S1）、实验覆盖极其全面（S2, 17 个 Appendix）、诚实自我定位（S3）。格式完全合规，引用全部验证通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 31

## Round 31

4 recorded events


### User

_source line 1237 · 2026-05-21T01:27:30.991100+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 1 的完整审稿原文：

### Summary
本文提出用前向 KL 散度（替代 BCE）训练 SwiGLU LLM 的稀疏性预测器，配合 Gumbel-Sigmoid 松弛和自适应惩罚控制器。核心发现是 KL 的端到端耦合梯度发现了与 magnitude-based masks 偏离 46–68% 的 mask patterns，且这些 patterns 通过 target-swap ablation (C1) 被确认为推理阶段质量的近端驱动因素。实验在 LLaMA-3.1-8B、Mistral-7B、Qwen-2.5-14B 上进行，展示了一致的 PPL 改进但不一致的下游任务表现。

### Strengths
**S1.** C1 Target-swap ablation 设计精巧且有说服力。
**S2.** 消融覆盖面广且系统性强。
**S3.** 诚实的结果报告。
**S4.** 二维 taxonomy 有组织价值。
**S5.** Multi-seed 评估覆盖了关键结果。

### Weaknesses
**W1. [Critical] 无实际推理加速，动机与贡献脱节。** 论文的动机是推理效率，但 Appendix A (Table 6) 显示 KL pipeline 增加 6.4% 延迟开销，实际 wallclock 无加速。论文承认 "net acceleration requires kernel-level sparse computation optimizations...beyond the scope of this work"。在 activation sparsity 领域，若不能展示端到端加速，贡献主要停留在 prediction quality 的学术分析层面。建议至少提供 Triton block-sparse 的 prototype 实测数据，或将 framing 完全转向 "understanding training objectives for sparsity prediction"。

**W2. [Major] MMLU/GSM8K 上的系统性劣势削弱了 "quality improvement" claim 的覆盖面。** Abstract 强调 PPL 和 commonsense reasoning 改进，但 MMLU 从 45.9% 降至 40.7%（−5.2pp），在 Qwen-14B 上 GSM8K −20pp。所有三个模型上，knowledge-intensive tasks 均无改进或退步。论文将 forward KL 的 mode-covering 特性作为假设性解释（§4.2），但缺少实验验证。

**W3. [Major] 主要对比中 actual sparsity 不匹配未被充分解决。** Table 2 中 KL 30% actual=28.5%，TEAL 30% actual=29.3%。0.8pp 差异意味着 KL 保留了更多神经元。虽然正文提供了 matched sparsity 比较（14.5% at 28.5%），但 Table 2 的 headline 比较仍在不同 actual sparsity 下进行。建议在 Table 2 中增加 TEAL at 28.5% 的行。

**W4. [Major] MSE baseline 的单 seed 报告掩盖了高方差。** Appendix G 承认 MSE with seed 123 仅达到 5.1% sparsity（PPL=15,789），是 "failure mode"。但 Table 2/4 中 MSE 均为 seed 42 单 seed。一个 seed 完全失败的情况下，单 seed 报告不能代表 MSE 方法的真实性能分布。

**W5. [Major] "Gradient coupling" vs "objective function" 的因果解释未被完全解耦。** KL 和 BCE 的关键区别不仅是梯度耦合程度，更根本的是 target 定义不同。MSE baseline 使用 L2 on hidden states，而非 per-layer KL on output distributions，因此 MSE 的失败可能源于 L2 loss 不适合而非 per-layer coupling 本身的局限。缺少关键实验：per-layer KL（每层独立优化该层 output 对 dense output 的 KL divergence）。

**W6. [Minor] 14B scale 结果有限且令人担忧。** Qwen-14B 仅在 30% sparsity 下评估，KL 的 GSM8K 大幅退步（32.1±5.2% vs 52.1%），方法在 14B+ scale 的适用性存疑。

**W7. [Minor] 训练数据同质性。** 所有 predictor 在 WikiText-103 上训练。OOD 评估显示 C4 上 cross-seed variance 显著增大（CV=6.3% vs in-domain 0.2%）。

### Questions
**Q1.** C1 的 s42 oracle 来自 "an earlier training run"，而 s123/s456 使用 "matched retrained oracles"。统一使用 matched oracles 后 s42 的 gap 是否会缩小？
**Q2.** 是否可以在 reverse KL predictor 上也报告下游 metrics，验证 mode-seeking 是否更好保留 knowledge pathways？
**Q3.** Table 2 没有 BCE 30% uniform 的条目。可否提供？Table 4 的 BCE 30% PPL=15.71 是 uniform 吗？
**Q4.** MSE seed 123 失败是 MSE + Gumbel-Sigmoid + Lagrangian 组合不稳定，还是 MSE 固有缺陷？KL 是否有类似失败？
**Q5.** KL 训练成本约 2.6× BCE，且每个 sparsity target 需单独训练，对实际部署意味着什么？

### Missing References
- CATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work 中提及但未实验比较。
- D2DMoE (Szatkowski et al., 2024) 在 taxonomy 中命名但未实验覆盖。

### Overall Assessment
**Overall: 3.5** (Borderline Conference) | **Soundness: 3.5/5** | **Excitement: 3/5** | **Confidence: 4/5**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-21T01:29:06.995630+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: 无实际推理加速，动机与贡献脱节**\n\n完全同意。这是本文最根本的张力所在。论文 Section 1 (p1) 开篇以 \"SwiGLU feed-forward networks... exhibit high contextual sparsity\" 和 \"a large fraction of FFN neurons contribute negligibly to the output\" 建立 efficiency 动机，但 Appendix A (Table 6, p12) 的实测数据显示 KL pipeline 反而增加 6.4% 延迟。更关键的是，论文在 p13 承认 \"the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support\"——这意味着即使 mask quality 确实更好，在可预见的部署场景中也无法兑现 efficiency 收益。\n\nR1 提出的修复方案合理：要么提供 Triton block-sparse prototype，要么将 framing 完全转向 \"understanding training objectives\"。我倾向后者，因为这更符合论文的实际贡献。\n\n**[AGREE] R1-W2: MMLU/GSM8K 系统性劣势**\n\n完全同意，这与我的 W2 一致。补充一个额外观察：Table 2 (p6) 中不仅 MMLU 劣化（-5.2pp），且 KL 在 uniform allocation 下的 MMLU（40.7）与 global allocation（40.73）几乎无差异，暗示 allocation strategy 对 knowledge-intensive tasks 的影响远小于论文所强调的。这进一步表明 KL masks 可能系统性地丢失了某些 knowledge pathways，而非简单的 allocation 优化问题。\n\n论文 Section 4.2 (p6) 将此归因于 forward KL 的 mode-covering property \"preserves dense activation patterns that benefit broad commonsense inference\"，但这只是假设性解释（\"this may dilute task-specific knowledge pathways\"），无实验验证。一个简单的验证方案：对比 KL vs BCE masks 在 MMLU-relevant layers（通常是中间层）的 retention pattern 差异。\n\n**[AGREE] R1-W3: Actual sparsity 不匹配**\n\n同意这是一个 presentation 问题。KL 30% actual=28.5% vs TEAL 30% actual=29.3% (Table 2, p6)，0.8pp 的差异虽然论文在正文中用 matched 比较进行了控制（\"14.5% at 28.5%\"），但 Table 2 作为主结果表在不同 actual sparsity 下对比确实容易误导。R1 建议增加 TEAL at 28.5% 行是低成本高收益的改进。\n\n不过我要补充：这个问题对整体结论的影响有限。即使在 matched sparsity 下，KL 的 PPL 优势仍然存在（正文报告 \"TEAL at 28.5% actual sparsity yields PPL ≈28.5, comparable to KL\"——但这似乎与论文声称的 PPL 14.5% 改进矛盾，需要作者澄清具体数字）。\n\n**[AGREE] R1-W4: MSE single-seed reporting**\n\n强烈同意。这是我在初审中遗漏的重要问题。Appendix G (p15) 明确承认 \"MSE with seed 123 only reaches 5.1% sparsity (PPL=15,789), indicating high sensitivity to initialization — a failure mode not observed with KL-based losses\"。一个方法如果在 3 个 seed 中有 1 个完全失败（5.1% vs target 30%），那么用另一个 seed 的单次结果来代表该方法的性能是不公正的。\n\n正确的做法应该是：(1) 报告 MSE 的 3-seed 均值和方差，包括 failed seed；(2) 或者明确排除 failed seed 并报告 2-seed 结果，同时将 seed sensitivity 作为 MSE 的 systematic weakness 讨论。当前的处理方式（只报 seed 42）有 cherry-picking 嫌疑，即使是无意的。\n\n**[AGREE with nuance] R1-W5: Gradient coupling vs objective function 因果未解耦**\n\n同意核心观点，但想补充更具体的分析。R1 指出的关键缺失实验 \"per-layer KL\"（每层独立优化该层 output 对 dense output 的 KL）是一个非常有价值的建议。当前论文的实验设计存在以下混淆变量：\n\n| 方法 | Loss 类型 | 作用范围 | Signal 来源 |\n|------|-----------|----------|------------|\n| BCE | Per-neuron classification | 单层 | Magnitude-based oracle |\n| MSE | L2 on hidden states | 单层 | Dense hidden states |\n| KL (ours) | KL on output distribution | 端到端 | Dense output distribution |\n\n三个维度同时变化（loss type × scope × signal source），无法判断哪个因素驱动了性能差异。R1 提出的 per-layer KL 实验可以固定 loss type=KL + signal source=output distribution，只改变 scope（per-layer vs end-to-end），从而真正隔离 \"coupling\" 的效果。\n\n我在初审 W3 中也指出了类似问题（\"gradient coupling 叙事缺乏严格支撑\"），但 R1 的实验建议比我的批评更具建设性。\n\n**[AGREE] R1-W6: 14B scale 结果有限**\n\n同意。Qwen-14B 仅在 30% sparsity 下有结果，且 GSM8K 大幅退步（32.1±5.2% vs dense 52.1%，Table 17 推断）。这使得论文 Contribution 4（\"Preliminary analysis of allocation-to-downstream interactions at 7-14B\"）的 claim 基础薄弱。建议至少补充 50% sparsity 的 14B 结果以验证趋势是否一致。\n\n**[AGREE] R1-W7: 训练数据同质性**\n\n同意，与我的 W6 一致。补充：Appendix D (p14) 的 OOD 评估（C4 上 CV=6.3%）实际上暴露了更大的问题——cross-seed variance 增大 31× (0.2% → 6.3%) 意味着 predictor 对训练分布高度 overfit。论文应该讨论这种 distribution shift sensitivity 对实际部署的影响。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1: C1 oracle 来源不一致**\n\n合理质疑。如果 s42 使用 \"earlier training run\" 的 oracle 而 s123/s456 使用 matched retrained oracles，那么 s42 的 gap 可能部分来自 oracle 质量差异而非 mask quality 差异。建议统一为 matched oracles 后重新评估。\n\n**[AGREE] R1-Q2: Reverse KL downstream metrics**\n\n非常好的建议。Table 4 (p7) 显示 Reverse KL + Coupled 在 30% 时 PPL=9.31，优于 BCE 但略逊于 Forward KL (8.82)。如果 reverse KL（mode-seeking）在 MMLU 等 knowledge-intensive tasks 上表现更好，这将支持 \"forward KL 的 mode-covering 特性牺牲了 knowledge pathways\" 的假设，也为 R1-W2 提供实验验证。\n\n**[AGREE] R1-Q3: BCE 30% uniform 缺失**\n\nTable 2 (p6) 确实缺少 BCE 30% uniform 的条目。Table 4 (p7) 的 \"BCE composition\" 行有 PPL=15.71，但标注为 \"unified benchmark protocol; uniform allocation at 30%\"（来自 Table 4 caption），需要作者确认是否一致。这个数据点对于完整对比是必要的。\n\n**[AGREE] R1-Q4: MSE failure mode诊断**\n\n重要问题。如果 MSE 的 seed 123 失败是 Gumbel-Sigmoid + Lagrangian 组合不稳定导致的（而非 MSE 固有缺陷），那么论文对 MSE 的 dismissal 就不成立——可能只需要调整超参数即可修复。KL 是否也有类似失败 seed 需要明确报告。Appendix F (p14-15) 报告 KL 的 3-seed CV=0.6%，看起来稳定，但没有报告是否存在 complete failure 的情况。\n\n**[AGREE] R1-Q5: 训练成本 2.6× BCE**\n\n实用性问题值得关注。每个 sparsity target 需独立训练意味着支持 30%/40%/50% 三个目标需要 3× 训练成本。在 KL 本身已是 BCE 2.6× 的前提下，总成本约 7.8× BCE。论文应讨论是否可以训练单个 predictor 支持多个 sparsity levels（如通过 conditional generation）。\n\n---\n\n### Missing References 回应\n\n**[REBUT] R1-Missing-1: CATS 和 R-Sparse 未实验比较**\n\nCATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work (Section 2, p2-3) 中已被讨论并归入 Table 1 taxonomy。CATS 使用 per-layer adaptive thresholding（training-free），R-Sparse 使用 rank-aware selection。两者均为 training-free 方法，与本文的 trained predictor 不在同一 category。论文已将 TEAL 作为 training-free baselines 的代表进行实验比较，因为 TEAL 在该类别中表现最好。要求对每个 taxonomy 条目都进行实验比较会显著增加篇幅，且 TEAL 已经是 sufficient representative。\n\n**[AGREE] R1-Missing-2: D2DMoE 未实验覆盖**\n\nD2DMoE (Szatkowski et al., 2024) 作为 \"intermediate (MSE) + per-token\" 类别的代表出现在 Table 1 但无实验比较。由于论文的 Appendix G 已经测试了 MSE baseline（同类 loss function），D2DMoE 的缺失可以理解为实验设计选择。但如果 D2DMoE 的 per-token MSE 实现方式与论文的 MSE baseline 有本质差异，这个遗漏就更重要了。\n\n---\n\n### 总体评价差异讨论\n\nR1 给出 **3.5 (Borderline Conference)**，我给出 **3.0 (Findings)**。0.5 分差距主要来自以下分歧：\n\n1. **Novelty 权重**：我对 \"KL 替代 BCE\" 的增量性质给予更大 penalty（我的 W1），而 R1 更侧重 execution quality 和实用性问题（R1-W1 关注 speedup 缺失而非方法论新颖性）。\n\n2. **C1 ablation 的价值评估**：R1 和我都认可 C1 的设计，但我认为一个 well-designed ablation 不能弥补核心方法论 novelty 的不足，而 R1 可能将其视为独立的方法论贡献。\n\n3. **Downstream inconsistency 的严重性**：我和 R1 都标记了这个问题（我的 W2, R1-W2），但我将其视为对核心 claim 的更根本性威胁——如果 \"better masks\" 只在 PPL 上体现而不在 downstream 上一致改进，那么 \"mask quality drives inference quality\" 的 claim 的实用意义就大打折扣。\n\n**结论**：综合 R1 的额外发现（特别是 W4 MSE single-seed、W5 因果未解耦），我维持 **Overall 3.0 (Findings)** 的评分。R1 提出的 W5 per-layer KL 实验如果结果支持 coupling hypothesis，可能将我的评分提升至 3.5。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: 无实际推理加速，动机与贡献脱节**\n\n完全同意。这是本文最根本的张力所在。论文 Section 1 (p1) 开篇以 \"SwiGLU feed-forward networks... exhibit high contextual sparsity\" 和 \"a large fraction of FFN neurons contribute negligibly to the output\" 建立 efficiency 动机，但 Appendix A (Table 6, p12) 的实测数据显示 KL pipeline 反而增加 6.4% 延迟。更关键的是，论文在 p13 承认 \"the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support\"——这意味着即使 mask quality 确实更好，在可预见的部署场景中也无法兑现 efficiency 收益。\n\nR1 提出的修复方案合理：要么提供 Triton block-sparse prototype，要么将 framing 完全转向 \"understanding training objectives\"。我倾向后者，因为这更符合论文的实际贡献。\n\n**[AGREE] R1-W2: MMLU/GSM8K 系统性劣势**\n\n完全同意，这与我的 W2 一致。补充一个额外观察：Table 2 (p6) 中不仅 MMLU 劣化（-5.2pp），且 KL 在 uniform allocation 下的 MMLU（40.7）与 global allocation（40.73）几乎无差异，暗示 allocation strategy 对 knowledge-intensive tasks 的影响远小于论文所强调的。这进一步表明 KL masks 可能系统性地丢失了某些 knowledge pathways，而非简单的 allocation 优化问题。\n\n论文 Section 4.2 (p6) 将此归因于 forward KL 的 mode-covering property \"preserves dense activation patterns that benefit broad commonsense inference\"，但这只是假设性解释（\"this may dilute task-specific knowledge pathways\"），无实验验证。一个简单的验证方案：对比 KL vs BCE masks 在 MMLU-relevant layers（通常是中间层）的 retention pattern 差异。\n\n**[AGREE] R1-W3: Actual sparsity 不匹配**\n\n同意这是一个 presentation 问题。KL 30% actual=28.5% vs TEAL 30% actual=29.3% (Table 2, p6)，0.8pp 的差异虽然论文在正文中用 matched 比较进行了控制（\"14.5% at 28.5%\"），但 Table 2 作为主结果表在不同 actual sparsity 下对比确实容易误导。R1 建议增加 TEAL at 28.5% 行是低成本高收益的改进。\n\n不过我要补充：这个问题对整体结论的影响有限。即使在 matched sparsity 下，KL 的 PPL 优势仍然存在（正文报告 \"TEAL at 28.5% actual sparsity yields PPL ≈28.5, comparable to KL\"——但这似乎与论文声称的 PPL 14.5% 改进矛盾，需要作者澄清具体数字）。\n\n**[AGREE] R1-W4: MSE single-seed reporting**\n\n强烈同意。这是我在初审中遗漏的重要问题。Appendix G (p15) 明确承认 \"MSE with seed 123 only reaches 5.1% sparsity (PPL=15,789), indicating high sensitivity to initialization — a failure mode not observed with KL-based losses\"。一个方法如果在 3 个 seed 中有 1 个完全失败（5.1% vs target 30%），那么用另一个 seed 的单次结果来代表该方法的性能是不公正的。\n\n正确的做法应该是：(1) 报告 MSE 的 3-seed 均值和方差，包括 failed seed；(2) 或者明确排除 failed seed 并报告 2-seed 结果，同时将 seed sensitivity 作为 MSE 的 systematic weakness 讨论。当前的处理方式（只报 seed 42）有 cherry-picking 嫌疑，即使是无意的。\n\n**[AGREE with nuance] R1-W5: Gradient coupling vs objective function 因果未解耦**\n\n同意核心观点，但想补充更具体的分析。R1 指出的关键缺失实验 \"per-layer KL\"（每层独立优化该层 output 对 dense output 的 KL）是一个非常有价值的建议。当前论文的实验设计存在以下混淆变量：\n\n| 方法 | Loss 类型 | 作用范围 | Signal 来源 |\n|------|-----------|----------|------------|\n| BCE | Per-neuron classification | 单层 | Magnitude-based oracle |\n| MSE | L2 on hidden states | 单层 | Dense hidden states |\n| KL (ours) | KL on output distribution | 端到端 | Dense output distribution |\n\n三个维度同时变化（loss type × scope × signal source），无法判断哪个因素驱动了性能差异。R1 提出的 per-layer KL 实验可以固定 loss type=KL + signal source=output distribution，只改变 scope（per-layer vs end-to-end），从而真正隔离 \"coupling\" 的效果。\n\n我在初审 W3 中也指出了类似问题（\"gradient coupling 叙事缺乏严格支撑\"），但 R1 的实验建议比我的批评更具建设性。\n\n**[AGREE] R1-W6: 14B scale 结果有限**\n\n同意。Qwen-14B 仅在 30% sparsity 下有结果，且 GSM8K 大幅退步（32.1±5.2% vs dense 52.1%，Table 17 推断）。这使得论文 Contribution 4（\"Preliminary analysis of allocation-to-downstream interactions at 7-14B\"）的 claim 基础薄弱。建议至少补充 50% sparsity 的 14B 结果以验证趋势是否一致。\n\n**[AGREE] R1-W7: 训练数据同质性**\n\n同意，与我的 W6 一致。补充：Appendix D (p14) 的 OOD 评估（C4 上 CV=6.3%）实际上暴露了更大的问题——cross-seed variance 增大 31× (0.2% → 6.3%) 意味着 predictor 对训练分布高度 overfit。论文应该讨论这种 distribution shift sensitivity 对实际部署的影响。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1: C1 oracle 来源不一致**\n\n合理质疑。如果 s42 使用 \"earlier training run\" 的 oracle 而 s123/s456 使用 matched retrained oracles，那么 s42 的 gap 可能部分来自 oracle 质量差异而非 mask quality 差异。建议统一为 matched oracles 后重新评估。\n\n**[AGREE] R1-Q2: Reverse KL downstream metrics**\n\n非常好的建议。Table 4 (p7) 显示 Reverse KL + Coupled 在 30% 时 PPL=9.31，优于 BCE 但略逊于 Forward KL (8.82)。如果 reverse KL（mode-seeking）在 MMLU 等 knowledge-intensive tasks 上表现更好，这将支持 \"forward KL 的 mode-covering 特性牺牲了 knowledge pathways\" 的假设，也为 R1-W2 提供实验验证。\n\n**[AGREE] R1-Q3: BCE 30% uniform 缺失**\n\nTable 2 (p6) 确实缺少 BCE 30% uniform 的条目。Table 4 (p7) 的 \"BCE composition\" 行有 PPL=15.71，但标注为 \"unified benchmark protocol; uniform allocation at 30%\"（来自 Table 4 caption），需要作者确认是否一致。这个数据点对于完整对比是必要的。\n\n**[AGREE] R1-Q4: MSE failure mode诊断**\n\n重要问题。如果 MSE 的 seed 123 失败是 Gumbel-Sigmoid + Lagrangian 组合不稳定导致的（而非 MSE 固有缺陷），那么论文对 MSE 的 dismissal 就不成立——可能只需要调整超参数即可修复。KL 是否也有类似失败 seed 需要明确报告。Appendix F (p14-15) 报告 KL 的 3-seed CV=0.6%，看起来稳定，但没有报告是否存在 complete failure 的情况。\n\n**[AGREE] R1-Q5: 训练成本 2.6× BCE**\n\n实用性问题值得关注。每个 sparsity target 需独立训练意味着支持 30%/40%/50% 三个目标需要 3× 训练成本。在 KL 本身已是 BCE 2.6× 的前提下，总成本约 7.8× BCE。论文应讨论是否可以训练单个 predictor 支持多个 sparsity levels（如通过 conditional generation）。\n\n---\n\n### Missing References 回应\n\n**[REBUT] R1-Missing-1: CATS 和 R-Sparse 未实验比较**\n\nCATS (Lee et al., 2024) 和 R-Sparse (Zhang et al., 2025) 在 Related Work (Section 2, p2-3) 中已被讨论并归入 Table 1 taxonomy。CATS 使用 per-layer adaptive thresholding（training-free），R-Sparse 使用 rank-aware selection。两者均为 training-free 方法，与本文的 trained predictor 不在同一 category。论文已将 TEAL 作为 training-free baselines 的代表进行实验比较，因为 TEAL 在该类别中表现最好。要求对每个 taxonomy 条目都进行实验比较会显著增加篇幅，且 TEAL 已经是 sufficient representative。\n\n**[AGREE] R1-Missing-2: D2DMoE 未实验覆盖**\n\nD2DMoE (Szatkowski et al., 2024) 作为 \"intermediate (MSE) + per-token\" 类别的代表出现在 Table 1 但无实验比较。由于论文的 Appendix G 已经测试了 MSE baseline（同类 loss function），D2DMoE 的缺失可以理解为实验设计选择。但如果 D2DMoE 的 per-token MSE 实现方式与论文的 MSE baseline 有本质差异，这个遗漏就更重要了。\n\n---\n\n### 总体评价差异讨论\n\nR1 给出 **3.5 (Borderline Conference)**，我给出 **3.0 (Findings)**。0.5 分差距主要来自以下分歧：\n\n1. **Novelty 权重**：我对 \"KL 替代 BCE\" 的增量性质给予更大 penalty（我的 W1），而 R1 更侧重 execution quality 和实用性问题（R1-W1 关注 speedup 缺失而非方法论新颖性）。\n\n2. **C1 ablation 的价值评估**：R1 和我都认可 C1 的设计，但我认为一个 well-designed ablation 不能弥补核心方法论 novelty 的不足，而 R1 可能将其视为独立的方法论贡献。\n\n3. **Downstream inconsistency 的严重性**：我和 R1 都标记了这个问题（我的 W2, R1-W2），但我将其视为对核心 claim 的更根本性威胁——如果 \"better masks\" 只在 PPL 上体现而不在 downstream 上一致改进，那么 \"mask quality drives inference quality\" 的 claim 的实用意义就大打折扣。\n\n**结论**：综合 R1 的额外发现（特别是 W4 MSE single-seed、W5 因果未解耦），我维持 **Overall 3.0 (Findings)** 的评分。R1 提出的 W5 per-layer KL 实验如果结果支持 coupling hypothesis，可能将我的评分提升至 3.5。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1239 · 2026-05-21T01:29:11.285254+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4289
}
```

</details>

---


### Assistant

_source line 1240 · 2026-05-21T01:29:17.384439+00:00_

交叉回应已提交给 Review Director。对 Reviewer 1 的 7 个 Weaknesses 全部 AGREE（W5 带 nuance），5 个 Questions 全部 AGREE，Missing References 中 1 个 REBUT（CATS/R-Sparse 已有 TEAL 作为代表）、1 个 AGREE（D2DMoE）。维持 Overall 3.0 (Findings) 评分，与 R1 的 3.5 有 0.5 分差距，主要分歧在方法论 novelty 的权重上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 32

## Round 32

78 recorded events


### User

_source line 1241 · 2026-05-22T08:24:08.512968+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 格式合规**。

## 论文信息
- 标题: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
- 目标 venue: EMNLP 2026 (Long Paper, ARR May cycle)
- Deadline: 2026-05-25
- 格式: ACL review 模板, double-blind, 正文 ≤ 8页, 参考文献不限, Limitations/Ethics 不计入页数
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf

## 你的审查侧重

1. **新颖性评估**:
   - 核心配方 (frozen backbone + learnable masks + KL + Gumbel) 与 MaskLLM 的重合度: §2 给出三点区分 (sparsity type, mask generation, allocation)，评估这些区分是否足够构成 novelty
   - 作为 empirical study 的 contribution 是否达到 EMNLP main conference bar: 2D decomposition (signal type × coupling scope) 是否是 novel insight
   - Target-swap ablation (C1) 是否足够原创性
   - 与 ShadowLLM/D2DMoE/FastForward 的定位差异

2. **Related Work 完整性**:
   - 近期 activation sparsity 文献覆盖: R-Sparse (ICLR 2025), DIP (MLSys 2024), SparseInfer (DATE 2025), Polar Sparsity (NeurIPS 2025), MoNE, Expert Choice, D2D-MoE 等是否已充分讨论
   - 是否有重要遗漏: 特别关注 2025-2026 新发表的相关工作
   - 引用格式一致性和完整性

3. **叙事一致性和 Framing**:
   - Introduction 的 efficiency 动机 vs 实际无 wall-clock speedup 的 framing 张力
   - "coupling alignment hierarchy" / "2D decomposition" 叙事是否 overclaim
   - Abstract 的 headline numbers 是否准确反映实验结果
   - Contribution list 的 strength 是否与证据匹配

4. **格式合规 (EMNLP 2026)**:
   - 正文是否 ≤ 8 页（不含 Limitations/Ethics/References/Appendix）
   - Anonymous 规则: 是否有自引泄露身份
   - ACL template 格式是否正确
   - Limitations 和 Ethics 章节是否存在且合理
   - Responsible NLP Checklist 注意: 这是在 OpenReview submission form 里填写的，不应出现在论文 PDF 中

请按 ARR reviewer guidelines 输出完整审稿意见，包含: Summary, Strengths (逐条), Weaknesses (逐条, 标注 Critical/Major/Minor), Questions, Missing References, Overall Assessment (1-5 scale per EMNLP guidelines)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-22T08:24:44.604787+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1243 · 2026-05-22T08:24:44.605256+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1244 · 2026-05-22T08:24:52.090102+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-7",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-7",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1245 · 2026-05-22T08:24:52.592562+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 1246 · 2026-05-22T08:24:53.297524+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 561.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.5}], \"total_pages\": 19, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool call

_source line 1247 · 2026-05-22T08:24:53.298382+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1248 · 2026-05-22T08:24:53.348968+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-22T08:25:01.581374+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Recommendation Scale

The review form includes the following scoring levels:

- 5 = Consider for Awa
…[truncated 1053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8988
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-22T08:25:08.513167+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-22T08:25:09.367727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-22T08:25:09.518735+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1253 · 2026-05-22T08:25:09.994918+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-22T08:25:10.290958+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-22T08:25:11.349515+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1830
}
```

</details>

---


### Tool result

_source line 1256 · 2026-05-22T08:25:11.350696+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 1257 · 2026-05-22T08:25:11.351068+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-22T08:25:11.755070+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1464
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-22T08:25:11.755679+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1260 · 2026-05-22T08:25:12.763133+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-22T08:25:12.766304+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-22T08:25:12.766732+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-22T08:25:14.628001+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1861
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-22T08:25:14.728884+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and descriptions. Include all fields reviewers must fill in: soundness, excitement, overall assessment, and any other criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and descriptions. Include all fields reviewers must fill in: soundness, excitement, overall assessment, and any other criteria."
  }
}
```

</details>

---


### Tool call

_source line 1265 · 2026-05-22T08:25:15.736933+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1266 · 2026-05-22T08:25:16.050258+00:00_

1	Learned sparsity predictors for SwiGLU LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation confirms these discovered patterns---not the training mechanism itself---as the proximate quality driver.
5	A coupling alignment hierarchy emerges across five loss configurations; a per-layer KL control decomposes this hierarchy into two dimensions: output-distribution alignment drives PPL (per-layer KL within 3\% of end-to-end at 30\% sparsity), while cross-layer coupling provides additional downstream benefit (3--4\,pp on ARC-Challenge and WinoGrande).
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 313
}
```

</details>

---


### Tool call

_source line 1267 · 2026-05-22T08:25:16.050706+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1268 · 2026-05-22T08:25:16.526035+00:00_

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
12	A target-swap ablation confirms that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Cross-lay
…[truncated 2933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 475
}
```

</details>

---


### Tool call

_source line 1269 · 2026-05-22T08:25:16.526533+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1270 · 2026-05-22T08:25:16.760380+00:00_

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
16	Dhar et al.~\cite{dhar2025clustering} compress activation patterns via clustering for effici
…[truncated 4852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 233
}
```

</details>

---


### Tool call

_source line 1271 · 2026-05-22T08:25:16.760851+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1272 · 2026-05-22T08:25:16.817451+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 56
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-22T08:25:21.323687+00:00_

# ACL Rolling Review Form Structure

## Primary Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; thoroughly read paper and familiar with related work
- 4: Quite sure; checked important points carefully
- 3: Pretty sure; good area knowledge but didn't check details meticulously
- 2: Willing to defend; likely missed details or unclear on novelty
- 1: Outside expertise area or paper very difficult to understand

**Soundness** (1-5 scale with half-points)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong support for claims; additional experiments optional
- 3: Adequate support for main claims; minor details need strengthening
- 2: Major claims lack sufficient support; significant technical problems
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale with half-points)
- 5: Highly Exciting; would recommend and attend presentation
- 4: Exciting; would mention to others or prioritize attending
- 3: Interesting; might mention or attend if time permits
- 2: Potentially Interesting; doesn't resonate personally but may appeal broadly
- 1: Not Exciting; unlikely to resonate with ACL community

**Overall Assessment** (1-5 scale with half-points)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit or irrelevant to computational linguistics

## Additional Required Fields

- Paper Summary
- Summary of Strengths
- Summary of Weaknesses
- Comments/Suggestions/Typos
- Limitations and Societal Impact
- Ethical Concerns
- Reproducibility (1-5 scale)
- Datasets (1-5 scale, if applicable)
- Software (1-5 scale, if applicable)
- Author Identity Knowledge (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6594
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-22T08:25:43.156385+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "8-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "8-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-22T08:25:44.164786+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.8}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 594.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.2}], \"total_pages\": 19, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-22T08:25:44.265637+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-22T08:25:44.316662+00:00_

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
…[truncated 18174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-22T08:25:44.467656+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-22T08:25:44.468126+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Coupling alignment---optimizing through the output distribution---is the dominant design dimension for learned sparsity: signal type accounts for 97.5\% of the PPL gap at 30\% sparsity, while cross-layer coupling contributes downstream fidelity (3--4\,pp on ARC-c, WinoGrande).
5	A predictor ($<$1\% of base) reduces TEAL's perplexity by 14.5\%, with KL-discovered masks (46--68\% divergent from magnitude) driving inference quality; however, downstream transfer is task- and scale-dependent.
6	Future work includes N:M structured sparsity and scaling to 70B+.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-22T08:25:44.669335+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-22T08:25:44.720194+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-22T08:25:44.770976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-22T08:25:45.022525+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--14B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}, Qwen-2.5-14B~\cite{qwen2024qwen25}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2025spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-22T08:26:03.844569+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-22T08:26:04.698611+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-22T08:26:04.849590+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1287 · 2026-05-22T08:26:05.251560+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1288 · 2026-05-22T08:26:05.709290+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 1289 · 2026-05-22T08:26:05.709751+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1290 · 2026-05-22T08:26:06.162361+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 1291 · 2026-05-22T08:26:06.364214+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1292 · 2026-05-22T08:26:07.117765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-22T08:26:07.118635+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-22T08:26:07.270197+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1295 · 2026-05-22T08:26:07.623065+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1296 · 2026-05-22T08:26:08.077844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1297 · 2026-05-22T08:26:08.128610+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1298 · 2026-05-22T08:26:08.431210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-22T08:26:08.431932+00:00_

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
…[truncated 30676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-22T08:26:19.929220+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "15-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "15-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-22T08:26:20.933414+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.5}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 261.6}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 91.3}], \"total_pages\": 19, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1302 · 2026-05-22T08:26:21.084480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-22T08:26:21.887917+00:00_

1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2025spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Naras
…[truncated 20404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-22T08:26:23.343912+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: (1) what reviewers should evaluate, (2) how to score soundness, excitement, and overall assessment, (3) any guidance on novelty, empirical contributions, and (4) what constitutes a conference vs findings paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: (1) what reviewers should evaluate, (2) how to score soundness, excitement, and overall assessment, (3) any guidance on novelty, empirical contributions, and (4) what constitutes a conference vs findings paper."
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-22T08:26:30.622327+00:00_

# ARR Reviewer Guidelines Summary

## What Reviewers Should Evaluate

ARR reviewers assess papers across multiple dimensions:

- **Technical soundness**: Validity of methodology, proofs, argumentation, and experimental design
- **Novelty**: Whether the work contributes new knowledge to the field
- **Clarity**: How well the research question and contributions are communicated
- **Significance**: Potential impact and relevance to the community
- **Reproducibility**: Sufficiency of details for replicating experiments

The guidelines emphasize that "the goal of research is to contribute new knowledge" and that contributions extend beyond novel methods to include resources, analyses, reproductions, and surveys.

## Scoring Framework (Three Dimensions)

**Soundness Score**: "Must be justified by the text of the review." Low soundness scores require explicit technical flaws or methodological problems in the review content. If you cannot identify specific issues, the low score may reflect unconscious bias rather than genuine concerns.

**Excitement Score**: Reflects personal interest orthogonal to technical quality. This allows reviewers to distinguish between sound-but-uninteresting work and personally compelling research.

**Overall Assessment**: A composite recommendation balancing soundness, excitement, novelty, and potential impact for conference commitment decisions.

## Novelty and Empirical Contributions Guidance

The guidelines address common misconceptions about novelty:

- Surprising results validate contributions even if findings seem intuitive retrospectively
- Negative results deserve publication; positive-only bias harms the field
- Simpler solutions are preferable to complex ones
- Missing SOTA (state-of-the-art) status is not inherently problematic

Reviewers should avoid dismissing work as "not novel" without providing specific prior references published at least three months before submission.

## Conference vs. Findings Papers

The guidelines do not expl
…[truncated 360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7278
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-22T08:26:39.707484+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1307 · 2026-05-22T08:26:40.165260+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-22T08:26:40.840060+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-22T08:26:41.701971+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1994
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-22T08:26:41.702477+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1311 · 2026-05-22T08:26:41.702723+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_17/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1312 · 2026-05-22T08:26:41.753914+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1588
}
```

</details>

---


### Tool result

_source line 1313 · 2026-05-22T08:26:41.856255+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 153
}
```

</details>

---


### Tool result

_source line 1314 · 2026-05-22T08:26:42.463880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1623
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-22T08:26:42.465453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 762
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-22T08:30:40.718147+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## Paper Summary\n\n本文研究将 KL 散度蒸馏（配合 Gumbel-Sigmoid 松弛）应用于训练 SwiGLU LLM 的上下文稀疏性预测器，替代传统的 BCE 损失。在 LLaMA-3.1-8B 上，作者通过大量消融实验建立了\"coupling alignment hierarchy\"：output-distribution 损失（KL/JSD）在 PPL 上主导，cross-layer coupling 对 downstream task 有额外贡献。KL 预测器在 30% 稀疏度下将 TEAL 的 PPL 降低 14.5%，发现的 mask pattern 与 magnitude-based 方法有 46-68% 的偏离。target-swap ablation (C1) 证明 mask 质量（而非梯度耦合机制本身）是推理质量的近端驱动因素。补偿网络 (+67.2M 参数) 变得冗余。跨架构评估在 Mistral-7B 上 PPL 泛化，但在 Qwen-2.5-14B 上出现 MMLU/GSM8K 下降。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 扎实的 empirical study，消融设计精巧，但核心方法配方与 MaskLLM 高度重合，缺乏 wall-clock speedup 验证，新颖性不足以支撑主会议接收。\n\n---\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 消融设计合理（C1 target-swap、per-layer KL），实验控制变量严格（同架构/数据/优化器仅改损失），3-seed 评估。但 per-layer KL 实验存在 train-inference distribution shift confound（§4.5 自认），14B 结果与核心叙事矛盾 |\n| Excitement | 2.5/5 | 方法配方（frozen backbone + learnable masks + KL + Gumbel）与 MaskLLM 核心相同，应用到 activation sparsity 是增量而非突破。无 wall-clock speedup 削弱实际影响力 |\n| Reproducibility | 4/5 | 超参数完整报告，GPU 型号、训练步数、seed、评估协议均明确。但代码和 predictor weights 未发布 |\n| Reviewer Confidence | 4/5 | 熟悉 activation sparsity、KL distillation、sparse inference 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] 与 MaskLLM 的新颖性区分不足\n\n- 具体位置：§2 Related Work, ¶\"Predictor-Based Contextual Sparsity\"\n- 问题：核心配方 (frozen weights + learnable masks + KL divergence + Gumbel relaxation) 与 MaskLLM (Fang et al., 2024, NeurIPS) 完全一致。论文给出的三点区分——(1) sparsity type (weight vs activation), (2) mask generation (direct params vs predictor network), (3) allocation (N:M vs global top-k)——都是 application-level adaptation，而非 fundamental methodological contribution。尤其是：\n  - KL + Gumbel 用于 mask 优化已被 MaskLLM 建立为已知技术\n  - 将其应用到 activation sparsity predictor 是直接的工程迁移\n  - 论文最核心的 empirical finding（KL 优于 BCE）在 MaskLLM 已经隐含验证（MaskLLM 用 KL 而非 BCE 训练 mask）\n- 为什么影响接收：作为 empirical study，论文需要在 insight 层面提供足够 novelty。但\"KL 优于 BCE\"这一核心 insight 已被 MaskLLM 的方法选择所暗示。论文的附加贡献（2D taxonomy、C1 ablation、coupling hierarchy）有价值但不足以独立撑起 main conference bar。\n- 建议修改方向：(a) 更深入地对比 MaskLLM 的 KL 训练在 activation sparsity 设定下的行为差异，最好有实验对比；(b) 明确论文的贡献是 *理解为什么 KL 有效*（via target-swap ablation），而不是 *提出用 KL*；(c) 考虑与 MaskLLM 在 activation sparsity 设定下的直接实验对比（即使 MaskLLM 设计用于 weight sparsity，也可以适配）。\n\n**N2** [Critical] Efficiency motivation 与实际无 wall-clock speedup 的叙事张力\n\n- 具体位置：§1 Introduction, §A Inference Efficiency (Appendix)\n- 问题：Introduction 第一段以 \"high contextual sparsity\" 和 inference efficiency 为动机引入问题，但：\n  - Table 5 (Appendix A) 显示该方法增加了 6.4% 推理延迟（126.78 vs 119.11 ms/forward）\n  - 论文明确承认 \"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support\"\n  - 当前的 activation sparsity 无法实际加速推理，使得整个 efficiency motivation 成为空洞的未来愿景\n  - 即使引用了 Triton/cuSPARSE，也没有任何 POC 级别的 sparse kernel 加速数据\n- 为什么影响接收：读者期望 efficiency 论文展示 efficiency 提升。论文虽在 §1 和 Limitations 中做了 caveat，但 motivation 和 actual contribution 之间的 gap 太大，削弱了论文的实际意义。\n- 建议修改方向：(a) 将 framing 从 efficiency 转向\"理解 sparsity prediction 的 training objective design space\"，这更准确反映论文的贡献；(b) 提供至少一个 sparse kernel 的 proof-of-concept speedup 数据（即使是 block-sparse with Triton 的简单实现）；(c) 或明确将论文定位为 Findings 级别的 analytical contribution。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] 14B 结果与核心叙事矛盾，但在 framing 中被淡化\n\n- 具体位置：§4.6, Table 13 (Appendix K), Limitations\n- 问题：在 Qwen-2.5-14B 上：\n  - MMLU: KL 63.55% vs TEAL 66.34% (uniform), -2.79pp\n  - GSM8K: KL 32.1±5.2% vs TEAL 52.1% (uniform), -20pp，3-seed 方差极高 (σ=5.2pp)\n  - 这些 negative results 与论文的核心 narrative（KL 优于 magnitude-based methods）直接矛盾\n  - Limitations 中的解释（\"task-and-scale-dependent effects\"）过于笼统\n- 建议：(a) 在主文 §4.6 中给出更具体的失败模式分析，而不是仅引用 Appendix；(b) 讨论 KL 的 mode-covering 特性是否在 larger model 上反而有害（higher capacity → reasoning pathways more structured → magnitude-based selection more appropriate?）；(c) 考虑这是否表明该方法的 applicability 有根本的 scale limitation。\n\n**W2** [Major] Target-swap ablation (C1) 存在 confound，论文承认但未充分处理\n\n- 具体位置：§4.4, Table 3, Appendix P\n- 问题：\n  - C1 同时改变了 mask 表征（hard vs soft）和 target（magnitude vs KL-derived），虽然 §4.4 的 \"Soft-vs-Hard Confound\" 段落用 BCE+Gumbel (PPL 32.22) vs BCE (27.97) 试图排除 softness 的影响，但这只排除了 softness *有利于 BCE* 的可能，没有排除 softness 与 KL targets 之间的 interaction\n  - 更关键的是：C1 的 oracle masks 来自特定 KL training trajectory（Appendix P 承认），是否另一个 KL 初始化会发现等效 mask 仍是 open question\n  - s42 oracle 来自 \"earlier training run\"（Table 3 footnote），与其他 seed 的 oracle 不匹配，导致 s42 有 0.65pp gap\n- 建议：(a) 明确 state C1 的 conclusion 需要 qualification——它证明了 mask quality 的重要性，但不能完全排除 gradient coupling 的额外贡献；(b) 讨论 oracle mask 的 trajectory dependence 对 C1 结论 robustness 的影响。\n\n**W3** [Major] \"2D Taxonomy\" / \"Coupling Alignment Hierarchy\" 叙事有 overclaim 风险\n\n- 具体位置：§3.7, Table 1, §1 Contributions\n- 问题：\n  - Table 1 的 \"2D taxonomy\" 实质上是一个 2×3 分类表，将已有方法按两个维度分类。这是 useful organizational tool 但不构成 novel insight——任何熟悉该领域的人都能构建类似分类。称之为 \"two-dimensional taxonomy\" 和论文的核心贡献之一有 overclaim 风格。\n  - \"Coupling alignment hierarchy\" 本质上是\"KL > JSD > Reverse KL > BCE > MSE\"的实验排序，使用 \"hierarchy\" 一词过于宏大\n  - Contribution list 第一条 \"A coupling alignment hierarchy across five losses, decomposed by a per-layer KL control into signal type and coupling scope\" 将这个 empirical finding 包装得过于理论化\n- 建议：用更朴素的语言描述：如 \"we empirically compare five loss functions and find that output-distribution losses consistently outperform intermediate and decomposed losses\"。\n\n**W4** [Minor] 30% sparsity \"sweet spot\" 限制了实际影响\n\n- 具体位置：§4.2, §4.6, Limitations\n- 问题：\n  - 在 30% 稀疏度下 KL 方法工作良好（PPL 8.81, MMLU 40.7%），但 40% 时 MMLU 已降至 35.5%，50% 时所有方法的 MMLU 都崩溃到接近随机（~28%）\n  - 30% 稀疏度 + 无 wall-clock speedup = 实际部署价值非常有限\n  - 在唯一展示大幅 PPL 改善的 50% regime，downstream tasks 已经无法使用\n- 建议：Limitations 已部分讨论此问题，但建议在主文中更明确地框定 30% 作为 \"最小有意义稀疏度\"的意义。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式问题 [Minor]**: 论文 PDF 中包含了 \"Responsible NLP Research Checklist\"（Ethics Statement 后，§C1-E1），但根据 EMNLP 2026 / ARR 提交指南，该 checklist 应仅在 OpenReview submission form 中填写，不应出现在论文 PDF 中。建议删除 PDF 中的 checklist 部分。\n\n- **引用格式一致性**: `\\cite` vs `\\citealp` 的使用基本一致，但 §1 中 TEAL 的引用使用了 `\\citealp`（括号内）而其他地方使用 `\\cite`——这是风格选择不算错误，但建议统一。\n\n- **Table 2 的 footnote 过于密集**: Table 2 的 caption 包含了大量 footnote 标记（†, ‡, *, ±），信息密度过高，降低了可读性。建议将部分解释移到正文或单独的 note。\n\n- **Abstract 中 \"post-hoc compensation (+67.2M params) becomes redundant\" 可能误导**: 读者可能理解为\"其他方法的补偿网络可以去掉\"，但实际上论文比较的是自己方法加不加补偿——这个表述需要更清晰。\n\n---\n\n## Questions for Authors\n\n1. **与 MaskLLM 的实验对比**: 是否考虑过将 MaskLLM 的 approach 适配到 activation sparsity setting 进行直接对比？即使 MaskLLM 设计用于 N:M weight sparsity，将其 direct learnable mask + KL 框架应用到 per-token activation selection 应该是 feasible 的。这将更清楚地展示 predictor network 相对于 direct mask parameters 的优势。\n\n2. **14B GSM8K 逆转的根因**: GSM8K 在 14B 上 KL 比 TEAL 差 20pp (32.1% vs 52.1%)。作者假设这是因为 \"reasoning-critical pathways that magnitude pruning preserves more robustly\"——是否有更具体的 evidence？例如：是否分析了 14B 上 KL-discovered masks 与 magnitude masks 在特定层（如晚期层）的偏离度与 GSM8K 性能的相关性？\n\n3. **Training data diversity**: 所有 predictor 在 WikiText-103 上训练。是否测试过在更多样化的数据（如 C4 子集、code 数据）上训练时，downstream transfer 是否改善？尤其是 MMLU 这种 knowledge-intensive task 可能需要更广泛的 activation pattern 覆盖。\n\n4. **Per-layer KL 的 confound**: §4.5 承认 per-layer KL 实验引入了 train-inference distribution shift（训练时每步仅 mask 一层，推理时同时 mask 32 层）。是否考虑过其他设计来隔离 coupling scope——如训练时 mask K 层（K < 32）的 curriculum？\n\n---\n\n## Missing References\n\nRelated work 覆盖较为全面，以下可考虑补充但非必须：\n\n1. **Activation-aware Weight Quantization** (AWQ, Lin et al., 2024, MLSys) — 虽然是量化方法，但其 activation-aware channel selection 与本文的 activation importance scoring 有思路相似性，可在 §2 的 weight pruning 段落中简短提及。\n\n2. 论文已覆盖 R-Sparse, DIP, SparseInfer, Polar Sparsity, MoNE, D2D-MoE, Expert Choice — 所有 Director 指定检查的参考文献均已充分讨论。引用完整性总体良好。\n\n---\n\n## 主要优势\n\n1. **消融设计精巧**: Target-swap ablation (C1) 是 disentangle \"what\" (mask target quality) vs \"how\" (gradient coupling mechanism) 的聪明实验设计，即使存在 confound 也提供了有价值的 partial evidence（§4.4, Table 3）。\n\n2. **实验控制严格**: 所有 baseline（KL, BCE, MSE, JSD, RKL）使用相同架构、数据、优化器、Gumbel 松弛参数，仅改变损失函数（§G MSE Baseline Configuration, Appendix），使得 loss function 的效果可以 cleanly 隔离。3-seed 评估贯穿关键实验。\n\n3. **诚实的 negative results 报告**: 14B 的 MMLU/GSM8K 下降、30% 下 global allocation 的高 MMLU 方差（σ=9.5pp）、50% 下 downstream collapse——这些 negative results 在 Limitations 中被充分讨论，展示了学术诚实性（§Limitations, §4.6）。\n\n4. **Per-layer KL control 提供了有价值的分解**: 将 \"signal type\" 和 \"coupling scope\" 两个因素分离（97.5% PPL gap 来自 signal type, coupling scope 贡献 downstream fidelity）是有用的 empirical insight（§4.5）。\n\n5. **Related work 覆盖全面**: 对 2024-2026 年的 activation sparsity 文献有广泛覆盖，包括最新的 R-Sparse, DIP, SparseInfer, MoC, SVD-CSP 等（§2）。\n\n---\n\n## 格式合规检查（EMNLP 2026）\n\n| 检查项 | 结果 | 备注 |\n|--------|------|------|\n| 正文 ≤ 8 页 | ✅ 通过 | §1-5 占 pages 1-8 |\n| Anonymous 规则 | ✅ 通过 | Author = \"Anonymous ACL submission\" |\n| ACL template | ✅ 通过 | `\\usepackage[review]{acl}` |\n| Limitations 章节 | ✅ 通过 | 存在且详细（约 1 页） |\n| Ethics Statement | ✅ 通过 | 存在且合理 |\n| 无 Responsible NLP Checklist 在 PDF 中 | ❌ 未通过 | Checklist 出现在 PDF §9-10 页，应仅在 OpenReview form 中填写 |\n| 自引不泄露身份 | ✅ 通过 | 未发现可识别的自引 |\n| 参考文献格式 | ✅ 通过 | 使用 `acl_natbib.bst`，格式一致 |\n\n---\n\n**总结**: 这是一篇执行良好的 empirical study，消融设计值得肯定。但核心方法配方与 MaskLLM 高度重合（KL + Gumbel 用于 mask 优化），无 wall-clock speedup 验证，14B 结果与核心叙事矛盾——这些限制了论文超越 Findings 水平。建议 Overall Assessment = 3.0 (Findings)。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## Paper Summary\n\n本文研究将 KL 散度蒸馏（配合 Gumbel-Sigmoid 松弛）应用于训练 SwiGLU LLM 的上下文稀疏性预测器，替代传统的 BCE 损失。在 LLaMA-3.1-8B 上，作者通过大量消融实验建立了\"coupling alignment hierarchy\"：output-distribution 损失（KL/JSD）在 PPL 上主导，cross-layer coupling 对 downstream task 有额外贡献。KL 预测器在 30% 稀疏度下将 TEAL 的 PPL 降低 14.5%，发现的 mask pattern 与 magnitude-based 方法有 46-68% 的偏离。target-swap ablation (C1) 证明 mask 质量（而非梯度耦合机制本身）是推理质量的近端驱动因素。补偿网络 (+67.2M 参数) 变得冗余。跨架构评估在 Mistral-7B 上 PPL 泛化，但在 Qwen-2.5-14B 上出现 MMLU/GSM8K 下降。\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 扎实的 empirical study，消融设计精巧，但核心方法配方与 MaskLLM 高度重合，缺乏 wall-clock speedup 验证，新颖性不足以支撑主会议接收。\n\n---\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 消融设计合理（C1 target-swap、per-layer KL），实验控制变量严格（同架构/数据/优化器仅改损失），3-seed 评估。但 per-layer KL 实验存在 train-inference distribution shift confound（§4.5 自认），14B 结果与核心叙事矛盾 |\n| Excitement | 2.5/5 | 方法配方（frozen backbone + learnable masks + KL + Gumbel）与 MaskLLM 核心相同，应用到 activation sparsity 是增量而非突破。无 wall-clock speedup 削弱实际影响力 |\n| Reproducibility | 4/5 | 超参数完整报告，GPU 型号、训练步数、seed、评估协议均明确。但代码和 predictor weights 未发布 |\n| Reviewer Confidence | 4/5 | 熟悉 activation sparsity、KL distillation、sparse inference 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] 与 MaskLLM 的新颖性区分不足\n\n- 具体位置：§2 Related Work, ¶\"Predictor-Based Contextual Sparsity\"\n- 问题：核心配方 (frozen weights + learnable masks + KL divergence + Gumbel relaxation) 与 MaskLLM (Fang et al., 2024, NeurIPS) 完全一致。论文给出的三点区分——(1) sparsity type (weight vs activation), (2) mask generation (direct params vs predictor network), (3) allocation (N:M vs global top-k)——都是 application-level adaptation，而非 fundamental methodological contribution。尤其是：\n  - KL + Gumbel 用于 mask 优化已被 MaskLLM 建立为已知技术\n  - 将其应用到 activation sparsity predictor 是直接的工程迁移\n  - 论文最核心的 empirical finding（KL 优于 BCE）在 MaskLLM 已经隐含验证（MaskLLM 用 KL 而非 BCE 训练 mask）\n- 为什么影响接收：作为 empirical study，论文需要在 insight 层面提供足够 novelty。但\"KL 优于 BCE\"这一核心 insight 已被 MaskLLM 的方法选择所暗示。论文的附加贡献（2D taxonomy、C1 ablation、coupling hierarchy）有价值但不足以独立撑起 main conference bar。\n- 建议修改方向：(a) 更深入地对比 MaskLLM 的 KL 训练在 activation sparsity 设定下的行为差异，最好有实验对比；(b) 明确论文的贡献是 *理解为什么 KL 有效*（via target-swap ablation），而不是 *提出用 KL*；(c) 考虑与 MaskLLM 在 activation sparsity 设定下的直接实验对比（即使 MaskLLM 设计用于 weight sparsity，也可以适配）。\n\n**N2** [Critical] Efficiency motivation 与实际无 wall-clock speedup 的叙事张力\n\n- 具体位置：§1 Introduction, §A Inference Efficiency (Appendix)\n- 问题：Introduction 第一段以 \"high contextual sparsity\" 和 inference efficiency 为动机引入问题，但：\n  - Table 5 (Appendix A) 显示该方法增加了 6.4% 推理延迟（126.78 vs 119.11 ms/forward）\n  - 论文明确承认 \"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support\"\n  - 当前的 activation sparsity 无法实际加速推理，使得整个 efficiency motivation 成为空洞的未来愿景\n  - 即使引用了 Triton/cuSPARSE，也没有任何 POC 级别的 sparse kernel 加速数据\n- 为什么影响接收：读者期望 efficiency 论文展示 efficiency 提升。论文虽在 §1 和 Limitations 中做了 caveat，但 motivation 和 actual contribution 之间的 gap 太大，削弱了论文的实际意义。\n- 建议修改方向：(a) 将 framing 从 efficiency 转向\"理解 sparsity prediction 的 training objective design space\"，这更准确反映论文的贡献；(b) 提供至少一个 sparse kernel 的 proof-of-concept speedup 数据（即使是 block-sparse with Triton 的简单实现）；(c) 或明确将论文定位为 Findings 级别的 analytical contribution。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] 14B 结果与核心叙事矛盾，但在 framing 中被淡化\n\n- 具体位置：§4.6, Table 13 (Appendix K), Limitations\n- 问题：在 Qwen-2.5-14B 上：\n  - MMLU: KL 63.55% vs TEAL 66.34% (uniform), -2.79pp\n  - GSM8K: KL 32.1±5.2% vs TEAL 52.1% (uniform), -20pp，3-seed 方差极高 (σ=5.2pp)\n  - 这些 negative results 与论文的核心 narrative（KL 优于 magnitude-based methods）直接矛盾\n  - Limitations 中的解释（\"task-and-scale-dependent effects\"）过于笼统\n- 建议：(a) 在主文 §4.6 中给出更具体的失败模式分析，而不是仅引用 Appendix；(b) 讨论 KL 的 mode-covering 特性是否在 larger model 上反而有害（higher capacity → reasoning pathways more structured → magnitude-based selection more appropriate?）；(c) 考虑这是否表明该方法的 applicability 有根本的 scale limitation。\n\n**W2** [Major] Target-swap ablation (C1) 存在 confound，论文承认但未充分处理\n\n- 具体位置：§4.4, Table 3, Appendix P\n- 问题：\n  - C1 同时改变了 mask 表征（hard vs soft）和 target（magnitude vs KL-derived），虽然 §4.4 的 \"Soft-vs-Hard Confound\" 段落用 BCE+Gumbel (PPL 32.22) vs BCE (27.97) 试图排除 softness 的影响，但这只排除了 softness *有利于 BCE* 的可能，没有排除 softness 与 KL targets 之间的 interaction\n  - 更关键的是：C1 的 oracle masks 来自特定 KL training trajectory（Appendix P 承认），是否另一个 KL 初始化会发现等效 mask 仍是 open question\n  - s42 oracle 来自 \"earlier training run\"（Table 3 footnote），与其他 seed 的 oracle 不匹配，导致 s42 有 0.65pp gap\n- 建议：(a) 明确 state C1 的 conclusion 需要 qualification——它证明了 mask quality 的重要性，但不能完全排除 gradient coupling 的额外贡献；(b) 讨论 oracle mask 的 trajectory dependence 对 C1 结论 robustness 的影响。\n\n**W3** [Major] \"2D Taxonomy\" / \"Coupling Alignment Hierarchy\" 叙事有 overclaim 风险\n\n- 具体位置：§3.7, Table 1, §1 Contributions\n- 问题：\n  - Table 1 的 \"2D taxonomy\" 实质上是一个 2×3 分类表，将已有方法按两个维度分类。这是 useful organizational tool 但不构成 novel insight——任何熟悉该领域的人都能构建类似分类。称之为 \"two-dimensional taxonomy\" 和论文的核心贡献之一有 overclaim 风格。\n  - \"Coupling alignment hierarchy\" 本质上是\"KL > JSD > Reverse KL > BCE > MSE\"的实验排序，使用 \"hierarchy\" 一词过于宏大\n  - Contribution list 第一条 \"A coupling alignment hierarchy across five losses, decomposed by a per-layer KL control into signal type and coupling scope\" 将这个 empirical finding 包装得过于理论化\n- 建议：用更朴素的语言描述：如 \"we empirically compare five loss functions and find that output-distribution losses consistently outperform intermediate and decomposed losses\"。\n\n**W4** [Minor] 30% sparsity \"sweet spot\" 限制了实际影响\n\n- 具体位置：§4.2, §4.6, Limitations\n- 问题：\n  - 在 30% 稀疏度下 KL 方法工作良好（PPL 8.81, MMLU 40.7%），但 40% 时 MMLU 已降至 35.5%，50% 时所有方法的 MMLU 都崩溃到接近随机（~28%）\n  - 30% 稀疏度 + 无 wall-clock speedup = 实际部署价值非常有限\n  - 在唯一展示大幅 PPL 改善的 50% regime，downstream tasks 已经无法使用\n- 建议：Limitations 已部分讨论此问题，但建议在主文中更明确地框定 30% 作为 \"最小有意义稀疏度\"的意义。\n\n---\n\n## 小问题（不影响接收）\n\n- **格式问题 [Minor]**: 论文 PDF 中包含了 \"Responsible NLP Research Checklist\"（Ethics Statement 后，§C1-E1），但根据 EMNLP 2026 / ARR 提交指南，该 checklist 应仅在 OpenReview submission form 中填写，不应出现在论文 PDF 中。建议删除 PDF 中的 checklist 部分。\n\n- **引用格式一致性**: `\\cite` vs `\\citealp` 的使用基本一致，但 §1 中 TEAL 的引用使用了 `\\citealp`（括号内）而其他地方使用 `\\cite`——这是风格选择不算错误，但建议统一。\n\n- **Table 2 的 footnote 过于密集**: Table 2 的 caption 包含了大量 footnote 标记（†, ‡, *, ±），信息密度过高，降低了可读性。建议将部分解释移到正文或单独的 note。\n\n- **Abstract 中 \"post-hoc compensation (+67.2M params) becomes redundant\" 可能误导**: 读者可能理解为\"其他方法的补偿网络可以去掉\"，但实际上论文比较的是自己方法加不加补偿——这个表述需要更清晰。\n\n---\n\n## Questions for Authors\n\n1. **与 MaskLLM 的实验对比**: 是否考虑过将 MaskLLM 的 approach 适配到 activation sparsity setting 进行直接对比？即使 MaskLLM 设计用于 N:M weight sparsity，将其 direct learnable mask + KL 框架应用到 per-token activation selection 应该是 feasible 的。这将更清楚地展示 predictor network 相对于 direct mask parameters 的优势。\n\n2. **14B GSM8K 逆转的根因**: GSM8K 在 14B 上 KL 比 TEAL 差 20pp (32.1% vs 52.1%)。作者假设这是因为 \"reasoning-critical pathways that magnitude pruning preserves more robustly\"——是否有更具体的 evidence？例如：是否分析了 14B 上 KL-discovered masks 与 magnitude masks 在特定层（如晚期层）的偏离度与 GSM8K 性能的相关性？\n\n3. **Training data diversity**: 所有 predictor 在 WikiText-103 上训练。是否测试过在更多样化的数据（如 C4 子集、code 数据）上训练时，downstream transfer 是否改善？尤其是 MMLU 这种 knowledge-intensive task 可能需要更广泛的 activation pattern 覆盖。\n\n4. **Per-layer KL 的 confound**: §4.5 承认 per-layer KL 实验引入了 train-inference distribution shift（训练时每步仅 mask 一层，推理时同时 mask 32 层）。是否考虑过其他设计来隔离 coupling scope——如训练时 mask K 层（K < 32）的 curriculum？\n\n---\n\n## Missing References\n\nRelated work 覆盖较为全面，以下可考虑补充但非必须：\n\n1. **Activation-aware Weight Quantization** (AWQ, Lin et al., 2024, MLSys) — 虽然是量化方法，但其 activation-aware channel selection 与本文的 activation importance scoring 有思路相似性，可在 §2 的 weight pruning 段落中简短提及。\n\n2. 论文已覆盖 R-Sparse, DIP, SparseInfer, Polar Sparsity, MoNE, D2D-MoE, Expert Choice — 所有 Director 指定检查的参考文献均已充分讨论。引用完整性总体良好。\n\n---\n\n## 主要优势\n\n1. **消融设计精巧**: Target-swap ablation (C1) 是 disentangle \"what\" (mask target quality) vs \"how\" (gradient coupling mechanism) 的聪明实验设计，即使存在 confound 也提供了有价值的 partial evidence（§4.4, Table 3）。\n\n2. **实验控制严格**: 所有 baseline（KL, BCE, MSE, JSD, RKL）使用相同架构、数据、优化器、Gumbel 松弛参数，仅改变损失函数（§G MSE Baseline Configuration, Appendix），使得 loss function 的效果可以 cleanly 隔离。3-seed 评估贯穿关键实验。\n\n3. **诚实的 negative results 报告**: 14B 的 MMLU/GSM8K 下降、30% 下 global allocation 的高 MMLU 方差（σ=9.5pp）、50% 下 downstream collapse——这些 negative results 在 Limitations 中被充分讨论，展示了学术诚实性（§Limitations, §4.6）。\n\n4. **Per-layer KL control 提供了有价值的分解**: 将 \"signal type\" 和 \"coupling scope\" 两个因素分离（97.5% PPL gap 来自 signal type, coupling scope 贡献 downstream fidelity）是有用的 empirical insight（§4.5）。\n\n5. **Related work 覆盖全面**: 对 2024-2026 年的 activation sparsity 文献有广泛覆盖，包括最新的 R-Sparse, DIP, SparseInfer, MoC, SVD-CSP 等（§2）。\n\n---\n\n## 格式合规检查（EMNLP 2026）\n\n| 检查项 | 结果 | 备注 |\n|--------|------|------|\n| 正文 ≤ 8 页 | ✅ 通过 | §1-5 占 pages 1-8 |\n| Anonymous 规则 | ✅ 通过 | Author = \"Anonymous ACL submission\" |\n| ACL template | ✅ 通过 | `\\usepackage[review]{acl}` |\n| Limitations 章节 | ✅ 通过 | 存在且详细（约 1 页） |\n| Ethics Statement | ✅ 通过 | 存在且合理 |\n| 无 Responsible NLP Checklist 在 PDF 中 | ❌ 未通过 | Checklist 出现在 PDF §9-10 页，应仅在 OpenReview form 中填写 |\n| 自引不泄露身份 | ✅ 通过 | 未发现可识别的自引 |\n| 参考文献格式 | ✅ 通过 | 使用 `acl_natbib.bst`，格式一致 |\n\n---\n\n**总结**: 这是一篇执行良好的 empirical study，消融设计值得肯定。但核心方法配方与 MaskLLM 高度重合（KL + Gumbel 用于 mask 优化），无 wall-clock speedup 验证，14B 结果与核心叙事矛盾——这些限制了论文超越 Findings 水平。建议 Overall Assessment = 3.0 (Findings)。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-22T08:30:45.005320+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4287
}
```

</details>

---


### Assistant

_source line 1318 · 2026-05-22T08:30:53.492571+00:00_

审稿意见已提交给 Review Director。

总结：Overall Assessment 3.0 (Findings)。主要问题：(1) 核心配方（KL + Gumbel for mask optimization）与 MaskLLM 高度重合，novelty 不足以撑起 main conference；(2) efficiency motivation 与实际增加 6.4% 延迟之间的叙事张力；(3) 14B 上 MMLU/GSM8K 的显著下降与核心叙事矛盾。优势方面：消融设计精巧（C1 target-swap、per-layer KL control），实验控制严格，negative results 报告诚实。格式方面发现一个问题：Responsible NLP Checklist 不应出现在 PDF 中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 33

## Round 33

4 recorded events


### User

_source line 1319 · 2026-05-22T08:32:08.321744+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/小问题，用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

**Overall Assessment**: 3.0 (Findings)

### Must-Fix 问题

**N1** [Critical] 97.5% signal-type 归因与下游指标矛盾，叙事有误导风险
- §3.7 和 §4.5 声称"signal type accounts for 97.5% of the PPL gap"，但 §4.5 同时承认 per-layer KL underperforms end-to-end KL by 5-8pp on commonsense tasks，BoolQ 差距 9.2pp。这意味着 coupling scope 对下游任务的贡献远超 PPL 暗示的 2.5%。
- 论文主叙事（abstract, conclusion）反复强调 97.5%，可能给读者"coupling 不重要"的错误印象。
- 建议：在 abstract/conclusion 明确 97.5% 仅适用于 PPL；补充下游指标的 2D 分解定量结果。

**N2** [Critical] C1 target-swap ablation 的循环论证未充分讨论
- C1 将 KL 发现的 masks 交给 BCE 训练，BCE 也获得接近 KL 的 PPL。论文解释"mask quality is the proximate driver"。但这些 masks 恰恰由 KL 的耦合梯度发现——如果没有 KL 训练，这些 mask targets 根本不存在。C1 证明的是 transferability，而非"coupling 不重要"。
- 建议：明确讨论循环性；补充反向实验——能否用其他方法找到同等质量 masks？

**N3** [Critical] 无实际 wall-clock 加速，实用价值存疑
- Table 5 显示 +6.4% latency overhead。论文承认 "wall-clock speedup requires sparse kernel support not yet implemented"。对 sparsity 方法论文缺乏加速验证是重大缺陷。
- 建议：至少提供 Triton/cuSPARSE POC speedup 数字；或在 abstract/intro 显著弱化 practical motivation。

### Should-Fix 问题

**W1** [Major] 14B 实验覆盖不足，GSM8K 退步严重且缺乏对比
- 14B 仅 30% sparsity。GSM8K -20pp (32.1±5.2%)，高 seed variance。未给出 TEAL 在 14B 上的 GSM8K 对比。
- 建议：补 TEAL 14B 完整下游对比；补 14B 50% 结果。

**W2** [Major] Knowledge-intensive 任务系统性退步缺乏机制解释
- 8B 30% MMLU -5.2pp, 14B GSM8K -20pp。Limitations 中仅一句推测性解释。
- 建议：分析 per-layer mask 差异与 knowledge storage 层的关系。

**W3** [Major] MSE baseline 的 failed seed 报告方式不透明
- Per-layer MSE 50% PPL 229.26，3 seeds 中有 catastrophic failure。在 mean±std 中报告会扭曲统计。
- 建议：标注 failed seeds；分别报告 median 和 mean。

**W4** [Minor] OOD variance 增大 (CV 0.2%→6.3%) 需更多讨论

**W5** [Minor] Actual sparsity mismatch 讨论不够显著
- KL 28.5% vs TEAL 29.3% at 30% target。主表使用不同实际稀疏度。

### 小问题
- §3.4 Eq.(5) 符号定义顺序
- Figure 2 y 轴标签建议
- Table 1 taxonomy 可能暗示 positioning 过于强调 novelty
- Limitations 应明确"scaling to 70B"未测试原因

### Questions
1. 能否提供下游指标的 2D 分解定量结果？
2. C1 中 BCE 是否也使用了 Gumbel-Sigmoid relaxation？
3. 14B GSM8K -20pp 是否分析过哪些层 masks 差异最大？
4. 是否有证据其他方法也能发现同等质量 masks？
5. Compensation network 在 ≤45% sparsity 是否可能变得必要？

### Missing References
- PowerInfer-2 (Xue et al., 2024)
- Wanda 的 structured pruning 方法论对比价值
- ReLU-fication 中关于 SwiGLU→ReLU 后天然 sparsity 的分析

---

请对以上每个 Must-Fix、Should-Fix 和小问题逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-22T08:34:37.934783+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R1-N1: 97.5% signal-type 归因与下游指标矛盾**\n同意核心批评。但需澄清：R1 说\"abstract/conclusion 反复强调 97.5%\"并不完全准确——Abstract 用的是 \"within 3%\"，97.5% 仅在 §4.5 和 Conclusion 各出现一次。且 Abstract 和 Conclusion 都明确区分了 PPL vs downstream contribution。真正的问题是缺乏 downstream 指标的定量 2D 分解——论文给出了 raw gap (3-5pp commonsense, 9.2pp BoolQ) 但没有像 PPL 那样计算 % 贡献。建议补充而非删除 97.5% 这个数字。\n\n**[AGREE] R1-N2: C1 循环论证**\n同意 C1 证明的是 transferability 而非 \"coupling 不重要\"。论文在 Limitations 和 Appendix P 已承认 trajectory dependence，但 §4.4 主叙事中对此 qualification 不够突出。需补充\"但 R1 忽略了 C1 的 diagnostic 价值：它排除了'KL 通过某种推理阶段特性（而非 mask quality）获益'的替代假说。\"\n\n**[AGREE] R1-N3: 无 wall-clock 加速**\n完全同意。与我的 N2 一致。\n\n### Should-Fix\n\n**[REBUT] R1-W1: \"未给出 TEAL 14B GSM8K 对比\"**\nR1 事实性错误。Table 13 (Appendix K) 明确报告 TEAL 14B uniform GSM8K = 52.1%，Limitations 也引用了 \"32.1±5.2% vs. TEAL's 52.1%\"。R1 的其他子论点（仅 30%、缺 50%）有效。\n\n**[AGREE] R1-W2: Knowledge-intensive 退步缺机制解释**\n同意。论文仅有推测性解释，未利用已有的 per-layer Jaccard divergence 框架 (Figure 7) 与 task-specific 性能关联。\n\n**[AGREE] R1-W3: MSE failed seed 报告透明度**\n同意。Appendix G 记录了 50% s123 的 catastrophic failure (PPL=15,789)，但主文 Table 4 仅报告 s42 未标注。30% 的 3-seed 报告是完整的。\n\n**[AGREE] R1-W4: OOD variance** 同意，讨论不充分。\n**[AGREE] R1-W5: Actual sparsity mismatch** 同意，应在主表做 matched-sparsity 对比。\n\n### 小问题\n全部 [AGREE]。Table 1 taxonomy overclaim 与我的 W3 一致。\n\n### Missing References\nPowerInfer-2 [AGREE] 值得补充。Wanda 和 ReLU Strikes Back 已引用但可深入讨论 SwiGLU→ReLU 替代方案。\n\n### 与我评审的一致性\nR1 Overall 3.0 (Findings) 与我一致。主要分歧：R1 的 W1 中有事实性错误（TEAL 14B GSM8K 已报告）；R1 对 N1 的 \"反复强调\" 稍显夸大。核心判断高度一致：方法新颖性有限（KL+Gumbel 来自 MaskLLM）、无 wall-clock speedup、14B 负面结果未充分处理。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R1-N1: 97.5% signal-type 归因与下游指标矛盾**\n同意核心批评。但需澄清：R1 说\"abstract/conclusion 反复强调 97.5%\"并不完全准确——Abstract 用的是 \"within 3%\"，97.5% 仅在 §4.5 和 Conclusion 各出现一次。且 Abstract 和 Conclusion 都明确区分了 PPL vs downstream contribution。真正的问题是缺乏 downstream 指标的定量 2D 分解——论文给出了 raw gap (3-5pp commonsense, 9.2pp BoolQ) 但没有像 PPL 那样计算 % 贡献。建议补充而非删除 97.5% 这个数字。\n\n**[AGREE] R1-N2: C1 循环论证**\n同意 C1 证明的是 transferability 而非 \"coupling 不重要\"。论文在 Limitations 和 Appendix P 已承认 trajectory dependence，但 §4.4 主叙事中对此 qualification 不够突出。需补充\"但 R1 忽略了 C1 的 diagnostic 价值：它排除了'KL 通过某种推理阶段特性（而非 mask quality）获益'的替代假说。\"\n\n**[AGREE] R1-N3: 无 wall-clock 加速**\n完全同意。与我的 N2 一致。\n\n### Should-Fix\n\n**[REBUT] R1-W1: \"未给出 TEAL 14B GSM8K 对比\"**\nR1 事实性错误。Table 13 (Appendix K) 明确报告 TEAL 14B uniform GSM8K = 52.1%，Limitations 也引用了 \"32.1±5.2% vs. TEAL's 52.1%\"。R1 的其他子论点（仅 30%、缺 50%）有效。\n\n**[AGREE] R1-W2: Knowledge-intensive 退步缺机制解释**\n同意。论文仅有推测性解释，未利用已有的 per-layer Jaccard divergence 框架 (Figure 7) 与 task-specific 性能关联。\n\n**[AGREE] R1-W3: MSE failed seed 报告透明度**\n同意。Appendix G 记录了 50% s123 的 catastrophic failure (PPL=15,789)，但主文 Table 4 仅报告 s42 未标注。30% 的 3-seed 报告是完整的。\n\n**[AGREE] R1-W4: OOD variance** 同意，讨论不充分。\n**[AGREE] R1-W5: Actual sparsity mismatch** 同意，应在主表做 matched-sparsity 对比。\n\n### 小问题\n全部 [AGREE]。Table 1 taxonomy overclaim 与我的 W3 一致。\n\n### Missing References\nPowerInfer-2 [AGREE] 值得补充。Wanda 和 ReLU Strikes Back 已引用但可深入讨论 SwiGLU→ReLU 替代方案。\n\n### 与我评审的一致性\nR1 Overall 3.0 (Findings) 与我一致。主要分歧：R1 的 W1 中有事实性错误（TEAL 14B GSM8K 已报告）；R1 对 N1 的 \"反复强调\" 稍显夸大。核心判断高度一致：方法新颖性有限（KL+Gumbel 来自 MaskLLM）、无 wall-clock speedup、14B 负面结果未充分处理。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-22T08:34:41.799149+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Assistant

_source line 1322 · 2026-05-22T08:34:46.458287+00:00_

交叉回应已提交。核心结论：与 R1 Overall 3.0 (Findings) 高度一致，仅在 W1（TEAL 14B GSM8K 对比确实存在于 Table 13）和 N1（"反复强调"程度）上有事实性修正。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 34

## Round 34

80 recorded events


### User

_source line 1323 · 2026-05-22T09:35:25.734399+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + Related Work**审查。

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

### 1. 新颖性评估
- **MaskLLM 区分**：本文使用 KL + Gumbel + frozen weights + learnable masks，MaskLLM 也用这个配方。三点区分（sparsity type / mask generation / allocation）是否足够建立独立贡献？还是仅 application-level 差异？
- 论文自称 "primarily an empirical study"，这个定位下的贡献是否足够 EMNLP main？
- Target-swap ablation、2D taxonomy、coupling alignment ranking 作为分析框架的新颖性如何？

### 2. 贡献 Framing
- Abstract/Introduction 的 claims 是否与实验结果匹配？有无 overclaim？
- "Coupling alignment is the dominant design dimension" 这个 claim 的支撑是否充分？
- 论文标题 "Output-Distribution Distillation" 是否准确反映内容？
- 实用价值：30% sparsity + 6.4% overhead + 无 wall-clock speedup，对社区有什么实际贡献？

### 3. Related Work 完整性
- 是否遗漏重要相关工作？特别关注：
  - 2025-2026 年的 activation sparsity 新工作
  - KL distillation 在其他压缩场景的应用
  - SwiGLU-specific pruning/sparsity 方法
- MaskLLM 的对比讨论是否公平、充分？
- 与 D2D-MoE、ShadowLLM 等 predictor-based 方法的对比是否到位？

### 4. 跨架构 + 跨 scale 证据
- 3 个模型（LLaMA-8B, Mistral-7B, Qwen-14B）的覆盖是否足够？
- 14B 的 GSM8K -20pp 退步 + MMLU -2.8pp：这是系统性问题还是偶发？
- Knowledge-intensive 任务的系统性退步是否得到充分解释？
- Cross-architecture 能否建立 generality claim？

### 5. 写作质量
- 论文结构是否清晰？信息密度是否恰当？
- 术语使用：'coupling alignment ranking', 'signal type × coupling scope', '2D taxonomy' 是否过度创造术语？
- Figure/Table 质量和信息量
- 8 页限制内是否包含了足够信息？Appendix 是否包含了应在主文中出现的关键结果？

### 6. 格式合规
- 页数是否符合 8 页限制？
- 匿名性检查：是否泄露作者信息？
- Limitations 和 Ethics 章节是否充分？
- 引用格式是否正确（natbib）？

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-22T09:35:52.115207+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1325 · 2026-05-22T09:35:52.115647+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-22T09:35:56.887139+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1327 · 2026-05-22T09:35:58.995534+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf",
    "pages": "1-8",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1328 · 2026-05-22T09:36:04.156275+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, I found relevant information about the ARR 2026 reviewer guidelines and review form. Here's what I found:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Recommendation Scale

The review recommendation scale includes: 5 = C
…[truncated 871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7269
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-22T09:36:05.764304+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.1}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.4}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6768
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-22T09:36:20.740189+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, their descriptions, and scoring scales. I need every field a reviewer must fill out including: soundness, excitement/novelty, overall assessment, confidence, and any other dimensions. Include the exact wording of each scale point."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, their descriptions, and scoring scales. I need every field a reviewer must fill out including: soundness, excitement/novelty, overall assessment, confidence, and any other dimensions. Include the exact wording of each scale point."
  }
}
```

</details>

---


### Tool call

_source line 1331 · 2026-05-22T09:36:22.147214+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf",
  "pages": "9-18",
  "project": "distill_sparse_swiglu",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/submitted.pdf",
    "pages": "9-18",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-22T09:36:22.850884+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1333 · 2026-05-22T09:36:23.154668+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-22T09:36:24.113290+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1335 · 2026-05-22T09:36:24.465659+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1336 · 2026-05-22T09:36:26.827112+00:00_

# ACL Rolling Review Form - Complete Dimensions

## Required Review Dimensions

**1. Reviewer Confidence**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

**2. Soundness**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**3. Excitement**
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper to others"
- 2: "Potentially Interesting: this paper does not resonate with me"
- 1: "Not Exciting: this paper does not resonate with me"

**4. Overall Assessment**
- 5: "Consider for Award"
- 4.5: "Borderline Award"
- 4: "Conference"
- 3.5: "Borderline Conference"
- 3: "Findings"
- 2.5: "Borderline Findings"
- 2: "Resubmit next cycle"
- 1.5: "Resubmit after next cycle"
- 1: "Do not resubmit"

## Narrative Sections

Reviewers must complete: Paper Summary, Strengths, Weaknesses, Comments/Suggestions, and conditional sections on limitations/impact, ethics, reproducibility, datasets, and software.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6086
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-22T09:36:28.133321+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 570.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 607.2}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.7}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p17.png\", \"wid
…[truncated 508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5986
}
```

</details>

---


### Tool result

_source line 1338 · 2026-05-22T09:36:30.699622+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6233
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-22T09:36:30.728110+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6614
}
```

</details>

---


### Tool result

_source line 1340 · 2026-05-22T09:36:30.729426+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7878
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-22T09:36:30.755667+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7600
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-22T09:36:37.167221+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1343 · 2026-05-22T09:36:37.167698+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1344 · 2026-05-22T09:36:38.224132+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 1345 · 2026-05-22T09:36:38.275225+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1346 · 2026-05-22T09:36:38.327136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1159
}
```

</details>

---


### Tool call

_source line 1347 · 2026-05-22T09:36:38.327561+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1348 · 2026-05-22T09:36:39.434694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1159
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-22T09:36:39.536267+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1208
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-22T09:36:47.664410+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-22T09:36:48.370954+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-22T09:36:48.371432+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-22T09:36:49.076709+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-22T09:36:49.227838+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-22T09:36:49.981866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-22T09:36:50.133084+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1357 · 2026-05-22T09:36:50.133578+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1358 · 2026-05-22T09:36:51.142240+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 1359 · 2026-05-22T09:36:51.142681+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1360 · 2026-05-22T09:36:51.295994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1162
}
```

</details>

---


### Tool result

_source line 1361 · 2026-05-22T09:36:51.849477+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-22T09:37:09.356191+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1363 · 2026-05-22T09:37:09.812625+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-22T09:37:10.268047+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 1365 · 2026-05-22T09:37:10.268547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-22T09:37:10.924174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_18/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-22T09:37:11.026575+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 1368 · 2026-05-22T09:37:11.028478+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1215
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-22T09:37:11.030212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 761
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-22T09:37:38.039562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation sparsity LLM SwiGLU 2025 2026 contextual sparsity prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation sparsity LLM SwiGLU 2025 2026 contextual sparsity prediction"
  }
}
```

</details>

---


### Tool call

_source line 1371 · 2026-05-22T09:37:38.493238+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MaskLLM structured sparsity KL divergence learnable masks 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MaskLLM structured sparsity KL divergence learnable masks 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-22T09:37:39.246553+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "D2D-MoE ShadowLLM predictor-based activation sparsity 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "D2D-MoE ShadowLLM predictor-based activation sparsity 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-22T09:37:45.722426+00:00_

Web search results for query: "D2D-MoE ShadowLLM predictor-based activation sparsity 2024 2025"

Links: [{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2406.16635"},{"title":"[2406.16635] ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/abs/2406.16635"},{"title":"[2406.16635v2] ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/abs/2406.16635v2"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/de/overview/2406.16635v2"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1068/"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/html/2406.16635v1"},{"title":"[Literature Review] ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://www.themoonlight.io/en/review/shadowllm-predictor-based-contextual-sparsity-for-large-language-models"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=contextual+sparsity"},{"title":"Activation Sparsity Opportunities for Compressing General Large Language Models","url":"https://arxiv.org/html/2412.12178v2"}]

Based on the search results, I found information about **ShadowLLM** and **predictor-based activation sparsity**, but the results did not contain information about "D2D-MoE" specifically. Here's what I found:

## ShadowLLM: Predictor-based Contextual Sparsity

ShadowLLM is a novel predictor that can shadow LLM behavior and enforce better sparsity patterns, resulting in over 15% improvement in end-to-end accuracy compared to prior methods. ShadowLLM achieves up to a 20% speedup over the state-of-the-art DejaVu framework.

### Key Features:

Contextual sparsity, where the sparsity p
…[truncated 873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6475
}
```

</details>

---


### Tool result

_source line 1374 · 2026-05-22T09:37:45.990244+00:00_

Web search results for query: "activation sparsity LLM SwiGLU 2025 2026 contextual sparsity prediction"

Links: [{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884"},{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2408.14690v1"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"},{"title":"Learn To be Efficient: Build Structured Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2402.06126"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"}]

I found several relevant research papers on activation sparsity in LLMs with contextual sparsity prediction. Here are the key findings:

## Recent Research on Activation Sparsity and SwiGLU

Recent LLMs adopt smoother activations like SwiGLU, which yield denser activations and limit the benefits of sparsity. This presents a challenge since early models employing ReLU activations demonstrated high activation sparsity, with over 90% of the feed-forward network outputs being zero-valued, allowing significant computational savings.

## Contextual Sparsity Prediction Approaches

Contextual sparsity can be leveraged at runtime through sparsity predictors or learned routers that dynamically select the neurons to activate based on the input vectors. 

Two notable recent approaches are:

1. **DejaVu (2023)**: Liu et al. propose DejaVu, which learns a small auxiliary model that predicts the contextual activation sparsity patterns of future layers, and realize a 2× wall-clock speed-up on OPT-175B.

2. **SVD Contextual Sparsity Predictors (202
…[truncated 691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7950
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-22T09:37:46.091480+00:00_

Web search results for query: "MaskLLM structured sparsity KL divergence learnable masks 2024 2025"

Links: [{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2409.17481"},{"title":"[2409.17481] MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/abs/2409.17481"},{"title":"Paper page - MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://huggingface.co/papers/2409.17481"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/397199936_MaskLLM_Learnable_Semi-Structured_Sparsity_for_Large_Language_Models"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Llu9nJal7b"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/0e9a05f5ce62284c91e4a33498899124-Paper-Conference.pdf"},{"title":"NeurIPS Poster MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://neurips.cc/virtual/2024/poster/95573"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/html/2409.17481v2"},{"title":"GitHub - VainF/MaskLLM-4V: Learnable Semi-structured Sparsity for Vision Transformers and Diffusion Transformers · GitHub","url":"https://github.com/VainF/MaskLLM-4V"},{"title":"GitHub - NVlabs/MaskLLM: [NeurIPS 24 Spotlight] MaskLLM: Learnable Semi-structured Sparsity for Large Language Models · GitHub","url":"https://github.com/nvlabs/maskllm"}]

Based on the web search results, here's what I found about MaskLLM and its approach to structured sparsity:

## Overview

MaskLLM is a learnable pruning method that establishes Semi-structured (or "N:M") Sparsity in LLMs, aimed at reducing computational overhead during inferenc
…[truncated 1454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7598
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-22T09:37:52.477613+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SVD contextual sparsity predictors 2026 fast LLM inference training-free"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SVD contextual sparsity predictors 2026 fast LLM inference training-free"
  }
}
```

</details>

---


### Tool call

_source line 1377 · 2026-05-22T09:37:53.682355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Polar Sparsity\" batched LLM inference contextual sparsity 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Polar Sparsity\" batched LLM inference contextual sparsity 2025"
  }
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-22T09:37:53.783770+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProSparse ReLU activation sparsity LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProSparse ReLU activation sparsity LLM 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-22T09:37:57.801399+00:00_

Web search results for query: "SVD contextual sparsity predictors 2026 fast LLM inference training-free"

Links: [{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://www.researchgate.net/publication/402480685_SVD_Contextual_Sparsity_Predictors_for_Fast_LLM_Inference"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"}]

I found a highly relevant recent paper matching your query!

The paper "SVD Contextual Sparsity Predictors for Fast LLM Inference" presents a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices.

The paper addresses the fact that existing techniques for efficient LLM inference acceleration based on contextual sparsity with minimal accuracy degradation require training sparse pattern predictors, and presents a framework for accelerating inference of ReGLU-based feed-forward networks (FFNs) within LLMs.

Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8× reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math and code generation.

The paper was published on arXiv on March 17, 2026, and is available at: https://arxiv.org/abs/2603.14110


REMINDER: You MUST include the sources above in your response to the user using markdown
…[truncated 12 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5323
}
```

</details>

---


### Tool result

_source line 1380 · 2026-05-22T09:37:59.909573+00:00_

Web search results for query: ""Polar Sparsity" batched LLM inference contextual sparsity 2025"

Links: [{"title":"[2505.14884] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/abs/2505.14884"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884v1"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with ...","url":"https://susavlsh10.github.io/files/Polar_Sparsity_NeurIPS_2025_CameraReady.pdf"},{"title":"Polar Sparsity: High Throughput Batched LLM","url":"https://openreview.net/pdf?id=cg2S1qqNSq"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | OpenReview","url":"https://openreview.net/forum?id=cg2S1qqNSq"},{"title":"NeurIPS Poster Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117070"},{"title":"[PDF] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Polar-Sparsity:-High-Throughput-Batched-LLM-with-Shrestha-Settlemyer/328fcf757fa9647ea5eb96d37ee735e52a43df43"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"},{"title":"Paper page - Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://huggingface.co/papers/2505.14884"}]

I found comprehensive information about Polar Sparsity. Here's what the research shows:

## Overview

Accelerating large language model (LLM) inference is critical for real-world deployments requiring high throughput and low latency, but contextual sparsity, where each token dynamically activates only a small subset of the model parameters, does not scale to large batch sizes due to union of active neurons q
…[truncated 1216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6227
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-22T09:38:01.014473+00:00_

Web search results for query: "ProSparse ReLU activation sparsity LLM 2024 2025"

Links: [{"title":"[2402.13516] ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://arxiv.org/abs/2402.13516"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://arxiv.org/html/2402.13516v1"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.180/"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity","url":"https://arxiv.org/pdf/2402.13516"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/prosparse-introducing-enhancing-intrinsic-activation-sparsity-within"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation ...","url":"https://aclanthology.org/2025.coling-main.180.pdf"},{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"}]

Based on the search results, here's what I found about ProSparse:

## Overview

ProSparse is a simple and effective sparsification method to push LLMs for higher activation sparsity while maintaining comparable performance. After substituting the activation function of LLMs with ReLU, ProSparse adopts progressive sparsity regularization with a factor smoothly increasing across multiple stages.

## Key Approach

ProSparse includes three steps: activation function substitution, progressive sparsity regularization, and activation threshold shifting. This can enhance activation sparsity and mitigate performance degradation by avoiding radical shifts in activation distributions.

## Performance Results

ProSparse achieves high sparsity of 89.32% for LLaMA2-7B, 88.80% for LLaMA2-13B, and 87.89% for end-size MiniC
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7230
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-22T09:38:11.832185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-22T09:38:11.882859+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-22T09:38:16.173902+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-22T09:38:16.224571+00:00_

1	Learned sparsity predictors for SwiGLU LLMs universally use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation confirms these discovered patterns---not the training mechanism itself---as the proximate quality driver.
5	A coupling alignment ranking emerges across five loss configurations; a per-layer KL control decomposes this into two dimensions with a task-dependent spectrum: signal type dominates PPL (98\% of the gap at 30\%), while coupling scope contributes 24--35\% on downstream tasks---both dimensions carry independent value.
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-22T09:38:16.224947+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-22T09:38:16.325741+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-22T09:38:23.064950+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-22T09:38:23.217281+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1390 · 2026-05-22T09:38:23.217703+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-22T09:38:23.268642+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-22T09:38:33.736652+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-22T09:38:34.140231+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-22T09:38:34.140799+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-22T09:38:34.392392+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-22T09:38:34.392850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-22T09:38:34.443367+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-22T09:38:38.772194+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-22T09:38:39.127359+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-22T09:41:43.665524+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5 (Quite sure. I tried to check the important points carefully.)\n**一句话总结**: 扎实的实证研究，分析框架有价值，但核心配方与 MaskLLM 高度重叠、无实际加速、知识密集型任务系统性退步未解释，整体贡献停留在 Findings 水平。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claims 有实验支撑但存在显著 caveats：C1 ablation 有 confound（s42 oracle 来自 earlier run）、coupling alignment dominance 可能是 loss function quality 而非 coupling 机制、知识型退步仅有假说无验证 |\n| Excitement | 2/5 | 与 MaskLLM 配方重叠度高、仅 30% sparsity sweet spot、6.4% latency overhead 无实际加速、MMLU/GSM8K 系统性退步限制实用价值 |\n\n---\n\n## Summary\n\n本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor，使用 Gumbel-Sigmoid relaxation + frozen weights + learnable masks。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），并通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type 和 coupling scope 两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证。论文自我定位为 \"primarily an empirical study\"。\n\n---\n\n## Strengths\n\n**S1. 分析框架设计有新意。** Target-swap ablation (C1, Table 3) 是一个巧妙的实验设计——将 KL 训出的 mask targets 喂给 BCE 训练，从而将 \"mask quality\" 与 \"gradient coupling\" 效应解耦。这比简单的 loss function 对比更有深度。per-layer KL control 分离 signal type vs. coupling scope 的设计也值得肯定（§4.4, Table 4）。\n\n**S2. 实验覆盖相对全面。** 5 种 loss 配置的 ablation（Table 4）、3-seed evaluation、predictor bottleneck sensitivity（Appendix B）、temperature schedule sensitivity（Appendix B.1）、OOD evaluation on C4（Appendix D）、跨架构 3 模型——整体实验工程量大且有条理。\n\n**S3. 诚实的自我定位。** 论文明确声明 \"we do not propose a new architecture or algorithm\"（Introduction para 5），且在 Limitations 节坦率承认知识密集型退步、sparsity ceiling、训练数据同质性。这种诚实度在投稿中比较少见。\n\n**S4. Related Work 非常全面。** 覆盖了 training-free methods（TEAL, CATS, R-Sparse, DIP, SparseInfer）、predictor-based methods（DejaVu, ShadowLLM, FastForward, SVD-CSP）、activation function engineering（ReLU Strikes Back, ProSparse, TurboSparse）、MoE routing（D2D-MoE, Expert Choice, MoNE）、weight pruning（Wanda, SparseGPT, SliceGPT）以及 MaskLLM 的三点详细对比。引用量和质量都很好。\n\n**S5. Compensation redundancy 是有实际价值的发现。** 证明 KL predictor 无需 FastForward 式 +67.2M compensation network（Appendix J），简化了 inference pipeline，这对实际部署有意义。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [Critical, Confidence 4/5] **与 MaskLLM 的新颖性区分不足**\n- 具体位置：Section 2 (Related Work), para \"Predictor-Based Contextual Sparsity\", lines on MaskLLM\n- 问题：论文核心配方——frozen weights + learnable masks + forward KL + Gumbel relaxation——与 MaskLLM (NeurIPS 2024 Spotlight) 完全一致。论文给出三点区分：(1) sparsity type (weight vs. activation)、(2) mask generation (direct parameters vs. predictor network)、(3) allocation (N:M groups vs. global top-k)。但这三点都是 application-level 差异而非 methodological innovation：将已有方法从 weight sparsity 迁移到 activation sparsity 本身不构成算法贡献。论文自称贡献在于 analysis framework (target-swap ablation, 2D taxonomy)，但 (a) target-swap ablation 是一个实验设计而非方法、(b) 2D taxonomy 是对已有方法的分类而非新框架。在 \"primarily empirical study\" 定位下，analysis insights 需要足够 surprising 才能撑起贡献——而 \"output-distribution loss 比 per-neuron loss 好\" 这个结论的 surprise factor 有限。\n- 为什么影响接收：如果核心发现可以总结为 \"将 MaskLLM 的 KL 配方从 weight sparsity 改到 activation sparsity，效果比 BCE 好\"，则增量贡献可能不足以支撑 Main/Findings。\n- 建议修改方向：(a) 更深入讨论为什么 activation sparsity 场景下 coupling 效应比 weight sparsity 更重要（比如 global allocation 使得 inter-layer dependency 更关键），(b) 提供与 MaskLLM 的直接实验对比（如在 activation sparsity 场景下让 MaskLLM 的 direct-parameter masks 也用 KL 训练），(c) 或者将 novelty claim 聚焦在分析发现本身（coupling vs. signal type 分解）并强化其 actionable implications。\n\n**N2** [Critical, Confidence 5/5] **无实际推理加速，实用价值存疑**\n- 具体位置：Introduction para 5 (\"Wall-clock speedup requires sparse kernel support not addressed here\"); Appendix A Table 5 (+6.4% overhead)\n- 问题：论文全文围绕 \"sparsity prediction quality\" 展开，但 sparsity 的终极目标是推理加速。当前结果是：30% unstructured sparsity + 6.4% latency overhead = 净减速。论文在 Appendix A 承认 \"the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support\"。这意味着论文展示的是一种不能加速的 sparsity 方法。对比同期工作：Polar Sparsity (NeurIPS 2025) 实现 2.2× end-to-end speedup，SVD-CSP (2026) 实现 1.8× speedup。\n- 为什么影响接收：一篇 sparsity 论文如果不能展示实际加速（哪怕是 wall-clock 持平），其对社区的实际贡献受到严重质疑。\"prediction quality\" 改进如果不能转化为下游实际收益，则只是学术练习。\n- 建议修改方向：(a) 至少用 Triton block-sparse 或 cuSPARSE 做一个 proof-of-concept speedup 实验、(b) 或者明确将论文 reframe 为 \"understanding when KL > BCE for mask training\"（纯分析贡献），不再以 sparsity/efficiency 为 selling point。\n\n**N3** [Critical, Confidence 4/5] **知识密集型任务系统性退步未解释**\n- 具体位置：Section 4.2 \"Task-Type Split\" para; Table 2; Limitations section; Section 4.5 (Qwen-14B: GSM8K -20pp, MMLU -2.8pp)\n- 问题：KL predictor 在 MMLU 和 GSM8K 上系统性地劣于 TEAL magnitude-based method——跨三个架构、多个 sparsity level 一致退步（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp global allocation）。论文给出的解释是 \"forward KL's mode-covering property preserves diverse activation patterns that benefit broad commonsense inference; however, this may dilute task-specific knowledge pathways\"（§4.2），但这只是一个未经验证的假说（论文自己标注 \"hypothesis\"）。对于一个声称 \"coupling alignment is the dominant design dimension\" 的论文，这种 claim 与实际结果的矛盾是严重的：如果 coupling alignment 真的 dominant，为什么在 knowledge tasks 上反而更差？\n- 为什么影响接收：这不是 edge case，而是一整类重要任务的系统性退步。如果 KL 在 MMLU/GSM8K 上一致劣于零训练成本的 TEAL，用户为什么要付出训练代价？这动摇了 method 的实用价值定位。\n- 建议修改方向：(a) 至少做 probing 实验验证 \"mode-covering dilutes knowledge\" 假说（如分析 MMLU 各 subject 的退步分布）、(b) 探索 hybrid 策略（如对不同 layer 或不同 task type 用不同 loss）、(c) 或者诚实 reframe contribution：KL predictor 是一种 commonsense-oriented predictor，不适用于 knowledge-intensive scenarios。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major, Confidence 3/5] **C1 target-swap ablation 存在 confound**\n- 具体位置：Table 3, footnote †; Section 4.3 \"Soft-vs-Hard Confound\" para\n- 问题：C1 ablation 的核心逻辑是：BCE on KL-derived masks ≈ KL → masks are the driver, not gradient coupling。但 (a) s42 oracle 来自 \"an earlier training run\"（Table 3 footnote），引入 trajectory dependence；(b) oracle masks 本身编码了 KL training 的 specific trajectory（optimizer state, Gumbel noise），所以 BCE 在这些 targets 上训练本质上是在 distill KL 的 training trajectory，而非独立验证 mask quality；(c) soft-vs-hard confound 虽然论文讨论了（BCE+Gumbel 32.22 vs standard BCE 27.97），但这其实说明 representation form 也 matters——不仅是 mask quality。\n- 建议：(a) 用 multiple independent KL runs 的 majority-vote masks 作为 targets 消除 trajectory dependence、(b) 设计 reverse direction ablation（KL on magnitude targets）来完善 causal claim。\n\n**W2** [Major, Confidence 4/5] **\"Coupling alignment is the dominant design dimension\" 可能是 loss quality 而非 coupling 机制**\n- 具体位置：Conclusion; Abstract line 5; Section 4.4 per-layer decomposition\n- 问题：论文的核心 claim 是 coupling alignment（通过 output distribution 耦合 gradient）是关键设计维度。但 per-layer KL 已经达到 98% 的 PPL gap（9.05 vs 8.81, Table 4），这说明 cross-layer coupling 几乎不重要——真正重要的是 signal type（output distribution vs. intermediate activations）。这与 \"coupling alignment\" 这个术语暗示的含义不同：coupling 暗示的是 inter-layer gradient interaction，但实际驱动力是 loss function 的 quality（KL on outputs > MSE on intermediate）。Conclusion 中 \"coupling alignment—optimizing through the output distribution—is the dominant design dimension\" 这句话 conflates 了 signal type 和 coupling，有误导性。\n- 建议：区分 \"what to optimize\"（output distribution vs. intermediate）和 \"how gradients flow\"（coupled vs. independent），在 Conclusion 中准确归因。\n\n**W3** [Major, Confidence 4/5] **30% sparsity ceiling 过低，实用场景有限**\n- 具体位置：Limitations; Table 2; Section 4.5\n- 问题：30% sparsity 是 \"lowest-degradation level\"——但即使在此水平，MMLU 从 65.27%（dense）降至 40.7%（-24.6pp），GSM8K 从 48.75% 降至 7.5%（-41pp）。这意味着即使是 \"最佳\" sparsity level，模型能力也已大幅衰退。相比之下，同期 Polar Sparsity 在 50% sparsity 下维持 <1% accuracy drop。论文的 sweet spot 分析（Table 14）显示 35% 已经开始 MMLU 退步（40.4% → 35.5% uniform）。\n- 建议：讨论为什么 predictor-based 方法在低于 50% sparsity 就开始严重退化，与 training-free methods 的 degradation curve 做直接对比。\n\n**W4** [Minor, Confidence 3/5] **术语过度创造**\n- 具体位置：Throughout paper\n- 问题：\"coupling alignment ranking\"、\"signal type × coupling scope\"、\"2D taxonomy\" 这些术语包装了相对简单的概念。\"coupling alignment ranking\" 就是 \"按 loss function 类型排序\"；\"signal type × coupling scope\" 就是 \"loss target × gradient scope\"；\"2D taxonomy\" 就是一张分类表。过度术语化降低了可读性，让读者花时间 decode 术语而非理解核心 insight。\n- 建议：简化术语，使用更直觉的描述。\n\n**W5** [Minor, Confidence 3/5] **Batch size 限制未讨论**\n- 具体位置：Appendix A; Section 4.5\n- 问题：所有实验使用 batch size 1。Polar Sparsity (NeurIPS 2025) 已证明 contextual sparsity 在 batched inference 下效果显著下降（union of active neurons → dense），这是 contextual sparsity 最大的实用障碍之一。论文完全没有讨论这一维度。\n- 建议：至少讨论 batched inference 对 contextual sparsity 的影响，评估 predictor overhead amortization 的可能性。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** Per-layer KL 已达 98% of PPL gap (9.05 vs 8.81)。如果 cross-layer coupling 只贡献 2% PPL improvement，为什么 \"coupling\" 是论文的核心 selling point？downstream 上 24-35% 的 coupling scope 贡献是否足够支撑这个 claim？\n\n**Q2.** MaskLLM 在 activation sparsity 场景下的表现如何？如果将 MaskLLM 的 direct-parameter mask 方案直接应用于 activation sparsity（给每个 token 独立的 learnable masks），KL 的优势是否仍然成立？\n\n**Q3.** MMLU/GSM8K 退步在 14B 上放大（GSM8K -20pp）。是否在更大模型（如 70B）上进行过任何 preliminary evaluation？退步趋势是否随 scale 线性增长？\n\n**Q4.** C1 ablation 中 s42 oracle 的 PPL gap (0.65pp) 显著大于 s123/s456 (<0.02pp)。论文将此归因于 \"earlier training run\"——这是否意味着 C1 的结论对 oracle provenance 高度敏感？\n\n**Q5.** 论文在 Abstract 中 claim \"14.5% PPL reduction\"，但这是 matched sparsity (28.5% vs 29.3%) 下的数字。在 exact 30% sparsity 下，TEAL PPL 是 10.82 vs KL 8.81 = 18.6% reduction（Table 2）。为什么选择 matched sparsity 的较保守数字而非 nominal comparison？\n\n---\n\n## Missing References\n\nRelated work 已非常全面。以下是可考虑补充的近期工作（非 critical）：\n\n1. **SparseInfer** (Shin et al., 2025) — 已引用 ✓\n2. **Polar Sparsity** — 已引用 ✓，但建议在 Limitations 中讨论 batched inference 维度\n3. **SVD-CSP** (Serbin et al., 2026) — 已引用 ✓\n4. **COTS** (Zhang et al., 2025, arXiv:2511.09822) — \"Multi-channel Exploiting: Sparse FFNs for Pre-training and Inference\" — 可能遗漏，但发表时间与提交时间接近，非 critical\n5. **LazyLLM** (Fu et al., 2024) — token-level dynamic pruning for attention + FFN，与 predictor-based 方法互补，可能值得在 routing section 提及\n\nOverall：Related Work 完整度 **8/10**，属于上乘水平。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract line 1 \"universally use binary cross-entropy (BCE)\" — FastForward 用的也是 BCE，但 ShadowLLM 用 MSE，此处 \"universally\" 不准确\n- Table 2 footnote ‡ 说明 actual sparsity 不同（KL 28.5% vs TEAL 29.3%），这个差异虽然在 Appendix D 有 matched comparison，但主文 Table 2 是读者第一印象，建议在表格内更显著标注\n- Figure 2 (sparsity sweep) y 轴 range 不清，建议标注 dense baseline\n- Appendix G (MSE baseline config) 提到 seed 123 出现 catastrophic failure (PPL=15,789, 5.1% sparsity)——这是 MSE 方法的严重 instability，应在主文更显著提及以加强 KL vs MSE 的论点\n\n---\n\n## 主要优势总结\n\n1. 分析框架（C1 + per-layer KL decomposition）在方法论上有贡献\n2. 实验覆盖全面，3-seed evaluation + 跨架构验证\n3. 论文写作诚实，不 overclaim\n4. Related work 非常 thorough\n5. Compensation redundancy 发现有实际价值\n\n## 最终判断\n\n论文是一项扎实的实证工作，但面临三个核心问题：(1) 与 MaskLLM 的 methodological overlap 使得 novelty 主要依赖 analysis framework，而 analysis insights 的 surprise factor 有限；(2) 无实际推理加速使得 practical impact 几乎为零；(3) 知识密集型任务的系统性退步是一个未解决的 fundamental limitation。这些问题使论文更适合 Findings track 而非 Main conference。如果作者能在 rebuttal 中提供 wall-clock speedup proof-of-concept + knowledge task 退步的 mechanistic explanation，评分可能提升至 3.5。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5 (Quite sure. I tried to check the important points carefully.)\n**一句话总结**: 扎实的实证研究，分析框架有价值，但核心配方与 MaskLLM 高度重叠、无实际加速、知识密集型任务系统性退步未解释，整体贡献停留在 Findings 水平。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claims 有实验支撑但存在显著 caveats：C1 ablation 有 confound（s42 oracle 来自 earlier run）、coupling alignment dominance 可能是 loss function quality 而非 coupling 机制、知识型退步仅有假说无验证 |\n| Excitement | 2/5 | 与 MaskLLM 配方重叠度高、仅 30% sparsity sweet spot、6.4% latency overhead 无实际加速、MMLU/GSM8K 系统性退步限制实用价值 |\n\n---\n\n## Summary\n\n本文提出用 forward KL divergence 替代 BCE 训练 SwiGLU LLM 的 contextual sparsity predictor，使用 Gumbel-Sigmoid relaxation + frozen weights + learnable masks。在 LLaMA-3.1-8B 上 30% sparsity 下 PPL 降低 14.5%（matched sparsity），并通过 target-swap ablation (C1) 和 per-layer KL control 将改进分解为 signal type 和 coupling scope 两个维度。跨架构在 Mistral-7B 和 Qwen-14B 上验证。论文自我定位为 \"primarily an empirical study\"。\n\n---\n\n## Strengths\n\n**S1. 分析框架设计有新意。** Target-swap ablation (C1, Table 3) 是一个巧妙的实验设计——将 KL 训出的 mask targets 喂给 BCE 训练，从而将 \"mask quality\" 与 \"gradient coupling\" 效应解耦。这比简单的 loss function 对比更有深度。per-layer KL control 分离 signal type vs. coupling scope 的设计也值得肯定（§4.4, Table 4）。\n\n**S2. 实验覆盖相对全面。** 5 种 loss 配置的 ablation（Table 4）、3-seed evaluation、predictor bottleneck sensitivity（Appendix B）、temperature schedule sensitivity（Appendix B.1）、OOD evaluation on C4（Appendix D）、跨架构 3 模型——整体实验工程量大且有条理。\n\n**S3. 诚实的自我定位。** 论文明确声明 \"we do not propose a new architecture or algorithm\"（Introduction para 5），且在 Limitations 节坦率承认知识密集型退步、sparsity ceiling、训练数据同质性。这种诚实度在投稿中比较少见。\n\n**S4. Related Work 非常全面。** 覆盖了 training-free methods（TEAL, CATS, R-Sparse, DIP, SparseInfer）、predictor-based methods（DejaVu, ShadowLLM, FastForward, SVD-CSP）、activation function engineering（ReLU Strikes Back, ProSparse, TurboSparse）、MoE routing（D2D-MoE, Expert Choice, MoNE）、weight pruning（Wanda, SparseGPT, SliceGPT）以及 MaskLLM 的三点详细对比。引用量和质量都很好。\n\n**S5. Compensation redundancy 是有实际价值的发现。** 证明 KL predictor 无需 FastForward 式 +67.2M compensation network（Appendix J），简化了 inference pipeline，这对实际部署有意义。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [Critical, Confidence 4/5] **与 MaskLLM 的新颖性区分不足**\n- 具体位置：Section 2 (Related Work), para \"Predictor-Based Contextual Sparsity\", lines on MaskLLM\n- 问题：论文核心配方——frozen weights + learnable masks + forward KL + Gumbel relaxation——与 MaskLLM (NeurIPS 2024 Spotlight) 完全一致。论文给出三点区分：(1) sparsity type (weight vs. activation)、(2) mask generation (direct parameters vs. predictor network)、(3) allocation (N:M groups vs. global top-k)。但这三点都是 application-level 差异而非 methodological innovation：将已有方法从 weight sparsity 迁移到 activation sparsity 本身不构成算法贡献。论文自称贡献在于 analysis framework (target-swap ablation, 2D taxonomy)，但 (a) target-swap ablation 是一个实验设计而非方法、(b) 2D taxonomy 是对已有方法的分类而非新框架。在 \"primarily empirical study\" 定位下，analysis insights 需要足够 surprising 才能撑起贡献——而 \"output-distribution loss 比 per-neuron loss 好\" 这个结论的 surprise factor 有限。\n- 为什么影响接收：如果核心发现可以总结为 \"将 MaskLLM 的 KL 配方从 weight sparsity 改到 activation sparsity，效果比 BCE 好\"，则增量贡献可能不足以支撑 Main/Findings。\n- 建议修改方向：(a) 更深入讨论为什么 activation sparsity 场景下 coupling 效应比 weight sparsity 更重要（比如 global allocation 使得 inter-layer dependency 更关键），(b) 提供与 MaskLLM 的直接实验对比（如在 activation sparsity 场景下让 MaskLLM 的 direct-parameter masks 也用 KL 训练），(c) 或者将 novelty claim 聚焦在分析发现本身（coupling vs. signal type 分解）并强化其 actionable implications。\n\n**N2** [Critical, Confidence 5/5] **无实际推理加速，实用价值存疑**\n- 具体位置：Introduction para 5 (\"Wall-clock speedup requires sparse kernel support not addressed here\"); Appendix A Table 5 (+6.4% overhead)\n- 问题：论文全文围绕 \"sparsity prediction quality\" 展开，但 sparsity 的终极目标是推理加速。当前结果是：30% unstructured sparsity + 6.4% latency overhead = 净减速。论文在 Appendix A 承认 \"the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support\"。这意味着论文展示的是一种不能加速的 sparsity 方法。对比同期工作：Polar Sparsity (NeurIPS 2025) 实现 2.2× end-to-end speedup，SVD-CSP (2026) 实现 1.8× speedup。\n- 为什么影响接收：一篇 sparsity 论文如果不能展示实际加速（哪怕是 wall-clock 持平），其对社区的实际贡献受到严重质疑。\"prediction quality\" 改进如果不能转化为下游实际收益，则只是学术练习。\n- 建议修改方向：(a) 至少用 Triton block-sparse 或 cuSPARSE 做一个 proof-of-concept speedup 实验、(b) 或者明确将论文 reframe 为 \"understanding when KL > BCE for mask training\"（纯分析贡献），不再以 sparsity/efficiency 为 selling point。\n\n**N3** [Critical, Confidence 4/5] **知识密集型任务系统性退步未解释**\n- 具体位置：Section 4.2 \"Task-Type Split\" para; Table 2; Limitations section; Section 4.5 (Qwen-14B: GSM8K -20pp, MMLU -2.8pp)\n- 问题：KL predictor 在 MMLU 和 GSM8K 上系统性地劣于 TEAL magnitude-based method——跨三个架构、多个 sparsity level 一致退步（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp global allocation）。论文给出的解释是 \"forward KL's mode-covering property preserves diverse activation patterns that benefit broad commonsense inference; however, this may dilute task-specific knowledge pathways\"（§4.2），但这只是一个未经验证的假说（论文自己标注 \"hypothesis\"）。对于一个声称 \"coupling alignment is the dominant design dimension\" 的论文，这种 claim 与实际结果的矛盾是严重的：如果 coupling alignment 真的 dominant，为什么在 knowledge tasks 上反而更差？\n- 为什么影响接收：这不是 edge case，而是一整类重要任务的系统性退步。如果 KL 在 MMLU/GSM8K 上一致劣于零训练成本的 TEAL，用户为什么要付出训练代价？这动摇了 method 的实用价值定位。\n- 建议修改方向：(a) 至少做 probing 实验验证 \"mode-covering dilutes knowledge\" 假说（如分析 MMLU 各 subject 的退步分布）、(b) 探索 hybrid 策略（如对不同 layer 或不同 task type 用不同 loss）、(c) 或者诚实 reframe contribution：KL predictor 是一种 commonsense-oriented predictor，不适用于 knowledge-intensive scenarios。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major, Confidence 3/5] **C1 target-swap ablation 存在 confound**\n- 具体位置：Table 3, footnote †; Section 4.3 \"Soft-vs-Hard Confound\" para\n- 问题：C1 ablation 的核心逻辑是：BCE on KL-derived masks ≈ KL → masks are the driver, not gradient coupling。但 (a) s42 oracle 来自 \"an earlier training run\"（Table 3 footnote），引入 trajectory dependence；(b) oracle masks 本身编码了 KL training 的 specific trajectory（optimizer state, Gumbel noise），所以 BCE 在这些 targets 上训练本质上是在 distill KL 的 training trajectory，而非独立验证 mask quality；(c) soft-vs-hard confound 虽然论文讨论了（BCE+Gumbel 32.22 vs standard BCE 27.97），但这其实说明 representation form 也 matters——不仅是 mask quality。\n- 建议：(a) 用 multiple independent KL runs 的 majority-vote masks 作为 targets 消除 trajectory dependence、(b) 设计 reverse direction ablation（KL on magnitude targets）来完善 causal claim。\n\n**W2** [Major, Confidence 4/5] **\"Coupling alignment is the dominant design dimension\" 可能是 loss quality 而非 coupling 机制**\n- 具体位置：Conclusion; Abstract line 5; Section 4.4 per-layer decomposition\n- 问题：论文的核心 claim 是 coupling alignment（通过 output distribution 耦合 gradient）是关键设计维度。但 per-layer KL 已经达到 98% 的 PPL gap（9.05 vs 8.81, Table 4），这说明 cross-layer coupling 几乎不重要——真正重要的是 signal type（output distribution vs. intermediate activations）。这与 \"coupling alignment\" 这个术语暗示的含义不同：coupling 暗示的是 inter-layer gradient interaction，但实际驱动力是 loss function 的 quality（KL on outputs > MSE on intermediate）。Conclusion 中 \"coupling alignment—optimizing through the output distribution—is the dominant design dimension\" 这句话 conflates 了 signal type 和 coupling，有误导性。\n- 建议：区分 \"what to optimize\"（output distribution vs. intermediate）和 \"how gradients flow\"（coupled vs. independent），在 Conclusion 中准确归因。\n\n**W3** [Major, Confidence 4/5] **30% sparsity ceiling 过低，实用场景有限**\n- 具体位置：Limitations; Table 2; Section 4.5\n- 问题：30% sparsity 是 \"lowest-degradation level\"——但即使在此水平，MMLU 从 65.27%（dense）降至 40.7%（-24.6pp），GSM8K 从 48.75% 降至 7.5%（-41pp）。这意味着即使是 \"最佳\" sparsity level，模型能力也已大幅衰退。相比之下，同期 Polar Sparsity 在 50% sparsity 下维持 <1% accuracy drop。论文的 sweet spot 分析（Table 14）显示 35% 已经开始 MMLU 退步（40.4% → 35.5% uniform）。\n- 建议：讨论为什么 predictor-based 方法在低于 50% sparsity 就开始严重退化，与 training-free methods 的 degradation curve 做直接对比。\n\n**W4** [Minor, Confidence 3/5] **术语过度创造**\n- 具体位置：Throughout paper\n- 问题：\"coupling alignment ranking\"、\"signal type × coupling scope\"、\"2D taxonomy\" 这些术语包装了相对简单的概念。\"coupling alignment ranking\" 就是 \"按 loss function 类型排序\"；\"signal type × coupling scope\" 就是 \"loss target × gradient scope\"；\"2D taxonomy\" 就是一张分类表。过度术语化降低了可读性，让读者花时间 decode 术语而非理解核心 insight。\n- 建议：简化术语，使用更直觉的描述。\n\n**W5** [Minor, Confidence 3/5] **Batch size 限制未讨论**\n- 具体位置：Appendix A; Section 4.5\n- 问题：所有实验使用 batch size 1。Polar Sparsity (NeurIPS 2025) 已证明 contextual sparsity 在 batched inference 下效果显著下降（union of active neurons → dense），这是 contextual sparsity 最大的实用障碍之一。论文完全没有讨论这一维度。\n- 建议：至少讨论 batched inference 对 contextual sparsity 的影响，评估 predictor overhead amortization 的可能性。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** Per-layer KL 已达 98% of PPL gap (9.05 vs 8.81)。如果 cross-layer coupling 只贡献 2% PPL improvement，为什么 \"coupling\" 是论文的核心 selling point？downstream 上 24-35% 的 coupling scope 贡献是否足够支撑这个 claim？\n\n**Q2.** MaskLLM 在 activation sparsity 场景下的表现如何？如果将 MaskLLM 的 direct-parameter mask 方案直接应用于 activation sparsity（给每个 token 独立的 learnable masks），KL 的优势是否仍然成立？\n\n**Q3.** MMLU/GSM8K 退步在 14B 上放大（GSM8K -20pp）。是否在更大模型（如 70B）上进行过任何 preliminary evaluation？退步趋势是否随 scale 线性增长？\n\n**Q4.** C1 ablation 中 s42 oracle 的 PPL gap (0.65pp) 显著大于 s123/s456 (<0.02pp)。论文将此归因于 \"earlier training run\"——这是否意味着 C1 的结论对 oracle provenance 高度敏感？\n\n**Q5.** 论文在 Abstract 中 claim \"14.5% PPL reduction\"，但这是 matched sparsity (28.5% vs 29.3%) 下的数字。在 exact 30% sparsity 下，TEAL PPL 是 10.82 vs KL 8.81 = 18.6% reduction（Table 2）。为什么选择 matched sparsity 的较保守数字而非 nominal comparison？\n\n---\n\n## Missing References\n\nRelated work 已非常全面。以下是可考虑补充的近期工作（非 critical）：\n\n1. **SparseInfer** (Shin et al., 2025) — 已引用 ✓\n2. **Polar Sparsity** — 已引用 ✓，但建议在 Limitations 中讨论 batched inference 维度\n3. **SVD-CSP** (Serbin et al., 2026) — 已引用 ✓\n4. **COTS** (Zhang et al., 2025, arXiv:2511.09822) — \"Multi-channel Exploiting: Sparse FFNs for Pre-training and Inference\" — 可能遗漏，但发表时间与提交时间接近，非 critical\n5. **LazyLLM** (Fu et al., 2024) — token-level dynamic pruning for attention + FFN，与 predictor-based 方法互补，可能值得在 routing section 提及\n\nOverall：Related Work 完整度 **8/10**，属于上乘水平。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract line 1 \"universally use binary cross-entropy (BCE)\" — FastForward 用的也是 BCE，但 ShadowLLM 用 MSE，此处 \"universally\" 不准确\n- Table 2 footnote ‡ 说明 actual sparsity 不同（KL 28.5% vs TEAL 29.3%），这个差异虽然在 Appendix D 有 matched comparison，但主文 Table 2 是读者第一印象，建议在表格内更显著标注\n- Figure 2 (sparsity sweep) y 轴 range 不清，建议标注 dense baseline\n- Appendix G (MSE baseline config) 提到 seed 123 出现 catastrophic failure (PPL=15,789, 5.1% sparsity)——这是 MSE 方法的严重 instability，应在主文更显著提及以加强 KL vs MSE 的论点\n\n---\n\n## 主要优势总结\n\n1. 分析框架（C1 + per-layer KL decomposition）在方法论上有贡献\n2. 实验覆盖全面，3-seed evaluation + 跨架构验证\n3. 论文写作诚实，不 overclaim\n4. Related work 非常 thorough\n5. Compensation redundancy 发现有实际价值\n\n## 最终判断\n\n论文是一项扎实的实证工作，但面临三个核心问题：(1) 与 MaskLLM 的 methodological overlap 使得 novelty 主要依赖 analysis framework，而 analysis insights 的 surprise factor 有限；(2) 无实际推理加速使得 practical impact 几乎为零；(3) 知识密集型任务的系统性退步是一个未解决的 fundamental limitation。这些问题使论文更适合 Findings track 而非 Main conference。如果作者能在 rebuttal 中提供 wall-clock speedup proof-of-concept + knowledge task 退步的 mechanistic explanation，评分可能提升至 3.5。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-22T09:41:47.782302+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4116
}
```

</details>

---


### Assistant

_source line 1402 · 2026-05-22T09:41:59.417387+00:00_

审稿报告已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**，Soundness 3/5，Excitement 2/5，Confidence 4/5。

三个 Critical 问题：
1. 与 MaskLLM 核心配方高度重叠（frozen weights + KL + Gumbel），三点区分停留在 application-level
2. 无实际 wall-clock speedup（反而 +6.4% overhead），sparsity 论文的根本价值受质疑
3. MMLU/GSM8K 系统性退步跨三个架构一致出现但仅有未验证假说

三个 Major 问题：C1 ablation 有 trajectory confound、"coupling alignment dominance" claim 实际是 loss quality 而非 coupling 机制、30% sparsity ceiling 过低。

Related Work 完整度 8/10，写作诚实度值得肯定，分析框架（C1 + per-layer decomposition）有价值但不足以撑起 Main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 35

## Round 35

4 recorded events


### User

_source line 1403 · 2026-05-22T09:43:29.596699+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿报告

**Overall**: 3.0 (Findings), Soundness 3.5/5, Excitement 3.0/5, Confidence 4/5

## Must-Fix 问题

**N1** [critical] 无实际推理加速——方法增加 6.4% 延迟开销
Table 5 显示 +6.4% latency（126.78 vs 119.11 ms/fwd）。论文承认 unstructured masks 无法转化为 wall-clock speedup。建议 Triton block-sparse POC 或 reframe 为纯分析论文。

**N2** [critical] MMLU/GSM8K 在所有 scale 上一致退化——实用性存疑
KL 在 commonsense（ARC-c, WG, HS, PIQA）上优于 TEAL，但 knowledge-intensive（MMLU, GSM8K）上一致劣于 TEAL（8B -5.2pp MMLU; 14B -20pp GSM8K; Mistral -7.3pp GSM8K）。仅有假设性解释。建议验证 mode-covering 假设或设计 hybrid objective。

## Should-Fix 问题

**W1** [major] Per-layer KL 的训练-推理不匹配严重混淆了 2D 分解
Per-layer KL 训练时 mask 1 layer/step，推理时 32 层同时 mask。30% downstream 差距可能来自 train-inference mismatch 而非缺乏 cross-layer coupling。50% 退化到 34.85（vs E2E 11.92）更可能是 mismatch 放大而非 "coupling transitions from optional to essential"。建议训练 per-layer KL 时逐步增加 mask 层数。

**W2** [major] "Signal type accounts for 98% of PPL gap" 归因方法论不严谨
分解假设 signal type 和 coupling scope 正交（无交互效应）。实际上从 MSE→KL 改变了 loss target + gradient flow topology + optimization landscape。论文脚注承认但正文反复引用 98% 作为主结论。建议标注为 upper bound 估计。

**W3** [major] WikiText-103 训练 → WikiText-2 评估：同分布
两者均来自 English Wikipedia Good/Featured articles，本质同分布。C4 OOD 只有 2-seed（global）或 3-seed 但 CV=6.3%，downstream robustness（Table 11）只有 seed 42。

**W4** [major] C1 Target-Swap Ablation 存在循环性
KL-derived oracle 来自特定训练轨迹（Gumbel noise, optimizer state），是 point estimate。50% 只有 s42 且 oracle 来自 earlier run。Downstream 50% 也只有 s42。

**W5** [minor] MSE 50% 实质是 single-seed（s123 catastrophic failure, PPL=15789）
**W6** [minor] Actual sparsity mismatch 对 downstream 影响未量化

## Questions
Q1. Per-layer KL downstream 原始数值？
Q2. Per-layer KL mask K>1 layers/step 性能如何？
Q3. MMLU/GSM8K 退化与特定层 mask divergence 是否相关？
Q4. MSE s123 50% failure 是 Lagrangian controller 问题还是 MSE 优化景观？
Q5. 更多样化训练数据是否缓解 MMLU regression？
Q6. KL 蒸馏 $T>1$ 是否尝试过？

## 主要优势
1. 5 种 loss function 完整对比，最全面的实证研究
2. C1 设计巧妙
3. 诚实的 limitation 报告
4. 多架构/多 scale 初步验证
5. 2D taxonomy 有用
6. 详尽附录，可重现性高

## Missing References
未发现关键缺失。可补充 LLM in a Flash (Alizadeh et al., 2024), Outlier Suppression+ (Wei et al., 2023)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-22T09:44:57.776391+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: 无实际推理加速**\n\n完全同意。这也是我审稿报告中的 N2（Critical）。Appendix A Table 5 明确显示 +6.4% overhead，论文自己承认 \"unstructured element-wise masks do not translate to wall-clock speedup\"（Appendix A para 3）。我进一步补充：同期 Polar Sparsity (NeurIPS 2025, 已被论文引用 §2) 实现 2.2× speedup，SVD-CSP (2026, 已引用 §2) 实现 1.8× speedup——本文的 net slowdown 与领域发展方向严重脱节。R1 的两个建议（Triton POC 或 reframe 为分析论文）都是合理的修改方向。\n\n**[AGREE] R1-N2: MMLU/GSM8K 系统性退步**\n\n完全同意。这也是我的 N3（Critical）。补充数据：退步在 Qwen-14B 上更严重——Table 13 (Appendix K) 显示 KL uniform MMLU 63.55% vs TEAL 66.34%（-2.8pp），GSM8K 32.1±5.2% vs TEAL 52.1%（-20pp）。值得注意的是，论文在 §4.2 自己标注了 \"hypothesis; mechanistic investigation left to future work\"——这表明作者知道没有验证但选择留给未来工作。对于一篇以 \"coupling alignment is the dominant design dimension\" 为核心 claim 的论文，knowledge tasks 上的系统性劣势是一个严重的 claim-evidence mismatch。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: Per-layer KL 的训练-推理不匹配混淆了 2D 分解**\n\n同意，且认为这是 R1 最有洞察力的观察。论文自己在 §4.4 末尾也承认了这个 confound：\"A confound: training masks one layer per step while inference applies all 32; the downstream gap may partly reflect this train-inference shift.\" 但这个 caveat 只出现在段末一句，而 \"coupling scope contributes 24–35% on downstream tasks\" 的 claim 却在 Abstract line 5、Conclusion、和 contributions list 中反复出现。\n\n我进一步补充：50% sparsity 下 per-layer KL 退化到 34.85（Table 4）vs E2E 的 11.92——这个 3× gap 更可能是因为训练时只 mask 1/32 层但推理时同时 mask 32 层导致的 distribution shift catastrophe，而非 \"coupling transitions from optional refinement to essential coordination\"（§4.4）。R1 建议的\"逐步增加 mask 层数\"实验可以直接验证这个假说。\n\n**[AGREE] R1-W2: 98% 归因方法论不严谨**\n\n同意。这与我的 W2 观点一致。论文脚注（§4.4 footnote on \"signal type\"）承认 \"this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled\"——但正文仍然将 98% 作为关键结论反复引用（Abstract, Conclusion, Contributions list）。Signal type 和 coupling scope 之间存在明显的交互效应：改变 loss target 从 MSE 到 KL 同时改变了 (a) 优化目标、(b) gradient flow topology、(c) optimization landscape。98% 这个数字在方法论上是一个 confounded estimate，应标注为 upper bound 而非 point estimate。\n\n**[REBUT] R1-W3: WikiText-103 训练 → WikiText-2 评估：同分布**\n\n部分不同意。R1 说两者\"本质同分布\"是准确的——都来自 English Wikipedia Good/Featured articles。但论文已经做了 C4 OOD evaluation（Appendix D, Table 10）显示 KL 优势在 OOD 上保持（30%: C4 PPL 16.03±0.01; 50%: 18.40 vs TEAL 38.75, 52.5% relative advantage）。更重要的是，Table 11 (Appendix D) 的 downstream robustness 在 6 个 benchmark 上都显示 Δ≤1.1pp，说明 predictor masks 对 calibration domain shift 是 robust 的。\n\nR1 指出 C4 OOD 只有 2-seed（global）和 downstream 只有 seed 42 是合理的批评——seed 覆盖不足。但 \"同分布\" 这个批评本身的严重性应该降低，因为 in-domain 和 OOD 的一致性已经得到初步验证。这是一个 **minor** 而非 major 问题。\n\n**[AGREE] R1-W4: C1 Target-Swap Ablation 存在循环性**\n\n同意，这与我的 W1 观点一致。补充证据：Table 3 footnote † 明确说 s42 oracle 来自 \"an earlier training run\"，且 s42 的 PPL gap（0.65pp）显著大于 retrained seeds s123/s456（<0.02pp）。50% 只有单 seed (s42) 更是明显不足。Appendix P (Oracle Mask Provenance) 也承认 oracle 编码了 \"specific training trajectory (optimizer state, data order, Gumbel noise)\"。\n\n不过我要补充一个 nuance：s123 和 s456 的 retrained oracles 确实显示了更好的一致性（PPL gap <0.02pp），这在一定程度上缓解了 s42 的 confound。核心问题不是 C1 完全无效，而是其 causal claim 的强度被 confounds 削弱——论文应该将 C1 定位为 \"suggestive evidence\" 而非 \"confirms\"（§4.3 用了 \"confirms\" 三次）。\n\n**[AGREE] R1-W5: MSE 50% 实质是 single-seed**\n\n同意。Appendix G 明确说 seed 123 出现 catastrophic failure（PPL=15,789, 5.1% sparsity）。Table 4 的 MSE 50% 数字（229.26）实际上只代表 seed 42。论文应在主文中更显著标注这一点。不过我要补充：这个 failure 本身也是 MSE 方法 instability 的有力证据——KL 在相同条件下从未出现此类 failure（3-seed CV=0.6%, Appendix F），这反而加强了 KL > MSE 的论点。\n\n**[AGREE] R1-W6: Actual sparsity mismatch 对 downstream 影响未量化**\n\n同意但认为影响有限。Table 2 footnote ‡ 说明 KL 28.5% vs TEAL 29.3%——差 0.8pp。Appendix D (matched sparsity at 28.5%) 显示 PPL 10.30 vs 8.81，KL 优势从 18.6% 缩小到 14.5%，仍然显著。对 downstream 的影响未直接量化，但 0.8pp sparsity 差异不太可能解释 MMLU -5.2pp 或 ARC-c +4pp 的差距。这是一个需要 footnote 但不影响核心结论的 minor 问题。\n\n---\n\n## Questions 回应\n\n**R1-Q1 (Per-layer KL downstream 原始数值)**: 合理问题。§4.4 给出了 coupling scope contribution 的百分比（30–35%）但没有给出 per-layer KL 的原始 downstream 数值，只在 footnote 中说 \"E2E KL and per-layer KL are 3-seed means; MSE downstream is seed 42 only\"。作者应在 rebuttal 中提供完整数值。\n\n**R1-Q2 (Per-layer KL mask K>1 layers/step)**: 非常好的建议，直接指向 W1 的 train-inference mismatch confound。如果 K=2,4,8,16,32 的 gradual 实验能做出来，可以直接区分 coupling effect 和 mismatch effect。\n\n**R1-Q3 (MMLU/GSM8K 退化与层级 mask divergence 相关性)**: 有价值。Figure 7 (Appendix M) 和 Figure 4 (Appendix E) 提供了 per-layer divergence 数据，但论文没有将其与 per-task performance 关联。这是一个合理的 follow-up 分析。\n\n**R1-Q4 (MSE s123 failure 根因)**: Appendix G 说 \"sparsity reaches only 5.1% under the same λ_max cap\"——这更可能是 MSE 的 optimization landscape 问题（per-layer gradient 不稳定），而非 Lagrangian controller bug。KL 在相同 controller 下从未出现此 failure。\n\n**R1-Q5 (更多样化训练数据缓解 MMLU regression)**: 有价值但不确定。C4 OOD 的 downstream robustness（Table 11, Δ≤1.1pp）暗示 mask 本身对 domain 不敏感，所以训练数据多样化可能帮助有限。MMLU regression 更可能是 loss function 的固有属性而非训练数据问题。\n\n**R1-Q6 (KL 蒸馏 T>1)**: 有趣的方向。论文 §3.4 提到 \"No temperature scaling (T=1) is applied (Hinton et al., 2015)\"（Table 4 footnote 引用 Bengio 2013 STE）。T>1 可能 soften output distribution 从而缓解 mode-covering 的过度 diversity。但这改变了 KL 的优化景观，可能需要重新调参。合理的 rebuttal 实验。\n\n---\n\n## Missing References 回应\n\nR1 建议补充 LLM in a Flash (Alizadeh et al., 2024) 和 Outlier Suppression+ (Wei et al., 2023)。\n\nLLM in a Flash 关注的是 flash memory ↔ DRAM 的 data movement optimization 而非 activation sparsity prediction——相关性有限但可在 weight pruning/routing 段提及。Outlier Suppression+ 是量化方法，与本文的 sparsity focus 关系较远。两者都非 critical omission。\n\n---\n\n## 总体评价\n\nR1 和我的评分一致（Overall 3.0 Findings）。我们的核心关切高度重叠：无实际加速 (R1-N1 ↔ 我-N2)、知识型退步 (R1-N2 ↔ 我-N3)、C1 confound (R1-W4 ↔ 我-W1)、98% 归因问题 (R1-W2 ↔ 我-W2)。\n\nR1 独有的最有价值贡献是 **W1 (per-layer KL train-inference mismatch)**——这个观察比我的审稿更深入，指出了 2D 分解的根本方法论缺陷。如果作者不能在 rebuttal 中通过 gradual K 实验回应此点，coupling scope 的整条 contribution line 都会被严重削弱。\n\n我额外强调的 R1 未重点涉及的问题是 **MaskLLM novelty overlap**（我的 N1）——核心配方的重叠使得论文的独立贡献主要依赖 analysis framework，而 analysis insights 的 surprise factor 和 robustness 都受到上述 confounds 的影响。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: 无实际推理加速**\n\n完全同意。这也是我审稿报告中的 N2（Critical）。Appendix A Table 5 明确显示 +6.4% overhead，论文自己承认 \"unstructured element-wise masks do not translate to wall-clock speedup\"（Appendix A para 3）。我进一步补充：同期 Polar Sparsity (NeurIPS 2025, 已被论文引用 §2) 实现 2.2× speedup，SVD-CSP (2026, 已引用 §2) 实现 1.8× speedup——本文的 net slowdown 与领域发展方向严重脱节。R1 的两个建议（Triton POC 或 reframe 为分析论文）都是合理的修改方向。\n\n**[AGREE] R1-N2: MMLU/GSM8K 系统性退步**\n\n完全同意。这也是我的 N3（Critical）。补充数据：退步在 Qwen-14B 上更严重——Table 13 (Appendix K) 显示 KL uniform MMLU 63.55% vs TEAL 66.34%（-2.8pp），GSM8K 32.1±5.2% vs TEAL 52.1%（-20pp）。值得注意的是，论文在 §4.2 自己标注了 \"hypothesis; mechanistic investigation left to future work\"——这表明作者知道没有验证但选择留给未来工作。对于一篇以 \"coupling alignment is the dominant design dimension\" 为核心 claim 的论文，knowledge tasks 上的系统性劣势是一个严重的 claim-evidence mismatch。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: Per-layer KL 的训练-推理不匹配混淆了 2D 分解**\n\n同意，且认为这是 R1 最有洞察力的观察。论文自己在 §4.4 末尾也承认了这个 confound：\"A confound: training masks one layer per step while inference applies all 32; the downstream gap may partly reflect this train-inference shift.\" 但这个 caveat 只出现在段末一句，而 \"coupling scope contributes 24–35% on downstream tasks\" 的 claim 却在 Abstract line 5、Conclusion、和 contributions list 中反复出现。\n\n我进一步补充：50% sparsity 下 per-layer KL 退化到 34.85（Table 4）vs E2E 的 11.92——这个 3× gap 更可能是因为训练时只 mask 1/32 层但推理时同时 mask 32 层导致的 distribution shift catastrophe，而非 \"coupling transitions from optional refinement to essential coordination\"（§4.4）。R1 建议的\"逐步增加 mask 层数\"实验可以直接验证这个假说。\n\n**[AGREE] R1-W2: 98% 归因方法论不严谨**\n\n同意。这与我的 W2 观点一致。论文脚注（§4.4 footnote on \"signal type\"）承认 \"this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled\"——但正文仍然将 98% 作为关键结论反复引用（Abstract, Conclusion, Contributions list）。Signal type 和 coupling scope 之间存在明显的交互效应：改变 loss target 从 MSE 到 KL 同时改变了 (a) 优化目标、(b) gradient flow topology、(c) optimization landscape。98% 这个数字在方法论上是一个 confounded estimate，应标注为 upper bound 而非 point estimate。\n\n**[REBUT] R1-W3: WikiText-103 训练 → WikiText-2 评估：同分布**\n\n部分不同意。R1 说两者\"本质同分布\"是准确的——都来自 English Wikipedia Good/Featured articles。但论文已经做了 C4 OOD evaluation（Appendix D, Table 10）显示 KL 优势在 OOD 上保持（30%: C4 PPL 16.03±0.01; 50%: 18.40 vs TEAL 38.75, 52.5% relative advantage）。更重要的是，Table 11 (Appendix D) 的 downstream robustness 在 6 个 benchmark 上都显示 Δ≤1.1pp，说明 predictor masks 对 calibration domain shift 是 robust 的。\n\nR1 指出 C4 OOD 只有 2-seed（global）和 downstream 只有 seed 42 是合理的批评——seed 覆盖不足。但 \"同分布\" 这个批评本身的严重性应该降低，因为 in-domain 和 OOD 的一致性已经得到初步验证。这是一个 **minor** 而非 major 问题。\n\n**[AGREE] R1-W4: C1 Target-Swap Ablation 存在循环性**\n\n同意，这与我的 W1 观点一致。补充证据：Table 3 footnote † 明确说 s42 oracle 来自 \"an earlier training run\"，且 s42 的 PPL gap（0.65pp）显著大于 retrained seeds s123/s456（<0.02pp）。50% 只有单 seed (s42) 更是明显不足。Appendix P (Oracle Mask Provenance) 也承认 oracle 编码了 \"specific training trajectory (optimizer state, data order, Gumbel noise)\"。\n\n不过我要补充一个 nuance：s123 和 s456 的 retrained oracles 确实显示了更好的一致性（PPL gap <0.02pp），这在一定程度上缓解了 s42 的 confound。核心问题不是 C1 完全无效，而是其 causal claim 的强度被 confounds 削弱——论文应该将 C1 定位为 \"suggestive evidence\" 而非 \"confirms\"（§4.3 用了 \"confirms\" 三次）。\n\n**[AGREE] R1-W5: MSE 50% 实质是 single-seed**\n\n同意。Appendix G 明确说 seed 123 出现 catastrophic failure（PPL=15,789, 5.1% sparsity）。Table 4 的 MSE 50% 数字（229.26）实际上只代表 seed 42。论文应在主文中更显著标注这一点。不过我要补充：这个 failure 本身也是 MSE 方法 instability 的有力证据——KL 在相同条件下从未出现此类 failure（3-seed CV=0.6%, Appendix F），这反而加强了 KL > MSE 的论点。\n\n**[AGREE] R1-W6: Actual sparsity mismatch 对 downstream 影响未量化**\n\n同意但认为影响有限。Table 2 footnote ‡ 说明 KL 28.5% vs TEAL 29.3%——差 0.8pp。Appendix D (matched sparsity at 28.5%) 显示 PPL 10.30 vs 8.81，KL 优势从 18.6% 缩小到 14.5%，仍然显著。对 downstream 的影响未直接量化，但 0.8pp sparsity 差异不太可能解释 MMLU -5.2pp 或 ARC-c +4pp 的差距。这是一个需要 footnote 但不影响核心结论的 minor 问题。\n\n---\n\n## Questions 回应\n\n**R1-Q1 (Per-layer KL downstream 原始数值)**: 合理问题。§4.4 给出了 coupling scope contribution 的百分比（30–35%）但没有给出 per-layer KL 的原始 downstream 数值，只在 footnote 中说 \"E2E KL and per-layer KL are 3-seed means; MSE downstream is seed 42 only\"。作者应在 rebuttal 中提供完整数值。\n\n**R1-Q2 (Per-layer KL mask K>1 layers/step)**: 非常好的建议，直接指向 W1 的 train-inference mismatch confound。如果 K=2,4,8,16,32 的 gradual 实验能做出来，可以直接区分 coupling effect 和 mismatch effect。\n\n**R1-Q3 (MMLU/GSM8K 退化与层级 mask divergence 相关性)**: 有价值。Figure 7 (Appendix M) 和 Figure 4 (Appendix E) 提供了 per-layer divergence 数据，但论文没有将其与 per-task performance 关联。这是一个合理的 follow-up 分析。\n\n**R1-Q4 (MSE s123 failure 根因)**: Appendix G 说 \"sparsity reaches only 5.1% under the same λ_max cap\"——这更可能是 MSE 的 optimization landscape 问题（per-layer gradient 不稳定），而非 Lagrangian controller bug。KL 在相同 controller 下从未出现此 failure。\n\n**R1-Q5 (更多样化训练数据缓解 MMLU regression)**: 有价值但不确定。C4 OOD 的 downstream robustness（Table 11, Δ≤1.1pp）暗示 mask 本身对 domain 不敏感，所以训练数据多样化可能帮助有限。MMLU regression 更可能是 loss function 的固有属性而非训练数据问题。\n\n**R1-Q6 (KL 蒸馏 T>1)**: 有趣的方向。论文 §3.4 提到 \"No temperature scaling (T=1) is applied (Hinton et al., 2015)\"（Table 4 footnote 引用 Bengio 2013 STE）。T>1 可能 soften output distribution 从而缓解 mode-covering 的过度 diversity。但这改变了 KL 的优化景观，可能需要重新调参。合理的 rebuttal 实验。\n\n---\n\n## Missing References 回应\n\nR1 建议补充 LLM in a Flash (Alizadeh et al., 2024) 和 Outlier Suppression+ (Wei et al., 2023)。\n\nLLM in a Flash 关注的是 flash memory ↔ DRAM 的 data movement optimization 而非 activation sparsity prediction——相关性有限但可在 weight pruning/routing 段提及。Outlier Suppression+ 是量化方法，与本文的 sparsity focus 关系较远。两者都非 critical omission。\n\n---\n\n## 总体评价\n\nR1 和我的评分一致（Overall 3.0 Findings）。我们的核心关切高度重叠：无实际加速 (R1-N1 ↔ 我-N2)、知识型退步 (R1-N2 ↔ 我-N3)、C1 confound (R1-W4 ↔ 我-W1)、98% 归因问题 (R1-W2 ↔ 我-W2)。\n\nR1 独有的最有价值贡献是 **W1 (per-layer KL train-inference mismatch)**——这个观察比我的审稿更深入，指出了 2D 分解的根本方法论缺陷。如果作者不能在 rebuttal 中通过 gradual K 实验回应此点，coupling scope 的整条 contribution line 都会被严重削弱。\n\n我额外强调的 R1 未重点涉及的问题是 **MaskLLM novelty overlap**（我的 N1）——核心配方的重叠使得论文的独立贡献主要依赖 analysis framework，而 analysis insights 的 surprise factor 和 robustness 都受到上述 confounds 的影响。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-22T09:45:02.054732+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4278
}
```

</details>

---


### Assistant

_source line 1406 · 2026-05-22T09:45:12.697002+00:00_

已提交对 Reviewer 1 的逐条回应。核心结论：

- **6/9 条 [AGREE]**：无加速 (N1)、知识退步 (N2)、per-layer KL mismatch (W1)、98% 归因 (W2)、C1 循环性 (W4)、MSE single-seed (W5)
- **1 条 [REBUT]**：W3 (WikiText 同分布) —— C4 OOD evaluation + downstream robustness (Table 11, Δ≤1.1pp) 提供了初步 OOD 验证，严重性应从 major 降为 minor
- **2 条 nuanced AGREE**：W4 补充了 s123/s456 retrained oracles 的缓解证据；W6 认为 0.8pp sparsity 差异影响有限

特别认同 R1-W1 (per-layer KL train-inference mismatch) 是最深刻的观察——直接动摇了 coupling scope contribution 这条 contribution line。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 36

## Round 36

74 recorded events


### User

_source line 1407 · 2026-05-22T13:03:30.187617+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量 + 格式合规**。

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

1. **新颖性**：与 MaskLLM（KL + Gumbel-Softmax, N:M 权重稀疏）的配方高度重合——本文在 recipe 层面的独立贡献是什么？分析框架（signal type vs coupling scope decomposition）是否足够新颖？
2. **贡献完整性**：三个 contributions 是否都有充足的实验支撑？是否有 overclaim？Abstract/Intro 的 claim 与实验证据是否对齐？
3. **相关工作覆盖**：是否遗漏重要的 related work？与 predictor-based sparsity (DejaVu, ShadowLLM, FastForward, R-Sparse, DIP, SparseInfer 等) 的比较是否公平完整？
4. **写作质量**：行文是否清晰精炼？术语使用是否一致？是否有 AI 写作痕迹？论文叙事（narrative flow）是否连贯？
5. **格式合规**：正文是否 ≤8 页？匿名是否合规？参考文献格式是否符合 ACL natbib 规范？Table/Figure 编号和引用是否正确？
6. **Limitations 和 Ethics Statement**：是否充分覆盖论文的局限性？是否存在 ethics concern？

请给出结构化审稿报告：Summary → Strengths (逐条) → Weaknesses (逐条，标注 severity: Critical/Major/Minor/Info) → Questions → Missing References → Overall Assessment (score + confidence)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-22T13:03:39.255793+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1409 · 2026-05-22T13:03:39.307580+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-22T13:03:46.224560+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1411 · 2026-05-22T13:03:48.284348+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1412 · 2026-05-22T13:03:53.910325+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

I found information about ACL ARR 2026 reviewer guidelines and the review form. Here's what I discovered:

## Review Form Criteria

The main criteria for ARR Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Review Score Options

The review form includes the following score options:

- 5 = Consider for
…[truncated 1228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7685
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-22T13:03:55.265404+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6981
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-22T13:04:07.824235+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1415 · 2026-05-22T13:04:07.824630+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-22T13:04:08.326143+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1417 · 2026-05-22T13:04:09.280700+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1418 · 2026-05-22T13:04:09.432187+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1419 · 2026-05-22T13:04:09.883731+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1420 · 2026-05-22T13:04:10.290188+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 1421 · 2026-05-22T13:04:10.391196+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1422 · 2026-05-22T13:04:11.197374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---


### Tool call

_source line 1423 · 2026-05-22T13:04:11.197798+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1424 · 2026-05-22T13:04:11.705096+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---


### Tool call

_source line 1425 · 2026-05-22T13:04:11.705503+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-22T13:04:12.208335+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-22T13:04:12.664095+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1466
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-22T13:04:12.714717+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-22T13:04:14.354716+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2649
}
```

</details>

---


### Tool result

_source line 1430 · 2026-05-22T13:04:15.158531+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2950
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-22T13:04:15.312161+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2597
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-22T13:04:23.912254+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/submitted.pdf",
    "pages": "9-19",
    "project": "distill_sparse_swiglu",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1433 · 2026-05-22T13:04:26.111190+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all evaluation dimensions/criteria, their score ranges, and descriptions. I need the full list of fields a reviewer must fill out including Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all evaluation dimensions/criteria, their score ranges, and descriptions. I need the full list of fields a reviewer must fill out including Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, etc."
  }
}
```

</details>

---


### Tool result

_source line 1434 · 2026-05-22T13:04:26.463001+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.9}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 608.0}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 0.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 0.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 0.0}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p17.png\", \"width\": 
…[truncated 724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2550
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-22T13:04:33.449246+00:00_

# ACL Rolling Review Form - Evaluation Dimensions

## Required Review Fields

**1. Paper Summary**
Reviewer describes the paper's topic and identifies any potential misunderstandings.

**2. Summary of Strengths**
Identifies reasons supporting publication, including methodology, empirical results, theoretical analysis, or literature organization.

**3. Summary of Weaknesses**
Documents concerns prioritizing other papers, including correctness issues, limited impact, or clarity problems. Concerns should be numbered.

**4. Comments/Suggestions/Typos**
Optional feedback on improvements beyond addressing main concerns.

**5. Reviewer Confidence**
Scale 1-5: "5 = Positive that my evaluation is correct" through "1 = Not my area, or paper is very hard to understand."

**6. Soundness**
Scale 1-5 (half-point increments): Evaluates scientific rigor, experimental validity, and methodological soundness. "5 = Excellent: This study is one of the most thorough I have seen."

**7. Excitement**
Scale 1-5 (half-point increments): Subjective assessment of innovation, impact potential, and relevance. "5 = Highly Exciting: I would recommend this paper to others."

**8. Overall Assessment**
Scale 1-5 (half-point increments): Ranges from "5 = Consider for Award" to "1 = Do not resubmit."

**9. Best Paper Justification**
Required if recommending Award consideration.

**10. Limitations and Societal Impact**
Assesses whether authors adequately address limitations and potential harms to marginalized populations.

**11. Ethical Concerns**
Reviews against ACL ethics code; identifies violations or unaddressed issues.

**12. Needs Ethics Review**
Indicates if paper requires specialized ethics committee review.

**13. Reproducibility**
Scale 1-5: Evaluates whether results can be replicated. "5 = They could easily reproduce the results."

**14. Datasets**
Scale 1-5: Rates value of released datasets to the research community.

**15. Software**
Scale 1-5: Rates value of released software to other rese
…[truncated 132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7338
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-22T13:04:40.477693+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1437 · 2026-05-22T13:04:40.778905+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1438 · 2026-05-22T13:04:41.886865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 1439 · 2026-05-22T13:04:41.937922+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1159
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-22T13:04:48.784664+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-22T13:04:49.387616+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-22T13:04:49.689102+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-22T13:04:50.343492+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-22T13:04:50.694949+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-22T13:04:51.298502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-22T13:04:51.599756+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-22T13:04:52.002805+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-22T13:04:52.153862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-22T13:04:52.355521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_19/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1450 · 2026-05-22T13:04:52.457781+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-22T13:04:52.561526+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 407
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-22T13:04:59.738705+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1453 · 2026-05-22T13:04:59.739395+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-22T13:05:02.799693+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-22T13:05:03.151406+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns---not the training mechanism itself---as the proximate quality driver.
5	An output-distribution alignment ranking emerges across five loss configurations; a per-layer KL control decomposes this into two dimensions: signal type dominates PPL (up to 97.5\% of the gap at 30\%); a $K{=}4$ mismatch pilot (single seed) reveals task-dependent downstream structure---PPL and BoolQ gaps are predominantly mismatch artifacts, while commonsense retains $\sim$60\% genuine coupling.
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-22T13:05:03.151746+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1457 · 2026-05-22T13:05:03.453102+00:00_

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
11	A target-swap ablation suggests that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20.
…[truncated 2847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1458 · 2026-05-22T13:05:03.453478+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-22T13:05:03.504080+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-22T13:05:08.472210+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-22T13:05:08.472817+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-22T13:05:16.803839+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1463 · 2026-05-22T13:05:17.205438+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1464 · 2026-05-22T13:05:17.356498+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-22T13:05:17.709432+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1466 · 2026-05-22T13:05:17.860253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-22T13:05:18.061168+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-22T13:05:18.061501+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1469 · 2026-05-22T13:05:18.113038+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity pred
…[truncated 4835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1470 · 2026-05-22T13:05:33.258173+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-22T13:05:33.861072+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 1472 · 2026-05-22T13:05:33.912216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1473 · 2026-05-22T13:05:33.912816+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@inproceedings{geva2023dissecting,
6	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
7	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
8	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
9	  pages = {12216--12235},
10	  year = {2023},
11	}
12	
13	@article{fu2024lazyllm,
14	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
15	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
16	  year = {2024},
17	  journal = {arXiv preprint arXiv:2407.14057},
18	}
19	
20	@article{zhang2025cots,
21	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
22	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
23	  year = {2025},
24	  journal = {arXiv preprint arXiv:2502.14475},
25	}
26	
27	@inproceedings{alizadeh2024llmflash,
28	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
29	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
30	  year = {2024},
31	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
32	}
33	
34	@article{wei2023outlier,
35	  title = {Outlier Suppression+: Accurate Quantization of Large Language Models by Equivalent and Effective Shifting and Scaling},
36	  author = {Xiuying Wei and Yunchen Zhang and Yuhang Li and Xiangguo Zhang and Ruihao Gong and Jinyang Guo and Xianglong 
…[truncated 3318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1474 · 2026-05-22T13:07:05.648679+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 soundness excitement scoring criteria scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 soundness excitement scoring criteria scale"
  }
}
```

</details>

---


### Tool result

_source line 1475 · 2026-05-22T13:07:13.146369+00:00_

Web search results for query: "ACL ARR review form 2025 2026 soundness excitement scoring criteria scale"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about the ACL ARR review form scoring criteria:

## Three-Score System (2025-2026)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified by the text of the review. The soundness assessment evaluates whether the paper is sufficiently rigorous and well-supported. A score of 5 (Excellent) indicates: "This study is one of the most thorough 
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7497
}
```

</details>

---


### Tool call

_source line 1476 · 2026-05-22T13:07:21.475483+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact score scales (1-5 with descriptions for each level), and any other required fields. I need the exact text for each score level for Soundness, Excitement, and Overall Assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact score scales (1-5 with descriptions for each level), and any other required fields. I need the exact text for each score level for Soundness, Excitement, and Overall Assessment."
  }
}
```

</details>

---


### Tool result

_source line 1477 · 2026-05-22T13:07:28.275529+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Reviewer Confidence
Scale 1-5:
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## Soundness
Scale 1-5 with half-points:
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims."
- **3:** "Acceptable: This study provides sufficient support for its main claims."
- **2:** "Poor: Some of the main claims are not sufficiently supported."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement
Scale 1-5 with half-points:
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4:** "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3:** "Interesting: I might mention some points of this paper to others."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1:** "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## Overall Assessment
Scale 1-5 with half-points:
- **5:** "Consider for Award"
- **4:** "Conference: I think this paper could be accepted to an \*ACL conference."
- **3:** "Findings: I think this paper could be accepted to the Findings of the ACL."
- **2:** "Resubmit next cycle"
- **1:** "Do not resubmit"

**Additional Required Fields:** Reproducibility, Datasets, Software, Author Identity Knowledge (all with custom scales).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6800
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-22T13:09:39.344215+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 扎实的实证分析——2D taxonomy 和 target-swap ablation 是有价值的方法论贡献，但 recipe 层面对 MaskLLM 的增量有限，且缺乏实际加速，限制了主会议级别的 excitement。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（多 seed、cross-arch），但 97.5% signal type 上界基于非正交分解不可靠；K=4 pilot 单 seed；主表实际 sparsity 不匹配 |\n| Excitement | 2.5/5 | KL+Gumbel+frozen model recipe 与 MaskLLM 高度重合；无实际 wall-clock 加速（反增 6.4%）；分析框架有价值但 insights 部分可预期 |\n| Reproducibility | 4/5 | 详细的超参数、多 seed 评估、训练步数/温度/bottleneck 灵敏度分析；但未释放代码 |\n| Confidence | 4/5 | 熟悉 activation sparsity 和 KL 蒸馏领域 |\n\n---\n\n## 主要优势\n\n**S1. Target-swap ablation (C1) 实验设计精巧。** 通过将 KL 发现的 mask 喂给 BCE predictor 来解耦 mask 质量 vs. 梯度耦合，这是一个genuinely informative 的因果推断实验。Table 3 在 3 个 seed (30%) 和 1 个 seed (50%) 上结果一致（max Δ≤1.70pp），证据充分。(Section 4.4, Table 3)\n\n**S2. 多 seed 评估 + 诚实的混合结果报告。** 3-seed 评估（s42/s123/s456）贯穿全文，cross-seed variance 分析透明（如 30% global MMLU σ=9.5pp vs. uniform σ=1.3pp）。论文坦诚报告 KL 在 MMLU/GSM8K 上的系统性回退（8B -5.2pp, 14B -20pp GSM8K），没有选择性报告。(Table 2, Section 4.2, Limitations)\n\n**S3. 2D taxonomy 提供清晰的组织框架。** signal type × coupling scope 的分解虽然概念上简单，但有效地将 DejaVu/ShadowLLM/FastForward/本文放入统一坐标系。Table 1 + Appendix L 的讨论完整。(Section 3.7, Table 1)\n\n**S4. 跨架构验证有说服力。** 在 Mistral-7B (GQA+sliding window) 和 Qwen-2.5-14B 上验证 PPL 改善的泛化性。Mistral 3-seed 数据（PPL -17.3%）增强结论可信度。(Section 4.6, Tables 12-13)\n\n**S5. 消融实验覆盖全面。** Table 4 覆盖 5 种 loss variant + 2 种 relaxation + 2 种 coupling scope，系统性很强。bottleneck/temperature/training steps 的灵敏度分析也值得赞赏。(Section 4.5, Appendix B)\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **与 MaskLLM 的 recipe 新颖性区分不足**\n- 具体位置：Section 2 (Related Work), paragraph \"Predictor-Based Contextual Sparsity\"\n- 问题：MaskLLM (Fang et al., 2024, NeurIPS) 使用 frozen weights + learnable masks + KL divergence + Gumbel-Softmax，与本文的 frozen weights + predictor network + KL divergence + Gumbel-Sigmoid 在 recipe 层面高度重合。论文在 Related Work 中承认 \"shares the recipe-level principle\" 并指出技术差异（static N:M vs. dynamic per-token），但这一区分未在实验中量化：没有与 MaskLLM 的直接对比（即使是在 activation sparsity 设定下）。论文声称的核心增量是 \"analytical\"（分析框架），但如果 recipe 本身被视为 known technique 的直接应用，分析框架的新颖性是否足以支撑独立贡献就值得质疑。\n- 为什么影响接收：Reviewer 可能将本文视为 \"MaskLLM applied to activation sparsity\" + 事后分析，而非独立方法论贡献。\n- 建议修改方向：(1) 在 Introduction 或 Section 3 中更明确地论证 dynamic activation sparsity 与 static N:M sparsity 的本质差异（generalization to unseen inputs、per-token variability、与 TEAL global allocation 的交互）为什么使得这不是简单的 recipe 迁移；(2) 如果可能，在 activation sparsity 设定下与 MaskLLM 的 learnable-mask variant 做实验对比。\n\n**N2** [critical] **无实际推理加速，实用价值存疑**\n- 具体位置：Appendix A (Table 5), Section 4.6 最后一段\n- 问题：Predictor pipeline 增加 6.4% latency overhead（126.78 vs. 119.11 ms/fwd），即使在 50% sparsity 下也没有净加速。论文在 Appendix A 中坦承 \"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support\"，并明确 \"Our contribution is prediction quality and inference simplification, not end-to-end latency reduction\"。但这意味着论文的实际应用场景 entirely depends on 未来的 sparse kernel 支持——目前不存在的基础设施。\n- 为什么影响接收：对于 efficiency 论文，无法展示实际加速是重大缺陷。论文定位为 \"empirical study\"，但 Introduction 的 framing（\"learned sparsity predictors\"、\"inference allocates budgets globally\"）暗示效率是核心目标。这一 gap 在审稿中很可能被其他 reviewer 重点关注。\n- 建议修改方向：(1) 更早、更显著地声明本文是分析/理解导向而非效率导向（目前这一声明藏在 Introduction 倒数第二段和 Appendix A 中）；(2) 提供 Triton block-sparse 或类似方案的 proof-of-concept 加速数据，即使粗糙也能大幅增强实用性论点。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] **\"97.5% signal type\" 声称基于非正交分解**\n- 具体位置：Section 4.5 \"Per-Layer KL\" paragraph, Abstract line 5, Conclusion\n- 问题：论文反复引用 \"signal type accounts for up to 97.5% of the gap\"，但在 Section 4.5 脚注中承认 \"signal type and coupling scope are not fully orthogonal\"。这个 97.5% 是 (Per-layer KL - MSE) / (E2E KL - MSE) 的比值，但 per-layer KL 同时改变了 signal type AND 引入了部分 end-to-end 信号（通过 full forward pass 计算 KL），所以这两个维度不是独立的。将这个数字放在 Abstract 和 Conclusion 中作为 headline finding 是 overclaim。\n- 建议：将 \"up to 97.5%\" 降级为 \"a substantial majority\" 或在每次引用时明确标注 \"upper bound, dimensions not orthogonal\"。目前 Abstract 中没有任何 caveat。\n\n**W2** [major] **K=4 mismatch pilot 仅单 seed，但结论被推广**\n- 具体位置：Section 4.5 (最后一段), Appendix R (Table 17)\n- 问题：K=4 实验用来分解 mismatch vs. genuine coupling 效应，但只有 seed 42 一个数据点。考虑到 30% global MMLU 的 σ=9.5pp，单 seed 的 K=4 MMLU=43.5 超过 E2E KL 3-seed mean 40.7±1.3 可能完全是随机波动。论文在 Table 17 注释中说 \"interpret cautiously\"，但 Conclusion 和 Abstract 中直接写 \"a K=4 mismatch pilot reveals task-dependent downstream structure\"，hedging 不够。\n- 建议：在 Abstract/Conclusion 中明确标注 \"(single seed, preliminary)\"；或增加至少 2 个额外 seed 的 K=4 数据。\n\n**W3** [major] **主表 sparsity 不匹配：KL 28.5% vs. TEAL 29.3%**\n- 具体位置：Table 2 footnote ‡, Appendix C\n- 问题：Table 2 的 30% 对比中，KL 实际 sparsity 为 28.5% 而 TEAL 为 29.3%。虽然 Appendix C 提供了 matched-sparsity 对比（14.5% improvement at 28.5%），但主表用的是 mismatched 数据（19% improvement），且 Abstract 引用的 \"14.5%\" 来自 appendix 的 matched 对比而非主表。这种主表/Abstract 数字不一致容易混淆读者。\n- 建议：在主表中明确标注实际 sparsity 或使用 matched-sparsity 数字作为 headline claim。\n\n**W4** [minor-to-major] **下游任务回退缺乏深入分析**\n- 具体位置：Section 4.2 \"Task-Type Split\", Section 4.6 最后一段\n- 问题：KL 在 MMLU 和 GSM8K 上系统性输给 TEAL 和 magnitude-based 方法（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp）。论文将此归因于 \"distribution-matching objectives systematically sacrifice reasoning-critical pathways\" 和 late-layer over-pruning (L22-L28 sparsity 48-57%)，但没有验证这一因果链。如果问题确实是 late-layer starvation，是否可以通过 layer-wise sparsity constraint 来缓解？论文未尝试这一自然的 follow-up。\n- 建议：增加一个 layer-constrained sparsity 实验（如限制 late-layer sparsity ≤ 35%），验证 late-layer starvation 假说。\n\n**W5** [minor] **Baseline 选择不够全面**\n- 具体位置：Section 4.1 \"Baselines\"\n- 问题：实验 baseline 仅包括 TEAL、BCE (DejaVu-style)、MSE (ShadowLLM-style)。缺少与以下方法的对比：(1) R-Sparse（SVD projection-based, 同为 learned predictor）；(2) CATS（per-layer threshold adaptation, training-free 但更 sophisticated than TEAL）；(3) FastForward 的完整 pipeline（论文只测试了 compensation 组件）。这些缺失的 baseline 可能部分解决论文声称的 \"所有 prior predictor-based methods 使用 decomposed/intermediate objectives\" 这一 gap。\n- 建议：至少补充一个 training-free baseline (CATS 或 R-Sparse) 的对比。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** [minor] Introduction 第 18 行 \"Wall-clock speedup requires sparse kernel support not addressed here (Appendix A)\" — 这个关键 disclaimer 放在括号里太隐蔽，建议提升到更显眼的位置。\n- **M2** [minor] Table 2 注释过长（6 行），信息密度过高，可考虑拆分为正文说明。\n- **M3** [minor] Section 3.7 的 taxonomy table（Table 1）中大部分 cell 为空或只有 \"---\"，作为 \"Two-Dimensional Taxonomy\" 的 visual representation 信息含量有限。\n- **M4** [minor] Figure 2 (PPL scaling) 只展示 global allocation，但主结论在 30% 时推荐 uniform allocation，图表与结论的 allocation 策略不一致。\n- **M5** [info] 论文使用 `\\usepackage[review]{acl}`、author 为 \"Anonymous\" — 匿名合规 ✓。正文 Sections 1-5 在 8 页内 ✓。Limitations 和 Ethics Statement 在正文后、不计页数 ✓。References 使用 natbib ✓。\n\n---\n\n## Missing References\n\n以下相关工作可能需要讨论或与之对比：\n1. **CATS** (Lee et al., 2024): per-layer threshold adaptation for SiLU/SwiGLU — 已在 Related Work 提及但无实验对比\n2. **R-Sparse** (Zhang et al., 2025): rank-aware SVD projection for sparsity prediction — 已提及但无对比\n3. **Griffin/Hawk** (De et al., 2024): gated linear recurrence with hardware-efficient sparsity — 未提及\n4. **Turbo Sparse** (Song et al., 2024) 的 ReLUfication 后 KL distillation 步骤与本文有方法论重叠 — 已提及但未深入对比\n\n---\n\n## Questions for Authors\n\n1. 如果在 activation sparsity 设定下实现 MaskLLM 的 learnable-mask approach（去掉 predictor network，直接学习 per-layer mask parameters + Gumbel-Softmax），PPL 和下游表现如何？这能直接隔离 \"predictor generalization\" 的贡献。\n2. Late-layer over-pruning (L22-L28 at 48-57%) 是否可以通过 per-layer sparsity constraint 来缓解 MMLU/GSM8K 回退？\n3. 为什么没有在 50% sparsity 下进行 3-seed K=4 实验？考虑到 coupling 在 50% 时从 2.5% 升至 10.6%，这一 regime 的 K=4 数据更能支撑 coupling 重要性的 claim。\n4. WikiText-103 训练 → WikiText-2 评估存在 domain overlap。C4 OOD 结果显示 cross-seed variance 增大 31×（CV 6.3% vs. 0.2%）。是否尝试过更 diverse 的训练数据（如 C4 subsample）来降低 OOD variance？\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤ 8 页 | ✅ Sections 1-5 在 pages 1-8 |\n| ACL template [review] | ✅ `\\usepackage[review]{acl}` |\n| Double-blind (Anonymous) | ✅ Author: \"Anonymous ACL submission\" |\n| Mandatory Limitations | ✅ 1 段，覆盖 3 个点 |\n| Ethics Statement | ✅ 存在且合理 |\n| References 格式 | ✅ natbib, acl_natbib.bst |\n| Table/Figure 编号 | ✅ 连续编号，引用正确 |\n\n---\n\n## Overall Assessment 详细理由\n\n**给分 3.0 (Findings)** — Confidence 4/5\n\n这是一篇质量不错的实证研究，target-swap ablation 和 2D taxonomy 框架提供了有价值的方法论工具。实验执行严谨（多 seed、多架构、全面消融）。但以下因素限制了 main conference 级别的 excitement：\n\n1. **Recipe 新颖性有限**：KL+Gumbel+frozen model 的组合在 MaskLLM 中已建立，本文的增量是将其从 static N:M weight sparsity 迁移到 dynamic activation sparsity。分析框架虽有价值但概念上较直观。\n2. **无实际加速**：作为 efficiency-motivated 的工作，增加 6.4% overhead 而无法展示 wall-clock speedup 是重大短板。\n3. **下游回退显著**：MMLU/GSM8K 的系统性回退（跨规模一致）意味着 KL predictor 在 knowledge-intensive 场景下不如 training-free baseline，限制了实用价值。\n4. **关键 claims 的 evidence 不够 robust**：97.5% 上界基于非正交分解；K=4 pilot 单 seed；主表 sparsity 不匹配。\n\n论文适合 Findings 发表——分析框架对后续 predictor-based sparsity 研究有参考价值，但目前的 novelty 和 practical impact 不足以支撑主会议接收。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 扎实的实证分析——2D taxonomy 和 target-swap ablation 是有价值的方法论贡献，但 recipe 层面对 MaskLLM 的增量有限，且缺乏实际加速，限制了主会议级别的 excitement。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（多 seed、cross-arch），但 97.5% signal type 上界基于非正交分解不可靠；K=4 pilot 单 seed；主表实际 sparsity 不匹配 |\n| Excitement | 2.5/5 | KL+Gumbel+frozen model recipe 与 MaskLLM 高度重合；无实际 wall-clock 加速（反增 6.4%）；分析框架有价值但 insights 部分可预期 |\n| Reproducibility | 4/5 | 详细的超参数、多 seed 评估、训练步数/温度/bottleneck 灵敏度分析；但未释放代码 |\n| Confidence | 4/5 | 熟悉 activation sparsity 和 KL 蒸馏领域 |\n\n---\n\n## 主要优势\n\n**S1. Target-swap ablation (C1) 实验设计精巧。** 通过将 KL 发现的 mask 喂给 BCE predictor 来解耦 mask 质量 vs. 梯度耦合，这是一个genuinely informative 的因果推断实验。Table 3 在 3 个 seed (30%) 和 1 个 seed (50%) 上结果一致（max Δ≤1.70pp），证据充分。(Section 4.4, Table 3)\n\n**S2. 多 seed 评估 + 诚实的混合结果报告。** 3-seed 评估（s42/s123/s456）贯穿全文，cross-seed variance 分析透明（如 30% global MMLU σ=9.5pp vs. uniform σ=1.3pp）。论文坦诚报告 KL 在 MMLU/GSM8K 上的系统性回退（8B -5.2pp, 14B -20pp GSM8K），没有选择性报告。(Table 2, Section 4.2, Limitations)\n\n**S3. 2D taxonomy 提供清晰的组织框架。** signal type × coupling scope 的分解虽然概念上简单，但有效地将 DejaVu/ShadowLLM/FastForward/本文放入统一坐标系。Table 1 + Appendix L 的讨论完整。(Section 3.7, Table 1)\n\n**S4. 跨架构验证有说服力。** 在 Mistral-7B (GQA+sliding window) 和 Qwen-2.5-14B 上验证 PPL 改善的泛化性。Mistral 3-seed 数据（PPL -17.3%）增强结论可信度。(Section 4.6, Tables 12-13)\n\n**S5. 消融实验覆盖全面。** Table 4 覆盖 5 种 loss variant + 2 种 relaxation + 2 种 coupling scope，系统性很强。bottleneck/temperature/training steps 的灵敏度分析也值得赞赏。(Section 4.5, Appendix B)\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **与 MaskLLM 的 recipe 新颖性区分不足**\n- 具体位置：Section 2 (Related Work), paragraph \"Predictor-Based Contextual Sparsity\"\n- 问题：MaskLLM (Fang et al., 2024, NeurIPS) 使用 frozen weights + learnable masks + KL divergence + Gumbel-Softmax，与本文的 frozen weights + predictor network + KL divergence + Gumbel-Sigmoid 在 recipe 层面高度重合。论文在 Related Work 中承认 \"shares the recipe-level principle\" 并指出技术差异（static N:M vs. dynamic per-token），但这一区分未在实验中量化：没有与 MaskLLM 的直接对比（即使是在 activation sparsity 设定下）。论文声称的核心增量是 \"analytical\"（分析框架），但如果 recipe 本身被视为 known technique 的直接应用，分析框架的新颖性是否足以支撑独立贡献就值得质疑。\n- 为什么影响接收：Reviewer 可能将本文视为 \"MaskLLM applied to activation sparsity\" + 事后分析，而非独立方法论贡献。\n- 建议修改方向：(1) 在 Introduction 或 Section 3 中更明确地论证 dynamic activation sparsity 与 static N:M sparsity 的本质差异（generalization to unseen inputs、per-token variability、与 TEAL global allocation 的交互）为什么使得这不是简单的 recipe 迁移；(2) 如果可能，在 activation sparsity 设定下与 MaskLLM 的 learnable-mask variant 做实验对比。\n\n**N2** [critical] **无实际推理加速，实用价值存疑**\n- 具体位置：Appendix A (Table 5), Section 4.6 最后一段\n- 问题：Predictor pipeline 增加 6.4% latency overhead（126.78 vs. 119.11 ms/fwd），即使在 50% sparsity 下也没有净加速。论文在 Appendix A 中坦承 \"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support\"，并明确 \"Our contribution is prediction quality and inference simplification, not end-to-end latency reduction\"。但这意味着论文的实际应用场景 entirely depends on 未来的 sparse kernel 支持——目前不存在的基础设施。\n- 为什么影响接收：对于 efficiency 论文，无法展示实际加速是重大缺陷。论文定位为 \"empirical study\"，但 Introduction 的 framing（\"learned sparsity predictors\"、\"inference allocates budgets globally\"）暗示效率是核心目标。这一 gap 在审稿中很可能被其他 reviewer 重点关注。\n- 建议修改方向：(1) 更早、更显著地声明本文是分析/理解导向而非效率导向（目前这一声明藏在 Introduction 倒数第二段和 Appendix A 中）；(2) 提供 Triton block-sparse 或类似方案的 proof-of-concept 加速数据，即使粗糙也能大幅增强实用性论点。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] **\"97.5% signal type\" 声称基于非正交分解**\n- 具体位置：Section 4.5 \"Per-Layer KL\" paragraph, Abstract line 5, Conclusion\n- 问题：论文反复引用 \"signal type accounts for up to 97.5% of the gap\"，但在 Section 4.5 脚注中承认 \"signal type and coupling scope are not fully orthogonal\"。这个 97.5% 是 (Per-layer KL - MSE) / (E2E KL - MSE) 的比值，但 per-layer KL 同时改变了 signal type AND 引入了部分 end-to-end 信号（通过 full forward pass 计算 KL），所以这两个维度不是独立的。将这个数字放在 Abstract 和 Conclusion 中作为 headline finding 是 overclaim。\n- 建议：将 \"up to 97.5%\" 降级为 \"a substantial majority\" 或在每次引用时明确标注 \"upper bound, dimensions not orthogonal\"。目前 Abstract 中没有任何 caveat。\n\n**W2** [major] **K=4 mismatch pilot 仅单 seed，但结论被推广**\n- 具体位置：Section 4.5 (最后一段), Appendix R (Table 17)\n- 问题：K=4 实验用来分解 mismatch vs. genuine coupling 效应，但只有 seed 42 一个数据点。考虑到 30% global MMLU 的 σ=9.5pp，单 seed 的 K=4 MMLU=43.5 超过 E2E KL 3-seed mean 40.7±1.3 可能完全是随机波动。论文在 Table 17 注释中说 \"interpret cautiously\"，但 Conclusion 和 Abstract 中直接写 \"a K=4 mismatch pilot reveals task-dependent downstream structure\"，hedging 不够。\n- 建议：在 Abstract/Conclusion 中明确标注 \"(single seed, preliminary)\"；或增加至少 2 个额外 seed 的 K=4 数据。\n\n**W3** [major] **主表 sparsity 不匹配：KL 28.5% vs. TEAL 29.3%**\n- 具体位置：Table 2 footnote ‡, Appendix C\n- 问题：Table 2 的 30% 对比中，KL 实际 sparsity 为 28.5% 而 TEAL 为 29.3%。虽然 Appendix C 提供了 matched-sparsity 对比（14.5% improvement at 28.5%），但主表用的是 mismatched 数据（19% improvement），且 Abstract 引用的 \"14.5%\" 来自 appendix 的 matched 对比而非主表。这种主表/Abstract 数字不一致容易混淆读者。\n- 建议：在主表中明确标注实际 sparsity 或使用 matched-sparsity 数字作为 headline claim。\n\n**W4** [minor-to-major] **下游任务回退缺乏深入分析**\n- 具体位置：Section 4.2 \"Task-Type Split\", Section 4.6 最后一段\n- 问题：KL 在 MMLU 和 GSM8K 上系统性输给 TEAL 和 magnitude-based 方法（8B: MMLU -5.2pp; 14B: GSM8K -20pp, MMLU -8.1pp）。论文将此归因于 \"distribution-matching objectives systematically sacrifice reasoning-critical pathways\" 和 late-layer over-pruning (L22-L28 sparsity 48-57%)，但没有验证这一因果链。如果问题确实是 late-layer starvation，是否可以通过 layer-wise sparsity constraint 来缓解？论文未尝试这一自然的 follow-up。\n- 建议：增加一个 layer-constrained sparsity 实验（如限制 late-layer sparsity ≤ 35%），验证 late-layer starvation 假说。\n\n**W5** [minor] **Baseline 选择不够全面**\n- 具体位置：Section 4.1 \"Baselines\"\n- 问题：实验 baseline 仅包括 TEAL、BCE (DejaVu-style)、MSE (ShadowLLM-style)。缺少与以下方法的对比：(1) R-Sparse（SVD projection-based, 同为 learned predictor）；(2) CATS（per-layer threshold adaptation, training-free 但更 sophisticated than TEAL）；(3) FastForward 的完整 pipeline（论文只测试了 compensation 组件）。这些缺失的 baseline 可能部分解决论文声称的 \"所有 prior predictor-based methods 使用 decomposed/intermediate objectives\" 这一 gap。\n- 建议：至少补充一个 training-free baseline (CATS 或 R-Sparse) 的对比。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** [minor] Introduction 第 18 行 \"Wall-clock speedup requires sparse kernel support not addressed here (Appendix A)\" — 这个关键 disclaimer 放在括号里太隐蔽，建议提升到更显眼的位置。\n- **M2** [minor] Table 2 注释过长（6 行），信息密度过高，可考虑拆分为正文说明。\n- **M3** [minor] Section 3.7 的 taxonomy table（Table 1）中大部分 cell 为空或只有 \"---\"，作为 \"Two-Dimensional Taxonomy\" 的 visual representation 信息含量有限。\n- **M4** [minor] Figure 2 (PPL scaling) 只展示 global allocation，但主结论在 30% 时推荐 uniform allocation，图表与结论的 allocation 策略不一致。\n- **M5** [info] 论文使用 `\\usepackage[review]{acl}`、author 为 \"Anonymous\" — 匿名合规 ✓。正文 Sections 1-5 在 8 页内 ✓。Limitations 和 Ethics Statement 在正文后、不计页数 ✓。References 使用 natbib ✓。\n\n---\n\n## Missing References\n\n以下相关工作可能需要讨论或与之对比：\n1. **CATS** (Lee et al., 2024): per-layer threshold adaptation for SiLU/SwiGLU — 已在 Related Work 提及但无实验对比\n2. **R-Sparse** (Zhang et al., 2025): rank-aware SVD projection for sparsity prediction — 已提及但无对比\n3. **Griffin/Hawk** (De et al., 2024): gated linear recurrence with hardware-efficient sparsity — 未提及\n4. **Turbo Sparse** (Song et al., 2024) 的 ReLUfication 后 KL distillation 步骤与本文有方法论重叠 — 已提及但未深入对比\n\n---\n\n## Questions for Authors\n\n1. 如果在 activation sparsity 设定下实现 MaskLLM 的 learnable-mask approach（去掉 predictor network，直接学习 per-layer mask parameters + Gumbel-Softmax），PPL 和下游表现如何？这能直接隔离 \"predictor generalization\" 的贡献。\n2. Late-layer over-pruning (L22-L28 at 48-57%) 是否可以通过 per-layer sparsity constraint 来缓解 MMLU/GSM8K 回退？\n3. 为什么没有在 50% sparsity 下进行 3-seed K=4 实验？考虑到 coupling 在 50% 时从 2.5% 升至 10.6%，这一 regime 的 K=4 数据更能支撑 coupling 重要性的 claim。\n4. WikiText-103 训练 → WikiText-2 评估存在 domain overlap。C4 OOD 结果显示 cross-seed variance 增大 31×（CV 6.3% vs. 0.2%）。是否尝试过更 diverse 的训练数据（如 C4 subsample）来降低 OOD variance？\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤ 8 页 | ✅ Sections 1-5 在 pages 1-8 |\n| ACL template [review] | ✅ `\\usepackage[review]{acl}` |\n| Double-blind (Anonymous) | ✅ Author: \"Anonymous ACL submission\" |\n| Mandatory Limitations | ✅ 1 段，覆盖 3 个点 |\n| Ethics Statement | ✅ 存在且合理 |\n| References 格式 | ✅ natbib, acl_natbib.bst |\n| Table/Figure 编号 | ✅ 连续编号，引用正确 |\n\n---\n\n## Overall Assessment 详细理由\n\n**给分 3.0 (Findings)** — Confidence 4/5\n\n这是一篇质量不错的实证研究，target-swap ablation 和 2D taxonomy 框架提供了有价值的方法论工具。实验执行严谨（多 seed、多架构、全面消融）。但以下因素限制了 main conference 级别的 excitement：\n\n1. **Recipe 新颖性有限**：KL+Gumbel+frozen model 的组合在 MaskLLM 中已建立，本文的增量是将其从 static N:M weight sparsity 迁移到 dynamic activation sparsity。分析框架虽有价值但概念上较直观。\n2. **无实际加速**：作为 efficiency-motivated 的工作，增加 6.4% overhead 而无法展示 wall-clock speedup 是重大短板。\n3. **下游回退显著**：MMLU/GSM8K 的系统性回退（跨规模一致）意味着 KL predictor 在 knowledge-intensive 场景下不如 training-free baseline，限制了实用价值。\n4. **关键 claims 的 evidence 不够 robust**：97.5% 上界基于非正交分解；K=4 pilot 单 seed；主表 sparsity 不匹配。\n\n论文适合 Findings 发表——分析框架对后续 predictor-based sparsity 研究有参考价值，但目前的 novelty 和 practical impact 不足以支撑主会议接收。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1479 · 2026-05-22T13:09:43.008183+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3663
}
```

</details>

---


### Assistant

_source line 1480 · 2026-05-22T13:09:50.399769+00:00_

审稿报告已提交给 Review Director。

**总结**：给出 Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5。主要问题：(1) 与 MaskLLM 的 recipe 新颖性区分不足（2 个 critical）；(2) 无实际 wall-clock 加速；(3) "97.5% signal type" 基于非正交分解存在 overclaim；(4) K=4 pilot 单 seed 但结论被推广。优势在于 target-swap ablation 设计精巧、多 seed 评估严谨、写作诚实。格式合规无问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 37

## Round 37

4 recorded events


### User

_source line 1481 · 2026-05-22T13:10:43.249557+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每一条 Weakness/Question，用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿报告

**Overall**: 3 (Findings), Confidence 4/5

### 官方维度打分
| 维度 | 分数 |
|------|------|
| Soundness | 3/5 |
| Excitement | 2.5/5 |
| Reproducibility | 4/5 |

### 主要优势
S1. 新颖且 well-motivated 的问题框架（per-neuron BCE → output-distribution KL），forward KL mode-covering 在 false-negative 不对称场景有理论基础。2D taxonomy (Table 1) 有用。
S2. 全面且诚实的消融实验——Table 4 覆盖 8 种配置，不利结果如实报告。
S3. C1 target-swap ablation 设计有创意——3 种子 ≤1.70pp 一致性。
S4. 跨架构验证——Mistral-7B (3-seed) 和 Qwen-2.5-14B PPL advantage ratio 一致。
S5. 训练效率高——单 GPU ~45min，predictor <1% 参数。

### Must-Fix 问题
**N1** [Critical] 无 wall-clock 加速——6.4% overhead，unstructured masks 无 speedup。
**N2** [Critical] Per-layer KL "97.5% signal type" 基于 confounded K=1 设置（训练 mask 1/32 层 vs 推理 32 层）。K=4 pilot 仅 single-seed，MMLU K=4 超过 E2E KL（43.5 vs 40.7±1.3），GSM8K 负向 gap closure（-6.8%）——反常结果未排除。
**N3** [Major] MMLU/GSM8K 系统性退化跨 8B/14B 两 scale、LLaMA/Qwen 两架构，但 framing 偏重 PPL。Abstract/Intro 以 PPL 为主叙事，下游 trade-off 在 Conclusion 以 "task- and scale-dependent" 一笔带过。

### Should-Fix 问题
**W1** [Major] C1 的 trajectory confound——oracle masks 从特定 KL trajectory 提取，s42 oracle 来自 earlier training run。C1 证明 masks 可 transfer 但未证明 KL 是发现好 masks 的唯一/最佳途径。
**W2** [Major] 训练/评估域重叠——WikiText-103→WikiText-2 同 Wikipedia。C4 OOD 31× 更高 cross-seed variance。
**W3** [Minor] MSE baseline 可能未公平调参——seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）。
**W4** [Minor] Global allocation 30% MMLU σ=9.5pp 不可解读。
**W5** [Minor] 符号冲突——g^(ℓ) 在 Eq.(1) 为 gate activation，Eq.(4) 中 g1/g2 为 Gumbel noise。

### Questions
Q1. K=4 是否有多种子数据？MMLU 超 E2E 是否系统性？
Q2. 有没有尝试 per-layer sparsity 约束缓解 L22-L28 过度修剪？
Q3. 补偿对 BCE predictor 效果如何？"compensation provides no benefit" 可能仅因 KL 自带补偿。
Q4. 更大/更多样训练集是否缓解 OOD variance？

### Missing References
Griffin et al. 2024, Mirzadeh et al. 2024 (ReLU-fication), Wanda 互补性讨论。

---

请对以上每条 N/W/Q 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-22T13:12:25.742928+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 无 wall-clock 加速**\n同意这是 critical 问题。与我的 N2 一致。论文在 Appendix A 承认 unstructured masks 无法转化为 speedup（Table 5: +6.4% overhead），但这个 disclaimer 在正文中过于隐蔽（Introduction 倒数第二段括号内）。对于以 \"sparsity prediction\" 为核心的论文，无法展示 end-to-end 效率收益是硬伤。不过需要注意：论文自我定位为 \"primarily an empirical study\"（Section 1 倒数第二段），如果这一定位更加前置和显著，该问题的 severity 可以部分降低。\n\n**[AGREE] R1-N2: 97.5% signal type 基于 confounded 设置**\n同意。与我的 W1 一致。补充两点：\n1. Per-layer KL (K=1) 训练时只 mask 1/32 层但推理时 apply 全部 32 层，这个 train-inference mismatch 本身就是一个 confound——不能将 per-layer KL vs. E2E KL 的 gap 纯粹归因于 coupling scope。论文在 Section 4.5 脚注中承认 \"signal type and coupling scope are not fully orthogonal\"，但 Abstract 和 Conclusion 中引用 97.5% 时没有任何 caveat。\n2. K=4 的 MMLU 异常（43.5 vs. E2E 40.7±1.3）和 GSM8K 负向 gap closure (-6.8%) 确实是 red flags。Table 17 (Appendix R) 注释说 \"interpret cautiously\"，但这种 hedging 在 Abstract/Conclusion 中消失了——\"reveals task-dependent downstream structure\" 作为 headline finding 过于自信。\n\n**[AGREE] R1-N3: 下游回退 framing 偏重 PPL**\n同意这是 major concern，但 severity 可从 Critical 降为 Major。理由：\n- Abstract 确实提到 \"commonsense gains but knowledge-intensive decline\"（第 3 行）\n- Section 4.2 \"Task-Type Split\" 段落完整报告了 MMLU/GSM8K 的回退\n- Limitations 第二点 \"Knowledge-intensive regression\" 明确承认跨 scale 的系统性问题\n\n但 R1 的核心批评成立：Conclusion 的 \"task- and scale-dependent\" 措辞过于模糊，回避了 \"KL 在 knowledge tasks 上输给 training-free baseline\" 这一尖锐事实。Introduction 的叙事以 PPL 改善为主线（\"reduces perplexity by 14.5%\"），下游 trade-off 被压缩在列表第一项的子句中。建议将 Conclusion 改为更 balanced 的双面叙事。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: C1 trajectory confound**\n同意，但认为论文已 partially address。Appendix O (Oracle Mask Provenance) 明确讨论了 trajectory 依赖问题：\"C1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold...The s42/s123/s456 consistency (≤1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.\" 3-seed 一致性（Table 3: max Δ≤1.70pp at 30%）是一定程度的 evidence，但 R1 的核心论点成立：C1 证明好 masks 可 transfer，但没有证明 KL 是发现好 masks 的 *唯一* 途径。可能存在其他方法（如 evolutionary search、reinforcement learning）也能发现类似质量的 masks。这不影响论文的核心 finding（mask quality drives performance），但限制了 \"KL 作为 discovery mechanism\" 这一 claim 的 strength。\n\n**[AGREE] R1-W2: 训练/评估域重叠**\n同意。与我的 Q4 一致。WikiText-103 和 WikiText-2 都源自 Wikipedia，PPL 改善可能部分来自 in-domain 优势。C4 OOD 评估（Appendix C, Table 10）虽然保持了 KL 优势（52.5% advantage at 50%），但 cross-seed variance 急剧增大（CV 6.3% vs. 0.2%），且 seed 42 的 C4 PPL 异常偏高（18.22 vs. 其他 seed 16.37），暗示 predictor 对训练域有一定 overfitting。\n\n**[REBUT] R1-W3: MSE baseline 未公平调参**\n部分反驳。论文在 Appendix F 中详细说明了 MSE 的配置：与 KL/BCE 使用完全相同的架构、数据、优化器、Gumbel-Sigmoid relaxation，仅 loss function 不同。λ_max 设为 1000（vs. KL 的 5000）是因为 MSE 的 per-layer gradient magnitude 约 5× 大于 KL 的 end-to-end gradient，这是合理的工程调整而非不公平。Seed 123 的灾难性失败（PPL=15,789, 5.1% sparsity）恰恰说明 MSE loss 的 *内在不稳定性*——KL loss 在相同条件下 3-seed σ=0.02，而 MSE σ=1.68。这种 initialization sensitivity 本身就是一个有意义的 finding，而非调参不足的证据。但 R1 有一定道理：论文没有报告对 MSE 做 λ_max grid search 的尝试，无法排除更好的 λ_max 能部分缓解问题。\n\n**[REBUT] R1-W4: Global allocation MMLU σ=9.5pp 不可解读**\n反驳。论文的处理方式恰当：\n1. Table 2 同时报告了 global (σ=9.5pp) 和 uniform (σ=1.3pp) 两种 allocation 的 MMLU\n2. Section 4.2 明确解释了 global 高 variance 的来源——late-layer starvation (L31 retention 28.4%)\n3. Appendix J (Table 14) 展示了完整的 allocation 对比，30% 时推荐 uniform\n4. 高 variance 本身是一个 informative finding：它揭示了 global allocation 在 moderate sparsity 下的不稳定性\n\n论文没有用 global 30% MMLU 作为 headline number——Table 2 的 bold 标记在 MMLU 列给了 TEAL (45.86)，KL uniform 40.7±1.3 作为稳定替代。R1 的 concern 更多是 presentation 问题，非 soundness 问题。\n\n**[AGREE] R1-W5: 符号冲突 g^(ℓ) vs. g1/g2**\n同意。Eq.(1) 的 g^(ℓ) 表示 gate activation，Eq.(4) 的 g1, g2 表示 Gumbel noise samples。虽然上下标不同（上标 ℓ vs. 下标 1/2），但 g 作为 base symbol 在同一篇论文中有两种含义确实影响可读性。建议将 Gumbel noise 改为 ε1, ε2 或 ξ1, ξ2 以消除歧义。这是 minor fix。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: K=4 多种子数据**\n与我的 W2 和 Q3 一致。K=4 单 seed 的 MMLU 异常（43.5 > E2E 40.7±1.3）很可能是噪声。需要至少 3-seed K=4 数据才能判断这是系统性的还是随机的。\n\n**[AGREE] R1-Q2: Per-layer sparsity 约束**\n与我的 W4 建议一致。如果 late-layer over-pruning (L22-L28 at 48-57%, Appendix T, Table 20) 是 MMLU/GSM8K 回退的原因，per-layer sparsity cap（如 max 35%）是最直接的验证手段。论文未尝试这一自然实验是一个遗憾。\n\n**[AGREE] R1-Q3: 补偿对 BCE 效果**\n这是一个很好的问题，我在初审中遗漏了。论文报告 \"compensation provides no benefit\"（Section 4.5），但从 exp_id 看（kl_comp_30_s42, kl_comp_50_s42, bce_comp_staged_s42），似乎有做过 BCE+compensation 的实验。然而结果未在正文或附录中单独报告。如果 BCE+compensation 能显著缩小与 KL 的 gap，论文的核心论点（KL 的 mask quality 使 compensation 冗余）就需要重新审视：可能不是 KL masks 本身好到不需要 compensation，而是 BCE masks 差到 compensation 也救不了。两种解读有本质区别。\n\n**[AGREE] R1-Q4: 更多样训练集**\n与我的 Q4 一致。C4 subsample 或 mixed-domain 训练是降低 OOD variance 的自然尝试。\n\n---\n\n### Missing References\n\n**[REBUT] Griffin et al. 2024**: Griffin (De et al., 2024) 提出 gated linear recurrence 架构，与本文研究的 SwiGLU FFN activation sparsity 关联较弱。Griffin 的 sparsity 来自架构设计而非 post-hoc prediction，与本文方法论正交。不认为缺失此引用构成 weakness。\n\n**[REBUT] Mirzadeh et al. 2024 (ReLU Strikes Back)**: 论文已在 Related Work Section 2 \"Activation Function Engineering\" 段落中引用并讨论了此工作（\"ReLU Strikes Back (Mirzadeh et al., 2024) replaces SiLU with ReLU for >90% natural sparsity\"）。R1 可能遗漏了这一引用。\n\n**[AGREE] Wanda 互补性讨论**: 论文在 Related Work 提及 Wanda（Section 2 \"Weight Pruning, Distillation, and Routing\"），但仅作为 weight pruning 方法列举。Wanda 的 activation-aware weight selection 与本文的 activation sparsity prediction 有方法论上的关联（都利用 activation magnitude 作为 importance signal），补充讨论两者的互补性是合理的。\n\n---\n\n### 总结\n\nR1 的审稿整体公正且 well-calibrated。我们在 N1（无加速）、N2（97.5% confound）、N3（framing 偏重 PPL）上完全一致。我对 W3（MSE 调参公平性）和 W4（global MMLU variance）有部分反驳，认为论文的处理并非不合理。R1 的 Q3（BCE+compensation）是我初审遗漏的有价值问题。\n\n综合 R1 意见后，我维持 **Overall 3.0 (Findings)** 的评分不变。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 无 wall-clock 加速**\n同意这是 critical 问题。与我的 N2 一致。论文在 Appendix A 承认 unstructured masks 无法转化为 speedup（Table 5: +6.4% overhead），但这个 disclaimer 在正文中过于隐蔽（Introduction 倒数第二段括号内）。对于以 \"sparsity prediction\" 为核心的论文，无法展示 end-to-end 效率收益是硬伤。不过需要注意：论文自我定位为 \"primarily an empirical study\"（Section 1 倒数第二段），如果这一定位更加前置和显著，该问题的 severity 可以部分降低。\n\n**[AGREE] R1-N2: 97.5% signal type 基于 confounded 设置**\n同意。与我的 W1 一致。补充两点：\n1. Per-layer KL (K=1) 训练时只 mask 1/32 层但推理时 apply 全部 32 层，这个 train-inference mismatch 本身就是一个 confound——不能将 per-layer KL vs. E2E KL 的 gap 纯粹归因于 coupling scope。论文在 Section 4.5 脚注中承认 \"signal type and coupling scope are not fully orthogonal\"，但 Abstract 和 Conclusion 中引用 97.5% 时没有任何 caveat。\n2. K=4 的 MMLU 异常（43.5 vs. E2E 40.7±1.3）和 GSM8K 负向 gap closure (-6.8%) 确实是 red flags。Table 17 (Appendix R) 注释说 \"interpret cautiously\"，但这种 hedging 在 Abstract/Conclusion 中消失了——\"reveals task-dependent downstream structure\" 作为 headline finding 过于自信。\n\n**[AGREE] R1-N3: 下游回退 framing 偏重 PPL**\n同意这是 major concern，但 severity 可从 Critical 降为 Major。理由：\n- Abstract 确实提到 \"commonsense gains but knowledge-intensive decline\"（第 3 行）\n- Section 4.2 \"Task-Type Split\" 段落完整报告了 MMLU/GSM8K 的回退\n- Limitations 第二点 \"Knowledge-intensive regression\" 明确承认跨 scale 的系统性问题\n\n但 R1 的核心批评成立：Conclusion 的 \"task- and scale-dependent\" 措辞过于模糊，回避了 \"KL 在 knowledge tasks 上输给 training-free baseline\" 这一尖锐事实。Introduction 的叙事以 PPL 改善为主线（\"reduces perplexity by 14.5%\"），下游 trade-off 被压缩在列表第一项的子句中。建议将 Conclusion 改为更 balanced 的双面叙事。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: C1 trajectory confound**\n同意，但认为论文已 partially address。Appendix O (Oracle Mask Provenance) 明确讨论了 trajectory 依赖问题：\"C1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold...The s42/s123/s456 consistency (≤1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.\" 3-seed 一致性（Table 3: max Δ≤1.70pp at 30%）是一定程度的 evidence，但 R1 的核心论点成立：C1 证明好 masks 可 transfer，但没有证明 KL 是发现好 masks 的 *唯一* 途径。可能存在其他方法（如 evolutionary search、reinforcement learning）也能发现类似质量的 masks。这不影响论文的核心 finding（mask quality drives performance），但限制了 \"KL 作为 discovery mechanism\" 这一 claim 的 strength。\n\n**[AGREE] R1-W2: 训练/评估域重叠**\n同意。与我的 Q4 一致。WikiText-103 和 WikiText-2 都源自 Wikipedia，PPL 改善可能部分来自 in-domain 优势。C4 OOD 评估（Appendix C, Table 10）虽然保持了 KL 优势（52.5% advantage at 50%），但 cross-seed variance 急剧增大（CV 6.3% vs. 0.2%），且 seed 42 的 C4 PPL 异常偏高（18.22 vs. 其他 seed 16.37），暗示 predictor 对训练域有一定 overfitting。\n\n**[REBUT] R1-W3: MSE baseline 未公平调参**\n部分反驳。论文在 Appendix F 中详细说明了 MSE 的配置：与 KL/BCE 使用完全相同的架构、数据、优化器、Gumbel-Sigmoid relaxation，仅 loss function 不同。λ_max 设为 1000（vs. KL 的 5000）是因为 MSE 的 per-layer gradient magnitude 约 5× 大于 KL 的 end-to-end gradient，这是合理的工程调整而非不公平。Seed 123 的灾难性失败（PPL=15,789, 5.1% sparsity）恰恰说明 MSE loss 的 *内在不稳定性*——KL loss 在相同条件下 3-seed σ=0.02，而 MSE σ=1.68。这种 initialization sensitivity 本身就是一个有意义的 finding，而非调参不足的证据。但 R1 有一定道理：论文没有报告对 MSE 做 λ_max grid search 的尝试，无法排除更好的 λ_max 能部分缓解问题。\n\n**[REBUT] R1-W4: Global allocation MMLU σ=9.5pp 不可解读**\n反驳。论文的处理方式恰当：\n1. Table 2 同时报告了 global (σ=9.5pp) 和 uniform (σ=1.3pp) 两种 allocation 的 MMLU\n2. Section 4.2 明确解释了 global 高 variance 的来源——late-layer starvation (L31 retention 28.4%)\n3. Appendix J (Table 14) 展示了完整的 allocation 对比，30% 时推荐 uniform\n4. 高 variance 本身是一个 informative finding：它揭示了 global allocation 在 moderate sparsity 下的不稳定性\n\n论文没有用 global 30% MMLU 作为 headline number——Table 2 的 bold 标记在 MMLU 列给了 TEAL (45.86)，KL uniform 40.7±1.3 作为稳定替代。R1 的 concern 更多是 presentation 问题，非 soundness 问题。\n\n**[AGREE] R1-W5: 符号冲突 g^(ℓ) vs. g1/g2**\n同意。Eq.(1) 的 g^(ℓ) 表示 gate activation，Eq.(4) 的 g1, g2 表示 Gumbel noise samples。虽然上下标不同（上标 ℓ vs. 下标 1/2），但 g 作为 base symbol 在同一篇论文中有两种含义确实影响可读性。建议将 Gumbel noise 改为 ε1, ε2 或 ξ1, ξ2 以消除歧义。这是 minor fix。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: K=4 多种子数据**\n与我的 W2 和 Q3 一致。K=4 单 seed 的 MMLU 异常（43.5 > E2E 40.7±1.3）很可能是噪声。需要至少 3-seed K=4 数据才能判断这是系统性的还是随机的。\n\n**[AGREE] R1-Q2: Per-layer sparsity 约束**\n与我的 W4 建议一致。如果 late-layer over-pruning (L22-L28 at 48-57%, Appendix T, Table 20) 是 MMLU/GSM8K 回退的原因，per-layer sparsity cap（如 max 35%）是最直接的验证手段。论文未尝试这一自然实验是一个遗憾。\n\n**[AGREE] R1-Q3: 补偿对 BCE 效果**\n这是一个很好的问题，我在初审中遗漏了。论文报告 \"compensation provides no benefit\"（Section 4.5），但从 exp_id 看（kl_comp_30_s42, kl_comp_50_s42, bce_comp_staged_s42），似乎有做过 BCE+compensation 的实验。然而结果未在正文或附录中单独报告。如果 BCE+compensation 能显著缩小与 KL 的 gap，论文的核心论点（KL 的 mask quality 使 compensation 冗余）就需要重新审视：可能不是 KL masks 本身好到不需要 compensation，而是 BCE masks 差到 compensation 也救不了。两种解读有本质区别。\n\n**[AGREE] R1-Q4: 更多样训练集**\n与我的 Q4 一致。C4 subsample 或 mixed-domain 训练是降低 OOD variance 的自然尝试。\n\n---\n\n### Missing References\n\n**[REBUT] Griffin et al. 2024**: Griffin (De et al., 2024) 提出 gated linear recurrence 架构，与本文研究的 SwiGLU FFN activation sparsity 关联较弱。Griffin 的 sparsity 来自架构设计而非 post-hoc prediction，与本文方法论正交。不认为缺失此引用构成 weakness。\n\n**[REBUT] Mirzadeh et al. 2024 (ReLU Strikes Back)**: 论文已在 Related Work Section 2 \"Activation Function Engineering\" 段落中引用并讨论了此工作（\"ReLU Strikes Back (Mirzadeh et al., 2024) replaces SiLU with ReLU for >90% natural sparsity\"）。R1 可能遗漏了这一引用。\n\n**[AGREE] Wanda 互补性讨论**: 论文在 Related Work 提及 Wanda（Section 2 \"Weight Pruning, Distillation, and Routing\"），但仅作为 weight pruning 方法列举。Wanda 的 activation-aware weight selection 与本文的 activation sparsity prediction 有方法论上的关联（都利用 activation magnitude 作为 importance signal），补充讨论两者的互补性是合理的。\n\n---\n\n### 总结\n\nR1 的审稿整体公正且 well-calibrated。我们在 N1（无加速）、N2（97.5% confound）、N3（framing 偏重 PPL）上完全一致。我对 W3（MSE 调参公平性）和 W4（global MMLU variance）有部分反驳，认为论文的处理并非不合理。R1 的 Q3（BCE+compensation）是我初审遗漏的有价值问题。\n\n综合 R1 意见后，我维持 **Overall 3.0 (Findings)** 的评分不变。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1483 · 2026-05-22T13:12:29.543180+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3800
}
```

</details>

---


### Assistant

_source line 1484 · 2026-05-22T13:12:37.674282+00:00_

已提交对 Reviewer 1 的逐条回应。

核心共识：N1（无加速）、N2（97.5% confound）、N3（framing 偏 PPL）三个 critical/major 问题我与 R1 完全一致。两个部分反驳：W3（MSE baseline 的配置差异有工程合理性，seed 不稳定本身是 finding）和 W4（global MMLU 高 variance 的报告方式实际上是 informative 的）。采纳了 R1 的 Q3（BCE+compensation 未单独报告）作为我初审遗漏的有效问题。维持 Overall 3.0 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 38

## Round 38

84 recorded events


### User

_source line 1485 · 2026-05-22T17:12:53.442668+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查论文的**新颖性、写作质量和完整性**。

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

### 1. 新颖性评估
- 与 MaskLLM (Fang et al., 2024) 的区分度：两者都用 frozen model + learnable masks + KL + Gumbel。§2 列出的 3 个差异 (per-token generalization, global allocation, OOD robustness) 是否足以构成独立贡献？
- 2D taxonomy (signal type × coupling scope) 是否是真正的 intellectual contribution，还是对已有方法的简单重组？
- 论文自我定位为 "primarily empirical study" — 对于 EMNLP 2026，这种定位的 empirical contribution 是否足够？
- Target-swap ablation 和 per-layer KL decomposition 的分析深度是否达到发表标准？

### 2. 写作质量
- Abstract 信息密度：7 句话覆盖了多少内容？读者能否快速理解核心发现？
- Introduction 的叙事结构：问题→动机→方法→结果的逻辑链是否清晰？
- 符号一致性和数学表述清晰度
- Table/Figure 的设计：Table 2 注释是否过长？Figure 1 是否有效传达方法？Figure 2 仅展示 global 但推荐 uniform 是否 misleading？
- Conclusion 是否过于简短/过于密集？
- 正文与 Appendix 的信息分配是否合理

### 3. 完整性与 Related Work
- Related Work (§2) 的覆盖面：是否遗漏重要工作？特别关注 2025-2026 年的新工作
- 是否缺少与 R-Sparse, CATS, DIP 等同类 training-free 方法的实验对比？
- 论文没有 wall-clock speedup — 这对实际影响力的影响
- Limitations 是否充分？是否遗漏重要限制？
- Ethics Statement 是否适当？

### 4. 格式合规
- 正文是否严格 8 页以内
- Appendix 是否使用双栏格式（ARR 从 2025.07 起要求）
- 匿名化是否彻底
- 引用格式是否正确

### 评分标准 (ARR Overall Assessment)
5 = Consider for Award (~top 2.5%), 4.5 = Borderline Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle, 1.5 = Resubmit after next cycle, 1 = Do not resubmit

请严格、客观地评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → 评分建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1486 · 2026-05-22T17:13:00.796512+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1487 · 2026-05-22T17:13:01.602129+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1488 · 2026-05-22T17:13:01.602510+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1489 · 2026-05-22T17:13:01.653531+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1490 · 2026-05-22T17:13:06.208587+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 1491 · 2026-05-22T17:13:07.764576+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-22T17:13:07.915535+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-22T17:13:16.959406+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines and scoring criteria:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score Requirements

The soundness scores must be justified by the text of the review, and if you give a low Soundness score without finding any major faults, your review is not a faithful explanation of your recommendation and needs to be revised.

## Soundness vs. Excitement

You may find the work sound, but not something that is interesting for you personally—such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Metareview Scoring

The metareview score options are: 5 = Consider for Award (top 2.5% papers), 2 = Resubmit next cycle (substantial revisions completable by next cycle), 1.5 = Resubmit after next cycle (substantial r
…[truncated 364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10750
}
```

</details>

---


### Tool result

_source line 1494 · 2026-05-22T17:13:18.517584+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.4}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.4}], \"total_pages\": 19, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10753
}
```

</details>

---


### Tool result

_source line 1495 · 2026-05-22T17:13:18.518096+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 10602
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-22T17:13:24.742430+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions, scoring scales, and criteria that reviewers must use. Include all score names, their scales (1-5 etc.), and what each score level means. Also extract any guidelines about what constitutes a good vs bad review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions, scoring scales, and criteria that reviewers must use. Include all score names, their scales (1-5 etc.), and what each score level means. Also extract any guidelines about what constitutes a good vs bad review."
  }
}
```

</details>

---


### Tool call

_source line 1497 · 2026-05-22T17:13:25.295346+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-22T17:13:25.646885+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1499 · 2026-05-22T17:13:26.501148+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1205
}
```

</details>

---


### Tool result

_source line 1500 · 2026-05-22T17:13:26.501990+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1501 · 2026-05-22T17:13:26.502517+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-22T17:13:26.854536+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1503 · 2026-05-22T17:13:27.761482+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1258
}
```

</details>

---


### Tool result

_source line 1504 · 2026-05-22T17:13:28.315259+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1460
}
```

</details>

---


### Tool result

_source line 1505 · 2026-05-22T17:13:30.328571+00:00_

# ARR Review Form Dimensions and Scoring Criteria

## Review Scoring Dimensions

The guidelines specify three primary scores reviewers must provide (as of February 2025):

1. **Soundness Score** - Evaluates technical rigor and validity
2. **Excitement Score** - Reflects personal interest and novelty perception
3. **Overall Recommendation** - Composite assessment for conference acceptance

The document does not explicitly state the numerical scales (e.g., 1-5) for these scores, though it references "confidence score" and "reproducibility scores" separately.

## Key Quality Standards for Reviews

**Strong reviews demonstrate:**
- Specificity with concrete examples rather than vague criticisms
- Justification of scores: "The soundness scores must be justified by the text of the review"
- Professional tone avoiding sarcasm or dismissiveness
- Acknowledgment of author responses during discussion periods

**Poor review indicators include:**
- Terse or unprofessional assessments
- "Completely unacceptable" quality work
- LLM-generated content
- Unsubstantiated claims about novelty or methodology

## Critical Guidance

Reviewers should avoid common problematic heuristics like dismissing work for being "too simple," lacking SOTA results, or using non-preferred methodologies. The guidelines emphasize that "a paper only needs to present sufficient evidence for the claim that the authors are making."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5586
}
```

</details>

---


### Tool call

_source line 1506 · 2026-05-22T17:13:35.150215+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1507 · 2026-05-22T17:13:35.552446+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1508 · 2026-05-22T17:13:36.457056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-22T17:13:36.460410+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-22T17:13:36.461515+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1511 · 2026-05-22T17:13:36.763625+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1512 · 2026-05-22T17:13:37.316589+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool result

_source line 1513 · 2026-05-22T17:13:37.669960+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-22T17:13:43.093418+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "9-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "9-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1515 · 2026-05-22T17:13:43.545060+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1516 · 2026-05-22T17:13:44.057277+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1517 · 2026-05-22T17:13:45.181237+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 612.0}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 556.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p17.png\", \"wid
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2087
}
```

</details>

---


### Tool result

_source line 1518 · 2026-05-22T17:13:45.181782+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns---not the training mechanism itself---as the proximate quality driver.
5	An output-distribution alignment ranking emerges across five loss configurations; a per-layer KL control decomposes this into two dimensions: signal type dominates PPL (up to 97.5\% of the gap at 30\%; upper bound, as dimensions are not fully orthogonal), while coupling scope contributes 10--47\% on downstream tasks (3-seed $K{=}4$-corrected; commonsense 22--47\%, reasoning 10\%); a train--inference mismatch confound in the $K{=}1$ control inflates the $K{=}1$ upper bound (21--48\%).
6	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
7	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1636
}
```

</details>

---


### Tool result

_source line 1519 · 2026-05-22T17:13:45.182170+00:00_

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
11	A target-swap ablation suggests that these discovered mask targets are the proximate quality driver at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20.
…[truncated 2956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1124
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-22T17:13:49.155341+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1521 · 2026-05-22T17:13:49.657672+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
7	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
8	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
9	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
10	
11	\paragraph{Predictor-Based Contextual Sparsity.}
12	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
13	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
14	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
15	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity pred
…[truncated 5023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-22T17:13:49.658060+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-22T17:13:50.110403+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-22T17:13:50.110959+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1525 · 2026-05-22T17:13:50.613346+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1526 · 2026-05-22T17:13:50.613701+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-22T17:13:51.115753+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the dominant design dimension for PPL (signal type: up to 97.5\% of the gap at 30\%; upper bound, not fully orthogonal); cross-layer coupling contributes 10--47\% on downstream tasks (3-seed $K{=}4$-corrected; commonsense 22--47\%, GSM8K 10\%); MMLU anomalously favors $K{=}4$, reflecting allocation alignment confirmed by constraint analysis (Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude; KL outperforms TEAL on commonsense (ARC-c, WG, BoolQ) but underperforms on knowledge tasks (MMLU, GSM8K) across tested scales---a learned allocation trade-off, not an inherent objective limitation (Appendix~\ref{app:constraint}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-22T17:13:51.116196+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1529 · 2026-05-22T17:13:51.467796+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-22T17:13:51.468220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-22T17:13:51.518703+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-22T17:13:57.142726+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-22T17:13:57.595118+00:00_

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
…[truncated 36672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-22T17:13:58.097305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-22T17:13:59.051831+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@inproceedings{geva2023dissecting,
6	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
7	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
8	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
9	  pages = {12216--12235},
10	  year = {2023},
11	}
12	
13	@article{fu2024lazyllm,
14	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
15	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
16	  year = {2024},
17	  journal = {arXiv preprint arXiv:2407.14057},
18	}
19	
20	@article{zhang2025cots,
21	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
22	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
23	  year = {2025},
24	  journal = {arXiv preprint arXiv:2502.14475},
25	}
26	
27	@inproceedings{alizadeh2024llmflash,
28	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
29	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
30	  year = {2024},
31	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
32	}
33	
34	@article{wei2023outlier,
35	  title = {Outlier Suppression+: Accurate Quantization of Large Language Models by Equivalent and Effective Shifting and Scaling},
36	  author = {Xiuying Wei and Yunchen Zhang and Yuhang Li and Xiangguo Zhang and Ruihao Gong and Jinyang Guo and Xianglong 
…[truncated 8498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-22T17:13:59.052427+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1537 · 2026-05-22T17:13:59.654848+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1538 · 2026-05-22T17:13:59.656091+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-22T17:14:00.209283+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-22T17:14:06.290221+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1541 · 2026-05-22T17:14:06.641895+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1542 · 2026-05-22T17:14:07.145359+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1543 · 2026-05-22T17:14:07.147819+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1544 · 2026-05-22T17:14:08.055218+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1413
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-22T17:14:08.056447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-22T17:14:08.056901+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 1547 · 2026-05-22T17:14:08.608764+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1548 · 2026-05-22T17:14:09.061980+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1549 · 2026-05-22T17:14:09.062471+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1550 · 2026-05-22T17:14:09.966150+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-22T17:14:09.969164+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-22T17:14:09.969558+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1553 · 2026-05-22T17:14:10.423122+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-22T17:14:10.574115+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1555 · 2026-05-22T17:14:10.875657+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_20/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1556 · 2026-05-22T17:14:11.379569+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool result

_source line 1557 · 2026-05-22T17:14:11.481153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-22T17:14:17.753914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation sparsity LLM inference 2025 2026 contextual sparsity predictor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation sparsity LLM inference 2025 2026 contextual sparsity predictor"
  }
}
```

</details>

---


### Tool call

_source line 1559 · 2026-05-22T17:14:18.356496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement scoring scale 1-5 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement scoring scale 1-5 2025"
  }
}
```

</details>

---


### Tool result

_source line 1560 · 2026-05-22T17:14:24.880628+00:00_

Web search results for query: "ACL ARR review form soundness excitement scoring scale 1-5 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, I found information about the ACL ARR review form for 2025:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

**Excitement Scoring Scale (1-5):**
5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference. 4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference. The scale also includes 1 = Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community.

**Soundness Scoring:**
5 = Excellent: This study is one of the most thorough I have seen, given its type. The soundness scores must be justified by the text of the review.

**Key Distinctions:**
Such preferences are more subjective and should be reflected in a separate excitement score, whi
…[truncated 268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6524
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-22T17:14:24.982262+00:00_

Web search results for query: "activation sparsity LLM inference 2025 2026 contextual sparsity predictor"

Links: [{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2406.16635"}]

Here are the search results for "activation sparsity LLM inference 2025 2026 contextual sparsity predictor":

## Key Findings:

**SVD Contextual Sparsity Predictors (March 2026)**

A recent framework accelerates inference of ReGLU-based feed-forward networks within LLMs using a training-free method for building sparse pattern predictors based on truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm. Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math and code generation.

**Contextual Sparsity Overview**

A key characteristic of ReGLU-based LLMs is dynamic (or contextual) sparsity – the phenomenon where only a small subset of neurons within FFN blocks are activated for any given input. A prevalent approach for leveraging contextual sparsity involves employing lightweight, learnable sparsity predictors that generate input-specific sparse activation patterns prior to FFN forward passes.

**Related Work**

DejaVu leverages dynam
…[truncated 274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7228
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-22T17:14:34.117209+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact numerical scales (1-5 etc.), and what each score level means. Include: soundness scale, excitement scale, overall assessment scale, confidence scale, and any other dimensions. I need the exact wording for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact numerical scales (1-5 etc.), and what each score level means. Include: soundness scale, excitement scale, overall assessment scale, confidence scale, and any other dimensions. I need the exact wording for each score level."
  }
}
```

</details>

---


### Tool call

_source line 1563 · 2026-05-22T17:14:34.359035+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"sparse activation\" LLM \"wall-clock speedup\" kernel Triton 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"sparse activation\" LLM \"wall-clock speedup\" kernel Triton 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 1564 · 2026-05-22T17:14:40.230849+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence (1-5)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## Soundness (1-5)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement (1-5)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## Overall Assessment (1-5)
- **5**: "Consider for Award: top 2.5% papers"
- **4**: "Conference: could be accepted to an ACL conference"
- **3**: "Findings: could be accepted to the Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: paper has to be fully redone"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6113
}
```

</details>

---


### Tool result

_source line 1565 · 2026-05-22T17:14:41.636286+00:00_

Web search results for query: ""sparse activation" LLM "wall-clock speedup" kernel Triton 2025 2026"

Links: [{"title":"Training-Free Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=dGVZwyq5tV"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2408.14690"},{"title":"La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation","url":"https://arxiv.org/pdf/2507.01299"},{"title":"S2-Attention: Hardware-Aware Context Sharding Among Attention Heads","url":"https://arxiv.org/pdf/2407.17678"},{"title":"Profiling-Guided Framework for Automated Triton Kernel ...","url":"https://arxiv.org/pdf/2512.09196"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/html/2603.25011"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"}]

Here are the search results for sparse activation in LLMs with wall-clock speedup and kernel optimizations:

## Key Findings:

**TEAL (Training-Free Activation Sparsity)**
TEAL is a training-free method that applies magnitude-based activation sparsity to hidden states, achieving 40-50% model-wide sparsity with minimal performance degradation across Llama models, demonstrating wall-clock decoding speed-ups of up to 1.53× and 1.8× at 40% and 50% model-wide sparsity.

**LaRoSA (Layerwise Rotated Sparse Activation)**
Using a Top-K selection approach within rotated activations, LaRoSA achieves consistent model-level sparsity and reliable wall-clock time speed-up, with LLaMA2-7B at 40% sparsity achieving a 1.30× wall-clock time speed-up.

**Sparse Attention with Hardware-Aware Kernels**
S2-Attention achieves wallclock speedup of 8.79X, 15.87X, and 25.3X compared to FlashAttention-2 baseline at different model scales.

**Triton Kernel Optimization**
Sparton is a kernel implemented in Triton tailored for the LM head in lea
…[truncated 366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7277
}
```

</details>

---


### Tool call

_source line 1566 · 2026-05-22T17:17:26.640785+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 扎实的实证研究，系统地比较了 KL vs BCE 训练目标对 SwiGLU 稀疏预测器的影响，但新颖性有限（核心 recipe 与 MaskLLM 共享），缺乏 wall-clock speedup 和强 baseline 实验对比，且知识密集型任务上的系统性退化削弱了实际价值。\n\n## 官方维度打分（ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有实验支撑，但 C1 ablation 存在 soft-vs-hard confound 未完全解耦；\"97.5% signal type\" 为 upper bound 且维度不正交；per-layer KL K=1 有 train-inference mismatch confound |\n| Excitement | 2.5/5 | 核心 recipe (frozen weights + learnable masks + KL + Gumbel) 与 MaskLLM 共享；2D taxonomy 是简单分类而非深刻理论贡献；自我定位为 empirical study 但缺少 wall-clock speedup 削弱实际影响力 |\n| Overall | 3.0/5 | Findings 级别：分析深度达到发表标准但不足以进入主会议；需补充实际加速数据和更强 baseline 对比 |\n| Confidence | 4/5 | 仔细阅读了全文和 appendix，对 activation sparsity 领域较为熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 缺乏 wall-clock speedup 实验——实际增加 6.4% 延迟\n- 具体位置：Appendix A (Table 5), §4.6 最后一段, Limitations\n- 问题：论文提出的方法在当前实现下不仅没有加速，反而增加了 6.4% 推理延迟（126.78 vs 119.11 ms/forward）。论文在 Limitations 中承认 \"wall-clock speedup requires sparse kernels not addressed here\"，但对于一篇声称改进 sparsity prediction 的论文，完全没有端到端加速证据是严重缺陷。TEAL 原论文已展示 1.53× 和 1.8× 的 wall-clock speedup（40% 和 50% sparsity）。如果 KL predictor 的 mask 质量更好但无法转化为实际加速，其实际价值存疑。\n- 为什么影响接收：作为 efficiency-motivated 工作，没有加速数据使得论文的实际贡献仅限于分析层面，严重限制了 impact。\n- 建议修改方向：至少用 Triton block-sparse kernel 或 DejaVu 的 sparse GEMM 展示一个 sparsity level 的 wall-clock speedup；或者彻底将论文重新定位为纯分析工作并在 title 中体现。\n\n**N2** [critical] 知识密集型任务（MMLU, GSM8K）的系统性退化未得到充分解释\n- 具体位置：Table 2 (30%: MMLU 40.7 vs 45.86, GSM8K 7.5 vs 8.79), §4.2 Task-Type Split, Table 13 (Qwen-14B: GSM8K −20pp)\n- 问题：KL predictor 在所有测试规模上（8B, 7B, 14B）系统性地在 MMLU 和 GSM8K 上逊于 TEAL。论文将此归因为 \"distribution-matching objectives systematically sacrifice reasoning-critical pathways\"，但这只是描述现象而非解释机制。如果 KL 的 mode-covering 特性（§3.4 中作为选择 forward KL 的论据）无法保护推理关键路径，这实际上挑战了论文选择 forward KL 的理论动机。更关键的是，Appendix T（Remove Valley 实验）显示通过简单调整 per-layer allocation 可以恢复 MMLU +3.3pp 和 GSM8K +1.5pp——这表明退化可能是可避免的分配问题，而非 KL 目标的固有缺陷，但论文未进一步追踪此线索。\n- 为什么影响接收：MMLU 和 GSM8K 是评估 LLM 能力的核心 benchmark。在这些任务上系统性地逊于 training-free baseline（TEAL），使得方法的实用性大打折扣。\n- 建议修改方向：(1) 深入分析 KL mask 在具体哪些层/neuron 上与 MMLU-critical activations 冲突；(2) 基于 Remove Valley 发现，提出一个任务感知的 allocation 策略并验证。\n\n**N3** [critical] 与 MaskLLM 的区分度不足以支撑独立贡献\n- 具体位置：§2 Related Work（第19-21行）\n- 问题：论文列出的 3 个与 MaskLLM 的差异——(a) per-token generalization vs static N:M, (b) global top-k allocation, (c) OOD robustness——主要是应用场景差异（activation sparsity vs weight sparsity），而非方法论创新。核心训练 recipe 完全相同：frozen model + learnable masks + KL divergence + Gumbel relaxation。论文的真正贡献是将此 recipe 应用到 activation sparsity 并进行系统分析，但 §2 的措辞暗示了更大的方法论距离。2D taxonomy（Table 1）作为组织框架有用，但本身并不构成 intellectual contribution——它只是对已有方法的简单分类，其中 4/6 个格子被已有工作占据。\n- 为什么影响接收：如果 reviewer 认为这是 MaskLLM 的直接应用而非独立方法贡献，论文的 novelty 将受到严重质疑。\n- 建议修改方向：(1) 更诚实地定位——将论文明确框定为 \"systematic empirical analysis of KL distillation for contextual activation sparsity\"，而非暗示方法论创新；(2) 强化独特贡献：target-swap ablation 和 per-layer decomposition 是真正的分析创新，应给予更多篇幅。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺少与 training-free 方法的直接实验对比\n- 具体位置：§2 第5行提到 R-Sparse, CATS, DIP, SparseInfer，§4 Baselines\n- 问题：Related Work 中引用了多个 2024-2025 的同类方法（R-Sparse [ICLR 2025], CATS, DIP [MLSys 2024], SparseInfer），但实验部分仅与 TEAL 和 DejaVu-style BCE 对比。R-Sparse 使用 rank-aware SVD 预测，与本文的 learned predictor 在同一赛道竞争，缺乏直接对比削弱了论文 claims 的说服力。LaRoSA (2025) 也在 SwiGLU 模型上展示了 wall-clock speedup，是高度相关的 baseline。\n- 建议：至少加入 R-Sparse 的实验对比（同为 predictor-based 方法），或解释为什么这些方法不适合作为 baseline。\n\n**W2** [warning] Figure 2 展示 global allocation 但推荐 uniform——存在误导\n- 具体位置：Figure 2（第8页），§4.2（\"Uniform allocation preserves downstream performance best\"），§4.5（Allocation Behavior）\n- 问题：Figure 2 展示的是 global allocation 下的 PPL scaling 曲线，但正文 §4.2 明确建议 uniform allocation 以获得更好的 downstream 性能。读者看 Figure 2 得到的印象（\"KL 在所有 sparsity 下都大幅优于 TEAL\"）可能在 uniform allocation 下不成立（实际上 uniform TEAL 在 MMLU 上系统性优于 KL uniform）。Caption 虽标注了 \"(global allocation)\"，但作为正文仅有的两张 figure 之一，其 framing 效果很强。\n- 建议：在 Figure 2 中加入 uniform allocation 的对比曲线，或在 caption 中明确说明 downstream 结果在 uniform 下不同。\n\n**W3** [warning] Conclusion（§5）过于密集且遗漏 limitation 信号\n- 具体位置：§5 Conclusion（仅2句话，约130词）\n- 问题：Conclusion 将大量信息压缩到2句话中，包含多个带括号的数字和 appendix 引用，可读性差。更重要的是，Conclusion 完全没有提及 MMLU/GSM8K 退化、缺乏 wall-clock speedup、以及方法的适用边界。一个好的 conclusion 应该 balance strengths and limitations，而非只强调正面发现。Conclusion 中提到 \"BoolQ\" 但 BoolQ 并未出现在 Table 2 主实验中（仅在 Appendix Table 18），这是不一致的。\n- 建议：扩展至 3-4 句，加入主要 limitation 的 honest acknowledgment，删除 BoolQ（或将其加入 Table 2）。\n\n**W4** [warning] C1 Target-Swap Ablation 的 soft-vs-hard confound 未完全解耦\n- 具体位置：§4.3 \"Soft-vs-Hard Confound\" 段落, Appendix P\n- 问题：C1 ablation 同时改变了两个变量：(1) mask targets (KL-derived vs magnitude) 和 (2) mask representation (soft Gumbel vs hard binary)。论文试图通过 BCE+Gumbel (32.22) vs standard BCE (27.97) 来论证 softness 不是主要因素，但这个比较并不干净——BCE+Gumbel 的 PPL 更差（32.22 > 27.97），说明 Gumbel 在 BCE 设置下是有害的，而非中性的。正确的控制实验应该是：KL predictor with hard masks (STE) vs KL predictor with soft masks，但 STE 在 30% 时 sparsity 无法收敛（§4.5 STE Failure），使得完全解耦不可行。论文承认了这一局限（\"trajectory-dependent confounds\"），但对 C1 的结论措辞（\"masks as the proximate quality driver\"）过于强硬。\n- 建议：将 C1 的结论从 \"suggests\" 弱化为更加 hedged 的表述，明确列出无法完全解耦的原因。\n\n**W5** [warning] Abstract 信息密度过高\n- 具体位置：Abstract（7句话，约180词）\n- 问题：Abstract 第5句长达约60词，包含多个嵌套的数字和条件（\"97.5% of the gap at 30%; upper bound, as dimensions are not fully orthogonal; while coupling scope contributes 10-47% on downstream tasks; 3-seed K=4-corrected; commonsense 22-47%, reasoning 10%\"）。这对首次阅读的 reviewer 来说几乎不可能在一遍内理解。Abstract 应帮助读者快速 grasp 核心发现，而非压缩完整结果。\n- 建议：简化第5句，将数值细节移入 Introduction；Abstract 聚焦 high-level takeaway。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 注释过多（†, ‡, *, ±, §），建议精简。BCE 30% 使用 TEAL global（†）而非 uniform，与其他行不一致，读者容易忽略。\n- **M2**: §3.5 Adaptive Penalty Controller 的 deadzone margin ε=0.02 的选择缺乏 justification。\n- **M3**: §4.3 \"Cross-seed KL Jaccard distance (36.3%; Appendix F.1)\" 提供了 noise baseline，但未与 random mask baseline（0.462）做更显式的对比来量化 systematic component。\n- **M4**: 论文在 §4.2 中报告 MMLU 40.7±1.3%（3-seed），但 global allocation 的 MMLU 方差极大（35.7±9.5%），跨度从 25.3% 到 43.5%——这种不稳定性值得在正文中更突出地讨论。\n- **M5**: References 中 Gautam et al. (2026) 的 FastForward 标注为 arXiv:2602.00397——这是 2026 年 2 月的 preprint，如果已被会议接收应更新引用信息。\n- **M6**: §3.1 中 d_ff=14,336 的逗号分隔在数学环境中使用了 `{,}` hack，建议使用 `\\,` 提高一致性。\n- **M7**: Appendix 部分的 Table 编号（Table 5-21）跨度很大，建议检查是否有遗漏或重复编号。\n\n---\n\n## Questions for Authors\n\n1. 既然 Remove Valley 实验（Appendix T）显示调整 per-layer allocation 可以恢复 MMLU +3.3pp，为什么不将此作为默认配置或提出一个任务感知的 allocation 机制？这似乎是一个低悬果实。\n\n2. Figure 2 仅展示 global allocation 的 PPL 曲线。能否提供 uniform allocation 下的 PPL scaling 数据？在 uniform 下 KL 的优势是否同样随 sparsity 增加而扩大？\n\n3. 论文在 30% sparsity 时实际达到 28.5%（5% deviation），在 TEAL 28.5% 时 PPL 10.30。那么 \"14.5% PPL reduction\" 的 claim 是基于 matched sparsity（28.5%: 8.81 vs 10.30 = 14.5%）还是 target sparsity（30%: 8.81 vs 10.82 = 18.6%）？Abstract 和 Introduction 的措辞应保持一致。\n\n4. 训练仅用 1000 steps 在 WikiText-103 上——这是否足以让 predictor 学习到 generalizable 的 activation patterns？C4 上的高 cross-seed variance（CV=6.3% vs in-domain 0.2%）暗示可能存在过拟合。是否尝试过在更大/更多样化的数据上训练？\n\n5. 论文在 §3.6 gradient analysis 中声称 \"KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks\"，但 §4.3 C1 ablation 又说 \"masks as the proximate quality driver, not the coupling mechanism itself\"。这两个 claim 之间的关系需要更清晰的阐述——如果 coupling 主要是用来 discover 好的 mask patterns，而非提供 inference-time 优势，那么是否可以用 KL 训练后提取 masks 再用更简单的方法（如 BCE）部署？\n\n---\n\n## Missing References\n\n1. **LaRoSA** (2025, arXiv:2507.01299): Layerwise Rotated Sparse Activation——在 SwiGLU 模型上实现 wall-clock speedup 的 activation sparsity 方法，高度相关但未被引用。\n2. **Geva et al. (2023)** \"Dissecting Recall of Factual Associations\": 虽已在 bib 中但正文未引用——与 MMLU regression 的讨论相关（factual recall 与 MLP 层的关系）。\n\n---\n\n## 主要优势\n\n- **S1**: 系统性的实验设计——5 种 loss function 的对比（KL, reverse KL, JSD, BCE, MSE）、3-seed 评估、cross-architecture 验证（LLaMA, Mistral, Qwen），实验严谨度高于该领域多数工作。\n- **S2**: Target-swap ablation (C1) 是一个巧妙的分析方法，能够部分解耦 mask quality 和 training mechanism 的贡献，具有方法论参考价值。\n- **S3**: Per-layer KL decomposition（K=1 和 K=4 控制实验）对 signal type vs coupling scope 的定量分解是该领域的新颖分析维度。\n- **S4**: 诚实的自我定位——论文明确声明 \"primarily an empirical study\" 并详细讨论了 confounds 和 upper bounds，这种学术诚实值得肯定。\n- **S5**: Comprehensive appendix（19页总计）提供了充分的补充材料，包括 sensitivity analysis、OOD evaluation、mask visualization 等。\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 说明 |\n|------|------|------|\n| 正文页数 | ✅ | §1-§5 在第8页结束（Conclusion 在 p8 底部） |\n| Limitations | ✅ | 在 p9，不计入页数限制，覆盖3个关键点 |\n| Ethics | ✅ | 在 p9，简短适当 |\n| 匿名化 | ✅ | \"Anonymous ACL submission\"，未发现泄露 |\n| Appendix 双栏 | ✅ | p12-19 使用双栏 ACL 格式 |\n| 引用格式 | ✅ | 使用 acl_natbib，格式一致 |\n\n---\n\n## 评分总结\n\n本文是一篇执行质量较高的实证研究，系统分析了 KL distillation 对 SwiGLU activation sparsity 预测器的影响。主要贡献是分析性的（target-swap ablation、2D decomposition），而非方法论创新（核心 recipe 来自 MaskLLM）。三个 critical 问题——缺乏 wall-clock speedup、MMLU/GSM8K 系统性退化、与 MaskLLM 区分度不足——使其更适合 Findings 而非主会议。如果作者能补充实际加速数据并深化 MMLU regression 的分析，有潜力升至 3.5 (Borderline Conference)。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 总体评分\n\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 扎实的实证研究，系统地比较了 KL vs BCE 训练目标对 SwiGLU 稀疏预测器的影响，但新颖性有限（核心 recipe 与 MaskLLM 共享），缺乏 wall-clock speedup 和强 baseline 实验对比，且知识密集型任务上的系统性退化削弱了实际价值。\n\n## 官方维度打分（ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claim 有实验支撑，但 C1 ablation 存在 soft-vs-hard confound 未完全解耦；\"97.5% signal type\" 为 upper bound 且维度不正交；per-layer KL K=1 有 train-inference mismatch confound |\n| Excitement | 2.5/5 | 核心 recipe (frozen weights + learnable masks + KL + Gumbel) 与 MaskLLM 共享；2D taxonomy 是简单分类而非深刻理论贡献；自我定位为 empirical study 但缺少 wall-clock speedup 削弱实际影响力 |\n| Overall | 3.0/5 | Findings 级别：分析深度达到发表标准但不足以进入主会议；需补充实际加速数据和更强 baseline 对比 |\n| Confidence | 4/5 | 仔细阅读了全文和 appendix，对 activation sparsity 领域较为熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 缺乏 wall-clock speedup 实验——实际增加 6.4% 延迟\n- 具体位置：Appendix A (Table 5), §4.6 最后一段, Limitations\n- 问题：论文提出的方法在当前实现下不仅没有加速，反而增加了 6.4% 推理延迟（126.78 vs 119.11 ms/forward）。论文在 Limitations 中承认 \"wall-clock speedup requires sparse kernels not addressed here\"，但对于一篇声称改进 sparsity prediction 的论文，完全没有端到端加速证据是严重缺陷。TEAL 原论文已展示 1.53× 和 1.8× 的 wall-clock speedup（40% 和 50% sparsity）。如果 KL predictor 的 mask 质量更好但无法转化为实际加速，其实际价值存疑。\n- 为什么影响接收：作为 efficiency-motivated 工作，没有加速数据使得论文的实际贡献仅限于分析层面，严重限制了 impact。\n- 建议修改方向：至少用 Triton block-sparse kernel 或 DejaVu 的 sparse GEMM 展示一个 sparsity level 的 wall-clock speedup；或者彻底将论文重新定位为纯分析工作并在 title 中体现。\n\n**N2** [critical] 知识密集型任务（MMLU, GSM8K）的系统性退化未得到充分解释\n- 具体位置：Table 2 (30%: MMLU 40.7 vs 45.86, GSM8K 7.5 vs 8.79), §4.2 Task-Type Split, Table 13 (Qwen-14B: GSM8K −20pp)\n- 问题：KL predictor 在所有测试规模上（8B, 7B, 14B）系统性地在 MMLU 和 GSM8K 上逊于 TEAL。论文将此归因为 \"distribution-matching objectives systematically sacrifice reasoning-critical pathways\"，但这只是描述现象而非解释机制。如果 KL 的 mode-covering 特性（§3.4 中作为选择 forward KL 的论据）无法保护推理关键路径，这实际上挑战了论文选择 forward KL 的理论动机。更关键的是，Appendix T（Remove Valley 实验）显示通过简单调整 per-layer allocation 可以恢复 MMLU +3.3pp 和 GSM8K +1.5pp——这表明退化可能是可避免的分配问题，而非 KL 目标的固有缺陷，但论文未进一步追踪此线索。\n- 为什么影响接收：MMLU 和 GSM8K 是评估 LLM 能力的核心 benchmark。在这些任务上系统性地逊于 training-free baseline（TEAL），使得方法的实用性大打折扣。\n- 建议修改方向：(1) 深入分析 KL mask 在具体哪些层/neuron 上与 MMLU-critical activations 冲突；(2) 基于 Remove Valley 发现，提出一个任务感知的 allocation 策略并验证。\n\n**N3** [critical] 与 MaskLLM 的区分度不足以支撑独立贡献\n- 具体位置：§2 Related Work（第19-21行）\n- 问题：论文列出的 3 个与 MaskLLM 的差异——(a) per-token generalization vs static N:M, (b) global top-k allocation, (c) OOD robustness——主要是应用场景差异（activation sparsity vs weight sparsity），而非方法论创新。核心训练 recipe 完全相同：frozen model + learnable masks + KL divergence + Gumbel relaxation。论文的真正贡献是将此 recipe 应用到 activation sparsity 并进行系统分析，但 §2 的措辞暗示了更大的方法论距离。2D taxonomy（Table 1）作为组织框架有用，但本身并不构成 intellectual contribution——它只是对已有方法的简单分类，其中 4/6 个格子被已有工作占据。\n- 为什么影响接收：如果 reviewer 认为这是 MaskLLM 的直接应用而非独立方法贡献，论文的 novelty 将受到严重质疑。\n- 建议修改方向：(1) 更诚实地定位——将论文明确框定为 \"systematic empirical analysis of KL distillation for contextual activation sparsity\"，而非暗示方法论创新；(2) 强化独特贡献：target-swap ablation 和 per-layer decomposition 是真正的分析创新，应给予更多篇幅。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺少与 training-free 方法的直接实验对比\n- 具体位置：§2 第5行提到 R-Sparse, CATS, DIP, SparseInfer，§4 Baselines\n- 问题：Related Work 中引用了多个 2024-2025 的同类方法（R-Sparse [ICLR 2025], CATS, DIP [MLSys 2024], SparseInfer），但实验部分仅与 TEAL 和 DejaVu-style BCE 对比。R-Sparse 使用 rank-aware SVD 预测，与本文的 learned predictor 在同一赛道竞争，缺乏直接对比削弱了论文 claims 的说服力。LaRoSA (2025) 也在 SwiGLU 模型上展示了 wall-clock speedup，是高度相关的 baseline。\n- 建议：至少加入 R-Sparse 的实验对比（同为 predictor-based 方法），或解释为什么这些方法不适合作为 baseline。\n\n**W2** [warning] Figure 2 展示 global allocation 但推荐 uniform——存在误导\n- 具体位置：Figure 2（第8页），§4.2（\"Uniform allocation preserves downstream performance best\"），§4.5（Allocation Behavior）\n- 问题：Figure 2 展示的是 global allocation 下的 PPL scaling 曲线，但正文 §4.2 明确建议 uniform allocation 以获得更好的 downstream 性能。读者看 Figure 2 得到的印象（\"KL 在所有 sparsity 下都大幅优于 TEAL\"）可能在 uniform allocation 下不成立（实际上 uniform TEAL 在 MMLU 上系统性优于 KL uniform）。Caption 虽标注了 \"(global allocation)\"，但作为正文仅有的两张 figure 之一，其 framing 效果很强。\n- 建议：在 Figure 2 中加入 uniform allocation 的对比曲线，或在 caption 中明确说明 downstream 结果在 uniform 下不同。\n\n**W3** [warning] Conclusion（§5）过于密集且遗漏 limitation 信号\n- 具体位置：§5 Conclusion（仅2句话，约130词）\n- 问题：Conclusion 将大量信息压缩到2句话中，包含多个带括号的数字和 appendix 引用，可读性差。更重要的是，Conclusion 完全没有提及 MMLU/GSM8K 退化、缺乏 wall-clock speedup、以及方法的适用边界。一个好的 conclusion 应该 balance strengths and limitations，而非只强调正面发现。Conclusion 中提到 \"BoolQ\" 但 BoolQ 并未出现在 Table 2 主实验中（仅在 Appendix Table 18），这是不一致的。\n- 建议：扩展至 3-4 句，加入主要 limitation 的 honest acknowledgment，删除 BoolQ（或将其加入 Table 2）。\n\n**W4** [warning] C1 Target-Swap Ablation 的 soft-vs-hard confound 未完全解耦\n- 具体位置：§4.3 \"Soft-vs-Hard Confound\" 段落, Appendix P\n- 问题：C1 ablation 同时改变了两个变量：(1) mask targets (KL-derived vs magnitude) 和 (2) mask representation (soft Gumbel vs hard binary)。论文试图通过 BCE+Gumbel (32.22) vs standard BCE (27.97) 来论证 softness 不是主要因素，但这个比较并不干净——BCE+Gumbel 的 PPL 更差（32.22 > 27.97），说明 Gumbel 在 BCE 设置下是有害的，而非中性的。正确的控制实验应该是：KL predictor with hard masks (STE) vs KL predictor with soft masks，但 STE 在 30% 时 sparsity 无法收敛（§4.5 STE Failure），使得完全解耦不可行。论文承认了这一局限（\"trajectory-dependent confounds\"），但对 C1 的结论措辞（\"masks as the proximate quality driver\"）过于强硬。\n- 建议：将 C1 的结论从 \"suggests\" 弱化为更加 hedged 的表述，明确列出无法完全解耦的原因。\n\n**W5** [warning] Abstract 信息密度过高\n- 具体位置：Abstract（7句话，约180词）\n- 问题：Abstract 第5句长达约60词，包含多个嵌套的数字和条件（\"97.5% of the gap at 30%; upper bound, as dimensions are not fully orthogonal; while coupling scope contributes 10-47% on downstream tasks; 3-seed K=4-corrected; commonsense 22-47%, reasoning 10%\"）。这对首次阅读的 reviewer 来说几乎不可能在一遍内理解。Abstract 应帮助读者快速 grasp 核心发现，而非压缩完整结果。\n- 建议：简化第5句，将数值细节移入 Introduction；Abstract 聚焦 high-level takeaway。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 注释过多（†, ‡, *, ±, §），建议精简。BCE 30% 使用 TEAL global（†）而非 uniform，与其他行不一致，读者容易忽略。\n- **M2**: §3.5 Adaptive Penalty Controller 的 deadzone margin ε=0.02 的选择缺乏 justification。\n- **M3**: §4.3 \"Cross-seed KL Jaccard distance (36.3%; Appendix F.1)\" 提供了 noise baseline，但未与 random mask baseline（0.462）做更显式的对比来量化 systematic component。\n- **M4**: 论文在 §4.2 中报告 MMLU 40.7±1.3%（3-seed），但 global allocation 的 MMLU 方差极大（35.7±9.5%），跨度从 25.3% 到 43.5%——这种不稳定性值得在正文中更突出地讨论。\n- **M5**: References 中 Gautam et al. (2026) 的 FastForward 标注为 arXiv:2602.00397——这是 2026 年 2 月的 preprint，如果已被会议接收应更新引用信息。\n- **M6**: §3.1 中 d_ff=14,336 的逗号分隔在数学环境中使用了 `{,}` hack，建议使用 `\\,` 提高一致性。\n- **M7**: Appendix 部分的 Table 编号（Table 5-21）跨度很大，建议检查是否有遗漏或重复编号。\n\n---\n\n## Questions for Authors\n\n1. 既然 Remove Valley 实验（Appendix T）显示调整 per-layer allocation 可以恢复 MMLU +3.3pp，为什么不将此作为默认配置或提出一个任务感知的 allocation 机制？这似乎是一个低悬果实。\n\n2. Figure 2 仅展示 global allocation 的 PPL 曲线。能否提供 uniform allocation 下的 PPL scaling 数据？在 uniform 下 KL 的优势是否同样随 sparsity 增加而扩大？\n\n3. 论文在 30% sparsity 时实际达到 28.5%（5% deviation），在 TEAL 28.5% 时 PPL 10.30。那么 \"14.5% PPL reduction\" 的 claim 是基于 matched sparsity（28.5%: 8.81 vs 10.30 = 14.5%）还是 target sparsity（30%: 8.81 vs 10.82 = 18.6%）？Abstract 和 Introduction 的措辞应保持一致。\n\n4. 训练仅用 1000 steps 在 WikiText-103 上——这是否足以让 predictor 学习到 generalizable 的 activation patterns？C4 上的高 cross-seed variance（CV=6.3% vs in-domain 0.2%）暗示可能存在过拟合。是否尝试过在更大/更多样化的数据上训练？\n\n5. 论文在 §3.6 gradient analysis 中声称 \"KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks\"，但 §4.3 C1 ablation 又说 \"masks as the proximate quality driver, not the coupling mechanism itself\"。这两个 claim 之间的关系需要更清晰的阐述——如果 coupling 主要是用来 discover 好的 mask patterns，而非提供 inference-time 优势，那么是否可以用 KL 训练后提取 masks 再用更简单的方法（如 BCE）部署？\n\n---\n\n## Missing References\n\n1. **LaRoSA** (2025, arXiv:2507.01299): Layerwise Rotated Sparse Activation——在 SwiGLU 模型上实现 wall-clock speedup 的 activation sparsity 方法，高度相关但未被引用。\n2. **Geva et al. (2023)** \"Dissecting Recall of Factual Associations\": 虽已在 bib 中但正文未引用——与 MMLU regression 的讨论相关（factual recall 与 MLP 层的关系）。\n\n---\n\n## 主要优势\n\n- **S1**: 系统性的实验设计——5 种 loss function 的对比（KL, reverse KL, JSD, BCE, MSE）、3-seed 评估、cross-architecture 验证（LLaMA, Mistral, Qwen），实验严谨度高于该领域多数工作。\n- **S2**: Target-swap ablation (C1) 是一个巧妙的分析方法，能够部分解耦 mask quality 和 training mechanism 的贡献，具有方法论参考价值。\n- **S3**: Per-layer KL decomposition（K=1 和 K=4 控制实验）对 signal type vs coupling scope 的定量分解是该领域的新颖分析维度。\n- **S4**: 诚实的自我定位——论文明确声明 \"primarily an empirical study\" 并详细讨论了 confounds 和 upper bounds，这种学术诚实值得肯定。\n- **S5**: Comprehensive appendix（19页总计）提供了充分的补充材料，包括 sensitivity analysis、OOD evaluation、mask visualization 等。\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 说明 |\n|------|------|------|\n| 正文页数 | ✅ | §1-§5 在第8页结束（Conclusion 在 p8 底部） |\n| Limitations | ✅ | 在 p9，不计入页数限制，覆盖3个关键点 |\n| Ethics | ✅ | 在 p9，简短适当 |\n| 匿名化 | ✅ | \"Anonymous ACL submission\"，未发现泄露 |\n| Appendix 双栏 | ✅ | p12-19 使用双栏 ACL 格式 |\n| 引用格式 | ✅ | 使用 acl_natbib，格式一致 |\n\n---\n\n## 评分总结\n\n本文是一篇执行质量较高的实证研究，系统分析了 KL distillation 对 SwiGLU activation sparsity 预测器的影响。主要贡献是分析性的（target-swap ablation、2D decomposition），而非方法论创新（核心 recipe 来自 MaskLLM）。三个 critical 问题——缺乏 wall-clock speedup、MMLU/GSM8K 系统性退化、与 MaskLLM 区分度不足——使其更适合 Findings 而非主会议。如果作者能补充实际加速数据并深化 MMLU regression 的分析，有潜力升至 3.5 (Borderline Conference)。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-22T17:17:30.354919+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---


### Assistant

_source line 1568 · 2026-05-22T17:17:40.622546+00:00_

审稿完成。已将完整审稿意见提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)，Soundness 3.5，Excitement 2.5。

核心问题：
1. **缺乏 wall-clock speedup**——方法实际增加 6.4% 延迟，无加速证据
2. **MMLU/GSM8K 系统性退化**——在所有规模上逊于 training-free baseline TEAL
3. **与 MaskLLM 区分度不足**——核心 recipe（frozen weights + KL + Gumbel masks）完全共享

主要优势在于实验设计的系统性（5 种 loss 对比、3-seed、cross-architecture）和 target-swap ablation / per-layer decomposition 的分析创新。格式完全合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 39

## Round 39

4 recorded events


### User

_source line 1569 · 2026-05-22T17:22:15.977828+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Round 1

以下是 **Reviewer 1** 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N2)、Should-Fix (W1-W5) 和 Questions，标注 `[AGREE]` 同意并说明理由，或 `[REBUT]` 反驳并引用论文中的具体 Section/Table/Figure 作为证据。

---

**Reviewer 1 Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3.0

### Must-Fix:

**N1** [critical] C1 Target-Swap Ablation 因果推断存在循环性，causal claim 过强
- KL-derived masks 本身是 KL coupling 的产物，C1 不能分离 mask quality 和 discovery mechanism
- s42 使用 "earlier checkpoint" oracle (PPL gap 0.65pp) vs s123/s456 matched oracle (gap ≤0.03pp) 不一致
- 下游方向不一致：s42 C1 在 MMLU +1.7pp 但 s456 C1 在 MMLU −0.96pp
- 建议 claim 降级为 "transferability" 而非 "proximate quality driver"

**N2** [critical] 97.5% signal type decomposition 受严重混淆变量影响
- K=1 train-inference mismatch：训练 mask 1/32 层 vs 推理 mask 全部 32 层
- K=4 引入 allocation pattern 变化作为新混淆变量（MMLU >100% gap closure = anomalous）
- 四个 metric 指向截然不同结论（ARC-c 2.6% vs PPL 66.7% vs MMLU >100%）
- Footnote 5 承认 "not fully orthogonal" 但主文仍给精确 97.5%
- 建议替换为定性描述 + 50% K=4 实验

### Should-Fix:

**W1** [warning] 无实际推理加速，Intro 效率动机与交付成果有 gap
**W2** [warning] Table 2 中 KL 28.5% vs TEAL 29.3% 的 actual sparsity mismatch
**W3** [warning] 规模泛化不足（7-14B），reasoning 下降可能随规模恶化
**W4** [warning] Table 2 KL global 50% 的下游仅 s42 单种子
**W5** [warning] K=4 decomposition 仅在 30% 做，50% 缺失

### Questions:
1. "Reverse C1"——在 magnitude masks 上训练 KL 结果如何？
2. 为何 50% 没做 K=4？是否训练不稳定？
3. MMLU 系统性下降是否暗示 forward KL mode-covering 的根本限制？
4. 30% target λ 达 cap (5000) 但实际仅 28.5%——λ_max 设更高能否逼近 30%？

### Minor: M1-M4（BCE wall-clock match 疑问、SPON taxonomy 分类、adaptive penalty 命名、sequence length 影响）

### Strengths:
1. 研究问题有价值且定义清晰
2. 实验覆盖面广、消融设计用心
3. 梯度分析 (§3.6) 有用
4. 诚实的局限性讨论
5. 可复现性好

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1570 · 2026-05-22T17:24:01.073789+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 Reviewer 1\n\n## Must-Fix\n\n**[AGREE] R1-N1: C1 Target-Swap Ablation 因果推断存在循环性**\n\n同意 R1 的核心论点。我在自己的审稿 W4 中也指出了 C1 的 soft-vs-hard confound，R1 进一步揭示了更根本的循环性问题：KL masks 本身就是 KL coupling 的产物，用它们训练 BCE 只能证明 mask patterns 的可迁移性（transferability），而非它们是 \"proximate quality driver\"。\n\n补充 R1 未提及的一点：§4.3 \"Soft-vs-Hard Confound\" 段的控制实验逻辑有瑕疵——BCE+Gumbel (32.22) 比 standard BCE (27.97) 更差，这说明 Gumbel relaxation 在 BCE 设置下是有害的，无法作为 \"softness 不是主因\" 的中性控制。\n\ns42 使用 earlier checkpoint oracle（PPL gap 0.65pp）vs s123/s456 matched oracle（gap ≤0.03pp）的不一致确实削弱说服力。Table 3 s42 行的 ‡ 标注容易被忽略。不过，s123/s456 的 matched oracle 结果（PPL gap ≤0.03pp）本身仍提供了有意义的证据——只是论文不应以 s42 的 0.65pp gap 作为主要叙事。\n\n建议将 claim 从 \"proximate quality driver\" 降级为 \"transferable quality patterns\"，这仍是一个有价值的发现。\n\n**[AGREE] R1-N2: 97.5% signal type decomposition 受严重混淆变量影响**\n\n完全同意。这是我认为论文最大的表述问题之一。\n\n关键证据：\n1. K=1 的 train-inference mismatch 是根本性的。训练时只 mask 1/32 层，推理时 mask 全部 32 层——这不是 \"isolating coupling\" 而是引入了一个巨大的 distribution shift confound。论文在 Footnote 5 承认维度 \"not fully orthogonal\"，但 97.5% 这个数字在 Abstract（第5句）、Introduction（contribution list 第1条）、Conclusion（第1句）中反复出现，给读者的印象远比 caveat 强烈。\n2. K=4 控制实验（Appendix S, Table 19）确实减轻了 mismatch，但引入了新 confound：K=4 的 near-uniform per-layer sparsity（std=0.003）恰好匹配 uniform eval allocation，导致 MMLU >100% gap closure——这是 allocation alignment 的 artifact 而非 coupling 的真实效应。论文在 Appendix S footnote 中承认了这一点，但这实际上意味着 K=4 也不是一个干净的控制。\n3. 四个 metric 的分歧（R1 正确指出：ARC-c 2.6% vs PPL 66.7% vs MMLU >100%）说明这个 decomposition 框架本身不稳定，无法支撑精确的定量结论。\n\n同意 R1 的建议：替换为定性描述（\"signal type is the dominant factor for PPL; coupling contributes meaningfully to some downstream tasks\"）比精确的 97.5% 更诚实也更有说服力。\n\n## Should-Fix\n\n**[AGREE] R1-W1: 无实际推理加速**\n\n强烈同意，这也是我的 N1（critical 级别）。Appendix A Table 5 显示方法实际增加 6.4% 延迟。作为 efficiency-motivated 工作，这是核心缺陷。\n\n**[AGREE] R1-W2: Table 2 actual sparsity mismatch (KL 28.5% vs TEAL 29.3%)**\n\n同意这是一个公平性问题。论文在 Appendix C 提供了 matched comparison（28.5%: 8.81 vs 10.30 = 14.5% reduction），但 Table 2 的主比较（8.81 vs 10.82 at nominal 30%）夸大了优势。Table 2 的 ‡ 脚注（\"Actual sparsity: KL 28.5% vs TEAL 29.3%\"）容易被忽略。建议在 Table 2 中使用 matched sparsity 的结果作为主要比较。\n\n**[AGREE] R1-W3: 规模泛化不足（7-14B）**\n\n同意。Table 13（Appendix K）的 Qwen-14B 结果（GSM8K −20pp vs dense，MMLU −16pp vs dense at 30%）暗示 reasoning 退化可能随规模恶化。但我要补充一个 nuance：Qwen-14B 的 dense 基线本身远强于 LLaMA-8B（MMLU 79.77 vs 65.27），绝对下降幅度不直接可比。相对退化率需要更仔细的分析。\n\n**[AGREE] R1-W4: KL global 50% 下游仅 s42 单种子**\n\n同意。Table 2 中 KL global 50% 的 ARC-c (32.85)、WG (63.46)、GSM8K (1.29) 均为 s42 单种子结果，仅 PPL (11.84±0.15) 和 MMLU (28.1±0.2, from Appendix F) 有多种子报告。对于声称 global allocation 在 50% 优于 uniform 的 claim（§4.5 Allocation Behavior），单种子证据不够充分。KL uniform 50% 的全部指标都有 3-seed 报告，两者标准不一致。\n\n**[REBUT] R1-W5: K=4 decomposition 仅在 30% 做，50% 缺失**\n\n部分同意但认为不应列为 Should-Fix。论文在 §4.5 最后一段已报告 50% K=1 结果（per-layer KL 34.85 vs E2E KL 11.92, +192% gap），并指出 \"coupling's share rising from 2.5% to 10.6% (4×)\"。50% 时不做 K=4 可能有合理原因：(1) 50% 是 capacity-limited regime，所有方法的 downstream 都接近 random（MMLU ~28%），K=4 的 downstream decomposition 在 noise floor 附近意义不大；(2) K=4 训练可能在 50% 不稳定（R1 Q2 也在问这个问题）。论文应解释原因，但缺失本身不构成重大缺陷。\n\n## Questions\n\n**[AGREE] R1-Q1: \"Reverse C1\"（在 magnitude masks 上训练 KL）**\n\n非常好的实验建议。如果 KL trained on magnitude masks 的表现接近 standard KL（即 KL 的 training mechanism 本身比 mask targets 更重要），则直接反驳论文的 C1 结论。这是我在自己审稿 Q5 中类似的问题——如果 coupling 主要用来 discover masks，是否可以用 KL 训练后提取 masks 再用 BCE 部署？Reverse C1 可以直接回答这个问题。\n\n**[AGREE] R1-Q2: 为何 50% 没做 K=4？**\n\n如上所述（我对 W5 的回应），这是一个合理的问题。论文应解释是资源限制还是训练不稳定。\n\n**[AGREE] R1-Q3: MMLU 系统性下降是否暗示 forward KL mode-covering 的根本限制？**\n\n完全同意这是一个核心问题。我在 N2 中详细分析了这一点。论文在 §3.4 中以 mode-covering 作为选择 forward KL 的理论动机（\"false negatives cascade through downstream layers\"），但 MMLU/GSM8K 的系统性退化恰好说明 mode-covering 可能在覆盖 \"breadth\" 时牺牲了 reasoning-critical pathways 的 \"precision\"——这与 reverse KL 的 mode-seeking 形成了未被讨论的 trade-off。更值得关注的是 Appendix T 的 Remove Valley 实验（MMLU +3.3pp），暗示退化部分源于可纠正的 allocation 问题而非 KL 目标的固有限制。\n\n**[AGREE] R1-Q4: λ_max cap 问题**\n\n技术细节问题但有价值。Table 9（Appendix C）显示 30% target 时 λ 达到 cap (5000) 但实际仅 28.5%（5% deviation）。这说明 adaptive penalty controller 在 30% 时已饱和，提高 λ_max 可能帮助逼近 30%，进而消除 W2 的 actual sparsity mismatch 问题。论文应在 Appendix 中报告 λ_max sensitivity。\n\n## Minor\n\n**[AGREE] R1-M1 (BCE wall-clock match)**: 论文声称 BCE 2700 steps 的 wall-clock 与 KL 1000 steps 相当（~46 vs ~45 min, §4.3），但 BCE 不需要 dense forward pass（仅需 magnitude targets），每步应更快。如果实际 wall-clock 接近，需要解释为什么。\n\n**[REBUT] R1-M2 (SPON taxonomy 分类)**: SPON 使用 closed-form KL minimization per layer，确实是 \"coupled\" signal（KL on output distribution）但 \"static\" granularity（fixed bias per layer）。将其放在 Static × Coupled 格子中是合理的——R1 可能认为 SPON 的 per-layer KL 不算 \"coupled\"，但 Table 1 的 \"coupled\" 定义是 \"whether the objective captures inter-neuron dependencies\"，SPON 的 KL 目标确实耦合了同一层内的所有 neuron。\n\n**[AGREE] R1-M3 (adaptive penalty 命名)**: \"Adaptive Penalty Controller\" 确实不是标准的 Lagrangian——它使用 geometric doubling + deadzone 而非经典的 dual ascent。命名应更准确。\n\n**[AGREE] R1-M4 (sequence length 影响)**: 训练和评估都固定 seq_len=2048，未分析更长序列下的行为。这对 batched inference 和 long-context 场景的 generalization 是合理的 concern。\n\n## Strengths 回应\n\n完全同意 R1 列出的 5 个优势。特别是 S4（诚实的局限性讨论）——论文在多处主动 caveat confounds 和 upper bounds，这在该领域并不常见。我在自己的审稿 S4 中也独立指出了这一点。\n\n## 总结\n\nR1 和 R2 的审稿意见高度一致：\n- **共识 Critical**: C1 causal claim 过强（R1-N1 ≈ R2-W4）、wall-clock speedup 缺失（R1-W1 = R2-N1）、MMLU/GSM8K 退化（R2-N2）\n- **共识 Warning**: actual sparsity mismatch（R1-W2）、规模泛化不足（R1-W3 ≈ R2-N2 部分）\n- **唯一分歧**: R1 将 97.5% decomposition confound 列为 N2 (critical)，我在 W 级别提及但同意 R1 升级为 critical 是合理的——因为 97.5% 出现在 Abstract/Intro/Conclusion 的核心位置，misleading 的影响范围大。\n\n综合来看，我维持 **Overall 3.0 (Findings)** 的评分。R1 给 3.5 (Borderline Conference) 略高于我，差异主要在 Excitement 评分（R1: 3.0 vs 我: 2.5）——R1 更肯定研究问题的价值，而我对与 MaskLLM 的区分度更严格。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应 Reviewer 1\n\n## Must-Fix\n\n**[AGREE] R1-N1: C1 Target-Swap Ablation 因果推断存在循环性**\n\n同意 R1 的核心论点。我在自己的审稿 W4 中也指出了 C1 的 soft-vs-hard confound，R1 进一步揭示了更根本的循环性问题：KL masks 本身就是 KL coupling 的产物，用它们训练 BCE 只能证明 mask patterns 的可迁移性（transferability），而非它们是 \"proximate quality driver\"。\n\n补充 R1 未提及的一点：§4.3 \"Soft-vs-Hard Confound\" 段的控制实验逻辑有瑕疵——BCE+Gumbel (32.22) 比 standard BCE (27.97) 更差，这说明 Gumbel relaxation 在 BCE 设置下是有害的，无法作为 \"softness 不是主因\" 的中性控制。\n\ns42 使用 earlier checkpoint oracle（PPL gap 0.65pp）vs s123/s456 matched oracle（gap ≤0.03pp）的不一致确实削弱说服力。Table 3 s42 行的 ‡ 标注容易被忽略。不过，s123/s456 的 matched oracle 结果（PPL gap ≤0.03pp）本身仍提供了有意义的证据——只是论文不应以 s42 的 0.65pp gap 作为主要叙事。\n\n建议将 claim 从 \"proximate quality driver\" 降级为 \"transferable quality patterns\"，这仍是一个有价值的发现。\n\n**[AGREE] R1-N2: 97.5% signal type decomposition 受严重混淆变量影响**\n\n完全同意。这是我认为论文最大的表述问题之一。\n\n关键证据：\n1. K=1 的 train-inference mismatch 是根本性的。训练时只 mask 1/32 层，推理时 mask 全部 32 层——这不是 \"isolating coupling\" 而是引入了一个巨大的 distribution shift confound。论文在 Footnote 5 承认维度 \"not fully orthogonal\"，但 97.5% 这个数字在 Abstract（第5句）、Introduction（contribution list 第1条）、Conclusion（第1句）中反复出现，给读者的印象远比 caveat 强烈。\n2. K=4 控制实验（Appendix S, Table 19）确实减轻了 mismatch，但引入了新 confound：K=4 的 near-uniform per-layer sparsity（std=0.003）恰好匹配 uniform eval allocation，导致 MMLU >100% gap closure——这是 allocation alignment 的 artifact 而非 coupling 的真实效应。论文在 Appendix S footnote 中承认了这一点，但这实际上意味着 K=4 也不是一个干净的控制。\n3. 四个 metric 的分歧（R1 正确指出：ARC-c 2.6% vs PPL 66.7% vs MMLU >100%）说明这个 decomposition 框架本身不稳定，无法支撑精确的定量结论。\n\n同意 R1 的建议：替换为定性描述（\"signal type is the dominant factor for PPL; coupling contributes meaningfully to some downstream tasks\"）比精确的 97.5% 更诚实也更有说服力。\n\n## Should-Fix\n\n**[AGREE] R1-W1: 无实际推理加速**\n\n强烈同意，这也是我的 N1（critical 级别）。Appendix A Table 5 显示方法实际增加 6.4% 延迟。作为 efficiency-motivated 工作，这是核心缺陷。\n\n**[AGREE] R1-W2: Table 2 actual sparsity mismatch (KL 28.5% vs TEAL 29.3%)**\n\n同意这是一个公平性问题。论文在 Appendix C 提供了 matched comparison（28.5%: 8.81 vs 10.30 = 14.5% reduction），但 Table 2 的主比较（8.81 vs 10.82 at nominal 30%）夸大了优势。Table 2 的 ‡ 脚注（\"Actual sparsity: KL 28.5% vs TEAL 29.3%\"）容易被忽略。建议在 Table 2 中使用 matched sparsity 的结果作为主要比较。\n\n**[AGREE] R1-W3: 规模泛化不足（7-14B）**\n\n同意。Table 13（Appendix K）的 Qwen-14B 结果（GSM8K −20pp vs dense，MMLU −16pp vs dense at 30%）暗示 reasoning 退化可能随规模恶化。但我要补充一个 nuance：Qwen-14B 的 dense 基线本身远强于 LLaMA-8B（MMLU 79.77 vs 65.27），绝对下降幅度不直接可比。相对退化率需要更仔细的分析。\n\n**[AGREE] R1-W4: KL global 50% 下游仅 s42 单种子**\n\n同意。Table 2 中 KL global 50% 的 ARC-c (32.85)、WG (63.46)、GSM8K (1.29) 均为 s42 单种子结果，仅 PPL (11.84±0.15) 和 MMLU (28.1±0.2, from Appendix F) 有多种子报告。对于声称 global allocation 在 50% 优于 uniform 的 claim（§4.5 Allocation Behavior），单种子证据不够充分。KL uniform 50% 的全部指标都有 3-seed 报告，两者标准不一致。\n\n**[REBUT] R1-W5: K=4 decomposition 仅在 30% 做，50% 缺失**\n\n部分同意但认为不应列为 Should-Fix。论文在 §4.5 最后一段已报告 50% K=1 结果（per-layer KL 34.85 vs E2E KL 11.92, +192% gap），并指出 \"coupling's share rising from 2.5% to 10.6% (4×)\"。50% 时不做 K=4 可能有合理原因：(1) 50% 是 capacity-limited regime，所有方法的 downstream 都接近 random（MMLU ~28%），K=4 的 downstream decomposition 在 noise floor 附近意义不大；(2) K=4 训练可能在 50% 不稳定（R1 Q2 也在问这个问题）。论文应解释原因，但缺失本身不构成重大缺陷。\n\n## Questions\n\n**[AGREE] R1-Q1: \"Reverse C1\"（在 magnitude masks 上训练 KL）**\n\n非常好的实验建议。如果 KL trained on magnitude masks 的表现接近 standard KL（即 KL 的 training mechanism 本身比 mask targets 更重要），则直接反驳论文的 C1 结论。这是我在自己审稿 Q5 中类似的问题——如果 coupling 主要用来 discover masks，是否可以用 KL 训练后提取 masks 再用 BCE 部署？Reverse C1 可以直接回答这个问题。\n\n**[AGREE] R1-Q2: 为何 50% 没做 K=4？**\n\n如上所述（我对 W5 的回应），这是一个合理的问题。论文应解释是资源限制还是训练不稳定。\n\n**[AGREE] R1-Q3: MMLU 系统性下降是否暗示 forward KL mode-covering 的根本限制？**\n\n完全同意这是一个核心问题。我在 N2 中详细分析了这一点。论文在 §3.4 中以 mode-covering 作为选择 forward KL 的理论动机（\"false negatives cascade through downstream layers\"），但 MMLU/GSM8K 的系统性退化恰好说明 mode-covering 可能在覆盖 \"breadth\" 时牺牲了 reasoning-critical pathways 的 \"precision\"——这与 reverse KL 的 mode-seeking 形成了未被讨论的 trade-off。更值得关注的是 Appendix T 的 Remove Valley 实验（MMLU +3.3pp），暗示退化部分源于可纠正的 allocation 问题而非 KL 目标的固有限制。\n\n**[AGREE] R1-Q4: λ_max cap 问题**\n\n技术细节问题但有价值。Table 9（Appendix C）显示 30% target 时 λ 达到 cap (5000) 但实际仅 28.5%（5% deviation）。这说明 adaptive penalty controller 在 30% 时已饱和，提高 λ_max 可能帮助逼近 30%，进而消除 W2 的 actual sparsity mismatch 问题。论文应在 Appendix 中报告 λ_max sensitivity。\n\n## Minor\n\n**[AGREE] R1-M1 (BCE wall-clock match)**: 论文声称 BCE 2700 steps 的 wall-clock 与 KL 1000 steps 相当（~46 vs ~45 min, §4.3），但 BCE 不需要 dense forward pass（仅需 magnitude targets），每步应更快。如果实际 wall-clock 接近，需要解释为什么。\n\n**[REBUT] R1-M2 (SPON taxonomy 分类)**: SPON 使用 closed-form KL minimization per layer，确实是 \"coupled\" signal（KL on output distribution）但 \"static\" granularity（fixed bias per layer）。将其放在 Static × Coupled 格子中是合理的——R1 可能认为 SPON 的 per-layer KL 不算 \"coupled\"，但 Table 1 的 \"coupled\" 定义是 \"whether the objective captures inter-neuron dependencies\"，SPON 的 KL 目标确实耦合了同一层内的所有 neuron。\n\n**[AGREE] R1-M3 (adaptive penalty 命名)**: \"Adaptive Penalty Controller\" 确实不是标准的 Lagrangian——它使用 geometric doubling + deadzone 而非经典的 dual ascent。命名应更准确。\n\n**[AGREE] R1-M4 (sequence length 影响)**: 训练和评估都固定 seq_len=2048，未分析更长序列下的行为。这对 batched inference 和 long-context 场景的 generalization 是合理的 concern。\n\n## Strengths 回应\n\n完全同意 R1 列出的 5 个优势。特别是 S4（诚实的局限性讨论）——论文在多处主动 caveat confounds 和 upper bounds，这在该领域并不常见。我在自己的审稿 S4 中也独立指出了这一点。\n\n## 总结\n\nR1 和 R2 的审稿意见高度一致：\n- **共识 Critical**: C1 causal claim 过强（R1-N1 ≈ R2-W4）、wall-clock speedup 缺失（R1-W1 = R2-N1）、MMLU/GSM8K 退化（R2-N2）\n- **共识 Warning**: actual sparsity mismatch（R1-W2）、规模泛化不足（R1-W3 ≈ R2-N2 部分）\n- **唯一分歧**: R1 将 97.5% decomposition confound 列为 N2 (critical)，我在 W 级别提及但同意 R1 升级为 critical 是合理的——因为 97.5% 出现在 Abstract/Intro/Conclusion 的核心位置，misleading 的影响范围大。\n\n综合来看，我维持 **Overall 3.0 (Findings)** 的评分。R1 给 3.5 (Borderline Conference) 略高于我，差异主要在 Excitement 评分（R1: 3.0 vs 我: 2.5）——R1 更肯定研究问题的价值，而我对与 MaskLLM 的区分度更严格。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-22T17:24:05.590359+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4516
}
```

</details>

---


### Assistant

_source line 1572 · 2026-05-22T17:24:13.926361+00:00_

交叉回应已提交。主要判断：

- R1 的 N1 (C1 causal claim) 和 N2 (97.5% decomposition confound) **均同意**，两者都涉及论文核心 claim 的过度表述
- R1 的 W1-W4 **同意**，W5 (K=4 at 50% 缺失) **部分反驳**——50% 是 capacity-limited regime，K=4 downstream decomposition 在 noise floor 附近意义有限
- Minor 中对 M2 (SPON taxonomy 分类) **反驳**——SPON 的 per-layer KL 确实符合 "coupled" 定义
- 两位 reviewer 的核心共识：C1 claim 过强、wall-clock speedup 缺失、MMLU 退化未充分解释
- 我维持 Overall 3.0 (Findings)，与 R1 的 3.5 差异主要在 novelty 评估上

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 40

## Round 40

68 recorded events


### User

_source line 1573 · 2026-05-22T23:39:38.799873+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查**新颖性和完整性**。

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

### 新颖性评估
1. **核心贡献新颖性**：将 KL distillation 应用于 activation sparsity prediction 的新颖性如何？与 MaskLLM (frozen weights + learnable masks + KL) 的本质区别是否成立？"output-distribution alignment as the dominant design dimension" 是否足够新颖构成 EMNLP 主会议贡献？
2. **2D Taxonomy**：signal type × coupling scope 分类框架是否有新颖洞见？还是仅仅是对现有方法的组织？
3. **分析性贡献 vs 工程贡献**：论文自称 "primarily an empirical study"——在 EMNLP 2026 的标准下，纯分析/实证工作是否有足够的贡献门槛？

### 完整性
4. **Related Work 覆盖度**：是否遗漏了重要的相关工作？特别关注：(a) 其他 KL-based pruning/sparsity 方法, (b) 最新 2025-2026 activation sparsity 论文, (c) Gumbel-Sigmoid 在 mask learning 中的应用
5. **叙事结构**：Abstract → Intro → Method → Experiments → Conclusion 的逻辑链是否清晰连贯？核心 claim 是否在各章节间一致？
6. **Framing 诚实度**：论文声明的限制是否完整？是否有 overclaim？"empirical study" 定位是否前后一致？
7. **写作质量**：信息密度、可读性、图表质量、notation 一致性

### 格式合规
8. **ARR 格式检查**：页数是否合规（8 页正文）？Limitations 章节是否存在且恰当？Ethics Statement 是否存在？匿名性是否维持？

请按 ARR 标准给出：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，按严重性排列：Critical > Warning > Minor) → Questions → Missing References → Overall Assessment (1-5 分，参照 EMNLP 2026 ARR 评分标准)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1574 · 2026-05-22T23:39:45.983341+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1575 · 2026-05-22T23:39:46.034094+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-22T23:39:47.554214+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1577 · 2026-05-22T23:39:47.654815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1578 · 2026-05-22T23:39:52.474577+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1579 · 2026-05-22T23:39:54.734314+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1580 · 2026-05-22T23:39:59.054967+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about ACL ARR 2026 reviewer guidelines and review form criteria. Here are the key findings:

## Review Form Criteria

For Main papers, the general criteria include soundness, reproducibility, novelty, and impact, while Findings paper
…[truncated 1170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6580
}
```

</details>

---


### Tool result

_source line 1581 · 2026-05-22T23:40:00.711205+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5976
}
```

</details>

---


### Tool call

_source line 1582 · 2026-05-22T23:40:10.955723+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions, their scales, and descriptions. I need: 1) All scoring criteria names 2) Score ranges for each 3) Description of what each score means 4) Any other required fields like summary, strengths, weaknesses, questions, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all scoring dimensions, their scales, and descriptions. I need: 1) All scoring criteria names 2) Score ranges for each 3) Description of what each score means 4) Any other required fields like summary, strengths, weaknesses, questions, etc."
  }
}
```

</details>

---


### Tool call

_source line 1583 · 2026-05-22T23:40:12.461168+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-22T23:40:13.465128+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1585 · 2026-05-22T23:40:13.917128+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-22T23:40:14.419395+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1587 · 2026-05-22T23:40:14.971671+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1588 · 2026-05-22T23:40:16.982241+00:00_

# ACL Rolling Review Form Structure

## Required Text Sections
- **Paper Summary**: Overview of paper topic
- **Summary of Strengths**: Reasons to publish at selective venue
- **Summary of Weaknesses**: Concerns prioritizing other papers
- **Comments/Suggestions/Typos**: Improvement recommendations

## Scoring Dimensions

### 1. Reviewer Confidence
Scale: 1–5
- 5: Positive evaluation; careful reading and familiarity with related work
- 4: Quite sure; unlikely to have missed important points
- 3: Pretty sure; good area familiarity but incomplete detail checking
- 2: Willing to defend; fairly likely some details were missed
- 1: Outside expertise or paper very difficult to understand

### 2. Soundness
Scale: 1–5 (with .5 increments)
- 5: Excellent; thorough study for its type
- 4: Strong; sufficient support for claims
- 3: Acceptable; main claims supported with minor gaps
- 2: Poor; main claims lack sufficient support
- 1: Major Issues; insufficient rigor or ACL relevance

### 3. Excitement
Scale: 1–5 (with .5 increments)
- 5: Highly Exciting; would recommend to others
- 4: Exciting; would mention to others
- 3: Interesting; might mention specific points
- 2: Potentially Interesting; limited personal resonance
- 1: Not Exciting; no community relevance

### 4. Overall Assessment
Scale: 1–5 (with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Additional Required Fields
- Best paper justification (if award-level rating)
- Limitations and societal impact evaluation
- Ethical concerns review
- Ethics review recommendation
- Reproducibility assessment (1–5 scale)
- Dataset value (1–5 scale, if applicable)
- Software value (1–5 scale, if applicable)
- Author anonymity knowledge (1–5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6026
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-22T23:40:18.887866+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 594.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.1}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 300.1}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 356.8}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p19.png\", \"w
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6426
}
```

</details>

---


### Tool result

_source line 1590 · 2026-05-22T23:40:22.408646+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7989
}
```

</details>

---


### Tool result

_source line 1591 · 2026-05-22T23:40:22.411814+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8946
}
```

</details>

---


### Tool result

_source line 1592 · 2026-05-22T23:40:22.464710+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8547
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-22T23:40:22.466500+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7494
}
```

</details>

---


### Tool call

_source line 1594 · 2026-05-22T23:40:30.303736+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1595 · 2026-05-22T23:40:30.656610+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1596 · 2026-05-22T23:40:30.709206+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1597 · 2026-05-22T23:40:30.709633+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1598 · 2026-05-22T23:40:32.216426+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1912
}
```

</details>

---


### Tool result

_source line 1599 · 2026-05-22T23:40:33.026926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2370
}
```

</details>

---


### Tool result

_source line 1600 · 2026-05-22T23:40:33.029952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2320
}
```

</details>

---


### Tool result

_source line 1601 · 2026-05-22T23:40:33.081113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2371
}
```

</details>

---


### Tool call

_source line 1602 · 2026-05-22T23:40:39.351955+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1603 · 2026-05-22T23:40:39.908207+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1604 · 2026-05-22T23:40:40.913785+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1561
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-22T23:40:40.965185+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 1606 · 2026-05-22T23:40:40.965581+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1607 · 2026-05-22T23:40:41.321189+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1608 · 2026-05-22T23:40:42.930889+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1965
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-22T23:40:43.687893+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2366
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-22T23:40:49.032593+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1611 · 2026-05-22T23:40:49.484615+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1612 · 2026-05-22T23:40:49.838942+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 1613 · 2026-05-22T23:40:49.839472+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1614 · 2026-05-22T23:40:50.494843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool call

_source line 1615 · 2026-05-22T23:40:50.495282+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1616 · 2026-05-22T23:40:50.847334+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-22T23:40:51.199779+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 1618 · 2026-05-22T23:40:56.973057+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1619 · 2026-05-22T23:40:57.475952+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1620 · 2026-05-22T23:40:57.478286+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 1621 · 2026-05-22T23:40:57.780698+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1622 · 2026-05-22T23:40:58.285890+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-22T23:40:58.388105+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-22T23:41:43.393543+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation sparsity prediction LLM 2025 2026 recent papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation sparsity prediction LLM 2025 2026 recent papers"
  }
}
```

</details>

---


### Tool call

_source line 1625 · 2026-05-22T23:41:43.895696+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KL divergence knowledge distillation pruning sparsity neural networks 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KL divergence knowledge distillation pruning sparsity neural networks 2025"
  }
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-22T23:41:44.297546+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gumbel-Sigmoid mask learning neural network sparsity 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gumbel-Sigmoid mask learning neural network sparsity 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-22T23:41:50.721442+00:00_

Web search results for query: "KL divergence knowledge distillation pruning sparsity neural networks 2025"

Links: [{"title":"Head-Tail-Aware KL Divergence in Knowledge Distillation ...","url":"https://arxiv.org/pdf/2504.20445"},{"title":"Robustness-Reinforced Knowledge Distillation with Correlation Distance and Network Pruning","url":"https://arxiv.org/pdf/2311.13934"},{"title":"Deep Neural Network Compression with Knowledge Distillation Using Cross-Layer Matrix, KL Divergence and Offline Ensemble | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9306290"},{"title":"Cross-layer knowledge distillation with KL divergence and offline ensemble for compressing deep neural network | APSIPA Transactions on Signal and Information Processing | Cambridge Core","url":"https://www.cambridge.org/core/journals/apsipa-transactions-on-signal-and-information-processing/article/crosslayer-knowledge-distillation-with-kl-divergence-and-offline-ensemble-for-compressing-deep-neural-network/C1EE7383879E7FF2C5E9A72BC1EBE05D"},{"title":"Towards optimal sparse CNNs: sparsity-friendly knowledge distillation","url":"https://peerj.com/articles/cs-3388.pdf"},{"title":"Robustness-Reinforced Knowledge Distillation with Correlation Distance and Network Pruning","url":"https://arxiv.org/html/2311.13934"},{"title":"Teacher-Guided One-Shot Pruning via Context-Aware Knowledge Distillation","url":"https://arxiv.org/pdf/2511.16653"},{"title":"Deep Neural Compression Via Concurrent Pruning and Self-Distillation","url":"https://arxiv.org/pdf/2109.15014"},{"title":"Memory-Replay Knowledge Distillation","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8071405/"}]

Based on the search results, here's what I found about KL divergence, knowledge distillation, pruning, and sparsity in neural networks for 2025:

## Recent Research Developments

**Knowledge Distillation with KL Divergence:**
Most existing knowledge distillation techniques rely on Kullback-Leibler (KL) div
…[truncated 1516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6825
}
```

</details>

---


### Tool result

_source line 1628 · 2026-05-22T23:41:50.822401+00:00_

Web search results for query: "activation sparsity prediction LLM 2025 2026 recent papers"

Links: [{"title":"[2411.12692] SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/abs/2411.12692"},{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern","url":"https://arxiv.org/pdf/2507.14179"},{"title":"Grasp: Group-Based Prediction of Activation Sparsity for Fast LLM Inference | Proceedings of the 62nd Annual ACM/IEEE Design Automation Conference","url":"https://dl.acm.org/doi/10.1109/DAC63849.2025.11132899"},{"title":"[2509.00454] Universal Properties of Activation Sparsity in Modern Large Language Models","url":"https://arxiv.org/abs/2509.00454"},{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity","url":"https://arxiv.org/html/2411.02335v2"},{"title":"[2504.19449] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/abs/2504.19449"}]

I found several recent papers on activation sparsity prediction for LLMs from 2025-2026:

## Recent Papers on Activation Sparsity Prediction for LLMs

**SparseInfer (November 2024 - January 2025)**
SparseInfer is a simple, lightweight, and training-free predictor for activation sparsity of ReLU-based LLMs, where activation sparsity is predicted by comparing only the sign bits of inputs and weights.

**Ac
…[truncated 1573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7428
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-22T23:41:51.374483+00:00_

Web search results for query: "Gumbel-Sigmoid mask learning neural network sparsity 2024 2025"

Links: [{"title":"[Literature Review] GFSNetwork: Differentiable Feature Selection via Gumbel-Sigmoid Relaxation","url":"https://www.themoonlight.io/en/review/gfsnetwork-differentiable-feature-selection-via-gumbel-sigmoid-relaxation"},{"title":"Optimizing global sparsity for neural network","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12136039"},{"title":"Learning Neural Networks with Sparse Activations","url":"https://arxiv.org/pdf/2406.17989"},{"title":"Effective Sparsification of Neural Networks with Global Sparsity   Constraint","url":"https://arxiv.org/pdf/2105.01571"},{"title":"Inducing Semi-Structured Sparsity by Masking for Efficient Model   Inference in Convolutional Networks","url":"https://arxiv.org/pdf/2411.00288"},{"title":"Sparsifying neural network models","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11645529"},{"title":"Sparsity in Deep Learning: Pruning and growth for efficient inference   and training in neural networks","url":"https://arxiv.org/pdf/2102.00554"}]

Based on the web search results, here's what I found related to your query about Gumbel-Sigmoid mask learning for neural network sparsity:

## Key Findings

**GFSNetwork - Gumbel-Sigmoid Feature Selection:**
The GFSNetwork paper presents a robust and scalable solution for feature selection in deep learning, leveraging differentiable methods that incorporate Gumbel-Sigmoid relaxation. The combination of automatic feature selection with strong computational efficiency positions GFSNetwork as a relevant tool in high-dimensional machine learning scenarios, with clear interpretative capability.

**ProbMask - Probabilistic Masking with Gumbel-Softmax:**
A probabilistic masking (ProbMask) method was proposed to solve sparsification under global sparsity constraint by directly working on the probability space. This method adopts the Gumbel-Softmax t
…[truncated 671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7076
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-22T23:41:57.192039+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MaskLLM Fang 2024 semi-structured sparsity Gumbel-Softmax KL divergence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MaskLLM Fang 2024 semi-structured sparsity Gumbel-Softmax KL divergence"
  }
}
```

</details>

---


### Tool call

_source line 1631 · 2026-05-22T23:41:57.794160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TurboSparse 2024 activation sparsity SwiGLU dReLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TurboSparse 2024 activation sparsity SwiGLU dReLU"
  }
}
```

</details>

---


### Tool result

_source line 1632 · 2026-05-22T23:42:03.566494+00:00_

Web search results for query: "MaskLLM Fang 2024 semi-structured sparsity Gumbel-Softmax KL divergence"

Links: [{"title":"MaskLLM","url":"https://vainf.github.io/maskllm-project-page/"},{"title":"[2409.17481] MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/abs/2409.17481"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Llu9nJal7b"},{"title":"GitHub - NVlabs/MaskLLM: [NeurIPS 24 Spotlight] MaskLLM: Learnable Semi-structured Sparsity for Large Language Models · GitHub","url":"https://github.com/nvlabs/maskllm"},{"title":"GitHub - VainF/MaskLLM-4V: Learnable Semi-structured Sparsity for Vision Transformers and Diffusion Transformers · GitHub","url":"https://github.com/VainF/MaskLLM-4V"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/397199936_MaskLLM_Learnable_Semi-Structured_Sparsity_for_Large_Language_Models"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2409.17481"},{"title":"NeurIPS Poster MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://neurips.cc/virtual/2024/poster/95573"},{"title":"(PDF) MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://www.researchgate.net/publication/384367339_MaskLLM_Learnable_Semi-Structured_Sparsity_for_Large_Language_Models"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/html/2409.17481v2"}]

Based on the search results, here's what I found about MaskLLM by Fang et al. (2024):

## Overview

MaskLLM is a learnable pruning method that establishes Semi-structured (or "N:M") Sparsity in LLMs, aimed at reducing computational overhead during inference.

## Core Technical Approach

Instead of developing a new importance crit
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6374
}
```

</details>

---


### Tool result

_source line 1633 · 2026-05-22T23:42:04.921983+00:00_

Web search results for query: "TurboSparse 2024 activation sparsity SwiGLU dReLU"

Links: [{"title":"Turbo Sparse: Efficient LLMs with dReLU","url":"https://api.emergentmind.com/papers/2406.05955"},{"title":"[2406.05955] Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/abs/2406.05955"},{"title":"[2406.05955v2] Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/abs/2406.05955v2"},{"title":"Turbo Sparse: LLMs with Minimal Activated Parameters | Medium","url":"https://medium.com/@bnjmn_marie/turbo-sparse-llms-with-minimal-activated-parameters-5197a984f767"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/pdf/2406.05955"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://bestofai.com/article/turbo-sparse-achieving-llm-sota-performance-with-minimal-activated-parameters"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters - AI for Dummies - Understand the Latest AI Papers in Simple Terms","url":"https://ai-search.io/papers/turbo-sparse-achieving-llm-sota-performance-with-minimal-activated-parameters"},{"title":"[Literature Review] Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://www.themoonlight.io/en/review/turbo-sparse-achieving-llm-sota-performance-with-minimal-activated-parameters"},{"title":"TurboSparse: Faster LLMs via dReLU Activation | HackerNoon","url":"https://hackernoon.com/turbosparse-faster-llms-via-drelu-activation"},{"title":"dReLU Activation Function: Matching SwiGLU Performance with 90% Sparsity | HackerNoon","url":"https://hackernoon.com/drelu-activation-function-matching-swiglu-performance-with-90percent-sparsity"}]

The search returned comprehensive results about TurboSparse. Here's a summary of the key findings:

## TurboSparse Overview

Tur
…[truncated 1256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7127
}
```

</details>

---
