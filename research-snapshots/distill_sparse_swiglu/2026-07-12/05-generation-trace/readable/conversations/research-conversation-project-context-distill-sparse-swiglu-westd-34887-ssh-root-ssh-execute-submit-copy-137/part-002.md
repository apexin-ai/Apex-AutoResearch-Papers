# Research conversation: <project_context> # 项目: distill_sparse_swiglu ## 运行环境 - 服务器名: westd-34887 - SSH 账户: root（调用 ssh_execute / submit_trainin — Part 2 of 2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-distill-sparse-swiglu-westd-34887-ssh-root-ssh-execute-submit-copy-137.md) · [Structured JSON](../../../sessions/a5/a59cabdab8c15ef79eb9.json)

## Round 1

### Tool call

_source line 26 · 2026-05-24T03:57:34.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PifDt1AQnz6xQfsUbXdjih`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d90af00-25b6-4068-8c5f-76f61503c0b2",
  "isSidechain": false,
  "requestId": "req_011CbLiqB9NFA8R3etBpvHv2",
  "type": "assistant",
  "uuid": "57f5be57-596d-4b08-97fe-024f2aab8ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177mv6yrzsEC656pgbU2FXb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 25598,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 776,
          "cache_read_input_tokens": 25598,
          "cache_creation_input_tokens": 1176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1176
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-24T03:57:34.244Z_

<details><summary>↩ Tool result · `toolu_01PifDt1AQnz6xQfsUbXdjih`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	ActTail~\cite{zheng2026acttail} applies heavy-tailed self-regularization for global activation sparsity allocation; WiSparse~\cite{yang2026wisparse} proposes weight-aware mixed activation sparsity.
11	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
12	
13	\paragraph{Predictor-Based Contextual Sparsity.}
14	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
15	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
16	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
17	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
18	Dhar et al.~\cite{dhar2025clustering} compress activation patterns via clustering for efficient neuron-level prediction.
19	LazyLLM~\cite{fu2024lazyllm} dynamically prunes tokens across layers for long-context efficiency; COTS~\cite{zhang2025cots} exploits connected activation patterns for structured sparse inference.
20	PowerInfer~\cite{song2024powerinfer} and PowerInfer-2~\cite{xue2024powerinfer2} exploit power-law activation frequencies for GPU--CPU/NPU scheduling.
21	MaskLLM~\cite{fang2024maskllm} shares the recipe-level principle of frozen weights + learnable masks + KL training.
22	The methods differ in three respects: (a) MaskLLM's mask parameters are fixed per input (static N:M weight sparsity via Gumbel-Softmax), while our predictor generates \emph{per-token} masks that must generalize to unseen inputs; (b) static N:M patterns have no cross-layer allocation interaction, whereas our masks coordinate through TEAL's global top-$k$; (c) activation masks must be robust to distribution shift at inference, while weight masks are input-independent.
23	Our contribution beyond the shared recipe is analytical: a systematic decomposition of signal type vs.\ coupling scope for sparsity prediction training, via target-swap ablation and per-layer KL controls (\S\ref{sec:perlayer}).
24	All prior predictor-based methods for activation sparsity use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
25	We empirically observe that an output-distribution-coupled objective propagates gradients through all downstream layers and quantify when this matters for global allocation quality.
26	
27	\paragraph{Static Bias Correction.}
28	SPON (Spontaneous Neurons;~\citealp{xu2025spon}) learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.
29	Our method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers that produces input-dependent masks.
30	SPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \S\ref{sec:experiments}).
31	
32	\paragraph{Activation Function Engineering.}
33	ReLU Strikes Back~\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\% natural sparsity; TurboSparse~\cite{song2024turbosparse} and ProSparse~\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.
34	MiniTron~\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.
35	Haziza et al.~\cite{haziza2025accelerating} demonstrate 2:4 semi-structured activation sparsity with hardware-native acceleration, complementing our unstructured approach.
36	MoC~\cite{wu2025moc} selectively activates Top-$K$ FFN channels using SwiGLU's native gating during pretraining.
37	All require retraining or weight modification; our method is a plug-in predictor on \emph{unmodified} SwiGLU models.
38	
39	\paragraph{Weight Pruning, Distillation, and Routing.}
40	Wanda~\cite{sun2024wanda}, SparseGPT~\cite{frantar2023sparsegpt}, and SliceGPT~\cite{ashkboos2024slicegpt} produce static weight masks via one-shot or structured pruning; Polar Sparsity~\cite{shrestha2025polar} scales contextual sparsity to batched inference by shifting focus from MLP to attention head sparsity; Alizadeh et al.~\cite{alizadeh2024llmflash} leverage activation sparsity for memory-efficient inference via selective flash loading.
41	Switch Transformers~\cite{fedus2022switch} and Mixture-of-Depths~\cite{raposo2024mod} achieve conditional computation through learned routing.
42	KL-based distillation~\cite{kim2016sequencekd,sanh2019distilbert,gu2024minillm,agarwal2024gkd,ko2024distillm} trains compact students; SparseLoRA~\cite{khaki2025sparselora} exploits contextual sparsity for fine-tuning.
43	We apply the KL principle to train a sparsity predictor on unmodified dense models, using Gumbel-Sigmoid sampling~\cite{maddison2017concrete,louizos2018l0} for differentiable discrete mask optimization.
44	
45	\paragraph{MoE Routing and Gated Sparsity.}
46	Expert Choice routing~\cite{zhou2022expertchoice} lets each expert select its top-$k$ tokens under a fixed capacity budget, a global allocation perspective that parallels TEAL's neuron-level global top-$k$.
47	D2D-MoE~\cite{szatkowski2024d2dmoe} converts dense SwiGLU layers into dynamic-$k$ MoE by exploiting the same activation sparsity we target, but restructures the network into discrete experts rather than predicting masks on the original architecture.
48	MoNE~\cite{cheng2025mone} applies neuron-granular top-$k$ selection within each MoE expert during pretraining for fine-grained conditional computation without additional routing parameters.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57f5be57-596d-4b08-97fe-024f2aab8ba6",
  "isSidechain": false,
  "promptId": "fdfb0d6d-9233-4c2a-afaa-5df266af136f",
  "type": "user",
  "uuid": "6494076d-031d-41d7-bb6a-d43308b26755",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\paragraph{Training-Free Activation Sparsity.}\nTEAL~\\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\\% sparsity with no training cost.\nCATS~\\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\\cite{shin2025sparseinfer} and GRASP~\\cite{shin2025grasp} predict activation sparsity patterns without additional training.\nLaRoSA~\\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.\nWang et al.~\\cite{wang2025dynamicsparse}, AWQ~\\cite{lin2024awq}, and Outlier Suppression+~\\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.\nDhar et al.~\\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.\nOWL~\\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.\nActTail~\\cite{zheng2026acttail} applies heavy-tailed self-regularization for global activation sparsity allocation; WiSparse~\\cite{yang2026wisparse} proposes weight-aware mixed activation sparsity.\nAll training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \\emph{input-dependent} masks trained to minimize output-distribution divergence.\n\n\\paragraph{Predictor-Based Contextual Sparsity.}\nDejaVu~\\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.\nShadowLLM~\\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.\nFastForward~\\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.\nSVD-CSP~\\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.\nDhar et al.~\\cite{dhar2025clustering} compress activation patterns via clustering for efficient neuron-level prediction.\nLazyLLM~\\cite{fu2024lazyllm} dynamically prunes tokens across layers for long-context efficiency; COTS~\\cite{zhang2025cots} exploits connected activation patterns for structured sparse inference.\nPowerInfer~\\cite{song2024powerinfer} and PowerInfer-2~\\cite{xue2024powerinfer2} exploit power-law activation frequencies for GPU--CPU/NPU scheduling.\nMaskLLM~\\cite{fang2024maskllm} shares the recipe-level principle of frozen weights + learnable masks + KL training.\nThe methods differ in three respects: (a) MaskLLM's mask parameters are fixed per input (static N:M weight sparsity via Gumbel-Softmax), while our predictor generates \\emph{per-token} masks that must generalize to unseen inputs; (b) static N:M patterns have no cross-layer allocation interaction, whereas our masks coordinate through TEAL's global top-$k$; (c) activation masks must be robust to distribution shift at inference, while weight masks are input-independent.\nOur contribution beyond the shared recipe is analytical: a systematic decomposition of signal type vs.\\ coupling scope for sparsity prediction training, via target-swap ablation and per-layer KL controls (\\S\\ref{sec:perlayer}).\nAll prior predictor-based methods for activation sparsity use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.\nWe empirically observe that an output-distribution-coupled objective propagates gradients through all downstream layers and quantify when this matters for global allocation quality.\n\n\\paragraph{Static Bias Correction.}\nSPON (Spontaneous Neurons;~\\citealp{xu2025spon}) learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.\nOur method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers that produces input-dependent masks.\nSPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \\S\\ref{sec:experiments}).\n\n\\paragraph{Activation Function Engineering.}\nReLU Strikes Back~\\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\\% natural sparsity; TurboSparse~\\cite{song2024turbosparse} and ProSparse~\\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.\nMiniTron~\\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.\nHaziza et al.~\\cite{haziza2025accelerating} demonstrate 2:4 semi-structured activation sparsity with hardware-native acceleration, complementing our unstructured approach.\nMoC~\\cite{wu2025moc} selectively activates Top-$K$ FFN channels using SwiGLU's native gating during pretraining.\nAll require retraining or weight modification; our method is a plug-in predictor on \\emph{unmodified} SwiGLU models.\n\n\\paragraph{Weight Pruning, Distillation, and Routing.}\nWanda~\\cite{sun2024wanda}, SparseGPT~\\cite{frantar2023sparsegpt}, and SliceGPT~\\cite{ashkboos2024slicegpt} produce static weight masks via one-shot or structured pruning; Polar Sparsity~\\cite{shrestha2025polar} scales contextual sparsity to batched inference by shifting focus from MLP to attention head sparsity; Alizadeh et al.~\\cite{alizadeh2024llmflash} leverage activation sparsity for memory-efficient inference via selective flash loading.\nSwitch Transformers~\\cite{fedus2022switch} and Mixture-of-Depths~\\cite{raposo2024mod} achieve conditional computation through learned routing.\nKL-based distillation~\\cite{kim2016sequencekd,sanh2019distilbert,gu2024minillm,agarwal2024gkd,ko2024distillm} trains compact students; SparseLoRA~\\cite{khaki2025sparselora} exploits contextual sparsity for fine-tuning.\nWe apply the KL principle to train a sparsity predictor on unmodified dense models, using Gumbel-Sigmoid sampling~\\cite{maddison2017concrete,louizos2018l0} for differentiable discrete mask optimization.\n\n\\paragraph{MoE Routing and Gated Sparsity.}\nExpert Choice routing~\\cite{zhou2022expertchoice} lets each expert select its top-$k$ tokens under a fixed capacity budget, a global allocation perspective that parallels TEAL's neuron-level global top-$k$.\nD2D-MoE~\\cite{szatkowski2024d2dmoe} converts dense SwiGLU layers into dynamic-$k$ MoE by exploiting the same activation sparsity we target, but restructures the network into discrete experts rather than predicting masks on the original architecture.\nMoNE~\\cite{cheng2025mone} applies neuron-granular top-$k$ selection within each MoE expert during pretraining for fine-grained conditional computation without additional routing parameters.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  },
  "sourceToolAssistantUUID": "57f5be57-596d-4b08-97fe-024f2aab8ba6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-24T03:57:34.714Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Szb6ZK7hsXfmH7xvdpypSx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6494076d-031d-41d7-bb6a-d43308b26755",
  "isSidechain": false,
  "requestId": "req_011CbLiqB9NFA8R3etBpvHv2",
  "type": "assistant",
  "uuid": "646584d3-cc5c-4ab2-8101-edf1fbaf2f46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177mv6yrzsEC656pgbU2FXb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 25598,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 776,
          "cache_read_input_tokens": 25598,
          "cache_creation_input_tokens": 1176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1176
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-24T03:57:34.988Z_

<details><summary>↩ Tool result · `toolu_01Szb6ZK7hsXfmH7xvdpypSx`</summary>

```text
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
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.
34	Our contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.
35	
36	
37	\section{Predictor Bottleneck Sensitivity}
38	\label{app:db_sensitivity}
39	
40	Table~\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.
41	
42	\begin{table}[h]
43	\centering
44	\caption{Predictor bottleneck sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}
45	\label{tab:db_sensitivity}
46	\small
47	\begin{tabular}{lcccc}
48	\toprule
49	$d_b$ & Params & TEAL global & $\Delta$ & Per-token \\
50	\midrule
51	64 & 38.2M (0.48\%) & 12.076 & +0.9\% & 10.16 \\ % exp_id: db_sensitivity_sweep
52	128 & 75.9M (0.95\%) & 11.963 & --- & 9.218 \\ % exp_id: db_sensitivity_sweep
53	256 & 151.5M (1.89\%) & 12.105 & +1.2\% & 8.586 \\ % exp_id: db_sensitivity_sweep
54	512 & 302.5M (3.77\%) & 12.315 & +2.9\% & 7.93 \\ % exp_id: db_sensitivity_sweep
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Under TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\to$7.93).
60	This divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.
61	The $d_b{=}128$ configuration (75.9M params, $<$1\% of base model) is therefore optimal for the TEAL inference protocol.
62	
63	\subsection{Temperature Schedule Sensitivity}
64	\label{app:tau_sensitivity}
65	
66	\begin{table}[h]
67	\centering
68	\caption{Temperature schedule sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
69	\label{tab:tau_sensitivity}
70	\small
71	\begin{tabular}{lc}
72	\toprule
73	$\tau$ Schedule & PPL$\downarrow$ \\
74	\midrule
75	Fixed $\tau{=}0.5$ & \textbf{11.861} \\ % exp_id: tau_schedule_sweep
76	Linear $1.0 \to 0.1$ (default) & 11.963 \\ % exp_id: tau_schedule_sweep
77	Fixed $\tau{=}0.1$ & 12.072 \\ % exp_id: tau_schedule_sweep
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	Temperature schedule has minimal impact ($<$1.8\% PPL variation).
83	The linear annealing default is a conservative choice; even removing annealing entirely (fixed $\tau{=}0.5$) yields comparable performance.
84	
85	\subsection{Training Convergence}
86	\label{app:training_convergence}
87	
88	\begin{table}[h]
89	\centering
90	\caption{Training convergence at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
91	\label{tab:training_convergence}
92	\small
93	\begin{tabular}{cc}
94	\toprule
95	Steps & PPL$\downarrow$ \\
96	\midrule
97	200 & 15.158 \\ % exp_id: training_steps_sweep
98	400 & 12.538 \\ % exp_id: training_steps_sweep
99	600 & 12.046 \\ % exp_id: training_steps_sweep
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
110	\section{Geometric Penalty Schedule Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Geometric penalty schedule convergence across sparsity targets (margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
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
135	The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation; this precision reflects a regime where the target is reachable without $\lambda$ saturation.
136	
137	\begin{figure}[h]
138	\centering
139	\includegraphics[width=\columnwidth]{lagrangian_dynamics.pdf}
140	\caption{Lagrangian controller dynamics for 30\% sparsity target ($\lambda_{\max}=5000$). Left axis (log scale): penalty weight $\lambda$ rises from $0.01$ to its cap once actual sparsity undershoots the target at $\sim$step~150, exhibiting bang-bang oscillations before saturating. Right axis: actual sparsity (solid) converges from the natural density ($\approx$0.41) toward the target (dashed) and stabilizes near 0.28.}
141	\label{fig:lagrangian_dynamics}
142	\end{figure}
143	
144	Temperature $\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.
145	A mild loss increase in the final $\sim$100 steps is expected: as masks become more binary ($\tau \to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.
146	
147	The controller reliably drives actual sparsity to within 5\% of the target across all tested regimes, with $\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.
148	For the 30\% target, actual sparsity is $\approx$28.5\% (5\% deviation). This does not affect conclusions: TEAL at 28.5\% actual sparsity yields PPL 10.30 (vs.\ 10.97 at exact 30\%), a 0.67 PPL difference negligible relative to the KL vs.\ TEAL gap (8.96 vs.\ 10.97).
149	
150	
151	\section{Out-of-Distribution Evaluation}
152	\label{app:ood}
153	
154	To address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\cite{raffel2020c4} validation set under TEAL global allocation.
155	
156	\begin{table}[h]
157	\centering
158	\caption{Out-of-distribution evaluation on C4 validation (PPL$\downarrow$). 30\% KL reports 2-seed mean$\pm$std; other entries use seed 42.}
159	\label{tab:ood}
160	\small
161	\begin{tabular}{llc}
162	\toprule
163	Sparsity & Method & C4 PPL$\downarrow$ \\
164	\midrule
165	0\% & Dense & 9.21 \\
166	\midrule
167	30\% & KL predictor (Ours) & \textbf{16.03$\pm$0.01} \\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123
168	\midrule
169	\multirow{2}{*}{50\%} & KL predictor (Ours) & \textbf{18.40} \\ % exp_id: eval_c4_ood_kl50
170	& TEAL vanilla & 38.75 \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	At the 30\% sparsity level, the KL predictor achieves C4 PPL 16.03$\pm$0.01 (2-seed, global allocation, $1.74\times$ dense), confirming OOD generalization.
176	At 50\%, the KL predictor achieves 52.5\% relative advantage over TEAL (18.40 vs.\ 38.75), comparable to the 50\% advantage on WikiText-2 (11.92 vs.\ 23.90), confirming that KL-trained predictions generalize across distributions.
177	
178	\paragraph{Uniform Allocation.}
179	Under uniform allocation at 30\%, C4 PPL across three seeds is 18.22 (s42), 16.37 (s123), 16.36 (s456), yielding mean 16.98$\pm$1.07 ($1.84\times$ dense). % exp_id: c4_ood_kl30_uniform_3seed
180	The cross-seed variance is substantially higher than in-domain: CV=6.3\% on C4 vs.\ 0.2\% on WikiText-2 (PPL 8.81$\pm$0.02), driven by seed 42's elevated C4 PPL (18.22 vs.\ 16.37 for other seeds).
181	Global allocation's cross-layer budget flexibility partially compensates for domain shift (PPL 16.03 global vs.\ 16.98 uniform), consistent with the Limitations observation that the predictor partially overfits to training-domain activation patterns.
182	
183	\paragraph{Downstream Task Robustness.}
184	Table~\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\ WikiText (in-domain), both at 30\% uniform allocation (seed 42). All six benchmarks show $\Delta$$\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa
185	
186	\begin{table}[h]
187	\centering
188	\caption{Downstream task robustness to calibration domain shift (KL 30\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\_match (GSM8K).}
189	\label{tab:ood_downstream}
190	\small
191	\begin{tabular}{lcccccc}
192	\toprule
193	Calibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
194	\midrule
195	WikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa
196	C4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\ % exp_id: c4_ood_downstream_kl30
197	\midrule
198	$\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	
204	\section{Per-Layer Retention Analysis}
205	\label{app:retention}
206	
207	\begin{figure}[h]
208	\centering
209	\includegraphics[width=\columnwidth]{per_layer_retention_chart.pdf}
210	\caption{Per-layer neuron retention under global top-$k$ allocation at 30\%, 50\%, and 70\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\% (L31) even at 30\% sparsity. At 70\%, starvation extends to mid-layers (L10--12: 16.7--20.1\%), explaining the transition to the capacity-limited regime.}
211	\label{fig:retention}
212	\end{figure}
213	
214	
215	\section{Training Stability}
216	\label{app:stability}
217	
218	Three-seed evaluation ($s \in \{42, 123, 456\}$) at 50\% sparsity under uniform allocation yields PPL $11.92 \pm 0.07$ (CV=0.6\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform
219	Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
220	
221	Under global allocation at 50\%, MMLU is $28.3 \pm 0.7$\%; the near-random performance is capacity-limited rather than seed-sensitive ($\sigma$=0.7pp vs.\ 9.5pp at 30\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval
222	The low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
223	
224	\subsection{Cross-Seed Mask Consistency}
225	\label{app:cross_seed_jaccard}
226	
227	To assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30
228	
229	The mean cross-seed Jaccard distance is 0.363 (IoU = 0.637), substantially lower than the KL-vs-magnitude divergence (0.46--0.68), confirming that KL-discovered patterns form a distinct cluster from magnitude-based masks.
230	Per-layer divergence follows a U-shaped pattern: lowest at embedding-adjacent layers (L0: 0.33), peaking at early layers (L1: 0.41), with a mid-network valley (L12--14: 0.33). The random baseline Jaccard distance is 0.462.
231	
232	While specific mask configurations vary moderately across seeds (Jaccard distance 36.3\%), the resulting PPL is highly stable (8.81$\pm$0.02, CV=0.2\%), suggesting multiple near-equivalent optima in the activation mask space.
233	The cross-seed divergence (36.3\%) is substantially lower than the KL-vs-magnitude divergence (46--68\%), confirming that KL discovers effective patterns that cluster distinctly from magnitude-based selection.
234	
235	
236	\section{MSE Baseline Configuration}
237	\label{app:mse_config}
238	
239	The MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\times}10^{-3}$, weight decay $1{\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\tau$: $1.0 \to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.
240	The only difference is the loss target: per-layer $\|\mathbf{W}_d^{(\ell)}(\tilde{\mathbf{m}}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}) - \mathbf{y}_{\text{dense}}^{(\ell)}\|_2^2$, replacing the end-to-end KL divergence.
241	This controlled comparison isolates the effect of output-distribution alignment: all three predictors see identical data in identical order with identical architectures; only the loss function differs. % exp_id: mse30_uniform_s42, mse50_uniform_s42
242	
243	MSE uses $\lambda_{\max}{=}1000$ (vs.\ KL's 5000) because MSE's per-layer gradient magnitude is approximately $5\times$ larger than KL's end-to-end gradient, requiring proportionally less penalty pressure to achieve comparable sparsity control. Both reach their target sparsity within 110 steps.
244	At 50\% target, MSE converges to the target sparsity for seed 42; however, with seed 123, sparsity reaches only 5.1\% under the same $\lambda_{\max}$ cap (eval PPL$=$15{,}789, random-level), indicating high sensitivity to initialization---a failure mode not observed with KL-based losses.
245	At 30\%, MSE achieves 27.7\% actual sparsity for s42 (gap 2.3pp).
246	The 3-seed MSE mean (18.52$\pm$1.68; s42=20.43, s123=17.73, s456=17.39) is still $1.7\times$ worse than TEAL (10.82), confirming that the performance deficit stems from the loss function, not insufficient sparsity pressure.
247	
248	
249	\section{Extended SNR Analysis}
250	\label{app:snr_extended}
251	
252	Figure~\ref{fig:snr_trajectory} plots gradient SNR across the full 1000-step training for both KL and BCE predictors, measured at 14 checkpoints (LLaMA-3.1-8B, C4) with 95\% bootstrap confidence intervals.
253	From step 100 onward, BCE maintains consistently higher SNR than KL (2.3--17$\times$ depending on training phase), with the gap narrowing toward convergence ($2.3\times$ at step 1000: $2.026{\times}10^{-3}$ vs.\ $8.78{\times}10^{-4}$). % exp_id: snr_full_curve_1000steps
254	Despite KL's noisier gradient signal, KL-trained predictors produce substantially better masks (Table~\ref{tab:main}), confirming that \emph{target alignment} matters more than gradient clarity for mask quality.
255	BCE's higher SNR reflects its simpler per-neuron classification objective, which concentrates gradients on individual neuron decisions; KL's coupled gradient distributes signal across all mask decisions jointly, yielding lower SNR but discovering compositionally superior mask patterns (\S\ref{sec:method:gradient}).
256	
257	\begin{figure}[t]
258	\centering
259	\includegraphics[width=\columnwidth]{snr_trajectory.pdf}
260	\caption{Gradient SNR trajectory across 1000 training steps. BCE (orange) maintains consistently higher SNR than KL (blue) from step 100 onward (2.3--17$\times$), yet KL produces superior masks (Table~\ref{tab:main}), suggesting that target alignment matters more than gradient clarity for mask quality.}
261	\label{fig:snr_trajectory}
262	\end{figure}
263	
264	
265	\section{Extended Downstream Evaluation}
266	\label{app:downstream}
267	
268	Table~\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.
269	
270	\begin{table}[h]
271	\centering
272	\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\% uniform: 3-seed mean$\pm$std; others: seed 42.}
273	\label{tab:downstream}
274	\small
275	\begin{tabular}{llcc}
276	\toprule
277	Sparsity & Method & HellaSwag & PIQA \\
278	\midrule
279	0\% & Dense & \textbf{82.35} & \textbf{80.90} \\
280	\midrule
281	\multirow{3}{*}{30\%}
282	& KL uniform & \textbf{71.07$\pm$0.54} & \textbf{74.95$\pm$0.25} \\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)
283	& TEAL uniform & 63.31 & 72.80 \\ % exp_id: bench_teal30_uniform_6task
284	& BCE isocompute & 62.81 & 74.21 \\ % exp_id: bce_isocompute_30u_hellaswag_piqa
285	\midrule
286	\multirow{3}{*}{50\%}
287	& KL global & \textbf{58.95} & \textbf{69.48} \\ % exp_id: hellaswag_piqa_kl50_global
288	& KL uniform & 56.66 & 69.10 \\ % exp_id: hellaswag_piqa_kl50_uniform
289	& TEAL uniform & 39.35 & 63.66 \\ % exp_id: bench_teal50_uniform_6task
290	\bottomrule
291	\end{tabular}
292	\end{table}
293	
294	At 30\%, the KL predictor retains 86.3\% of dense HellaSwag accuracy (71.07$\pm$0.54 vs.\ 82.35, 3-seed) and 92.6\% of PIQA (74.95$\pm$0.25 vs.\ 80.90), confirming moderate degradation on non-reasoning tasks.
295	At 50\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\S\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).
296	
297	
298	\section{Compensation Training Convergence}
299	\label{app:comp_convergence}
300	
301	All compensation networks~\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\% s42 (final loss 0.70), 30\% s456 (0.68), 50\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42
302	
303	
304	\section{Qwen-2.5-14B Detailed Results}
305	\label{app:14b}
306	
307	\begin{table}[h]
308	\centering
309	\caption{Qwen-2.5-14B at 30\% nominal sparsity. Actual sparsity differs: KL 29.6\% (3-seed), TEAL 29.3\% (target 30\%). \textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\% native sparsity (\S\ref{sec:method:gradient}), so forced global top-$k$ is used.}
310	\label{tab:14b}
311	\small
312	\resizebox{\columnwidth}{!}{
313	\begin{tabular}{lcccccccc}
314	\toprule
315	Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
316	\midrule
317	Dense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\
318	\midrule
319	\multicolumn{8}{l}{\emph{Global top-$k$ allocation}} \\
320	KL (Ours) & \textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \textbf{75.01} & \textbf{77.37} \\ % exp_id: qwen14b_kl30_s42
321	TEAL & 8.73 & 56.83 & \textbf{72.69} & \textbf{71.83} & 49.51 & 70.51 & 74.70 \\ % exp_id: qwen14b_teal30_eval
322	BCE & 8.76 & \textbf{57.59} & 72.61 & 71.67 & \textbf{53.07} & 53.43 & 68.28 \\ % exp_id: qwen14b_bce30_s42_eval
323	\midrule
324	\multicolumn{8}{l}{\emph{Uniform allocation}} \\
325	KL (Ours) & \textbf{7.90} & 53.50 & \textbf{72.82} & 63.55 & 32.2$\pm$5.3 & \textbf{72.68$\pm$0.2} & \textbf{76.01$\pm$1.1} \\ % exp_id: qwen14b_kl30_uniform (3-seed s42/s123(v4)/s456)
326	TEAL & 8.01 & \textbf{55.29} & 69.85 & \textbf{66.34} & \textbf{52.1} & 67.72 & 74.70 \\ % exp_id: qwen14b_teal30_uniform
327	\bottomrule
328	\multicolumn{8}{l}{\footnotesize GSM8K: 3-seed (s42/s123(v4)/s456).} \\
329	\end{tabular}}
330	\end{table}
331	
332	Under global allocation, BCE's HellaSwag drops to 53.43\% ($-$17pp vs.\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval
333	
334	\section{Full Allocation Analysis}
335	\label{app:alloc_full}
336	
337	\begin{table}[t]
338	\centering
339	\caption{Allocation summary (LLaMA-3.1-8B). $\pm$: 3-seed; $^\ast$high seed variance.}
340	\label{tab:phase}
341	\footnotesize
342	\begin{tabular}{llcc}
343	\toprule
344	Sparsity & Allocation & PPL$\downarrow$ & MMLU \\
345	\midrule
346	\multirow{2}{*}{30\%}
347	& Global & 8.96$\pm$0.02 & 35.7$\pm$9.5$^\ast$ \\ % exp_id: kl30_3seed_global
348	& Uniform & \textbf{8.81$\pm$0.02} & \textbf{40.7$\pm$1.3} \\ % exp_id: bench_kl30_uniform
349	\midrule
350	\multirow{2}{*}{50\%}
351	& Global & \textbf{11.84$\pm$0.15} & \textbf{28.3$\pm$0.7} \\ % exp_id: bench_kl50_global, kl50_global_s123_reeval, kl50_global_s123_downstream_v2, kl50_global_s456_eval
352	& Uniform & 11.92$\pm$0.07 & 28.0$\pm$0.6 \\ % exp_id: multi_seed_kl50_uniform
353	\bottomrule
354	\end{tabular}
355	\end{table}
356	
357	Table~\ref{tab:phase_full} extends Table~\ref{tab:phase} with all downstream metrics.
358	
359	\begin{table*}[t]
360	\centering
361	\caption{Full allocation analysis: global top-$k$ vs.\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\pm$: 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); others: seed 42. $^\ast$High MMLU seed variance (individual seeds span 25.3--43.5\%).}
362	\label{tab:phase_full}
363	\begin{tabular}{llccccc}
364	\toprule
365	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
366	\midrule
367	\multirow{2}{*}{25\%}
368	& Global & \textbf{8.17} & 45.4 & 70.6 & \textbf{46.6} & \textbf{11.5} \\
369	& Uniform & 8.23 & \textbf{46.5} & \textbf{71.8} & 44.0 & 11.0 \\
370	\midrule
371	\multirow{2}{*}{30\%}
372	& Global & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5$^\ast$ & \textbf{8.0$\pm$0.7} \\
373	& Uniform & \textbf{8.81$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & \textbf{40.7$\pm$1.3} & 7.5$\pm$0.1 \\
374	\midrule
375	\multirow{2}{*}{35\%}
376	& Global & \textbf{9.31} & \textbf{38.9} & \textbf{67.6} & \textbf{40.4} & \textbf{7.7} \\
377	& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\
378	\midrule
379	\multirow{2}{*}{40\%}
380	& Global & \textbf{10.14} & 39.5 & \textbf{67.5} & \textbf{39.5} & \textbf{6.6} \\
381	& Uniform & 10.76 & \textbf{39.6} & 63.1 & 35.5 & 3.6 \\
382	\midrule
383	\multirow{2}{*}{45\%}
384	& Global & \textbf{10.80} & \textbf{39.2} & \textbf{64.6} & 30.4 & \textbf{3.0} \\
385	& Uniform & 10.95 & 37.6 & 63.6 & \textbf{30.6} & 2.7 \\
386	\midrule
387	\multirow{2}{*}{50\%}
388	& Global & \textbf{11.84$\pm$0.15} & \textbf{36.3$\pm$3.2} & \textbf{63.8$\pm$0.3} & \textbf{28.3$\pm$0.7} & \textbf{2.7$\pm$1.3} \\
389	& Uniform & 11.92$\pm$0.07 & 33.8$\pm$1.2 & 62.9$\pm$0.1 & 28.0$\pm$0.6 & 2.2$\pm$0.1 \\
390	\bottomrule
391	\end{tabular}
392	\end{table*}
393	
394	
395	\section{Mask Pattern Visualization}
396	\label{app:mask_viz}
397	
398	Figure~\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\% and 50\% sparsity.
399	Figure~\ref{fig:scatter} shows per-neuron importance scores at layer 16.
400	Figure~\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.
401	
402	\begin{figure}[t]
403	\centering
404	\includegraphics[width=0.95\columnwidth]{neuron_scatter_layer16.pdf}
405	\caption{KL vs.\ magnitude importance scores for layer 16 neurons at 50\% sparsity. 41\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}
406	\label{fig:scatter}
407	\end{figure}
408	
409	\begin{figure*}[t]
410	\centering
411	\includegraphics[width=\textwidth]{mask_divergence_heatmap.pdf}
412	\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\% and 50\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\%) and increases with sparsity across all layers.}
413	\label{fig:mask_heatmap}
414	\end{figure*}
415	
416	\begin{figure*}[t]
417	\centering
418	\includegraphics[width=\textwidth]{mask_comparison.pdf}
419	\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\% and 50\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\%, 0.74 at 50\%).}
420	\label{fig:mask_comparison}
421	\end{figure*}
422	
423	
424	\section{Cross-Architecture Comparison}
425	\label{app:cross_arch}
426	
427	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
428	
429	\begin{table}[h]
430	\centering
431	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. \textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\%: 3-seed mean$\pm$std; other rows: seed 42.}
432	\label{tab:cross_arch}
433	\small
434	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
435	\toprule
436	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
437	 & KL & TEAL & Adv & KL & TEAL & Adv \\
438	\midrule
439	30\% & \textbf{6.93$\pm$0.19} & 8.38 & 1.21$\times$ & \textbf{8.96} & 10.97 & 1.22$\times$ \\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, teal_30_mistral, kl30_3seed_global
440	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
441	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
442	\bottomrule
443	\end{tabular}
444	\end{table}
445	
446	The KL PPL advantage ratio is consistent across architectures (within 8\% at $\leq$50\% sparsity).
447	Table~\ref{tab:mistral_downstream} reports downstream task accuracy at 30\% sparsity on Mistral-7B-v0.3 (3-seed). KL improves PPL ($-$17.3\%) and commonsense tasks (WG +6.7pp) but MMLU is tied (43.3\% vs.\ 43.5\%); ARC-c shows high seed variance ($\sigma$=6.4pp); GSM8K reverses.
448	
449	\begin{table}[h]
450	\centering
451	\caption{Mistral-7B-v0.3 downstream evaluation at 30\% sparsity. $\pm$: 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); TEAL is deterministic (single run). ARC-c exhibits high seed variance ($\sigma$=6.4pp).}
452	\label{tab:mistral_downstream}
453	\small
454	\resizebox{\columnwidth}{!}{
455	\begin{tabular}{lccccccc}
456	\toprule
457	Method & PPL$\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\
458	\midrule
459	Dense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa
460	KL 30\% & \textbf{6.93$\pm$0.19} & \textbf{44.9$\pm$6.4} & \textbf{70.2$\pm$1.2} & \textbf{69.7$\pm$0.8} & \textbf{74.8$\pm$0.4} & 43.3$\pm$1.5 & 8.6$\pm$2.2 \\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456
461	TEAL 30\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & \textbf{43.5} & \textbf{15.9} \\ % exp_id: mistral_teal30_downstream
462	\bottomrule
463	\end{tabular}}
464	\end{table}
465	
466	
467	\section{Taxonomy Discussion}
468	\label{app:taxonomy}
469	
470	\paragraph{Correction granularity.}
471	\emph{Static} methods~\cite{xu2025spon} learn a fixed bias vector per layer that does not depend on the input token.
472	\emph{Per-token} methods~\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.
473	
474	\paragraph{Training signal coupling.}
475	\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.
476	\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.
477	\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass; each mask decision's gradient reflects its joint effect with all other masks on the final distribution.
478	
479	SPON~\cite{xu2025spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\times$ coupled).
480	DejaVu~\cite{liu2023dejavu} and FastForward~\cite{gautam2026fastforward} achieve per-token granularity but use BCE, where each neuron's gradient is independent of other mask states.
481	D2DMoE~\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.
482	We define \emph{output-distribution alignment} as whether the training loss optimizes a quantity that composes across layers.
483	KL on output logits directly optimizes next-token prediction loss, which does not suffer from error composition; per-layer MSE minimizes reconstruction error independently at each layer, but layer-wise optima do not compose---a mask minimizing FFN output error at layer $\ell$ may amplify errors in layers $\ell{+}1 \ldots L$.
484	The SNR analysis (\S\ref{sec:method:gradient}) corroborates this: KL achieves the best masks despite $2.3\times$ lower SNR than BCE, while MSE produces the worst masks.
485	The framework predicts that losses operating on output-level quantities should outperform intermediate-level losses, a hypothesis consistent with our MSE results and testable with alternative output-level objectives.
486	
487	\section{Oracle Mask Provenance}
488	\label{app:oracle_provenance}
489	
490	C1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold (logits $> 0$, equivalent to $\sigma > 0.5$); they reflect one specific training trajectory (optimizer state, data order, Gumbel noise).
491	The s42/s123/s456 consistency ($\leq$1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.
492	
493	\section{SPON Orthogonality}
494	\label{app:spon}
495	
496	SPON~\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\% PPL improvement (12.08$\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
497	The decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.
498	
499	\section{Per-Layer KL Downstream Decomposition}
500	\label{app:perlayer_downstream}
501	
502	Table~\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\ coupling scope decomposition at 30\% sparsity (\S\ref{sec:perlayer}). BoolQ's $\approx$100\% coupling is an upper bound confounded by high cross-seed variance ($\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.
503	
504	\begin{table}[h]
505	\centering
506	\caption{2D decomposition at 30\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \S\ref{sec:perlayer}).}
507	\label{tab:perlayer_downstream}
508	\resizebox{\columnwidth}{!}{
509	\begin{tabular}{lcccccc}
510	\toprule
511	& PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\
512	\midrule
513	E2E KL & 8.81$\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\
514	Per-layer KL & 9.05$\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\
515	MSE & 18.52$\pm$1.68 & 35.8$\pm$4.1 & 59.8$\pm$2.6 & 30.7$\pm$2.6 & 2.3$\pm$0.7 & 64.5$\pm$5.3 \\
516	\midrule
517	Total gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\
518	Signal type (\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\approx$0 \\
519	Coupling (\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\approx$100 \\
520	\bottomrule
521	\end{tabular}}
522	\end{table}
523	
524	\section{$K{=}4$ Mismatch Control}
525	\label{app:k4_downstream}
526	
527	Table~\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\% sparsity.
528	Training with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\ 1/32 layers masked during training, while inference applies all 32).
529	The gap closure column reports the fraction of the $K{=}1 \to$ E2E KL gap closed by $K{=}4$.
530	
531	\begin{table}[h]
532	\centering
533	\caption{3-seed $K{=}4$ mismatch control at 30\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \in \{42, 123, 456\}$). Actual sparsity 29.6\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\text{E2E} - K{=}1) \times 100$.}
534	\label{tab:k4_downstream}
535	\resizebox{\columnwidth}{!}{
536	\begin{tabular}{lcccc}
537	\toprule
538	& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\%) \\
539	\midrule
540	PPL$\downarrow$ & 8.89$\pm$0.01 & 9.05$\pm$0.02 & 8.81$\pm$0.02 & 66.7 \\
541	ARC-c & 40.0$\pm$1.3 & 39.9 & 43.7$\pm$2.5 & 2.6 \\
542	WG & 66.9$\pm$0.2 & 65.9 & 68.9$\pm$0.4 & 33.3 \\
543	MMLU$^\ast$ & 42.7$\pm$1.4 & 38.6 & 40.7$\pm$1.3 & $>$100 \\
544	GSM8K & 7.0$\pm$1.6 & 5.8 & 7.5$\pm$0.1 & 70.6 \\
545	BoolQ$^\dagger$ & 67.7$\pm$7.5 & 64.5$\pm$11.5 & 73.7 & 34.8 \\
546	\bottomrule
547	\end{tabular}}
548	\vspace{2pt}
549	{\footnotesize $^\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\% (Appendix~\ref{app:constraint}).
550	$^\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}
551	\end{table}
552	
553	\section{Per-Layer Sparsity Constraint Analysis}
554	\label{app:constraint}
555	
556	To test the causal role of the KL predictor's learned per-layer allocation, we evaluate two inference-time interventions at 30\% overall sparsity (seed 42, uniform allocation baseline):
557	
558	\begin{table}[h]
559	\centering
560	\caption{Per-layer sparsity constraint analysis. \emph{Protect late}: cap L22--L28 sparsity $\leq$30\%; \emph{Remove valley}: override L14--L18 sparsity to 30\%. Budget redistributed to maintain 30\% overall.}
561	\label{tab:constraint}
562	\begin{tabular}{lcccc}
563	\toprule
564	Condition & PPL & ARC-c & MMLU & GSM8K \\
565	\midrule
566	KL baseline (s42) & 8.82 & 40.8 & 40.6 & 7.4 \\
567	Protect late layers & 9.26 & 42.4 & 40.7 & 6.5 \\
568	Remove valley & 8.76 & 39.3 & 44.0 & 9.0 \\
569	\bottomrule
570	\end{tabular}
571	\end{table}
572	
573	Protecting late layers (L22--L28) does not improve knowledge-intensive metrics despite reducing their sparsity from 48--57\% to $\leq$30\%, while worsening PPL by 5.2\%.
574	Conversely, removing the protection valley (forcing L14--L18 to 30\% instead of 14--18\%) improves MMLU by +3.4pp and GSM8K by +1.6pp at the cost of ARC-c $-$1.5pp.
575	The KL predictor's learned allocation thus represents a task-dependent trade-off---prioritizing commonsense reasoning via middle-layer protection---rather than a uniformly optimal pattern.
576	This allocation trade-off also explains the $K{=}4$ MMLU anomaly (\S\ref{app:k4_downstream}): $K{=}4$'s near-uniform learned sparsity (std=0.003) inherently removes the valley, producing MMLU=43.5 comparable to the remove-valley condition (44.0).
577	
578	\section{Per-Layer Sparsity Distribution}
579	\label{app:perlayer_sparsity}
580	
581	The KL predictor at 30\% target sparsity learns a non-uniform per-layer allocation that differs markedly from magnitude-based selection.
582	Aggregate sparsity is similar across broad regions (early L0--L7: KL 28.1\% vs.\ magnitude 27.5\%; late L24--L31: 44.9\% vs.\ 47.2\%), but middle layers (L8--L23) exhibit high internal variance despite similar averages (28.2\% vs.\ 27.3\%).
583	Table~\ref{tab:perlayer_sparsity} highlights three sub-ranges.
584	
585	\begin{table}[h]
586	\centering
587	\caption{Per-layer sparsity sub-ranges: KL predictor vs.\ magnitude (LLaMA-3.1-8B, 30\%, uniform allocation). Ranges denote min--max across layers in each group.}
588	\label{tab:perlayer_sparsity}
589	\begin{tabular}{lccc}
590	\toprule
591	Layer Range & KL (\%) & Mag (\%) & $\Delta$ (pp) \\
592	\midrule
593	L8--L12 (high pruning) & 32--36 & 25--26 & $+$7 to $+$10 \\
594	L14--L18 (protection valley) & 14--18 & 28--30 & $-$8 to $-$16 \\
595	L22--L28 (aggressive pruning) & 48--57 & --- & --- \\
596	\bottomrule
597	\end{tabular}
598	\end{table}
599	
600	\section{C4 Training Data Control}
601	\label{app:c4_control}
602	
603	To test whether WikiText-103's narrow domain drives the knowledge-task regression (\S\ref{sec:experiments}), we train the KL predictor on C4~\cite{raffel2020c4} (diverse web text) under identical hyperparameters (1000 steps, 30\% uniform, s42).
604	
605	\begin{table}[h]
606	\centering
607	\caption{C4-trained vs.\ WikiText-trained KL predictor (LLaMA-3.1-8B, 30\% uniform, s42).}
608	\label{tab:c4_control}
609	\resizebox{\columnwidth}{!}{
610	\begin{tabular}{lcccccc}
611	\toprule
612	Training Data & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\
613	\midrule
614	WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa
615	C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\ % exp_id: c4_kl30_s42_eval
616	\bottomrule
617	\end{tabular}}
618	\end{table}
619	
620	The C4-trained predictor achieves comparable MMLU (40.0\% vs.\ 40.6\%) but worse GSM8K (4.1\% vs.\ 7.4\%) and higher PPL (11.55 vs.\ 8.82), despite training on more diverse text.
621	This rules out training data composition as the primary cause of knowledge-task regression and supports the hypothesis that forward KL's mode-covering property structurally under-protects rare reasoning-critical activations. % exp_id: c4_control_eval
622	
623	\section{Per-Layer Coupling Breadth Analysis}
624	\label{app:k_curve}
625	
626	We vary the number of layers coupled per training step ($K$) from 1 (pure per-layer) to 32 (end-to-end), evaluating all predictors under TEAL uniform allocation at 30\% sparsity on LLaMA-3.1-8B.
627	
628	\begin{table}[h]
629	\centering
630	\caption{K-curve: coupling breadth vs.\ predictor quality (30\%, TEAL uniform, LLaMA-3.1-8B). All values are 3-seed mean$\pm$std (s42/s123/s456) except $K{=}1$ downstream (single seed). ``---'' = not evaluated.}
631	\label{tab:k_curve}
632	\resizebox{\columnwidth}{!}{
633	\begin{tabular}{cccccccc}
634	\toprule
635	$K$ & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
636	\midrule
637	1 & 9.05$\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & --- & --- \\
638	2 & 10.75$\pm$0.15 & 39.7$\pm$1.2 & 63.2$\pm$1.7 & 38.3$\pm$3.2 & 2.8$\pm$0.6 & 66.5$\pm$1.0 & 73.5$\pm$0.7 \\
639	4 & 8.89$\pm$0.01 & 40.0$\pm$1.2 & 66.9$\pm$0.2 & 42.7$\pm$1.4 & 7.0$\pm$1.6 & 67.8$\pm$1.0 & 74.5$\pm$0.5 \\
640	8 & 9.00$\pm$0.06 & 40.7$\pm$1.0 & 68.7$\pm$1.3 & 40.4$\pm$0.6 & 6.8$\pm$1.3 & 69.0$\pm$1.1 & 75.1$\pm$1.1 \\
641	16 & 8.67$\pm$0.02 & 41.9$\pm$1.1 & 68.5$\pm$0.9 & 40.9$\pm$2.9 & 8.5$\pm$1.2 & 70.1$\pm$0.4 & 75.0$\pm$0.8 \\
642	32 (E2E) & 8.81$\pm$0.02 & 43.7$\pm$2.5 & 68.9$\pm$0.4 & 40.7$\pm$1.3 & 7.5$\pm$0.1 & --- & --- \\
643	\bottomrule
644	\end{tabular}}
645	\end{table}
646	
647	PPL exhibits a non-monotonic U-shape (Figure~\ref{fig:k_curve_ppl}): $K{=}2$ is worst (10.75$\pm$0.15), likely due to insufficient per-layer updates (${\sim}$62 updates/layer vs.\ ${\sim}$250 at $K{=}8$). $K{=}16$ achieves the lowest PPL (8.67$\pm$0.02), marginally better than E2E (8.81$\pm$0.02). $K{=}16$ MMLU exhibits high seed variance (std=2.9; s42=44.0, s123=40.0, s456=38.7), with the 3-seed mean (40.9) indistinguishable from E2E (40.7$\pm$1.3).
648	The signal type gap ($K{=}1$ KL 9.05 vs.\ per-layer MSE 18.52$\pm$1.68) of 9.47 PPL dwarfs the coupling breadth range within KL (best $K{=}16$ 8.67 vs.\ worst $K{=}2$ 10.75 = 2.08 PPL), reinforcing that output-distribution alignment, not coupling scope, is the primary quality lever for PPL at this sparsity level. % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed, perlayer_kl_30_3seed, perlayer_kl_k4_3seed
649	
650	\section{Licenses}
651	\label{app:licenses}
652	
653	LLaMA-3.1-8B is released under the Llama 3.1 Community License Agreement.
654	Mistral-7B-v0.3 is released under the Apache 2.0 License.
655	Qwen-2.5-14B is released under the Apache 2.0 License.
656	WikiText-103 and WikiText-2~\cite{merity2017pointer} are released under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).
657	All evaluation benchmarks (ARC, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA) are publicly available under their respective licenses.
658	Our code will be released under the MIT License upon acceptance.
659	
660	\section{Use of AI Assistants}
661	\label{app:ai-assistants}
662	
663	We used Claude (Anthropic) as an AI coding and writing assistant
664	throughout this work. Specifically:
665	\begin{itemize}
666	    \item \textbf{Code:} drafting experiment scripts, data-processing
667	    pipelines, and analysis utilities; debugging and refactoring.
668	    \item \textbf{Writing:} drafting and revising paper sections,
669	    polishing prose, and reformatting LaTeX.
670	    \item \textbf{Literature:} summarizing related papers to inform
671	    related-work section.
672	\end{itemize}
673	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "646584d3-cc5c-4ab2-8101-edf1fbaf2f46",
  "isSidechain": false,
  "promptId": "fdfb0d6d-9233-4c2a-afaa-5df266af136f",
  "type": "user",
  "uuid": "7f5b5c1b-020d-454b-aa52-023a7b62c940",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Inference Efficiency}\n\\label{app:latency}\n\nTable~\\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Sparsity & ms/fwd & tok/s & Overhead \\\\\n\\midrule\nDense & 0\\% & 119.11$\\pm$0.57 & 17{,}195 & --- \\\\\n\\midrule\nKL predictor-only & 30\\% & 126.64$\\pm$0.70 & 16{,}172 & +6.3\\% \\\\ % exp_id: latency_bench\nKL predictor-only & 50\\% & 126.78$\\pm$0.31 & 16{,}154 & +6.4\\% \\\\ % exp_id: latency_bench\n\\midrule\nPredictor + compensation & 30\\% & 129.94$\\pm$0.75 & 15{,}761 & +9.1\\% \\\\ % exp_id: latency_bench\nPredictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full KL-sparse pipeline adds 6.4\\% overhead to dense inference (126.78 vs.\\ 119.11\\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\\,ms (2.7\\%); the remainder arises from mask application and sparse FFN indexing.\nEliminating the compensation network saves an additional $\\sim$2.7\\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.\nThe overhead is near-identical at 30\\% and 50\\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.\n\nNote that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.\nThe pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\nOur contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.\n\n\n\\section{Predictor Bottleneck Sensitivity}\n\\label{app:db_sensitivity}\n\nTable~\\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Predictor bottleneck sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}\n\\label{tab:db_sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$d_b$ & Params & TEAL global & $\\Delta$ & Per-token \\\\\n\\midrule\n64 & 38.2M (0.48\\%) & 12.076 & +0.9\\% & 10.16 \\\\ % exp_id: db_sensitivity_sweep\n128 & 75.9M (0.95\\%) & 11.963 & --- & 9.218 \\\\ % exp_id: db_sensitivity_sweep\n256 & 151.5M (1.89\\%) & 12.105 & +1.2\\% & 8.586 \\\\ % exp_id: db_sensitivity_sweep\n512 & 302.5M (3.77\\%) & 12.315 & +2.9\\% & 7.93 \\\\ % exp_id: db_sensitivity_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\\to$7.93).\nThis divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.\nThe $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\n\n\\subsection{Temperature Schedule Sensitivity}\n\\label{app:tau_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature schedule sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:tau_sensitivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n$\\tau$ Schedule & PPL$\\downarrow$ \\\\\n\\midrule\nFixed $\\tau{=}0.5$ & \\textbf{11.861} \\\\ % exp_id: tau_schedule_sweep\nLinear $1.0 \\to 0.1$ (default) & 11.963 \\\\ % exp_id: tau_schedule_sweep\nFixed $\\tau{=}0.1$ & 12.072 \\\\ % exp_id: tau_schedule_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature schedule has minimal impact ($<$1.8\\% PPL variation).\nThe linear annealing default is a conservative choice; even removing annealing entirely (fixed $\\tau{=}0.5$) yields comparable performance.\n\n\\subsection{Training Convergence}\n\\label{app:training_convergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training convergence at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:training_convergence}\n\\small\n\\begin{tabular}{cc}\n\\toprule\nSteps & PPL$\\downarrow$ \\\\\n\\midrule\n200 & 15.158 \\\\ % exp_id: training_steps_sweep\n400 & 12.538 \\\\ % exp_id: training_steps_sweep\n600 & 12.046 \\\\ % exp_id: training_steps_sweep\n800 & 11.907 \\\\ % exp_id: training_steps_sweep\n1000 & \\textbf{11.906} \\\\ % exp_id: training_steps_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining converges rapidly: 95\\% of the quality gap closes by step 600, and performance saturates by step 800 ($\\Delta < 0.001$ between 800 and 1000 steps).\nOur default of 1000 steps provides a conservative margin.\n\n\n\\section{Geometric Penalty Schedule Dynamics}\n\\label{app:lagrangian}\n\nTable~\\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.\nThe geometric doubling pattern ($1 \\to 2 \\to 4 \\to 8 \\to \\ldots$) enables $\\lambda$ to reach steady state within $\\sim$10 steps; the deadzone ($\\epsilon = 0.02$) then stabilizes $\\lambda$ once actual sparsity is within $\\pm$2\\% of the target.\n\n\\begin{table}[h]\n\\centering\n\\caption{Geometric penalty schedule convergence across sparsity targets (margin $\\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}\n\\label{tab:lagrangian}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTarget $\\rho$ & $\\lambda_{\\max}$ & Final $\\lambda$ & Actual sparsity & Deviation \\\\\n\\midrule\n30\\% & 5000 & 5000 (cap) & 0.285 & 5.0\\% \\\\ % exp_id: kl_30pct_s42\n40\\% & 5000 & 625 & 0.398 & 0.5\\% \\\\ % exp_id: kl_40pct_s42\n50\\% & 1000 & 8 & 0.504 & 0.8\\% \\\\ % exp_id: kl_50pct_s42\n70\\% & 1000 & 1000 (cap) & 0.688 & 1.7\\% \\\\ % exp_id: kl_70pct_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 50\\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.\nAt 30\\% and 70\\%, the gap between the gate prior and target is larger, driving $\\lambda$ to its respective caps.\nThe 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation; this precision reflects a regime where the target is reachable without $\\lambda$ saturation.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{lagrangian_dynamics.pdf}\n\\caption{Lagrangian controller dynamics for 30\\% sparsity target ($\\lambda_{\\max}=5000$). Left axis (log scale): penalty weight $\\lambda$ rises from $0.01$ to its cap once actual sparsity undershoots the target at $\\sim$step~150, exhibiting bang-bang oscillations before saturating. Right axis: actual sparsity (solid) converges from the natural density ($\\approx$0.41) toward the target (dashed) and stabilizes near 0.28.}\n\\label{fig:lagrangian_dynamics}\n\\end{figure}\n\nTemperature $\\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.\nA mild loss increase in the final $\\sim$100 steps is expected: as masks become more binary ($\\tau \\to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.\n\nThe controller reliably drives actual sparsity to within 5\\% of the target across all tested regimes, with $\\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.\nFor the 30\\% target, actual sparsity is $\\approx$28.5\\% (5\\% deviation). This does not affect conclusions: TEAL at 28.5\\% actual sparsity yields PPL 10.30 (vs.\\ 10.97 at exact 30\\%), a 0.67 PPL difference negligible relative to the KL vs.\\ TEAL gap (8.96 vs.\\ 10.97).\n\n\n\\section{Out-of-Distribution Evaluation}\n\\label{app:ood}\n\nTo address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\\cite{raffel2020c4} validation set under TEAL global allocation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Out-of-distribution evaluation on C4 validation (PPL$\\downarrow$). 30\\% KL reports 2-seed mean$\\pm$std; other entries use seed 42.}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{llc}\n\\toprule\nSparsity & Method & C4 PPL$\\downarrow$ \\\\\n\\midrule\n0\\% & Dense & 9.21 \\\\\n\\midrule\n30\\% & KL predictor (Ours) & \\textbf{16.03$\\pm$0.01} \\\\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123\n\\midrule\n\\multirow{2}{*}{50\\%} & KL predictor (Ours) & \\textbf{18.40} \\\\ % exp_id: eval_c4_ood_kl50\n& TEAL vanilla & 38.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the 30\\% sparsity level, the KL predictor achieves C4 PPL 16.03$\\pm$0.01 (2-seed, global allocation, $1.74\\times$ dense), confirming OOD generalization.\nAt 50\\%, the KL predictor achieves 52.5\\% relative advantage over TEAL (18.40 vs.\\ 38.75), comparable to the 50\\% advantage on WikiText-2 (11.92 vs.\\ 23.90), confirming that KL-trained predictions generalize across distributions.\n\n\\paragraph{Uniform Allocation.}\nUnder uniform allocation at 30\\%, C4 PPL across three seeds is 18.22 (s42), 16.37 (s123), 16.36 (s456), yielding mean 16.98$\\pm$1.07 ($1.84\\times$ dense). % exp_id: c4_ood_kl30_uniform_3seed\nThe cross-seed variance is substantially higher than in-domain: CV=6.3\\% on C4 vs.\\ 0.2\\% on WikiText-2 (PPL 8.81$\\pm$0.02), driven by seed 42's elevated C4 PPL (18.22 vs.\\ 16.37 for other seeds).\nGlobal allocation's cross-layer budget flexibility partially compensates for domain shift (PPL 16.03 global vs.\\ 16.98 uniform), consistent with the Limitations observation that the predictor partially overfits to training-domain activation patterns.\n\n\\paragraph{Downstream Task Robustness.}\nTable~\\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\\ WikiText (in-domain), both at 30\\% uniform allocation (seed 42). All six benchmarks show $\\Delta$$\\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream task robustness to calibration domain shift (KL 30\\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\\_match (GSM8K).}\n\\label{tab:ood_downstream}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nCalibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nWikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\\\ % exp_id: c4_ood_downstream_kl30\n\\midrule\n$\\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Layer Retention Analysis}\n\\label{app:retention}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{per_layer_retention_chart.pdf}\n\\caption{Per-layer neuron retention under global top-$k$ allocation at 30\\%, 50\\%, and 70\\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\\% (L31) even at 30\\% sparsity. At 70\\%, starvation extends to mid-layers (L10--12: 16.7--20.1\\%), explaining the transition to the capacity-limited regime.}\n\\label{fig:retention}\n\\end{figure}\n\n\n\\section{Training Stability}\n\\label{app:stability}\n\nThree-seed evaluation ($s \\in \\{42, 123, 456\\}$) at 50\\% sparsity under uniform allocation yields PPL $11.92 \\pm 0.07$ (CV=0.6\\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform\nDownstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\n\nUnder global allocation at 50\\%, MMLU is $28.3 \\pm 0.7$\\%; the near-random performance is capacity-limited rather than seed-sensitive ($\\sigma$=0.7pp vs.\\ 9.5pp at 30\\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\nThe low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.\n\n\\subsection{Cross-Seed Mask Consistency}\n\\label{app:cross_seed_jaccard}\n\nTo assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30\n\nThe mean cross-seed Jaccard distance is 0.363 (IoU = 0.637), substantially lower than the KL-vs-magnitude divergence (0.46--0.68), confirming that KL-discovered patterns form a distinct cluster from magnitude-based masks.\nPer-layer divergence follows a U-shaped pattern: lowest at embedding-adjacent layers (L0: 0.33), peaking at early layers (L1: 0.41), with a mid-network valley (L12--14: 0.33). The random baseline Jaccard distance is 0.462.\n\nWhile specific mask configurations vary moderately across seeds (Jaccard distance 36.3\\%), the resulting PPL is highly stable (8.81$\\pm$0.02, CV=0.2\\%), suggesting multiple near-equivalent optima in the activation mask space.\nThe cross-seed divergence (36.3\\%) is substantially lower than the KL-vs-magnitude divergence (46--68\\%), confirming that KL discovers effective patterns that cluster distinctly from magnitude-based selection.\n\n\n\\section{MSE Baseline Configuration}\n\\label{app:mse_config}\n\nThe MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\\times}10^{-3}$, weight decay $1{\\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\\tau$: $1.0 \\to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.\nThe only difference is the loss target: per-layer $\\|\\mathbf{W}_d^{(\\ell)}(\\tilde{\\mathbf{m}}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}) - \\mathbf{y}_{\\text{dense}}^{(\\ell)}\\|_2^2$, replacing the end-to-end KL divergence.\nThis controlled comparison isolates the effect of output-distribution alignment: all three predictors see identical data in identical order with identical architectures; only the loss function differs. % exp_id: mse30_uniform_s42, mse50_uniform_s42\n\nMSE uses $\\lambda_{\\max}{=}1000$ (vs.\\ KL's 5000) because MSE's per-layer gradient magnitude is approximately $5\\times$ larger than KL's end-to-end gradient, requiring proportionally less penalty pressure to achieve comparable sparsity control. Both reach their target sparsity within 110 steps.\nAt 50\\% target, MSE converges to the target sparsity for seed 42; however, with seed 123, sparsity reaches only 5.1\\% under the same $\\lambda_{\\max}$ cap (eval PPL$=$15{,}789, random-level), indicating high sensitivity to initialization---a failure mode not observed with KL-based losses.\nAt 30\\%, MSE achieves 27.7\\% actual sparsity for s42 (gap 2.3pp).\nThe 3-seed MSE mean (18.52$\\pm$1.68; s42=20.43, s123=17.73, s456=17.39) is still $1.7\\times$ worse than TEAL (10.82), confirming that the performance deficit stems from the loss function, not insufficient sparsity pressure.\n\n\n\\section{Extended SNR Analysis}\n\\label{app:snr_extended}\n\nFigure~\\ref{fig:snr_trajectory} plots gradient SNR across the full 1000-step training for both KL and BCE predictors, measured at 14 checkpoints (LLaMA-3.1-8B, C4) with 95\\% bootstrap confidence intervals.\nFrom step 100 onward, BCE maintains consistently higher SNR than KL (2.3--17$\\times$ depending on training phase), with the gap narrowing toward convergence ($2.3\\times$ at step 1000: $2.026{\\times}10^{-3}$ vs.\\ $8.78{\\times}10^{-4}$). % exp_id: snr_full_curve_1000steps\nDespite KL's noisier gradient signal, KL-trained predictors produce substantially better masks (Table~\\ref{tab:main}), confirming that \\emph{target alignment} matters more than gradient clarity for mask quality.\nBCE's higher SNR reflects its simpler per-neuron classification objective, which concentrates gradients on individual neuron decisions; KL's coupled gradient distributes signal across all mask decisions jointly, yielding lower SNR but discovering compositionally superior mask patterns (\\S\\ref{sec:method:gradient}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{snr_trajectory.pdf}\n\\caption{Gradient SNR trajectory across 1000 training steps. BCE (orange) maintains consistently higher SNR than KL (blue) from step 100 onward (2.3--17$\\times$), yet KL produces superior masks (Table~\\ref{tab:main}), suggesting that target alignment matters more than gradient clarity for mask quality.}\n\\label{fig:snr_trajectory}\n\\end{figure}\n\n\n\\section{Extended Downstream Evaluation}\n\\label{app:downstream}\n\nTable~\\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\\% uniform: 3-seed mean$\\pm$std; others: seed 42.}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Method & HellaSwag & PIQA \\\\\n\\midrule\n0\\% & Dense & \\textbf{82.35} & \\textbf{80.90} \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& KL uniform & \\textbf{71.07$\\pm$0.54} & \\textbf{74.95$\\pm$0.25} \\\\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)\n& TEAL uniform & 63.31 & 72.80 \\\\ % exp_id: bench_teal30_uniform_6task\n& BCE isocompute & 62.81 & 74.21 \\\\ % exp_id: bce_isocompute_30u_hellaswag_piqa\n\\midrule\n\\multirow{3}{*}{50\\%}\n& KL global & \\textbf{58.95} & \\textbf{69.48} \\\\ % exp_id: hellaswag_piqa_kl50_global\n& KL uniform & 56.66 & 69.10 \\\\ % exp_id: hellaswag_piqa_kl50_uniform\n& TEAL uniform & 39.35 & 63.66 \\\\ % exp_id: bench_teal50_uniform_6task\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 30\\%, the KL predictor retains 86.3\\% of dense HellaSwag accuracy (71.07$\\pm$0.54 vs.\\ 82.35, 3-seed) and 92.6\\% of PIQA (74.95$\\pm$0.25 vs.\\ 80.90), confirming moderate degradation on non-reasoning tasks.\nAt 50\\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\\S\\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).\n\n\n\\section{Compensation Training Convergence}\n\\label{app:comp_convergence}\n\nAll compensation networks~\\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\\% s42 (final loss 0.70), 30\\% s456 (0.68), 50\\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42\n\n\n\\section{Qwen-2.5-14B Detailed Results}\n\\label{app:14b}\n\n\\begin{table}[h]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% nominal sparsity. Actual sparsity differs: KL 29.6\\% (3-seed), TEAL 29.3\\% (target 30\\%). \\textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\\% native sparsity (\\S\\ref{sec:method:gradient}), so forced global top-$k$ is used.}\n\\label{tab:14b}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \\textbf{75.01} & \\textbf{77.37} \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 & 70.51 & 74.70 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} & 53.43 & 68.28 \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{8}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.90} & 53.50 & \\textbf{72.82} & 63.55 & 32.2$\\pm$5.3 & \\textbf{72.68$\\pm$0.2} & \\textbf{76.01$\\pm$1.1} \\\\ % exp_id: qwen14b_kl30_uniform (3-seed s42/s123(v4)/s456)\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & \\textbf{52.1} & 67.72 & 74.70 \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\multicolumn{8}{l}{\\footnotesize GSM8K: 3-seed (s42/s123(v4)/s456).} \\\\\n\\end{tabular}}\n\\end{table}\n\nUnder global allocation, BCE's HellaSwag drops to 53.43\\% ($-$17pp vs.\\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval\n\n\\section{Full Allocation Analysis}\n\\label{app:alloc_full}\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation summary (LLaMA-3.1-8B). $\\pm$: 3-seed; $^\\ast$high seed variance.}\n\\label{tab:phase}\n\\footnotesize\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & MMLU \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & 35.7$\\pm$9.5$^\\ast$ \\\\ % exp_id: kl30_3seed_global\n& Uniform & \\textbf{8.81$\\pm$0.02} & \\textbf{40.7$\\pm$1.3} \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_reeval, kl50_global_s123_downstream_v2, kl50_global_s456_eval\n& Uniform & 11.92$\\pm$0.07 & 28.0$\\pm$0.6 \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:phase_full} extends Table~\\ref{tab:phase} with all downstream metrics.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Full allocation analysis: global top-$k$ vs.\\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); others: seed 42. $^\\ast$High MMLU seed variance (individual seeds span 25.3--43.5\\%).}\n\\label{tab:phase_full}\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{2}{*}{25\\%}\n& Global & \\textbf{8.17} & 45.4 & 70.6 & \\textbf{46.6} & \\textbf{11.5} \\\\\n& Uniform & 8.23 & \\textbf{46.5} & \\textbf{71.8} & 44.0 & 11.0 \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5$^\\ast$ & \\textbf{8.0$\\pm$0.7} \\\\\n& Uniform & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & \\textbf{40.7$\\pm$1.3} & 7.5$\\pm$0.1 \\\\\n\\midrule\n\\multirow{2}{*}{35\\%}\n& Global & \\textbf{9.31} & \\textbf{38.9} & \\textbf{67.6} & \\textbf{40.4} & \\textbf{7.7} \\\\\n& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\\\\n\\midrule\n\\multirow{2}{*}{40\\%}\n& Global & \\textbf{10.14} & 39.5 & \\textbf{67.5} & \\textbf{39.5} & \\textbf{6.6} \\\\\n& Uniform & 10.76 & \\textbf{39.6} & 63.1 & 35.5 & 3.6 \\\\\n\\midrule\n\\multirow{2}{*}{45\\%}\n& Global & \\textbf{10.80} & \\textbf{39.2} & \\textbf{64.6} & 30.4 & \\textbf{3.0} \\\\\n& Uniform & 10.95 & 37.6 & 63.6 & \\textbf{30.6} & 2.7 \\\\\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.7$\\pm$1.3} \\\\\n& Uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Mask Pattern Visualization}\n\\label{app:mask_viz}\n\nFigure~\\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity.\nFigure~\\ref{fig:scatter} shows per-neuron importance scores at layer 16.\nFigure~\\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{neuron_scatter_layer16.pdf}\n\\caption{KL vs.\\ magnitude importance scores for layer 16 neurons at 50\\% sparsity. 41\\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}\n\\label{fig:scatter}\n\\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_divergence_heatmap.pdf}\n\\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\\%) and increases with sparsity across all layers.}\n\\label{fig:mask_heatmap}\n\\end{figure*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_comparison.pdf}\n\\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\\% and 50\\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\\%, 0.74 at 50\\%).}\n\\label{fig:mask_comparison}\n\\end{figure*}\n\n\n\\section{Cross-Architecture Comparison}\n\\label{app:cross_arch}\n\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. \\textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\\%: 3-seed mean$\\pm$std; other rows: seed 42.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.93$\\pm$0.19} & 8.38 & 1.21$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL PPL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity).\nTable~\\ref{tab:mistral_downstream} reports downstream task accuracy at 30\\% sparsity on Mistral-7B-v0.3 (3-seed). KL improves PPL ($-$17.3\\%) and commonsense tasks (WG +6.7pp) but MMLU is tied (43.3\\% vs.\\ 43.5\\%); ARC-c shows high seed variance ($\\sigma$=6.4pp); GSM8K reverses.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B-v0.3 downstream evaluation at 30\\% sparsity. $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); TEAL is deterministic (single run). ARC-c exhibits high seed variance ($\\sigma$=6.4pp).}\n\\label{tab:mistral_downstream}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\\\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa\nKL 30\\% & \\textbf{6.93$\\pm$0.19} & \\textbf{44.9$\\pm$6.4} & \\textbf{70.2$\\pm$1.2} & \\textbf{69.7$\\pm$0.8} & \\textbf{74.8$\\pm$0.4} & 43.3$\\pm$1.5 & 8.6$\\pm$2.2 \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456\nTEAL 30\\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & \\textbf{43.5} & \\textbf{15.9} \\\\ % exp_id: mistral_teal30_downstream\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Taxonomy Discussion}\n\\label{app:taxonomy}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2025spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-token} methods~\\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass; each mask decision's gradient reflects its joint effect with all other masks on the final distribution.\n\nSPON~\\cite{xu2025spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\\times$ coupled).\nDejaVu~\\cite{liu2023dejavu} and FastForward~\\cite{gautam2026fastforward} achieve per-token granularity but use BCE, where each neuron's gradient is independent of other mask states.\nD2DMoE~\\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.\nWe define \\emph{output-distribution alignment} as whether the training loss optimizes a quantity that composes across layers.\nKL on output logits directly optimizes next-token prediction loss, which does not suffer from error composition; per-layer MSE minimizes reconstruction error independently at each layer, but layer-wise optima do not compose---a mask minimizing FFN output error at layer $\\ell$ may amplify errors in layers $\\ell{+}1 \\ldots L$.\nThe SNR analysis (\\S\\ref{sec:method:gradient}) corroborates this: KL achieves the best masks despite $2.3\\times$ lower SNR than BCE, while MSE produces the worst masks.\nThe framework predicts that losses operating on output-level quantities should outperform intermediate-level losses, a hypothesis consistent with our MSE results and testable with alternative output-level objectives.\n\n\\section{Oracle Mask Provenance}\n\\label{app:oracle_provenance}\n\nC1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold (logits $> 0$, equivalent to $\\sigma > 0.5$); they reflect one specific training trajectory (optimizer state, data order, Gumbel noise).\nThe s42/s123/s456 consistency ($\\leq$1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.\n\n\\section{SPON Orthogonality}\n\\label{app:spon}\n\nSPON~\\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\nThe decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.\n\n\\section{Per-Layer KL Downstream Decomposition}\n\\label{app:perlayer_downstream}\n\nTable~\\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\\ coupling scope decomposition at 30\\% sparsity (\\S\\ref{sec:perlayer}). BoolQ's $\\approx$100\\% coupling is an upper bound confounded by high cross-seed variance ($\\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.\n\n\\begin{table}[h]\n\\centering\n\\caption{2D decomposition at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \\S\\ref{sec:perlayer}).}\n\\label{tab:perlayer_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\n& PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\\\\n\\midrule\nE2E KL & 8.81$\\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\\\\nPer-layer KL & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\\\\nMSE & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 & 64.5$\\pm$5.3 \\\\\n\\midrule\nTotal gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\\\\nSignal type (\\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\\approx$0 \\\\\nCoupling (\\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\\approx$100 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{$K{=}4$ Mismatch Control}\n\\label{app:k4_downstream}\n\nTable~\\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\\% sparsity.\nTraining with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\\ 1/32 layers masked during training, while inference applies all 32).\nThe gap closure column reports the fraction of the $K{=}1 \\to$ E2E KL gap closed by $K{=}4$.\n\n\\begin{table}[h]\n\\centering\n\\caption{3-seed $K{=}4$ mismatch control at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \\in \\{42, 123, 456\\}$). Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\\text{E2E} - K{=}1) \\times 100$.}\n\\label{tab:k4_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\n& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\\%) \\\\\n\\midrule\nPPL$\\downarrow$ & 8.89$\\pm$0.01 & 9.05$\\pm$0.02 & 8.81$\\pm$0.02 & 66.7 \\\\\nARC-c & 40.0$\\pm$1.3 & 39.9 & 43.7$\\pm$2.5 & 2.6 \\\\\nWG & 66.9$\\pm$0.2 & 65.9 & 68.9$\\pm$0.4 & 33.3 \\\\\nMMLU$^\\ast$ & 42.7$\\pm$1.4 & 38.6 & 40.7$\\pm$1.3 & $>$100 \\\\\nGSM8K & 7.0$\\pm$1.6 & 5.8 & 7.5$\\pm$0.1 & 70.6 \\\\\nBoolQ$^\\dagger$ & 67.7$\\pm$7.5 & 64.5$\\pm$11.5 & 73.7 & 34.8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize $^\\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\\% (Appendix~\\ref{app:constraint}).\n$^\\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}\n\\end{table}\n\n\\section{Per-Layer Sparsity Constraint Analysis}\n\\label{app:constraint}\n\nTo test the causal role of the KL predictor's learned per-layer allocation, we evaluate two inference-time interventions at 30\\% overall sparsity (seed 42, uniform allocation baseline):\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity constraint analysis. \\emph{Protect late}: cap L22--L28 sparsity $\\leq$30\\%; \\emph{Remove valley}: override L14--L18 sparsity to 30\\%. Budget redistributed to maintain 30\\% overall.}\n\\label{tab:constraint}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & PPL & ARC-c & MMLU & GSM8K \\\\\n\\midrule\nKL baseline (s42) & 8.82 & 40.8 & 40.6 & 7.4 \\\\\nProtect late layers & 9.26 & 42.4 & 40.7 & 6.5 \\\\\nRemove valley & 8.76 & 39.3 & 44.0 & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nProtecting late layers (L22--L28) does not improve knowledge-intensive metrics despite reducing their sparsity from 48--57\\% to $\\leq$30\\%, while worsening PPL by 5.2\\%.\nConversely, removing the protection valley (forcing L14--L18 to 30\\% instead of 14--18\\%) improves MMLU by +3.4pp and GSM8K by +1.6pp at the cost of ARC-c $-$1.5pp.\nThe KL predictor's learned allocation thus represents a task-dependent trade-off---prioritizing commonsense reasoning via middle-layer protection---rather than a uniformly optimal pattern.\nThis allocation trade-off also explains the $K{=}4$ MMLU anomaly (\\S\\ref{app:k4_downstream}): $K{=}4$'s near-uniform learned sparsity (std=0.003) inherently removes the valley, producing MMLU=43.5 comparable to the remove-valley condition (44.0).\n\n\\section{Per-Layer Sparsity Distribution}\n\\label{app:perlayer_sparsity}\n\nThe KL predictor at 30\\% target sparsity learns a non-uniform per-layer allocation that differs markedly from magnitude-based selection.\nAggregate sparsity is similar across broad regions (early L0--L7: KL 28.1\\% vs.\\ magnitude 27.5\\%; late L24--L31: 44.9\\% vs.\\ 47.2\\%), but middle layers (L8--L23) exhibit high internal variance despite similar averages (28.2\\% vs.\\ 27.3\\%).\nTable~\\ref{tab:perlayer_sparsity} highlights three sub-ranges.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity sub-ranges: KL predictor vs.\\ magnitude (LLaMA-3.1-8B, 30\\%, uniform allocation). Ranges denote min--max across layers in each group.}\n\\label{tab:perlayer_sparsity}\n\\begin{tabular}{lccc}\n\\toprule\nLayer Range & KL (\\%) & Mag (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nL8--L12 (high pruning) & 32--36 & 25--26 & $+$7 to $+$10 \\\\\nL14--L18 (protection valley) & 14--18 & 28--30 & $-$8 to $-$16 \\\\\nL22--L28 (aggressive pruning) & 48--57 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{C4 Training Data Control}\n\\label{app:c4_control}\n\nTo test whether WikiText-103's narrow domain drives the knowledge-task regression (\\S\\ref{sec:experiments}), we train the KL predictor on C4~\\cite{raffel2020c4} (diverse web text) under identical hyperparameters (1000 steps, 30\\% uniform, s42).\n\n\\begin{table}[h]\n\\centering\n\\caption{C4-trained vs.\\ WikiText-trained KL predictor (LLaMA-3.1-8B, 30\\% uniform, s42).}\n\\label{tab:c4_control}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\nTraining Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\\n\\midrule\nWikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe C4-trained predictor achieves comparable MMLU (40.0\\% vs.\\ 40.6\\%) but worse GSM8K (4.1\\% vs.\\ 7.4\\%) and higher PPL (11.55 vs.\\ 8.82), despite training on more diverse text.\nThis rules out training data composition as the primary cause of knowledge-task regression and supports the hypothesis that forward KL's mode-covering property structurally under-protects rare reasoning-critical activations. % exp_id: c4_control_eval\n\n\\section{Per-Layer Coupling Breadth Analysis}\n\\label{app:k_curve}\n\nWe vary the number of layers coupled per training step ($K$) from 1 (pure per-layer) to 32 (end-to-end), evaluating all predictors under TEAL uniform allocation at 30\\% sparsity on LLaMA-3.1-8B.\n\n\\begin{table}[h]\n\\centering\n\\caption{K-curve: coupling breadth vs.\\ predictor quality (30\\%, TEAL uniform, LLaMA-3.1-8B). All values are 3-seed mean$\\pm$std (s42/s123/s456) except $K{=}1$ downstream (single seed). ``---'' = not evaluated.}\n\\label{tab:k_curve}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{cccccccc}\n\\toprule\n$K$ & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\n1 & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & --- & --- \\\\\n2 & 10.75$\\pm$0.15 & 39.7$\\pm$1.2 & 63.2$\\pm$1.7 & 38.3$\\pm$3.2 & 2.8$\\pm$0.6 & 66.5$\\pm$1.0 & 73.5$\\pm$0.7 \\\\\n4 & 8.89$\\pm$0.01 & 40.0$\\pm$1.2 & 66.9$\\pm$0.2 & 42.7$\\pm$1.4 & 7.0$\\pm$1.6 & 67.8$\\pm$1.0 & 74.5$\\pm$0.5 \\\\\n8 & 9.00$\\pm$0.06 & 40.7$\\pm$1.0 & 68.7$\\pm$1.3 & 40.4$\\pm$0.6 & 6.8$\\pm$1.3 & 69.0$\\pm$1.1 & 75.1$\\pm$1.1 \\\\\n16 & 8.67$\\pm$0.02 & 41.9$\\pm$1.1 & 68.5$\\pm$0.9 & 40.9$\\pm$2.9 & 8.5$\\pm$1.2 & 70.1$\\pm$0.4 & 75.0$\\pm$0.8 \\\\\n32 (E2E) & 8.81$\\pm$0.02 & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nPPL exhibits a non-monotonic U-shape (Figure~\\ref{fig:k_curve_ppl}): $K{=}2$ is worst (10.75$\\pm$0.15), likely due to insufficient per-layer updates (${\\sim}$62 updates/layer vs.\\ ${\\sim}$250 at $K{=}8$). $K{=}16$ achieves the lowest PPL (8.67$\\pm$0.02), marginally better than E2E (8.81$\\pm$0.02). $K{=}16$ MMLU exhibits high seed variance (std=2.9; s42=44.0, s123=40.0, s456=38.7), with the 3-seed mean (40.9) indistinguishable from E2E (40.7$\\pm$1.3).\nThe signal type gap ($K{=}1$ KL 9.05 vs.\\ per-layer MSE 18.52$\\pm$1.68) of 9.47 PPL dwarfs the coupling breadth range within KL (best $K{=}16$ 8.67 vs.\\ worst $K{=}2$ 10.75 = 2.08 PPL), reinforcing that output-distribution alignment, not coupling scope, is the primary quality lever for PPL at this sparsity level. % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed, perlayer_kl_30_3seed, perlayer_kl_k4_3seed\n\n\\section{Licenses}\n\\label{app:licenses}\n\nLLaMA-3.1-8B is released under the Llama 3.1 Community License Agreement.\nMistral-7B-v0.3 is released under the Apache 2.0 License.\nQwen-2.5-14B is released under the Apache 2.0 License.\nWikiText-103 and WikiText-2~\\cite{merity2017pointer} are released under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).\nAll evaluation benchmarks (ARC, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA) are publicly available under their respective licenses.\nOur code will be released under the MIT License upon acceptance.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
      "numLines": 673,
      "startLine": 1,
      "totalLines": 673
    }
  },
  "sourceToolAssistantUUID": "646584d3-cc5c-4ab2-8101-edf1fbaf2f46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-24T03:57:35.658Z_

<details open><summary>🔧 Tool call — Read · `toolu_0123WRHr4X9KeBAMcsRgE1Jg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f5b5c1b-020d-454b-aa52-023a7b62c940",
  "isSidechain": false,
  "requestId": "req_011CbLiqB9NFA8R3etBpvHv2",
  "type": "assistant",
  "uuid": "c85124f1-7237-48ac-a3cd-aa63c0b87c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177mv6yrzsEC656pgbU2FXb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 25598,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 776,
          "cache_read_input_tokens": 25598,
          "cache_creation_input_tokens": 1176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1176
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-24T03:57:35.662Z_

<details><summary>↩ Tool result · `toolu_0123WRHr4X9KeBAMcsRgE1Jg`</summary>

```text
1	\section*{Limitations}
2	
3	Our findings are bounded by four limitations.
4	\textbf{Sparsity sweet spot.} 30\% is the lowest-degradation level; at 50\%, all methods collapse on reasoning tasks, and a separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$19.9pp GSM8K), suggesting output-distribution objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Evaluation scope.} Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.
7	\textbf{Baseline coverage.} The 30\% isocompute comparison lacks a BCE 2700-step baseline; WikiText-2 evaluation shares provenance with the training corpus (WikiText-103), partially mitigated by C4 OOD results (Appendix~\ref{app:ood}).
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c85124f1-7237-48ac-a3cd-aa63c0b87c6a",
  "isSidechain": false,
  "promptId": "fdfb0d6d-9233-4c2a-afaa-5df266af136f",
  "type": "user",
  "uuid": "78c5e098-5eb2-4c9d-b372-1e82d648a587",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\nOur findings are bounded by four limitations.\n\\textbf{Sparsity sweet spot.} 30\\% is the lowest-degradation level; at 50\\%, all methods collapse on reasoning tasks, and a separate predictor must be retrained per target.\n\\textbf{Knowledge-intensive regression.} KL consistently underperforms on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$19.9pp GSM8K), suggesting output-distribution objectives systematically sacrifice reasoning-critical pathways.\n\\textbf{Evaluation scope.} Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.\n\\textbf{Baseline coverage.} The 30\\% isocompute comparison lacks a BCE 2700-step baseline; WikiText-2 evaluation shares provenance with the training corpus (WikiText-103), partially mitigated by C4 OOD results (Appendix~\\ref{app:ood}).\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "c85124f1-7237-48ac-a3cd-aa63c0b87c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-24T03:57:35.811Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B8pLgxbMghAhq4NVjozm2x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78c5e098-5eb2-4c9d-b372-1e82d648a587",
  "isSidechain": false,
  "requestId": "req_011CbLiqB9NFA8R3etBpvHv2",
  "type": "assistant",
  "uuid": "2c5caaf7-735d-4d4a-b660-d3647b9a6de6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177mv6yrzsEC656pgbU2FXb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 25598,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1176,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 776,
          "cache_read_input_tokens": 25598,
          "cache_creation_input_tokens": 1176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1176
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 33 · 2026-05-24T03:57:35.864Z_

```json
{
  "parentUuid": "4b0048ff-8bcf-4901-bf0d-3c336ed31c65",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d0f2037d-5a55-4901-a659-c0f636db8c7f",
  "timestamp": "2026-05-24T03:57:35.864Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "leafUuid": "d0f2037d-5a55-4901-a659-c0f636db8c7f",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper and registry data consistency for R28",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Assistant

_source line 36 · 2026-05-24T03:57:39.415Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the registry data. It was saved to a file because it was too large. Let me read it in chunks to extract the relevant experiment data.

Let me use jq to extract just the success experiments with their metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0f2037d-5a55-4901-a659-c0f636db8c7f",
  "isSidechain": false,
  "requestId": "req_011CbLiqxSR5hupyLb5pAagj",
  "type": "assistant",
  "uuid": "7dceeb7e-c636-40cd-9300-20930b50201c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dr36FsiDfE4qvFWsdiLn8h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36532,
      "cache_read_input_tokens": 26774,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36532,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 26774,
          "cache_creation_input_tokens": 36532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36532
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 37 · 2026-05-24T03:57:40.399Z_

Registry 数据太大，用 jq 提取 success 实验的关键字段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dceeb7e-c636-40cd-9300-20930b50201c",
  "isSidechain": false,
  "requestId": "req_011CbLiqxSR5hupyLb5pAagj",
  "type": "assistant",
  "uuid": "1b333c8f-d91e-4ebd-afd5-afee17ebae05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dr36FsiDfE4qvFWsdiLn8h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36532,
      "cache_read_input_tokens": 26774,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36532,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 26774,
          "cache_creation_input_tokens": 36532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36532
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-24T03:57:47.858Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013gzWv2P6W2BEbTKn65PzjP`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/mcp-agent-ml-research-read_registry-1779595051440.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\nsuccess = [e for e in exps if e.get('conclusion') == 'success']\nfor e in success:\n    eid = e.get('exp_id', e.get('id', ''))\n    metrics = e.get('metrics', {})\n    notes = e.get('notes', '')\n    print(f'=== {eid} ===')\n    print(f'  metrics: {json.dumps(metrics, ensure_ascii=False)}')\n    if notes:\n        print(f'  notes: {notes[:200]}')\n    print()\n\" 2>&1 | head -3000",
  "description": "Extract success experiments from registry JSON",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b333c8f-d91e-4ebd-afd5-afee17ebae05",
  "isSidechain": false,
  "requestId": "req_011CbLiqxSR5hupyLb5pAagj",
  "type": "assistant",
  "uuid": "3abc3b4b-7ac7-4dc4-868b-088bb9544d3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dr36FsiDfE4qvFWsdiLn8h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36532,
      "cache_read_input_tokens": 26774,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36532,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 488,
          "cache_read_input_tokens": 26774,
          "cache_creation_input_tokens": 36532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36532
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-24T03:57:48.384Z_

<details><summary>↩ Tool result · `toolu_013gzWv2P6W2BEbTKn65PzjP`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 6, in &lt;module>
    success = [e for e in exps if e.get('conclusion') == 'success']
                                  ^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3abc3b4b-7ac7-4dc4-868b-088bb9544d3d",
  "isSidechain": false,
  "promptId": "fdfb0d6d-9233-4c2a-afaa-5df266af136f",
  "type": "user",
  "uuid": "88aaaf4b-061e-4545-89e2-3b53ae37489a",
  "toolUseResult": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 6, in &lt;module>\n    success = [e for e in exps if e.get('conclusion') == 'success']\n                                  ^^^^^\nAttributeError: 'str' object has no attribute 'get'",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3abc3b4b-7ac7-4dc4-868b-088bb9544d3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-24T03:57:51.121Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019Hm7aWiiJ53fnf3CSaNQEE`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/mcp-agent-ml-research-read_registry-1779595051440.txt",
  "description": "Inspect registry file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88aaaf4b-061e-4545-89e2-3b53ae37489a",
  "isSidechain": false,
  "requestId": "req_011CbLirt1YXg1GWtbSiWr5D",
  "type": "assistant",
  "uuid": "4505d134-c701-48dc-9c14-a6682c2ccd15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCjA36A7doELhp5FTkZeko",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 570,
      "cache_read_input_tokens": 63306,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 570,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 63306,
          "cache_creation_input_tokens": 570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 570
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-24T03:57:51.163Z_

<details><summary>↩ Tool result · `toolu_019Hm7aWiiJ53fnf3CSaNQEE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"qwen14b_kl30_s123_eval_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T11:25:23.513Z\", \"updated_at\": \"2026-05-24T03:27:37.442Z\", \"hypothesis\": \"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Retry after v2/v3 OOM (caused by orphan PID 93142, now killed). Multi-seed replication to confirm MMLU reversal is systematic.\", \"parent\": \"qwen14b_kl30_s123\", \"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-34887\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-19T11:25:41.684Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\"\", \"finished_at\": \"2026-05-19T12:55:31.217Z\", \"training_hours\": 1.5}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_k
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4505d134-c701-48dc-9c14-a6682c2ccd15",
  "isSidechain": false,
  "promptId": "fdfb0d6d-9233-4c2a-afaa-5df266af136f",
  "type": "user",
  "uuid": "851bafa4-9f62-4a43-a052-370b3707eeec",
  "toolUseResult": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"qwen14b_kl30_s123_eval_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-19T11:25:23.513Z\\\", \\\"updated_at\\\": \\\"2026-05-24T03:27:37.442Z\\\", \\\"hypothesis\\\": \\\"Qwen-14B KL 30% s123 benchmark eval (WikiText-2 PPL + 5 downstream: ARC/WG/HS/PIQA/MMLU) with TEAL uniform allocation. Retry after v2/v3 OOM (caused by orphan PID 93142, now killed). Multi-seed replication to confirm MMLU reversal is systematic.\\\", \\\"parent\\\": \\\"qwen14b_kl30_s123\\\", \\\"server\\\": \\\"westd-34887\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"westd-34887\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-19T11:25:41.684Z\\\", \\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks wikitext2,arc_challenge,winogrande,hellaswag,piqa,mmlu --seq_len 2048 --gpu 0 2>&1\\\\\\\"\\\", \\\"finished_at\\\": \\\"2026-05-19T12:55:31.217Z\\\", \\\"training_hours\\\": 1.5}, \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export WANDB_MODE=disabled && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s123_eval_v4 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s123/predictor_k",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4505d134-c701-48dc-9c14-a6682c2ccd15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-24T03:58:01.883Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KK9NpwGn8DMVXhsjwK22tS`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/mcp-agent-ml-research-read_registry-1779595051440.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nsuccess = {k: v for k, v in exps.items() if v.get('conclusion') == 'success'}\nprint(f'Total experiments: {len(exps)}')\nprint(f'Success experiments: {len(success)}')\nprint()\nfor eid, e in sorted(success.items()):\n    metrics = e.get('metrics', {})\n    print(f'=== {eid} ===')\n    print(f'  metrics: {json.dumps(metrics, ensure_ascii=False)}')\n    print()\n\" 2>&1 | head -5000",
  "description": "Extract success experiments with metrics from registry",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "851bafa4-9f62-4a43-a052-370b3707eeec",
  "isSidechain": false,
  "requestId": "req_011CbLis62rBeNkrNsfp2tJm",
  "type": "assistant",
  "uuid": "ba2eb6a9-a5a7-4c3c-bcc1-647f81047294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D91oV5sRLPPzQmEKH24AZQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 63876,
      "output_tokens": 376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 376,
          "cache_read_input_tokens": 63876,
          "cache_creation_input_tokens": 1013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1013
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-24T03:58:02.065Z_

<details><summary>↩ Tool result · `toolu_01KK9NpwGn8DMVXhsjwK22tS`</summary>

```text
&lt;persisted-output>
Output too large (49.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/bt4n79nxb.txt

Preview (first 2KB):
Total experiments: 408
Success experiments: 257

=== bce_30_s42_uniform_eval ===
  metrics: {"ppl": 15.7069, "arc_challenge": 0.3319, "winogrande": 0.618, "mmlu": 0.4237, "gsm8k": 0.0394, "hellaswag": 0.6156, "piqa": 0.741}

=== bce_30pct_s42 ===
  metrics: {}

=== bce_50pct_teal_global_unified ===
  metrics: {"wikitext2_ppl": 27.97, "arc_challenge_acc_norm": 0.2765, "winogrande_acc": 0.5162, "mmlu_acc": 0.2614, "gsm8k_exact_match": 0.019}

=== bce_gumbel_lagrangian_isolation ===
  metrics: {"lr_1e4_ppl": 42.99, "lr_1e3_ppl": 48.4, "lr_3e3_ppl": 38.02, "lr_1e4_bce_loss": 0.7158, "lr_1e3_bce_loss": 0.6781, "lr_3e3_bce_loss": 0.6632, "lr_1e4_sparsity": 0.514, "lr_1e3_sparsity": 0.506, "lr_3e3_sparsity": 0.504, "best_ppl": 38.02, "best_lr": "3e-3", "kl_baseline_ppl": 11.79, "gap_vs_kl": 26.23}

=== bce_gumbel_no_penalty_s42 ===
  metrics: {"training_bce_loss": 0.6307, "training_sparsity": 0.383, "wikitext2_ppl": 32.22, "training_time_seconds": 977.6}

=== bce_iso_v3_s123_30pct_uniform_eval ===
  metrics: {"ppl": 15.2051, "arc_challenge": 0.3396, "winogrande": 0.6046, "mmlu": 0.4363, "gsm8k": 0.0455, "hellaswag": 0.614, "piqa": 0.7356}

=== bce_iso_v3_s42_30pct_uniform_eval ===
  metrics: {"ppl": 14.947, "arc_challenge": 0.3294, "winogrande": 0.6062, "mmlu": 0.4291, "gsm8k": 0.0379, "hellaswag": 0.6165, "piqa": 0.7356}

=== bce_iso_v3_s456_30pct_uniform_eval ===
  metrics: {"ppl": 15.1102, "arc_challenge": 0.3345, "winogrande": 0.6219, "mmlu": 0.4261, "gsm8k": 0.0356, "hellaswag": 0.6158, "piqa": 0.7323}

=== bce_isocompute_hellaswag_piqa_v2 ===
  metrics: {"hellaswag_acc_norm": 0.6281, "piqa_acc_norm": 0.7421}

=== bce_isocompute_v3_s123 ===
  metrics: {}

=== bce_isocompute_v3_s123_eval ===
  metrics: {"wikitext2_ppl": 28.0627, "arc_challenge_acc_norm": 0.2696, "winogrande_acc": 0.513, "mmlu_acc": 0.2655, "gsm8k_exact_match": 0.022}

=== bce_isocompute_v3_s42 ===
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba2eb6a9-a5a7-4c3c-bcc1-647f81047294",
  "isSidechain": false,
  "promptId": "fdfb0d6d-9233-4c2a-afaa-5df266af136f",
  "type": "user",
  "uuid": "332a9c0a-4d48-4f8e-a53e-afe3d8b70775",
  "toolUseResult": {
    "stdout": "Total experiments: 408\nSuccess experiments: 257\n\n=== bce_30_s42_uniform_eval ===\n  metrics: {\"ppl\": 15.7069, \"arc_challenge\": 0.3319, \"winogrande\": 0.618, \"mmlu\": 0.4237, \"gsm8k\": 0.0394, \"hellaswag\": 0.6156, \"piqa\": 0.741}\n\n=== bce_30pct_s42 ===\n  metrics: {}\n\n=== bce_50pct_teal_global_unified ===\n  metrics: {\"wikitext2_ppl\": 27.97, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}\n\n=== bce_gumbel_lagrangian_isolation ===\n  metrics: {\"lr_1e4_ppl\": 42.99, \"lr_1e3_ppl\": 48.4, \"lr_3e3_ppl\": 38.02, \"lr_1e4_bce_loss\": 0.7158, \"lr_1e3_bce_loss\": 0.6781, \"lr_3e3_bce_loss\": 0.6632, \"lr_1e4_sparsity\": 0.514, \"lr_1e3_sparsity\": 0.506, \"lr_3e3_sparsity\": 0.504, \"best_ppl\": 38.02, \"best_lr\": \"3e-3\", \"kl_baseline_ppl\": 11.79, \"gap_vs_kl\": 26.23}\n\n=== bce_gumbel_no_penalty_s42 ===\n  metrics: {\"training_bce_loss\": 0.6307, \"training_sparsity\": 0.383, \"wikitext2_ppl\": 32.22, \"training_time_seconds\": 977.6}\n\n=== bce_iso_v3_s123_30pct_uniform_eval ===\n  metrics: {\"ppl\": 15.2051, \"arc_challenge\": 0.3396, \"winogrande\": 0.6046, \"mmlu\": 0.4363, \"gsm8k\": 0.0455, \"hellaswag\": 0.614, \"piqa\": 0.7356}\n\n=== bce_iso_v3_s42_30pct_uniform_eval ===\n  metrics: {\"ppl\": 14.947, \"arc_challenge\": 0.3294, \"winogrande\": 0.6062, \"mmlu\": 0.4291, \"gsm8k\": 0.0379, \"hellaswag\": 0.6165, \"piqa\": 0.7356}\n\n=== bce_iso_v3_s456_30pct_uniform_eval ===\n  metrics: {\"ppl\": 15.1102, \"arc_challenge\": 0.3345, \"winogrande\": 0.6219, \"mmlu\": 0.4261, \"gsm8k\": 0.0356, \"hellaswag\": 0.6158, \"piqa\": 0.7323}\n\n=== bce_isocompute_hellaswag_piqa_v2 ===\n  metrics: {\"hellaswag_acc_norm\": 0.6281, \"piqa_acc_norm\": 0.7421}\n\n=== bce_isocompute_v3_s123 ===\n  metrics: {}\n\n=== bce_isocompute_v3_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 28.0627, \"arc_challenge_acc_norm\": 0.2696, \"winogrande_acc\": 0.513, \"mmlu_acc\": 0.2655, \"gsm8k_exact_match\": 0.022}\n\n=== bce_isocompute_v3_s42 ===\n  metrics: {\"steps\": 2700, \"loss\": 0.6382, \"bce_loss\": 0.6371, \"reg_loss\": 0.001, \"sparsity\": 0.51, \"training_time_seconds\": 2828, \"note\": \"BCE saturation confirmed: step 500→2700 only 0.006 improvement\"}\n\n=== bce_isocompute_v3_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 27.9696, \"arc_challenge_acc\": 0.2346, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}\n\n=== bce_isocompute_v3_s456 ===\n  metrics: {\"final_loss\": 0.6368, \"final_sparsity\": 0.51, \"training_steps\": 2700}\n\n=== bce_isocompute_v3_s456_eval ===\n  metrics: {\"teal_sparse_ppl\": 28.3503, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2312, \"arc_challenge_acc_stderr\": 0.01232, \"arc_challenge_acc_norm\": 0.2807, \"arc_challenge_acc_norm_stderr\": 0.01313, \"winogrande_acc\": 0.5241, \"winogrande_acc_stderr\": 0.01404, \"mmlu_acc\": 0.2567, \"mmlu_acc_stderr\": 0.00367, \"gsm8k_exact_match\": 0.022, \"gsm8k_exact_match_stderr\": 0.00404, \"gsm8k_exact_match_strict\": 0.00834, \"gsm8k_exact_match_strict_stderr\": 0.0025}\n\n=== bench_dense ===\n  metrics: {\"wikitext2_ppl\": 6.1173, \"arc_challenge_acc\": 0.5478, \"arc_challenge_acc_norm\": 0.5828, \"winogrande_acc\": 0.7806, \"mmlu_acc\": 0.6527, \"gsm8k_exact_match\": 0.4875}\n\n=== bench_kl30_global ===\n  metrics: {\"wikitext2_ppl\": 8.9768, \"arc_challenge_acc_norm\": 0.3968, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.2527, \"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}\n\n=== bench_kl30_uniform ===\n  metrics: {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3}\n\n=== bench_kl40_global ===\n  metrics: {\"wikitext2_ppl\": 10.117, \"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6535, \"mmlu_acc\": 0.3806, \"gsm8k_exact_match\": 0.05, \"actual_sparsity\": 0.4}\n\n=== bench_kl50_global ===\n  metrics: {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129, \"actual_sparsity\": 0.5}\n\n=== bench_kl50_uniform ===\n  metrics: {\"wikitext2_ppl\": 11.963, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}\n\n=== bench_kl50_uniform_s123 ===\n  metrics: {\"wikitext2_ppl\": 11.83, \"arc_challenge_acc_norm\": 0.3515, \"winogrande_acc\": 0.6298, \"mmlu_acc\": 0.2751, \"gsm8k_exact_match\": 0.0235, \"actual_sparsity\": 0.5}\n\n=== bench_kl50_uniform_s456 ===\n  metrics: {\"wikitext2_ppl\": 11.9604, \"arc_challenge_acc_norm\": 0.3345, \"winogrande_acc\": 0.6275, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}\n\n=== bench_kl70_global ===\n  metrics: {\"wikitext2_ppl\": 17.91, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"kl_sparsity70_s42_v2 (teal_global_masks protocol)\", \"vanilla_teal_ppl\": 100.11}\n\n=== bench_teal30 ===\n  metrics: {\"wikitext2_ppl\": 10.97, \"arc_challenge_acc_norm\": 0.4232, \"winogrande_acc\": 0.6606, \"mmlu_acc\": 0.3861, \"gsm8k_exact_match\": 0.0788, \"actual_sparsity\": 0.3}\n\n=== bench_teal50 ===\n  metrics: {\"wikitext2_ppl\": 23.31, \"arc_challenge_acc_norm\": 0.2841, \"winogrande_acc\": 0.5304, \"mmlu_acc\": 0.2832, \"gsm8k_exact_match\": 0.0197, \"actual_sparsity\": 0.5}\n\n=== bench_teal50_uniform_gsm8k ===\n  metrics: {\"gsm8k_exact_match_flexible\": 0.0174}\n\n=== bench_teal70 ===\n  metrics: {\"wikitext2_ppl\": 100.11, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"training_free_baselines experiment (vanilla teal global)\"}\n\n=== c1_ablation_30pct_s123 ===\n  metrics: {\"wikitext2_ppl\": 8.83, \"mmlu_acc\": 0.3833, \"winogrande_acc\": 0.7119}\n\n=== c1_ablation_30pct_s42_eval_v2 ===\n  metrics: {\"wikitext2_ppl\": 9.4463, \"arc_challenge_acc_norm\": 0.4027, \"winogrande_acc\": 0.674, \"mmlu_acc\": 0.4229, \"gsm8k_exact_match\": 0.0758}\n\n=== c1_ablation_30pct_s42_v2 ===\n  metrics: {\"agreement\": 0.975}\n\n=== c1_ablation_30pct_s456 ===\n  metrics: {\"wikitext2_ppl\": 8.84, \"mmlu_acc\": 0.367, \"winogrande_acc\": 0.6938}\n\n=== c1_ablation_bce_kl_targets_s123_v2 ===\n  metrics: {\"final_loss\": 0.0537, \"ppl\": 9.32, \"sparsity\": 0.615, \"agreement\": 0.979, \"note\": \"Consistent with s42 (PPL=9.29, sparsity=0.609, agreement=0.978). Both seeds converge to ~61% eval sparsity. C1 confirmed multi-seed robust.\"}\n\n=== c1_ablation_bce_kl_targets_s42 ===\n  metrics: {\"wt2_ppl\": 9.29, \"eval_sparsity\": 0.609, \"oracle_agreement\": 0.978, \"final_bce_loss\": 0.0545, \"train_steps\": 1000, \"train_time_sec\": 877.1, \"reference_kl_ppl\": 11.79, \"reference_bce_ppl\": 22.51}\n\n=== c1_ablation_eval_uniform ===\n  metrics: {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3217, \"winogrande_acc\": 0.6314, \"mmlu_acc\": 0.2779, \"gsm8k_exact_match\": 0.0205, \"sparsity_target\": 0.5, \"allocation\": \"uniform\"}\n\n=== c1_retrain_30pct_s123 ===\n  metrics: {\"training_agreement\": 0.977, \"training_sparsity\": 0.31, \"wikitext2_ppl\": 7.54, \"actual_sparsity\": 0.332}\n\n=== c1_retrain_30pct_s456 ===\n  metrics: {\"training_agreement\": 0.977, \"training_sparsity\": 0.312, \"wikitext2_ppl\": 7.38, \"actual_sparsity\": 0.346}\n\n=== c4_kl30_s42 ===\n  metrics: {}\n\n=== c4_kl30_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 11.554, \"arc_challenge_acc_norm\": 0.4309, \"winogrande_acc\": 0.6867, \"mmlu_acc\": 0.3995, \"gsm8k_exact_match\": 0.0409, \"hellaswag_acc_norm\": 0.6924, \"piqa_acc_norm\": 0.7503, \"sparsity\": 0.295}\n\n=== c4_ood_dense_baseline_v2 ===\n  metrics: {\"c4_ppl\": 9.2075, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}\n\n=== c4_ood_downstream_kl30 ===\n  metrics: {\"arc_challenge_acc_norm\": 0.4036, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.4137, \"gsm8k_exact_match\": 0.0629, \"hellaswag_acc_norm\": 0.7074, \"piqa_acc_norm\": 0.7399, \"model_level_sparsity\": 0.295}\n\n=== c4_ood_kl30_s123_v2 ===\n  metrics: {\"c4_ppl\": 16.0259, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}\n\n=== c4_ood_kl30_s42 ===\n  metrics: {\"c4_ppl\": 16.0458, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}\n\n=== c4_ood_kl30_s42_v2 ===\n  metrics: {\"c4_ppl\": 16.0401, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"seed\": 42}\n\n=== c4_ood_kl30_s456 ===\n  metrics: {}\n\n=== c4_ood_kl30_uniform_s123 ===\n  metrics: {\"c4_ppl\": 16.3686, \"allocation\": \"uniform\", \"sparsity\": 0.3, \"seed\": 123}\n\n=== c4_ood_kl30_uniform_s42 ===\n  metrics: {\"c4_ppl\": 18.2211, \"allocation\": \"uniform\", \"sparsity\": 0.296, \"seed\": 42}\n\n=== c4_ood_kl30_uniform_s456 ===\n  metrics: {\"c4_ppl\": 16.3551, \"allocation\": \"uniform\", \"sparsity\": 0.3, \"seed\": 456}\n\n=== c4_ood_kl50_s123 ===\n  metrics: {\"c4_ppl\": 23.6064, \"allocation\": \"global_topk\", \"sparsity\": 0.5, \"model\": \"llama-3.1-8b\"}\n\n=== c4_ood_kl50_s42 ===\n  metrics: {\"c4_ppl\": 23.5297, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 42}\n\n=== c4_ood_kl50_s456 ===\n  metrics: {\"c4_ppl\": 23.9867, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 456}\n\n=== d030_kl30_uniform ===\n  metrics: {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.301 across all 32 layers\", \"mmlu_improvement_vs_global\": \"+11.87pp (0.2874 → 0.4061)\", \"gsm8k_change_vs_global\": \"no change (0.0743 → 0.0735, within noise)\"}\n\n=== d030_kl40_uniform ===\n  metrics: {\"wikitext2_ppl\": 8.3627, \"arc_challenge_acc_norm\": 0.4181, \"winogrande_acc\": 0.6717, \"mmlu_acc\": 0.3068, \"gsm8k_exact_match\": 0.0394, \"actual_sparsity\": 0.398}\n\n=== d030_kl50_uniform ===\n  metrics: {\"wikitext2_ppl\": 11.96, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.500 across all 32 layers\", \"mmlu_change_vs_global\": \"+1.86pp (0.2591 → 0.2777, not significant)\", \"gsm8k_change_vs_global\": \"+0.91pp (0.0121 → 0.0212, not significant)\", \"conclusion_note\": \"50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\"}\n\n=== db_sensitivity_sweep ===\n  metrics: {\"db64_per_token_ppl\": 10.158, \"db64_teal_global_ppl\": 12.076, \"db64_sparsity\": 0.5, \"db64_loss\": 0.361, \"db128_teal_global_ppl\": 11.963, \"db128_per_token_ppl\": 9.218, \"db256_per_token_ppl\": 8.586, \"db256_teal_global_ppl\": 12.105, \"db256_sparsity\": 0.5, \"db256_loss\": 0.27, \"db512_per_token_ppl\": 7.933, \"db512_teal_global_ppl\": 12.315, \"db512_sparsity\": 0.5, \"db512_loss\": 0.224, \"best_teal_global_db\": 128, \"best_teal_global_ppl\": 11.963}\n\n=== dense_baseline_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.8235, \"piqa_acc_norm\": 0.809}\n\n=== downstream_dense_baseline ===\n  metrics: {\"hellaswag_acc_norm\": 0.8233, \"hellaswag_acc_norm_stderr\": 0.0038, \"piqa_acc_norm\": 0.8074, \"piqa_acc_norm_stderr\": 0.0092, \"boolq_acc\": 0.8294, \"boolq_acc_stderr\": 0.0066}\n\n=== downstream_extended_kl30_s42 ===\n  metrics: {\"hellaswag_acc_norm\": 0.727, \"hellaswag_acc\": 0.527, \"piqa_acc_norm\": 0.7595, \"piqa_acc\": 0.747, \"boolq_acc\": 0.7685}\n\n=== downstream_teal30_baseline ===\n  metrics: {\"hellaswag_acc\": 0.4878, \"hellaswag_acc_norm\": 0.667, \"piqa_acc\": 0.7258, \"piqa_acc_norm\": 0.7361, \"boolq_acc\": 0.685}\n\n=== eval_bce_v3_s42 ===\n  metrics: {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 22.51, \"teal_sparse_ppl\": 27.97, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2048, \"arc_challenge_acc_norm\": 0.2398, \"arc_challenge_acc_norm_stderr\": 0.0125, \"winogrande_acc\": 0.5059, \"winogrande_acc_stderr\": 0.0141, \"mmlu_acc\": 0.3002, \"mmlu_acc_stderr\": 0.0038, \"gsm8k_exact_match\": 0.0485, \"gsm8k_exact_match_strict\": 0.0425, \"gsm8k_exact_match_stderr\": 0.0059}\n\n=== eval_c1_retrain_30pct_s123 ===\n  metrics: {\"wikitext2_ppl\": 8.84, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6977, \"mmlu_acc\": 0.3992, \"gsm8k_exact_match\": 0.0682}\n\n=== eval_c1_retrain_30pct_s456 ===\n  metrics: {\"wikitext2_ppl\": 8.82, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6993, \"mmlu_acc\": 0.4104, \"gsm8k_exact_match\": 0.066}\n\n=== eval_c4_ood_kl50 ===\n  metrics: {\"dense_ppl\": 9.2075, \"kl_50_global_ppl\": 18.401, \"teal_50_ppl\": 38.7503, \"kl_vs_dense_ratio\": 2, \"teal_vs_dense_ratio\": 4.21}\n\n=== eval_kl30_teal_30pct ===\n  metrics: {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"sparsity_target\": 0.3, \"actual_sparsity\": 0.3}\n\n=== gradient_snr_constrained_v2 ===\n  metrics: {\"kl_avg_snr\": 0.000545, \"bce_avg_snr\": 5.28e-06, \"snr_ratio\": 103.2, \"kl_final_sparsity\": 0.508, \"bce_final_sparsity\": 0.591, \"steps\": 200}\n\n=== gradient_snr_kl_vs_bce ===\n  metrics: {\"kl_avg_snr\": 5.77e-05, \"bce_avg_snr\": 1e-05, \"snr_ratio\": 5.76, \"early_layer_ratio_range\": \"34-156x\", \"late_layer_ratio_range\": \"2-4x\"}\n\n=== jsd_30_s123 ===\n  metrics: {\"ppl\": 8.9144, \"sparsity\": 0.296, \"allocation\": \"uniform\"}\n\n=== jsd_30_s42 ===\n  metrics: {\"wikitext2_ppl\": 8.884, \"arc_challenge_acc_norm\": 0.4445, \"winogrande_acc\": 0.7072, \"mmlu_acc\": 0.3825, \"gsm8k_exact_match\": 0.0925, \"hellaswag_acc_norm\": 0.7073, \"piqa_acc_norm\": 0.7508, \"model_level_sparsity\": 0.285}\n\n=== jsd_30_s42_uniform_eval ===\n  metrics: {\"ppl\": 8.8848, \"arc_challenge\": 0.4437, \"winogrande\": 0.6977, \"mmlu\": 0.3857, \"gsm8k\": 0.0857, \"hellaswag\": 0.7063, \"piqa\": 0.7519}\n\n=== jsd_30_s456 ===\n  metrics: {\"ppl\": 8.9099, \"sparsity\": 0.296, \"allocation\": \"uniform\"}\n\n=== kl30_8b_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9267, \"arc_challenge_acc\": 0.4462, \"arc_challenge_acc_norm\": 0.4744, \"winogrande_acc\": 0.7024, \"mmlu_acc\": 0.3836, \"gsm8k_exact_match\": 0.0917}\n\n=== kl30_8b_s123_train ===\n  metrics: {\"wikitext2_ppl\": 8.9267, \"sparsity\": 0.3, \"training_loss\": 0.147}\n\n=== kl30_8b_s456_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc\": 0.436, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}\n\n=== kl30_8b_s456_train ===\n  metrics: {\"wikitext2_ppl\": 8.9614, \"sparsity\": 0.3, \"training_loss\": 0.148}\n\n=== kl30_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\"}\n\n=== kl30_s123_global_v3 ===\n  metrics: {\"wikitext2_ppl\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}\n\n=== kl30_s123_uniform_v2 ===\n  metrics: {\"wikitext2_ppl\": 8.8186, \"arc_challenge_acc_norm\": 0.471, \"winogrande_acc\": 0.6961, \"mmlu_acc\": 0.3763, \"gsm8k_exact_match\": 0.0705}\n\n=== kl30_s123_uniform_v3 ===\n  metrics: {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2157.6}\n\n=== kl30_s42_global_mmlu_recheck ===\n  metrics: {\"mmlu_acc\": 0.2527, \"mmlu_stderr\": 0.00364}\n\n=== kl30_s456_global_eval ===\n  metrics: {\"ppl_wikitext2\": 8.9332, \"arc_challenge\": 0.4633, \"winogrande\": 0.7111, \"mmlu\": 0.4382, \"gsm8k\": 0.0758}\n\n=== kl30_s456_global_v3 ===\n  metrics: {\"wikitext2_ppl\": 8.9332, \"arc_challenge_acc_norm\": 0.4633, \"winogrande_acc\": 0.7111, \"mmlu_acc\": 0.4382, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}\n\n=== kl30_s456_train ===\n  metrics: {\"final_loss\": 0.2021, \"actual_sparsity\": 0.289, \"constraint_satisfied\": true, \"training_steps\": 1000}\n\n=== kl30_s456_uniform_eval ===\n  metrics: {\"mmlu\": 0.4198, \"ppl_uniform\": 8.7947, \"arc_challenge\": 0.4505, \"winogrande\": 0.6875, \"gsm8k\": 0.0758}\n\n=== kl30_s456_uniform_v2 ===\n  metrics: {\"wikitext2_ppl\": 8.8284, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6953, \"mmlu_acc\": 0.3727, \"gsm8k_exact_match\": 0.0705}\n\n=== kl30_s456_uniform_v3 ===\n  metrics: {\"wikitext2_ppl\": 8.7947, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6875, \"mmlu_acc\": 0.4198, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2325.3}\n\n=== kl30_uniform_boolq_s123 ===\n  metrics: {\"boolq_acc\": 0.7006}\n\n=== kl30_uniform_boolq_s42 ===\n  metrics: {\"boolq_acc\": 0.756}\n\n=== kl30_uniform_boolq_s456 ===\n  metrics: {\"boolq_acc\": 0.7554}\n\n=== kl30_uniform_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481, \"note\": \"from v2 retry\"}\n\n=== kl30_uniform_hellaswag_piqa_v2 ===\n  metrics: {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481}\n\n=== kl50_global_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948, \"note\": \"from v2 retry\"}\n\n=== kl50_global_hellaswag_piqa_v2 ===\n  metrics: {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948}\n\n=== kl50_global_s123_downstream_v2 ===\n  metrics: {\"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6401, \"mmlu_acc\": 0.2908, \"gsm8k_exact_match\": 0.0341}\n\n=== kl50_global_s123_reeval ===\n  metrics: {\"wikitext2_ppl\": 11.7184, \"arc_challenge_acc_norm\": 0.3635, \"winogrande_acc\": 0.6109, \"mmlu_acc\": 0.2834, \"gsm8k_exact_match\": 0.0258}\n\n=== kl50_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 11.745, \"arc_challenge\": 0.3814, \"winogrande\": 0.6125, \"mmlu\": 0.2752, \"gsm8k\": 0.0281}\n\n=== kl50_s123_uniform_eval ===\n  metrics: {\"wikitext2_ppl\": 11.89, \"arc_challenge_acc_norm\": 37.88, \"winogrande_acc\": 62.19, \"mmlu_acc\": 27.75, \"gsm8k_exact_match\": 2.35, \"comparison_vs_global_topk\": {\"ppl_delta\": -0.94, \"arc_c_delta\": -5.55, \"wg_delta\": -6.71, \"mmlu_delta\": -8.2, \"gsm8k_delta\": -5}, \"note\": \"Uniform allocation: better PPL but catastrophic downstream degradation vs global_topk. Confirms global_topk allocation is critical for downstream quality.\"}\n\n=== kl50_s42_global_eval ===\n  metrics: {\"wikitext2_ppl\": 11.8038, \"arc_challenge_acc_norm\": 0.3336, \"winogrande_acc\": 0.6338, \"mmlu_acc\": 0.2819, \"gsm8k_exact_match\": 0.0167}\n\n=== kl50_s42_uniform_eval ===\n  metrics: {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3259, \"winogrande_acc\": 0.6235, \"mmlu_acc\": 0.2792, \"gsm8k_exact_match\": 0.0197}\n\n=== kl50_s456_eval ===\n  metrics: {\"wikitext2_ppl\": 11.8614, \"arc_challenge_acc_norm\": 0.3754, \"winogrande_acc\": 0.6417, \"mmlu_acc\": 0.2784, \"gsm8k_exact_match\": 0.0212}\n\n=== kl50_s456_global_eval ===\n  metrics: {\"ppl_wikitext2\": 11.8057, \"arc_challenge\": 0.3319, \"winogrande\": 0.6488, \"mmlu\": 0.2794, \"gsm8k\": 0.0212}\n\n=== kl50_s456_train ===\n  metrics: {\"final_loss\": 0.397, \"final_kl_normalized\": 0.397, \"final_sparsity\": 0.492, \"final_lambda\": 5000, \"final_tau\": 0.1, \"steps_completed\": 1000}\n\n=== kl50_s456_uniform_eval ===\n  metrics: {\"wikitext2_ppl\": 11.9538, \"arc_challenge_acc_norm\": 0.3831, \"winogrande_acc\": 0.6196, \"mmlu_acc\": 0.275, \"gsm8k_exact_match\": 0.0288}\n\n=== kl50_uniform_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.5666, \"piqa_acc_norm\": 0.691}\n\n=== kl_30pct_s123 ===\n  metrics: {\"ppl_wikitext2\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"sparsity\": 0.3, \"allocation\": \"global\"}\n\n=== kl_50pct_s123 ===\n  metrics: {\"ppl_wikitext2\": 11.745, \"arc_challenge_acc_norm\": 0.3814, \"winogrande_acc\": 0.6125, \"mmlu_acc\": 0.2752, \"gsm8k_exact_match\": 0.0281, \"sparsity\": 0.5, \"allocation\": \"global\"}\n\n=== kl_bce_f1_oracle ===\n  metrics: {\"bce_f1\": 0.6128, \"bce_precision\": 0.6132, \"bce_recall\": 0.6124, \"kl_f1\": 0.5397, \"kl_precision\": 0.5112, \"kl_recall\": 0.5715, \"random_f1\": 0.5, \"kl_ppl\": 11.79, \"bce_ppl\": 22.51}\n\n=== kl_comp_30pct_s123 ===\n  metrics: {\"final_loss\": 0.7617, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.0469, 1.3828, 1.0703, 0.9609, 0.8711, 0.7305, 0.6875, 0.7773, 0.7969, 0.7617]}\n\n=== kl_comp_30pct_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}\n\n=== kl_comp_30pct_s123_ppl ===\n  metrics: {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 123}\n\n=== kl_comp_30pct_s42 ===\n  metrics: {\"final_loss\": 0.6992, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.3594, 1.3516, 1.0859, 0.9219, 0.8789, 0.8281, 0.7461, 0.7344, 0.6953, 0.6992]}\n\n=== kl_comp_30pct_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}\n\n=== kl_comp_30pct_s42_ppl ===\n  metrics: {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 42}\n\n=== kl_comp_30pct_s456 ===\n  metrics: {}\n\n=== kl_comp_30pct_s456_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}\n\n=== kl_comp_50pct_s42 ===\n  metrics: {}\n\n=== kl_comp_50pct_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129}\n\n=== kl_only_s0 ===\n  metrics: {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.19, \"teal_sparse_ppl\": 12.03, \"model_level_sparsity\": 0.499, \"ppl_increase_vs_true_dense_pct\": 96.57, \"eval_seq_len\": 2048, \"calibration_samples\": 32}\n\n=== kl_only_s1 ===\n  metrics: {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.15, \"teal_sparse_ppl\": 11.99, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 96}\n\n=== kl_sparsity25_s123 ===\n  metrics: {\"final_loss\": 0.153, \"final_sparsity\": 0.23, \"steps\": 1000}\n\n=== kl_sparsity25_s42 ===\n  metrics: {\"train_loss_final\": 0.1582, \"kl_normalized_final\": 0.1582, \"sparsity_actual\": 0.23, \"sparsity_target\": 0.25, \"lambda_final\": 5000, \"tau_final\": 0.1, \"steps\": 1000}\n\n=== kl_sparsity25_s42_eval_teal ===\n  metrics: {\"wikitext2_ppl\": 8.169, \"arc_challenge_acc_norm\": 0.4539, \"winogrande_acc\": 0.7056, \"mmlu_acc\": 0.466, \"gsm8k_exact_match\": 0.1145, \"actual_sparsity\": 0.23, \"allocation\": \"global_topk\"}\n\n=== kl_sparsity25_s42_eval_teal_uniform ===\n  metrics: {\"wikitext2_ppl\": 8.2344, \"arc_challenge_acc_norm\": 0.465, \"winogrande_acc\": 0.7182, \"mmlu_acc\": 0.4395, \"gsm8k_exact_match\": 0.1099, \"actual_sparsity\": 0.25, \"allocation\": \"uniform\"}\n\n=== kl_sparsity30_s42_v3 ===\n  metrics: {\"loss\": 0.165, \"kl_normalized\": 0.165, \"kl_raw\": 0.165, \"sparsity\": 0.285, \"lambda_sparse\": 5000, \"tau\": 0.1, \"constraint_loss\": 0, \"steps\": 1000, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"teal_sparse_ppl_note\": \"已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\", \"model_level_sparsity\": 0.3, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048}\n\n=== kl_sparsity35_s42 ===\n  metrics: {\"final_loss\": 0.203, \"final_sparsity\": 0.336, \"steps\": 1000}\n\n=== kl_sparsity35_s42_eval_teal ===\n  metrics: {\"ppl_wikitext2\": 9.3133, \"arc_challenge_acc\": 0.3643, \"arc_challenge_acc_norm\": 0.3891, \"winogrande_acc\": 0.6764, \"mmlu_acc\": 0.4041, \"gsm8k_exact_match\": 0.0773, \"actual_sparsity\": 0.336}\n\n=== kl_sparsity35_s42_eval_teal_uniform ===\n  metrics: {\"wikitext2_ppl\": 9.4416, \"arc_challenge_acc_norm\": 0.3874, \"winogrande_acc\": 0.6654, \"mmlu_acc\": 0.3783, \"gsm8k_exact_match\": 0.0432, \"actual_sparsity\": 0.35, \"allocation\": \"uniform\"}\n\n=== kl_sparsity40_s42_global_eval_v2 ===\n  metrics: {\"wikitext2_ppl\": 10.14, \"arc_challenge_acc_norm\": 0.3951, \"winogrande_acc\": 0.6748, \"mmlu_acc\": 0.3947, \"gsm8k_exact_match\": 0.066, \"hellaswag_acc_norm\": 0.6779, \"piqa_acc_norm\": 0.7269}\n\n=== kl_sparsity40_s42_retrain_uniform ===\n  metrics: {\"wikitext2_ppl\": 10.76, \"arc_challenge_acc_norm\": 0.3959, \"winogrande_acc\": 0.6306, \"mmlu_acc\": 0.355, \"gsm8k_acc\": 0.0356, \"training_final_loss\": 0.2598, \"training_final_sparsity\": 0.387}\n\n=== kl_sparsity40_s42_uniform_hspiqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.6497, \"piqa_acc_norm\": 0.7236, \"model_level_sparsity\": 0.397}\n\n=== kl_sparsity45_s42 ===\n  metrics: {\"final_loss\": 0.33, \"final_sparsity\": 0.449, \"steps\": 1000}\n\n=== kl_sparsity45_s42_eval_teal ===\n  metrics: {\"ppl_wikitext2\": 10.803, \"arc_challenge_acc\": 0.3498, \"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6464, \"mmlu_acc\": 0.3037, \"gsm8k_exact_match\": 0.0296, \"actual_sparsity\": 0.449}\n\n=== kl_sparsity45_s42_eval_teal_uniform ===\n  metrics: {\"wikitext2_ppl\": 10.9488, \"arc_challenge_acc_norm\": 0.3763, \"winogrande_acc\": 0.6361, \"mmlu_acc\": 0.3063, \"gsm8k_exact_match\": 0.0273, \"actual_sparsity\": 0.45, \"allocation\": \"uniform\"}\n\n=== latency_benchmark ===\n  metrics: {\"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition\", \"dtype\": \"float16\", \"attn\": \"flash_attention_2\", \"batch\": 1, \"seq_len\": 2048, \"warmup\": 10, \"iters\": 100, \"dense_ms\": 119.11, \"dense_std\": 0.57, \"dense_tokens_per_s\": 17194.5, \"kl_30pct_ms\": 126.64, \"kl_30pct_std\": 0.7, \"kl_30pct_tokens_per_s\": 16171.8, \"kl_30pct_speedup\": 0.941, \"kl_50pct_ms\": 126.78, \"kl_50pct_std\": 0.31, \"kl_50pct_tokens_per_s\": 16154.2, \"kl_50pct_speedup\": 0.939, \"comp_30pct_ms\": 129.94, \"comp_30pct_std\": 0.75, \"comp_30pct_tokens_per_s\": 15761.4, \"comp_30pct_speedup\": 0.917, \"comp_50pct_ms\": 129.71, \"comp_50pct_std\": 0.53, \"comp_50pct_tokens_per_s\": 15788.8, \"comp_50pct_speedup\": 0.918, \"predictor_overhead_ms\": 3.17, \"predictor_overhead_pct\": 2.7, \"per_layer_predictor_ms\": 0.099, \"dense_ffn_per_layer_ms\": 2.427, \"sparse_ffn_pred_per_layer_ms\": 2.686, \"compensation_overhead_ms\": 3.3}\n\n=== lm_eval_dense ===\n  metrics: {\"arc_challenge_acc_norm\": 0.5819, \"winogrande_acc\": 0.7814, \"mmlu_acc\": 0.6532, \"gsm8k_exact_match\": 0.5004, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"dense\", \"server\": \"westd-34887\"}\n\n=== lm_eval_mistral_dense ===\n  metrics: {\"arc_challenge_acc_norm\": 0.6024, \"winogrande_acc\": 0.7869, \"mmlu_acc\": 0.6244, \"gsm8k_exact_match\": 0.3654, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"server\": \"westd-34887\"}\n\n=== lm_eval_teal_50pct ===\n  metrics: {\"method\": \"vanilla_teal\", \"sparsity\": 0.5, \"actual_sparsity\": 0.5, \"arc_challenge_acc_norm\": 0.291, \"winogrande_acc\": 0.5556, \"mmlu_acc\": 0.2856, \"gsm8k_exact_match_flexible\": 0.019, \"gsm8k_exact_match_strict\": 0.0114, \"arc_challenge_drop_vs_dense\": -0.5, \"winogrande_drop_vs_dense\": -0.289, \"mmlu_drop_vs_dense\": -0.563, \"gsm8k_drop_vs_dense\": -0.962, \"model\": \"Llama-3.1-8B\", \"condition\": \"TEAL 50% training-free sparsity\"}\n\n=== longbench_dense_v6 ===\n  metrics: {\"longbench_narrativeqa\": 7.3, \"longbench_qasper\": 13.4, \"longbench_gov_report\": 30.5, \"longbench_multi_news\": 2.5}\n\n=== mistral_dense_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.832, \"piqa_acc_norm\": 0.8188}\n\n=== mistral_dense_ppl ===\n  metrics: {\"wikitext2_ppl\": 5.5238, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"sparsity\": 0}\n\n=== mistral_kl30_downstream ===\n  metrics: {\"arc_challenge_acc_norm\": 0.5017, \"winogrande_acc\": 0.6914, \"mmlu_acc\": 0.4404, \"gsm8k_exact_match\": 0.1114}\n\n=== mistral_kl30_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.6892, \"piqa_acc_norm\": 0.7519}\n\n=== mistral_kl30_pertoken ===\n  metrics: {\"wikitext2_ppl\": 6.048, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 0.5242}\n\n=== mistral_kl30_s123 ===\n  metrics: {\"training_final_loss\": 0.0996, \"training_final_sparsity\": 0.281, \"wikitext2_ppl\": 7.1491, \"arc_challenge_acc_norm\": 0.378, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.4423, \"gsm8k_exact_match\": 0.0773, \"hellaswag_acc_norm\": 0.6961, \"piqa_acc_norm\": 0.7459}\n\n=== mistral_kl30_s42 ===\n  metrics: {\"kl_per_token_ppl\": 6.048, \"kl_teal_global_ppl\": 6.7733, \"teal_baseline_ppl\": 8.3807, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 1.386, \"ppl_vs_dense_pct\": 9.5}\n\n=== mistral_kl30_s456 ===\n  metrics: {\"training_final_loss\": 0.105, \"training_final_sparsity\": 0.281, \"wikitext2_ppl\": 6.8752, \"arc_challenge_acc_norm\": 0.4684, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.4161, \"gsm8k_exact_match\": 0.0697, \"hellaswag_acc_norm\": 0.705, \"piqa_acc_norm\": 0.7448}\n\n=== mistral_kl30_teal_global ===\n  metrics: {\"wikitext2_ppl\": 6.7733, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.2495}\n\n=== mistral_kl50_pertoken ===\n  metrics: {\"wikitext2_ppl\": 7.2931, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.7693}\n\n=== mistral_kl50_teal_global ===\n  metrics: {\"wikitext2_ppl\": 8.6489, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.1251}\n\n=== mistral_kl70_pertoken ===\n  metrics: {\"wikitext2_ppl\": 9.1086, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.5848}\n\n=== mistral_kl70_s42 ===\n  metrics: {\"kl_per_token_ppl\": 9.1086, \"kl_teal_global_ppl\": 13.3254, \"teal_baseline_ppl\": 61.716, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 6.77, \"final_loss\": 0.3945, \"actual_sparsity\": 0.682}\n\n=== mistral_kl70_teal_global ===\n  metrics: {\"wikitext2_ppl\": 13.3254, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 7.8016}\n\n=== mistral_kl_s42 ===\n  metrics: {\"train_final_loss\": 0.2188, \"train_final_kl_raw\": 0.2188, \"train_final_kl_norm\": 0.2188, \"train_final_constraint\": 0, \"train_final_sparsity\": 0.48, \"train_final_lambda\": 1000, \"train_final_tau\": 0.1, \"train_steps_completed\": 1000, \"true_dense_ppl\": 5.52, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_samples\": 159}\n\n=== mistral_teal30_baseline ===\n  metrics: {\"wikitext2_ppl\": 8.3807, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 2.8569}\n\n=== mistral_teal30_downstream ===\n  metrics: {\"wikitext2_ppl\": 8.3807, \"arc_challenge_acc_norm\": 0.4113, \"winogrande_acc\": 0.6354, \"mmlu_acc",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/bt4n79nxb.txt",
    "persistedOutputSize": 50403
  },
  "sourceToolAssistantUUID": "ba2eb6a9-a5a7-4c3c-bcc1-647f81047294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "leafUuid": "332a9c0a-4d48-4f8e-a53e-afe3d8b70775",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper and registry data consistency for R28",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Assistant

_source line 46 · 2026-05-24T03:58:04.817Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the full output file to get all the success experiments and their metrics. This is a large output, so I'll need to read it in chunks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "332a9c0a-4d48-4f8e-a53e-afe3d8b70775",
  "isSidechain": false,
  "requestId": "req_011CbListX5VBLTFNEUkccsc",
  "type": "assistant",
  "uuid": "5c2a38d2-9f18-43b9-a43f-7f62dc677122",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDg5BAx1TBX3V8CRGoXnKC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 64889,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1525,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 64889,
          "cache_creation_input_tokens": 1525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1525
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 47 · 2026-05-24T03:58:05.785Z_

Let me read the full registry output and do the cross-validation systematically. I'll delegate this to a thorough agent since there's a lot of data to cross-reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c2a38d2-9f18-43b9-a43f-7f62dc677122",
  "isSidechain": false,
  "requestId": "req_011CbListX5VBLTFNEUkccsc",
  "type": "assistant",
  "uuid": "3b8e403c-2b42-4e1f-b316-2ca3a14333a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDg5BAx1TBX3V8CRGoXnKC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 64889,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1525,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 64889,
          "cache_creation_input_tokens": 1525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1525
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-24T03:58:09.781Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fe8muR4Z3fJCLqdXrU9NX3`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/bt4n79nxb.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b8e403c-2b42-4e1f-b316-2ca3a14333a1",
  "isSidechain": false,
  "requestId": "req_011CbListX5VBLTFNEUkccsc",
  "type": "assistant",
  "uuid": "1fcacb78-9c16-4d25-a5f0-419d7d2ccce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDg5BAx1TBX3V8CRGoXnKC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1525,
      "cache_read_input_tokens": 64889,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1525,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 64889,
          "cache_creation_input_tokens": 1525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1525
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-24T03:58:09.787Z_

<details><summary>↩ Tool result · `toolu_01Fe8muR4Z3fJCLqdXrU9NX3`</summary>

```text
1	Total experiments: 408
2	Success experiments: 257
3	
4	=== bce_30_s42_uniform_eval ===
5	  metrics: {"ppl": 15.7069, "arc_challenge": 0.3319, "winogrande": 0.618, "mmlu": 0.4237, "gsm8k": 0.0394, "hellaswag": 0.6156, "piqa": 0.741}
6	
7	=== bce_30pct_s42 ===
8	  metrics: {}
9	
10	=== bce_50pct_teal_global_unified ===
11	  metrics: {"wikitext2_ppl": 27.97, "arc_challenge_acc_norm": 0.2765, "winogrande_acc": 0.5162, "mmlu_acc": 0.2614, "gsm8k_exact_match": 0.019}
12	
13	=== bce_gumbel_lagrangian_isolation ===
14	  metrics: {"lr_1e4_ppl": 42.99, "lr_1e3_ppl": 48.4, "lr_3e3_ppl": 38.02, "lr_1e4_bce_loss": 0.7158, "lr_1e3_bce_loss": 0.6781, "lr_3e3_bce_loss": 0.6632, "lr_1e4_sparsity": 0.514, "lr_1e3_sparsity": 0.506, "lr_3e3_sparsity": 0.504, "best_ppl": 38.02, "best_lr": "3e-3", "kl_baseline_ppl": 11.79, "gap_vs_kl": 26.23}
15	
16	=== bce_gumbel_no_penalty_s42 ===
17	  metrics: {"training_bce_loss": 0.6307, "training_sparsity": 0.383, "wikitext2_ppl": 32.22, "training_time_seconds": 977.6}
18	
19	=== bce_iso_v3_s123_30pct_uniform_eval ===
20	  metrics: {"ppl": 15.2051, "arc_challenge": 0.3396, "winogrande": 0.6046, "mmlu": 0.4363, "gsm8k": 0.0455, "hellaswag": 0.614, "piqa": 0.7356}
21	
22	=== bce_iso_v3_s42_30pct_uniform_eval ===
23	  metrics: {"ppl": 14.947, "arc_challenge": 0.3294, "winogrande": 0.6062, "mmlu": 0.4291, "gsm8k": 0.0379, "hellaswag": 0.6165, "piqa": 0.7356}
24	
25	=== bce_iso_v3_s456_30pct_uniform_eval ===
26	  metrics: {"ppl": 15.1102, "arc_challenge": 0.3345, "winogrande": 0.6219, "mmlu": 0.4261, "gsm8k": 0.0356, "hellaswag": 0.6158, "piqa": 0.7323}
27	
28	=== bce_isocompute_hellaswag_piqa_v2 ===
29	  metrics: {"hellaswag_acc_norm": 0.6281, "piqa_acc_norm": 0.7421}
30	
31	=== bce_isocompute_v3_s123 ===
32	  metrics: {}
33	
34	=== bce_isocompute_v3_s123_eval ===
35	  metrics: {"wikitext2_ppl": 28.0627, "arc_challenge_acc_norm": 0.2696, "winogrande_acc": 0.513, "mmlu_acc": 0.2655, "gsm8k_exact_match": 0.022}
36	
37	=== bce_isocompute_v3_s42 ===
38	  metrics: {"steps": 2700, "loss": 0.6382, "bce_loss": 0.6371, "reg_loss": 0.001, "sparsity": 0.51, "training_time_seconds": 2828, "note": "BCE saturation confirmed: step 500→2700 only 0.006 improvement"}
39	
40	=== bce_isocompute_v3_s42_eval ===
41	  metrics: {"wikitext2_ppl": 27.9696, "arc_challenge_acc": 0.2346, "arc_challenge_acc_norm": 0.2765, "winogrande_acc": 0.5162, "mmlu_acc": 0.2614, "gsm8k_exact_match": 0.019}
42	
43	=== bce_isocompute_v3_s456 ===
44	  metrics: {"final_loss": 0.6368, "final_sparsity": 0.51, "training_steps": 2700}
45	
46	=== bce_isocompute_v3_s456_eval ===
47	  metrics: {"teal_sparse_ppl": 28.3503, "model_level_sparsity": 0.5, "arc_challenge_acc": 0.2312, "arc_challenge_acc_stderr": 0.01232, "arc_challenge_acc_norm": 0.2807, "arc_challenge_acc_norm_stderr": 0.01313, "winogrande_acc": 0.5241, "winogrande_acc_stderr": 0.01404, "mmlu_acc": 0.2567, "mmlu_acc_stderr": 0.00367, "gsm8k_exact_match": 0.022, "gsm8k_exact_match_stderr": 0.00404, "gsm8k_exact_match_strict": 0.00834, "gsm8k_exact_match_strict_stderr": 0.0025}
48	
49	=== bench_dense ===
50	  metrics: {"wikitext2_ppl": 6.1173, "arc_challenge_acc": 0.5478, "arc_challenge_acc_norm": 0.5828, "winogrande_acc": 0.7806, "mmlu_acc": 0.6527, "gsm8k_exact_match": 0.4875}
51	
52	=== bench_kl30_global ===
53	  metrics: {"wikitext2_ppl": 8.9768, "arc_challenge_acc_norm": 0.3968, "winogrande_acc": 0.7017, "mmlu_acc": 0.2527, "gsm8k_exact_match": 0.0879, "actual_sparsity": 0.3}
54	
55	=== bench_kl30_uniform ===
56	  metrics: {"wikitext2_ppl": 8.8157, "arc_challenge_acc_norm": 0.4078, "winogrande_acc": 0.6859, "mmlu_acc": 0.4061, "gsm8k_exact_match": 0.0735, "actual_sparsity": 0.3}
57	
58	=== bench_kl40_global ===
59	  metrics: {"wikitext2_ppl": 10.117, "arc_challenge_acc_norm": 0.4096, "winogrande_acc": 0.6535, "mmlu_acc": 0.3806, "gsm8k_exact_match": 0.05, "actual_sparsity": 0.4}
60	
61	=== bench_kl50_global ===
62	  metrics: {"wikitext2_ppl": 11.7933, "arc_challenge_acc_norm": 0.3285, "winogrande_acc": 0.6346, "mmlu_acc": 0.2789, "gsm8k_exact_match": 0.0129, "actual_sparsity": 0.5}
63	
64	=== bench_kl50_uniform ===
65	  metrics: {"wikitext2_ppl": 11.963, "arc_challenge_acc_norm": 0.3276, "winogrande_acc": 0.629, "mmlu_acc": 0.2777, "gsm8k_exact_match": 0.0212, "actual_sparsity": 0.5}
66	
67	=== bench_kl50_uniform_s123 ===
68	  metrics: {"wikitext2_ppl": 11.83, "arc_challenge_acc_norm": 0.3515, "winogrande_acc": 0.6298, "mmlu_acc": 0.2751, "gsm8k_exact_match": 0.0235, "actual_sparsity": 0.5}
69	
70	=== bench_kl50_uniform_s456 ===
71	  metrics: {"wikitext2_ppl": 11.9604, "arc_challenge_acc_norm": 0.3345, "winogrande_acc": 0.6275, "mmlu_acc": 0.2874, "gsm8k_exact_match": 0.0212, "actual_sparsity": 0.5}
72	
73	=== bench_kl70_global ===
74	  metrics: {"wikitext2_ppl": 17.91, "dense_ppl": 6.12, "actual_sparsity": 0.7, "source": "kl_sparsity70_s42_v2 (teal_global_masks protocol)", "vanilla_teal_ppl": 100.11}
75	
76	=== bench_teal30 ===
77	  metrics: {"wikitext2_ppl": 10.97, "arc_challenge_acc_norm": 0.4232, "winogrande_acc": 0.6606, "mmlu_acc": 0.3861, "gsm8k_exact_match": 0.0788, "actual_sparsity": 0.3}
78	
79	=== bench_teal50 ===
80	  metrics: {"wikitext2_ppl": 23.31, "arc_challenge_acc_norm": 0.2841, "winogrande_acc": 0.5304, "mmlu_acc": 0.2832, "gsm8k_exact_match": 0.0197, "actual_sparsity": 0.5}
81	
82	=== bench_teal50_uniform_gsm8k ===
83	  metrics: {"gsm8k_exact_match_flexible": 0.0174}
84	
85	=== bench_teal70 ===
86	  metrics: {"wikitext2_ppl": 100.11, "dense_ppl": 6.12, "actual_sparsity": 0.7, "source": "training_free_baselines experiment (vanilla teal global)"}
87	
88	=== c1_ablation_30pct_s123 ===
89	  metrics: {"wikitext2_ppl": 8.83, "mmlu_acc": 0.3833, "winogrande_acc": 0.7119}
90	
91	=== c1_ablation_30pct_s42_eval_v2 ===
92	  metrics: {"wikitext2_ppl": 9.4463, "arc_challenge_acc_norm": 0.4027, "winogrande_acc": 0.674, "mmlu_acc": 0.4229, "gsm8k_exact_match": 0.0758}
93	
94	=== c1_ablation_30pct_s42_v2 ===
95	  metrics: {"agreement": 0.975}
96	
97	=== c1_ablation_30pct_s456 ===
98	  metrics: {"wikitext2_ppl": 8.84, "mmlu_acc": 0.367, "winogrande_acc": 0.6938}
99	
100	=== c1_ablation_bce_kl_targets_s123_v2 ===
101	  metrics: {"final_loss": 0.0537, "ppl": 9.32, "sparsity": 0.615, "agreement": 0.979, "note": "Consistent with s42 (PPL=9.29, sparsity=0.609, agreement=0.978). Both seeds converge to ~61% eval sparsity. C1 confirmed multi-seed robust."}
102	
103	=== c1_ablation_bce_kl_targets_s42 ===
104	  metrics: {"wt2_ppl": 9.29, "eval_sparsity": 0.609, "oracle_agreement": 0.978, "final_bce_loss": 0.0545, "train_steps": 1000, "train_time_sec": 877.1, "reference_kl_ppl": 11.79, "reference_bce_ppl": 22.51}
105	
106	=== c1_ablation_eval_uniform ===
107	  metrics: {"wikitext2_ppl": 11.9638, "arc_challenge_acc_norm": 0.3217, "winogrande_acc": 0.6314, "mmlu_acc": 0.2779, "gsm8k_exact_match": 0.0205, "sparsity_target": 0.5, "allocation": "uniform"}
108	
109	=== c1_retrain_30pct_s123 ===
110	  metrics: {"training_agreement": 0.977, "training_sparsity": 0.31, "wikitext2_ppl": 7.54, "actual_sparsity": 0.332}
111	
112	=== c1_retrain_30pct_s456 ===
113	  metrics: {"training_agreement": 0.977, "training_sparsity": 0.312, "wikitext2_ppl": 7.38, "actual_sparsity": 0.346}
114	
115	=== c4_kl30_s42 ===
116	  metrics: {}
117	
118	=== c4_kl30_s42_eval ===
119	  metrics: {"wikitext2_ppl": 11.554, "arc_challenge_acc_norm": 0.4309, "winogrande_acc": 0.6867, "mmlu_acc": 0.3995, "gsm8k_exact_match": 0.0409, "hellaswag_acc_norm": 0.6924, "piqa_acc_norm": 0.7503, "sparsity": 0.295}
120	
121	=== c4_ood_dense_baseline_v2 ===
122	  metrics: {"c4_ppl": 9.2075, "model": "llama-3.1-8b", "eval_sequences": 132, "seq_len": 2048}
123	
124	=== c4_ood_downstream_kl30 ===
125	  metrics: {"arc_challenge_acc_norm": 0.4036, "winogrande_acc": 0.693, "mmlu_acc": 0.4137, "gsm8k_exact_match": 0.0629, "hellaswag_acc_norm": 0.7074, "piqa_acc_norm": 0.7399, "model_level_sparsity": 0.295}
126	
127	=== c4_ood_kl30_s123_v2 ===
128	  metrics: {"c4_ppl": 16.0259, "allocation": "global_topk", "sparsity": 0.3, "model": "llama-3.1-8b", "eval_sequences": 132, "seq_len": 2048}
129	
130	=== c4_ood_kl30_s42 ===
131	  metrics: {"c4_ppl": 16.0458, "allocation": "global_topk", "sparsity": 0.3, "model": "llama-3.1-8b", "eval_sequences": 132, "seq_len": 2048}
132	
133	=== c4_ood_kl30_s42_v2 ===
134	  metrics: {"c4_ppl": 16.0401, "allocation": "global_topk", "sparsity": 0.3, "model": "llama-3.1-8b", "seed": 42}
135	
136	=== c4_ood_kl30_s456 ===
137	  metrics: {}
138	
139	=== c4_ood_kl30_uniform_s123 ===
140	  metrics: {"c4_ppl": 16.3686, "allocation": "uniform", "sparsity": 0.3, "seed": 123}
141	
142	=== c4_ood_kl30_uniform_s42 ===
143	  metrics: {"c4_ppl": 18.2211, "allocation": "uniform", "sparsity": 0.296, "seed": 42}
144	
145	=== c4_ood_kl30_uniform_s456 ===
146	  metrics: {"c4_ppl": 16.3551, "allocation": "uniform", "sparsity": 0.3, "seed": 456}
147	
148	=== c4_ood_kl50_s123 ===
149	  metrics: {"c4_ppl": 23.6064, "allocation": "global_topk", "sparsity": 0.5, "model": "llama-3.1-8b"}
150	
151	=== c4_ood_kl50_s42 ===
152	  metrics: {"c4_ppl": 23.5297, "sparsity": 0.5, "allocation": "global_topk", "seed": 42}
153	
154	=== c4_ood_kl50_s456 ===
155	  metrics: {"c4_ppl": 23.9867, "sparsity": 0.5, "allocation": "global_topk", "seed": 456}
156	
157	=== d030_kl30_uniform ===
158	  metrics: {"wikitext2_ppl": 8.8157, "arc_challenge_acc_norm": 0.4078, "winogrande_acc": 0.6859, "mmlu_acc": 0.4061, "gsm8k_exact_match": 0.0735, "actual_sparsity": 0.3, "allocation": "uniform", "per_layer_sparsity": "uniform 0.301 across all 32 layers", "mmlu_improvement_vs_global": "+11.87pp (0.2874 → 0.4061)", "gsm8k_change_vs_global": "no change (0.0743 → 0.0735, within noise)"}
159	
160	=== d030_kl40_uniform ===
161	  metrics: {"wikitext2_ppl": 8.3627, "arc_challenge_acc_norm": 0.4181, "winogrande_acc": 0.6717, "mmlu_acc": 0.3068, "gsm8k_exact_match": 0.0394, "actual_sparsity": 0.398}
162	
163	=== d030_kl50_uniform ===
164	  metrics: {"wikitext2_ppl": 11.96, "arc_challenge_acc_norm": 0.3276, "winogrande_acc": 0.629, "mmlu_acc": 0.2777, "gsm8k_exact_match": 0.0212, "actual_sparsity": 0.5, "allocation": "uniform", "per_layer_sparsity": "uniform 0.500 across all 32 layers", "mmlu_change_vs_global": "+1.86pp (0.2591 → 0.2777, not significant)", "gsm8k_change_vs_global": "+0.91pp (0.0121 → 0.0212, not significant)", "conclusion_note": "50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。"}
165	
166	=== db_sensitivity_sweep ===
167	  metrics: {"db64_per_token_ppl": 10.158, "db64_teal_global_ppl": 12.076, "db64_sparsity": 0.5, "db64_loss": 0.361, "db128_teal_global_ppl": 11.963, "db128_per_token_ppl": 9.218, "db256_per_token_ppl": 8.586, "db256_teal_global_ppl": 12.105, "db256_sparsity": 0.5, "db256_loss": 0.27, "db512_per_token_ppl": 7.933, "db512_teal_global_ppl": 12.315, "db512_sparsity": 0.5, "db512_loss": 0.224, "best_teal_global_db": 128, "best_teal_global_ppl": 11.963}
168	
169	=== dense_baseline_hellaswag_piqa ===
170	  metrics: {"hellaswag_acc_norm": 0.8235, "piqa_acc_norm": 0.809}
171	
172	=== downstream_dense_baseline ===
173	  metrics: {"hellaswag_acc_norm": 0.8233, "hellaswag_acc_norm_stderr": 0.0038, "piqa_acc_norm": 0.8074, "piqa_acc_norm_stderr": 0.0092, "boolq_acc": 0.8294, "boolq_acc_stderr": 0.0066}
174	
175	=== downstream_extended_kl30_s42 ===
176	  metrics: {"hellaswag_acc_norm": 0.727, "hellaswag_acc": 0.527, "piqa_acc_norm": 0.7595, "piqa_acc": 0.747, "boolq_acc": 0.7685}
177	
178	=== downstream_teal30_baseline ===
179	  metrics: {"hellaswag_acc": 0.4878, "hellaswag_acc_norm": 0.667, "piqa_acc": 0.7258, "piqa_acc_norm": 0.7361, "boolq_acc": 0.685}
180	
181	=== eval_bce_v3_s42 ===
182	  metrics: {"dense_ppl": 6.12, "predictor_hard_mask_ppl": 22.51, "teal_sparse_ppl": 27.97, "model_level_sparsity": 0.5, "arc_challenge_acc": 0.2048, "arc_challenge_acc_norm": 0.2398, "arc_challenge_acc_norm_stderr": 0.0125, "winogrande_acc": 0.5059, "winogrande_acc_stderr": 0.0141, "mmlu_acc": 0.3002, "mmlu_acc_stderr": 0.0038, "gsm8k_exact_match": 0.0485, "gsm8k_exact_match_strict": 0.0425, "gsm8k_exact_match_stderr": 0.0059}
183	
184	=== eval_c1_retrain_30pct_s123 ===
185	  metrics: {"wikitext2_ppl": 8.84, "arc_challenge_acc_norm": 0.4471, "winogrande_acc": 0.6977, "mmlu_acc": 0.3992, "gsm8k_exact_match": 0.0682}
186	
187	=== eval_c1_retrain_30pct_s456 ===
188	  metrics: {"wikitext2_ppl": 8.82, "arc_challenge_acc_norm": 0.4471, "winogrande_acc": 0.6993, "mmlu_acc": 0.4104, "gsm8k_exact_match": 0.066}
189	
190	=== eval_c4_ood_kl50 ===
191	  metrics: {"dense_ppl": 9.2075, "kl_50_global_ppl": 18.401, "teal_50_ppl": 38.7503, "kl_vs_dense_ratio": 2, "teal_vs_dense_ratio": 4.21}
192	
193	=== eval_kl30_teal_30pct ===
194	  metrics: {"dense_ppl": 6.12, "predictor_hard_mask_ppl": 7.3, "teal_sparse_ppl": 8.98, "sparsity_target": 0.3, "actual_sparsity": 0.3}
195	
196	=== gradient_snr_constrained_v2 ===
197	  metrics: {"kl_avg_snr": 0.000545, "bce_avg_snr": 5.28e-06, "snr_ratio": 103.2, "kl_final_sparsity": 0.508, "bce_final_sparsity": 0.591, "steps": 200}
198	
199	=== gradient_snr_kl_vs_bce ===
200	  metrics: {"kl_avg_snr": 5.77e-05, "bce_avg_snr": 1e-05, "snr_ratio": 5.76, "early_layer_ratio_range": "34-156x", "late_layer_ratio_range": "2-4x"}
201	
202	=== jsd_30_s123 ===
203	  metrics: {"ppl": 8.9144, "sparsity": 0.296, "allocation": "uniform"}
204	
205	=== jsd_30_s42 ===
206	  metrics: {"wikitext2_ppl": 8.884, "arc_challenge_acc_norm": 0.4445, "winogrande_acc": 0.7072, "mmlu_acc": 0.3825, "gsm8k_exact_match": 0.0925, "hellaswag_acc_norm": 0.7073, "piqa_acc_norm": 0.7508, "model_level_sparsity": 0.285}
207	
208	=== jsd_30_s42_uniform_eval ===
209	  metrics: {"ppl": 8.8848, "arc_challenge": 0.4437, "winogrande": 0.6977, "mmlu": 0.3857, "gsm8k": 0.0857, "hellaswag": 0.7063, "piqa": 0.7519}
210	
211	=== jsd_30_s456 ===
212	  metrics: {"ppl": 8.9099, "sparsity": 0.296, "allocation": "uniform"}
213	
214	=== kl30_8b_s123_eval ===
215	  metrics: {"wikitext2_ppl": 8.9267, "arc_challenge_acc": 0.4462, "arc_challenge_acc_norm": 0.4744, "winogrande_acc": 0.7024, "mmlu_acc": 0.3836, "gsm8k_exact_match": 0.0917}
216	
217	=== kl30_8b_s123_train ===
218	  metrics: {"wikitext2_ppl": 8.9267, "sparsity": 0.3, "training_loss": 0.147}
219	
220	=== kl30_8b_s456_eval ===
221	  metrics: {"wikitext2_ppl": 8.9614, "arc_challenge_acc": 0.436, "arc_challenge_acc_norm": 0.4462, "winogrande_acc": 0.7143, "mmlu_acc": 0.2714, "gsm8k_exact_match": 0.0887}
222	
223	=== kl30_8b_s456_train ===
224	  metrics: {"wikitext2_ppl": 8.9614, "sparsity": 0.3, "training_loss": 0.148}
225	
226	=== kl30_s123_eval ===
227	  metrics: {"wikitext2_ppl": 8.8308, "arc_challenge_acc_norm": 0.4531, "winogrande_acc": 0.6938, "mmlu_acc": 0.3944, "gsm8k_exact_match": 0.0751, "actual_sparsity": 0.3, "allocation": "uniform"}
228	
229	=== kl30_s123_global_v3 ===
230	  metrics: {"wikitext2_ppl": 8.9748, "arc_challenge_acc_norm": 0.4531, "winogrande_acc": 0.693, "mmlu_acc": 0.3807, "gsm8k_exact_match": 0.0758, "actual_sparsity": 0.3, "allocation": "global_topk"}
231	
232	=== kl30_s123_uniform_v2 ===
233	  metrics: {"wikitext2_ppl": 8.8186, "arc_challenge_acc_norm": 0.471, "winogrande_acc": 0.6961, "mmlu_acc": 0.3763, "gsm8k_exact_match": 0.0705}
234	
235	=== kl30_s123_uniform_v3 ===
236	  metrics: {"wikitext2_ppl": 8.8308, "arc_challenge_acc_norm": 0.4531, "winogrande_acc": 0.6938, "mmlu_acc": 0.3944, "gsm8k_exact_match": 0.0751, "actual_sparsity": 0.3, "allocation": "uniform", "eval_wall_time_sec": 2157.6}
237	
238	=== kl30_s42_global_mmlu_recheck ===
239	  metrics: {"mmlu_acc": 0.2527, "mmlu_stderr": 0.00364}
240	
241	=== kl30_s456_global_eval ===
242	  metrics: {"ppl_wikitext2": 8.9332, "arc_challenge": 0.4633, "winogrande": 0.7111, "mmlu": 0.4382, "gsm8k": 0.0758}
243	
244	=== kl30_s456_global_v3 ===
245	  metrics: {"wikitext2_ppl": 8.9332, "arc_challenge_acc_norm": 0.4633, "winogrande_acc": 0.7111, "mmlu_acc": 0.4382, "gsm8k_exact_match": 0.0758, "actual_sparsity": 0.3, "allocation": "global_topk"}
246	
247	=== kl30_s456_train ===
248	  metrics: {"final_loss": 0.2021, "actual_sparsity": 0.289, "constraint_satisfied": true, "training_steps": 1000}
249	
250	=== kl30_s456_uniform_eval ===
251	  metrics: {"mmlu": 0.4198, "ppl_uniform": 8.7947, "arc_challenge": 0.4505, "winogrande": 0.6875, "gsm8k": 0.0758}
252	
253	=== kl30_s456_uniform_v2 ===
254	  metrics: {"wikitext2_ppl": 8.8284, "arc_challenge_acc_norm": 0.4505, "winogrande_acc": 0.6953, "mmlu_acc": 0.3727, "gsm8k_exact_match": 0.0705}
255	
256	=== kl30_s456_uniform_v3 ===
257	  metrics: {"wikitext2_ppl": 8.7947, "arc_challenge_acc_norm": 0.4505, "winogrande_acc": 0.6875, "mmlu_acc": 0.4198, "gsm8k_exact_match": 0.0758, "actual_sparsity": 0.3, "allocation": "uniform", "eval_wall_time_sec": 2325.3}
258	
259	=== kl30_uniform_boolq_s123 ===
260	  metrics: {"boolq_acc": 0.7006}
261	
262	=== kl30_uniform_boolq_s42 ===
263	  metrics: {"boolq_acc": 0.756}
264	
265	=== kl30_uniform_boolq_s456 ===
266	  metrics: {"boolq_acc": 0.7554}
267	
268	=== kl30_uniform_hellaswag_piqa ===
269	  metrics: {"hellaswag_acc_norm": 0.7085, "piqa_acc_norm": 0.7481, "note": "from v2 retry"}
270	
271	=== kl30_uniform_hellaswag_piqa_v2 ===
272	  metrics: {"hellaswag_acc_norm": 0.7085, "piqa_acc_norm": 0.7481}
273	
274	=== kl50_global_hellaswag_piqa ===
275	  metrics: {"hellaswag_acc_norm": 0.5895, "piqa_acc_norm": 0.6948, "note": "from v2 retry"}
276	
277	=== kl50_global_hellaswag_piqa_v2 ===
278	  metrics: {"hellaswag_acc_norm": 0.5895, "piqa_acc_norm": 0.6948}
279	
280	=== kl50_global_s123_downstream_v2 ===
281	  metrics: {"arc_challenge_acc_norm": 0.3916, "winogrande_acc": 0.6401, "mmlu_acc": 0.2908, "gsm8k_exact_match": 0.0341}
282	
283	=== kl50_global_s123_reeval ===
284	  metrics: {"wikitext2_ppl": 11.7184, "arc_challenge_acc_norm": 0.3635, "winogrande_acc": 0.6109, "mmlu_acc": 0.2834, "gsm8k_exact_match": 0.0258}
285	
286	=== kl50_s123_eval ===
287	  metrics: {"wikitext2_ppl": 11.745, "arc_challenge": 0.3814, "winogrande": 0.6125, "mmlu": 0.2752, "gsm8k": 0.0281}
288	
289	=== kl50_s123_uniform_eval ===
290	  metrics: {"wikitext2_ppl": 11.89, "arc_challenge_acc_norm": 37.88, "winogrande_acc": 62.19, "mmlu_acc": 27.75, "gsm8k_exact_match": 2.35, "comparison_vs_global_topk": {"ppl_delta": -0.94, "arc_c_delta": -5.55, "wg_delta": -6.71, "mmlu_delta": -8.2, "gsm8k_delta": -5}, "note": "Uniform allocation: better PPL but catastrophic downstream degradation vs global_topk. Confirms global_topk allocation is critical for downstream quality."}
291	
292	=== kl50_s42_global_eval ===
293	  metrics: {"wikitext2_ppl": 11.8038, "arc_challenge_acc_norm": 0.3336, "winogrande_acc": 0.6338, "mmlu_acc": 0.2819, "gsm8k_exact_match": 0.0167}
294	
295	=== kl50_s42_uniform_eval ===
296	  metrics: {"wikitext2_ppl": 11.9638, "arc_challenge_acc_norm": 0.3259, "winogrande_acc": 0.6235, "mmlu_acc": 0.2792, "gsm8k_exact_match": 0.0197}
297	
298	=== kl50_s456_eval ===
299	  metrics: {"wikitext2_ppl": 11.8614, "arc_challenge_acc_norm": 0.3754, "winogrande_acc": 0.6417, "mmlu_acc": 0.2784, "gsm8k_exact_match": 0.0212}
300	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fcacb78-9c16-4d25-a5f0-419d7d2ccce2",
  "isSidechain": false,
  "promptId": "fdfb0d6d-9233-4c2a-afaa-5df266af136f",
  "type": "user",
  "uuid": "0757e91a-4439-43bd-9735-8f907f763549",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/bt4n79nxb.txt",
      "content": "Total experiments: 408\nSuccess experiments: 257\n\n=== bce_30_s42_uniform_eval ===\n  metrics: {\"ppl\": 15.7069, \"arc_challenge\": 0.3319, \"winogrande\": 0.618, \"mmlu\": 0.4237, \"gsm8k\": 0.0394, \"hellaswag\": 0.6156, \"piqa\": 0.741}\n\n=== bce_30pct_s42 ===\n  metrics: {}\n\n=== bce_50pct_teal_global_unified ===\n  metrics: {\"wikitext2_ppl\": 27.97, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}\n\n=== bce_gumbel_lagrangian_isolation ===\n  metrics: {\"lr_1e4_ppl\": 42.99, \"lr_1e3_ppl\": 48.4, \"lr_3e3_ppl\": 38.02, \"lr_1e4_bce_loss\": 0.7158, \"lr_1e3_bce_loss\": 0.6781, \"lr_3e3_bce_loss\": 0.6632, \"lr_1e4_sparsity\": 0.514, \"lr_1e3_sparsity\": 0.506, \"lr_3e3_sparsity\": 0.504, \"best_ppl\": 38.02, \"best_lr\": \"3e-3\", \"kl_baseline_ppl\": 11.79, \"gap_vs_kl\": 26.23}\n\n=== bce_gumbel_no_penalty_s42 ===\n  metrics: {\"training_bce_loss\": 0.6307, \"training_sparsity\": 0.383, \"wikitext2_ppl\": 32.22, \"training_time_seconds\": 977.6}\n\n=== bce_iso_v3_s123_30pct_uniform_eval ===\n  metrics: {\"ppl\": 15.2051, \"arc_challenge\": 0.3396, \"winogrande\": 0.6046, \"mmlu\": 0.4363, \"gsm8k\": 0.0455, \"hellaswag\": 0.614, \"piqa\": 0.7356}\n\n=== bce_iso_v3_s42_30pct_uniform_eval ===\n  metrics: {\"ppl\": 14.947, \"arc_challenge\": 0.3294, \"winogrande\": 0.6062, \"mmlu\": 0.4291, \"gsm8k\": 0.0379, \"hellaswag\": 0.6165, \"piqa\": 0.7356}\n\n=== bce_iso_v3_s456_30pct_uniform_eval ===\n  metrics: {\"ppl\": 15.1102, \"arc_challenge\": 0.3345, \"winogrande\": 0.6219, \"mmlu\": 0.4261, \"gsm8k\": 0.0356, \"hellaswag\": 0.6158, \"piqa\": 0.7323}\n\n=== bce_isocompute_hellaswag_piqa_v2 ===\n  metrics: {\"hellaswag_acc_norm\": 0.6281, \"piqa_acc_norm\": 0.7421}\n\n=== bce_isocompute_v3_s123 ===\n  metrics: {}\n\n=== bce_isocompute_v3_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 28.0627, \"arc_challenge_acc_norm\": 0.2696, \"winogrande_acc\": 0.513, \"mmlu_acc\": 0.2655, \"gsm8k_exact_match\": 0.022}\n\n=== bce_isocompute_v3_s42 ===\n  metrics: {\"steps\": 2700, \"loss\": 0.6382, \"bce_loss\": 0.6371, \"reg_loss\": 0.001, \"sparsity\": 0.51, \"training_time_seconds\": 2828, \"note\": \"BCE saturation confirmed: step 500→2700 only 0.006 improvement\"}\n\n=== bce_isocompute_v3_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 27.9696, \"arc_challenge_acc\": 0.2346, \"arc_challenge_acc_norm\": 0.2765, \"winogrande_acc\": 0.5162, \"mmlu_acc\": 0.2614, \"gsm8k_exact_match\": 0.019}\n\n=== bce_isocompute_v3_s456 ===\n  metrics: {\"final_loss\": 0.6368, \"final_sparsity\": 0.51, \"training_steps\": 2700}\n\n=== bce_isocompute_v3_s456_eval ===\n  metrics: {\"teal_sparse_ppl\": 28.3503, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2312, \"arc_challenge_acc_stderr\": 0.01232, \"arc_challenge_acc_norm\": 0.2807, \"arc_challenge_acc_norm_stderr\": 0.01313, \"winogrande_acc\": 0.5241, \"winogrande_acc_stderr\": 0.01404, \"mmlu_acc\": 0.2567, \"mmlu_acc_stderr\": 0.00367, \"gsm8k_exact_match\": 0.022, \"gsm8k_exact_match_stderr\": 0.00404, \"gsm8k_exact_match_strict\": 0.00834, \"gsm8k_exact_match_strict_stderr\": 0.0025}\n\n=== bench_dense ===\n  metrics: {\"wikitext2_ppl\": 6.1173, \"arc_challenge_acc\": 0.5478, \"arc_challenge_acc_norm\": 0.5828, \"winogrande_acc\": 0.7806, \"mmlu_acc\": 0.6527, \"gsm8k_exact_match\": 0.4875}\n\n=== bench_kl30_global ===\n  metrics: {\"wikitext2_ppl\": 8.9768, \"arc_challenge_acc_norm\": 0.3968, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.2527, \"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}\n\n=== bench_kl30_uniform ===\n  metrics: {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3}\n\n=== bench_kl40_global ===\n  metrics: {\"wikitext2_ppl\": 10.117, \"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6535, \"mmlu_acc\": 0.3806, \"gsm8k_exact_match\": 0.05, \"actual_sparsity\": 0.4}\n\n=== bench_kl50_global ===\n  metrics: {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129, \"actual_sparsity\": 0.5}\n\n=== bench_kl50_uniform ===\n  metrics: {\"wikitext2_ppl\": 11.963, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}\n\n=== bench_kl50_uniform_s123 ===\n  metrics: {\"wikitext2_ppl\": 11.83, \"arc_challenge_acc_norm\": 0.3515, \"winogrande_acc\": 0.6298, \"mmlu_acc\": 0.2751, \"gsm8k_exact_match\": 0.0235, \"actual_sparsity\": 0.5}\n\n=== bench_kl50_uniform_s456 ===\n  metrics: {\"wikitext2_ppl\": 11.9604, \"arc_challenge_acc_norm\": 0.3345, \"winogrande_acc\": 0.6275, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5}\n\n=== bench_kl70_global ===\n  metrics: {\"wikitext2_ppl\": 17.91, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"kl_sparsity70_s42_v2 (teal_global_masks protocol)\", \"vanilla_teal_ppl\": 100.11}\n\n=== bench_teal30 ===\n  metrics: {\"wikitext2_ppl\": 10.97, \"arc_challenge_acc_norm\": 0.4232, \"winogrande_acc\": 0.6606, \"mmlu_acc\": 0.3861, \"gsm8k_exact_match\": 0.0788, \"actual_sparsity\": 0.3}\n\n=== bench_teal50 ===\n  metrics: {\"wikitext2_ppl\": 23.31, \"arc_challenge_acc_norm\": 0.2841, \"winogrande_acc\": 0.5304, \"mmlu_acc\": 0.2832, \"gsm8k_exact_match\": 0.0197, \"actual_sparsity\": 0.5}\n\n=== bench_teal50_uniform_gsm8k ===\n  metrics: {\"gsm8k_exact_match_flexible\": 0.0174}\n\n=== bench_teal70 ===\n  metrics: {\"wikitext2_ppl\": 100.11, \"dense_ppl\": 6.12, \"actual_sparsity\": 0.7, \"source\": \"training_free_baselines experiment (vanilla teal global)\"}\n\n=== c1_ablation_30pct_s123 ===\n  metrics: {\"wikitext2_ppl\": 8.83, \"mmlu_acc\": 0.3833, \"winogrande_acc\": 0.7119}\n\n=== c1_ablation_30pct_s42_eval_v2 ===\n  metrics: {\"wikitext2_ppl\": 9.4463, \"arc_challenge_acc_norm\": 0.4027, \"winogrande_acc\": 0.674, \"mmlu_acc\": 0.4229, \"gsm8k_exact_match\": 0.0758}\n\n=== c1_ablation_30pct_s42_v2 ===\n  metrics: {\"agreement\": 0.975}\n\n=== c1_ablation_30pct_s456 ===\n  metrics: {\"wikitext2_ppl\": 8.84, \"mmlu_acc\": 0.367, \"winogrande_acc\": 0.6938}\n\n=== c1_ablation_bce_kl_targets_s123_v2 ===\n  metrics: {\"final_loss\": 0.0537, \"ppl\": 9.32, \"sparsity\": 0.615, \"agreement\": 0.979, \"note\": \"Consistent with s42 (PPL=9.29, sparsity=0.609, agreement=0.978). Both seeds converge to ~61% eval sparsity. C1 confirmed multi-seed robust.\"}\n\n=== c1_ablation_bce_kl_targets_s42 ===\n  metrics: {\"wt2_ppl\": 9.29, \"eval_sparsity\": 0.609, \"oracle_agreement\": 0.978, \"final_bce_loss\": 0.0545, \"train_steps\": 1000, \"train_time_sec\": 877.1, \"reference_kl_ppl\": 11.79, \"reference_bce_ppl\": 22.51}\n\n=== c1_ablation_eval_uniform ===\n  metrics: {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3217, \"winogrande_acc\": 0.6314, \"mmlu_acc\": 0.2779, \"gsm8k_exact_match\": 0.0205, \"sparsity_target\": 0.5, \"allocation\": \"uniform\"}\n\n=== c1_retrain_30pct_s123 ===\n  metrics: {\"training_agreement\": 0.977, \"training_sparsity\": 0.31, \"wikitext2_ppl\": 7.54, \"actual_sparsity\": 0.332}\n\n=== c1_retrain_30pct_s456 ===\n  metrics: {\"training_agreement\": 0.977, \"training_sparsity\": 0.312, \"wikitext2_ppl\": 7.38, \"actual_sparsity\": 0.346}\n\n=== c4_kl30_s42 ===\n  metrics: {}\n\n=== c4_kl30_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 11.554, \"arc_challenge_acc_norm\": 0.4309, \"winogrande_acc\": 0.6867, \"mmlu_acc\": 0.3995, \"gsm8k_exact_match\": 0.0409, \"hellaswag_acc_norm\": 0.6924, \"piqa_acc_norm\": 0.7503, \"sparsity\": 0.295}\n\n=== c4_ood_dense_baseline_v2 ===\n  metrics: {\"c4_ppl\": 9.2075, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}\n\n=== c4_ood_downstream_kl30 ===\n  metrics: {\"arc_challenge_acc_norm\": 0.4036, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.4137, \"gsm8k_exact_match\": 0.0629, \"hellaswag_acc_norm\": 0.7074, \"piqa_acc_norm\": 0.7399, \"model_level_sparsity\": 0.295}\n\n=== c4_ood_kl30_s123_v2 ===\n  metrics: {\"c4_ppl\": 16.0259, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}\n\n=== c4_ood_kl30_s42 ===\n  metrics: {\"c4_ppl\": 16.0458, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"eval_sequences\": 132, \"seq_len\": 2048}\n\n=== c4_ood_kl30_s42_v2 ===\n  metrics: {\"c4_ppl\": 16.0401, \"allocation\": \"global_topk\", \"sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"seed\": 42}\n\n=== c4_ood_kl30_s456 ===\n  metrics: {}\n\n=== c4_ood_kl30_uniform_s123 ===\n  metrics: {\"c4_ppl\": 16.3686, \"allocation\": \"uniform\", \"sparsity\": 0.3, \"seed\": 123}\n\n=== c4_ood_kl30_uniform_s42 ===\n  metrics: {\"c4_ppl\": 18.2211, \"allocation\": \"uniform\", \"sparsity\": 0.296, \"seed\": 42}\n\n=== c4_ood_kl30_uniform_s456 ===\n  metrics: {\"c4_ppl\": 16.3551, \"allocation\": \"uniform\", \"sparsity\": 0.3, \"seed\": 456}\n\n=== c4_ood_kl50_s123 ===\n  metrics: {\"c4_ppl\": 23.6064, \"allocation\": \"global_topk\", \"sparsity\": 0.5, \"model\": \"llama-3.1-8b\"}\n\n=== c4_ood_kl50_s42 ===\n  metrics: {\"c4_ppl\": 23.5297, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 42}\n\n=== c4_ood_kl50_s456 ===\n  metrics: {\"c4_ppl\": 23.9867, \"sparsity\": 0.5, \"allocation\": \"global_topk\", \"seed\": 456}\n\n=== d030_kl30_uniform ===\n  metrics: {\"wikitext2_ppl\": 8.8157, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.6859, \"mmlu_acc\": 0.4061, \"gsm8k_exact_match\": 0.0735, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.301 across all 32 layers\", \"mmlu_improvement_vs_global\": \"+11.87pp (0.2874 → 0.4061)\", \"gsm8k_change_vs_global\": \"no change (0.0743 → 0.0735, within noise)\"}\n\n=== d030_kl40_uniform ===\n  metrics: {\"wikitext2_ppl\": 8.3627, \"arc_challenge_acc_norm\": 0.4181, \"winogrande_acc\": 0.6717, \"mmlu_acc\": 0.3068, \"gsm8k_exact_match\": 0.0394, \"actual_sparsity\": 0.398}\n\n=== d030_kl50_uniform ===\n  metrics: {\"wikitext2_ppl\": 11.96, \"arc_challenge_acc_norm\": 0.3276, \"winogrande_acc\": 0.629, \"mmlu_acc\": 0.2777, \"gsm8k_exact_match\": 0.0212, \"actual_sparsity\": 0.5, \"allocation\": \"uniform\", \"per_layer_sparsity\": \"uniform 0.500 across all 32 layers\", \"mmlu_change_vs_global\": \"+1.86pp (0.2591 → 0.2777, not significant)\", \"gsm8k_change_vs_global\": \"+0.91pp (0.0121 → 0.0212, not significant)\", \"conclusion_note\": \"50% uniform 未能修复 MMLU/GSM8K collapse. Uniform allocation 的修复效应在 50% sparsity 下消失。\"}\n\n=== db_sensitivity_sweep ===\n  metrics: {\"db64_per_token_ppl\": 10.158, \"db64_teal_global_ppl\": 12.076, \"db64_sparsity\": 0.5, \"db64_loss\": 0.361, \"db128_teal_global_ppl\": 11.963, \"db128_per_token_ppl\": 9.218, \"db256_per_token_ppl\": 8.586, \"db256_teal_global_ppl\": 12.105, \"db256_sparsity\": 0.5, \"db256_loss\": 0.27, \"db512_per_token_ppl\": 7.933, \"db512_teal_global_ppl\": 12.315, \"db512_sparsity\": 0.5, \"db512_loss\": 0.224, \"best_teal_global_db\": 128, \"best_teal_global_ppl\": 11.963}\n\n=== dense_baseline_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.8235, \"piqa_acc_norm\": 0.809}\n\n=== downstream_dense_baseline ===\n  metrics: {\"hellaswag_acc_norm\": 0.8233, \"hellaswag_acc_norm_stderr\": 0.0038, \"piqa_acc_norm\": 0.8074, \"piqa_acc_norm_stderr\": 0.0092, \"boolq_acc\": 0.8294, \"boolq_acc_stderr\": 0.0066}\n\n=== downstream_extended_kl30_s42 ===\n  metrics: {\"hellaswag_acc_norm\": 0.727, \"hellaswag_acc\": 0.527, \"piqa_acc_norm\": 0.7595, \"piqa_acc\": 0.747, \"boolq_acc\": 0.7685}\n\n=== downstream_teal30_baseline ===\n  metrics: {\"hellaswag_acc\": 0.4878, \"hellaswag_acc_norm\": 0.667, \"piqa_acc\": 0.7258, \"piqa_acc_norm\": 0.7361, \"boolq_acc\": 0.685}\n\n=== eval_bce_v3_s42 ===\n  metrics: {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 22.51, \"teal_sparse_ppl\": 27.97, \"model_level_sparsity\": 0.5, \"arc_challenge_acc\": 0.2048, \"arc_challenge_acc_norm\": 0.2398, \"arc_challenge_acc_norm_stderr\": 0.0125, \"winogrande_acc\": 0.5059, \"winogrande_acc_stderr\": 0.0141, \"mmlu_acc\": 0.3002, \"mmlu_acc_stderr\": 0.0038, \"gsm8k_exact_match\": 0.0485, \"gsm8k_exact_match_strict\": 0.0425, \"gsm8k_exact_match_stderr\": 0.0059}\n\n=== eval_c1_retrain_30pct_s123 ===\n  metrics: {\"wikitext2_ppl\": 8.84, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6977, \"mmlu_acc\": 0.3992, \"gsm8k_exact_match\": 0.0682}\n\n=== eval_c1_retrain_30pct_s456 ===\n  metrics: {\"wikitext2_ppl\": 8.82, \"arc_challenge_acc_norm\": 0.4471, \"winogrande_acc\": 0.6993, \"mmlu_acc\": 0.4104, \"gsm8k_exact_match\": 0.066}\n\n=== eval_c4_ood_kl50 ===\n  metrics: {\"dense_ppl\": 9.2075, \"kl_50_global_ppl\": 18.401, \"teal_50_ppl\": 38.7503, \"kl_vs_dense_ratio\": 2, \"teal_vs_dense_ratio\": 4.21}\n\n=== eval_kl30_teal_30pct ===\n  metrics: {\"dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"sparsity_target\": 0.3, \"actual_sparsity\": 0.3}\n\n=== gradient_snr_constrained_v2 ===\n  metrics: {\"kl_avg_snr\": 0.000545, \"bce_avg_snr\": 5.28e-06, \"snr_ratio\": 103.2, \"kl_final_sparsity\": 0.508, \"bce_final_sparsity\": 0.591, \"steps\": 200}\n\n=== gradient_snr_kl_vs_bce ===\n  metrics: {\"kl_avg_snr\": 5.77e-05, \"bce_avg_snr\": 1e-05, \"snr_ratio\": 5.76, \"early_layer_ratio_range\": \"34-156x\", \"late_layer_ratio_range\": \"2-4x\"}\n\n=== jsd_30_s123 ===\n  metrics: {\"ppl\": 8.9144, \"sparsity\": 0.296, \"allocation\": \"uniform\"}\n\n=== jsd_30_s42 ===\n  metrics: {\"wikitext2_ppl\": 8.884, \"arc_challenge_acc_norm\": 0.4445, \"winogrande_acc\": 0.7072, \"mmlu_acc\": 0.3825, \"gsm8k_exact_match\": 0.0925, \"hellaswag_acc_norm\": 0.7073, \"piqa_acc_norm\": 0.7508, \"model_level_sparsity\": 0.285}\n\n=== jsd_30_s42_uniform_eval ===\n  metrics: {\"ppl\": 8.8848, \"arc_challenge\": 0.4437, \"winogrande\": 0.6977, \"mmlu\": 0.3857, \"gsm8k\": 0.0857, \"hellaswag\": 0.7063, \"piqa\": 0.7519}\n\n=== jsd_30_s456 ===\n  metrics: {\"ppl\": 8.9099, \"sparsity\": 0.296, \"allocation\": \"uniform\"}\n\n=== kl30_8b_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9267, \"arc_challenge_acc\": 0.4462, \"arc_challenge_acc_norm\": 0.4744, \"winogrande_acc\": 0.7024, \"mmlu_acc\": 0.3836, \"gsm8k_exact_match\": 0.0917}\n\n=== kl30_8b_s123_train ===\n  metrics: {\"wikitext2_ppl\": 8.9267, \"sparsity\": 0.3, \"training_loss\": 0.147}\n\n=== kl30_8b_s456_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc\": 0.436, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}\n\n=== kl30_8b_s456_train ===\n  metrics: {\"wikitext2_ppl\": 8.9614, \"sparsity\": 0.3, \"training_loss\": 0.148}\n\n=== kl30_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\"}\n\n=== kl30_s123_global_v3 ===\n  metrics: {\"wikitext2_ppl\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}\n\n=== kl30_s123_uniform_v2 ===\n  metrics: {\"wikitext2_ppl\": 8.8186, \"arc_challenge_acc_norm\": 0.471, \"winogrande_acc\": 0.6961, \"mmlu_acc\": 0.3763, \"gsm8k_exact_match\": 0.0705}\n\n=== kl30_s123_uniform_v3 ===\n  metrics: {\"wikitext2_ppl\": 8.8308, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.6938, \"mmlu_acc\": 0.3944, \"gsm8k_exact_match\": 0.0751, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2157.6}\n\n=== kl30_s42_global_mmlu_recheck ===\n  metrics: {\"mmlu_acc\": 0.2527, \"mmlu_stderr\": 0.00364}\n\n=== kl30_s456_global_eval ===\n  metrics: {\"ppl_wikitext2\": 8.9332, \"arc_challenge\": 0.4633, \"winogrande\": 0.7111, \"mmlu\": 0.4382, \"gsm8k\": 0.0758}\n\n=== kl30_s456_global_v3 ===\n  metrics: {\"wikitext2_ppl\": 8.9332, \"arc_challenge_acc_norm\": 0.4633, \"winogrande_acc\": 0.7111, \"mmlu_acc\": 0.4382, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"global_topk\"}\n\n=== kl30_s456_train ===\n  metrics: {\"final_loss\": 0.2021, \"actual_sparsity\": 0.289, \"constraint_satisfied\": true, \"training_steps\": 1000}\n\n=== kl30_s456_uniform_eval ===\n  metrics: {\"mmlu\": 0.4198, \"ppl_uniform\": 8.7947, \"arc_challenge\": 0.4505, \"winogrande\": 0.6875, \"gsm8k\": 0.0758}\n\n=== kl30_s456_uniform_v2 ===\n  metrics: {\"wikitext2_ppl\": 8.8284, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6953, \"mmlu_acc\": 0.3727, \"gsm8k_exact_match\": 0.0705}\n\n=== kl30_s456_uniform_v3 ===\n  metrics: {\"wikitext2_ppl\": 8.7947, \"arc_challenge_acc_norm\": 0.4505, \"winogrande_acc\": 0.6875, \"mmlu_acc\": 0.4198, \"gsm8k_exact_match\": 0.0758, \"actual_sparsity\": 0.3, \"allocation\": \"uniform\", \"eval_wall_time_sec\": 2325.3}\n\n=== kl30_uniform_boolq_s123 ===\n  metrics: {\"boolq_acc\": 0.7006}\n\n=== kl30_uniform_boolq_s42 ===\n  metrics: {\"boolq_acc\": 0.756}\n\n=== kl30_uniform_boolq_s456 ===\n  metrics: {\"boolq_acc\": 0.7554}\n\n=== kl30_uniform_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481, \"note\": \"from v2 retry\"}\n\n=== kl30_uniform_hellaswag_piqa_v2 ===\n  metrics: {\"hellaswag_acc_norm\": 0.7085, \"piqa_acc_norm\": 0.7481}\n\n=== kl50_global_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948, \"note\": \"from v2 retry\"}\n\n=== kl50_global_hellaswag_piqa_v2 ===\n  metrics: {\"hellaswag_acc_norm\": 0.5895, \"piqa_acc_norm\": 0.6948}\n\n=== kl50_global_s123_downstream_v2 ===\n  metrics: {\"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6401, \"mmlu_acc\": 0.2908, \"gsm8k_exact_match\": 0.0341}\n\n=== kl50_global_s123_reeval ===\n  metrics: {\"wikitext2_ppl\": 11.7184, \"arc_challenge_acc_norm\": 0.3635, \"winogrande_acc\": 0.6109, \"mmlu_acc\": 0.2834, \"gsm8k_exact_match\": 0.0258}\n\n=== kl50_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 11.745, \"arc_challenge\": 0.3814, \"winogrande\": 0.6125, \"mmlu\": 0.2752, \"gsm8k\": 0.0281}\n\n=== kl50_s123_uniform_eval ===\n  metrics: {\"wikitext2_ppl\": 11.89, \"arc_challenge_acc_norm\": 37.88, \"winogrande_acc\": 62.19, \"mmlu_acc\": 27.75, \"gsm8k_exact_match\": 2.35, \"comparison_vs_global_topk\": {\"ppl_delta\": -0.94, \"arc_c_delta\": -5.55, \"wg_delta\": -6.71, \"mmlu_delta\": -8.2, \"gsm8k_delta\": -5}, \"note\": \"Uniform allocation: better PPL but catastrophic downstream degradation vs global_topk. Confirms global_topk allocation is critical for downstream quality.\"}\n\n=== kl50_s42_global_eval ===\n  metrics: {\"wikitext2_ppl\": 11.8038, \"arc_challenge_acc_norm\": 0.3336, \"winogrande_acc\": 0.6338, \"mmlu_acc\": 0.2819, \"gsm8k_exact_match\": 0.0167}\n\n=== kl50_s42_uniform_eval ===\n  metrics: {\"wikitext2_ppl\": 11.9638, \"arc_challenge_acc_norm\": 0.3259, \"winogrande_acc\": 0.6235, \"mmlu_acc\": 0.2792, \"gsm8k_exact_match\": 0.0197}\n\n=== kl50_s456_eval ===\n  metrics: {\"wikitext2_ppl\": 11.8614, \"arc_challenge_acc_norm\": 0.3754, \"winogrande_acc\": 0.6417, \"mmlu_acc\": 0.2784, \"gsm8k_exact_match\": 0.0212}\n",
      "numLines": 300,
      "startLine": 1,
      "totalLines": 775
    }
  },
  "sourceToolAssistantUUID": "1fcacb78-9c16-4d25-a5f0-419d7d2ccce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "leafUuid": "0757e91a-4439-43bd-9735-8f907f763549",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper and registry data consistency for R28",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Tool call

_source line 52 · 2026-05-24T03:58:15.526Z_

<details open><summary>🔧 Tool call — Read · `toolu_018k4wjbRQuPQrE3WZ9nLDGL`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/bt4n79nxb.txt",
  "offset": 300,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0757e91a-4439-43bd-9735-8f907f763549",
  "isSidechain": false,
  "requestId": "req_011CbLitTi7DfVmoRGTwJzev",
  "type": "assistant",
  "uuid": "3f6e0a8b-28bc-4c2b-899d-078bd41d4ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrmMFujrxMhDX5ErKk88qE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9980,
      "cache_read_input_tokens": 66414,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 66414,
          "cache_creation_input_tokens": 9980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9980
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-24T03:58:15.530Z_

<details><summary>↩ Tool result · `toolu_018k4wjbRQuPQrE3WZ9nLDGL`</summary>

```text
300	
301	=== kl50_s456_global_eval ===
302	  metrics: {"ppl_wikitext2": 11.8057, "arc_challenge": 0.3319, "winogrande": 0.6488, "mmlu": 0.2794, "gsm8k": 0.0212}
303	
304	=== kl50_s456_train ===
305	  metrics: {"final_loss": 0.397, "final_kl_normalized": 0.397, "final_sparsity": 0.492, "final_lambda": 5000, "final_tau": 0.1, "steps_completed": 1000}
306	
307	=== kl50_s456_uniform_eval ===
308	  metrics: {"wikitext2_ppl": 11.9538, "arc_challenge_acc_norm": 0.3831, "winogrande_acc": 0.6196, "mmlu_acc": 0.275, "gsm8k_exact_match": 0.0288}
309	
310	=== kl50_uniform_hellaswag_piqa ===
311	  metrics: {"hellaswag_acc_norm": 0.5666, "piqa_acc_norm": 0.691}
312	
313	=== kl_30pct_s123 ===
314	  metrics: {"ppl_wikitext2": 8.9748, "arc_challenge_acc_norm": 0.4531, "winogrande_acc": 0.693, "mmlu_acc": 0.3807, "gsm8k_exact_match": 0.0758, "sparsity": 0.3, "allocation": "global"}
315	
316	=== kl_50pct_s123 ===
317	  metrics: {"ppl_wikitext2": 11.745, "arc_challenge_acc_norm": 0.3814, "winogrande_acc": 0.6125, "mmlu_acc": 0.2752, "gsm8k_exact_match": 0.0281, "sparsity": 0.5, "allocation": "global"}
318	
319	=== kl_bce_f1_oracle ===
320	  metrics: {"bce_f1": 0.6128, "bce_precision": 0.6132, "bce_recall": 0.6124, "kl_f1": 0.5397, "kl_precision": 0.5112, "kl_recall": 0.5715, "random_f1": 0.5, "kl_ppl": 11.79, "bce_ppl": 22.51}
321	
322	=== kl_comp_30pct_s123 ===
323	  metrics: {"final_loss": 0.7617, "steps": 1000, "compensation_params": 67248128, "compensation_pct": 0.837, "mean_head_norm_final": 9.2012, "loss_trajectory": [2.0469, 1.3828, 1.0703, 0.9609, 0.8711, 0.7305, 0.6875, 0.7773, 0.7969, 0.7617]}
324	
325	=== kl_comp_30pct_s123_eval ===
326	  metrics: {"wikitext2_ppl": 8.9788, "arc_challenge_acc_norm": 0.3993, "winogrande_acc": 0.6898, "mmlu_acc": 0.2531, "gsm8k_exact_match": 0.0842}
327	
328	=== kl_comp_30pct_s123_ppl ===
329	  metrics: {"wikitext2_ppl": 8.9768, "c4_ppl": 16.0401, "sparsity": 0.3, "allocation": "global_topk", "model": "llama-3.1-8b", "seed": 123}
330	
331	=== kl_comp_30pct_s42 ===
332	  metrics: {"final_loss": 0.6992, "steps": 1000, "compensation_params": 67248128, "compensation_pct": 0.837, "mean_head_norm_final": 9.2012, "loss_trajectory": [2.3594, 1.3516, 1.0859, 0.9219, 0.8789, 0.8281, 0.7461, 0.7344, 0.6953, 0.6992]}
333	
334	=== kl_comp_30pct_s42_eval ===
335	  metrics: {"wikitext2_ppl": 8.9788, "arc_challenge_acc_norm": 0.3993, "winogrande_acc": 0.6898, "mmlu_acc": 0.2531, "gsm8k_exact_match": 0.0842}
336	
337	=== kl_comp_30pct_s42_ppl ===
338	  metrics: {"wikitext2_ppl": 8.9768, "c4_ppl": 16.0401, "sparsity": 0.3, "allocation": "global_topk", "model": "llama-3.1-8b", "seed": 42}
339	
340	=== kl_comp_30pct_s456 ===
341	  metrics: {}
342	
343	=== kl_comp_30pct_s456_eval ===
344	  metrics: {"wikitext2_ppl": 8.9614, "arc_challenge_acc_norm": 0.4462, "winogrande_acc": 0.7143, "mmlu_acc": 0.2714, "gsm8k_exact_match": 0.0887}
345	
346	=== kl_comp_50pct_s42 ===
347	  metrics: {}
348	
349	=== kl_comp_50pct_s42_eval ===
350	  metrics: {"wikitext2_ppl": 11.7933, "arc_challenge_acc_norm": 0.3285, "winogrande_acc": 0.6346, "mmlu_acc": 0.2789, "gsm8k_exact_match": 0.0129}
351	
352	=== kl_only_s0 ===
353	  metrics: {"true_dense_ppl": 6.12, "predictor_hard_mask_ppl": 9.19, "teal_sparse_ppl": 12.03, "model_level_sparsity": 0.499, "ppl_increase_vs_true_dense_pct": 96.57, "eval_seq_len": 2048, "calibration_samples": 32}
354	
355	=== kl_only_s1 ===
356	  metrics: {"true_dense_ppl": 6.12, "predictor_hard_mask_ppl": 9.15, "teal_sparse_ppl": 11.99, "model_level_sparsity": 0.498, "ppl_increase_vs_true_dense_pct": 96}
357	
358	=== kl_sparsity25_s123 ===
359	  metrics: {"final_loss": 0.153, "final_sparsity": 0.23, "steps": 1000}
360	
361	=== kl_sparsity25_s42 ===
362	  metrics: {"train_loss_final": 0.1582, "kl_normalized_final": 0.1582, "sparsity_actual": 0.23, "sparsity_target": 0.25, "lambda_final": 5000, "tau_final": 0.1, "steps": 1000}
363	
364	=== kl_sparsity25_s42_eval_teal ===
365	  metrics: {"wikitext2_ppl": 8.169, "arc_challenge_acc_norm": 0.4539, "winogrande_acc": 0.7056, "mmlu_acc": 0.466, "gsm8k_exact_match": 0.1145, "actual_sparsity": 0.23, "allocation": "global_topk"}
366	
367	=== kl_sparsity25_s42_eval_teal_uniform ===
368	  metrics: {"wikitext2_ppl": 8.2344, "arc_challenge_acc_norm": 0.465, "winogrande_acc": 0.7182, "mmlu_acc": 0.4395, "gsm8k_exact_match": 0.1099, "actual_sparsity": 0.25, "allocation": "uniform"}
369	
370	=== kl_sparsity30_s42_v3 ===
371	  metrics: {"loss": 0.165, "kl_normalized": 0.165, "kl_raw": 0.165, "sparsity": 0.285, "lambda_sparse": 5000, "tau": 0.1, "constraint_loss": 0, "steps": 1000, "true_dense_ppl": 6.12, "predictor_hard_mask_ppl": 7.3, "teal_sparse_ppl": 8.98, "teal_sparse_ppl_note": "已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)", "model_level_sparsity": 0.3, "eval_dataset": "wikitext-2", "eval_seq_len": 2048}
372	
373	=== kl_sparsity35_s42 ===
374	  metrics: {"final_loss": 0.203, "final_sparsity": 0.336, "steps": 1000}
375	
376	=== kl_sparsity35_s42_eval_teal ===
377	  metrics: {"ppl_wikitext2": 9.3133, "arc_challenge_acc": 0.3643, "arc_challenge_acc_norm": 0.3891, "winogrande_acc": 0.6764, "mmlu_acc": 0.4041, "gsm8k_exact_match": 0.0773, "actual_sparsity": 0.336}
378	
379	=== kl_sparsity35_s42_eval_teal_uniform ===
380	  metrics: {"wikitext2_ppl": 9.4416, "arc_challenge_acc_norm": 0.3874, "winogrande_acc": 0.6654, "mmlu_acc": 0.3783, "gsm8k_exact_match": 0.0432, "actual_sparsity": 0.35, "allocation": "uniform"}
381	
382	=== kl_sparsity40_s42_global_eval_v2 ===
383	  metrics: {"wikitext2_ppl": 10.14, "arc_challenge_acc_norm": 0.3951, "winogrande_acc": 0.6748, "mmlu_acc": 0.3947, "gsm8k_exact_match": 0.066, "hellaswag_acc_norm": 0.6779, "piqa_acc_norm": 0.7269}
384	
385	=== kl_sparsity40_s42_retrain_uniform ===
386	  metrics: {"wikitext2_ppl": 10.76, "arc_challenge_acc_norm": 0.3959, "winogrande_acc": 0.6306, "mmlu_acc": 0.355, "gsm8k_acc": 0.0356, "training_final_loss": 0.2598, "training_final_sparsity": 0.387}
387	
388	=== kl_sparsity40_s42_uniform_hspiqa ===
389	  metrics: {"hellaswag_acc_norm": 0.6497, "piqa_acc_norm": 0.7236, "model_level_sparsity": 0.397}
390	
391	=== kl_sparsity45_s42 ===
392	  metrics: {"final_loss": 0.33, "final_sparsity": 0.449, "steps": 1000}
393	
394	=== kl_sparsity45_s42_eval_teal ===
395	  metrics: {"ppl_wikitext2": 10.803, "arc_challenge_acc": 0.3498, "arc_challenge_acc_norm": 0.3916, "winogrande_acc": 0.6464, "mmlu_acc": 0.3037, "gsm8k_exact_match": 0.0296, "actual_sparsity": 0.449}
396	
397	=== kl_sparsity45_s42_eval_teal_uniform ===
398	  metrics: {"wikitext2_ppl": 10.9488, "arc_challenge_acc_norm": 0.3763, "winogrande_acc": 0.6361, "mmlu_acc": 0.3063, "gsm8k_exact_match": 0.0273, "actual_sparsity": 0.45, "allocation": "uniform"}
399	
400	=== latency_benchmark ===
401	  metrics: {"gpu_model": "NVIDIA RTX PRO 6000 Blackwell Server Edition", "dtype": "float16", "attn": "flash_attention_2", "batch": 1, "seq_len": 2048, "warmup": 10, "iters": 100, "dense_ms": 119.11, "dense_std": 0.57, "dense_tokens_per_s": 17194.5, "kl_30pct_ms": 126.64, "kl_30pct_std": 0.7, "kl_30pct_tokens_per_s": 16171.8, "kl_30pct_speedup": 0.941, "kl_50pct_ms": 126.78, "kl_50pct_std": 0.31, "kl_50pct_tokens_per_s": 16154.2, "kl_50pct_speedup": 0.939, "comp_30pct_ms": 129.94, "comp_30pct_std": 0.75, "comp_30pct_tokens_per_s": 15761.4, "comp_30pct_speedup": 0.917, "comp_50pct_ms": 129.71, "comp_50pct_std": 0.53, "comp_50pct_tokens_per_s": 15788.8, "comp_50pct_speedup": 0.918, "predictor_overhead_ms": 3.17, "predictor_overhead_pct": 2.7, "per_layer_predictor_ms": 0.099, "dense_ffn_per_layer_ms": 2.427, "sparse_ffn_pred_per_layer_ms": 2.686, "compensation_overhead_ms": 3.3}
402	
403	=== lm_eval_dense ===
404	  metrics: {"arc_challenge_acc_norm": 0.5819, "winogrande_acc": 0.7814, "mmlu_acc": 0.6532, "gsm8k_exact_match": 0.5004, "eval_tasks": ["arc_challenge", "winogrande", "mmlu", "gsm8k"], "model": "llama-3.1-8b", "condition": "dense", "server": "westd-34887"}
405	
406	=== lm_eval_mistral_dense ===
407	  metrics: {"arc_challenge_acc_norm": 0.6024, "winogrande_acc": 0.7869, "mmlu_acc": 0.6244, "gsm8k_exact_match": 0.3654, "model": "Mistral-7B-v0.3", "condition": "dense", "server": "westd-34887"}
408	
409	=== lm_eval_teal_50pct ===
410	  metrics: {"method": "vanilla_teal", "sparsity": 0.5, "actual_sparsity": 0.5, "arc_challenge_acc_norm": 0.291, "winogrande_acc": 0.5556, "mmlu_acc": 0.2856, "gsm8k_exact_match_flexible": 0.019, "gsm8k_exact_match_strict": 0.0114, "arc_challenge_drop_vs_dense": -0.5, "winogrande_drop_vs_dense": -0.289, "mmlu_drop_vs_dense": -0.563, "gsm8k_drop_vs_dense": -0.962, "model": "Llama-3.1-8B", "condition": "TEAL 50% training-free sparsity"}
411	
412	=== longbench_dense_v6 ===
413	  metrics: {"longbench_narrativeqa": 7.3, "longbench_qasper": 13.4, "longbench_gov_report": 30.5, "longbench_multi_news": 2.5}
414	
415	=== mistral_dense_hellaswag_piqa ===
416	  metrics: {"hellaswag_acc_norm": 0.832, "piqa_acc_norm": 0.8188}
417	
418	=== mistral_dense_ppl ===
419	  metrics: {"wikitext2_ppl": 5.5238, "model": "Mistral-7B-v0.3", "condition": "dense", "sparsity": 0}
420	
421	=== mistral_kl30_downstream ===
422	  metrics: {"arc_challenge_acc_norm": 0.5017, "winogrande_acc": 0.6914, "mmlu_acc": 0.4404, "gsm8k_exact_match": 0.1114}
423	
424	=== mistral_kl30_hellaswag_piqa ===
425	  metrics: {"hellaswag_acc_norm": 0.6892, "piqa_acc_norm": 0.7519}
426	
427	=== mistral_kl30_pertoken ===
428	  metrics: {"wikitext2_ppl": 6.048, "model": "Mistral-7B-v0.3", "condition": "kl_pertoken_30pct", "sparsity": 0.3, "allocation": "uniform", "ppl_increase_vs_dense": 0.5242}
429	
430	=== mistral_kl30_s123 ===
431	  metrics: {"training_final_loss": 0.0996, "training_final_sparsity": 0.281, "wikitext2_ppl": 7.1491, "arc_challenge_acc_norm": 0.378, "winogrande_acc": 0.7017, "mmlu_acc": 0.4423, "gsm8k_exact_match": 0.0773, "hellaswag_acc_norm": 0.6961, "piqa_acc_norm": 0.7459}
432	
433	=== mistral_kl30_s42 ===
434	  metrics: {"kl_per_token_ppl": 6.048, "kl_teal_global_ppl": 6.7733, "teal_baseline_ppl": 8.3807, "dense_ppl": 5.5238, "kl_advantage_ratio": 1.386, "ppl_vs_dense_pct": 9.5}
435	
436	=== mistral_kl30_s456 ===
437	  metrics: {"training_final_loss": 0.105, "training_final_sparsity": 0.281, "wikitext2_ppl": 6.8752, "arc_challenge_acc_norm": 0.4684, "winogrande_acc": 0.7143, "mmlu_acc": 0.4161, "gsm8k_exact_match": 0.0697, "hellaswag_acc_norm": 0.705, "piqa_acc_norm": 0.7448}
438	
439	=== mistral_kl30_teal_global ===
440	  metrics: {"wikitext2_ppl": 6.7733, "model": "Mistral-7B-v0.3", "condition": "kl_teal_global_30pct", "sparsity": 0.3, "allocation": "uniform", "ppl_increase_vs_dense": 1.2495}
441	
442	=== mistral_kl50_pertoken ===
443	  metrics: {"wikitext2_ppl": 7.2931, "model": "Mistral-7B-v0.3", "condition": "kl_pertoken_50pct", "sparsity": 0.5, "allocation": "uniform", "ppl_increase_vs_dense": 1.7693}
444	
445	=== mistral_kl50_teal_global ===
446	  metrics: {"wikitext2_ppl": 8.6489, "model": "Mistral-7B-v0.3", "condition": "kl_teal_global_50pct", "sparsity": 0.5, "allocation": "uniform", "ppl_increase_vs_dense": 3.1251}
447	
448	=== mistral_kl70_pertoken ===
449	  metrics: {"wikitext2_ppl": 9.1086, "model": "Mistral-7B-v0.3", "condition": "kl_pertoken_70pct", "sparsity": 0.7, "allocation": "uniform", "ppl_increase_vs_dense": 3.5848}
450	
451	=== mistral_kl70_s42 ===
452	  metrics: {"kl_per_token_ppl": 9.1086, "kl_teal_global_ppl": 13.3254, "teal_baseline_ppl": 61.716, "dense_ppl": 5.5238, "kl_advantage_ratio": 6.77, "final_loss": 0.3945, "actual_sparsity": 0.682}
453	
454	=== mistral_kl70_teal_global ===
455	  metrics: {"wikitext2_ppl": 13.3254, "model": "Mistral-7B-v0.3", "condition": "kl_teal_global_70pct", "sparsity": 0.7, "allocation": "uniform", "ppl_increase_vs_dense": 7.8016}
456	
457	=== mistral_kl_s42 ===
458	  metrics: {"train_final_loss": 0.2188, "train_final_kl_raw": 0.2188, "train_final_kl_norm": 0.2188, "train_final_constraint": 0, "train_final_sparsity": 0.48, "train_final_lambda": 1000, "train_final_tau": 0.1, "train_steps_completed": 1000, "true_dense_ppl": 5.52, "predictor_hard_mask_ppl": 7.3, "teal_sparse_ppl": 8.98, "model_level_sparsity": 0.5, "eval_dataset": "wikitext-2", "eval_seq_len": 2048, "calibration_samples": 32, "eval_samples": 159}
459	
460	=== mistral_teal30_baseline ===
461	  metrics: {"wikitext2_ppl": 8.3807, "model": "Mistral-7B-v0.3", "condition": "teal_vanilla_30pct", "sparsity": 0.3, "allocation": "uniform", "ppl_increase_vs_dense": 2.8569}
462	
463	=== mistral_teal30_downstream ===
464	  metrics: {"wikitext2_ppl": 8.3807, "arc_challenge_acc_norm": 0.4113, "winogrande_acc": 0.6354, "mmlu_acc": 0.4348, "gsm8k_exact_match": 0.1592, "hellaswag_acc_norm": 0.6011, "piqa_acc_norm": 0.7214}
465	
466	=== mistral_teal50_baseline ===
467	  metrics: {"teal_baseline_ppl": 18.3061, "dense_ppl": 5.5238, "teal_vs_dense_ratio": 3.31}
468	
469	=== mistral_teal50_downstream ===
470	  metrics: {"wikitext2_ppl": 18.3061, "arc_challenge_acc_norm": 0.2457, "winogrande_acc": 0.5091, "mmlu_acc": 0.2635, "gsm8k_exact_match": 0.0341, "hellaswag_acc_norm": 0.3603, "piqa_acc_norm": 0.6045}
471	
472	=== mistral_teal70_baseline ===
473	  metrics: {"wikitext2_ppl": 61.716, "model": "Mistral-7B-v0.3", "condition": "teal_vanilla_70pct", "sparsity": 0.7, "allocation": "uniform", "ppl_increase_vs_dense": 56.1922}
474	
475	=== mse30_s123 ===
476	  metrics: {"ppl": 17.7313, "sparsity": 0.273, "allocation": "uniform"}
477	
478	=== mse30_s123_downstream ===
479	  metrics: {"arc_challenge_acc": 0.3285, "arc_challenge_acc_norm": 0.3737, "winogrande_acc": 0.5699, "mmlu_acc": 0.2781, "gsm8k_exact_match": 0.0174, "hellaswag_acc": 0.4009, "hellaswag_acc_norm": 0.5358, "piqa_acc": 0.7106, "piqa_acc_norm": 0.7067, "boolq_acc": 0.6324}
480	
481	=== mse30_s42_boolq ===
482	  metrics: {"boolq_acc": 0.5997, "boolq_acc_stderr": 0.008569, "boolq_sample_len": 3270}
483	
484	=== mse30_s42_eval_7task ===
485	  metrics: {"wikitext2_ppl": 20.43, "arc_challenge_acc_norm": 0.3123, "winogrande_acc": 0.6038, "mmlu_acc": 0.3179, "gsm8k_exact_match": 0.0197, "hellaswag_acc_norm": 0.5248, "piqa_acc_norm": 0.6937}
486	
487	=== mse30_s42_train ===
488	  metrics: {"final_mse_loss": 0.005735, "final_constraint_loss": 0.007294, "final_total_loss": 0.013, "final_sparsity": 0.277, "final_tau": 0.1, "final_lambda": 1000, "steps": 1000}
489	
490	=== mse30_s456 ===
491	  metrics: {"ppl": 17.3888, "sparsity": 0.28, "allocation": "uniform"}
492	
493	=== mse30_s456_downstream ===
494	  metrics: {"arc_challenge_acc_norm": 0.3882, "winogrande_acc": 0.6196, "mmlu_acc": 0.3264, "gsm8k_exact_match": 0.0311, "hellaswag_acc_norm": 0.6129, "piqa_acc_norm": 0.7383, "boolq_acc": 0.7034}
495	
496	=== mse50_s42_eval_7task ===
497	  metrics: {"wikitext2_ppl": 229.26, "arc_challenge_acc_norm": 0.25, "winogrande_acc": 0.5059, "mmlu_acc": 0.2379, "gsm8k_exact_match": 0.0159, "hellaswag_acc_norm": 0.2722, "piqa_acc_norm": 0.5577}
498	
499	=== mse50_s42_train ===
500	  metrics: {"final_loss": 0.0083, "final_sparsity": 0.539, "steps": 1000}
501	
502	=== mvp_bce_s123 ===
503	  metrics: {"true_dense_ppl": 6.1173, "predictor_hard_mask_ppl": 28.3817, "teal_sparse_ppl": 44.5864, "model_level_sparsity": 0.4957, "ppl_increase_vs_true_dense_pct": 629, "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a", "calibration_samples": 32, "vanilla_teal_sparse_ppl_INVALID": 66036.4062}
504	
505	=== mvp_bce_s42 ===
506	  metrics: {"true_dense_ppl": 6.1173, "predictor_hard_mask_ppl": 27.9603, "teal_sparse_ppl": 44.537, "model_level_sparsity": 0.4957, "ppl_increase_vs_true_dense_pct": 628, "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a", "calibration_samples": 32, "vanilla_teal_sparse_ppl_INVALID": 66036.4062}
507	
508	=== mvp_bce_s456 ===
509	  metrics: {"true_dense_ppl": 6.1173, "predictor_hard_mask_ppl": 28.1437, "teal_sparse_ppl": 43.033, "model_level_sparsity": 0.4957, "ppl_increase_vs_true_dense_pct": 603.3, "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a", "calibration_samples": 32, "vanilla_teal_sparse_ppl_INVALID": 66036.4062}
510	
511	=== mvp_kl_norm_v2_s123 ===
512	  metrics: {"true_dense_ppl": 6.1173, "predictor_hard_mask_ppl": 9.2474, "teal_sparse_ppl": 11.9128, "model_level_sparsity": 0.4979, "ppl_increase_vs_true_dense_pct": 94.7, "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a", "calibration_samples": 32, "vanilla_teal_sparse_ppl_INVALID": 66036.4062}
513	
514	=== mvp_kl_norm_v2_s42 ===
515	  metrics: {"true_dense_ppl": 6.1173, "predictor_hard_mask_ppl": 9.2142, "teal_sparse_ppl": 12.0776, "model_level_sparsity": 0.4979, "ppl_increase_vs_true_dense_pct": 97.4, "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a", "calibration_samples": 32, "vanilla_teal_sparse_ppl_INVALID": 66036.4062}
516	
517	=== mvp_kl_norm_v2_s456 ===
518	  metrics: {"true_dense_ppl": 6.1173, "predictor_hard_mask_ppl": 9.14, "teal_sparse_ppl": 13.58, "model_level_sparsity": 0.498, "ppl_increase_vs_true_dense_pct": 121.9, "eval_md5": "f4086818bb55dc354ea4c6fe8ed8899a", "calibration_samples": 32, "vanilla_teal_sparse_ppl_INVALID": 66036.4062}
519	
520	=== natural_sparsity_floor_30pct ===
521	  metrics: {"always_pruned_ratio": 0.0006, "always_pruned_count": 278, "total_neurons": 458752, "late_layer_max_ratio": 0.0051, "threshold": 0.1}
522	
523	=== perlayer_kl_30_s123_v4 ===
524	  metrics: {"final_avg_kl": 0.0114, "final_tau": 0.1, "steps": 10000}
525	
526	=== perlayer_kl_30_s42_v6 ===
527	  metrics: {"steps": 10000}
528	
529	=== perlayer_kl_30_s456_downstream ===
530	  metrics: {"arc_challenge_acc_norm": 0.3848, "winogrande_acc": 0.663, "mmlu_acc": 0.3904, "gsm8k_exact_match": 0.0644, "hellaswag_acc_norm": 0.6616, "piqa_acc_norm": 0.7356}
531	
532	=== perlayer_kl_30_s456_ppl ===
533	  metrics: {"wikitext2_ppl": 9.0282, "model_level_sparsity": 0.297}
534	
535	=== perlayer_kl_k16_eval_final2 ===
536	  metrics: {"wikitext2_ppl": 8.6737, "arc_challenge_acc_norm": 0.4104, "winogrande_acc": 0.6843, "mmlu_acc": 0.4403, "gsm8k_exact_match": 0.0811, "hellaswag_acc_norm": 0.6963, "piqa_acc_norm": 0.759}
537	
538	=== perlayer_kl_k16_s123 ===
539	  metrics: {"avg_kl": 0.1617, "avg_sparsity": 0.287, "final_kl": 0.1436, "wall_time_s": 1982.8}
540	
541	=== perlayer_kl_k16_s123_eval ===
542	  metrics: {"wikitext2_ppl": 8.6939, "arc_challenge_acc_norm": 0.4317, "winogrande_acc": 0.6772, "mmlu_acc": 0.3996, "gsm8k_exact_match": 0.0986, "hellaswag_acc_norm": 0.705, "piqa_acc_norm": 0.7481}
543	
544	=== perlayer_kl_k16_s42_v3 ===
545	  metrics: {"final_kl": 0.1406, "final_avg_kl": 0.1582, "final_avg_sparsity": 0.286, "wall_time_s": 1982.9}
546	
547	=== perlayer_kl_k16_s456_eval ===
548	  metrics: {"ppl_wikitext2": 8.655, "arc_challenge_acc_norm": 0.4155, "winogrande_acc": 0.6946, "mmlu_acc": 0.3873, "gsm8k_exact_match": 0.0766, "hellaswag_acc_norm": 0.7015, "piqa_acc_norm": 0.7437}
549	
550	=== perlayer_kl_k16_s456_v2 ===
551	  metrics: {"avg_kl": 0.1565, "avg_sparsity": 0.287, "final_kl": 0.1611, "wall_time_s": 1977.9}
552	
553	=== perlayer_kl_k2_s123 ===
554	  metrics: {}
555	
556	=== perlayer_kl_k2_s123_eval ===
557	  metrics: {"wikitext2_ppl": 10.8835, "arc_challenge_acc_norm": 0.4078, "winogrande_acc": 0.614, "mmlu_acc": 0.3789, "gsm8k_exact_match": 0.0326, "hellaswag_acc_norm": 0.6605, "piqa_acc_norm": 0.741}
558	
559	=== perlayer_kl_k2_s42 ===
560	  metrics: {"final_avg_kl": 0.0358, "final_avg_sparsity": 0.268, "wall_time_s": 3841.2, "training_steps": 1000, "note": "training only, PPL eval not yet run"}
561	
562	=== perlayer_kl_k2_s42_eval ===
563	  metrics: {"wikitext2_ppl": 10.7958, "arc_challenge_acc_norm": 0.3985, "winogrande_acc": 0.6322, "mmlu_acc": 0.4172, "gsm8k_exact_match": 0.0296, "hellaswag_acc_norm": 0.6773, "piqa_acc_norm": 0.7356}
564	
565	=== perlayer_kl_k2_s42_train ===
566	  metrics: {"wikitext2_ppl": 10.7958, "wikitext2_ppl_pertoken": 11.0812, "final_avg_kl": 0.0358, "final_avg_sparsity": 0.268, "wall_time_s": 3843, "eval_mode": "teal_global_uniform_30pct"}
567	
568	=== perlayer_kl_k2_s456 ===
569	  metrics: {}
570	
571	=== perlayer_kl_k2_s456_eval ===
572	  metrics: {"wikitext2_ppl": 10.5826, "arc_challenge_acc_norm": 0.384, "winogrande_acc": 0.6488, "mmlu_acc": 0.3542, "gsm8k_exact_match": 0.0205, "hellaswag_acc_norm": 0.659, "piqa_acc_norm": 0.728}
573	
574	=== perlayer_kl_k4_50_s42 ===
575	  metrics: {}
576	
577	=== perlayer_kl_k4_s42_downstream ===
578	  metrics: {"arc_challenge_acc_norm": 0.4096, "winogrande_acc": 0.6669, "mmlu_acc": 0.4353, "gsm8k_exact_match": 0.0516, "hellaswag_acc_norm": 0.6849, "piqa_acc_norm": 0.7399, "boolq_acc": 0.7318}
579	
580	=== perlayer_kl_k8_s123 ===
581	  metrics: {"avg_kl": 0.0997, "avg_sparsity": 0.286, "final_kl": 0.0825, "avg_lambda": 2182.2, "steps": 1000}
582	
583	=== perlayer_kl_k8_s123_eval ===
584	  metrics: {"wikitext2_ppl": 9.0648, "arc_challenge_acc_norm": 0.4155, "winogrande_acc": 0.6993, "mmlu_acc": 0.4042, "gsm8k_exact_match": 0.0682, "hellaswag_acc_norm": 0.6997, "piqa_acc_norm": 0.7508}
585	
586	=== perlayer_kl_k8_s42 ===
587	  metrics: {"wikitext2_ppl": 8.97, "final_avg_kl": 0.0983, "final_avg_sparsity": 0.281, "wall_time_s": 1894.1}
588	
589	=== perlayer_kl_k8_s42_eval ===
590	  metrics: {"wikitext2_ppl": 8.9704, "arc_challenge_acc_norm": 0.4104, "winogrande_acc": 0.674, "mmlu_acc": 0.398, "gsm8k_exact_match": 0.0561, "hellaswag_acc_norm": 0.6919, "piqa_acc_norm": 0.7612}
591	
592	=== perlayer_kl_k8_s456 ===
593	  metrics: {"avg_kl": 0.0982, "avg_sparsity": 0.285, "final_kl": 0.1079, "avg_lambda": 2244.28, "steps": 1000}
594	
595	=== perlayer_kl_k8_s456_eval ===
596	  metrics: {"wikitext2_ppl": 8.9515, "arc_challenge_acc_norm": 0.3951, "winogrande_acc": 0.6875, "mmlu_acc": 0.4105, "gsm8k_exact_match": 0.0811, "hellaswag_acc_norm": 0.6783, "piqa_acc_norm": 0.7399, "sparsity": 0.298}
597	
598	=== perlayer_kl_s123_boolq ===
599	  metrics: {"boolq_acc": 0.7046}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f6e0a8b-28bc-4c2b-899d-078bd41d4ad9",
  "isSidechain": false,
  "promptId": "fdfb0d6d-9233-4c2a-afaa-5df266af136f",
  "type": "user",
  "uuid": "048732af-9360-4581-b1b4-cfe678a6d893",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6/tool-results/bt4n79nxb.txt",
      "content": "\n=== kl50_s456_global_eval ===\n  metrics: {\"ppl_wikitext2\": 11.8057, \"arc_challenge\": 0.3319, \"winogrande\": 0.6488, \"mmlu\": 0.2794, \"gsm8k\": 0.0212}\n\n=== kl50_s456_train ===\n  metrics: {\"final_loss\": 0.397, \"final_kl_normalized\": 0.397, \"final_sparsity\": 0.492, \"final_lambda\": 5000, \"final_tau\": 0.1, \"steps_completed\": 1000}\n\n=== kl50_s456_uniform_eval ===\n  metrics: {\"wikitext2_ppl\": 11.9538, \"arc_challenge_acc_norm\": 0.3831, \"winogrande_acc\": 0.6196, \"mmlu_acc\": 0.275, \"gsm8k_exact_match\": 0.0288}\n\n=== kl50_uniform_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.5666, \"piqa_acc_norm\": 0.691}\n\n=== kl_30pct_s123 ===\n  metrics: {\"ppl_wikitext2\": 8.9748, \"arc_challenge_acc_norm\": 0.4531, \"winogrande_acc\": 0.693, \"mmlu_acc\": 0.3807, \"gsm8k_exact_match\": 0.0758, \"sparsity\": 0.3, \"allocation\": \"global\"}\n\n=== kl_50pct_s123 ===\n  metrics: {\"ppl_wikitext2\": 11.745, \"arc_challenge_acc_norm\": 0.3814, \"winogrande_acc\": 0.6125, \"mmlu_acc\": 0.2752, \"gsm8k_exact_match\": 0.0281, \"sparsity\": 0.5, \"allocation\": \"global\"}\n\n=== kl_bce_f1_oracle ===\n  metrics: {\"bce_f1\": 0.6128, \"bce_precision\": 0.6132, \"bce_recall\": 0.6124, \"kl_f1\": 0.5397, \"kl_precision\": 0.5112, \"kl_recall\": 0.5715, \"random_f1\": 0.5, \"kl_ppl\": 11.79, \"bce_ppl\": 22.51}\n\n=== kl_comp_30pct_s123 ===\n  metrics: {\"final_loss\": 0.7617, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.0469, 1.3828, 1.0703, 0.9609, 0.8711, 0.7305, 0.6875, 0.7773, 0.7969, 0.7617]}\n\n=== kl_comp_30pct_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}\n\n=== kl_comp_30pct_s123_ppl ===\n  metrics: {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 123}\n\n=== kl_comp_30pct_s42 ===\n  metrics: {\"final_loss\": 0.6992, \"steps\": 1000, \"compensation_params\": 67248128, \"compensation_pct\": 0.837, \"mean_head_norm_final\": 9.2012, \"loss_trajectory\": [2.3594, 1.3516, 1.0859, 0.9219, 0.8789, 0.8281, 0.7461, 0.7344, 0.6953, 0.6992]}\n\n=== kl_comp_30pct_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9788, \"arc_challenge_acc_norm\": 0.3993, \"winogrande_acc\": 0.6898, \"mmlu_acc\": 0.2531, \"gsm8k_exact_match\": 0.0842}\n\n=== kl_comp_30pct_s42_ppl ===\n  metrics: {\"wikitext2_ppl\": 8.9768, \"c4_ppl\": 16.0401, \"sparsity\": 0.3, \"allocation\": \"global_topk\", \"model\": \"llama-3.1-8b\", \"seed\": 42}\n\n=== kl_comp_30pct_s456 ===\n  metrics: {}\n\n=== kl_comp_30pct_s456_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9614, \"arc_challenge_acc_norm\": 0.4462, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.2714, \"gsm8k_exact_match\": 0.0887}\n\n=== kl_comp_50pct_s42 ===\n  metrics: {}\n\n=== kl_comp_50pct_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 11.7933, \"arc_challenge_acc_norm\": 0.3285, \"winogrande_acc\": 0.6346, \"mmlu_acc\": 0.2789, \"gsm8k_exact_match\": 0.0129}\n\n=== kl_only_s0 ===\n  metrics: {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.19, \"teal_sparse_ppl\": 12.03, \"model_level_sparsity\": 0.499, \"ppl_increase_vs_true_dense_pct\": 96.57, \"eval_seq_len\": 2048, \"calibration_samples\": 32}\n\n=== kl_only_s1 ===\n  metrics: {\"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 9.15, \"teal_sparse_ppl\": 11.99, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 96}\n\n=== kl_sparsity25_s123 ===\n  metrics: {\"final_loss\": 0.153, \"final_sparsity\": 0.23, \"steps\": 1000}\n\n=== kl_sparsity25_s42 ===\n  metrics: {\"train_loss_final\": 0.1582, \"kl_normalized_final\": 0.1582, \"sparsity_actual\": 0.23, \"sparsity_target\": 0.25, \"lambda_final\": 5000, \"tau_final\": 0.1, \"steps\": 1000}\n\n=== kl_sparsity25_s42_eval_teal ===\n  metrics: {\"wikitext2_ppl\": 8.169, \"arc_challenge_acc_norm\": 0.4539, \"winogrande_acc\": 0.7056, \"mmlu_acc\": 0.466, \"gsm8k_exact_match\": 0.1145, \"actual_sparsity\": 0.23, \"allocation\": \"global_topk\"}\n\n=== kl_sparsity25_s42_eval_teal_uniform ===\n  metrics: {\"wikitext2_ppl\": 8.2344, \"arc_challenge_acc_norm\": 0.465, \"winogrande_acc\": 0.7182, \"mmlu_acc\": 0.4395, \"gsm8k_exact_match\": 0.1099, \"actual_sparsity\": 0.25, \"allocation\": \"uniform\"}\n\n=== kl_sparsity30_s42_v3 ===\n  metrics: {\"loss\": 0.165, \"kl_normalized\": 0.165, \"kl_raw\": 0.165, \"sparsity\": 0.285, \"lambda_sparse\": 5000, \"tau\": 0.1, \"constraint_loss\": 0, \"steps\": 1000, \"true_dense_ppl\": 6.12, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"teal_sparse_ppl_note\": \"已通过 eval_kl30_teal_30pct 独立验证 (sparsity_target=0.3, D034)\", \"model_level_sparsity\": 0.3, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048}\n\n=== kl_sparsity35_s42 ===\n  metrics: {\"final_loss\": 0.203, \"final_sparsity\": 0.336, \"steps\": 1000}\n\n=== kl_sparsity35_s42_eval_teal ===\n  metrics: {\"ppl_wikitext2\": 9.3133, \"arc_challenge_acc\": 0.3643, \"arc_challenge_acc_norm\": 0.3891, \"winogrande_acc\": 0.6764, \"mmlu_acc\": 0.4041, \"gsm8k_exact_match\": 0.0773, \"actual_sparsity\": 0.336}\n\n=== kl_sparsity35_s42_eval_teal_uniform ===\n  metrics: {\"wikitext2_ppl\": 9.4416, \"arc_challenge_acc_norm\": 0.3874, \"winogrande_acc\": 0.6654, \"mmlu_acc\": 0.3783, \"gsm8k_exact_match\": 0.0432, \"actual_sparsity\": 0.35, \"allocation\": \"uniform\"}\n\n=== kl_sparsity40_s42_global_eval_v2 ===\n  metrics: {\"wikitext2_ppl\": 10.14, \"arc_challenge_acc_norm\": 0.3951, \"winogrande_acc\": 0.6748, \"mmlu_acc\": 0.3947, \"gsm8k_exact_match\": 0.066, \"hellaswag_acc_norm\": 0.6779, \"piqa_acc_norm\": 0.7269}\n\n=== kl_sparsity40_s42_retrain_uniform ===\n  metrics: {\"wikitext2_ppl\": 10.76, \"arc_challenge_acc_norm\": 0.3959, \"winogrande_acc\": 0.6306, \"mmlu_acc\": 0.355, \"gsm8k_acc\": 0.0356, \"training_final_loss\": 0.2598, \"training_final_sparsity\": 0.387}\n\n=== kl_sparsity40_s42_uniform_hspiqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.6497, \"piqa_acc_norm\": 0.7236, \"model_level_sparsity\": 0.397}\n\n=== kl_sparsity45_s42 ===\n  metrics: {\"final_loss\": 0.33, \"final_sparsity\": 0.449, \"steps\": 1000}\n\n=== kl_sparsity45_s42_eval_teal ===\n  metrics: {\"ppl_wikitext2\": 10.803, \"arc_challenge_acc\": 0.3498, \"arc_challenge_acc_norm\": 0.3916, \"winogrande_acc\": 0.6464, \"mmlu_acc\": 0.3037, \"gsm8k_exact_match\": 0.0296, \"actual_sparsity\": 0.449}\n\n=== kl_sparsity45_s42_eval_teal_uniform ===\n  metrics: {\"wikitext2_ppl\": 10.9488, \"arc_challenge_acc_norm\": 0.3763, \"winogrande_acc\": 0.6361, \"mmlu_acc\": 0.3063, \"gsm8k_exact_match\": 0.0273, \"actual_sparsity\": 0.45, \"allocation\": \"uniform\"}\n\n=== latency_benchmark ===\n  metrics: {\"gpu_model\": \"NVIDIA RTX PRO 6000 Blackwell Server Edition\", \"dtype\": \"float16\", \"attn\": \"flash_attention_2\", \"batch\": 1, \"seq_len\": 2048, \"warmup\": 10, \"iters\": 100, \"dense_ms\": 119.11, \"dense_std\": 0.57, \"dense_tokens_per_s\": 17194.5, \"kl_30pct_ms\": 126.64, \"kl_30pct_std\": 0.7, \"kl_30pct_tokens_per_s\": 16171.8, \"kl_30pct_speedup\": 0.941, \"kl_50pct_ms\": 126.78, \"kl_50pct_std\": 0.31, \"kl_50pct_tokens_per_s\": 16154.2, \"kl_50pct_speedup\": 0.939, \"comp_30pct_ms\": 129.94, \"comp_30pct_std\": 0.75, \"comp_30pct_tokens_per_s\": 15761.4, \"comp_30pct_speedup\": 0.917, \"comp_50pct_ms\": 129.71, \"comp_50pct_std\": 0.53, \"comp_50pct_tokens_per_s\": 15788.8, \"comp_50pct_speedup\": 0.918, \"predictor_overhead_ms\": 3.17, \"predictor_overhead_pct\": 2.7, \"per_layer_predictor_ms\": 0.099, \"dense_ffn_per_layer_ms\": 2.427, \"sparse_ffn_pred_per_layer_ms\": 2.686, \"compensation_overhead_ms\": 3.3}\n\n=== lm_eval_dense ===\n  metrics: {\"arc_challenge_acc_norm\": 0.5819, \"winogrande_acc\": 0.7814, \"mmlu_acc\": 0.6532, \"gsm8k_exact_match\": 0.5004, \"eval_tasks\": [\"arc_challenge\", \"winogrande\", \"mmlu\", \"gsm8k\"], \"model\": \"llama-3.1-8b\", \"condition\": \"dense\", \"server\": \"westd-34887\"}\n\n=== lm_eval_mistral_dense ===\n  metrics: {\"arc_challenge_acc_norm\": 0.6024, \"winogrande_acc\": 0.7869, \"mmlu_acc\": 0.6244, \"gsm8k_exact_match\": 0.3654, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"server\": \"westd-34887\"}\n\n=== lm_eval_teal_50pct ===\n  metrics: {\"method\": \"vanilla_teal\", \"sparsity\": 0.5, \"actual_sparsity\": 0.5, \"arc_challenge_acc_norm\": 0.291, \"winogrande_acc\": 0.5556, \"mmlu_acc\": 0.2856, \"gsm8k_exact_match_flexible\": 0.019, \"gsm8k_exact_match_strict\": 0.0114, \"arc_challenge_drop_vs_dense\": -0.5, \"winogrande_drop_vs_dense\": -0.289, \"mmlu_drop_vs_dense\": -0.563, \"gsm8k_drop_vs_dense\": -0.962, \"model\": \"Llama-3.1-8B\", \"condition\": \"TEAL 50% training-free sparsity\"}\n\n=== longbench_dense_v6 ===\n  metrics: {\"longbench_narrativeqa\": 7.3, \"longbench_qasper\": 13.4, \"longbench_gov_report\": 30.5, \"longbench_multi_news\": 2.5}\n\n=== mistral_dense_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.832, \"piqa_acc_norm\": 0.8188}\n\n=== mistral_dense_ppl ===\n  metrics: {\"wikitext2_ppl\": 5.5238, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"dense\", \"sparsity\": 0}\n\n=== mistral_kl30_downstream ===\n  metrics: {\"arc_challenge_acc_norm\": 0.5017, \"winogrande_acc\": 0.6914, \"mmlu_acc\": 0.4404, \"gsm8k_exact_match\": 0.1114}\n\n=== mistral_kl30_hellaswag_piqa ===\n  metrics: {\"hellaswag_acc_norm\": 0.6892, \"piqa_acc_norm\": 0.7519}\n\n=== mistral_kl30_pertoken ===\n  metrics: {\"wikitext2_ppl\": 6.048, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 0.5242}\n\n=== mistral_kl30_s123 ===\n  metrics: {\"training_final_loss\": 0.0996, \"training_final_sparsity\": 0.281, \"wikitext2_ppl\": 7.1491, \"arc_challenge_acc_norm\": 0.378, \"winogrande_acc\": 0.7017, \"mmlu_acc\": 0.4423, \"gsm8k_exact_match\": 0.0773, \"hellaswag_acc_norm\": 0.6961, \"piqa_acc_norm\": 0.7459}\n\n=== mistral_kl30_s42 ===\n  metrics: {\"kl_per_token_ppl\": 6.048, \"kl_teal_global_ppl\": 6.7733, \"teal_baseline_ppl\": 8.3807, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 1.386, \"ppl_vs_dense_pct\": 9.5}\n\n=== mistral_kl30_s456 ===\n  metrics: {\"training_final_loss\": 0.105, \"training_final_sparsity\": 0.281, \"wikitext2_ppl\": 6.8752, \"arc_challenge_acc_norm\": 0.4684, \"winogrande_acc\": 0.7143, \"mmlu_acc\": 0.4161, \"gsm8k_exact_match\": 0.0697, \"hellaswag_acc_norm\": 0.705, \"piqa_acc_norm\": 0.7448}\n\n=== mistral_kl30_teal_global ===\n  metrics: {\"wikitext2_ppl\": 6.7733, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.2495}\n\n=== mistral_kl50_pertoken ===\n  metrics: {\"wikitext2_ppl\": 7.2931, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 1.7693}\n\n=== mistral_kl50_teal_global ===\n  metrics: {\"wikitext2_ppl\": 8.6489, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_50pct\", \"sparsity\": 0.5, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.1251}\n\n=== mistral_kl70_pertoken ===\n  metrics: {\"wikitext2_ppl\": 9.1086, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_pertoken_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 3.5848}\n\n=== mistral_kl70_s42 ===\n  metrics: {\"kl_per_token_ppl\": 9.1086, \"kl_teal_global_ppl\": 13.3254, \"teal_baseline_ppl\": 61.716, \"dense_ppl\": 5.5238, \"kl_advantage_ratio\": 6.77, \"final_loss\": 0.3945, \"actual_sparsity\": 0.682}\n\n=== mistral_kl70_teal_global ===\n  metrics: {\"wikitext2_ppl\": 13.3254, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"kl_teal_global_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 7.8016}\n\n=== mistral_kl_s42 ===\n  metrics: {\"train_final_loss\": 0.2188, \"train_final_kl_raw\": 0.2188, \"train_final_kl_norm\": 0.2188, \"train_final_constraint\": 0, \"train_final_sparsity\": 0.48, \"train_final_lambda\": 1000, \"train_final_tau\": 0.1, \"train_steps_completed\": 1000, \"true_dense_ppl\": 5.52, \"predictor_hard_mask_ppl\": 7.3, \"teal_sparse_ppl\": 8.98, \"model_level_sparsity\": 0.5, \"eval_dataset\": \"wikitext-2\", \"eval_seq_len\": 2048, \"calibration_samples\": 32, \"eval_samples\": 159}\n\n=== mistral_teal30_baseline ===\n  metrics: {\"wikitext2_ppl\": 8.3807, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_30pct\", \"sparsity\": 0.3, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 2.8569}\n\n=== mistral_teal30_downstream ===\n  metrics: {\"wikitext2_ppl\": 8.3807, \"arc_challenge_acc_norm\": 0.4113, \"winogrande_acc\": 0.6354, \"mmlu_acc\": 0.4348, \"gsm8k_exact_match\": 0.1592, \"hellaswag_acc_norm\": 0.6011, \"piqa_acc_norm\": 0.7214}\n\n=== mistral_teal50_baseline ===\n  metrics: {\"teal_baseline_ppl\": 18.3061, \"dense_ppl\": 5.5238, \"teal_vs_dense_ratio\": 3.31}\n\n=== mistral_teal50_downstream ===\n  metrics: {\"wikitext2_ppl\": 18.3061, \"arc_challenge_acc_norm\": 0.2457, \"winogrande_acc\": 0.5091, \"mmlu_acc\": 0.2635, \"gsm8k_exact_match\": 0.0341, \"hellaswag_acc_norm\": 0.3603, \"piqa_acc_norm\": 0.6045}\n\n=== mistral_teal70_baseline ===\n  metrics: {\"wikitext2_ppl\": 61.716, \"model\": \"Mistral-7B-v0.3\", \"condition\": \"teal_vanilla_70pct\", \"sparsity\": 0.7, \"allocation\": \"uniform\", \"ppl_increase_vs_dense\": 56.1922}\n\n=== mse30_s123 ===\n  metrics: {\"ppl\": 17.7313, \"sparsity\": 0.273, \"allocation\": \"uniform\"}\n\n=== mse30_s123_downstream ===\n  metrics: {\"arc_challenge_acc\": 0.3285, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.5699, \"mmlu_acc\": 0.2781, \"gsm8k_exact_match\": 0.0174, \"hellaswag_acc\": 0.4009, \"hellaswag_acc_norm\": 0.5358, \"piqa_acc\": 0.7106, \"piqa_acc_norm\": 0.7067, \"boolq_acc\": 0.6324}\n\n=== mse30_s42_boolq ===\n  metrics: {\"boolq_acc\": 0.5997, \"boolq_acc_stderr\": 0.008569, \"boolq_sample_len\": 3270}\n\n=== mse30_s42_eval_7task ===\n  metrics: {\"wikitext2_ppl\": 20.43, \"arc_challenge_acc_norm\": 0.3123, \"winogrande_acc\": 0.6038, \"mmlu_acc\": 0.3179, \"gsm8k_exact_match\": 0.0197, \"hellaswag_acc_norm\": 0.5248, \"piqa_acc_norm\": 0.6937}\n\n=== mse30_s42_train ===\n  metrics: {\"final_mse_loss\": 0.005735, \"final_constraint_loss\": 0.007294, \"final_total_loss\": 0.013, \"final_sparsity\": 0.277, \"final_tau\": 0.1, \"final_lambda\": 1000, \"steps\": 1000}\n\n=== mse30_s456 ===\n  metrics: {\"ppl\": 17.3888, \"sparsity\": 0.28, \"allocation\": \"uniform\"}\n\n=== mse30_s456_downstream ===\n  metrics: {\"arc_challenge_acc_norm\": 0.3882, \"winogrande_acc\": 0.6196, \"mmlu_acc\": 0.3264, \"gsm8k_exact_match\": 0.0311, \"hellaswag_acc_norm\": 0.6129, \"piqa_acc_norm\": 0.7383, \"boolq_acc\": 0.7034}\n\n=== mse50_s42_eval_7task ===\n  metrics: {\"wikitext2_ppl\": 229.26, \"arc_challenge_acc_norm\": 0.25, \"winogrande_acc\": 0.5059, \"mmlu_acc\": 0.2379, \"gsm8k_exact_match\": 0.0159, \"hellaswag_acc_norm\": 0.2722, \"piqa_acc_norm\": 0.5577}\n\n=== mse50_s42_train ===\n  metrics: {\"final_loss\": 0.0083, \"final_sparsity\": 0.539, \"steps\": 1000}\n\n=== mvp_bce_s123 ===\n  metrics: {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.3817, \"teal_sparse_ppl\": 44.5864, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 629, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}\n\n=== mvp_bce_s42 ===\n  metrics: {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 27.9603, \"teal_sparse_ppl\": 44.537, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 628, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}\n\n=== mvp_bce_s456 ===\n  metrics: {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 28.1437, \"teal_sparse_ppl\": 43.033, \"model_level_sparsity\": 0.4957, \"ppl_increase_vs_true_dense_pct\": 603.3, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}\n\n=== mvp_kl_norm_v2_s123 ===\n  metrics: {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2474, \"teal_sparse_ppl\": 11.9128, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 94.7, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}\n\n=== mvp_kl_norm_v2_s42 ===\n  metrics: {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.2142, \"teal_sparse_ppl\": 12.0776, \"model_level_sparsity\": 0.4979, \"ppl_increase_vs_true_dense_pct\": 97.4, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}\n\n=== mvp_kl_norm_v2_s456 ===\n  metrics: {\"true_dense_ppl\": 6.1173, \"predictor_hard_mask_ppl\": 9.14, \"teal_sparse_ppl\": 13.58, \"model_level_sparsity\": 0.498, \"ppl_increase_vs_true_dense_pct\": 121.9, \"eval_md5\": \"f4086818bb55dc354ea4c6fe8ed8899a\", \"calibration_samples\": 32, \"vanilla_teal_sparse_ppl_INVALID\": 66036.4062}\n\n=== natural_sparsity_floor_30pct ===\n  metrics: {\"always_pruned_ratio\": 0.0006, \"always_pruned_count\": 278, \"total_neurons\": 458752, \"late_layer_max_ratio\": 0.0051, \"threshold\": 0.1}\n\n=== perlayer_kl_30_s123_v4 ===\n  metrics: {\"final_avg_kl\": 0.0114, \"final_tau\": 0.1, \"steps\": 10000}\n\n=== perlayer_kl_30_s42_v6 ===\n  metrics: {\"steps\": 10000}\n\n=== perlayer_kl_30_s456_downstream ===\n  metrics: {\"arc_challenge_acc_norm\": 0.3848, \"winogrande_acc\": 0.663, \"mmlu_acc\": 0.3904, \"gsm8k_exact_match\": 0.0644, \"hellaswag_acc_norm\": 0.6616, \"piqa_acc_norm\": 0.7356}\n\n=== perlayer_kl_30_s456_ppl ===\n  metrics: {\"wikitext2_ppl\": 9.0282, \"model_level_sparsity\": 0.297}\n\n=== perlayer_kl_k16_eval_final2 ===\n  metrics: {\"wikitext2_ppl\": 8.6737, \"arc_challenge_acc_norm\": 0.4104, \"winogrande_acc\": 0.6843, \"mmlu_acc\": 0.4403, \"gsm8k_exact_match\": 0.0811, \"hellaswag_acc_norm\": 0.6963, \"piqa_acc_norm\": 0.759}\n\n=== perlayer_kl_k16_s123 ===\n  metrics: {\"avg_kl\": 0.1617, \"avg_sparsity\": 0.287, \"final_kl\": 0.1436, \"wall_time_s\": 1982.8}\n\n=== perlayer_kl_k16_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 8.6939, \"arc_challenge_acc_norm\": 0.4317, \"winogrande_acc\": 0.6772, \"mmlu_acc\": 0.3996, \"gsm8k_exact_match\": 0.0986, \"hellaswag_acc_norm\": 0.705, \"piqa_acc_norm\": 0.7481}\n\n=== perlayer_kl_k16_s42_v3 ===\n  metrics: {\"final_kl\": 0.1406, \"final_avg_kl\": 0.1582, \"final_avg_sparsity\": 0.286, \"wall_time_s\": 1982.9}\n\n=== perlayer_kl_k16_s456_eval ===\n  metrics: {\"ppl_wikitext2\": 8.655, \"arc_challenge_acc_norm\": 0.4155, \"winogrande_acc\": 0.6946, \"mmlu_acc\": 0.3873, \"gsm8k_exact_match\": 0.0766, \"hellaswag_acc_norm\": 0.7015, \"piqa_acc_norm\": 0.7437}\n\n=== perlayer_kl_k16_s456_v2 ===\n  metrics: {\"avg_kl\": 0.1565, \"avg_sparsity\": 0.287, \"final_kl\": 0.1611, \"wall_time_s\": 1977.9}\n\n=== perlayer_kl_k2_s123 ===\n  metrics: {}\n\n=== perlayer_kl_k2_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 10.8835, \"arc_challenge_acc_norm\": 0.4078, \"winogrande_acc\": 0.614, \"mmlu_acc\": 0.3789, \"gsm8k_exact_match\": 0.0326, \"hellaswag_acc_norm\": 0.6605, \"piqa_acc_norm\": 0.741}\n\n=== perlayer_kl_k2_s42 ===\n  metrics: {\"final_avg_kl\": 0.0358, \"final_avg_sparsity\": 0.268, \"wall_time_s\": 3841.2, \"training_steps\": 1000, \"note\": \"training only, PPL eval not yet run\"}\n\n=== perlayer_kl_k2_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 10.7958, \"arc_challenge_acc_norm\": 0.3985, \"winogrande_acc\": 0.6322, \"mmlu_acc\": 0.4172, \"gsm8k_exact_match\": 0.0296, \"hellaswag_acc_norm\": 0.6773, \"piqa_acc_norm\": 0.7356}\n\n=== perlayer_kl_k2_s42_train ===\n  metrics: {\"wikitext2_ppl\": 10.7958, \"wikitext2_ppl_pertoken\": 11.0812, \"final_avg_kl\": 0.0358, \"final_avg_sparsity\": 0.268, \"wall_time_s\": 3843, \"eval_mode\": \"teal_global_uniform_30pct\"}\n\n=== perlayer_kl_k2_s456 ===\n  metrics: {}\n\n=== perlayer_kl_k2_s456_eval ===\n  metrics: {\"wikitext2_ppl\": 10.5826, \"arc_challenge_acc_norm\": 0.384, \"winogrande_acc\": 0.6488, \"mmlu_acc\": 0.3542, \"gsm8k_exact_match\": 0.0205, \"hellaswag_acc_norm\": 0.659, \"piqa_acc_norm\": 0.728}\n\n=== perlayer_kl_k4_50_s42 ===\n  metrics: {}\n\n=== perlayer_kl_k4_s42_downstream ===\n  metrics: {\"arc_challenge_acc_norm\": 0.4096, \"winogrande_acc\": 0.6669, \"mmlu_acc\": 0.4353, \"gsm8k_exact_match\": 0.0516, \"hellaswag_acc_norm\": 0.6849, \"piqa_acc_norm\": 0.7399, \"boolq_acc\": 0.7318}\n\n=== perlayer_kl_k8_s123 ===\n  metrics: {\"avg_kl\": 0.0997, \"avg_sparsity\": 0.286, \"final_kl\": 0.0825, \"avg_lambda\": 2182.2, \"steps\": 1000}\n\n=== perlayer_kl_k8_s123_eval ===\n  metrics: {\"wikitext2_ppl\": 9.0648, \"arc_challenge_acc_norm\": 0.4155, \"winogrande_acc\": 0.6993, \"mmlu_acc\": 0.4042, \"gsm8k_exact_match\": 0.0682, \"hellaswag_acc_norm\": 0.6997, \"piqa_acc_norm\": 0.7508}\n\n=== perlayer_kl_k8_s42 ===\n  metrics: {\"wikitext2_ppl\": 8.97, \"final_avg_kl\": 0.0983, \"final_avg_sparsity\": 0.281, \"wall_time_s\": 1894.1}\n\n=== perlayer_kl_k8_s42_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9704, \"arc_challenge_acc_norm\": 0.4104, \"winogrande_acc\": 0.674, \"mmlu_acc\": 0.398, \"gsm8k_exact_match\": 0.0561, \"hellaswag_acc_norm\": 0.6919, \"piqa_acc_norm\": 0.7612}\n\n=== perlayer_kl_k8_s456 ===\n  metrics: {\"avg_kl\": 0.0982, \"avg_sparsity\": 0.285, \"final_kl\": 0.1079, \"avg_lambda\": 2244.28, \"steps\": 1000}\n\n=== perlayer_kl_k8_s456_eval ===\n  metrics: {\"wikitext2_ppl\": 8.9515, \"arc_challenge_acc_norm\": 0.3951, \"winogrande_acc\": 0.6875, \"mmlu_acc\": 0.4105, \"gsm8k_exact_match\": 0.0811, \"hellaswag_acc_norm\": 0.6783, \"piqa_acc_norm\": 0.7399, \"sparsity\": 0.298}\n\n=== perlayer_kl_s123_boolq ===\n  metrics: {\"boolq_acc\": 0.7046}",
      "numLines": 300,
      "startLine": 300,
      "totalLines": 775
    }
  },
  "sourceToolAssistantUUID": "3f6e0a8b-28bc-4c2b-899d-078bd41d4ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "leafUuid": "048732af-9360-4581-b1b4-cfe678a6d893",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper and registry data consistency for R28",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "leafUuid": "048732af-9360-4581-b1b4-cfe678a6d893",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---


### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper and registry data consistency for R28",
  "sessionId": "fa6c7579-d32d-4d0f-b4b4-db9180ddb9b6"
}
```

---
