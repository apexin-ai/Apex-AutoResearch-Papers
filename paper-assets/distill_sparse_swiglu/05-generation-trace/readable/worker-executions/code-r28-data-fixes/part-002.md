# code r28 data fixes — Part 2 of 2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-r28-data-fixes.md) · [Structured JSON](../../../sessions/0a/0a561fb295fd2fb51889.json)

## Before a recorded user message

### Tool result

_source line 104 · 2026-05-24T02:18:32.977Z_

<details><summary>↩ Tool result · `toolu_0142dcWLP1pEWBnqMSpZskfk`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "f33db48b-a9a6-45f3-8f4a-7dd4b28c3910",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Bash · `toolu_01NAhSpKZF6JtKH2hiAhWLce`</summary>

```json
{
  "command": "git show HEAD:paper/method.tex 2>/dev/null | grep -n '148' | head -10",
  "description": "Check committed method.tex for 148"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "d52fe26c-04c0-4f42-a7e7-a9c625253b63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLuzqyJ2417oxvc2t7sxuF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 96725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-24T02:18:33.924Z_

<details><summary>↩ Tool result · `toolu_01NAhSpKZF6JtKH2hiAhWLce`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "0f66e292-e8dc-4962-9f2e-e1c50860bcae",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 107_

<details open><summary>🔧 Tool call — Bash · `toolu_01VotUkmSVA5UJ7Zgon3XeGc`</summary>

```json
{
  "command": "git show HEAD:paper/conclusion.tex 2>/dev/null | grep -n '148' | head -10; git show HEAD:paper/introduction.tex 2>/dev/null | grep -n '148' | head -10; git show HEAD:paper/abstract.tex 2>/dev/null | grep -n '148' | head -10; git show HEAD:paper/limitations.tex 2>/dev/null | grep -n '148' | head -10; git show HEAD:paper/related_work.tex 2>/dev/null | grep -n '148' | head -10",
  "description": "Check all committed tex files for 148"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "e885ebcf-dea3-4de9-be64-a598e4d0ed44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLuzqyJ2417oxvc2t7sxuF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 96725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1798
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 108 · 2026-05-24T02:18:35.618Z_

<details><summary>↩ Tool result · `toolu_01VotUkmSVA5UJ7Zgon3XeGc`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "0a1cb5d3-5c73-4a05-87d1-5fa0e85f4bae",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 109_

<details><summary>Logged reasoning block</summary>

```text
"148" doesn't appear in any committed .tex file either. So Fix 4 was never in the paper tex files. Maybe the task is referring to something planned but not yet written? Or maybe it was in a previous version that was already corrected before the current commits.

Let me also check the Qwen-14B section more carefully. The paper appendix has the Qwen-14B table, let me see if there's any mention of compression ratio.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "e6f9e55a-4a93-4726-8f72-d8282f45c8c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4jReYfz2M3AcC48SvhWwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 98523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Grep · `toolu_01A7T6W7PHDNkSweATQzupSH`</summary>

```json
{
  "pattern": "compress|ratio|\\\\$d_",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "25883e42-1d7b-4549-97e4-b3a80c2affbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4jReYfz2M3AcC48SvhWwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 98523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-24T02:18:43.829Z_

<details><summary>↩ Tool result · `toolu_01A7T6W7PHDNkSweATQzupSH`</summary>

```text
paper/related_work.tex:9:OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
paper/related_work.tex:16:SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
paper/related_work.tex:17:Dhar et al.~\cite{dhar2025clustering} compress activation patterns via clustering for efficient neuron-level prediction.
paper/related_work.tex:34:Haziza et al.~\cite{haziza2025accelerating} demonstrate 2:4 semi-structured activation sparsity with hardware-native acceleration, complementing our unstructured approach.
paper/experiments.tex:129:Configuration & 30\% PPL$\downarrow$ & 50\% PPL$\downarrow$ & $\Delta_{50}$ \\
paper/method.tex:26:At inference, the scores are fed to a global top-$k$ allocation mechanism~\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\rho) \times L \times d_{\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\rho$.
paper/method.tex:55:The Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\tau \to 0$, $\tilde{m}_j$ approaches a binary decision.
paper/method.tex:58:At high temperature, the soft mask permits gradient flow through all neurons for broad exploration.
paper/method.tex:108:Under output-distribution KL, the chain rule introduces a downstream Jacobian $\partial \mathbf{z}_{\text{sparse}} / \partial \tilde{m}_j^{(\ell)}$ that couples neuron $j$'s gradient to all other retained neurons in layers $\ell$ through $L$, because the sparse hidden state propagates through subsequent attention and FFN operations.
paper/limitations.tex:6:\textbf{Evaluation scope.} All predictors train on WikiText-103; C4 evaluation shows preserved KL advantage but $31\times$ higher cross-seed variance. Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.
paper/appendix.tex:33:The pipeline adds $\sim$6.4\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.
paper/appendix.tex:61:The $d_b{=}128$ configuration (75.9M params, $<$1\% of base model) is therefore optimal for the TEAL inference protocol.
paper/appendix.tex:135:The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation; this precision reflects a regime where the target is reachable without $\lambda$ saturation.
paper/appendix.tex:184:Table~\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\ WikiText (in-domain), both at 30\% uniform allocation (seed 42). All six benchmarks show $\Delta$$\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa
paper/appendix.tex:188:\caption{Downstream task robustness to calibration domain shift (KL 30\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\_match (GSM8K).}
paper/appendix.tex:193:Calibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
paper/appendix.tex:232:While specific mask configurations vary moderately across seeds (Jaccard distance 36.3\%), the resulting PPL is highly stable (8.81$\pm$0.02, CV=0.2\%), suggesting multiple near-equivalent optima in the activation mask space.
paper/appendix.tex:236:\section{MSE Baseline Configuration}
paper/appendix.tex:239:The MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\times}10^{-3}$, weight decay $1{\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\tau$: $1.0 \to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.
paper/appendix.tex:295:At 50\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\S\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).
paper/appendix.tex:430:\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. \textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\%: 3-seed mean$\pm$std; other rows: seed 42.}
paper/appendix.tex:445:The KL PPL advantage ratio is consistent across architectures (within 8\% at $\leq$50\% sparsity).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "5767e85f-59c5-4229-9116-7fc10a138092",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/related_work.tex:9:OWL~\\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.\npaper/related_work.tex:16:SVD-CSP~\\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.\npaper/related_work.tex:17:Dhar et al.~\\cite{dhar2025clustering} compress activation patterns via clustering for efficient neuron-level prediction.\npaper/related_work.tex:34:Haziza et al.~\\cite{haziza2025accelerating} demonstrate 2:4 semi-structured activation sparsity with hardware-native acceleration, complementing our unstructured approach.\npaper/experiments.tex:129:Configuration & 30\\% PPL$\\downarrow$ & 50\\% PPL$\\downarrow$ & $\\Delta_{50}$ \\\\\npaper/method.tex:26:At inference, the scores are fed to a global top-$k$ allocation mechanism~\\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\\rho) \\times L \\times d_{\\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\\rho$.\npaper/method.tex:55:The Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\\tau \\to 0$, $\\tilde{m}_j$ approaches a binary decision.\npaper/method.tex:58:At high temperature, the soft mask permits gradient flow through all neurons for broad exploration.\npaper/method.tex:108:Under output-distribution KL, the chain rule introduces a downstream Jacobian $\\partial \\mathbf{z}_{\\text{sparse}} / \\partial \\tilde{m}_j^{(\\ell)}$ that couples neuron $j$'s gradient to all other retained neurons in layers $\\ell$ through $L$, because the sparse hidden state propagates through subsequent attention and FFN operations.\npaper/limitations.tex:6:\\textbf{Evaluation scope.} All predictors train on WikiText-103; C4 evaluation shows preserved KL advantage but $31\\times$ higher cross-seed variance. Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.\npaper/appendix.tex:33:The pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\npaper/appendix.tex:61:The $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\npaper/appendix.tex:135:The 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation; this precision reflects a regime where the target is reachable without $\\lambda$ saturation.\npaper/appendix.tex:184:Table~\\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\\ WikiText (in-domain), both at 30\\% uniform allocation (seed 42). All six benchmarks show $\\Delta$$\\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa\npaper/appendix.tex:188:\\caption{Downstream task robustness to calibration domain shift (KL 30\\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\\_match (GSM8K).}\npaper/appendix.tex:193:Calibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\npaper/appendix.tex:232:While specific mask configurations vary moderately across seeds (Jaccard distance 36.3\\%), the resulting PPL is highly stable (8.81$\\pm$0.02, CV=0.2\\%), suggesting multiple near-equivalent optima in the activation mask space.\npaper/appendix.tex:236:\\section{MSE Baseline Configuration}\npaper/appendix.tex:239:The MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\\times}10^{-3}$, weight decay $1{\\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\\tau$: $1.0 \\to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.\npaper/appendix.tex:295:At 50\\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\\S\\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).\npaper/appendix.tex:430:\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. \\textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\\%: 3-seed mean$\\pm$std; other rows: seed 42.}\npaper/appendix.tex:445:The KL PPL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity).",
    "numLines": 22
  }
}
```

</details>

---


### Assistant

_source line 112_

<details><summary>Logged reasoning block</summary>

```text
OK, I've confirmed that "148×" does NOT appear anywhere in the current paper (neither committed nor working tree). Fix 4 is either already resolved or was never in the paper.

Now let me focus on what actually needs fixing:

**Fix 1**: Table 2 KL 50% global row: PPL 11.84±0.15. Need to recompute from registry.
**Fix 2**: C4 control table WikiText row HS/PIQA: currently 70.85/74.81, needs to be 70.9/74.8


**Fix 3**: C4 control table C4 row PIQA: currently 75.03, needs to be 75.0
**Fix 5**: Extended downstream table TEAL 30% uniform PIQA: 72.80 vs registry 71.98

Now I need to verify Fix 5 by checking the original results.json for the TEAL 30% uniform evaluation to see what acc and acc_norm values are there, and I should also recalculate the Fix 1 values.

Looking at the experiment IDs from the paper comment, I'm pulling together the metrics across different seeds and evaluation runs: the base seed 42 results, the seed 123 PPL re-evaluation, the seed 123 downstream evaluation, and the seed 456 evaluation. I need to aggregate these to get the correct Fix 1 values.

Now I'm calculating the mean and standard deviation across seeds for PPL, getting 11.79 ± 0.07, and working through the same process for ARC-c where the mean comes to 36.52.

Continuing with the remaining benchmarks... I'm finishing the standard deviation calculation for GSM8K, then comparing the corrected benchmark scores across all metrics to see where the biggest changes occurred.

Now I need to track down where the old PPL value of 11.84 appears throughout the document—it shows up in Table 2, a text paragraph, and a couple of appendix tables with allocation data. I'll need to update all instances to 11.79, and for the appendix tables, I should also recalculate any downstream values that depend on this correction.

Looking at the experiments.tex paragraph more carefully, the current text says the E2E value is 11.84, which needs to change to 11.79. But I'm also noticing another value in the main text at line 39 that mentions 11.92 for the KL uniform case. Let me verify this is correct by checking the raw benchmark data—the uniform values across the three seeds average to about 11.92, which matches what's already in the paper, so that one's fine and outside the scope of this fix. I'm going to skip verifying that specific number since it's outside the scope of these five fixes. For Fix 5, I need to SSH into the server to check the TEAL 30% uniform evaluation results, specifically looking for either a `bench_teal30_uniform_6task` result file or a `teal_30pct_uniform_multiseed_eval` file. I'm noticing the registry shows different experiments with different metrics—`teal_30pct_uniform_multiseed_eval` has piqa = 0.7198 while `downstream_teal30_baseline` has piqa_acc = 0.7258—but the table references `bench_teal30_uniform_6task`, which doesn't appear to exist in the registry.

The discrepancy is puzzling: the table shows 72.80 but the registry value is 71.98, and since the caption specifies normalized accuracy, I need to determine whether the 72.80 came from raw accuracy instead. I'll need to check the actual result files on the server to find the correct normalized accuracy value for TEAL 30% uniform.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "4ee23bfc-ee4e-4353-9a53-99532dec056c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRXS7kAyz2SU5cgMLkVtV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1768,
      "cache_read_input_tokens": 99905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1768
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 113_

Now let me SSH to check the TEAL 30% uniform PIQA acc vs acc_norm, and verify Fix 1 calculations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "c92a0f8d-dd4a-4404-9957-11db8a5e5ba7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRXS7kAyz2SU5cgMLkVtV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1768,
      "cache_read_input_tokens": 99905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1768
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 114_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016onNk1BPcVqKc6HsApvHd4`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -path \"*teal*30*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "ed8e2428-10f8-4dee-a589-73941216d475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KRXS7kAyz2SU5cgMLkVtV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1768,
      "cache_read_input_tokens": 99905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1768
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-24T02:19:37.365Z_

<details><summary>↩ Tool result · `toolu_016onNk1BPcVqKc6HsApvHd4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_baseline/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_downstream/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "c0d7651d-4d82-404e-a19b-47dc8c07e8b3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_baseline/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_downstream/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_baseline/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_downstream/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 116_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Aicd9mCAPqLbKu5zxT6Ldt`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -path \"*teal*uniform*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "da9d396c-4e1b-4fc2-a51a-2d06d79100ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Mhq6QgKiVx8ZLomsmR6st",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2949,
      "cache_read_input_tokens": 101673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2949
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-24T02:19:40.232Z_

<details><summary>↩ Tool result · `toolu_01Aicd9mCAPqLbKu5zxT6Ldt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\n/root/distill_sparse_swiglu/results/benchmark/kl_sparsity45_s42_eval_teal_uniform/results.json\\n/root/distill_sparse_swiglu/results/benchmark/kl_sparsity35_s42_eval_teal_uniform/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal275_uniform_eval_v3/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal275_uniform_hspiqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "cb2369b5-05ac-4eff-867a-b35c21ae3b5a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/kl_sparsity45_s42_eval_teal_uniform/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/kl_sparsity35_s42_eval_teal_uniform/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal275_uniform_eval_v3/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal275_uniform_hspiqa/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\n/root/distill_sparse_swiglu/results/benchmark/kl_sparsity45_s42_eval_teal_uniform/results.json\\n/root/distill_sparse_swiglu/results/benchmark/kl_sparsity35_s42_eval_teal_uniform/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal275_uniform_eval_v3/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal275_uniform_hspiqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 118_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01745Zqe2PeNwaHPk2kitpkY`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -path \"*teal*30pct*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "26f2edf0-f76b-4e55-a6a4-14c8c70a73e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4oXmE3CSuFHgBeF92RRgy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 104622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-24T02:19:45.563Z_

<details><summary>↩ Tool result · `toolu_01745Zqe2PeNwaHPk2kitpkY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "62e98cae-cfb3-4977-9b14-2b6b2d629f26",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 120_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DUp3WPcFLtNMmf4eCZuA9a`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -path \"*6task*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "edc83776-ed9a-4328-8b9f-09023e0fff6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4oXmE3CSuFHgBeF92RRgy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 104622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-24T02:19:46.175Z_

<details><summary>↩ Tool result · `toolu_01DUp3WPcFLtNMmf4eCZuA9a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "4472f69c-66c3-43dc-a92e-4dec1cbe5596",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 122_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MQC3gvpue89MsyKZmKNTCf`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -path \"*teal30*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "e1cbca16-eae0-4b39-9f24-c5a32ce46096",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F323DE1Rf6aKuBZMXgzPsa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 456,
      "cache_read_input_tokens": 105087,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 456
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-24T02:19:48.888Z_

<details><summary>↩ Tool result · `toolu_01MQC3gvpue89MsyKZmKNTCf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_baseline/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_downstream/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "1687b287-cb8a-4cf4-8cf0-8d99921ae12c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_baseline/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_downstream/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_baseline/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_4task/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_teal30_downstream/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_gsm8k/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 124_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BUfNnt7oFugXD434DBQfUp`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -type f -path \"*downstream*teal*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "7b57191a-d127-44c5-8762-78333235895c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVj3FPFUx7fAzc2uwdiBxe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 105543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-24T02:19:52.132Z_

<details><summary>↩ Tool result · `toolu_01BUfNnt7oFugXD434DBQfUp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "eba76357-bffc-476d-bda5-ef8e417fdc23",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 126_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012Jo1uyAkdXNBnjzPWo8DBi`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -type f -path \"*teal*hellaswag*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "814656d4-68b7-4530-8548-036f5242bf33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVj3FPFUx7fAzc2uwdiBxe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 105543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-24T02:19:52.896Z_

<details><summary>↩ Tool result · `toolu_012Jo1uyAkdXNBnjzPWo8DBi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "5a4532be-90ce-4489-a816-80887f1f32ed",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 128_

<details><summary>Logged reasoning block</summary>

```text
There's no TEAL 30% uniform HellaSwag/PIQA result file on the server. The registry has `teal_30pct_uniform_multiseed_eval` with piqa=0.7198 and hellaswag=0.6331, but that file doesn't exist on the server.

Let me look at the bench_teal30 results to see if it has PIQA.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "10c9ed15-d12e-4362-abb5-4bebaee2c795",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011isQV2pgx5ZeYhfoDXrmqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 105979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 129_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019AHmbFv2s1pvWK5ofeTaTq`</summary>

```json
{
  "server": "westd-34887",
  "command": "cat /root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "fb8a2874-bd04-42d6-9a5e-c7b26f695a6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011isQV2pgx5ZeYhfoDXrmqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 105979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-24T02:19:59.776Z_

<details><summary>↩ Tool result · `toolu_019AHmbFv2s1pvWK5ofeTaTq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_id\\\": \\\"bench_teal30\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/llama-3.1-8b\\\",\\n    \\\"checkpoint\\\": null,\\n    \\\"tasks\\\": \\\"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\\\",\\n    \\\"sparsity_mode\\\": \\\"per_token\\\",\\n    \\\"baseline_mode\\\": \\\"teal_vanilla\\\",\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"bench_teal30\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"global_topk\\\",\\n    \\\"gpu\\\": 0,\\n    \\\"seq_len\\\": 2048,\\n    \\\"calibration_samples\\\": 32,\\n    \\\"batch_size\\\": 8,\\n    \\\"bottleneck_size\\\": 128,\\n    \\\"svd_rank\\\": 256,\\n    \\\"max_eval_samples\\\": null\\n  },\\n  \\\"mode\\\": {\\n    \\\"mode\\\": \\\"baseline_teal_vanilla\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"global_topk\\\"\\n  },\\n  \\\"metrics\\\": {\\n    \\\"wikitext2_ppl\\\": 10.9688,\\n    \\\"lm_eval\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc\\\": 0.3857,\\n        \\\"acc_stderr\\\": 0.014224250973257123,\\n        \\\"acc_norm\\\": 0.4232,\\n        \\\"acc_norm_stderr\\\": 0.014438036220848015\\n      },\\n      \\\"winogrande\\\": {\\n        \\\"sample_len\\\": 1267,\\n        \\\"acc\\\": 0.6606,\\n        \\\"acc_stderr\\\": 0.01330771492894184\\n      },\\n      \\\"mmlu\\\": {\\n        \\\"sample_len\\\": 14042,\\n        \\\"acc\\\": 0.3861,\\n        \\\"acc_stderr\\\": 0.004044650114820884\\n      },\\n      \\\"gsm8k\\\": {\\n        \\\"sample_len\\\": 1319,\\n        \\\"exact_match\\\": 0.0788,\\n        \\\"exact_match_stderr\\\": 0.007423390519873243\\n      }\\n    },\\n    \\\"lm_eval_raw\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"name\\\": \\\"arc_challenge\\\",\\n        \\\"alias\\\": \\\"arc_challenge\\\",\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc,none\\\": 0.3856655290102389,\\n        \\\"acc_stderr,none\\\": 0.014224250973257123,\\n        \\\"acc_norm,none\\\": 0.4232081911262799,\\n        \\\"acc_norm_stderr,none\\\": 0.014438036220848015\\n      },\\n      \\\"winogrande\\\": {\\n        \\\"name\\\": \\\"winogrande\\\",\\n        \\\"alias\\\": \\\"winogrande\\\",\\n        \\\"sample_len\\\": 1267,\\n        \\\"acc,none\\\": 0.6606156274664562,\\n        \\\"acc_stderr,none\\\": 0.01330771492894184\\n      },\\n      \\\"mmlu\\\": {\\n        \\\"alias\\\": \\\"mmlu\\\",\\n        \\\"name\\\": \\\"mmlu\\\",\\n        \\\"sample_len\\\": 14042,\\n        \\\"acc,none\\\": 0.38605611736219914,\\n        \\\"acc_stderr,none\\\": 0.004044650114820884,\\n        \\\"sample_count\\\": {\\n          \\\"acc,none\\\": 14042\\n        }\\n      },\\n      \\\"gsm8k\\\": {\\n        \\\"name\\\": \\\"gsm8k\\\",\\n        \\\"alias\\\": \\\"gsm8k\\\",\\n        \\\"sample_len\\\": 1319,\\n        \\\"exact_match,strict-match\\\": 0.07505686125852919,\\n        \\\"exact_match_stderr,strict-match\\\": 0.007257633145486642,\\n        \\\"exact_match,flexible-extract\\\": 0.07884761182714177,\\n        \\\"exact_match_stderr,flexible-extract\\\": 0.007423390519873243\\n      }\\n    }\\n  },\\n  \\\"timestamp\\\": \\\"2026-05-16 19:40:24\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "00f52b8e-38af-4016-81ef-bb67307ca0f0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"exp_id\\\\\\\": \\\\\\\"bench_teal30\\\\\\\",\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"model_name_or_path\\\\\\\": \\\\\\\"/root/autodl-tmp/models/llama-3.1-8b\\\\\\\",\\\\n    \\\\\\\"checkpoint\\\\\\\": null,\\\\n    \\\\\\\"tasks\\\\\\\": \\\\\\\"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\\\\\\\",\\\\n    \\\\\\\"sparsity_mode\\\\\\\": \\\\\\\"per_token\\\\\\\",\\\\n    \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"teal_vanilla\\\\\\\",\\\\n    \\\\\\\"dense\\\\\\\": false,\\\\n    \\\\\\\"exp_id\\\\\\\": \\\\\\\"bench_teal30\\\\\\\",\\\\n    \\\\\\\"sparsity_target\\\\\\\": 0.3,\\\\n    \\\\\\\"allocation\\\\\\\": \\\\\\\"global_topk\\\\\\\",\\\\n    \\\\\\\"gpu\\\\\\\": 0,\\\\n    \\\\\\\"seq_len\\\\\\\": 2048,\\\\n    \\\\\\\"calibration_samples\\\\\\\": 32,\\\\n    \\\\\\\"batch_size\\\\\\\": 8,\\\\n    \\\\\\\"bottleneck_size\\\\\\\": 128,\\\\n    \\\\\\\"svd_rank\\\\\\\": 256,\\\\n    \\\\\\\"max_eval_samples\\\\\\\": null\\\\n  },\\\\n  \\\\\\\"mode\\\\\\\": {\\\\n    \\\\\\\"mode\\\\\\\": \\\\\\\"baseline_teal_vanilla\\\\\\\",\\\\n    \\\\\\\"sparsity_target\\\\\\\": 0.3,\\\\n    \\\\\\\"allocation\\\\\\\": \\\\\\\"global_topk\\\\\\\"\\\\n  },\\\\n  \\\\\\\"metrics\\\\\\\": {\\\\n    \\\\\\\"wikitext2_ppl\\\\\\\": 10.9688,\\\\n    \\\\\\\"lm_eval\\\\\\\": {\\\\n      \\\\\\\"arc_challenge\\\\\\\": {\\\\n        \\\\\\\"sample_len\\\\\\\": 1172,\\\\n        \\\\\\\"acc\\\\\\\": 0.3857,\\\\n        \\\\\\\"acc_stderr\\\\\\\": 0.014224250973257123,\\\\n        \\\\\\\"acc_norm\\\\\\\": 0.4232,\\\\n        \\\\\\\"acc_norm_stderr\\\\\\\": 0.014438036220848015\\\\n      },\\\\n      \\\\\\\"winogrande\\\\\\\": {\\\\n        \\\\\\\"sample_len\\\\\\\": 1267,\\\\n        \\\\\\\"acc\\\\\\\": 0.6606,\\\\n        \\\\\\\"acc_stderr\\\\\\\": 0.01330771492894184\\\\n      },\\\\n      \\\\\\\"mmlu\\\\\\\": {\\\\n        \\\\\\\"sample_len\\\\\\\": 14042,\\\\n        \\\\\\\"acc\\\\\\\": 0.3861,\\\\n        \\\\\\\"acc_stderr\\\\\\\": 0.004044650114820884\\\\n      },\\\\n      \\\\\\\"gsm8k\\\\\\\": {\\\\n        \\\\\\\"sample_len\\\\\\\": 1319,\\\\n        \\\\\\\"exact_match\\\\\\\": 0.0788,\\\\n        \\\\\\\"exact_match_stderr\\\\\\\": 0.007423390519873243\\\\n      }\\\\n    },\\\\n    \\\\\\\"lm_eval_raw\\\\\\\": {\\\\n      \\\\\\\"arc_challenge\\\\\\\": {\\\\n        \\\\\\\"name\\\\\\\": \\\\\\\"arc_challenge\\\\\\\",\\\\n        \\\\\\\"alias\\\\\\\": \\\\\\\"arc_challenge\\\\\\\",\\\\n        \\\\\\\"sample_len\\\\\\\": 1172,\\\\n        \\\\\\\"acc,none\\\\\\\": 0.3856655290102389,\\\\n        \\\\\\\"acc_stderr,none\\\\\\\": 0.014224250973257123,\\\\n        \\\\\\\"acc_norm,none\\\\\\\": 0.4232081911262799,\\\\n        \\\\\\\"acc_norm_stderr,none\\\\\\\": 0.014438036220848015\\\\n      },\\\\n      \\\\\\\"winogrande\\\\\\\": {\\\\n        \\\\\\\"name\\\\\\\": \\\\\\\"winogrande\\\\\\\",\\\\n        \\\\\\\"alias\\\\\\\": \\\\\\\"winogrande\\\\\\\",\\\\n        \\\\\\\"sample_len\\\\\\\": 1267,\\\\n        \\\\\\\"acc,none\\\\\\\": 0.6606156274664562,\\\\n        \\\\\\\"acc_stderr,none\\\\\\\": 0.01330771492894184\\\\n      },\\\\n      \\\\\\\"mmlu\\\\\\\": {\\\\n        \\\\\\\"alias\\\\\\\": \\\\\\\"mmlu\\\\\\\",\\\\n        \\\\\\\"name\\\\\\\": \\\\\\\"mmlu\\\\\\\",\\\\n        \\\\\\\"sample_len\\\\\\\": 14042,\\\\n        \\\\\\\"acc,none\\\\\\\": 0.38605611736219914,\\\\n        \\\\\\\"acc_stderr,none\\\\\\\": 0.004044650114820884,\\\\n        \\\\\\\"sample_count\\\\\\\": {\\\\n          \\\\\\\"acc,none\\\\\\\": 14042\\\\n        }\\\\n      },\\\\n      \\\\\\\"gsm8k\\\\\\\": {\\\\n        \\\\\\\"name\\\\\\\": \\\\\\\"gsm8k\\\\\\\",\\\\n        \\\\\\\"alias\\\\\\\": \\\\\\\"gsm8k\\\\\\\",\\\\n        \\\\\\\"sample_len\\\\\\\": 1319,\\\\n        \\\\\\\"exact_match,strict-match\\\\\\\": 0.07505686125852919,\\\\n        \\\\\\\"exact_match_stderr,strict-match\\\\\\\": 0.007257633145486642,\\\\n        \\\\\\\"exact_match,flexible-extract\\\\\\\": 0.07884761182714177,\\\\n        \\\\\\\"exact_match_stderr,flexible-extract\\\\\\\": 0.007423390519873243\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"timestamp\\\\\\\": \\\\\\\"2026-05-16 19:40:24\\\\\\\"\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_id\\\": \\\"bench_teal30\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/llama-3.1-8b\\\",\\n    \\\"checkpoint\\\": null,\\n    \\\"tasks\\\": \\\"wikitext2,arc_challenge,winogrande,mmlu,gsm8k\\\",\\n    \\\"sparsity_mode\\\": \\\"per_token\\\",\\n    \\\"baseline_mode\\\": \\\"teal_vanilla\\\",\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"bench_teal30\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"global_topk\\\",\\n    \\\"gpu\\\": 0,\\n    \\\"seq_len\\\": 2048,\\n    \\\"calibration_samples\\\": 32,\\n    \\\"batch_size\\\": 8,\\n    \\\"bottleneck_size\\\": 128,\\n    \\\"svd_rank\\\": 256,\\n    \\\"max_eval_samples\\\": null\\n  },\\n  \\\"mode\\\": {\\n    \\\"mode\\\": \\\"baseline_teal_vanilla\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"global_topk\\\"\\n  },\\n  \\\"metrics\\\": {\\n    \\\"wikitext2_ppl\\\": 10.9688,\\n    \\\"lm_eval\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc\\\": 0.3857,\\n        \\\"acc_stderr\\\": 0.014224250973257123,\\n        \\\"acc_norm\\\": 0.4232,\\n        \\\"acc_norm_stderr\\\": 0.014438036220848015\\n      },\\n      \\\"winogrande\\\": {\\n        \\\"sample_len\\\": 1267,\\n        \\\"acc\\\": 0.6606,\\n        \\\"acc_stderr\\\": 0.01330771492894184\\n      },\\n      \\\"mmlu\\\": {\\n        \\\"sample_len\\\": 14042,\\n        \\\"acc\\\": 0.3861,\\n        \\\"acc_stderr\\\": 0.004044650114820884\\n      },\\n      \\\"gsm8k\\\": {\\n        \\\"sample_len\\\": 1319,\\n        \\\"exact_match\\\": 0.0788,\\n        \\\"exact_match_stderr\\\": 0.007423390519873243\\n      }\\n    },\\n    \\\"lm_eval_raw\\\": {\\n      \\\"arc_challenge\\\": {\\n        \\\"name\\\": \\\"arc_challenge\\\",\\n        \\\"alias\\\": \\\"arc_challenge\\\",\\n        \\\"sample_len\\\": 1172,\\n        \\\"acc,none\\\": 0.3856655290102389,\\n        \\\"acc_stderr,none\\\": 0.014224250973257123,\\n        \\\"acc_norm,none\\\": 0.4232081911262799,\\n        \\\"acc_norm_stderr,none\\\": 0.014438036220848015\\n      },\\n      \\\"winogrande\\\": {\\n        \\\"name\\\": \\\"winogrande\\\",\\n        \\\"alias\\\": \\\"winogrande\\\",\\n        \\\"sample_len\\\": 1267,\\n        \\\"acc,none\\\": 0.6606156274664562,\\n        \\\"acc_stderr,none\\\": 0.01330771492894184\\n      },\\n      \\\"mmlu\\\": {\\n        \\\"alias\\\": \\\"mmlu\\\",\\n        \\\"name\\\": \\\"mmlu\\\",\\n        \\\"sample_len\\\": 14042,\\n        \\\"acc,none\\\": 0.38605611736219914,\\n        \\\"acc_stderr,none\\\": 0.004044650114820884,\\n        \\\"sample_count\\\": {\\n          \\\"acc,none\\\": 14042\\n        }\\n      },\\n      \\\"gsm8k\\\": {\\n        \\\"name\\\": \\\"gsm8k\\\",\\n        \\\"alias\\\": \\\"gsm8k\\\",\\n        \\\"sample_len\\\": 1319,\\n        \\\"exact_match,strict-match\\\": 0.07505686125852919,\\n        \\\"exact_match_stderr,strict-match\\\": 0.007257633145486642,\\n        \\\"exact_match,flexible-extract\\\": 0.07884761182714177,\\n        \\\"exact_match_stderr,flexible-extract\\\": 0.007423390519873243\\n      }\\n    }\\n  },\\n  \\\"timestamp\\\": \\\"2026-05-16 19:40:24\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 131_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013gyfu9skxyPBJ8J1d3QPkf`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -type f -path \"*bench_teal*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "fb65669b-c8c6-48e9-bb5f-caa58a9ae794",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011isQV2pgx5ZeYhfoDXrmqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 105979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-24T02:20:00.523Z_

<details><summary>↩ Tool result · `toolu_013gyfu9skxyPBJ8J1d3QPkf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/bench_teal50/results.json\\n/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "1d2e6183-8247-48d7-8843-7f500e00bda0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/distill_sparse_swiglu/results/benchmark/bench_teal50/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/bench_teal50/results.json\\n/root/distill_sparse_swiglu/results/benchmark/bench_teal30/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 133_

<details><summary>Logged reasoning block</summary>

```text
bench_teal30 is TEAL global, not uniform. I can't find a TEAL 30% uniform with HellaSwag/PIQA on the server. 

Let me look for the `teal_30pct_uniform_multiseed_eval` results. They might be in a different directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "17ffae3c-f8c1-48cc-9e1e-5fc3e4333593",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNCevhNGSTMtbCA48qCJyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2191,
      "cache_read_input_tokens": 106438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2191
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 134_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PgK259E3C18JNeeCgj5VsG`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu -name \"*.json\" -type f -path \"*teal*30*piqa*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "6f24018f-7720-4c93-8a01-3b99a4a95ef7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNCevhNGSTMtbCA48qCJyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2191,
      "cache_read_input_tokens": 106438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2191
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-24T02:20:07.178Z_

<details><summary>↩ Tool result · `toolu_01PgK259E3C18JNeeCgj5VsG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "9ecf3e5d-1d1c-492f-a1f6-414ed0c98a68",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform_hspiqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_global_hspiqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 136_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019kphWbktMRrHPszAyH3CCb`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu -name \"*.json\" -type f -path \"*multiseed*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "669a82c8-2baa-4912-9d9e-b5d342dba6da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNCevhNGSTMtbCA48qCJyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2191,
      "cache_read_input_tokens": 106438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2191
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-24T02:20:07.707Z_

<details><summary>↩ Tool result · `toolu_019kphWbktMRrHPszAyH3CCb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "83821aa0-0d4b-44d0-961f-336aa42ae413",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 138_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0167p7aJvFXfahT73RqYAPG7`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu -name \"*.json\" -type f -path \"*teal*uniform*hellaswag*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "1b502493-1f61-4c31-8086-872708dd08fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017phLvXL6XtQVFo4CiKmtTp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 108629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 615
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-24T02:20:11.823Z_

<details><summary>↩ Tool result · `toolu_0167p7aJvFXfahT73RqYAPG7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "86535ea0-2297-4ff2-a90b-46f5ef35f569",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 140_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Ha2KjeoEpVFvKVeJxZqngQ`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu -name \"*.json\" -type f -path \"*bench_teal*uniform*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "91a17d9c-6981-4e7d-9306-13f133125527",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017phLvXL6XtQVFo4CiKmtTp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 108629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 615
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-24T02:20:12.677Z_

<details><summary>↩ Tool result · `toolu_01Ha2KjeoEpVFvKVeJxZqngQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "d96a3a3b-30b0-4b64-87fb-59f3e62922ab",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 142_

<details><summary>Logged reasoning block</summary>

```text
I can't find the TEAL 30% uniform HellaSwag/PIQA results file on the server. The registry entry `teal_30pct_uniform_multiseed_eval` has `piqa: 0.7198` but I can't verify if this is acc or acc_norm from the raw results.

Looking at the registry data again:
- `teal_30pct_uniform_multiseed_eval`: piqa = 0.7198, hellaswag = 0.6331
- `downstream_teal30_baseline`: piqa_acc = 0.7258, piqa_acc_norm = 0.7361, hellaswag_acc = 0.4878, hellaswag_acc_norm = 0.667


The `downstream_teal30_baseline` appears to be the non-uniform TEAL 30% baseline with both acc and acc_norm values, while `teal_30pct_uniform_multiseed_eval` only has a single piqa value that's ambiguous—it could be either 0.7198 as acc_norm (which would round to 72.0 in the paper) or as acc with the acc_norm value missing. I need to check what the paper's table actually shows to resolve this.

The paper's caption indicates "PIQA: 0-shot normalized acc," so it should be acc_norm, but the table shows 72.80 which doesn't match 0.7198 at all. Let me look at the actual metric keys in the registry data—I can see that `downstream_teal30_baseline` has both piqa_acc and piqa_acc_norm values, and the registry's single "piqa" value of 0.6331 for HellaSwag matches the paper's 63.31, suggesting the registry key maps directly to the paper's reported values.

For PIQA specifically, the registry shows 0.7198 but the paper reports 72.80—that's a discrepancy of 0.82 percentage points, which is too large to be a rounding difference. I need to figure out whether the paper's value is actually acc (not acc_norm as the caption claims) or if there's an error in one of these sources.

Let me search through the actual experiment results to find a case where I can see both PIQA's acc and acc_norm values side by side, which should clarify the pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "989cc715-4719-4db8-a992-60af0bf2053f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXxkzgcVtfULz7YkAkC8bh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 109244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 143_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VsKKTWCbVTXfwCL6W3oR3j`</summary>

```json
{
  "server": "westd-34887",
  "command": "find /root/distill_sparse_swiglu/results -name \"*.json\" -type f -path \"*hellaswag_piqa*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "f91c4e97-05c3-4fce-817e-f789838f9bc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXxkzgcVtfULz7YkAkC8bh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 109244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-24T02:20:33.828Z_

<details><summary>↩ Tool result · `toolu_01VsKKTWCbVTXfwCL6W3oR3j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/kl30_uniform_hellaswag_piqa_v2/results.json\\n/root/distill_sparse_swiglu/results/benchmark/dense_baseline_hellaswag_piqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/bce_isocompute_hellaswag_piqa_v2/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_hellaswag_piqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_dense_hellaswag_piqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "18c9e1b4-ad3e-46fa-aae3-9f4c9408e05a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/distill_sparse_swiglu/results/benchmark/kl30_uniform_hellaswag_piqa_v2/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/dense_baseline_hellaswag_piqa/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/bce_isocompute_hellaswag_piqa_v2/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_hellaswag_piqa/results.json\\\\n/root/distill_sparse_swiglu/results/benchmark/mistral_dense_hellaswag_piqa/results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/distill_sparse_swiglu/results/benchmark/kl30_uniform_hellaswag_piqa_v2/results.json\\n/root/distill_sparse_swiglu/results/benchmark/dense_baseline_hellaswag_piqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/bce_isocompute_hellaswag_piqa_v2/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_kl30_hellaswag_piqa/results.json\\n/root/distill_sparse_swiglu/results/benchmark/mistral_dense_hellaswag_piqa/results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 145_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LEyYLCAm2bejw9mpQLqkjM`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -A3 piqa /root/distill_sparse_swiglu/results/benchmark/kl30_uniform_hellaswag_piqa_v2/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "14f7a91d-5a45-4504-ab96-1a9e8589364a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5D5eSauDAaDvML4M1pMc7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 109703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1274
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-24T02:20:36.633Z_

<details><summary>↩ Tool result · `toolu_01LEyYLCAm2bejw9mpQLqkjM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"exp_id\\\": \\\"kl30_uniform_hellaswag_piqa_v2\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/llama-3.1-8b\\\",\\n    \\\"checkpoint\\\": \\\"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\\\",\\n    \\\"tasks\\\": \\\"hellaswag,piqa\\\",\\n    \\\"sparsity_mode\\\": \\\"teal_global\\\",\\n    \\\"baseline_mode\\\": null,\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"kl30_uniform_hellaswag_piqa_v2\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\",\\n    \\\"gpu\\\": 0,\\n--\\n      \\\"piqa\\\": {\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc\\\": 0.7399,\\n        \\\"acc_stderr\\\": 0.010234893249061136,\\n--\\n      \\\"piqa\\\": {\\n        \\\"name\\\": \\\"piqa\\\",\\n        \\\"alias\\\": \\\"piqa\\\",\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc,none\\\": 0.7399347116430903,\\n        \\\"acc_stderr,none\\\": 0.010234893249061136,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "83c9f30f-449f-494d-8afe-a7423cb57f42",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  \\\\\\\"exp_id\\\\\\\": \\\\\\\"kl30_uniform_hellaswag_piqa_v2\\\\\\\",\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"model_name_or_path\\\\\\\": \\\\\\\"/root/autodl-tmp/models/llama-3.1-8b\\\\\\\",\\\\n    \\\\\\\"checkpoint\\\\\\\": \\\\\\\"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\\\\\\\",\\\\n    \\\\\\\"tasks\\\\\\\": \\\\\\\"hellaswag,piqa\\\\\\\",\\\\n    \\\\\\\"sparsity_mode\\\\\\\": \\\\\\\"teal_global\\\\\\\",\\\\n    \\\\\\\"baseline_mode\\\\\\\": null,\\\\n    \\\\\\\"dense\\\\\\\": false,\\\\n    \\\\\\\"exp_id\\\\\\\": \\\\\\\"kl30_uniform_hellaswag_piqa_v2\\\\\\\",\\\\n    \\\\\\\"sparsity_target\\\\\\\": 0.3,\\\\n    \\\\\\\"allocation\\\\\\\": \\\\\\\"uniform\\\\\\\",\\\\n    \\\\\\\"gpu\\\\\\\": 0,\\\\n--\\\\n      \\\\\\\"piqa\\\\\\\": {\\\\n        \\\\\\\"sample_len\\\\\\\": 1838,\\\\n        \\\\\\\"acc\\\\\\\": 0.7399,\\\\n        \\\\\\\"acc_stderr\\\\\\\": 0.010234893249061136,\\\\n--\\\\n      \\\\\\\"piqa\\\\\\\": {\\\\n        \\\\\\\"name\\\\\\\": \\\\\\\"piqa\\\\\\\",\\\\n        \\\\\\\"alias\\\\\\\": \\\\\\\"piqa\\\\\\\",\\\\n        \\\\\\\"sample_len\\\\\\\": 1838,\\\\n        \\\\\\\"acc,none\\\\\\\": 0.7399347116430903,\\\\n        \\\\\\\"acc_stderr,none\\\\\\\": 0.010234893249061136,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  \\\"exp_id\\\": \\\"kl30_uniform_hellaswag_piqa_v2\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/llama-3.1-8b\\\",\\n    \\\"checkpoint\\\": \\\"checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt\\\",\\n    \\\"tasks\\\": \\\"hellaswag,piqa\\\",\\n    \\\"sparsity_mode\\\": \\\"teal_global\\\",\\n    \\\"baseline_mode\\\": null,\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"kl30_uniform_hellaswag_piqa_v2\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\",\\n    \\\"gpu\\\": 0,\\n--\\n      \\\"piqa\\\": {\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc\\\": 0.7399,\\n        \\\"acc_stderr\\\": 0.010234893249061136,\\n--\\n      \\\"piqa\\\": {\\n        \\\"name\\\": \\\"piqa\\\",\\n        \\\"alias\\\": \\\"piqa\\\",\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc,none\\\": 0.7399347116430903,\\n        \\\"acc_stderr,none\\\": 0.010234893249061136,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 147_

<details><summary>Logged reasoning block</summary>

```text
Hmm, the `kl30_uniform_hellaswag_piqa_v2` result for PIQA only shows acc=0.7399, not acc_norm. Let me get the full output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "e7062f1e-059e-4006-a610-e34dadb24100",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYRY4Jk7XH33VxZ7X9x4Mo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 110977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 148_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0156fu8pPJqtThXG5HZ1syJJ`</summary>

```json
{
  "server": "westd-34887",
  "command": "grep -A8 \"\\\"piqa\\\":\" /root/distill_sparse_swiglu/results/benchmark/kl30_uniform_hellaswag_piqa_v2/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "f79a3388-7c9d-4ec3-a32e-8350bae61bb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYRY4Jk7XH33VxZ7X9x4Mo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 110977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-24T02:20:41.064Z_

<details><summary>↩ Tool result · `toolu_0156fu8pPJqtThXG5HZ1syJJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"piqa\\\": {\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc\\\": 0.7399,\\n        \\\"acc_stderr\\\": 0.010234893249061136,\\n        \\\"acc_norm\\\": 0.7481,\\n        \\\"acc_norm_stderr\\\": 0.010128421335088757\\n      }\\n    },\\n    \\\"lm_eval_raw\\\": {\\n--\\n      \\\"piqa\\\": {\\n        \\\"name\\\": \\\"piqa\\\",\\n        \\\"alias\\\": \\\"piqa\\\",\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc,none\\\": 0.7399347116430903,\\n        \\\"acc_stderr,none\\\": 0.010234893249061136,\\n        \\\"acc_norm,none\\\": 0.7480957562568009,\\n        \\\"acc_norm_stderr,none\\\": 0.010128421335088757\\n      }\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "095d536e-c797-401d-912b-f2623339a6b2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"      \\\\\\\"piqa\\\\\\\": {\\\\n        \\\\\\\"sample_len\\\\\\\": 1838,\\\\n        \\\\\\\"acc\\\\\\\": 0.7399,\\\\n        \\\\\\\"acc_stderr\\\\\\\": 0.010234893249061136,\\\\n        \\\\\\\"acc_norm\\\\\\\": 0.7481,\\\\n        \\\\\\\"acc_norm_stderr\\\\\\\": 0.010128421335088757\\\\n      }\\\\n    },\\\\n    \\\\\\\"lm_eval_raw\\\\\\\": {\\\\n--\\\\n      \\\\\\\"piqa\\\\\\\": {\\\\n        \\\\\\\"name\\\\\\\": \\\\\\\"piqa\\\\\\\",\\\\n        \\\\\\\"alias\\\\\\\": \\\\\\\"piqa\\\\\\\",\\\\n        \\\\\\\"sample_len\\\\\\\": 1838,\\\\n        \\\\\\\"acc,none\\\\\\\": 0.7399347116430903,\\\\n        \\\\\\\"acc_stderr,none\\\\\\\": 0.010234893249061136,\\\\n        \\\\\\\"acc_norm,none\\\\\\\": 0.7480957562568009,\\\\n        \\\\\\\"acc_norm_stderr,none\\\\\\\": 0.010128421335088757\\\\n      }\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"      \\\"piqa\\\": {\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc\\\": 0.7399,\\n        \\\"acc_stderr\\\": 0.010234893249061136,\\n        \\\"acc_norm\\\": 0.7481,\\n        \\\"acc_norm_stderr\\\": 0.010128421335088757\\n      }\\n    },\\n    \\\"lm_eval_raw\\\": {\\n--\\n      \\\"piqa\\\": {\\n        \\\"name\\\": \\\"piqa\\\",\\n        \\\"alias\\\": \\\"piqa\\\",\\n        \\\"sample_len\\\": 1838,\\n        \\\"acc,none\\\": 0.7399347116430903,\\n        \\\"acc_stderr,none\\\": 0.010234893249061136,\\n        \\\"acc_norm,none\\\": 0.7480957562568009,\\n        \\\"acc_norm_stderr,none\\\": 0.010128421335088757\\n      }\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 150_

<details><summary>Logged reasoning block</summary>

```text
Great, so for `kl30_uniform_hellaswag_piqa_v2`:
- piqa_acc = 0.7399, piqa_acc_norm = 0.7481

The registry for this experiment shows `piqa_acc_norm: 0.7481` — which matches. So the registry properly stores acc_norm for this experiment.

Now for `teal_30pct_uniform_multiseed_eval`, the registry shows just `piqa: 0.7198`. Since the key doesn't have `_acc_norm`, it's ambiguous. But the piqa value for this experiment could be acc (not acc_norm).


Since I don't have the results file for this experiment, I need to infer the correct acc_norm value by comparing it to the global baseline. The uniform allocation version at 30% TEAL should produce different PIQA scores than the global baseline, which shows piqa_acc=0.7258 and piqa_acc_norm=0.7361.

Looking at the registry value of 0.7198 for piqa and comparing it to the paper's 0.7280, the 0.82 percentage point difference matches exactly what I see in the kl30_uniform experiment (acc=73.99, acc_norm=74.81). This suggests the paper is likely using piqa_acc_norm ≈ 0.7280, which would be consistent with the acc_norm pattern. However, without access to the raw results, I can't definitively verify this, and the task indicates the value is incorrect.

Let me check the registry directly for the TEAL 30% uniform evaluation to see whether the metric is stored as piqa_acc or piqa_acc_norm, and if only the acc value exists, I may need to access the server to retrieve the original results.

json file. Looking at the pattern from KL 30% uniform which uses acc_norm consistently, the TEAL table should follow the same metric convention, but the registry entry for teal_30pct_uniform_multiseed_eval only shows perplexity and arc_challenge scores without the PIQA breakdown.

Comparing the registry values to Table 2, I can see the PPL matches (10.8173 ≈ 10.82), and the other metrics like winogrande (0.6504) and mmlu (0.4586) align with the table percentages when converted—so these are likely accuracy scores, not normalized variants. The issue is that PIQA is missing from this registry entry entirely, which is why I can't verify whether the table's 71.98 value is correct or needs updating. The registry entry for teal_30pct_uniform_multiseed_eval shows arc_challenge = 0.3771, but I'm not sure if that's the accuracy or normalized accuracy metric. If it's normalized accuracy, that would be 37.71%, which doesn't match Table 2's 39.33% for TEAL uniform. The bench_teal30 global entry shows arc_challenge_acc_norm = 0.4232, which is also different. It seems like the table might be referencing a different experiment entirely—possibly teal30_uniform—that isn't in the registry I'm looking at.

Let me focus on what I can actually fix with confidence. I have clear registry data with properly labeled metrics for the KL 50% global row, so I can recalculate those values. I also notice some potential rounding issues in the C4 control table's WikiText row for HS/PIQA that I should check.

There are a few other discrepancies I've identified: the "148×" notation doesn't match the actual intermediate size calculation for Qwen-2.5-14B, and the extended downstream table's TEAL 30% uniform PIQA value of 72.80 doesn't align with what the registry shows. For that last one, the registry only has an ambiguous metric key without clear labeling, so I'm uncertain whether 72.80 represents the correct normalized accuracy or if it's a different metric entirely.

Actually, reconsidering this—the task notes that other parts of the paper use acc_norm (like for arc_challenge), so PIQA should probably follow the same convention. The registry only has acc=71.98 without an acc_norm value, which means I'd need to access the original results file on the server to find the normalized accuracy. Looking at the typical gap between acc and acc_norm for PIQA, the KL experiment shows a difference of about 0.82 percentage points, so I could estimate from there, but without the actual value I'm hesitant to guess. I need to clarify what the task is actually asking for. The paper shows 72.80 for PIQA, but the registry only has 71.98, and the instructions are telling me to check whether the metric key should be `piqa_acc` or `piqa_acc_norm`, then find the correct `acc_norm` value from the original results.json file if it exists on the server. Since I can't access that file, I need to figure out what the right value should be based on the paper's requirements.

Looking at the other metrics in the same evaluation run, HellaSwag shows 0.6331 in the registry, which matches the paper's 63.31 — and this is clearly `acc_norm` since the baseline `acc` is only 0.4878. For PIQA, the baseline shows `acc=0.7258` and `acc_norm=0.7361`, so I need to determine which one the paper is actually using and whether 72.80 corresponds to either of these values or if there's a different `acc_norm` value from the multiseed evaluation.

Since HellaSwag is definitely using `acc_norm` in this experiment, it would be inconsistent for PIQA to use `acc` instead — they should follow the same convention. The lm-evaluation-harness likely designates a primary metric for each task, and if HellaSwag's primary is `acc_norm`, then PIQA's probably is too. The default metrics in lm-evaluation-harness are acc_norm for HellaSwag and acc for PIQA, which would make the registry values hellaswag=0.6331 (acc_norm) and piqa=0.7198 (acc). If piqa_acc_norm is actually around 72.80% as the paper claims, that would explain the discrepancy—but then this wouldn't be a problem worth flagging, so something's still off.

Since I can't access the server's results.json to verify the actual acc_norm value and the registry key is ambiguous, I'm stuck between trusting the paper's 72.80% figure or reporting the uncertainty to the user. Given the tight deadline, I need to decide whether to make an educated guess based on the 0.82 percentage point gap pattern or escalate this as unverifiable.

Let me cross-check if there's another benchmark entry with the same PIQA configuration that might help me validate which value is correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "f4cfce88-5940-46d1-b822-748fba5f55c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C6htPafYwQ1qeP8aZmauD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 111659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 582
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 151_

<details open><summary>🔧 Tool call — Bash · `toolu_01FTsWn6dgVwc7mgm8o28zuz`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/c3531263-9e9c-43e4-8f45-2fbded6acba7/tool-results/mcp-agent-ml-research-read_registry-1779588692860.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Check bench_teal50_uniform_6task and hellaswag_piqa_kl50 experiments\nfor k in ['bench_teal50_uniform_6task', 'hellaswag_piqa_kl50_global', 'hellaswag_piqa_kl50_uniform',\n          'bce_isocompute_30u_hellaswag_piqa', 'bce_isocompute_hellaswag_piqa', 'bce_isocompute_hellaswag_piqa_v2']:\n    if k in exps:\n        e = exps[k]\n        m = e.get('metrics',{})\n        print(f'{k}: {json.dumps(m, indent=2)}')\n        print()\n\n# Also check all experiments with piqa close to 0.72-0.73  \nprint('=== All PIQA values in paper range ===')\nfor k in sorted(exps.keys()):\n    m = exps[k].get('metrics', {})\n    for mk, mv in m.items():\n        if 'piqa' in mk and isinstance(mv, (int, float)) and 0.71 < mv < 0.73:\n            print(f'{k}: {mk} = {mv}')\n\"\n",
  "description": "Check additional PIQA experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "16ae12e7-0429-482c-89ae-43873f9eeb48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C6htPafYwQ1qeP8aZmauD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 111659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 582
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-24T02:22:10.540Z_

<details><summary>↩ Tool result · `toolu_01FTsWn6dgVwc7mgm8o28zuz`</summary>

```text
bce_isocompute_hellaswag_piqa_v2: {
  "hellaswag_acc_norm": 0.6281,
  "piqa_acc_norm": 0.7421
}

=== All PIQA values in paper range ===
downstream_teal30_baseline: piqa_acc = 0.7258
kl_sparsity40_s42_global_eval_v2: piqa_acc_norm = 0.7269
kl_sparsity40_s42_uniform_hspiqa: piqa_acc_norm = 0.7236
mistral_teal30_downstream: piqa_acc_norm = 0.7214
mse30_s123_downstream: piqa_acc = 0.7106
perlayer_kl_k2_s456_eval: piqa_acc_norm = 0.728
teal_30pct_uniform_multiseed_eval: piqa = 0.7198
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "8286d55a-ecb4-42de-b50e-2ee6da6d045f",
  "tool_use_result": {
    "stdout": "bce_isocompute_hellaswag_piqa_v2: {\n  \"hellaswag_acc_norm\": 0.6281,\n  \"piqa_acc_norm\": 0.7421\n}\n\n=== All PIQA values in paper range ===\ndownstream_teal30_baseline: piqa_acc = 0.7258\nkl_sparsity40_s42_global_eval_v2: piqa_acc_norm = 0.7269\nkl_sparsity40_s42_uniform_hspiqa: piqa_acc_norm = 0.7236\nmistral_teal30_downstream: piqa_acc_norm = 0.7214\nmse30_s123_downstream: piqa_acc = 0.7106\nperlayer_kl_k2_s456_eval: piqa_acc_norm = 0.728\nteal_30pct_uniform_multiseed_eval: piqa = 0.7198",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 153_

<details><summary>Logged reasoning block</summary>

```text
Looking at the data, `teal_30pct_uniform_multiseed_eval` has piqa = 0.7198 and no other entries with this exact value or different acc/acc_norm.

There's no way to determine the acc_norm value since the raw results file doesn't exist on the server. However:

1. The registry's hellaswag=0.6331 is definitely acc_norm (HellaSwag acc is typically ~0.49)
2. The piqa=0.7198 value is ambiguous

Given the pattern:


- HellaSwag stored acc_norm as the standard metric
- PIQA's standard metric in lm-eval-harness is acc, not acc_norm

So the 0.7198 is likely the acc value, with acc_norm being higher. The paper's 72.80 could be the acc_norm if the eval script captured it separately, but I can't verify this. Since I can't determine which is correct, I need to decide whether to keep 72.80 or find the true value.

Actually, wait—if the paper table caption specifies "normalized acc," then 72.80 might already be the correct acc_norm value to use, which would mean no fix is needed at all. Let me check the other TEAL experiment to see the typical difference between acc and acc_norm for PIQA. The downstream baseline shows about a 1.03 percentage point gap between them, so if the uniform variant has piqa_acc at 0.7198, the acc_norm should be around 0.7301, which is closer to 0.7280 than I initially thought.

So the registry's 0.7198 is likely the raw accuracy, while the paper's 72.80 is the normalized version—both could be correct depending on which metric the paper intended to report. Since the task explicitly flags this as a must-fix discrepancy, I should surface this ambiguity to the user and let them clarify whether the paper meant to use acc_norm or if there's a genuine mismatch that needs resolving.

For the other fixes, I'm looking at rounding adjustments in the tables—specifically making the C4 control WikiText row consistent with the downstream results by rounding 70.85 to 70.9 and 74.81 to 74.8.

Now for Fix 3, I'm checking the PIQA value in the C4 control row. The task mentions a discrepancy between the paper showing 74.86 and the registry showing 75.03, but when I look at the current paper, it already has 75.03, which matches the registry. The task description suggests 74.86 might have been the original value that was already corrected to 75.03, and now it just needs rounding to 75.0 for consistency. I see the task is asking to round 75.03 to 75.0 for consistency with 1-decimal precision across the table, just like 70.85 becomes 70.9 and 74.81 becomes 74.8.

Now for Fix 4, I need to verify the Qwen-2.5-14B architecture parameters and check if the 148× ratio mentioned in the task actually appears in the paper or appendix. Looking at the Qwen-14B section in the appendix, I can see it mentions 30% nominal sparsity but the text cuts off—I need to find where this ratio calculation should be documented or if it's missing from the current version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "e2503ed8-cd89-491a-b013-5de4d183127c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GznGudNMZ6oTFZS2h2DEA3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4517,
      "cache_read_input_tokens": 112241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4517
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 154_

<details open><summary>🔧 Tool call — Grep · `toolu_01AUZGgrRkD1GccVqaKw8ipV`</summary>

```json
{
  "pattern": "148",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "glob": "*.md",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "31b151fa-6ffb-4e2a-b4a5-3d90c41e29f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GznGudNMZ6oTFZS2h2DEA3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4517,
      "cache_read_input_tokens": 112241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4517
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-24T02:23:07.360Z_

<details><summary>↩ Tool result · `toolu_01AUZGgrRkD1GccVqaKw8ipV`</summary>

```text
artifacts/westd34887_check_results.md:34:Layer 25: 0.137, Layer 26: 0.148, Layer 27: 0.172, Layer 28: 0.230, Layer 29: 0.227
artifacts/r28_data_consistency_report.md:58:### 5. Experiments prose — "148× vs. 112× compression" for Qwen14B
artifacts/r28_data_consistency_report.md:60:Paper claims Qwen-2.5-14B has d_ff/d_b = 148× (implying d_ff=18,944). Registry shows `trainable_params='117M (0.793%)'` for `qwen14b_kl30_s123`. Back-computing:
artifacts/r28_data_consistency_report.md:64:- 13,923 / 128 ≈ **109×**, not 148×
artifacts/r28_data_consistency_report.md:67:The 148× claim is inconsistent with the registered trainable parameter count.
artifacts/r28_data_consistency_report.md:199:4. **148× compression claim:** Back-computation from registered 117M params implies d_ff≈13,923 (109×), not 18,944 (148×). Verify Qwen-2.5-14B's actual intermediate_size and correct.
artifacts/_project/report/r28_data_consistency_report.md:58:### 5. Experiments prose — "148× vs. 112× compression" for Qwen14B
artifacts/_project/report/r28_data_consistency_report.md:60:Paper claims Qwen-2.5-14B has d_ff/d_b = 148× (implying d_ff=18,944). Registry shows `trainable_params='117M (0.793%)'` for `qwen14b_kl30_s123`. Back-computing:
artifacts/_project/report/r28_data_consistency_report.md:64:- 13,923 / 128 ≈ **109×**, not 148×
artifacts/_project/report/r28_data_consistency_report.md:67:The 148× claim is inconsistent with the registered trainable parameter count.
artifacts/_project/report/r28_data_consistency_report.md:199:4. **148× compression claim:** Back-computation from registered 117M params implies d_ff≈13,923 (109×), not 18,944 (148×). Verify Qwen-2.5-14B's actual intermediate_size and correct.
task_context/history/agent/loop_10_1779054963.md:30:刚派出 worker_infra_urgent_collect_all_14b_results_20260517T214835 去两台机器收集所有结果——这个 Worker 尚未返回。
task_context/history/agent/loop_12.md:26:- 活跃 Worker: `worker_infra_urgent_collect_all_14b_results_20260517T214835`（CPU，读 4 个 eval 日志）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "3c1bb741-bca6-4158-891d-dd437140fade",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/westd34887_check_results.md:34:Layer 25: 0.137, Layer 26: 0.148, Layer 27: 0.172, Layer 28: 0.230, Layer 29: 0.227\nartifacts/r28_data_consistency_report.md:58:### 5. Experiments prose — \"148× vs. 112× compression\" for Qwen14B\nartifacts/r28_data_consistency_report.md:60:Paper claims Qwen-2.5-14B has d_ff/d_b = 148× (implying d_ff=18,944). Registry shows `trainable_params='117M (0.793%)'` for `qwen14b_kl30_s123`. Back-computing:\nartifacts/r28_data_consistency_report.md:64:- 13,923 / 128 ≈ **109×**, not 148×\nartifacts/r28_data_consistency_report.md:67:The 148× claim is inconsistent with the registered trainable parameter count.\nartifacts/r28_data_consistency_report.md:199:4. **148× compression claim:** Back-computation from registered 117M params implies d_ff≈13,923 (109×), not 18,944 (148×). Verify Qwen-2.5-14B's actual intermediate_size and correct.\nartifacts/_project/report/r28_data_consistency_report.md:58:### 5. Experiments prose — \"148× vs. 112× compression\" for Qwen14B\nartifacts/_project/report/r28_data_consistency_report.md:60:Paper claims Qwen-2.5-14B has d_ff/d_b = 148× (implying d_ff=18,944). Registry shows `trainable_params='117M (0.793%)'` for `qwen14b_kl30_s123`. Back-computing:\nartifacts/_project/report/r28_data_consistency_report.md:64:- 13,923 / 128 ≈ **109×**, not 148×\nartifacts/_project/report/r28_data_consistency_report.md:67:The 148× claim is inconsistent with the registered trainable parameter count.\nartifacts/_project/report/r28_data_consistency_report.md:199:4. **148× compression claim:** Back-computation from registered 117M params implies d_ff≈13,923 (109×), not 18,944 (148×). Verify Qwen-2.5-14B's actual intermediate_size and correct.\ntask_context/history/agent/loop_10_1779054963.md:30:刚派出 worker_infra_urgent_collect_all_14b_results_20260517T214835 去两台机器收集所有结果——这个 Worker 尚未返回。\ntask_context/history/agent/loop_12.md:26:- 活跃 Worker: `worker_infra_urgent_collect_all_14b_results_20260517T214835`（CPU，读 4 个 eval 日志）",
    "numLines": 13
  }
}
```

</details>

---


### Assistant

_source line 156_

<details><summary>Logged reasoning block</summary>

````text
The report says "Paper claims Qwen-2.5-14B has d_ff/d_b = 148×" but I can't find this in the actual tex files. This means the 148× was planned to be written or was in a draft that's been edited. Since it's not in the current paper, Fix 4 is either already resolved or was preemptively caught.

But let me check if there was supposed to be a sentence added to the experiments.tex cross-architecture section about the compression ratio. Looking at the current text:

```
On Mistral-7B-v0.3~\cite{jiang2023mistral}, PPL generalizes ($-$17.3\%, 3-seed; Table~\ref{tab:mistral_downstream}); on Qwen-2.5-14B~\cite{qwen2024qwen25}, PPL generalizes but MMLU/GSM8K decline

(Table~\ref{tab:14b}).
```

No mention of compression ratio. The r28_data_consistency_report mentions "Experiments prose" so maybe this was planned for the experiments section but never written. In that case, Fix 4 doesn't need any changes to the current paper. The appendix tables just show results without mentioning predictor parameter counts for Qwen, so the "148×" claim appears to have been dropped entirely from the final version.

For Fix 4, the correct ratio would be 108× (13824/128) if this information were to be added back, but since it's not currently in the paper, no edits are needed here.

Now I'm identifying what actually needs fixing. Fix 1 requires updating Table 2's KL 50% global row with the correct values from the registry: PPL should be 11.79±0.07 instead of 11.84±0.15, ARC-c should be 36.5±3.3 instead of 36.3±3.2, and WG should be 63.9±0.4 instead of 63.8±0.3, while MMLU and GSM8K remain unchanged. I'm debating whether to round the HS value in the C4 row for consistency across the column, even though the task only specifies rounding PIQA. Since I'm already changing WikiText to use 1 decimal place, it makes sense to apply the same formatting to C4 for uniformity — so I'll round both HS and PIQA values to 1 decimal: WikiText becomes 70.9 / 74.8 and C4 becomes 69.2 / 75.0.

For the compression ratio issue, I've noted that the paper claims 148× but the actual ratio is 108×, so I'll flag this discrepancy to the user.

On the PIQA downstream result, the registry shows 0.7198 while the paper reports 72.80, which likely represents different metrics (piqa_acc vs piqa_acc_norm). Since I can't verify the results file, I'll flag this uncertainty to the user but note that 72.80 aligns with the expected piqa_acc_norm based on the typical gap patterns I'm seeing across other experiments.

Now I'm cross-checking the HellaSwag results between the registry and paper values. The registry shows hellaswag_acc_norm=0.7085 for the 3-seed experiment, but the paper reports 71.07±0.54, which is slightly higher. I'm trying to determine if there's a version mismatch or if I'm looking at different experiment configurations.

Let me step back and focus on the actual edits I need to make. For Fix 5, I'm checking whether the paper's PIQA value of 72.80 is the normalized accuracy (which would be correct) or the raw accuracy. The gap between piqa_acc and piqa_acc_norm is typically 0.8-1.0 percentage points in these experiments, and 72.80 - 71.98 = 0.82pp, which fits that pattern and suggests 72.80 is indeed the normalized accuracy.

The HellaSwag value of 63.31 is definitely normalized accuracy since raw HS accuracy would be around 49%. While the registry uses unsuffixed keys without clarification and I don't have a server results file to verify, the evidence points to 72.80 being correct as piqa_acc_norm. I'll keep it as-is and explain to the user that the registry value (71.98) is likely the raw accuracy, not normalized. If they want to verify, they could SSH into the server to check the original results file.

Given the time constraints with the deadline tomorrow, I'll flag this uncertainty to the user and move forward with the other fixes I'm confident about rather than attempting to re-run the evaluation or search for additional TEAL uniform eval results. this is acc, it doesn't match 72.80; if this is acc_norm, it should be 71.98

Since the HellaSwag value matches perfectly with the table, and the table caption says "normalized acc", the registry must be storing normalized acc for HellaSwag but might be storing raw acc for PIQA. This inconsistency is possible if the eval script used the "default" metric for each benchmark (HellaSwag's default is acc_norm, PIQA's default is acc in many implementations).

I'm now fairly confident that:
- piqa = 0.7198 in registry is piqa_acc
- The paper's 72.80 is piqa_acc_norm
- These are consistent

But I still can't verify the acc_norm value. Let me just note this to the user and move on. If 72.80 is correct acc_norm, no change needed. If it's wrong, the user would need to re-run the eval.

Looking at the TEAL 50% row in the extended downstream table, I notice those experiment IDs don't exist in the registry—they might be runs that weren't registered. So I'm going to proceed with my edits now. I need to update Table 2 for the KL 50% global row across all locations, changing PPL from 11.84±0.15 to 11.79±0.07 and ARC-c from 36.3±3.2 to 36.5±3.3. I need to verify Fix 1 with a careful calculation using Python to make sure I'm getting the arithmetic right.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "114728e5-0d54-4eb9-8bdd-304aa138d9e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1nMWRXyC9W8v3y3SX3X5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 116758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2917
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 157_

Now I have all the data needed. Let me verify my Fix 1 calculations precisely and then make all edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "1ff2213f-8ad7-4e52-9266-196c8bee9c25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1nMWRXyC9W8v3y3SX3X5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 116758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2917
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 158_

<details open><summary>🔧 Tool call — Bash · `toolu_012gvu1VStcZGhzGptN2WaPw`</summary>

```json
{
  "command": "python3 -c \"\nimport math\n\n# Fix 1: Recalculate KL 50% global 3-seed stats\n# Source exp_ids: bench_kl50_global (s42), kl50_global_s123_reeval (s123 PPL), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456)\n\nppl = [11.7933, 11.7184, 11.8614]\narc = [32.85, 39.16, 37.54]  # ARC-c acc_norm as percentages\nwg = [63.46, 64.01, 64.17]  # WG acc as percentages\nmmlu = [27.89, 29.08, 27.84]  # MMLU acc as percentages\ngsm = [1.29, 3.41, 2.12]  # GSM8K exact_match as percentages\n\ndef stats(vals, name):\n    n = len(vals)\n    mean = sum(vals) / n\n    var = sum((v - mean)**2 for v in vals) / (n - 1)  # sample std\n    std = math.sqrt(var)\n    print(f'{name}: mean={mean:.2f}, std={std:.2f}  (raw: {[round(v,4) for v in vals]})')\n    return mean, std\n\nstats(ppl, 'PPL')\nstats(arc, 'ARC-c')\nstats(wg, 'WG')\nstats(mmlu, 'MMLU')\nstats(gsm, 'GSM8K')\n\n# Also check: the 50% KL uniform PPL (mentioned in text as 11.92)\nppl_uniform = [11.963, 11.83, 11.9604]\nstats(ppl_uniform, 'KL 50% uniform PPL')\n\n# Check the paragraph text: '11.92 vs. 23.90, 50% reduction'\nprint(f'\\\\nKL uniform mean: {sum(ppl_uniform)/3:.2f}')\nprint(f'Reduction: {(23.90 - 11.92)/23.90 * 100:.1f}%')\n\"\n",
  "description": "Calculate Fix 1 3-seed statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "8c61395e-2b6c-4a23-a459-0bd62f1eea68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1nMWRXyC9W8v3y3SX3X5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2917,
      "cache_read_input_tokens": 116758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2917
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-24T02:24:20.662Z_

<details><summary>↩ Tool result · `toolu_012gvu1VStcZGhzGptN2WaPw`</summary>

```text
PPL: mean=11.79, std=0.07  (raw: [11.7933, 11.7184, 11.8614])
ARC-c: mean=36.52, std=3.28  (raw: [32.85, 39.16, 37.54])
WG: mean=63.88, std=0.37  (raw: [63.46, 64.01, 64.17])
MMLU: mean=28.27, std=0.70  (raw: [27.89, 29.08, 27.84])
GSM8K: mean=2.27, std=1.07  (raw: [1.29, 3.41, 2.12])
KL 50% uniform PPL: mean=11.92, std=0.08  (raw: [11.963, 11.83, 11.9604])

KL uniform mean: 11.92
Reduction: 50.1%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "7e6f627f-0412-4f9c-b211-5b931f400369",
  "tool_use_result": {
    "stdout": "PPL: mean=11.79, std=0.07  (raw: [11.7933, 11.7184, 11.8614])\nARC-c: mean=36.52, std=3.28  (raw: [32.85, 39.16, 37.54])\nWG: mean=63.88, std=0.37  (raw: [63.46, 64.01, 64.17])\nMMLU: mean=28.27, std=0.70  (raw: [27.89, 29.08, 27.84])\nGSM8K: mean=2.27, std=1.07  (raw: [1.29, 3.41, 2.12])\nKL 50% uniform PPL: mean=11.92, std=0.08  (raw: [11.963, 11.83, 11.9604])\n\nKL uniform mean: 11.92\nReduction: 50.1%",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 160_

<details><summary>Logged reasoning block</summary>

```text
Good, the stats confirm:
- PPL: 11.79±0.07
- ARC-c: 36.5±3.3 
- WG: 63.9±0.4 (I'll round 0.37 to 0.4)
- MMLU: 28.3±0.7 (same)
- GSM8K: 2.3±1.1

Now let me also verify the text at experiments.tex:39:
"At 50\%, the PPL advantage widens (11.92 vs.\ 23.90, 50\% reduction)"


I see the discrepancy — the text is comparing KL uniform (11.92) against TEAL uniform (23.90), not KL global which is 11.79. So the 50% reduction figure refers to the uniform variant comparison, not the global one.

Looking at the GSM8K numbers, the current table shows 2.7±1.3 for KL global, which would become 2.3±1.1 with the correction. The statement "≤2.7%" technically still holds as an upper bound, but given that the maximum across individual seeds reaches 3.41%, I should tighten this to "≤3%" or "≤3.4%" for accuracy. Looking at the corrected mean values across methods, the maximum is 2.3% for KL global, so I should update the statement from "≤2.7%" to "≤2.3%" — though individual seeds with the ±1.1 standard deviation can reach up to 3.4%. The corrected mean for KL global on GSM8K is 2.3%, so I should update the bound from 2.7% to either 2.3% or round up to 3% for a cleaner statement. Since the text is already describing "near-random" performance, I'll go with ≤3% as a simple, safe bound that captures the corrected value. The corrected KL global value of 2.3% is still within the ≤2.7% bound, so that claim remains valid even if it's now looser. Now I need to update the E2E result at 50% from 11.84 to 11.79, and I'm finding this value referenced in multiple places—the main experiments section and the appendix at lines 350 and 387. Let me check if there are other KL-related values scattered throughout the paper that need correction. I'm tracking down all the references to that 11.84 metric across the paper to ensure consistency, and now I need to search for any mentions of percentage improvements like "50% reduction" or "49% advantage" that might be tied to outdated performance numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "8738fd64-cf35-497b-a647-d6bac1b1fdb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHmtAbQW6d3ggTKtfxSYQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3775,
      "cache_read_input_tokens": 119675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3775
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 161_

Good. Now let me also check for references to the KL 50% global PPL ratio elsewhere.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "edf90a29-55ab-4ec4-b181-646e0212f1d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHmtAbQW6d3ggTKtfxSYQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3775,
      "cache_read_input_tokens": 119675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3775
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 162_

<details open><summary>🔧 Tool call — Grep · `toolu_01T98CRquNhJqvLkE1xGkCxY`</summary>

```json
{
  "pattern": "50.*reduction|49.*advantage|11\\.79|50\\%.*PPL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "76b53307-1e6c-4593-9cc6-a5f8b4b1a019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHmtAbQW6d3ggTKtfxSYQf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3775,
      "cache_read_input_tokens": 119675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3775
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-24T02:25:06.556Z_

<details><summary>↩ Tool result · `toolu_01T98CRquNhJqvLkE1xGkCxY`</summary>

```text
paper/experiments.tex:39:At 50\%, the PPL advantage widens (11.92 vs.\ 23.90, 50\% reduction) and generalizes to C4 (Appendix~\ref{app:ood}), but all methods collapse to near-random on MMLU and GSM8K ($\leq$2.7\%); no allocation strategy recovers at this capacity limit. % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval, d030_kl50_uniform, multi_seed_kl50_global
paper/experiments.tex:74:At $2.71\times$ KL compute budget (2700 steps, matched wall-clock), BCE achieves PPL 28.13$\pm$0.20 (3-seed), still $2.39\times$ worse than KL (11.79). % exp_id: bce50_3seed
paper/experiments.tex:82:Despite this, KL achieves PPL 11.79 vs.\ BCE's 28.13$\pm$0.20, confirming that distributional fidelity, not magnitude agreement, produces better masks. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap
paper/experiments.tex:132:Forward KL + Gumbel (Ours) & \textbf{8.81$\pm$0.02} & \textbf{11.79} & --- \\ % exp_id: kl30_ablation_s42, bench_kl50_global
paper/experiments.tex:152:At 50\%, Gumbel-Sigmoid outperforms STE~\cite{bengio2013ste} by 33.8\% (11.79 vs.\ 15.77); forward KL outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with mode-covering~\cite{gu2024minillm}. % exp_id: ste_baseline_s42, jsd_ablation_s42, reverse_kl_ablation_s42
paper/method.tex:64:Gumbel relaxation eliminates this pathology and contributes a 33.8\% improvement (PPL 15.77 $\to$ 11.79 at 50\% sparsity), as we verify empirically in \S\ref{sec:experiments}.
paper/appendix.tex:439:50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
paper/appendix.tex:495:SPON~\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\% PPL improvement (12.08$\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "c1398d77-6de3-4e01-8f22-a3db7699c381",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:39:At 50\\%, the PPL advantage widens (11.92 vs.\\ 23.90, 50\\% reduction) and generalizes to C4 (Appendix~\\ref{app:ood}), but all methods collapse to near-random on MMLU and GSM8K ($\\leq$2.7\\%); no allocation strategy recovers at this capacity limit. % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval, d030_kl50_uniform, multi_seed_kl50_global\npaper/experiments.tex:74:At $2.71\\times$ KL compute budget (2700 steps, matched wall-clock), BCE achieves PPL 28.13$\\pm$0.20 (3-seed), still $2.39\\times$ worse than KL (11.79). % exp_id: bce50_3seed\npaper/experiments.tex:82:Despite this, KL achieves PPL 11.79 vs.\\ BCE's 28.13$\\pm$0.20, confirming that distributional fidelity, not magnitude agreement, produces better masks. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap\npaper/experiments.tex:132:Forward KL + Gumbel (Ours) & \\textbf{8.81$\\pm$0.02} & \\textbf{11.79} & --- \\\\ % exp_id: kl30_ablation_s42, bench_kl50_global\npaper/experiments.tex:152:At 50\\%, Gumbel-Sigmoid outperforms STE~\\cite{bengio2013ste} by 33.8\\% (11.79 vs.\\ 15.77); forward KL outperforms JSD (+6.4\\%) and reverse KL (+8.6\\%), consistent with mode-covering~\\cite{gu2024minillm}. % exp_id: ste_baseline_s42, jsd_ablation_s42, reverse_kl_ablation_s42\npaper/method.tex:64:Gumbel relaxation eliminates this pathology and contributes a 33.8\\% improvement (PPL 15.77 $\\to$ 11.79 at 50\\% sparsity), as we verify empirically in \\S\\ref{sec:experiments}.\npaper/appendix.tex:439:50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\npaper/appendix.tex:495:SPON~\\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42",
    "numLines": 8
  }
}
```

</details>

---


### Assistant

_source line 164_

<details><summary>Logged reasoning block</summary>

```text
The 11.79 that appears in the ablation table (experiments.tex:132), comparison text (experiments.tex:74, 82, 152), method.tex:64, and appendix.tex:439, 495 all reference the single-seed s42 KL 50% global PPL (bench_kl50_global = 11.7933 ≈ 11.79). These are correct single-seed values and should NOT be changed. Only the 3-seed mean (11.84±0.15) needs correction.

Now let me also check:
- experiments.tex:39 says "11.92 vs.\ 23.90, 50\% reduction" — this is KL uniform vs TEAL uniform, not KL global. 

The 11.92 is the 3-seed uniform mean (11.92±0.08), which checks out. The 23.90 is TEAL uniform at 50%, and the 50% reduction claim holds up: (23.90-11.92)/23.90 = 50.1%. I also need to verify the "$\leq$2.7\%" bound for max GSM8K across methods—with the corrected KL global GSM8K = 2.3, all methods still fall within that threshold.

Now I'm going through the edits systematically. For experiments.tex line 64, I need to update the KL global row with the corrected values...

And then line 159 needs the E2E value changed from 11.84 to 11.79. But I'm realizing there's a subtle issue here—11.84 was the original 3-seed mean, and now that I've recalculated it, the new 3-seed mean is also 11.79, which happens to match the s42 value. So the text change is correct, but I should verify this is the right number to use. Looking at the actual experiment IDs and their corresponding values, bench_kl50_global gives PPL=11.7933 for the s42 checkpoint, which rounds to 11.79—so that's the value I should use instead of 11.84. The 3-seed mean also comes out to 11.79, so either way the number is consistent.

Updating the LaTeX tables to reflect the correct PPL values and standard deviations... Now I'm applying these corrections to the appendix file, updating the numerical values in the control rows for both WikiText-103 and C4 datasets to reflect the rounded metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "e1fe1197-7380-42a9-a4a7-6de5fad52df2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g6Y39r7jBS5W46SHjbohC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 123450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3015
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 165_

I now have a complete picture. Let me make all the edits.

**Summary of changes needed:**
- Fix 1: Table 2 KL 50% global → PPL 11.79±0.07, ARC 36.5±3.3, WG 63.9±0.4, GSM8K 2.3±1.1 (4 locations)
- Fix 2: C4 control table WikiText row HS/PIQA → 70.9/74.8
- Fix 3: C4 control table C4 row → 69.2/75.0
- Fix 4: "148×" not in paper — confirmed correct ratio is 108× (Qwen intermediate_size=13824)
- Fix 5: TEAL PIQA 72.80 — registry "piqa"=71.98 is likely raw acc; paper's 72.80 is likely correct acc_norm (gap matches pattern)

Starting edits:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "35d0a2d1-448a-40a2-a5c5-62160952e5bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g6Y39r7jBS5W46SHjbohC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 123450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3015
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 166_

<details open><summary>🔧 Tool call — Edit · `toolu_01QoWrUWRgrPqB8dwVA6ztHr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "old_string": "& KL global (Ours) & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & 28.3$\\pm$0.7 & \\textbf{2.7$\\pm$1.3} \\\\ % exp_id: bench_kl50_global (s42), kl50_global_s123_reeval (s123 PPL), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456)",
  "new_string": "& KL global (Ours) & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & 28.3$\\pm$0.7 & \\textbf{2.3$\\pm$1.1} \\\\ % exp_id: bench_kl50_global (s42 PPL=11.79), kl50_global_s123_reeval (s123 PPL=11.72), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456 PPL=11.86)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "55d45775-07e3-4189-8e9b-b3d1e86e3997",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g6Y39r7jBS5W46SHjbohC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 123450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3015
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-24T02:25:52.046Z_

<details><summary>↩ Tool result · `toolu_01QoWrUWRgrPqB8dwVA6ztHr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "3390d05d-7dd1-4a6a-a1d3-e2ef460b0c07",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "oldString": "& KL global (Ours) & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & 28.3$\\pm$0.7 & \\textbf{2.7$\\pm$1.3} \\\\ % exp_id: bench_kl50_global (s42), kl50_global_s123_reeval (s123 PPL), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456)",
    "newString": "& KL global (Ours) & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & 28.3$\\pm$0.7 & \\textbf{2.3$\\pm$1.1} \\\\ % exp_id: bench_kl50_global (s42 PPL=11.79), kl50_global_s123_reeval (s123 PPL=11.72), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456 PPL=11.86)",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + GELU + Linear($128 \\to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB), using AdamW~\\cite{loshchilov2019adamw} with learning rate $1 \\times 10^{-3}$, weight decay $1 \\times 10^{-2}$, and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly\\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \\textbf{BCE predictor} (DejaVu-style~\\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; and (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison. Uniform allocation preserves downstream performance best; global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).\nAt 30\\% sparsity, output-distribution KL under uniform allocation achieves PPL 8.81$\\pm$0.02 (3-seed), a 14.5\\% reduction over TEAL at matched actual sparsity (8.81 vs.\\ 10.30, both at 28.5\\%; Appendix~\\ref{app:ood}).\nUniform allocation yields stable downstream (MMLU 40.7$\\pm$1.3\\%, 3-seed; Appendix~\\ref{app:stability}), while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%) from late-layer starvation (L31 retention 28.4\\%; \\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform, kl30_3seed\n\n\\paragraph{Task-Type Split.}\nKL shows directional improvements over TEAL on commonsense reasoning (ARC-c, WG, HellaSwag, PIQA: 4/4 wins at 30\\% uniform) but underperforms on knowledge-intensive tasks (MMLU, GSM8K: 0/2).\nWith only three seeds, 95\\% confidence intervals for individual downstream tasks overlap; we therefore treat PPL ($\\sigma{=}0.02$, non-overlapping) as the primary metric and downstream differences as directional evidence.\nThe KL predictor protects L14--L18 (14--18\\% sparsity vs.\\ 32\\% global mean) while aggressively pruning L22--L28 (48--57\\%). Constraint interventions (Appendix~\\ref{app:constraint}) confirm a task-dependent trade-off: removing the valley improves MMLU +3.4pp but reduces ARC-c by 1.5pp, consistent with localized factual associations~\\cite{geva2023dissecting}; task-aware allocation may resolve this. % exp_id: bench_kl30_uniform, teal30_uniform, hellaswag_piqa_kl30_uniform, perlayer_sparsity_analysis, constraint_protect_late, constraint_remove_valley\n\n\\paragraph{Knowledge-Task Regression: Hypothesis.}\nWe consider two hypotheses. First, WikiText-103's limited mathematical content may bias allocation against reasoning pathways---however, a C4-trained control does not support this (see below). Second, forward KL's mode-covering property distributes mass across high-frequency patterns, potentially diluting rare activations encoding factual knowledge concentrated in specific FFN neurons~\\cite{meng2022locating}. Constraint experiments (Appendix~\\ref{app:constraint}) confirm allocation contributes: removing the learned valley improves MMLU +3.4pp and GSM8K +1.6pp. A predictor trained on C4 (diverse web text; Appendix~\\ref{app:c4_control}) does not alleviate the regression (MMLU 40.0\\%, GSM8K 4.1\\% vs.\\ 40.7\\%, 7.5\\%), confirming the deficit is structural to output-distribution KL rather than training data composition. % exp_id: constraint_remove_valley, c4_control_eval\n\nAt 50\\%, the PPL advantage widens (11.92 vs.\\ 23.90, 50\\% reduction) and generalizes to C4 (Appendix~\\ref{app:ood}), but all methods collapse to near-random on MMLU and GSM8K ($\\leq$2.7\\%); no allocation strategy recovers at this capacity limit. % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval, d030_kl50_uniform, multi_seed_kl50_global\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. $^\\ast$$2.71\\times$ KL compute (\\S\\ref{sec:isocompute}). $\\pm$: 3-seed; unmarked: s42. $^\\ddagger$Actual sparsity: KL 28.5\\% vs.\\ TEAL 29.3\\% at 30\\% (Appendix~\\ref{app:ood}).}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{6}{*}{30\\%}\n& TEAL uniform & 10.82 & 39.33 & 65.04 & \\textbf{45.86} & \\textbf{8.79} \\\\ % exp_id: teal30_uniform\n& BCE global & 11.25 & 41.2 & 66.0 & 36.3 & 6.0 \\\\ % exp_id: bce30_teal_global\n& BCE uniform & 15.09$\\pm$0.13 & 33.45 & 61.09 & 43.05 & 3.97 \\\\ % exp_id: bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456\n& MSE uniform & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 \\\\ % exp_id: mse30_3seed\n& KL global (Ours)$^\\ddagger$ & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & 8.0$\\pm$0.7 \\\\ % exp_id: kl30_3seed_global\n& KL uniform$^\\ddagger$ & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 \\\\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform\n\\midrule\n\\multirow{5}{*}{50\\%}\n& TEAL uniform & 23.90 & 27.47 & 54.38 & \\textbf{29.26} & 1.74 \\\\ % exp_id: teal50_uniform\n& BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed\n& MSE uniform & 229.26 & 25.00 & 50.59 & 23.79 & 1.59 \\\\ % exp_id: mse50_uniform_s42\n& KL global (Ours) & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & 28.3$\\pm$0.7 & \\textbf{2.7$\\pm$1.3} \\\\ % exp_id: bench_kl50_global (s42), kl50_global_s123_reeval (s123 PPL), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456)\n& KL uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\subsection{Extended Training Analysis}\n\\label{sec:isocompute}\n\nAt $2.71\\times$ KL compute budget (2700 steps, matched wall-clock), BCE achieves PPL 28.13$\\pm$0.20 (3-seed), still $2.39\\times$ worse than KL (11.79). % exp_id: bce50_3seed\nThe gap is systematic: BCE reaches higher oracle F1 (0.613 vs.\\ 0.540) with 139\\% worse PPL, confirming KL optimizes for distributional fidelity rather than magnitude agreement. % exp_id: f1_oracle_analysis, bce_isocompute_s42\n\n\n\\subsection{Mask Pattern Analysis}\n\\label{sec:mask_analysis}\n\nKL-derived masks diverge from magnitude oracles: per-layer Jaccard distance averages 68\\% at 50\\% (64 samples, 131K tokens; Figure~\\ref{fig:mask_heatmap}), with cross-seed variation (36.3\\%) confirming systematic divergence (Appendices~\\ref{app:cross_seed_jaccard},~\\ref{app:mask_viz}).\nDespite this, KL achieves PPL 11.79 vs.\\ BCE's 28.13$\\pm$0.20, confirming that distributional fidelity, not magnitude agreement, produces better masks. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap\nDivergence follows a U-shaped per-layer pattern, peaking in late layers (0.70--0.75 at 50\\%). % exp_id: c1_mask_overlap\n\n\\paragraph{Target-Swap Ablation: Target Quality vs.\\ Gradient Coupling.}\nTo disentangle whether KL's advantage stems from its coupled gradient pathway or from the mask patterns it discovers, we train a standard BCE predictor on KL-derived oracle masks instead of magnitude-based masks (C1 target-swap ablation).\nTable~\\ref{tab:c1} reports results under TEAL uniform allocation at matched sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Target-swap ablation (C1): BCE on KL-derived masks vs.\\ KL predictor (same seed), TEAL uniform. All seeds show max $\\Delta$$\\leq$1.70pp at 30\\%; max $\\Delta$$\\leq$0.79pp at 50\\% (s42). $^\\dagger$\\textbf{Provenance:} s42 oracle extracted from an earlier training run (not seed-matched); s123/s456 use seed-matched retrained oracles (Appendix~\\ref{app:oracle_provenance}).}\n\\label{tab:c1}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lllccccc}\n\\toprule\nSparsity & Seed & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{6}{*}{30\\%}\n& s42$^\\dagger$ & C1 & 9.45 & 40.27 & 67.40 & \\textbf{42.30} & \\textbf{7.58} \\\\ % exp_id: c1_ablation_30pct_s42_eval_v2\n& & KL & \\textbf{8.82} & \\textbf{40.78} & \\textbf{68.59} & 40.6 & 7.35 \\\\ % exp_id: bench_kl30_uniform\n& s123 & C1 & 8.84 & 44.71 & \\textbf{69.77} & \\textbf{39.92} & 6.82 \\\\ % exp_id: eval_c1_retrain_30pct_s123\n& & KL & \\textbf{8.83} & \\textbf{45.31} & 69.38 & 39.4 & \\textbf{7.51} \\\\ % exp_id: kl30_s123_eval\n& s456 & C1 & 8.82 & 44.71 & \\textbf{69.93} & 41.04 & 6.60 \\\\ % exp_id: eval_c1_retrain_30pct_s456\n& & KL & \\textbf{8.79} & \\textbf{45.05} & 68.75 & \\textbf{42.0} & \\textbf{7.58} \\\\ % exp_id: kl30_s456_uniform_eval\n\\midrule\n\\multirow{2}{*}{50\\%}\n& s42 & C1 & 11.96 & 32.17 & \\textbf{63.14} & 27.79 & \\textbf{2.05} \\\\ % exp_id: c1_bce_kl_targets_teal50u\n& & KL & 11.96 & \\textbf{32.59} & 62.35 & \\textbf{27.92} & 1.97 \\\\ % exp_id: c1_kl_teal50u\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt 50\\% (s42, earlier oracle), C1 matches KL within 0.79pp, while magnitude-trained BCE yields $2.4\\times$ worse PPL (Table~\\ref{tab:main}).\nAt 30\\%, retrained seeds show $\\leq$1.18pp agreement\\footnote{s42 oracle from earlier checkpoint (gap 0.65pp); s123/s456 use seed-matched converged oracles ($\\leq$0.03pp gap).}.\nC1 demonstrates that KL-discovered mask patterns \\emph{transfer} to a simpler training mechanism (PPL within 0.79pp; downstream variation up to 4.5pp MMLU); per-layer KL controls (\\S\\ref{sec:perlayer}) further show coupling contributes marginally to PPL but substantially to downstream fidelity.\nHowever, C1 also changes mask representation: binarizing oracle soft logits ($>$0) into hard masks discards ranking information, so the near-zero delta reflects transferability of binary mask \\emph{patterns} rather than full predictor knowledge. BCE+Gumbel (32.22) vs.\\ standard BCE (27.97) suggests softness alone does not explain KL's advantage, though trajectory-dependent confounds remain (Appendix~\\ref{app:oracle_provenance}). % exp_id: bce50_3seed, c1_bce_kl_targets_30u, c1_s123, bce_gumbel_no_penalty_s42, eval_bce_v3_s42\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 30\\% and 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$; uniform at 30\\%, global at 50\\%). $\\pm$: 3-seed; unmarked: s42. $^\\ddagger$STE: 20.8\\% actual sparsity at 30\\% target; loss effect ($\\Delta$PPL=20.4) is $5.1\\times$ relaxation effect ($\\Delta$PPL=3.98). $^\\S$MSE 50\\%: s42 only; s123 catastrophic (PPL{=}15{,}789; Appendix~\\ref{app:mse_config}).}\n\\label{tab:ablation}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\nConfiguration & 30\\% PPL$\\downarrow$ & 50\\% PPL$\\downarrow$ & $\\Delta_{50}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{KL-based variants}} \\\\\nForward KL + Gumbel (Ours) & \\textbf{8.81$\\pm$0.02} & \\textbf{11.79} & --- \\\\ % exp_id: kl30_ablation_s42, bench_kl50_global\nJSD (symmetric) + Gumbel & 8.90$\\pm$0.02 & 12.54 & +0.75 \\\\ % exp_id: jsd30_ablation_s42, jsd_ablation_s42\nReverse KL + Gumbel & 9.26$\\pm$0.07 & 12.80 & +1.01 \\\\ % exp_id: rkl30_ablation_s42, reverse_kl_ablation_s42\nForward KL + STE & ---$^\\ddagger$ & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-layer training}} \\\\\nPer-layer MSE & 18.52$\\pm$1.68 & 229.26$^\\S$ & +217.47 \\\\ % exp_id: mse30_uniform_s42, mse50_uniform_s42\nPer-layer KL ($K{=}1$) & 9.05$\\pm$0.02 & 34.85 & +23.06 \\\\ % exp_id: perlayer_kl_30_3seed, perlayer_kl_50_s42\nPer-layer KL ($K{=}4$) & 8.89$\\pm$0.01 & 44.23 & +32.44 \\\\ % exp_id: perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42\n\\midrule\n\\multicolumn{4}{l}{\\textit{BCE-based variants}} \\\\\nBCE (no compensation) & 15.71 & 27.97 & +16.18 \\\\ % exp_id: bce30_uniform_s42, eval_bce_v3_s42\nBCE + Gumbel (no penalty) & --- & 32.22 & +20.43 \\\\ % exp_id: bce_gumbel_no_penalty_s42\nBCE + Gumbel + Penalty & --- & 38.02 & +26.23 \\\\ % exp_id: bce_gumbel_lagrangian_isolation\nBCE + STE & --- & 60.54 & +48.75 \\\\ % exp_id: bce_ste_s42\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Relaxation, Divergence, and SPON.}\nAt 50\\%, Gumbel-Sigmoid outperforms STE~\\cite{bengio2013ste} by 33.8\\% (11.79 vs.\\ 15.77); forward KL outperforms JSD (+6.4\\%) and reverse KL (+8.6\\%), consistent with mode-covering~\\cite{gu2024minillm}. % exp_id: ste_baseline_s42, jsd_ablation_s42, reverse_kl_ablation_s42\nAt 30\\%, forward KL (8.81) and JSD (8.90) are near-identical, both outperforming reverse KL (9.26) and MSE (18.52$\\pm$1.68). % exp_id: kl30_ablation_s42, jsd30_ablation_s42, rkl30_ablation_s42, mse30_uniform_s42, mse30_3seed\nKL--JSD near-equivalence suggests the divergence measure matters less than optimizing through the output distribution; coupling scope provides additional downstream benefits (\\S\\ref{sec:perlayer}). % exp_id: bce30_uniform_s42, rkl30_downstream_3seed\n\\paragraph{Per-Layer KL: Exploratory Decomposition of Signal Type and Coupling Scope.}\n\\label{sec:perlayer}\nTo isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.\nAt $K{=}1$, per-layer KL achieves 9.05$\\pm$0.02, within 2.7\\% of end-to-end KL (8.81$\\pm$0.02), while per-layer MSE degrades to 18.52$\\pm$1.68 ($2.05\\times$ worse). For PPL, signal type\\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} may account for a substantial portion of the gap---an upper bound, as $K{=}1$ conflates coupling removal with train--inference mismatch. A 3-seed $K{=}4$ control\\footnote{Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds this (Appendix~\\ref{app:k4_downstream}): \\emph{coupling-dominated}---ARC-c (97\\% residual gap) and WG (67\\%) indicate genuine cross-layer benefits; \\emph{mismatch-dominated}---PPL (67\\% closure) and GSM8K (71\\%) largely close; \\emph{anomalous}---MMLU exceeds E2E (42.7$\\pm$1.4 vs.\\ 40.7$\\pm$1.3), explained by $K{=}4$'s near-uniform allocation matching uniform inference (Appendix~\\ref{app:constraint}). % exp_id: perlayer_kl_30_3seed, perlayer_kl_downstream, mse30_downstream_decomp, perlayer_kl_k4_3seed\nAt 50\\%, partial coupling ($K{=}4$: 44.23) is \\emph{worse} than $K{=}1$ (34.85) while E2E achieves 11.84, suggesting gradient interference under tight capacity; the decomposition is interpretable only at 30\\%. % exp_id: perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{k_curve_ppl}\n\\vspace{-8pt}\n\\caption{Coupling breadth $K$ vs.\\ perplexity (30\\%, TEAL uniform, 3-seed mean$\\pm$std). $K{=}32$ denotes end-to-end training. $K{=}2$ degradation reflects insufficient per-layer updates (${\\sim}62$ vs.\\ ${\\sim}250$ at $K{=}8$).}\n\\label{fig:k_curve_ppl}\n\\vspace{-8pt}\n\\end{figure}\n\nThe $K$-curve (Figure~\\ref{fig:k_curve_ppl}) confirms non-monotonic coupling effects: $K{=}16$ achieves the lowest PPL (8.67$\\pm$0.02 vs.\\ E2E 8.81$\\pm$0.02), yet the full coupling range (2.08 PPL) is dwarfed by the signal type gap (9.47 PPL). % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed\n\n\\paragraph{Compensation Redundancy.}\n\\label{sec:compensation}\nFastForward-style compensation~\\cite{gautam2026fastforward} (+67.2M params) provides no benefit (Appendices~\\ref{app:comp_convergence}--\\ref{app:training_convergence}). % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42, bce_comp_staged_s42, db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep\n\n\n\\subsection{Sparsity Scaling and Regime Analysis}\n\\label{sec:scaling}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_sparsity_sweep.pdf}\n\\vspace{-8pt}\n\\caption{PPL scaling with sparsity (global allocation). KL's advantage over TEAL grows with sparsity.}\n\\label{fig:sparsity_sweep}\n\\vspace{-8pt}\n\\end{figure}\n\n\\paragraph{Allocation Behavior.}\nTable~\\ref{tab:phase} (Appendix~\\ref{app:alloc_full}) reveals non-monotonic allocation preference: uniform is best at $\\leq$30\\% ($7.3\\times$ smaller MMLU $\\sigma$), global at 35--40\\%, both collapse at $\\geq$45\\%. % exp_id: kl30_3seed, regime_kl35_global, regime_kl35_uniform, multi_seed_kl50_global, multi_seed_kl50_uniform\n\n\\paragraph{Cross-Architecture and Scale.}\n\\label{sec:cross_arch}\nOn Mistral-7B-v0.3~\\cite{jiang2023mistral}, PPL generalizes ($-$17.3\\%, 3-seed; Table~\\ref{tab:mistral_downstream}); on Qwen-2.5-14B~\\cite{qwen2024qwen25}, PPL generalizes but MMLU/GSM8K decline (Table~\\ref{tab:14b}).\nThe consistent regression across scales (8B MMLU $-$5.2pp, 14B GSM8K 32.0$\\pm$5.2 vs.\\ 52.1) suggests a systematic property of output-distribution KL; Qwen's stronger reasoning baseline (GSM8K 87.6\\% vs.\\ 48.8\\% dense) may amplify sensitivity to distribution-based pruning. The pipeline adds 6.4\\% latency overhead absent sparse kernels (Appendix~\\ref{app:latency}). % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, mistral_teal30_downstream, qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform, latency_profiling\n\n",
    "structuredPatch": [
      {
        "oldStart": 61,
        "oldLines": 7,
        "newStart": 61,
        "newLines": 7,
        "lines": [
          " & TEAL uniform & 23.90 & 27.47 & 54.38 & \\textbf{29.26} & 1.74 \\\\ % exp_id: teal50_uniform",
          " & BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed",
          " & MSE uniform & 229.26 & 25.00 & 50.59 & 23.79 & 1.59 \\\\ % exp_id: mse50_uniform_s42",
          "-& KL global (Ours) & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & 28.3$\\pm$0.7 & \\textbf{2.7$\\pm$1.3} \\\\ % exp_id: bench_kl50_global (s42), kl50_global_s123_reeval (s123 PPL), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456)",
          "+& KL global (Ours) & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & 28.3$\\pm$0.7 & \\textbf{2.3$\\pm$1.1} \\\\ % exp_id: bench_kl50_global (s42 PPL=11.79), kl50_global_s123_reeval (s123 PPL=11.72), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456 PPL=11.86)",
          " & KL uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456",
          " \\bottomrule",
          " \\end{tabular}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 168_

<details open><summary>🔧 Tool call — Edit · `toolu_018HvVmHTSZLivBBoK1bRtgt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "old_string": "while E2E achieves 11.84, suggesting gradient interference",
  "new_string": "while E2E achieves 11.79, suggesting gradient interference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "b23f2b6c-3aa6-4d44-b4d7-10dccbfcd5e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g6Y39r7jBS5W46SHjbohC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 123450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3015
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-24T02:25:53.679Z_

<details><summary>↩ Tool result · `toolu_018HvVmHTSZLivBBoK1bRtgt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "acf787ac-b921-44f1-b16d-1c7cefc6d7d4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "oldString": "while E2E achieves 11.84, suggesting gradient interference",
    "newString": "while E2E achieves 11.79, suggesting gradient interference",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + GELU + Linear($128 \\to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB), using AdamW~\\cite{loshchilov2019adamw} with learning rate $1 \\times 10^{-3}$, weight decay $1 \\times 10^{-2}$, and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly\\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \\textbf{BCE predictor} (DejaVu-style~\\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; and (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison. Uniform allocation preserves downstream performance best; global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).\nAt 30\\% sparsity, output-distribution KL under uniform allocation achieves PPL 8.81$\\pm$0.02 (3-seed), a 14.5\\% reduction over TEAL at matched actual sparsity (8.81 vs.\\ 10.30, both at 28.5\\%; Appendix~\\ref{app:ood}).\nUniform allocation yields stable downstream (MMLU 40.7$\\pm$1.3\\%, 3-seed; Appendix~\\ref{app:stability}), while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%) from late-layer starvation (L31 retention 28.4\\%; \\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform, kl30_3seed\n\n\\paragraph{Task-Type Split.}\nKL shows directional improvements over TEAL on commonsense reasoning (ARC-c, WG, HellaSwag, PIQA: 4/4 wins at 30\\% uniform) but underperforms on knowledge-intensive tasks (MMLU, GSM8K: 0/2).\nWith only three seeds, 95\\% confidence intervals for individual downstream tasks overlap; we therefore treat PPL ($\\sigma{=}0.02$, non-overlapping) as the primary metric and downstream differences as directional evidence.\nThe KL predictor protects L14--L18 (14--18\\% sparsity vs.\\ 32\\% global mean) while aggressively pruning L22--L28 (48--57\\%). Constraint interventions (Appendix~\\ref{app:constraint}) confirm a task-dependent trade-off: removing the valley improves MMLU +3.4pp but reduces ARC-c by 1.5pp, consistent with localized factual associations~\\cite{geva2023dissecting}; task-aware allocation may resolve this. % exp_id: bench_kl30_uniform, teal30_uniform, hellaswag_piqa_kl30_uniform, perlayer_sparsity_analysis, constraint_protect_late, constraint_remove_valley\n\n\\paragraph{Knowledge-Task Regression: Hypothesis.}\nWe consider two hypotheses. First, WikiText-103's limited mathematical content may bias allocation against reasoning pathways---however, a C4-trained control does not support this (see below). Second, forward KL's mode-covering property distributes mass across high-frequency patterns, potentially diluting rare activations encoding factual knowledge concentrated in specific FFN neurons~\\cite{meng2022locating}. Constraint experiments (Appendix~\\ref{app:constraint}) confirm allocation contributes: removing the learned valley improves MMLU +3.4pp and GSM8K +1.6pp. A predictor trained on C4 (diverse web text; Appendix~\\ref{app:c4_control}) does not alleviate the regression (MMLU 40.0\\%, GSM8K 4.1\\% vs.\\ 40.7\\%, 7.5\\%), confirming the deficit is structural to output-distribution KL rather than training data composition. % exp_id: constraint_remove_valley, c4_control_eval\n\nAt 50\\%, the PPL advantage widens (11.92 vs.\\ 23.90, 50\\% reduction) and generalizes to C4 (Appendix~\\ref{app:ood}), but all methods collapse to near-random on MMLU and GSM8K ($\\leq$2.7\\%); no allocation strategy recovers at this capacity limit. % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval, d030_kl50_uniform, multi_seed_kl50_global\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. $^\\ast$$2.71\\times$ KL compute (\\S\\ref{sec:isocompute}). $\\pm$: 3-seed; unmarked: s42. $^\\ddagger$Actual sparsity: KL 28.5\\% vs.\\ TEAL 29.3\\% at 30\\% (Appendix~\\ref{app:ood}).}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{6}{*}{30\\%}\n& TEAL uniform & 10.82 & 39.33 & 65.04 & \\textbf{45.86} & \\textbf{8.79} \\\\ % exp_id: teal30_uniform\n& BCE global & 11.25 & 41.2 & 66.0 & 36.3 & 6.0 \\\\ % exp_id: bce30_teal_global\n& BCE uniform & 15.09$\\pm$0.13 & 33.45 & 61.09 & 43.05 & 3.97 \\\\ % exp_id: bce_iso_v3_s42, bce_iso_v3_s123, bce_iso_v3_s456\n& MSE uniform & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 \\\\ % exp_id: mse30_3seed\n& KL global (Ours)$^\\ddagger$ & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & 8.0$\\pm$0.7 \\\\ % exp_id: kl30_3seed_global\n& KL uniform$^\\ddagger$ & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 \\\\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform\n\\midrule\n\\multirow{5}{*}{50\\%}\n& TEAL uniform & 23.90 & 27.47 & 54.38 & \\textbf{29.26} & 1.74 \\\\ % exp_id: teal50_uniform\n& BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed\n& MSE uniform & 229.26 & 25.00 & 50.59 & 23.79 & 1.59 \\\\ % exp_id: mse50_uniform_s42\n& KL global (Ours) & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & 28.3$\\pm$0.7 & \\textbf{2.3$\\pm$1.1} \\\\ % exp_id: bench_kl50_global (s42 PPL=11.79), kl50_global_s123_reeval (s123 PPL=11.72), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456 PPL=11.86)\n& KL uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\subsection{Extended Training Analysis}\n\\label{sec:isocompute}\n\nAt $2.71\\times$ KL compute budget (2700 steps, matched wall-clock), BCE achieves PPL 28.13$\\pm$0.20 (3-seed), still $2.39\\times$ worse than KL (11.79). % exp_id: bce50_3seed\nThe gap is systematic: BCE reaches higher oracle F1 (0.613 vs.\\ 0.540) with 139\\% worse PPL, confirming KL optimizes for distributional fidelity rather than magnitude agreement. % exp_id: f1_oracle_analysis, bce_isocompute_s42\n\n\n\\subsection{Mask Pattern Analysis}\n\\label{sec:mask_analysis}\n\nKL-derived masks diverge from magnitude oracles: per-layer Jaccard distance averages 68\\% at 50\\% (64 samples, 131K tokens; Figure~\\ref{fig:mask_heatmap}), with cross-seed variation (36.3\\%) confirming systematic divergence (Appendices~\\ref{app:cross_seed_jaccard},~\\ref{app:mask_viz}).\nDespite this, KL achieves PPL 11.79 vs.\\ BCE's 28.13$\\pm$0.20, confirming that distributional fidelity, not magnitude agreement, produces better masks. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap\nDivergence follows a U-shaped per-layer pattern, peaking in late layers (0.70--0.75 at 50\\%). % exp_id: c1_mask_overlap\n\n\\paragraph{Target-Swap Ablation: Target Quality vs.\\ Gradient Coupling.}\nTo disentangle whether KL's advantage stems from its coupled gradient pathway or from the mask patterns it discovers, we train a standard BCE predictor on KL-derived oracle masks instead of magnitude-based masks (C1 target-swap ablation).\nTable~\\ref{tab:c1} reports results under TEAL uniform allocation at matched sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Target-swap ablation (C1): BCE on KL-derived masks vs.\\ KL predictor (same seed), TEAL uniform. All seeds show max $\\Delta$$\\leq$1.70pp at 30\\%; max $\\Delta$$\\leq$0.79pp at 50\\% (s42). $^\\dagger$\\textbf{Provenance:} s42 oracle extracted from an earlier training run (not seed-matched); s123/s456 use seed-matched retrained oracles (Appendix~\\ref{app:oracle_provenance}).}\n\\label{tab:c1}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lllccccc}\n\\toprule\nSparsity & Seed & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{6}{*}{30\\%}\n& s42$^\\dagger$ & C1 & 9.45 & 40.27 & 67.40 & \\textbf{42.30} & \\textbf{7.58} \\\\ % exp_id: c1_ablation_30pct_s42_eval_v2\n& & KL & \\textbf{8.82} & \\textbf{40.78} & \\textbf{68.59} & 40.6 & 7.35 \\\\ % exp_id: bench_kl30_uniform\n& s123 & C1 & 8.84 & 44.71 & \\textbf{69.77} & \\textbf{39.92} & 6.82 \\\\ % exp_id: eval_c1_retrain_30pct_s123\n& & KL & \\textbf{8.83} & \\textbf{45.31} & 69.38 & 39.4 & \\textbf{7.51} \\\\ % exp_id: kl30_s123_eval\n& s456 & C1 & 8.82 & 44.71 & \\textbf{69.93} & 41.04 & 6.60 \\\\ % exp_id: eval_c1_retrain_30pct_s456\n& & KL & \\textbf{8.79} & \\textbf{45.05} & 68.75 & \\textbf{42.0} & \\textbf{7.58} \\\\ % exp_id: kl30_s456_uniform_eval\n\\midrule\n\\multirow{2}{*}{50\\%}\n& s42 & C1 & 11.96 & 32.17 & \\textbf{63.14} & 27.79 & \\textbf{2.05} \\\\ % exp_id: c1_bce_kl_targets_teal50u\n& & KL & 11.96 & \\textbf{32.59} & 62.35 & \\textbf{27.92} & 1.97 \\\\ % exp_id: c1_kl_teal50u\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt 50\\% (s42, earlier oracle), C1 matches KL within 0.79pp, while magnitude-trained BCE yields $2.4\\times$ worse PPL (Table~\\ref{tab:main}).\nAt 30\\%, retrained seeds show $\\leq$1.18pp agreement\\footnote{s42 oracle from earlier checkpoint (gap 0.65pp); s123/s456 use seed-matched converged oracles ($\\leq$0.03pp gap).}.\nC1 demonstrates that KL-discovered mask patterns \\emph{transfer} to a simpler training mechanism (PPL within 0.79pp; downstream variation up to 4.5pp MMLU); per-layer KL controls (\\S\\ref{sec:perlayer}) further show coupling contributes marginally to PPL but substantially to downstream fidelity.\nHowever, C1 also changes mask representation: binarizing oracle soft logits ($>$0) into hard masks discards ranking information, so the near-zero delta reflects transferability of binary mask \\emph{patterns} rather than full predictor knowledge. BCE+Gumbel (32.22) vs.\\ standard BCE (27.97) suggests softness alone does not explain KL's advantage, though trajectory-dependent confounds remain (Appendix~\\ref{app:oracle_provenance}). % exp_id: bce50_3seed, c1_bce_kl_targets_30u, c1_s123, bce_gumbel_no_penalty_s42, eval_bce_v3_s42\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 30\\% and 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$; uniform at 30\\%, global at 50\\%). $\\pm$: 3-seed; unmarked: s42. $^\\ddagger$STE: 20.8\\% actual sparsity at 30\\% target; loss effect ($\\Delta$PPL=20.4) is $5.1\\times$ relaxation effect ($\\Delta$PPL=3.98). $^\\S$MSE 50\\%: s42 only; s123 catastrophic (PPL{=}15{,}789; Appendix~\\ref{app:mse_config}).}\n\\label{tab:ablation}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\nConfiguration & 30\\% PPL$\\downarrow$ & 50\\% PPL$\\downarrow$ & $\\Delta_{50}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{KL-based variants}} \\\\\nForward KL + Gumbel (Ours) & \\textbf{8.81$\\pm$0.02} & \\textbf{11.79} & --- \\\\ % exp_id: kl30_ablation_s42, bench_kl50_global\nJSD (symmetric) + Gumbel & 8.90$\\pm$0.02 & 12.54 & +0.75 \\\\ % exp_id: jsd30_ablation_s42, jsd_ablation_s42\nReverse KL + Gumbel & 9.26$\\pm$0.07 & 12.80 & +1.01 \\\\ % exp_id: rkl30_ablation_s42, reverse_kl_ablation_s42\nForward KL + STE & ---$^\\ddagger$ & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\n\\midrule\n\\multicolumn{4}{l}{\\textit{Per-layer training}} \\\\\nPer-layer MSE & 18.52$\\pm$1.68 & 229.26$^\\S$ & +217.47 \\\\ % exp_id: mse30_uniform_s42, mse50_uniform_s42\nPer-layer KL ($K{=}1$) & 9.05$\\pm$0.02 & 34.85 & +23.06 \\\\ % exp_id: perlayer_kl_30_3seed, perlayer_kl_50_s42\nPer-layer KL ($K{=}4$) & 8.89$\\pm$0.01 & 44.23 & +32.44 \\\\ % exp_id: perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42\n\\midrule\n\\multicolumn{4}{l}{\\textit{BCE-based variants}} \\\\\nBCE (no compensation) & 15.71 & 27.97 & +16.18 \\\\ % exp_id: bce30_uniform_s42, eval_bce_v3_s42\nBCE + Gumbel (no penalty) & --- & 32.22 & +20.43 \\\\ % exp_id: bce_gumbel_no_penalty_s42\nBCE + Gumbel + Penalty & --- & 38.02 & +26.23 \\\\ % exp_id: bce_gumbel_lagrangian_isolation\nBCE + STE & --- & 60.54 & +48.75 \\\\ % exp_id: bce_ste_s42\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Relaxation, Divergence, and SPON.}\nAt 50\\%, Gumbel-Sigmoid outperforms STE~\\cite{bengio2013ste} by 33.8\\% (11.79 vs.\\ 15.77); forward KL outperforms JSD (+6.4\\%) and reverse KL (+8.6\\%), consistent with mode-covering~\\cite{gu2024minillm}. % exp_id: ste_baseline_s42, jsd_ablation_s42, reverse_kl_ablation_s42\nAt 30\\%, forward KL (8.81) and JSD (8.90) are near-identical, both outperforming reverse KL (9.26) and MSE (18.52$\\pm$1.68). % exp_id: kl30_ablation_s42, jsd30_ablation_s42, rkl30_ablation_s42, mse30_uniform_s42, mse30_3seed\nKL--JSD near-equivalence suggests the divergence measure matters less than optimizing through the output distribution; coupling scope provides additional downstream benefits (\\S\\ref{sec:perlayer}). % exp_id: bce30_uniform_s42, rkl30_downstream_3seed\n\\paragraph{Per-Layer KL: Exploratory Decomposition of Signal Type and Coupling Scope.}\n\\label{sec:perlayer}\nTo isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.\nAt $K{=}1$, per-layer KL achieves 9.05$\\pm$0.02, within 2.7\\% of end-to-end KL (8.81$\\pm$0.02), while per-layer MSE degrades to 18.52$\\pm$1.68 ($2.05\\times$ worse). For PPL, signal type\\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} may account for a substantial portion of the gap---an upper bound, as $K{=}1$ conflates coupling removal with train--inference mismatch. A 3-seed $K{=}4$ control\\footnote{Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds this (Appendix~\\ref{app:k4_downstream}): \\emph{coupling-dominated}---ARC-c (97\\% residual gap) and WG (67\\%) indicate genuine cross-layer benefits; \\emph{mismatch-dominated}---PPL (67\\% closure) and GSM8K (71\\%) largely close; \\emph{anomalous}---MMLU exceeds E2E (42.7$\\pm$1.4 vs.\\ 40.7$\\pm$1.3), explained by $K{=}4$'s near-uniform allocation matching uniform inference (Appendix~\\ref{app:constraint}). % exp_id: perlayer_kl_30_3seed, perlayer_kl_downstream, mse30_downstream_decomp, perlayer_kl_k4_3seed\nAt 50\\%, partial coupling ($K{=}4$: 44.23) is \\emph{worse} than $K{=}1$ (34.85) while E2E achieves 11.84, suggesting gradient interference under tight capacity; the decomposition is interpretable only at 30\\%. % exp_id: perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{k_curve_ppl}\n\\vspace{-8pt}\n\\caption{Coupling breadth $K$ vs.\\ perplexity (30\\%, TEAL uniform, 3-seed mean$\\pm$std). $K{=}32$ denotes end-to-end training. $K{=}2$ degradation reflects insufficient per-layer updates (${\\sim}62$ vs.\\ ${\\sim}250$ at $K{=}8$).}\n\\label{fig:k_curve_ppl}\n\\vspace{-8pt}\n\\end{figure}\n\nThe $K$-curve (Figure~\\ref{fig:k_curve_ppl}) confirms non-monotonic coupling effects: $K{=}16$ achieves the lowest PPL (8.67$\\pm$0.02 vs.\\ E2E 8.81$\\pm$0.02), yet the full coupling range (2.08 PPL) is dwarfed by the signal type gap (9.47 PPL). % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed\n\n\\paragraph{Compensation Redundancy.}\n\\label{sec:compensation}\nFastForward-style compensation~\\cite{gautam2026fastforward} (+67.2M params) provides no benefit (Appendices~\\ref{app:comp_convergence}--\\ref{app:training_convergence}). % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42, bce_comp_staged_s42, db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep\n\n\n\\subsection{Sparsity Scaling and Regime Analysis}\n\\label{sec:scaling}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_sparsity_sweep.pdf}\n\\vspace{-8pt}\n\\caption{PPL scaling with sparsity (global allocation). KL's advantage over TEAL grows with sparsity.}\n\\label{fig:sparsity_sweep}\n\\vspace{-8pt}\n\\end{figure}\n\n\\paragraph{Allocation Behavior.}\nTable~\\ref{tab:phase} (Appendix~\\ref{app:alloc_full}) reveals non-monotonic allocation preference: uniform is best at $\\leq$30\\% ($7.3\\times$ smaller MMLU $\\sigma$), global at 35--40\\%, both collapse at $\\geq$45\\%. % exp_id: kl30_3seed, regime_kl35_global, regime_kl35_uniform, multi_seed_kl50_global, multi_seed_kl50_uniform\n\n\\paragraph{Cross-Architecture and Scale.}\n\\label{sec:cross_arch}\nOn Mistral-7B-v0.3~\\cite{jiang2023mistral}, PPL generalizes ($-$17.3\\%, 3-seed; Table~\\ref{tab:mistral_downstream}); on Qwen-2.5-14B~\\cite{qwen2024qwen25}, PPL generalizes but MMLU/GSM8K decline (Table~\\ref{tab:14b}).\nThe consistent regression across scales (8B MMLU $-$5.2pp, 14B GSM8K 32.0$\\pm$5.2 vs.\\ 52.1) suggests a systematic property of output-distribution KL; Qwen's stronger reasoning baseline (GSM8K 87.6\\% vs.\\ 48.8\\% dense) may amplify sensitivity to distribution-based pruning. The pipeline adds 6.4\\% latency overhead absent sparse kernels (Appendix~\\ref{app:latency}). % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, mistral_teal30_downstream, qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform, latency_profiling\n\n",
    "structuredPatch": [
      {
        "oldStart": 156,
        "oldLines": 7,
        "newStart": 156,
        "newLines": 7,
        "lines": [
          " \\label{sec:perlayer}",
          " To isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.",
          " At $K{=}1$, per-layer KL achieves 9.05$\\pm$0.02, within 2.7\\% of end-to-end KL (8.81$\\pm$0.02), while per-layer MSE degrades to 18.52$\\pm$1.68 ($2.05\\times$ worse). For PPL, signal type\\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} may account for a substantial portion of the gap---an upper bound, as $K{=}1$ conflates coupling removal with train--inference mismatch. A 3-seed $K{=}4$ control\\footnote{Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds this (Appendix~\\ref{app:k4_downstream}): \\emph{coupling-dominated}---ARC-c (97\\% residual gap) and WG (67\\%) indicate genuine cross-layer benefits; \\emph{mismatch-dominated}---PPL (67\\% closure) and GSM8K (71\\%) largely close; \\emph{anomalous}---MMLU exceeds E2E (42.7$\\pm$1.4 vs.\\ 40.7$\\pm$1.3), explained by $K{=}4$'s near-uniform allocation matching uniform inference (Appendix~\\ref{app:constraint}). % exp_id: perlayer_kl_30_3seed, perlayer_kl_downstream, mse30_downstream_decomp, perlayer_kl_k4_3seed",
          "-At 50\\%, partial coupling ($K{=}4$: 44.23) is \\emph{worse} than $K{=}1$ (34.85) while E2E achieves 11.84, suggesting gradient interference under tight capacity; the decomposition is interpretable only at 30\\%. % exp_id: perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global",
          "+At 50\\%, partial coupling ($K{=}4$: 44.23) is \\emph{worse} than $K{=}1$ (34.85) while E2E achieves 11.79, suggesting gradient interference under tight capacity; the decomposition is interpretable only at 30\\%. % exp_id: perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global",
          " ",
          " \\begin{figure}[t]",
          " \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 170_

<details open><summary>🔧 Tool call — Edit · `toolu_011VJ5MUgeeGzHbRfk4MtrtG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "old_string": "& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval",
  "new_string": "& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "4876bc26-1b74-4c7b-8261-10c7dcca4b7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g6Y39r7jBS5W46SHjbohC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 123450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3015
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-24T02:25:55.391Z_

<details><summary>↩ Tool result · `toolu_011VJ5MUgeeGzHbRfk4MtrtG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "ee2761c3-486a-4389-8c1e-4e158fde1ed2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "oldString": "& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval",
    "newString": "& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval",
    "originalFile": "\\appendix\n\n\\section{Inference Efficiency}\n\\label{app:latency}\n\nTable~\\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Sparsity & ms/fwd & tok/s & Overhead \\\\\n\\midrule\nDense & 0\\% & 119.11$\\pm$0.57 & 17{,}195 & --- \\\\\n\\midrule\nKL predictor-only & 30\\% & 126.64$\\pm$0.70 & 16{,}172 & +6.3\\% \\\\ % exp_id: latency_bench\nKL predictor-only & 50\\% & 126.78$\\pm$0.31 & 16{,}154 & +6.4\\% \\\\ % exp_id: latency_bench\n\\midrule\nPredictor + compensation & 30\\% & 129.94$\\pm$0.75 & 15{,}761 & +9.1\\% \\\\ % exp_id: latency_bench\nPredictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full KL-sparse pipeline adds 6.4\\% overhead to dense inference (126.78 vs.\\ 119.11\\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\\,ms (2.7\\%); the remainder arises from mask application and sparse FFN indexing.\nEliminating the compensation network saves an additional $\\sim$2.7\\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.\nThe overhead is near-identical at 30\\% and 50\\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.\n\nNote that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.\nThe pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\nOur contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.\n\n\n\\section{Predictor Bottleneck Sensitivity}\n\\label{app:db_sensitivity}\n\nTable~\\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Predictor bottleneck sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}\n\\label{tab:db_sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$d_b$ & Params & TEAL global & $\\Delta$ & Per-token \\\\\n\\midrule\n64 & 38.2M (0.48\\%) & 12.076 & +0.9\\% & 10.16 \\\\ % exp_id: db_sensitivity_sweep\n128 & 75.9M (0.95\\%) & 11.963 & --- & 9.218 \\\\ % exp_id: db_sensitivity_sweep\n256 & 151.5M (1.89\\%) & 12.105 & +1.2\\% & 8.586 \\\\ % exp_id: db_sensitivity_sweep\n512 & 302.5M (3.77\\%) & 12.315 & +2.9\\% & 7.93 \\\\ % exp_id: db_sensitivity_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\\to$7.93).\nThis divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.\nThe $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\n\n\\subsection{Temperature Schedule Sensitivity}\n\\label{app:tau_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature schedule sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:tau_sensitivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n$\\tau$ Schedule & PPL$\\downarrow$ \\\\\n\\midrule\nFixed $\\tau{=}0.5$ & \\textbf{11.861} \\\\ % exp_id: tau_schedule_sweep\nLinear $1.0 \\to 0.1$ (default) & 11.963 \\\\ % exp_id: tau_schedule_sweep\nFixed $\\tau{=}0.1$ & 12.072 \\\\ % exp_id: tau_schedule_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature schedule has minimal impact ($<$1.8\\% PPL variation).\nThe linear annealing default is a conservative choice; even removing annealing entirely (fixed $\\tau{=}0.5$) yields comparable performance.\n\n\\subsection{Training Convergence}\n\\label{app:training_convergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training convergence at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:training_convergence}\n\\small\n\\begin{tabular}{cc}\n\\toprule\nSteps & PPL$\\downarrow$ \\\\\n\\midrule\n200 & 15.158 \\\\ % exp_id: training_steps_sweep\n400 & 12.538 \\\\ % exp_id: training_steps_sweep\n600 & 12.046 \\\\ % exp_id: training_steps_sweep\n800 & 11.907 \\\\ % exp_id: training_steps_sweep\n1000 & \\textbf{11.906} \\\\ % exp_id: training_steps_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining converges rapidly: 95\\% of the quality gap closes by step 600, and performance saturates by step 800 ($\\Delta < 0.001$ between 800 and 1000 steps).\nOur default of 1000 steps provides a conservative margin.\n\n\n\\section{Geometric Penalty Schedule Dynamics}\n\\label{app:lagrangian}\n\nTable~\\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.\nThe geometric doubling pattern ($1 \\to 2 \\to 4 \\to 8 \\to \\ldots$) enables $\\lambda$ to reach steady state within $\\sim$10 steps; the deadzone ($\\epsilon = 0.02$) then stabilizes $\\lambda$ once actual sparsity is within $\\pm$2\\% of the target.\n\n\\begin{table}[h]\n\\centering\n\\caption{Geometric penalty schedule convergence across sparsity targets (margin $\\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}\n\\label{tab:lagrangian}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTarget $\\rho$ & $\\lambda_{\\max}$ & Final $\\lambda$ & Actual sparsity & Deviation \\\\\n\\midrule\n30\\% & 5000 & 5000 (cap) & 0.285 & 5.0\\% \\\\ % exp_id: kl_30pct_s42\n40\\% & 5000 & 625 & 0.398 & 0.5\\% \\\\ % exp_id: kl_40pct_s42\n50\\% & 1000 & 8 & 0.504 & 0.8\\% \\\\ % exp_id: kl_50pct_s42\n70\\% & 1000 & 1000 (cap) & 0.688 & 1.7\\% \\\\ % exp_id: kl_70pct_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 50\\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.\nAt 30\\% and 70\\%, the gap between the gate prior and target is larger, driving $\\lambda$ to its respective caps.\nThe 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation; this precision reflects a regime where the target is reachable without $\\lambda$ saturation.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{lagrangian_dynamics.pdf}\n\\caption{Lagrangian controller dynamics for 30\\% sparsity target ($\\lambda_{\\max}=5000$). Left axis (log scale): penalty weight $\\lambda$ rises from $0.01$ to its cap once actual sparsity undershoots the target at $\\sim$step~150, exhibiting bang-bang oscillations before saturating. Right axis: actual sparsity (solid) converges from the natural density ($\\approx$0.41) toward the target (dashed) and stabilizes near 0.28.}\n\\label{fig:lagrangian_dynamics}\n\\end{figure}\n\nTemperature $\\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.\nA mild loss increase in the final $\\sim$100 steps is expected: as masks become more binary ($\\tau \\to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.\n\nThe controller reliably drives actual sparsity to within 5\\% of the target across all tested regimes, with $\\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.\nFor the 30\\% target, actual sparsity is $\\approx$28.5\\% (5\\% deviation). This does not affect conclusions: TEAL at 28.5\\% actual sparsity yields PPL 10.30 (vs.\\ 10.97 at exact 30\\%), a 0.67 PPL difference negligible relative to the KL vs.\\ TEAL gap (8.96 vs.\\ 10.97).\n\n\n\\section{Out-of-Distribution Evaluation}\n\\label{app:ood}\n\nTo address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\\cite{raffel2020c4} validation set under TEAL global allocation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Out-of-distribution evaluation on C4 validation (PPL$\\downarrow$). 30\\% KL reports 2-seed mean$\\pm$std; other entries use seed 42.}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{llc}\n\\toprule\nSparsity & Method & C4 PPL$\\downarrow$ \\\\\n\\midrule\n0\\% & Dense & 9.21 \\\\\n\\midrule\n30\\% & KL predictor (Ours) & \\textbf{16.03$\\pm$0.01} \\\\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123\n\\midrule\n\\multirow{2}{*}{50\\%} & KL predictor (Ours) & \\textbf{18.40} \\\\ % exp_id: eval_c4_ood_kl50\n& TEAL vanilla & 38.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the 30\\% sparsity level, the KL predictor achieves C4 PPL 16.03$\\pm$0.01 (2-seed, global allocation, $1.74\\times$ dense), confirming OOD generalization.\nAt 50\\%, the KL predictor achieves 52.5\\% relative advantage over TEAL (18.40 vs.\\ 38.75), comparable to the 50\\% advantage on WikiText-2 (11.92 vs.\\ 23.90), confirming that KL-trained predictions generalize across distributions.\n\n\\paragraph{Uniform Allocation.}\nUnder uniform allocation at 30\\%, C4 PPL across three seeds is 18.22 (s42), 16.37 (s123), 16.36 (s456), yielding mean 16.98$\\pm$1.07 ($1.84\\times$ dense). % exp_id: c4_ood_kl30_uniform_3seed\nThe cross-seed variance is substantially higher than in-domain: CV=6.3\\% on C4 vs.\\ 0.2\\% on WikiText-2 (PPL 8.81$\\pm$0.02), driven by seed 42's elevated C4 PPL (18.22 vs.\\ 16.37 for other seeds).\nGlobal allocation's cross-layer budget flexibility partially compensates for domain shift (PPL 16.03 global vs.\\ 16.98 uniform), consistent with the Limitations observation that the predictor partially overfits to training-domain activation patterns.\n\n\\paragraph{Downstream Task Robustness.}\nTable~\\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\\ WikiText (in-domain), both at 30\\% uniform allocation (seed 42). All six benchmarks show $\\Delta$$\\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream task robustness to calibration domain shift (KL 30\\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\\_match (GSM8K).}\n\\label{tab:ood_downstream}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nCalibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nWikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\\\ % exp_id: c4_ood_downstream_kl30\n\\midrule\n$\\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Layer Retention Analysis}\n\\label{app:retention}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{per_layer_retention_chart.pdf}\n\\caption{Per-layer neuron retention under global top-$k$ allocation at 30\\%, 50\\%, and 70\\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\\% (L31) even at 30\\% sparsity. At 70\\%, starvation extends to mid-layers (L10--12: 16.7--20.1\\%), explaining the transition to the capacity-limited regime.}\n\\label{fig:retention}\n\\end{figure}\n\n\n\\section{Training Stability}\n\\label{app:stability}\n\nThree-seed evaluation ($s \\in \\{42, 123, 456\\}$) at 50\\% sparsity under uniform allocation yields PPL $11.92 \\pm 0.07$ (CV=0.6\\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform\nDownstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\n\nUnder global allocation at 50\\%, MMLU is $28.3 \\pm 0.7$\\%; the near-random performance is capacity-limited rather than seed-sensitive ($\\sigma$=0.7pp vs.\\ 9.5pp at 30\\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\nThe low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.\n\n\\subsection{Cross-Seed Mask Consistency}\n\\label{app:cross_seed_jaccard}\n\nTo assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30\n\nThe mean cross-seed Jaccard distance is 0.363 (IoU = 0.637), substantially lower than the KL-vs-magnitude divergence (0.46--0.68), confirming that KL-discovered patterns form a distinct cluster from magnitude-based masks.\nPer-layer divergence follows a U-shaped pattern: lowest at embedding-adjacent layers (L0: 0.33), peaking at early layers (L1: 0.41), with a mid-network valley (L12--14: 0.33). The random baseline Jaccard distance is 0.462.\n\nWhile specific mask configurations vary moderately across seeds (Jaccard distance 36.3\\%), the resulting PPL is highly stable (8.81$\\pm$0.02, CV=0.2\\%), suggesting multiple near-equivalent optima in the activation mask space.\nThe cross-seed divergence (36.3\\%) is substantially lower than the KL-vs-magnitude divergence (46--68\\%), confirming that KL discovers effective patterns that cluster distinctly from magnitude-based selection.\n\n\n\\section{MSE Baseline Configuration}\n\\label{app:mse_config}\n\nThe MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\\times}10^{-3}$, weight decay $1{\\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\\tau$: $1.0 \\to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.\nThe only difference is the loss target: per-layer $\\|\\mathbf{W}_d^{(\\ell)}(\\tilde{\\mathbf{m}}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}) - \\mathbf{y}_{\\text{dense}}^{(\\ell)}\\|_2^2$, replacing the end-to-end KL divergence.\nThis controlled comparison isolates the effect of output-distribution alignment: all three predictors see identical data in identical order with identical architectures; only the loss function differs. % exp_id: mse30_uniform_s42, mse50_uniform_s42\n\nMSE uses $\\lambda_{\\max}{=}1000$ (vs.\\ KL's 5000) because MSE's per-layer gradient magnitude is approximately $5\\times$ larger than KL's end-to-end gradient, requiring proportionally less penalty pressure to achieve comparable sparsity control. Both reach their target sparsity within 110 steps.\nAt 50\\% target, MSE converges to the target sparsity for seed 42; however, with seed 123, sparsity reaches only 5.1\\% under the same $\\lambda_{\\max}$ cap (eval PPL$=$15{,}789, random-level), indicating high sensitivity to initialization---a failure mode not observed with KL-based losses.\nAt 30\\%, MSE achieves 27.7\\% actual sparsity for s42 (gap 2.3pp).\nThe 3-seed MSE mean (18.52$\\pm$1.68; s42=20.43, s123=17.73, s456=17.39) is still $1.7\\times$ worse than TEAL (10.82), confirming that the performance deficit stems from the loss function, not insufficient sparsity pressure.\n\n\n\\section{Extended SNR Analysis}\n\\label{app:snr_extended}\n\nFigure~\\ref{fig:snr_trajectory} plots gradient SNR across the full 1000-step training for both KL and BCE predictors, measured at 14 checkpoints (LLaMA-3.1-8B, C4) with 95\\% bootstrap confidence intervals.\nFrom step 100 onward, BCE maintains consistently higher SNR than KL (2.3--17$\\times$ depending on training phase), with the gap narrowing toward convergence ($2.3\\times$ at step 1000: $2.026{\\times}10^{-3}$ vs.\\ $8.78{\\times}10^{-4}$). % exp_id: snr_full_curve_1000steps\nDespite KL's noisier gradient signal, KL-trained predictors produce substantially better masks (Table~\\ref{tab:main}), confirming that \\emph{target alignment} matters more than gradient clarity for mask quality.\nBCE's higher SNR reflects its simpler per-neuron classification objective, which concentrates gradients on individual neuron decisions; KL's coupled gradient distributes signal across all mask decisions jointly, yielding lower SNR but discovering compositionally superior mask patterns (\\S\\ref{sec:method:gradient}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{snr_trajectory.pdf}\n\\caption{Gradient SNR trajectory across 1000 training steps. BCE (orange) maintains consistently higher SNR than KL (blue) from step 100 onward (2.3--17$\\times$), yet KL produces superior masks (Table~\\ref{tab:main}), suggesting that target alignment matters more than gradient clarity for mask quality.}\n\\label{fig:snr_trajectory}\n\\end{figure}\n\n\n\\section{Extended Downstream Evaluation}\n\\label{app:downstream}\n\nTable~\\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\\% uniform: 3-seed mean$\\pm$std; others: seed 42.}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Method & HellaSwag & PIQA \\\\\n\\midrule\n0\\% & Dense & \\textbf{82.35} & \\textbf{80.90} \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& KL uniform & \\textbf{71.07$\\pm$0.54} & \\textbf{74.95$\\pm$0.25} \\\\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)\n& TEAL uniform & 63.31 & 72.80 \\\\ % exp_id: bench_teal30_uniform_6task\n& BCE isocompute & 62.81 & 74.21 \\\\ % exp_id: bce_isocompute_30u_hellaswag_piqa\n\\midrule\n\\multirow{3}{*}{50\\%}\n& KL global & \\textbf{58.95} & \\textbf{69.48} \\\\ % exp_id: hellaswag_piqa_kl50_global\n& KL uniform & 56.66 & 69.10 \\\\ % exp_id: hellaswag_piqa_kl50_uniform\n& TEAL uniform & 39.35 & 63.66 \\\\ % exp_id: bench_teal50_uniform_6task\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 30\\%, the KL predictor retains 86.3\\% of dense HellaSwag accuracy (71.07$\\pm$0.54 vs.\\ 82.35, 3-seed) and 92.6\\% of PIQA (74.95$\\pm$0.25 vs.\\ 80.90), confirming moderate degradation on non-reasoning tasks.\nAt 50\\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\\S\\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).\n\n\n\\section{Compensation Training Convergence}\n\\label{app:comp_convergence}\n\nAll compensation networks~\\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\\% s42 (final loss 0.70), 30\\% s456 (0.68), 50\\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42\n\n\n\\section{Qwen-2.5-14B Detailed Results}\n\\label{app:14b}\n\n\\begin{table}[h]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% nominal sparsity. Actual sparsity differs: KL 29.6\\% (3-seed), TEAL 29.3\\% (target 30\\%). \\textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\\% native sparsity (\\S\\ref{sec:method:gradient}), so forced global top-$k$ is used.}\n\\label{tab:14b}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \\textbf{75.01} & \\textbf{77.37} \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 & 70.51 & 74.70 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} & 53.43 & 68.28 \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{8}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.90} & 53.50 & \\textbf{72.82} & 63.55 & 32.0$\\pm$5.2 & \\textbf{72.68$\\pm$0.2} & \\textbf{76.01$\\pm$1.1} \\\\ % exp_id: qwen14b_kl30_uniform (3-seed s42/s123/s456)\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & \\textbf{52.1} & 67.72 & 74.70 \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nUnder global allocation, BCE's HellaSwag drops to 53.43\\% ($-$17pp vs.\\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval\n\n\\section{Full Allocation Analysis}\n\\label{app:alloc_full}\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation summary (LLaMA-3.1-8B). $\\pm$: 3-seed; $^\\ast$high seed variance.}\n\\label{tab:phase}\n\\footnotesize\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & MMLU \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & 35.7$\\pm$9.5$^\\ast$ \\\\ % exp_id: kl30_3seed_global\n& Uniform & \\textbf{8.81$\\pm$0.02} & \\textbf{40.7$\\pm$1.3} \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\n& Uniform & 11.92$\\pm$0.07 & 28.0$\\pm$0.6 \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:phase_full} extends Table~\\ref{tab:phase} with all downstream metrics.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Full allocation analysis: global top-$k$ vs.\\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); others: seed 42. $^\\ast$High MMLU seed variance (individual seeds span 25.3--43.5\\%).}\n\\label{tab:phase_full}\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{2}{*}{25\\%}\n& Global & \\textbf{8.17} & 45.4 & 70.6 & \\textbf{46.6} & \\textbf{11.5} \\\\\n& Uniform & 8.23 & \\textbf{46.5} & \\textbf{71.8} & 44.0 & 11.0 \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5$^\\ast$ & \\textbf{8.0$\\pm$0.7} \\\\\n& Uniform & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & \\textbf{40.7$\\pm$1.3} & 7.5$\\pm$0.1 \\\\\n\\midrule\n\\multirow{2}{*}{35\\%}\n& Global & \\textbf{9.31} & \\textbf{38.9} & \\textbf{67.6} & \\textbf{40.4} & \\textbf{7.7} \\\\\n& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\\\\n\\midrule\n\\multirow{2}{*}{40\\%}\n& Global & \\textbf{10.14} & 39.5 & \\textbf{67.5} & \\textbf{39.5} & \\textbf{6.6} \\\\\n& Uniform & 10.76 & \\textbf{39.6} & 63.1 & 35.5 & 3.6 \\\\\n\\midrule\n\\multirow{2}{*}{45\\%}\n& Global & \\textbf{10.80} & \\textbf{39.2} & \\textbf{64.6} & 30.4 & \\textbf{3.0} \\\\\n& Uniform & 10.95 & 37.6 & 63.6 & \\textbf{30.6} & 2.7 \\\\\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.7$\\pm$1.3} \\\\\n& Uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Mask Pattern Visualization}\n\\label{app:mask_viz}\n\nFigure~\\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity.\nFigure~\\ref{fig:scatter} shows per-neuron importance scores at layer 16.\nFigure~\\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{neuron_scatter_layer16.pdf}\n\\caption{KL vs.\\ magnitude importance scores for layer 16 neurons at 50\\% sparsity. 41\\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}\n\\label{fig:scatter}\n\\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_divergence_heatmap.pdf}\n\\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\\%) and increases with sparsity across all layers.}\n\\label{fig:mask_heatmap}\n\\end{figure*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_comparison.pdf}\n\\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\\% and 50\\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\\%, 0.74 at 50\\%).}\n\\label{fig:mask_comparison}\n\\end{figure*}\n\n\n\\section{Cross-Architecture Comparison}\n\\label{app:cross_arch}\n\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. \\textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\\%: 3-seed mean$\\pm$std; other rows: seed 42.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.93$\\pm$0.19} & 8.38 & 1.21$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL PPL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity).\nTable~\\ref{tab:mistral_downstream} reports downstream task accuracy at 30\\% sparsity on Mistral-7B-v0.3 (3-seed). KL improves PPL ($-$17.3\\%) and commonsense tasks (WG +6.7pp) but MMLU is tied (43.3\\% vs.\\ 43.5\\%); ARC-c shows high seed variance ($\\sigma$=6.4pp); GSM8K reverses.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B-v0.3 downstream evaluation at 30\\% sparsity. $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); TEAL is deterministic (single run). ARC-c exhibits high seed variance ($\\sigma$=6.4pp).}\n\\label{tab:mistral_downstream}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\\\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa\nKL 30\\% & \\textbf{6.93$\\pm$0.19} & \\textbf{44.9$\\pm$6.4} & \\textbf{70.2$\\pm$1.2} & \\textbf{69.7$\\pm$0.8} & \\textbf{74.8$\\pm$0.4} & 43.3$\\pm$1.5 & 8.6$\\pm$2.2 \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456\nTEAL 30\\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & \\textbf{43.5} & \\textbf{15.9} \\\\ % exp_id: mistral_teal30_downstream\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Taxonomy Discussion}\n\\label{app:taxonomy}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2025spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-token} methods~\\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass; each mask decision's gradient reflects its joint effect with all other masks on the final distribution.\n\nSPON~\\cite{xu2025spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\\times$ coupled).\nDejaVu~\\cite{liu2023dejavu} and FastForward~\\cite{gautam2026fastforward} achieve per-token granularity but use BCE, where each neuron's gradient is independent of other mask states.\nD2DMoE~\\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.\nWe define \\emph{output-distribution alignment} as whether the training loss optimizes a quantity that composes across layers.\nKL on output logits directly optimizes next-token prediction loss, which does not suffer from error composition; per-layer MSE minimizes reconstruction error independently at each layer, but layer-wise optima do not compose---a mask minimizing FFN output error at layer $\\ell$ may amplify errors in layers $\\ell{+}1 \\ldots L$.\nThe SNR analysis (\\S\\ref{sec:method:gradient}) corroborates this: KL achieves the best masks despite $2.3\\times$ lower SNR than BCE, while MSE produces the worst masks.\nThe framework predicts that losses operating on output-level quantities should outperform intermediate-level losses, a hypothesis consistent with our MSE results and testable with alternative output-level objectives.\n\n\\section{Oracle Mask Provenance}\n\\label{app:oracle_provenance}\n\nC1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold (logits $> 0$, equivalent to $\\sigma > 0.5$); they reflect one specific training trajectory (optimizer state, data order, Gumbel noise).\nThe s42/s123/s456 consistency ($\\leq$1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.\n\n\\section{SPON Orthogonality}\n\\label{app:spon}\n\nSPON~\\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\nThe decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.\n\n\\section{Per-Layer KL Downstream Decomposition}\n\\label{app:perlayer_downstream}\n\nTable~\\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\\ coupling scope decomposition at 30\\% sparsity (\\S\\ref{sec:perlayer}). BoolQ's $\\approx$100\\% coupling is an upper bound confounded by high cross-seed variance ($\\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.\n\n\\begin{table}[h]\n\\centering\n\\caption{2D decomposition at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \\S\\ref{sec:perlayer}).}\n\\label{tab:perlayer_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\n& PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\\\\n\\midrule\nE2E KL & 8.81$\\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\\\\nPer-layer KL & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\\\\nMSE & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 & 64.5$\\pm$5.3 \\\\\n\\midrule\nTotal gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\\\\nSignal type (\\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\\approx$0 \\\\\nCoupling (\\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\\approx$100 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{$K{=}4$ Mismatch Control}\n\\label{app:k4_downstream}\n\nTable~\\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\\% sparsity.\nTraining with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\\ 1/32 layers masked during training, while inference applies all 32).\nThe gap closure column reports the fraction of the $K{=}1 \\to$ E2E KL gap closed by $K{=}4$.\n\n\\begin{table}[h]\n\\centering\n\\caption{3-seed $K{=}4$ mismatch control at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \\in \\{42, 123, 456\\}$). Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\\text{E2E} - K{=}1) \\times 100$.}\n\\label{tab:k4_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\n& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\\%) \\\\\n\\midrule\nPPL$\\downarrow$ & 8.89$\\pm$0.01 & 9.05$\\pm$0.02 & 8.81$\\pm$0.02 & 66.7 \\\\\nARC-c & 40.0$\\pm$1.3 & 39.9 & 43.7$\\pm$2.5 & 2.6 \\\\\nWG & 66.9$\\pm$0.2 & 65.9 & 68.9$\\pm$0.4 & 33.3 \\\\\nMMLU$^\\ast$ & 42.7$\\pm$1.4 & 38.6 & 40.7$\\pm$1.3 & $>$100 \\\\\nGSM8K & 7.0$\\pm$1.6 & 5.8 & 7.5$\\pm$0.1 & 70.6 \\\\\nBoolQ$^\\dagger$ & 67.7$\\pm$7.5 & 64.5$\\pm$11.5 & 73.7 & 34.8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize $^\\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\\% (Appendix~\\ref{app:constraint}).\n$^\\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}\n\\end{table}\n\n\\section{Per-Layer Sparsity Constraint Analysis}\n\\label{app:constraint}\n\nTo test the causal role of the KL predictor's learned per-layer allocation, we evaluate two inference-time interventions at 30\\% overall sparsity (seed 42, uniform allocation baseline):\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity constraint analysis. \\emph{Protect late}: cap L22--L28 sparsity $\\leq$30\\%; \\emph{Remove valley}: override L14--L18 sparsity to 30\\%. Budget redistributed to maintain 30\\% overall.}\n\\label{tab:constraint}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & PPL & ARC-c & MMLU & GSM8K \\\\\n\\midrule\nKL baseline (s42) & 8.82 & 40.8 & 40.6 & 7.4 \\\\\nProtect late layers & 9.26 & 42.4 & 40.7 & 6.5 \\\\\nRemove valley & 8.76 & 39.3 & 44.0 & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nProtecting late layers (L22--L28) does not improve knowledge-intensive metrics despite reducing their sparsity from 48--57\\% to $\\leq$30\\%, while worsening PPL by 5.2\\%.\nConversely, removing the protection valley (forcing L14--L18 to 30\\% instead of 14--18\\%) improves MMLU by +3.4pp and GSM8K by +1.6pp at the cost of ARC-c $-$1.5pp.\nThe KL predictor's learned allocation thus represents a task-dependent trade-off---prioritizing commonsense reasoning via middle-layer protection---rather than a uniformly optimal pattern.\nThis allocation trade-off also explains the $K{=}4$ MMLU anomaly (\\S\\ref{app:k4_downstream}): $K{=}4$'s near-uniform learned sparsity (std=0.003) inherently removes the valley, producing MMLU=43.5 comparable to the remove-valley condition (44.0).\n\n\\section{Per-Layer Sparsity Distribution}\n\\label{app:perlayer_sparsity}\n\nThe KL predictor at 30\\% target sparsity learns a non-uniform per-layer allocation that differs markedly from magnitude-based selection.\nAggregate sparsity is similar across broad regions (early L0--L7: KL 28.1\\% vs.\\ magnitude 27.5\\%; late L24--L31: 44.9\\% vs.\\ 47.2\\%), but middle layers (L8--L23) exhibit high internal variance despite similar averages (28.2\\% vs.\\ 27.3\\%).\nTable~\\ref{tab:perlayer_sparsity} highlights three sub-ranges.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity sub-ranges: KL predictor vs.\\ magnitude (LLaMA-3.1-8B, 30\\%, uniform allocation). Ranges denote min--max across layers in each group.}\n\\label{tab:perlayer_sparsity}\n\\begin{tabular}{lccc}\n\\toprule\nLayer Range & KL (\\%) & Mag (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nL8--L12 (high pruning) & 32--36 & 25--26 & $+$7 to $+$10 \\\\\nL14--L18 (protection valley) & 14--18 & 28--30 & $-$8 to $-$16 \\\\\nL22--L28 (aggressive pruning) & 48--57 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{C4 Training Data Control}\n\\label{app:c4_control}\n\nTo test whether WikiText-103's narrow domain drives the knowledge-task regression (\\S\\ref{sec:experiments}), we train the KL predictor on C4~\\cite{raffel2020c4} (diverse web text) under identical hyperparameters (1000 steps, 30\\% uniform, s42).\n\n\\begin{table}[h]\n\\centering\n\\caption{C4-trained vs.\\ WikiText-trained KL predictor (LLaMA-3.1-8B, 30\\% uniform, s42).}\n\\label{tab:c4_control}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\nTraining Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\\n\\midrule\nWikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe C4-trained predictor achieves comparable MMLU (40.0\\% vs.\\ 40.6\\%) but worse GSM8K (4.1\\% vs.\\ 7.4\\%) and higher PPL (11.55 vs.\\ 8.82), despite training on more diverse text.\nThis rules out training data composition as the primary cause of knowledge-task regression and supports the hypothesis that forward KL's mode-covering property structurally under-protects rare reasoning-critical activations. % exp_id: c4_control_eval\n\n\\section{Per-Layer Coupling Breadth Analysis}\n\\label{app:k_curve}\n\nWe vary the number of layers coupled per training step ($K$) from 1 (pure per-layer) to 32 (end-to-end), evaluating all predictors under TEAL uniform allocation at 30\\% sparsity on LLaMA-3.1-8B.\n\n\\begin{table}[h]\n\\centering\n\\caption{K-curve: coupling breadth vs.\\ predictor quality (30\\%, TEAL uniform, LLaMA-3.1-8B). All values are 3-seed mean$\\pm$std (s42/s123/s456) except $K{=}1$ downstream (single seed). ``---'' = not evaluated.}\n\\label{tab:k_curve}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{cccccccc}\n\\toprule\n$K$ & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\n1 & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & --- & --- \\\\\n2 & 10.75$\\pm$0.15 & 39.7$\\pm$1.2 & 63.2$\\pm$1.7 & 38.3$\\pm$3.2 & 2.8$\\pm$0.6 & 66.5$\\pm$1.0 & 73.5$\\pm$0.7 \\\\\n4 & 8.89$\\pm$0.01 & 40.0$\\pm$1.2 & 66.9$\\pm$0.2 & 42.7$\\pm$1.4 & 7.0$\\pm$1.6 & 67.8$\\pm$1.0 & 74.5$\\pm$0.5 \\\\\n8 & 9.00$\\pm$0.06 & 40.7$\\pm$1.0 & 68.7$\\pm$1.3 & 40.4$\\pm$0.6 & 6.8$\\pm$1.3 & 69.0$\\pm$1.1 & 75.1$\\pm$1.1 \\\\\n16 & 8.67$\\pm$0.02 & 41.9$\\pm$1.1 & 68.5$\\pm$0.9 & 40.9$\\pm$2.9 & 8.5$\\pm$1.2 & 70.1$\\pm$0.4 & 75.0$\\pm$0.8 \\\\\n32 (E2E) & 8.81$\\pm$0.02 & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nPPL exhibits a non-monotonic U-shape (Figure~\\ref{fig:k_curve_ppl}): $K{=}2$ is worst (10.75$\\pm$0.15), likely due to insufficient per-layer updates (${\\sim}$62 updates/layer vs.\\ ${\\sim}$250 at $K{=}8$). $K{=}16$ achieves the lowest PPL (8.67$\\pm$0.02), marginally better than E2E (8.81$\\pm$0.02). $K{=}16$ MMLU exhibits high seed variance (std=2.9; s42=44.0, s123=40.0, s456=38.7), with the 3-seed mean (40.9) indistinguishable from E2E (40.7$\\pm$1.3).\nThe signal type gap ($K{=}1$ KL 9.05 vs.\\ per-layer MSE 18.52$\\pm$1.68) of 9.47 PPL dwarfs the coupling breadth range within KL (best $K{=}16$ 8.67 vs.\\ worst $K{=}2$ 10.75 = 2.08 PPL), reinforcing that output-distribution alignment, not coupling scope, is the primary quality lever for PPL at this sparsity level. % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed, perlayer_kl_30_3seed, perlayer_kl_k4_3seed\n\n\\section{Licenses}\n\\label{app:licenses}\n\nLLaMA-3.1-8B is released under the Llama 3.1 Community License Agreement.\nMistral-7B-v0.3 is released under the Apache 2.0 License.\nQwen-2.5-14B is released under the Apache 2.0 License.\nWikiText-103 and WikiText-2~\\cite{merity2017pointer} are released under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).\nAll evaluation benchmarks (ARC, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA) are publicly available under their respective licenses.\nOur code will be released under the MIT License upon acceptance.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 347,
        "oldLines": 7,
        "newStart": 347,
        "newLines": 7,
        "lines": [
          " & Uniform & \\textbf{8.81$\\pm$0.02} & \\textbf{40.7$\\pm$1.3} \\\\ % exp_id: bench_kl30_uniform",
          " \\midrule",
          " \\multirow{2}{*}{50\\%}",
          "-& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval",
          "+& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval",
          " & Uniform & 11.92$\\pm$0.07 & 28.0$\\pm$0.6 \\\\ % exp_id: multi_seed_kl50_uniform",
          " \\bottomrule",
          " \\end{tabular}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 172_

<details open><summary>🔧 Tool call — Edit · `toolu_01CgKs8ZLbewoNrKsLy5JMqd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "old_string": "& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.7$\\pm$1.3} \\\\",
  "new_string": "& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.3$\\pm$1.1} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "2cb21574-a889-48ca-a3d9-77e32e4cb14f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019g6Y39r7jBS5W46SHjbohC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 123450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3015
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-24T02:25:57.397Z_

<details><summary>↩ Tool result · `toolu_01CgKs8ZLbewoNrKsLy5JMqd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "bd8779f3-93b6-47f1-a698-49704d99a447",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "oldString": "& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.7$\\pm$1.3} \\\\",
    "newString": "& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.3$\\pm$1.1} \\\\",
    "originalFile": "\\appendix\n\n\\section{Inference Efficiency}\n\\label{app:latency}\n\nTable~\\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Sparsity & ms/fwd & tok/s & Overhead \\\\\n\\midrule\nDense & 0\\% & 119.11$\\pm$0.57 & 17{,}195 & --- \\\\\n\\midrule\nKL predictor-only & 30\\% & 126.64$\\pm$0.70 & 16{,}172 & +6.3\\% \\\\ % exp_id: latency_bench\nKL predictor-only & 50\\% & 126.78$\\pm$0.31 & 16{,}154 & +6.4\\% \\\\ % exp_id: latency_bench\n\\midrule\nPredictor + compensation & 30\\% & 129.94$\\pm$0.75 & 15{,}761 & +9.1\\% \\\\ % exp_id: latency_bench\nPredictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full KL-sparse pipeline adds 6.4\\% overhead to dense inference (126.78 vs.\\ 119.11\\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\\,ms (2.7\\%); the remainder arises from mask application and sparse FFN indexing.\nEliminating the compensation network saves an additional $\\sim$2.7\\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.\nThe overhead is near-identical at 30\\% and 50\\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.\n\nNote that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.\nThe pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\nOur contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.\n\n\n\\section{Predictor Bottleneck Sensitivity}\n\\label{app:db_sensitivity}\n\nTable~\\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Predictor bottleneck sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}\n\\label{tab:db_sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$d_b$ & Params & TEAL global & $\\Delta$ & Per-token \\\\\n\\midrule\n64 & 38.2M (0.48\\%) & 12.076 & +0.9\\% & 10.16 \\\\ % exp_id: db_sensitivity_sweep\n128 & 75.9M (0.95\\%) & 11.963 & --- & 9.218 \\\\ % exp_id: db_sensitivity_sweep\n256 & 151.5M (1.89\\%) & 12.105 & +1.2\\% & 8.586 \\\\ % exp_id: db_sensitivity_sweep\n512 & 302.5M (3.77\\%) & 12.315 & +2.9\\% & 7.93 \\\\ % exp_id: db_sensitivity_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\\to$7.93).\nThis divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.\nThe $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\n\n\\subsection{Temperature Schedule Sensitivity}\n\\label{app:tau_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature schedule sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:tau_sensitivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n$\\tau$ Schedule & PPL$\\downarrow$ \\\\\n\\midrule\nFixed $\\tau{=}0.5$ & \\textbf{11.861} \\\\ % exp_id: tau_schedule_sweep\nLinear $1.0 \\to 0.1$ (default) & 11.963 \\\\ % exp_id: tau_schedule_sweep\nFixed $\\tau{=}0.1$ & 12.072 \\\\ % exp_id: tau_schedule_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature schedule has minimal impact ($<$1.8\\% PPL variation).\nThe linear annealing default is a conservative choice; even removing annealing entirely (fixed $\\tau{=}0.5$) yields comparable performance.\n\n\\subsection{Training Convergence}\n\\label{app:training_convergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training convergence at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:training_convergence}\n\\small\n\\begin{tabular}{cc}\n\\toprule\nSteps & PPL$\\downarrow$ \\\\\n\\midrule\n200 & 15.158 \\\\ % exp_id: training_steps_sweep\n400 & 12.538 \\\\ % exp_id: training_steps_sweep\n600 & 12.046 \\\\ % exp_id: training_steps_sweep\n800 & 11.907 \\\\ % exp_id: training_steps_sweep\n1000 & \\textbf{11.906} \\\\ % exp_id: training_steps_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining converges rapidly: 95\\% of the quality gap closes by step 600, and performance saturates by step 800 ($\\Delta < 0.001$ between 800 and 1000 steps).\nOur default of 1000 steps provides a conservative margin.\n\n\n\\section{Geometric Penalty Schedule Dynamics}\n\\label{app:lagrangian}\n\nTable~\\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.\nThe geometric doubling pattern ($1 \\to 2 \\to 4 \\to 8 \\to \\ldots$) enables $\\lambda$ to reach steady state within $\\sim$10 steps; the deadzone ($\\epsilon = 0.02$) then stabilizes $\\lambda$ once actual sparsity is within $\\pm$2\\% of the target.\n\n\\begin{table}[h]\n\\centering\n\\caption{Geometric penalty schedule convergence across sparsity targets (margin $\\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}\n\\label{tab:lagrangian}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTarget $\\rho$ & $\\lambda_{\\max}$ & Final $\\lambda$ & Actual sparsity & Deviation \\\\\n\\midrule\n30\\% & 5000 & 5000 (cap) & 0.285 & 5.0\\% \\\\ % exp_id: kl_30pct_s42\n40\\% & 5000 & 625 & 0.398 & 0.5\\% \\\\ % exp_id: kl_40pct_s42\n50\\% & 1000 & 8 & 0.504 & 0.8\\% \\\\ % exp_id: kl_50pct_s42\n70\\% & 1000 & 1000 (cap) & 0.688 & 1.7\\% \\\\ % exp_id: kl_70pct_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 50\\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.\nAt 30\\% and 70\\%, the gap between the gate prior and target is larger, driving $\\lambda$ to its respective caps.\nThe 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation; this precision reflects a regime where the target is reachable without $\\lambda$ saturation.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{lagrangian_dynamics.pdf}\n\\caption{Lagrangian controller dynamics for 30\\% sparsity target ($\\lambda_{\\max}=5000$). Left axis (log scale): penalty weight $\\lambda$ rises from $0.01$ to its cap once actual sparsity undershoots the target at $\\sim$step~150, exhibiting bang-bang oscillations before saturating. Right axis: actual sparsity (solid) converges from the natural density ($\\approx$0.41) toward the target (dashed) and stabilizes near 0.28.}\n\\label{fig:lagrangian_dynamics}\n\\end{figure}\n\nTemperature $\\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.\nA mild loss increase in the final $\\sim$100 steps is expected: as masks become more binary ($\\tau \\to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.\n\nThe controller reliably drives actual sparsity to within 5\\% of the target across all tested regimes, with $\\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.\nFor the 30\\% target, actual sparsity is $\\approx$28.5\\% (5\\% deviation). This does not affect conclusions: TEAL at 28.5\\% actual sparsity yields PPL 10.30 (vs.\\ 10.97 at exact 30\\%), a 0.67 PPL difference negligible relative to the KL vs.\\ TEAL gap (8.96 vs.\\ 10.97).\n\n\n\\section{Out-of-Distribution Evaluation}\n\\label{app:ood}\n\nTo address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\\cite{raffel2020c4} validation set under TEAL global allocation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Out-of-distribution evaluation on C4 validation (PPL$\\downarrow$). 30\\% KL reports 2-seed mean$\\pm$std; other entries use seed 42.}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{llc}\n\\toprule\nSparsity & Method & C4 PPL$\\downarrow$ \\\\\n\\midrule\n0\\% & Dense & 9.21 \\\\\n\\midrule\n30\\% & KL predictor (Ours) & \\textbf{16.03$\\pm$0.01} \\\\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123\n\\midrule\n\\multirow{2}{*}{50\\%} & KL predictor (Ours) & \\textbf{18.40} \\\\ % exp_id: eval_c4_ood_kl50\n& TEAL vanilla & 38.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the 30\\% sparsity level, the KL predictor achieves C4 PPL 16.03$\\pm$0.01 (2-seed, global allocation, $1.74\\times$ dense), confirming OOD generalization.\nAt 50\\%, the KL predictor achieves 52.5\\% relative advantage over TEAL (18.40 vs.\\ 38.75), comparable to the 50\\% advantage on WikiText-2 (11.92 vs.\\ 23.90), confirming that KL-trained predictions generalize across distributions.\n\n\\paragraph{Uniform Allocation.}\nUnder uniform allocation at 30\\%, C4 PPL across three seeds is 18.22 (s42), 16.37 (s123), 16.36 (s456), yielding mean 16.98$\\pm$1.07 ($1.84\\times$ dense). % exp_id: c4_ood_kl30_uniform_3seed\nThe cross-seed variance is substantially higher than in-domain: CV=6.3\\% on C4 vs.\\ 0.2\\% on WikiText-2 (PPL 8.81$\\pm$0.02), driven by seed 42's elevated C4 PPL (18.22 vs.\\ 16.37 for other seeds).\nGlobal allocation's cross-layer budget flexibility partially compensates for domain shift (PPL 16.03 global vs.\\ 16.98 uniform), consistent with the Limitations observation that the predictor partially overfits to training-domain activation patterns.\n\n\\paragraph{Downstream Task Robustness.}\nTable~\\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\\ WikiText (in-domain), both at 30\\% uniform allocation (seed 42). All six benchmarks show $\\Delta$$\\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream task robustness to calibration domain shift (KL 30\\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\\_match (GSM8K).}\n\\label{tab:ood_downstream}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nCalibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nWikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\\\ % exp_id: c4_ood_downstream_kl30\n\\midrule\n$\\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Layer Retention Analysis}\n\\label{app:retention}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{per_layer_retention_chart.pdf}\n\\caption{Per-layer neuron retention under global top-$k$ allocation at 30\\%, 50\\%, and 70\\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\\% (L31) even at 30\\% sparsity. At 70\\%, starvation extends to mid-layers (L10--12: 16.7--20.1\\%), explaining the transition to the capacity-limited regime.}\n\\label{fig:retention}\n\\end{figure}\n\n\n\\section{Training Stability}\n\\label{app:stability}\n\nThree-seed evaluation ($s \\in \\{42, 123, 456\\}$) at 50\\% sparsity under uniform allocation yields PPL $11.92 \\pm 0.07$ (CV=0.6\\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform\nDownstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\n\nUnder global allocation at 50\\%, MMLU is $28.3 \\pm 0.7$\\%; the near-random performance is capacity-limited rather than seed-sensitive ($\\sigma$=0.7pp vs.\\ 9.5pp at 30\\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\nThe low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.\n\n\\subsection{Cross-Seed Mask Consistency}\n\\label{app:cross_seed_jaccard}\n\nTo assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30\n\nThe mean cross-seed Jaccard distance is 0.363 (IoU = 0.637), substantially lower than the KL-vs-magnitude divergence (0.46--0.68), confirming that KL-discovered patterns form a distinct cluster from magnitude-based masks.\nPer-layer divergence follows a U-shaped pattern: lowest at embedding-adjacent layers (L0: 0.33), peaking at early layers (L1: 0.41), with a mid-network valley (L12--14: 0.33). The random baseline Jaccard distance is 0.462.\n\nWhile specific mask configurations vary moderately across seeds (Jaccard distance 36.3\\%), the resulting PPL is highly stable (8.81$\\pm$0.02, CV=0.2\\%), suggesting multiple near-equivalent optima in the activation mask space.\nThe cross-seed divergence (36.3\\%) is substantially lower than the KL-vs-magnitude divergence (46--68\\%), confirming that KL discovers effective patterns that cluster distinctly from magnitude-based selection.\n\n\n\\section{MSE Baseline Configuration}\n\\label{app:mse_config}\n\nThe MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\\times}10^{-3}$, weight decay $1{\\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\\tau$: $1.0 \\to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.\nThe only difference is the loss target: per-layer $\\|\\mathbf{W}_d^{(\\ell)}(\\tilde{\\mathbf{m}}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}) - \\mathbf{y}_{\\text{dense}}^{(\\ell)}\\|_2^2$, replacing the end-to-end KL divergence.\nThis controlled comparison isolates the effect of output-distribution alignment: all three predictors see identical data in identical order with identical architectures; only the loss function differs. % exp_id: mse30_uniform_s42, mse50_uniform_s42\n\nMSE uses $\\lambda_{\\max}{=}1000$ (vs.\\ KL's 5000) because MSE's per-layer gradient magnitude is approximately $5\\times$ larger than KL's end-to-end gradient, requiring proportionally less penalty pressure to achieve comparable sparsity control. Both reach their target sparsity within 110 steps.\nAt 50\\% target, MSE converges to the target sparsity for seed 42; however, with seed 123, sparsity reaches only 5.1\\% under the same $\\lambda_{\\max}$ cap (eval PPL$=$15{,}789, random-level), indicating high sensitivity to initialization---a failure mode not observed with KL-based losses.\nAt 30\\%, MSE achieves 27.7\\% actual sparsity for s42 (gap 2.3pp).\nThe 3-seed MSE mean (18.52$\\pm$1.68; s42=20.43, s123=17.73, s456=17.39) is still $1.7\\times$ worse than TEAL (10.82), confirming that the performance deficit stems from the loss function, not insufficient sparsity pressure.\n\n\n\\section{Extended SNR Analysis}\n\\label{app:snr_extended}\n\nFigure~\\ref{fig:snr_trajectory} plots gradient SNR across the full 1000-step training for both KL and BCE predictors, measured at 14 checkpoints (LLaMA-3.1-8B, C4) with 95\\% bootstrap confidence intervals.\nFrom step 100 onward, BCE maintains consistently higher SNR than KL (2.3--17$\\times$ depending on training phase), with the gap narrowing toward convergence ($2.3\\times$ at step 1000: $2.026{\\times}10^{-3}$ vs.\\ $8.78{\\times}10^{-4}$). % exp_id: snr_full_curve_1000steps\nDespite KL's noisier gradient signal, KL-trained predictors produce substantially better masks (Table~\\ref{tab:main}), confirming that \\emph{target alignment} matters more than gradient clarity for mask quality.\nBCE's higher SNR reflects its simpler per-neuron classification objective, which concentrates gradients on individual neuron decisions; KL's coupled gradient distributes signal across all mask decisions jointly, yielding lower SNR but discovering compositionally superior mask patterns (\\S\\ref{sec:method:gradient}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{snr_trajectory.pdf}\n\\caption{Gradient SNR trajectory across 1000 training steps. BCE (orange) maintains consistently higher SNR than KL (blue) from step 100 onward (2.3--17$\\times$), yet KL produces superior masks (Table~\\ref{tab:main}), suggesting that target alignment matters more than gradient clarity for mask quality.}\n\\label{fig:snr_trajectory}\n\\end{figure}\n\n\n\\section{Extended Downstream Evaluation}\n\\label{app:downstream}\n\nTable~\\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\\% uniform: 3-seed mean$\\pm$std; others: seed 42.}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Method & HellaSwag & PIQA \\\\\n\\midrule\n0\\% & Dense & \\textbf{82.35} & \\textbf{80.90} \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& KL uniform & \\textbf{71.07$\\pm$0.54} & \\textbf{74.95$\\pm$0.25} \\\\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)\n& TEAL uniform & 63.31 & 72.80 \\\\ % exp_id: bench_teal30_uniform_6task\n& BCE isocompute & 62.81 & 74.21 \\\\ % exp_id: bce_isocompute_30u_hellaswag_piqa\n\\midrule\n\\multirow{3}{*}{50\\%}\n& KL global & \\textbf{58.95} & \\textbf{69.48} \\\\ % exp_id: hellaswag_piqa_kl50_global\n& KL uniform & 56.66 & 69.10 \\\\ % exp_id: hellaswag_piqa_kl50_uniform\n& TEAL uniform & 39.35 & 63.66 \\\\ % exp_id: bench_teal50_uniform_6task\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 30\\%, the KL predictor retains 86.3\\% of dense HellaSwag accuracy (71.07$\\pm$0.54 vs.\\ 82.35, 3-seed) and 92.6\\% of PIQA (74.95$\\pm$0.25 vs.\\ 80.90), confirming moderate degradation on non-reasoning tasks.\nAt 50\\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\\S\\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).\n\n\n\\section{Compensation Training Convergence}\n\\label{app:comp_convergence}\n\nAll compensation networks~\\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\\% s42 (final loss 0.70), 30\\% s456 (0.68), 50\\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42\n\n\n\\section{Qwen-2.5-14B Detailed Results}\n\\label{app:14b}\n\n\\begin{table}[h]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% nominal sparsity. Actual sparsity differs: KL 29.6\\% (3-seed), TEAL 29.3\\% (target 30\\%). \\textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\\% native sparsity (\\S\\ref{sec:method:gradient}), so forced global top-$k$ is used.}\n\\label{tab:14b}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \\textbf{75.01} & \\textbf{77.37} \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 & 70.51 & 74.70 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} & 53.43 & 68.28 \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{8}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.90} & 53.50 & \\textbf{72.82} & 63.55 & 32.0$\\pm$5.2 & \\textbf{72.68$\\pm$0.2} & \\textbf{76.01$\\pm$1.1} \\\\ % exp_id: qwen14b_kl30_uniform (3-seed s42/s123/s456)\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & \\textbf{52.1} & 67.72 & 74.70 \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nUnder global allocation, BCE's HellaSwag drops to 53.43\\% ($-$17pp vs.\\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval\n\n\\section{Full Allocation Analysis}\n\\label{app:alloc_full}\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation summary (LLaMA-3.1-8B). $\\pm$: 3-seed; $^\\ast$high seed variance.}\n\\label{tab:phase}\n\\footnotesize\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & MMLU \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & 35.7$\\pm$9.5$^\\ast$ \\\\ % exp_id: kl30_3seed_global\n& Uniform & \\textbf{8.81$\\pm$0.02} & \\textbf{40.7$\\pm$1.3} \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\n& Uniform & 11.92$\\pm$0.07 & 28.0$\\pm$0.6 \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:phase_full} extends Table~\\ref{tab:phase} with all downstream metrics.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Full allocation analysis: global top-$k$ vs.\\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); others: seed 42. $^\\ast$High MMLU seed variance (individual seeds span 25.3--43.5\\%).}\n\\label{tab:phase_full}\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{2}{*}{25\\%}\n& Global & \\textbf{8.17} & 45.4 & 70.6 & \\textbf{46.6} & \\textbf{11.5} \\\\\n& Uniform & 8.23 & \\textbf{46.5} & \\textbf{71.8} & 44.0 & 11.0 \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5$^\\ast$ & \\textbf{8.0$\\pm$0.7} \\\\\n& Uniform & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & \\textbf{40.7$\\pm$1.3} & 7.5$\\pm$0.1 \\\\\n\\midrule\n\\multirow{2}{*}{35\\%}\n& Global & \\textbf{9.31} & \\textbf{38.9} & \\textbf{67.6} & \\textbf{40.4} & \\textbf{7.7} \\\\\n& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\\\\n\\midrule\n\\multirow{2}{*}{40\\%}\n& Global & \\textbf{10.14} & 39.5 & \\textbf{67.5} & \\textbf{39.5} & \\textbf{6.6} \\\\\n& Uniform & 10.76 & \\textbf{39.6} & 63.1 & 35.5 & 3.6 \\\\\n\\midrule\n\\multirow{2}{*}{45\\%}\n& Global & \\textbf{10.80} & \\textbf{39.2} & \\textbf{64.6} & 30.4 & \\textbf{3.0} \\\\\n& Uniform & 10.95 & 37.6 & 63.6 & \\textbf{30.6} & 2.7 \\\\\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.7$\\pm$1.3} \\\\\n& Uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Mask Pattern Visualization}\n\\label{app:mask_viz}\n\nFigure~\\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity.\nFigure~\\ref{fig:scatter} shows per-neuron importance scores at layer 16.\nFigure~\\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{neuron_scatter_layer16.pdf}\n\\caption{KL vs.\\ magnitude importance scores for layer 16 neurons at 50\\% sparsity. 41\\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}\n\\label{fig:scatter}\n\\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_divergence_heatmap.pdf}\n\\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\\%) and increases with sparsity across all layers.}\n\\label{fig:mask_heatmap}\n\\end{figure*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_comparison.pdf}\n\\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\\% and 50\\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\\%, 0.74 at 50\\%).}\n\\label{fig:mask_comparison}\n\\end{figure*}\n\n\n\\section{Cross-Architecture Comparison}\n\\label{app:cross_arch}\n\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. \\textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\\%: 3-seed mean$\\pm$std; other rows: seed 42.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.93$\\pm$0.19} & 8.38 & 1.21$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL PPL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity).\nTable~\\ref{tab:mistral_downstream} reports downstream task accuracy at 30\\% sparsity on Mistral-7B-v0.3 (3-seed). KL improves PPL ($-$17.3\\%) and commonsense tasks (WG +6.7pp) but MMLU is tied (43.3\\% vs.\\ 43.5\\%); ARC-c shows high seed variance ($\\sigma$=6.4pp); GSM8K reverses.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B-v0.3 downstream evaluation at 30\\% sparsity. $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); TEAL is deterministic (single run). ARC-c exhibits high seed variance ($\\sigma$=6.4pp).}\n\\label{tab:mistral_downstream}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\\\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa\nKL 30\\% & \\textbf{6.93$\\pm$0.19} & \\textbf{44.9$\\pm$6.4} & \\textbf{70.2$\\pm$1.2} & \\textbf{69.7$\\pm$0.8} & \\textbf{74.8$\\pm$0.4} & 43.3$\\pm$1.5 & 8.6$\\pm$2.2 \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456\nTEAL 30\\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & \\textbf{43.5} & \\textbf{15.9} \\\\ % exp_id: mistral_teal30_downstream\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Taxonomy Discussion}\n\\label{app:taxonomy}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2025spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-token} methods~\\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass; each mask decision's gradient reflects its joint effect with all other masks on the final distribution.\n\nSPON~\\cite{xu2025spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\\times$ coupled).\nDejaVu~\\cite{liu2023dejavu} and FastForward~\\cite{gautam2026fastforward} achieve per-token granularity but use BCE, where each neuron's gradient is independent of other mask states.\nD2DMoE~\\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.\nWe define \\emph{output-distribution alignment} as whether the training loss optimizes a quantity that composes across layers.\nKL on output logits directly optimizes next-token prediction loss, which does not suffer from error composition; per-layer MSE minimizes reconstruction error independently at each layer, but layer-wise optima do not compose---a mask minimizing FFN output error at layer $\\ell$ may amplify errors in layers $\\ell{+}1 \\ldots L$.\nThe SNR analysis (\\S\\ref{sec:method:gradient}) corroborates this: KL achieves the best masks despite $2.3\\times$ lower SNR than BCE, while MSE produces the worst masks.\nThe framework predicts that losses operating on output-level quantities should outperform intermediate-level losses, a hypothesis consistent with our MSE results and testable with alternative output-level objectives.\n\n\\section{Oracle Mask Provenance}\n\\label{app:oracle_provenance}\n\nC1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold (logits $> 0$, equivalent to $\\sigma > 0.5$); they reflect one specific training trajectory (optimizer state, data order, Gumbel noise).\nThe s42/s123/s456 consistency ($\\leq$1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.\n\n\\section{SPON Orthogonality}\n\\label{app:spon}\n\nSPON~\\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\nThe decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.\n\n\\section{Per-Layer KL Downstream Decomposition}\n\\label{app:perlayer_downstream}\n\nTable~\\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\\ coupling scope decomposition at 30\\% sparsity (\\S\\ref{sec:perlayer}). BoolQ's $\\approx$100\\% coupling is an upper bound confounded by high cross-seed variance ($\\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.\n\n\\begin{table}[h]\n\\centering\n\\caption{2D decomposition at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \\S\\ref{sec:perlayer}).}\n\\label{tab:perlayer_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\n& PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\\\\n\\midrule\nE2E KL & 8.81$\\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\\\\nPer-layer KL & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\\\\nMSE & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 & 64.5$\\pm$5.3 \\\\\n\\midrule\nTotal gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\\\\nSignal type (\\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\\approx$0 \\\\\nCoupling (\\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\\approx$100 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{$K{=}4$ Mismatch Control}\n\\label{app:k4_downstream}\n\nTable~\\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\\% sparsity.\nTraining with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\\ 1/32 layers masked during training, while inference applies all 32).\nThe gap closure column reports the fraction of the $K{=}1 \\to$ E2E KL gap closed by $K{=}4$.\n\n\\begin{table}[h]\n\\centering\n\\caption{3-seed $K{=}4$ mismatch control at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \\in \\{42, 123, 456\\}$). Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\\text{E2E} - K{=}1) \\times 100$.}\n\\label{tab:k4_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\n& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\\%) \\\\\n\\midrule\nPPL$\\downarrow$ & 8.89$\\pm$0.01 & 9.05$\\pm$0.02 & 8.81$\\pm$0.02 & 66.7 \\\\\nARC-c & 40.0$\\pm$1.3 & 39.9 & 43.7$\\pm$2.5 & 2.6 \\\\\nWG & 66.9$\\pm$0.2 & 65.9 & 68.9$\\pm$0.4 & 33.3 \\\\\nMMLU$^\\ast$ & 42.7$\\pm$1.4 & 38.6 & 40.7$\\pm$1.3 & $>$100 \\\\\nGSM8K & 7.0$\\pm$1.6 & 5.8 & 7.5$\\pm$0.1 & 70.6 \\\\\nBoolQ$^\\dagger$ & 67.7$\\pm$7.5 & 64.5$\\pm$11.5 & 73.7 & 34.8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize $^\\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\\% (Appendix~\\ref{app:constraint}).\n$^\\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}\n\\end{table}\n\n\\section{Per-Layer Sparsity Constraint Analysis}\n\\label{app:constraint}\n\nTo test the causal role of the KL predictor's learned per-layer allocation, we evaluate two inference-time interventions at 30\\% overall sparsity (seed 42, uniform allocation baseline):\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity constraint analysis. \\emph{Protect late}: cap L22--L28 sparsity $\\leq$30\\%; \\emph{Remove valley}: override L14--L18 sparsity to 30\\%. Budget redistributed to maintain 30\\% overall.}\n\\label{tab:constraint}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & PPL & ARC-c & MMLU & GSM8K \\\\\n\\midrule\nKL baseline (s42) & 8.82 & 40.8 & 40.6 & 7.4 \\\\\nProtect late layers & 9.26 & 42.4 & 40.7 & 6.5 \\\\\nRemove valley & 8.76 & 39.3 & 44.0 & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nProtecting late layers (L22--L28) does not improve knowledge-intensive metrics despite reducing their sparsity from 48--57\\% to $\\leq$30\\%, while worsening PPL by 5.2\\%.\nConversely, removing the protection valley (forcing L14--L18 to 30\\% instead of 14--18\\%) improves MMLU by +3.4pp and GSM8K by +1.6pp at the cost of ARC-c $-$1.5pp.\nThe KL predictor's learned allocation thus represents a task-dependent trade-off---prioritizing commonsense reasoning via middle-layer protection---rather than a uniformly optimal pattern.\nThis allocation trade-off also explains the $K{=}4$ MMLU anomaly (\\S\\ref{app:k4_downstream}): $K{=}4$'s near-uniform learned sparsity (std=0.003) inherently removes the valley, producing MMLU=43.5 comparable to the remove-valley condition (44.0).\n\n\\section{Per-Layer Sparsity Distribution}\n\\label{app:perlayer_sparsity}\n\nThe KL predictor at 30\\% target sparsity learns a non-uniform per-layer allocation that differs markedly from magnitude-based selection.\nAggregate sparsity is similar across broad regions (early L0--L7: KL 28.1\\% vs.\\ magnitude 27.5\\%; late L24--L31: 44.9\\% vs.\\ 47.2\\%), but middle layers (L8--L23) exhibit high internal variance despite similar averages (28.2\\% vs.\\ 27.3\\%).\nTable~\\ref{tab:perlayer_sparsity} highlights three sub-ranges.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity sub-ranges: KL predictor vs.\\ magnitude (LLaMA-3.1-8B, 30\\%, uniform allocation). Ranges denote min--max across layers in each group.}\n\\label{tab:perlayer_sparsity}\n\\begin{tabular}{lccc}\n\\toprule\nLayer Range & KL (\\%) & Mag (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nL8--L12 (high pruning) & 32--36 & 25--26 & $+$7 to $+$10 \\\\\nL14--L18 (protection valley) & 14--18 & 28--30 & $-$8 to $-$16 \\\\\nL22--L28 (aggressive pruning) & 48--57 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{C4 Training Data Control}\n\\label{app:c4_control}\n\nTo test whether WikiText-103's narrow domain drives the knowledge-task regression (\\S\\ref{sec:experiments}), we train the KL predictor on C4~\\cite{raffel2020c4} (diverse web text) under identical hyperparameters (1000 steps, 30\\% uniform, s42).\n\n\\begin{table}[h]\n\\centering\n\\caption{C4-trained vs.\\ WikiText-trained KL predictor (LLaMA-3.1-8B, 30\\% uniform, s42).}\n\\label{tab:c4_control}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\nTraining Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\\n\\midrule\nWikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe C4-trained predictor achieves comparable MMLU (40.0\\% vs.\\ 40.6\\%) but worse GSM8K (4.1\\% vs.\\ 7.4\\%) and higher PPL (11.55 vs.\\ 8.82), despite training on more diverse text.\nThis rules out training data composition as the primary cause of knowledge-task regression and supports the hypothesis that forward KL's mode-covering property structurally under-protects rare reasoning-critical activations. % exp_id: c4_control_eval\n\n\\section{Per-Layer Coupling Breadth Analysis}\n\\label{app:k_curve}\n\nWe vary the number of layers coupled per training step ($K$) from 1 (pure per-layer) to 32 (end-to-end), evaluating all predictors under TEAL uniform allocation at 30\\% sparsity on LLaMA-3.1-8B.\n\n\\begin{table}[h]\n\\centering\n\\caption{K-curve: coupling breadth vs.\\ predictor quality (30\\%, TEAL uniform, LLaMA-3.1-8B). All values are 3-seed mean$\\pm$std (s42/s123/s456) except $K{=}1$ downstream (single seed). ``---'' = not evaluated.}\n\\label{tab:k_curve}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{cccccccc}\n\\toprule\n$K$ & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\n1 & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & --- & --- \\\\\n2 & 10.75$\\pm$0.15 & 39.7$\\pm$1.2 & 63.2$\\pm$1.7 & 38.3$\\pm$3.2 & 2.8$\\pm$0.6 & 66.5$\\pm$1.0 & 73.5$\\pm$0.7 \\\\\n4 & 8.89$\\pm$0.01 & 40.0$\\pm$1.2 & 66.9$\\pm$0.2 & 42.7$\\pm$1.4 & 7.0$\\pm$1.6 & 67.8$\\pm$1.0 & 74.5$\\pm$0.5 \\\\\n8 & 9.00$\\pm$0.06 & 40.7$\\pm$1.0 & 68.7$\\pm$1.3 & 40.4$\\pm$0.6 & 6.8$\\pm$1.3 & 69.0$\\pm$1.1 & 75.1$\\pm$1.1 \\\\\n16 & 8.67$\\pm$0.02 & 41.9$\\pm$1.1 & 68.5$\\pm$0.9 & 40.9$\\pm$2.9 & 8.5$\\pm$1.2 & 70.1$\\pm$0.4 & 75.0$\\pm$0.8 \\\\\n32 (E2E) & 8.81$\\pm$0.02 & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nPPL exhibits a non-monotonic U-shape (Figure~\\ref{fig:k_curve_ppl}): $K{=}2$ is worst (10.75$\\pm$0.15), likely due to insufficient per-layer updates (${\\sim}$62 updates/layer vs.\\ ${\\sim}$250 at $K{=}8$). $K{=}16$ achieves the lowest PPL (8.67$\\pm$0.02), marginally better than E2E (8.81$\\pm$0.02). $K{=}16$ MMLU exhibits high seed variance (std=2.9; s42=44.0, s123=40.0, s456=38.7), with the 3-seed mean (40.9) indistinguishable from E2E (40.7$\\pm$1.3).\nThe signal type gap ($K{=}1$ KL 9.05 vs.\\ per-layer MSE 18.52$\\pm$1.68) of 9.47 PPL dwarfs the coupling breadth range within KL (best $K{=}16$ 8.67 vs.\\ worst $K{=}2$ 10.75 = 2.08 PPL), reinforcing that output-distribution alignment, not coupling scope, is the primary quality lever for PPL at this sparsity level. % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed, perlayer_kl_30_3seed, perlayer_kl_k4_3seed\n\n\\section{Licenses}\n\\label{app:licenses}\n\nLLaMA-3.1-8B is released under the Llama 3.1 Community License Agreement.\nMistral-7B-v0.3 is released under the Apache 2.0 License.\nQwen-2.5-14B is released under the Apache 2.0 License.\nWikiText-103 and WikiText-2~\\cite{merity2017pointer} are released under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).\nAll evaluation benchmarks (ARC, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA) are publicly available under their respective licenses.\nOur code will be released under the MIT License upon acceptance.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 384,
        "oldLines": 7,
        "newStart": 384,
        "newLines": 7,
        "lines": [
          " & Uniform & 10.95 & 37.6 & 63.6 & \\textbf{30.6} & 2.7 \\\\",
          " \\midrule",
          " \\multirow{2}{*}{50\\%}",
          "-& Global & \\textbf{11.84$\\pm$0.15} & \\textbf{36.3$\\pm$3.2} & \\textbf{63.8$\\pm$0.3} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.7$\\pm$1.3} \\\\",
          "+& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.3$\\pm$1.1} \\\\",
          " & Uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\",
          " \\bottomrule",
          " \\end{tabular}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 174_

Now Fix 2 and Fix 3 — C4 control table rounding:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "e45b00ca-1429-4a63-920a-2b0a1256adcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcQxWgTm55tphrARuV1w4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3508,
      "cache_read_input_tokens": 126465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3508
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 175_

<details open><summary>🔧 Tool call — Edit · `toolu_01NHw3QSC6E5Ck1w52pxZtGP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "old_string": "WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa",
  "new_string": "WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "6d942386-2240-4326-9d2a-5faa1077b129",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcQxWgTm55tphrARuV1w4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3508,
      "cache_read_input_tokens": 126465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3508
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 176 · 2026-05-24T02:26:03.669Z_

<details><summary>↩ Tool result · `toolu_01NHw3QSC6E5Ck1w52pxZtGP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "26e1e907-484a-4a2b-99ad-da6a9986eaff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "oldString": "WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa",
    "newString": "WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)",
    "originalFile": "\\appendix\n\n\\section{Inference Efficiency}\n\\label{app:latency}\n\nTable~\\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Sparsity & ms/fwd & tok/s & Overhead \\\\\n\\midrule\nDense & 0\\% & 119.11$\\pm$0.57 & 17{,}195 & --- \\\\\n\\midrule\nKL predictor-only & 30\\% & 126.64$\\pm$0.70 & 16{,}172 & +6.3\\% \\\\ % exp_id: latency_bench\nKL predictor-only & 50\\% & 126.78$\\pm$0.31 & 16{,}154 & +6.4\\% \\\\ % exp_id: latency_bench\n\\midrule\nPredictor + compensation & 30\\% & 129.94$\\pm$0.75 & 15{,}761 & +9.1\\% \\\\ % exp_id: latency_bench\nPredictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full KL-sparse pipeline adds 6.4\\% overhead to dense inference (126.78 vs.\\ 119.11\\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\\,ms (2.7\\%); the remainder arises from mask application and sparse FFN indexing.\nEliminating the compensation network saves an additional $\\sim$2.7\\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.\nThe overhead is near-identical at 30\\% and 50\\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.\n\nNote that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.\nThe pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\nOur contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.\n\n\n\\section{Predictor Bottleneck Sensitivity}\n\\label{app:db_sensitivity}\n\nTable~\\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Predictor bottleneck sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}\n\\label{tab:db_sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$d_b$ & Params & TEAL global & $\\Delta$ & Per-token \\\\\n\\midrule\n64 & 38.2M (0.48\\%) & 12.076 & +0.9\\% & 10.16 \\\\ % exp_id: db_sensitivity_sweep\n128 & 75.9M (0.95\\%) & 11.963 & --- & 9.218 \\\\ % exp_id: db_sensitivity_sweep\n256 & 151.5M (1.89\\%) & 12.105 & +1.2\\% & 8.586 \\\\ % exp_id: db_sensitivity_sweep\n512 & 302.5M (3.77\\%) & 12.315 & +2.9\\% & 7.93 \\\\ % exp_id: db_sensitivity_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\\to$7.93).\nThis divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.\nThe $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\n\n\\subsection{Temperature Schedule Sensitivity}\n\\label{app:tau_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature schedule sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:tau_sensitivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n$\\tau$ Schedule & PPL$\\downarrow$ \\\\\n\\midrule\nFixed $\\tau{=}0.5$ & \\textbf{11.861} \\\\ % exp_id: tau_schedule_sweep\nLinear $1.0 \\to 0.1$ (default) & 11.963 \\\\ % exp_id: tau_schedule_sweep\nFixed $\\tau{=}0.1$ & 12.072 \\\\ % exp_id: tau_schedule_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature schedule has minimal impact ($<$1.8\\% PPL variation).\nThe linear annealing default is a conservative choice; even removing annealing entirely (fixed $\\tau{=}0.5$) yields comparable performance.\n\n\\subsection{Training Convergence}\n\\label{app:training_convergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training convergence at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:training_convergence}\n\\small\n\\begin{tabular}{cc}\n\\toprule\nSteps & PPL$\\downarrow$ \\\\\n\\midrule\n200 & 15.158 \\\\ % exp_id: training_steps_sweep\n400 & 12.538 \\\\ % exp_id: training_steps_sweep\n600 & 12.046 \\\\ % exp_id: training_steps_sweep\n800 & 11.907 \\\\ % exp_id: training_steps_sweep\n1000 & \\textbf{11.906} \\\\ % exp_id: training_steps_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining converges rapidly: 95\\% of the quality gap closes by step 600, and performance saturates by step 800 ($\\Delta < 0.001$ between 800 and 1000 steps).\nOur default of 1000 steps provides a conservative margin.\n\n\n\\section{Geometric Penalty Schedule Dynamics}\n\\label{app:lagrangian}\n\nTable~\\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.\nThe geometric doubling pattern ($1 \\to 2 \\to 4 \\to 8 \\to \\ldots$) enables $\\lambda$ to reach steady state within $\\sim$10 steps; the deadzone ($\\epsilon = 0.02$) then stabilizes $\\lambda$ once actual sparsity is within $\\pm$2\\% of the target.\n\n\\begin{table}[h]\n\\centering\n\\caption{Geometric penalty schedule convergence across sparsity targets (margin $\\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}\n\\label{tab:lagrangian}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTarget $\\rho$ & $\\lambda_{\\max}$ & Final $\\lambda$ & Actual sparsity & Deviation \\\\\n\\midrule\n30\\% & 5000 & 5000 (cap) & 0.285 & 5.0\\% \\\\ % exp_id: kl_30pct_s42\n40\\% & 5000 & 625 & 0.398 & 0.5\\% \\\\ % exp_id: kl_40pct_s42\n50\\% & 1000 & 8 & 0.504 & 0.8\\% \\\\ % exp_id: kl_50pct_s42\n70\\% & 1000 & 1000 (cap) & 0.688 & 1.7\\% \\\\ % exp_id: kl_70pct_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 50\\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.\nAt 30\\% and 70\\%, the gap between the gate prior and target is larger, driving $\\lambda$ to its respective caps.\nThe 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation; this precision reflects a regime where the target is reachable without $\\lambda$ saturation.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{lagrangian_dynamics.pdf}\n\\caption{Lagrangian controller dynamics for 30\\% sparsity target ($\\lambda_{\\max}=5000$). Left axis (log scale): penalty weight $\\lambda$ rises from $0.01$ to its cap once actual sparsity undershoots the target at $\\sim$step~150, exhibiting bang-bang oscillations before saturating. Right axis: actual sparsity (solid) converges from the natural density ($\\approx$0.41) toward the target (dashed) and stabilizes near 0.28.}\n\\label{fig:lagrangian_dynamics}\n\\end{figure}\n\nTemperature $\\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.\nA mild loss increase in the final $\\sim$100 steps is expected: as masks become more binary ($\\tau \\to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.\n\nThe controller reliably drives actual sparsity to within 5\\% of the target across all tested regimes, with $\\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.\nFor the 30\\% target, actual sparsity is $\\approx$28.5\\% (5\\% deviation). This does not affect conclusions: TEAL at 28.5\\% actual sparsity yields PPL 10.30 (vs.\\ 10.97 at exact 30\\%), a 0.67 PPL difference negligible relative to the KL vs.\\ TEAL gap (8.96 vs.\\ 10.97).\n\n\n\\section{Out-of-Distribution Evaluation}\n\\label{app:ood}\n\nTo address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\\cite{raffel2020c4} validation set under TEAL global allocation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Out-of-distribution evaluation on C4 validation (PPL$\\downarrow$). 30\\% KL reports 2-seed mean$\\pm$std; other entries use seed 42.}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{llc}\n\\toprule\nSparsity & Method & C4 PPL$\\downarrow$ \\\\\n\\midrule\n0\\% & Dense & 9.21 \\\\\n\\midrule\n30\\% & KL predictor (Ours) & \\textbf{16.03$\\pm$0.01} \\\\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123\n\\midrule\n\\multirow{2}{*}{50\\%} & KL predictor (Ours) & \\textbf{18.40} \\\\ % exp_id: eval_c4_ood_kl50\n& TEAL vanilla & 38.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the 30\\% sparsity level, the KL predictor achieves C4 PPL 16.03$\\pm$0.01 (2-seed, global allocation, $1.74\\times$ dense), confirming OOD generalization.\nAt 50\\%, the KL predictor achieves 52.5\\% relative advantage over TEAL (18.40 vs.\\ 38.75), comparable to the 50\\% advantage on WikiText-2 (11.92 vs.\\ 23.90), confirming that KL-trained predictions generalize across distributions.\n\n\\paragraph{Uniform Allocation.}\nUnder uniform allocation at 30\\%, C4 PPL across three seeds is 18.22 (s42), 16.37 (s123), 16.36 (s456), yielding mean 16.98$\\pm$1.07 ($1.84\\times$ dense). % exp_id: c4_ood_kl30_uniform_3seed\nThe cross-seed variance is substantially higher than in-domain: CV=6.3\\% on C4 vs.\\ 0.2\\% on WikiText-2 (PPL 8.81$\\pm$0.02), driven by seed 42's elevated C4 PPL (18.22 vs.\\ 16.37 for other seeds).\nGlobal allocation's cross-layer budget flexibility partially compensates for domain shift (PPL 16.03 global vs.\\ 16.98 uniform), consistent with the Limitations observation that the predictor partially overfits to training-domain activation patterns.\n\n\\paragraph{Downstream Task Robustness.}\nTable~\\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\\ WikiText (in-domain), both at 30\\% uniform allocation (seed 42). All six benchmarks show $\\Delta$$\\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream task robustness to calibration domain shift (KL 30\\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\\_match (GSM8K).}\n\\label{tab:ood_downstream}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nCalibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nWikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\\\ % exp_id: c4_ood_downstream_kl30\n\\midrule\n$\\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Layer Retention Analysis}\n\\label{app:retention}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{per_layer_retention_chart.pdf}\n\\caption{Per-layer neuron retention under global top-$k$ allocation at 30\\%, 50\\%, and 70\\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\\% (L31) even at 30\\% sparsity. At 70\\%, starvation extends to mid-layers (L10--12: 16.7--20.1\\%), explaining the transition to the capacity-limited regime.}\n\\label{fig:retention}\n\\end{figure}\n\n\n\\section{Training Stability}\n\\label{app:stability}\n\nThree-seed evaluation ($s \\in \\{42, 123, 456\\}$) at 50\\% sparsity under uniform allocation yields PPL $11.92 \\pm 0.07$ (CV=0.6\\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform\nDownstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\n\nUnder global allocation at 50\\%, MMLU is $28.3 \\pm 0.7$\\%; the near-random performance is capacity-limited rather than seed-sensitive ($\\sigma$=0.7pp vs.\\ 9.5pp at 30\\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\nThe low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.\n\n\\subsection{Cross-Seed Mask Consistency}\n\\label{app:cross_seed_jaccard}\n\nTo assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30\n\nThe mean cross-seed Jaccard distance is 0.363 (IoU = 0.637), substantially lower than the KL-vs-magnitude divergence (0.46--0.68), confirming that KL-discovered patterns form a distinct cluster from magnitude-based masks.\nPer-layer divergence follows a U-shaped pattern: lowest at embedding-adjacent layers (L0: 0.33), peaking at early layers (L1: 0.41), with a mid-network valley (L12--14: 0.33). The random baseline Jaccard distance is 0.462.\n\nWhile specific mask configurations vary moderately across seeds (Jaccard distance 36.3\\%), the resulting PPL is highly stable (8.81$\\pm$0.02, CV=0.2\\%), suggesting multiple near-equivalent optima in the activation mask space.\nThe cross-seed divergence (36.3\\%) is substantially lower than the KL-vs-magnitude divergence (46--68\\%), confirming that KL discovers effective patterns that cluster distinctly from magnitude-based selection.\n\n\n\\section{MSE Baseline Configuration}\n\\label{app:mse_config}\n\nThe MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\\times}10^{-3}$, weight decay $1{\\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\\tau$: $1.0 \\to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.\nThe only difference is the loss target: per-layer $\\|\\mathbf{W}_d^{(\\ell)}(\\tilde{\\mathbf{m}}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}) - \\mathbf{y}_{\\text{dense}}^{(\\ell)}\\|_2^2$, replacing the end-to-end KL divergence.\nThis controlled comparison isolates the effect of output-distribution alignment: all three predictors see identical data in identical order with identical architectures; only the loss function differs. % exp_id: mse30_uniform_s42, mse50_uniform_s42\n\nMSE uses $\\lambda_{\\max}{=}1000$ (vs.\\ KL's 5000) because MSE's per-layer gradient magnitude is approximately $5\\times$ larger than KL's end-to-end gradient, requiring proportionally less penalty pressure to achieve comparable sparsity control. Both reach their target sparsity within 110 steps.\nAt 50\\% target, MSE converges to the target sparsity for seed 42; however, with seed 123, sparsity reaches only 5.1\\% under the same $\\lambda_{\\max}$ cap (eval PPL$=$15{,}789, random-level), indicating high sensitivity to initialization---a failure mode not observed with KL-based losses.\nAt 30\\%, MSE achieves 27.7\\% actual sparsity for s42 (gap 2.3pp).\nThe 3-seed MSE mean (18.52$\\pm$1.68; s42=20.43, s123=17.73, s456=17.39) is still $1.7\\times$ worse than TEAL (10.82), confirming that the performance deficit stems from the loss function, not insufficient sparsity pressure.\n\n\n\\section{Extended SNR Analysis}\n\\label{app:snr_extended}\n\nFigure~\\ref{fig:snr_trajectory} plots gradient SNR across the full 1000-step training for both KL and BCE predictors, measured at 14 checkpoints (LLaMA-3.1-8B, C4) with 95\\% bootstrap confidence intervals.\nFrom step 100 onward, BCE maintains consistently higher SNR than KL (2.3--17$\\times$ depending on training phase), with the gap narrowing toward convergence ($2.3\\times$ at step 1000: $2.026{\\times}10^{-3}$ vs.\\ $8.78{\\times}10^{-4}$). % exp_id: snr_full_curve_1000steps\nDespite KL's noisier gradient signal, KL-trained predictors produce substantially better masks (Table~\\ref{tab:main}), confirming that \\emph{target alignment} matters more than gradient clarity for mask quality.\nBCE's higher SNR reflects its simpler per-neuron classification objective, which concentrates gradients on individual neuron decisions; KL's coupled gradient distributes signal across all mask decisions jointly, yielding lower SNR but discovering compositionally superior mask patterns (\\S\\ref{sec:method:gradient}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{snr_trajectory.pdf}\n\\caption{Gradient SNR trajectory across 1000 training steps. BCE (orange) maintains consistently higher SNR than KL (blue) from step 100 onward (2.3--17$\\times$), yet KL produces superior masks (Table~\\ref{tab:main}), suggesting that target alignment matters more than gradient clarity for mask quality.}\n\\label{fig:snr_trajectory}\n\\end{figure}\n\n\n\\section{Extended Downstream Evaluation}\n\\label{app:downstream}\n\nTable~\\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\\% uniform: 3-seed mean$\\pm$std; others: seed 42.}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Method & HellaSwag & PIQA \\\\\n\\midrule\n0\\% & Dense & \\textbf{82.35} & \\textbf{80.90} \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& KL uniform & \\textbf{71.07$\\pm$0.54} & \\textbf{74.95$\\pm$0.25} \\\\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)\n& TEAL uniform & 63.31 & 72.80 \\\\ % exp_id: bench_teal30_uniform_6task\n& BCE isocompute & 62.81 & 74.21 \\\\ % exp_id: bce_isocompute_30u_hellaswag_piqa\n\\midrule\n\\multirow{3}{*}{50\\%}\n& KL global & \\textbf{58.95} & \\textbf{69.48} \\\\ % exp_id: hellaswag_piqa_kl50_global\n& KL uniform & 56.66 & 69.10 \\\\ % exp_id: hellaswag_piqa_kl50_uniform\n& TEAL uniform & 39.35 & 63.66 \\\\ % exp_id: bench_teal50_uniform_6task\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 30\\%, the KL predictor retains 86.3\\% of dense HellaSwag accuracy (71.07$\\pm$0.54 vs.\\ 82.35, 3-seed) and 92.6\\% of PIQA (74.95$\\pm$0.25 vs.\\ 80.90), confirming moderate degradation on non-reasoning tasks.\nAt 50\\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\\S\\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).\n\n\n\\section{Compensation Training Convergence}\n\\label{app:comp_convergence}\n\nAll compensation networks~\\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\\% s42 (final loss 0.70), 30\\% s456 (0.68), 50\\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42\n\n\n\\section{Qwen-2.5-14B Detailed Results}\n\\label{app:14b}\n\n\\begin{table}[h]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% nominal sparsity. Actual sparsity differs: KL 29.6\\% (3-seed), TEAL 29.3\\% (target 30\\%). \\textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\\% native sparsity (\\S\\ref{sec:method:gradient}), so forced global top-$k$ is used.}\n\\label{tab:14b}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \\textbf{75.01} & \\textbf{77.37} \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 & 70.51 & 74.70 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} & 53.43 & 68.28 \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{8}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.90} & 53.50 & \\textbf{72.82} & 63.55 & 32.0$\\pm$5.2 & \\textbf{72.68$\\pm$0.2} & \\textbf{76.01$\\pm$1.1} \\\\ % exp_id: qwen14b_kl30_uniform (3-seed s42/s123/s456)\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & \\textbf{52.1} & 67.72 & 74.70 \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nUnder global allocation, BCE's HellaSwag drops to 53.43\\% ($-$17pp vs.\\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval\n\n\\section{Full Allocation Analysis}\n\\label{app:alloc_full}\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation summary (LLaMA-3.1-8B). $\\pm$: 3-seed; $^\\ast$high seed variance.}\n\\label{tab:phase}\n\\footnotesize\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & MMLU \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & 35.7$\\pm$9.5$^\\ast$ \\\\ % exp_id: kl30_3seed_global\n& Uniform & \\textbf{8.81$\\pm$0.02} & \\textbf{40.7$\\pm$1.3} \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\n& Uniform & 11.92$\\pm$0.07 & 28.0$\\pm$0.6 \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:phase_full} extends Table~\\ref{tab:phase} with all downstream metrics.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Full allocation analysis: global top-$k$ vs.\\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); others: seed 42. $^\\ast$High MMLU seed variance (individual seeds span 25.3--43.5\\%).}\n\\label{tab:phase_full}\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{2}{*}{25\\%}\n& Global & \\textbf{8.17} & 45.4 & 70.6 & \\textbf{46.6} & \\textbf{11.5} \\\\\n& Uniform & 8.23 & \\textbf{46.5} & \\textbf{71.8} & 44.0 & 11.0 \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5$^\\ast$ & \\textbf{8.0$\\pm$0.7} \\\\\n& Uniform & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & \\textbf{40.7$\\pm$1.3} & 7.5$\\pm$0.1 \\\\\n\\midrule\n\\multirow{2}{*}{35\\%}\n& Global & \\textbf{9.31} & \\textbf{38.9} & \\textbf{67.6} & \\textbf{40.4} & \\textbf{7.7} \\\\\n& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\\\\n\\midrule\n\\multirow{2}{*}{40\\%}\n& Global & \\textbf{10.14} & 39.5 & \\textbf{67.5} & \\textbf{39.5} & \\textbf{6.6} \\\\\n& Uniform & 10.76 & \\textbf{39.6} & 63.1 & 35.5 & 3.6 \\\\\n\\midrule\n\\multirow{2}{*}{45\\%}\n& Global & \\textbf{10.80} & \\textbf{39.2} & \\textbf{64.6} & 30.4 & \\textbf{3.0} \\\\\n& Uniform & 10.95 & 37.6 & 63.6 & \\textbf{30.6} & 2.7 \\\\\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.3$\\pm$1.1} \\\\\n& Uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Mask Pattern Visualization}\n\\label{app:mask_viz}\n\nFigure~\\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity.\nFigure~\\ref{fig:scatter} shows per-neuron importance scores at layer 16.\nFigure~\\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{neuron_scatter_layer16.pdf}\n\\caption{KL vs.\\ magnitude importance scores for layer 16 neurons at 50\\% sparsity. 41\\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}\n\\label{fig:scatter}\n\\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_divergence_heatmap.pdf}\n\\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\\%) and increases with sparsity across all layers.}\n\\label{fig:mask_heatmap}\n\\end{figure*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_comparison.pdf}\n\\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\\% and 50\\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\\%, 0.74 at 50\\%).}\n\\label{fig:mask_comparison}\n\\end{figure*}\n\n\n\\section{Cross-Architecture Comparison}\n\\label{app:cross_arch}\n\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. \\textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\\%: 3-seed mean$\\pm$std; other rows: seed 42.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.93$\\pm$0.19} & 8.38 & 1.21$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL PPL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity).\nTable~\\ref{tab:mistral_downstream} reports downstream task accuracy at 30\\% sparsity on Mistral-7B-v0.3 (3-seed). KL improves PPL ($-$17.3\\%) and commonsense tasks (WG +6.7pp) but MMLU is tied (43.3\\% vs.\\ 43.5\\%); ARC-c shows high seed variance ($\\sigma$=6.4pp); GSM8K reverses.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B-v0.3 downstream evaluation at 30\\% sparsity. $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); TEAL is deterministic (single run). ARC-c exhibits high seed variance ($\\sigma$=6.4pp).}\n\\label{tab:mistral_downstream}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\\\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa\nKL 30\\% & \\textbf{6.93$\\pm$0.19} & \\textbf{44.9$\\pm$6.4} & \\textbf{70.2$\\pm$1.2} & \\textbf{69.7$\\pm$0.8} & \\textbf{74.8$\\pm$0.4} & 43.3$\\pm$1.5 & 8.6$\\pm$2.2 \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456\nTEAL 30\\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & \\textbf{43.5} & \\textbf{15.9} \\\\ % exp_id: mistral_teal30_downstream\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Taxonomy Discussion}\n\\label{app:taxonomy}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2025spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-token} methods~\\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass; each mask decision's gradient reflects its joint effect with all other masks on the final distribution.\n\nSPON~\\cite{xu2025spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\\times$ coupled).\nDejaVu~\\cite{liu2023dejavu} and FastForward~\\cite{gautam2026fastforward} achieve per-token granularity but use BCE, where each neuron's gradient is independent of other mask states.\nD2DMoE~\\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.\nWe define \\emph{output-distribution alignment} as whether the training loss optimizes a quantity that composes across layers.\nKL on output logits directly optimizes next-token prediction loss, which does not suffer from error composition; per-layer MSE minimizes reconstruction error independently at each layer, but layer-wise optima do not compose---a mask minimizing FFN output error at layer $\\ell$ may amplify errors in layers $\\ell{+}1 \\ldots L$.\nThe SNR analysis (\\S\\ref{sec:method:gradient}) corroborates this: KL achieves the best masks despite $2.3\\times$ lower SNR than BCE, while MSE produces the worst masks.\nThe framework predicts that losses operating on output-level quantities should outperform intermediate-level losses, a hypothesis consistent with our MSE results and testable with alternative output-level objectives.\n\n\\section{Oracle Mask Provenance}\n\\label{app:oracle_provenance}\n\nC1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold (logits $> 0$, equivalent to $\\sigma > 0.5$); they reflect one specific training trajectory (optimizer state, data order, Gumbel noise).\nThe s42/s123/s456 consistency ($\\leq$1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.\n\n\\section{SPON Orthogonality}\n\\label{app:spon}\n\nSPON~\\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\nThe decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.\n\n\\section{Per-Layer KL Downstream Decomposition}\n\\label{app:perlayer_downstream}\n\nTable~\\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\\ coupling scope decomposition at 30\\% sparsity (\\S\\ref{sec:perlayer}). BoolQ's $\\approx$100\\% coupling is an upper bound confounded by high cross-seed variance ($\\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.\n\n\\begin{table}[h]\n\\centering\n\\caption{2D decomposition at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \\S\\ref{sec:perlayer}).}\n\\label{tab:perlayer_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\n& PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\\\\n\\midrule\nE2E KL & 8.81$\\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\\\\nPer-layer KL & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\\\\nMSE & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 & 64.5$\\pm$5.3 \\\\\n\\midrule\nTotal gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\\\\nSignal type (\\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\\approx$0 \\\\\nCoupling (\\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\\approx$100 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{$K{=}4$ Mismatch Control}\n\\label{app:k4_downstream}\n\nTable~\\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\\% sparsity.\nTraining with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\\ 1/32 layers masked during training, while inference applies all 32).\nThe gap closure column reports the fraction of the $K{=}1 \\to$ E2E KL gap closed by $K{=}4$.\n\n\\begin{table}[h]\n\\centering\n\\caption{3-seed $K{=}4$ mismatch control at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \\in \\{42, 123, 456\\}$). Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\\text{E2E} - K{=}1) \\times 100$.}\n\\label{tab:k4_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\n& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\\%) \\\\\n\\midrule\nPPL$\\downarrow$ & 8.89$\\pm$0.01 & 9.05$\\pm$0.02 & 8.81$\\pm$0.02 & 66.7 \\\\\nARC-c & 40.0$\\pm$1.3 & 39.9 & 43.7$\\pm$2.5 & 2.6 \\\\\nWG & 66.9$\\pm$0.2 & 65.9 & 68.9$\\pm$0.4 & 33.3 \\\\\nMMLU$^\\ast$ & 42.7$\\pm$1.4 & 38.6 & 40.7$\\pm$1.3 & $>$100 \\\\\nGSM8K & 7.0$\\pm$1.6 & 5.8 & 7.5$\\pm$0.1 & 70.6 \\\\\nBoolQ$^\\dagger$ & 67.7$\\pm$7.5 & 64.5$\\pm$11.5 & 73.7 & 34.8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize $^\\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\\% (Appendix~\\ref{app:constraint}).\n$^\\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}\n\\end{table}\n\n\\section{Per-Layer Sparsity Constraint Analysis}\n\\label{app:constraint}\n\nTo test the causal role of the KL predictor's learned per-layer allocation, we evaluate two inference-time interventions at 30\\% overall sparsity (seed 42, uniform allocation baseline):\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity constraint analysis. \\emph{Protect late}: cap L22--L28 sparsity $\\leq$30\\%; \\emph{Remove valley}: override L14--L18 sparsity to 30\\%. Budget redistributed to maintain 30\\% overall.}\n\\label{tab:constraint}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & PPL & ARC-c & MMLU & GSM8K \\\\\n\\midrule\nKL baseline (s42) & 8.82 & 40.8 & 40.6 & 7.4 \\\\\nProtect late layers & 9.26 & 42.4 & 40.7 & 6.5 \\\\\nRemove valley & 8.76 & 39.3 & 44.0 & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nProtecting late layers (L22--L28) does not improve knowledge-intensive metrics despite reducing their sparsity from 48--57\\% to $\\leq$30\\%, while worsening PPL by 5.2\\%.\nConversely, removing the protection valley (forcing L14--L18 to 30\\% instead of 14--18\\%) improves MMLU by +3.4pp and GSM8K by +1.6pp at the cost of ARC-c $-$1.5pp.\nThe KL predictor's learned allocation thus represents a task-dependent trade-off---prioritizing commonsense reasoning via middle-layer protection---rather than a uniformly optimal pattern.\nThis allocation trade-off also explains the $K{=}4$ MMLU anomaly (\\S\\ref{app:k4_downstream}): $K{=}4$'s near-uniform learned sparsity (std=0.003) inherently removes the valley, producing MMLU=43.5 comparable to the remove-valley condition (44.0).\n\n\\section{Per-Layer Sparsity Distribution}\n\\label{app:perlayer_sparsity}\n\nThe KL predictor at 30\\% target sparsity learns a non-uniform per-layer allocation that differs markedly from magnitude-based selection.\nAggregate sparsity is similar across broad regions (early L0--L7: KL 28.1\\% vs.\\ magnitude 27.5\\%; late L24--L31: 44.9\\% vs.\\ 47.2\\%), but middle layers (L8--L23) exhibit high internal variance despite similar averages (28.2\\% vs.\\ 27.3\\%).\nTable~\\ref{tab:perlayer_sparsity} highlights three sub-ranges.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity sub-ranges: KL predictor vs.\\ magnitude (LLaMA-3.1-8B, 30\\%, uniform allocation). Ranges denote min--max across layers in each group.}\n\\label{tab:perlayer_sparsity}\n\\begin{tabular}{lccc}\n\\toprule\nLayer Range & KL (\\%) & Mag (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nL8--L12 (high pruning) & 32--36 & 25--26 & $+$7 to $+$10 \\\\\nL14--L18 (protection valley) & 14--18 & 28--30 & $-$8 to $-$16 \\\\\nL22--L28 (aggressive pruning) & 48--57 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{C4 Training Data Control}\n\\label{app:c4_control}\n\nTo test whether WikiText-103's narrow domain drives the knowledge-task regression (\\S\\ref{sec:experiments}), we train the KL predictor on C4~\\cite{raffel2020c4} (diverse web text) under identical hyperparameters (1000 steps, 30\\% uniform, s42).\n\n\\begin{table}[h]\n\\centering\n\\caption{C4-trained vs.\\ WikiText-trained KL predictor (LLaMA-3.1-8B, 30\\% uniform, s42).}\n\\label{tab:c4_control}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\nTraining Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\\n\\midrule\nWikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe C4-trained predictor achieves comparable MMLU (40.0\\% vs.\\ 40.6\\%) but worse GSM8K (4.1\\% vs.\\ 7.4\\%) and higher PPL (11.55 vs.\\ 8.82), despite training on more diverse text.\nThis rules out training data composition as the primary cause of knowledge-task regression and supports the hypothesis that forward KL's mode-covering property structurally under-protects rare reasoning-critical activations. % exp_id: c4_control_eval\n\n\\section{Per-Layer Coupling Breadth Analysis}\n\\label{app:k_curve}\n\nWe vary the number of layers coupled per training step ($K$) from 1 (pure per-layer) to 32 (end-to-end), evaluating all predictors under TEAL uniform allocation at 30\\% sparsity on LLaMA-3.1-8B.\n\n\\begin{table}[h]\n\\centering\n\\caption{K-curve: coupling breadth vs.\\ predictor quality (30\\%, TEAL uniform, LLaMA-3.1-8B). All values are 3-seed mean$\\pm$std (s42/s123/s456) except $K{=}1$ downstream (single seed). ``---'' = not evaluated.}\n\\label{tab:k_curve}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{cccccccc}\n\\toprule\n$K$ & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\n1 & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & --- & --- \\\\\n2 & 10.75$\\pm$0.15 & 39.7$\\pm$1.2 & 63.2$\\pm$1.7 & 38.3$\\pm$3.2 & 2.8$\\pm$0.6 & 66.5$\\pm$1.0 & 73.5$\\pm$0.7 \\\\\n4 & 8.89$\\pm$0.01 & 40.0$\\pm$1.2 & 66.9$\\pm$0.2 & 42.7$\\pm$1.4 & 7.0$\\pm$1.6 & 67.8$\\pm$1.0 & 74.5$\\pm$0.5 \\\\\n8 & 9.00$\\pm$0.06 & 40.7$\\pm$1.0 & 68.7$\\pm$1.3 & 40.4$\\pm$0.6 & 6.8$\\pm$1.3 & 69.0$\\pm$1.1 & 75.1$\\pm$1.1 \\\\\n16 & 8.67$\\pm$0.02 & 41.9$\\pm$1.1 & 68.5$\\pm$0.9 & 40.9$\\pm$2.9 & 8.5$\\pm$1.2 & 70.1$\\pm$0.4 & 75.0$\\pm$0.8 \\\\\n32 (E2E) & 8.81$\\pm$0.02 & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nPPL exhibits a non-monotonic U-shape (Figure~\\ref{fig:k_curve_ppl}): $K{=}2$ is worst (10.75$\\pm$0.15), likely due to insufficient per-layer updates (${\\sim}$62 updates/layer vs.\\ ${\\sim}$250 at $K{=}8$). $K{=}16$ achieves the lowest PPL (8.67$\\pm$0.02), marginally better than E2E (8.81$\\pm$0.02). $K{=}16$ MMLU exhibits high seed variance (std=2.9; s42=44.0, s123=40.0, s456=38.7), with the 3-seed mean (40.9) indistinguishable from E2E (40.7$\\pm$1.3).\nThe signal type gap ($K{=}1$ KL 9.05 vs.\\ per-layer MSE 18.52$\\pm$1.68) of 9.47 PPL dwarfs the coupling breadth range within KL (best $K{=}16$ 8.67 vs.\\ worst $K{=}2$ 10.75 = 2.08 PPL), reinforcing that output-distribution alignment, not coupling scope, is the primary quality lever for PPL at this sparsity level. % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed, perlayer_kl_30_3seed, perlayer_kl_k4_3seed\n\n\\section{Licenses}\n\\label{app:licenses}\n\nLLaMA-3.1-8B is released under the Llama 3.1 Community License Agreement.\nMistral-7B-v0.3 is released under the Apache 2.0 License.\nQwen-2.5-14B is released under the Apache 2.0 License.\nWikiText-103 and WikiText-2~\\cite{merity2017pointer} are released under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).\nAll evaluation benchmarks (ARC, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA) are publicly available under their respective licenses.\nOur code will be released under the MIT License upon acceptance.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 610,
        "oldLines": 7,
        "newStart": 610,
        "newLines": 7,
        "lines": [
          " \\toprule",
          " Training Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\",
          " \\midrule",
          "-WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.85 / 74.81 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa",
          "+WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)",
          " C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval",
          " \\bottomrule",
          " \\end{tabular}}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 177_

<details open><summary>🔧 Tool call — Edit · `toolu_016MavkgZ7NEPvJmMQTsbzvb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "old_string": "C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval",
  "new_string": "C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.2 / 75.0 \\\\ % exp_id: c4_kl30_s42_eval (HS=69.24→69.2, PIQA=75.03→75.0 rounded)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "74d65b92-9a81-4647-9777-00014df647a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcQxWgTm55tphrARuV1w4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3508,
      "cache_read_input_tokens": 126465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3508
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-24T02:26:06.414Z_

<details><summary>↩ Tool result · `toolu_016MavkgZ7NEPvJmMQTsbzvb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "b897b92e-363d-45e3-b068-9dcd39380af0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "oldString": "C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval",
    "newString": "C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.2 / 75.0 \\\\ % exp_id: c4_kl30_s42_eval (HS=69.24→69.2, PIQA=75.03→75.0 rounded)",
    "originalFile": "\\appendix\n\n\\section{Inference Efficiency}\n\\label{app:latency}\n\nTable~\\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nMethod & Sparsity & ms/fwd & tok/s & Overhead \\\\\n\\midrule\nDense & 0\\% & 119.11$\\pm$0.57 & 17{,}195 & --- \\\\\n\\midrule\nKL predictor-only & 30\\% & 126.64$\\pm$0.70 & 16{,}172 & +6.3\\% \\\\ % exp_id: latency_bench\nKL predictor-only & 50\\% & 126.78$\\pm$0.31 & 16{,}154 & +6.4\\% \\\\ % exp_id: latency_bench\n\\midrule\nPredictor + compensation & 30\\% & 129.94$\\pm$0.75 & 15{,}761 & +9.1\\% \\\\ % exp_id: latency_bench\nPredictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe full KL-sparse pipeline adds 6.4\\% overhead to dense inference (126.78 vs.\\ 119.11\\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\\,ms (2.7\\%); the remainder arises from mask application and sparse FFN indexing.\nEliminating the compensation network saves an additional $\\sim$2.7\\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.\nThe overhead is near-identical at 30\\% and 50\\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.\n\nNote that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.\nThe pipeline adds $\\sim$6.4\\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.\nOur contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.\n\n\n\\section{Predictor Bottleneck Sensitivity}\n\\label{app:db_sensitivity}\n\nTable~\\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Predictor bottleneck sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}\n\\label{tab:db_sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$d_b$ & Params & TEAL global & $\\Delta$ & Per-token \\\\\n\\midrule\n64 & 38.2M (0.48\\%) & 12.076 & +0.9\\% & 10.16 \\\\ % exp_id: db_sensitivity_sweep\n128 & 75.9M (0.95\\%) & 11.963 & --- & 9.218 \\\\ % exp_id: db_sensitivity_sweep\n256 & 151.5M (1.89\\%) & 12.105 & +1.2\\% & 8.586 \\\\ % exp_id: db_sensitivity_sweep\n512 & 302.5M (3.77\\%) & 12.315 & +2.9\\% & 7.93 \\\\ % exp_id: db_sensitivity_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\\to$7.93).\nThis divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.\nThe $d_b{=}128$ configuration (75.9M params, $<$1\\% of base model) is therefore optimal for the TEAL inference protocol.\n\n\\subsection{Temperature Schedule Sensitivity}\n\\label{app:tau_sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature schedule sensitivity at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:tau_sensitivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n$\\tau$ Schedule & PPL$\\downarrow$ \\\\\n\\midrule\nFixed $\\tau{=}0.5$ & \\textbf{11.861} \\\\ % exp_id: tau_schedule_sweep\nLinear $1.0 \\to 0.1$ (default) & 11.963 \\\\ % exp_id: tau_schedule_sweep\nFixed $\\tau{=}0.1$ & 12.072 \\\\ % exp_id: tau_schedule_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature schedule has minimal impact ($<$1.8\\% PPL variation).\nThe linear annealing default is a conservative choice; even removing annealing entirely (fixed $\\tau{=}0.5$) yields comparable performance.\n\n\\subsection{Training Convergence}\n\\label{app:training_convergence}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training convergence at 50\\% sparsity (WikiText-2 PPL$\\downarrow$, TEAL global).}\n\\label{tab:training_convergence}\n\\small\n\\begin{tabular}{cc}\n\\toprule\nSteps & PPL$\\downarrow$ \\\\\n\\midrule\n200 & 15.158 \\\\ % exp_id: training_steps_sweep\n400 & 12.538 \\\\ % exp_id: training_steps_sweep\n600 & 12.046 \\\\ % exp_id: training_steps_sweep\n800 & 11.907 \\\\ % exp_id: training_steps_sweep\n1000 & \\textbf{11.906} \\\\ % exp_id: training_steps_sweep\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining converges rapidly: 95\\% of the quality gap closes by step 600, and performance saturates by step 800 ($\\Delta < 0.001$ between 800 and 1000 steps).\nOur default of 1000 steps provides a conservative margin.\n\n\n\\section{Geometric Penalty Schedule Dynamics}\n\\label{app:lagrangian}\n\nTable~\\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.\nThe geometric doubling pattern ($1 \\to 2 \\to 4 \\to 8 \\to \\ldots$) enables $\\lambda$ to reach steady state within $\\sim$10 steps; the deadzone ($\\epsilon = 0.02$) then stabilizes $\\lambda$ once actual sparsity is within $\\pm$2\\% of the target.\n\n\\begin{table}[h]\n\\centering\n\\caption{Geometric penalty schedule convergence across sparsity targets (margin $\\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}\n\\label{tab:lagrangian}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTarget $\\rho$ & $\\lambda_{\\max}$ & Final $\\lambda$ & Actual sparsity & Deviation \\\\\n\\midrule\n30\\% & 5000 & 5000 (cap) & 0.285 & 5.0\\% \\\\ % exp_id: kl_30pct_s42\n40\\% & 5000 & 625 & 0.398 & 0.5\\% \\\\ % exp_id: kl_40pct_s42\n50\\% & 1000 & 8 & 0.504 & 0.8\\% \\\\ % exp_id: kl_50pct_s42\n70\\% & 1000 & 1000 (cap) & 0.688 & 1.7\\% \\\\ % exp_id: kl_70pct_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 50\\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.\nAt 30\\% and 70\\%, the gap between the gate prior and target is larger, driving $\\lambda$ to its respective caps.\nThe 40\\% target converges to $\\lambda = 625$ with only 0.5\\% deviation; this precision reflects a regime where the target is reachable without $\\lambda$ saturation.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{lagrangian_dynamics.pdf}\n\\caption{Lagrangian controller dynamics for 30\\% sparsity target ($\\lambda_{\\max}=5000$). Left axis (log scale): penalty weight $\\lambda$ rises from $0.01$ to its cap once actual sparsity undershoots the target at $\\sim$step~150, exhibiting bang-bang oscillations before saturating. Right axis: actual sparsity (solid) converges from the natural density ($\\approx$0.41) toward the target (dashed) and stabilizes near 0.28.}\n\\label{fig:lagrangian_dynamics}\n\\end{figure}\n\nTemperature $\\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.\nA mild loss increase in the final $\\sim$100 steps is expected: as masks become more binary ($\\tau \\to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.\n\nThe controller reliably drives actual sparsity to within 5\\% of the target across all tested regimes, with $\\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.\nFor the 30\\% target, actual sparsity is $\\approx$28.5\\% (5\\% deviation). This does not affect conclusions: TEAL at 28.5\\% actual sparsity yields PPL 10.30 (vs.\\ 10.97 at exact 30\\%), a 0.67 PPL difference negligible relative to the KL vs.\\ TEAL gap (8.96 vs.\\ 10.97).\n\n\n\\section{Out-of-Distribution Evaluation}\n\\label{app:ood}\n\nTo address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\\cite{raffel2020c4} validation set under TEAL global allocation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Out-of-distribution evaluation on C4 validation (PPL$\\downarrow$). 30\\% KL reports 2-seed mean$\\pm$std; other entries use seed 42.}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{llc}\n\\toprule\nSparsity & Method & C4 PPL$\\downarrow$ \\\\\n\\midrule\n0\\% & Dense & 9.21 \\\\\n\\midrule\n30\\% & KL predictor (Ours) & \\textbf{16.03$\\pm$0.01} \\\\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123\n\\midrule\n\\multirow{2}{*}{50\\%} & KL predictor (Ours) & \\textbf{18.40} \\\\ % exp_id: eval_c4_ood_kl50\n& TEAL vanilla & 38.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the 30\\% sparsity level, the KL predictor achieves C4 PPL 16.03$\\pm$0.01 (2-seed, global allocation, $1.74\\times$ dense), confirming OOD generalization.\nAt 50\\%, the KL predictor achieves 52.5\\% relative advantage over TEAL (18.40 vs.\\ 38.75), comparable to the 50\\% advantage on WikiText-2 (11.92 vs.\\ 23.90), confirming that KL-trained predictions generalize across distributions.\n\n\\paragraph{Uniform Allocation.}\nUnder uniform allocation at 30\\%, C4 PPL across three seeds is 18.22 (s42), 16.37 (s123), 16.36 (s456), yielding mean 16.98$\\pm$1.07 ($1.84\\times$ dense). % exp_id: c4_ood_kl30_uniform_3seed\nThe cross-seed variance is substantially higher than in-domain: CV=6.3\\% on C4 vs.\\ 0.2\\% on WikiText-2 (PPL 8.81$\\pm$0.02), driven by seed 42's elevated C4 PPL (18.22 vs.\\ 16.37 for other seeds).\nGlobal allocation's cross-layer budget flexibility partially compensates for domain shift (PPL 16.03 global vs.\\ 16.98 uniform), consistent with the Limitations observation that the predictor partially overfits to training-domain activation patterns.\n\n\\paragraph{Downstream Task Robustness.}\nTable~\\ref{tab:ood_downstream} compares downstream performance when the predictor generates masks from C4 text (OOD) vs.\\ WikiText (in-domain), both at 30\\% uniform allocation (seed 42). All six benchmarks show $\\Delta$$\\leq$1.1pp, confirming that predictor masks are robust to calibration domain shift. % exp_id: c4_ood_downstream_kl30, bench_kl30_uniform, kl30_uniform_hellaswag_piqa\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream task robustness to calibration domain shift (KL 30\\% uniform, seed 42). WikiText: predictor masks from in-domain text; C4: masks from OOD text. Metrics: acc\\_norm (ARC-c, HS, PIQA), acc (WG, MMLU), exact\\_match (GSM8K).}\n\\label{tab:ood_downstream}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nCalibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nWikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\\\ % exp_id: c4_ood_downstream_kl30\n\\midrule\n$\\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Layer Retention Analysis}\n\\label{app:retention}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{per_layer_retention_chart.pdf}\n\\caption{Per-layer neuron retention under global top-$k$ allocation at 30\\%, 50\\%, and 70\\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\\% (L31) even at 30\\% sparsity. At 70\\%, starvation extends to mid-layers (L10--12: 16.7--20.1\\%), explaining the transition to the capacity-limited regime.}\n\\label{fig:retention}\n\\end{figure}\n\n\n\\section{Training Stability}\n\\label{app:stability}\n\nThree-seed evaluation ($s \\in \\{42, 123, 456\\}$) at 50\\% sparsity under uniform allocation yields PPL $11.92 \\pm 0.07$ (CV=0.6\\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform\nDownstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\n\nUnder global allocation at 50\\%, MMLU is $28.3 \\pm 0.7$\\%; the near-random performance is capacity-limited rather than seed-sensitive ($\\sigma$=0.7pp vs.\\ 9.5pp at 30\\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\nThe low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.\n\n\\subsection{Cross-Seed Mask Consistency}\n\\label{app:cross_seed_jaccard}\n\nTo assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30\n\nThe mean cross-seed Jaccard distance is 0.363 (IoU = 0.637), substantially lower than the KL-vs-magnitude divergence (0.46--0.68), confirming that KL-discovered patterns form a distinct cluster from magnitude-based masks.\nPer-layer divergence follows a U-shaped pattern: lowest at embedding-adjacent layers (L0: 0.33), peaking at early layers (L1: 0.41), with a mid-network valley (L12--14: 0.33). The random baseline Jaccard distance is 0.462.\n\nWhile specific mask configurations vary moderately across seeds (Jaccard distance 36.3\\%), the resulting PPL is highly stable (8.81$\\pm$0.02, CV=0.2\\%), suggesting multiple near-equivalent optima in the activation mask space.\nThe cross-seed divergence (36.3\\%) is substantially lower than the KL-vs-magnitude divergence (46--68\\%), confirming that KL discovers effective patterns that cluster distinctly from magnitude-based selection.\n\n\n\\section{MSE Baseline Configuration}\n\\label{app:mse_config}\n\nThe MSE predictor uses identical architecture (two-layer MLP, bottleneck $d_b{=}128$), training data (WikiText-103, 1000 steps), optimizer (AdamW, lr=$1{\\times}10^{-3}$, weight decay $1{\\times}10^{-2}$, cosine decay), Gumbel-Sigmoid mask generation ($\\tau$: $1.0 \\to 0.1$), and adaptive Lagrangian sparsity control as the KL and BCE predictors.\nThe only difference is the loss target: per-layer $\\|\\mathbf{W}_d^{(\\ell)}(\\tilde{\\mathbf{m}}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}) - \\mathbf{y}_{\\text{dense}}^{(\\ell)}\\|_2^2$, replacing the end-to-end KL divergence.\nThis controlled comparison isolates the effect of output-distribution alignment: all three predictors see identical data in identical order with identical architectures; only the loss function differs. % exp_id: mse30_uniform_s42, mse50_uniform_s42\n\nMSE uses $\\lambda_{\\max}{=}1000$ (vs.\\ KL's 5000) because MSE's per-layer gradient magnitude is approximately $5\\times$ larger than KL's end-to-end gradient, requiring proportionally less penalty pressure to achieve comparable sparsity control. Both reach their target sparsity within 110 steps.\nAt 50\\% target, MSE converges to the target sparsity for seed 42; however, with seed 123, sparsity reaches only 5.1\\% under the same $\\lambda_{\\max}$ cap (eval PPL$=$15{,}789, random-level), indicating high sensitivity to initialization---a failure mode not observed with KL-based losses.\nAt 30\\%, MSE achieves 27.7\\% actual sparsity for s42 (gap 2.3pp).\nThe 3-seed MSE mean (18.52$\\pm$1.68; s42=20.43, s123=17.73, s456=17.39) is still $1.7\\times$ worse than TEAL (10.82), confirming that the performance deficit stems from the loss function, not insufficient sparsity pressure.\n\n\n\\section{Extended SNR Analysis}\n\\label{app:snr_extended}\n\nFigure~\\ref{fig:snr_trajectory} plots gradient SNR across the full 1000-step training for both KL and BCE predictors, measured at 14 checkpoints (LLaMA-3.1-8B, C4) with 95\\% bootstrap confidence intervals.\nFrom step 100 onward, BCE maintains consistently higher SNR than KL (2.3--17$\\times$ depending on training phase), with the gap narrowing toward convergence ($2.3\\times$ at step 1000: $2.026{\\times}10^{-3}$ vs.\\ $8.78{\\times}10^{-4}$). % exp_id: snr_full_curve_1000steps\nDespite KL's noisier gradient signal, KL-trained predictors produce substantially better masks (Table~\\ref{tab:main}), confirming that \\emph{target alignment} matters more than gradient clarity for mask quality.\nBCE's higher SNR reflects its simpler per-neuron classification objective, which concentrates gradients on individual neuron decisions; KL's coupled gradient distributes signal across all mask decisions jointly, yielding lower SNR but discovering compositionally superior mask patterns (\\S\\ref{sec:method:gradient}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{snr_trajectory.pdf}\n\\caption{Gradient SNR trajectory across 1000 training steps. BCE (orange) maintains consistently higher SNR than KL (blue) from step 100 onward (2.3--17$\\times$), yet KL produces superior masks (Table~\\ref{tab:main}), suggesting that target alignment matters more than gradient clarity for mask quality.}\n\\label{fig:snr_trajectory}\n\\end{figure}\n\n\n\\section{Extended Downstream Evaluation}\n\\label{app:downstream}\n\nTable~\\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\\% uniform: 3-seed mean$\\pm$std; others: seed 42.}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Method & HellaSwag & PIQA \\\\\n\\midrule\n0\\% & Dense & \\textbf{82.35} & \\textbf{80.90} \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& KL uniform & \\textbf{71.07$\\pm$0.54} & \\textbf{74.95$\\pm$0.25} \\\\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)\n& TEAL uniform & 63.31 & 72.80 \\\\ % exp_id: bench_teal30_uniform_6task\n& BCE isocompute & 62.81 & 74.21 \\\\ % exp_id: bce_isocompute_30u_hellaswag_piqa\n\\midrule\n\\multirow{3}{*}{50\\%}\n& KL global & \\textbf{58.95} & \\textbf{69.48} \\\\ % exp_id: hellaswag_piqa_kl50_global\n& KL uniform & 56.66 & 69.10 \\\\ % exp_id: hellaswag_piqa_kl50_uniform\n& TEAL uniform & 39.35 & 63.66 \\\\ % exp_id: bench_teal50_uniform_6task\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 30\\%, the KL predictor retains 86.3\\% of dense HellaSwag accuracy (71.07$\\pm$0.54 vs.\\ 82.35, 3-seed) and 92.6\\% of PIQA (74.95$\\pm$0.25 vs.\\ 80.90), confirming moderate degradation on non-reasoning tasks.\nAt 50\\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\\S\\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).\n\n\n\\section{Compensation Training Convergence}\n\\label{app:comp_convergence}\n\nAll compensation networks~\\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\\% s42 (final loss 0.70), 30\\% s456 (0.68), 50\\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42\n\n\n\\section{Qwen-2.5-14B Detailed Results}\n\\label{app:14b}\n\n\\begin{table}[h]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% nominal sparsity. Actual sparsity differs: KL 29.6\\% (3-seed), TEAL 29.3\\% (target 30\\%). \\textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\\% native sparsity (\\S\\ref{sec:method:gradient}), so forced global top-$k$ is used.}\n\\label{tab:14b}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \\textbf{75.01} & \\textbf{77.37} \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 & 70.51 & 74.70 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} & 53.43 & 68.28 \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{8}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.90} & 53.50 & \\textbf{72.82} & 63.55 & 32.0$\\pm$5.2 & \\textbf{72.68$\\pm$0.2} & \\textbf{76.01$\\pm$1.1} \\\\ % exp_id: qwen14b_kl30_uniform (3-seed s42/s123/s456)\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & \\textbf{52.1} & 67.72 & 74.70 \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nUnder global allocation, BCE's HellaSwag drops to 53.43\\% ($-$17pp vs.\\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval\n\n\\section{Full Allocation Analysis}\n\\label{app:alloc_full}\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation summary (LLaMA-3.1-8B). $\\pm$: 3-seed; $^\\ast$high seed variance.}\n\\label{tab:phase}\n\\footnotesize\n\\begin{tabular}{llcc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & MMLU \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & 35.7$\\pm$9.5$^\\ast$ \\\\ % exp_id: kl30_3seed_global\n& Uniform & \\textbf{8.81$\\pm$0.02} & \\textbf{40.7$\\pm$1.3} \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\n& Uniform & 11.92$\\pm$0.07 & 28.0$\\pm$0.6 \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:phase_full} extends Table~\\ref{tab:phase} with all downstream metrics.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Full allocation analysis: global top-$k$ vs.\\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); others: seed 42. $^\\ast$High MMLU seed variance (individual seeds span 25.3--43.5\\%).}\n\\label{tab:phase_full}\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n\\multirow{2}{*}{25\\%}\n& Global & \\textbf{8.17} & 45.4 & 70.6 & \\textbf{46.6} & \\textbf{11.5} \\\\\n& Uniform & 8.23 & \\textbf{46.5} & \\textbf{71.8} & 44.0 & 11.0 \\\\\n\\midrule\n\\multirow{2}{*}{30\\%}\n& Global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5$^\\ast$ & \\textbf{8.0$\\pm$0.7} \\\\\n& Uniform & \\textbf{8.81$\\pm$0.02} & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & \\textbf{40.7$\\pm$1.3} & 7.5$\\pm$0.1 \\\\\n\\midrule\n\\multirow{2}{*}{35\\%}\n& Global & \\textbf{9.31} & \\textbf{38.9} & \\textbf{67.6} & \\textbf{40.4} & \\textbf{7.7} \\\\\n& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\\\\n\\midrule\n\\multirow{2}{*}{40\\%}\n& Global & \\textbf{10.14} & 39.5 & \\textbf{67.5} & \\textbf{39.5} & \\textbf{6.6} \\\\\n& Uniform & 10.76 & \\textbf{39.6} & 63.1 & 35.5 & 3.6 \\\\\n\\midrule\n\\multirow{2}{*}{45\\%}\n& Global & \\textbf{10.80} & \\textbf{39.2} & \\textbf{64.6} & 30.4 & \\textbf{3.0} \\\\\n& Uniform & 10.95 & 37.6 & 63.6 & \\textbf{30.6} & 2.7 \\\\\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.3$\\pm$1.1} \\\\\n& Uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Mask Pattern Visualization}\n\\label{app:mask_viz}\n\nFigure~\\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity.\nFigure~\\ref{fig:scatter} shows per-neuron importance scores at layer 16.\nFigure~\\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{neuron_scatter_layer16.pdf}\n\\caption{KL vs.\\ magnitude importance scores for layer 16 neurons at 50\\% sparsity. 41\\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}\n\\label{fig:scatter}\n\\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_divergence_heatmap.pdf}\n\\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\\% and 50\\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\\%) and increases with sparsity across all layers.}\n\\label{fig:mask_heatmap}\n\\end{figure*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{mask_comparison.pdf}\n\\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\\% and 50\\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\\%, 0.74 at 50\\%).}\n\\label{fig:mask_comparison}\n\\end{figure*}\n\n\n\\section{Cross-Architecture Comparison}\n\\label{app:cross_arch}\n\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. \\textbf{Note:} LLaMA results use global top-$k$ allocation; Mistral results use uniform allocation. Mistral 30\\%: 3-seed mean$\\pm$std; other rows: seed 42.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.93$\\pm$0.19} & 8.38 & 1.21$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL PPL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity).\nTable~\\ref{tab:mistral_downstream} reports downstream task accuracy at 30\\% sparsity on Mistral-7B-v0.3 (3-seed). KL improves PPL ($-$17.3\\%) and commonsense tasks (WG +6.7pp) but MMLU is tied (43.3\\% vs.\\ 43.5\\%); ARC-c shows high seed variance ($\\sigma$=6.4pp); GSM8K reverses.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B-v0.3 downstream evaluation at 30\\% sparsity. $\\pm$: 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); TEAL is deterministic (single run). ARC-c exhibits high seed variance ($\\sigma$=6.4pp).}\n\\label{tab:mistral_downstream}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\\\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa\nKL 30\\% & \\textbf{6.93$\\pm$0.19} & \\textbf{44.9$\\pm$6.4} & \\textbf{70.2$\\pm$1.2} & \\textbf{69.7$\\pm$0.8} & \\textbf{74.8$\\pm$0.4} & 43.3$\\pm$1.5 & 8.6$\\pm$2.2 \\\\ % exp_id: mistral_kl30_s42, mistral_kl30_s123, mistral_kl30_s456\nTEAL 30\\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & \\textbf{43.5} & \\textbf{15.9} \\\\ % exp_id: mistral_teal30_downstream\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Taxonomy Discussion}\n\\label{app:taxonomy}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2025spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-token} methods~\\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass; each mask decision's gradient reflects its joint effect with all other masks on the final distribution.\n\nSPON~\\cite{xu2025spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\\times$ coupled).\nDejaVu~\\cite{liu2023dejavu} and FastForward~\\cite{gautam2026fastforward} achieve per-token granularity but use BCE, where each neuron's gradient is independent of other mask states.\nD2DMoE~\\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.\nWe define \\emph{output-distribution alignment} as whether the training loss optimizes a quantity that composes across layers.\nKL on output logits directly optimizes next-token prediction loss, which does not suffer from error composition; per-layer MSE minimizes reconstruction error independently at each layer, but layer-wise optima do not compose---a mask minimizing FFN output error at layer $\\ell$ may amplify errors in layers $\\ell{+}1 \\ldots L$.\nThe SNR analysis (\\S\\ref{sec:method:gradient}) corroborates this: KL achieves the best masks despite $2.3\\times$ lower SNR than BCE, while MSE produces the worst masks.\nThe framework predicts that losses operating on output-level quantities should outperform intermediate-level losses, a hypothesis consistent with our MSE results and testable with alternative output-level objectives.\n\n\\section{Oracle Mask Provenance}\n\\label{app:oracle_provenance}\n\nC1's oracle masks are extracted from a converged KL predictor and binarized via hard threshold (logits $> 0$, equivalent to $\\sigma > 0.5$); they reflect one specific training trajectory (optimizer state, data order, Gumbel noise).\nThe s42/s123/s456 consistency ($\\leq$1.70pp) provides partial evidence of robustness, but does not rule out trajectory-dependent confounds.\n\n\\section{SPON Orthogonality}\n\\label{app:spon}\n\nSPON~\\cite{xu2025spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\nThe decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.\n\n\\section{Per-Layer KL Downstream Decomposition}\n\\label{app:perlayer_downstream}\n\nTable~\\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\\ coupling scope decomposition at 30\\% sparsity (\\S\\ref{sec:perlayer}). BoolQ's $\\approx$100\\% coupling is an upper bound confounded by high cross-seed variance ($\\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.\n\n\\begin{table}[h]\n\\centering\n\\caption{2D decomposition at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \\S\\ref{sec:perlayer}).}\n\\label{tab:perlayer_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\n& PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\\\\n\\midrule\nE2E KL & 8.81$\\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\\\\nPer-layer KL & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\\\\nMSE & 18.52$\\pm$1.68 & 35.8$\\pm$4.1 & 59.8$\\pm$2.6 & 30.7$\\pm$2.6 & 2.3$\\pm$0.7 & 64.5$\\pm$5.3 \\\\\n\\midrule\nTotal gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\\\\nSignal type (\\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\\approx$0 \\\\\nCoupling (\\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\\approx$100 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{$K{=}4$ Mismatch Control}\n\\label{app:k4_downstream}\n\nTable~\\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\\% sparsity.\nTraining with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\\ 1/32 layers masked during training, while inference applies all 32).\nThe gap closure column reports the fraction of the $K{=}1 \\to$ E2E KL gap closed by $K{=}4$.\n\n\\begin{table}[h]\n\\centering\n\\caption{3-seed $K{=}4$ mismatch control at 30\\% sparsity (LLaMA-3.1-8B, uniform allocation, $s \\in \\{42, 123, 456\\}$). Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform). Gap closure $= (K{=}4 - K{=}1) / (\\text{E2E} - K{=}1) \\times 100$.}\n\\label{tab:k4_downstream}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\n& $K{=}4$ (3-seed) & $K{=}1$ (3-seed) & E2E KL (3-seed) & Gap closure (\\%) \\\\\n\\midrule\nPPL$\\downarrow$ & 8.89$\\pm$0.01 & 9.05$\\pm$0.02 & 8.81$\\pm$0.02 & 66.7 \\\\\nARC-c & 40.0$\\pm$1.3 & 39.9 & 43.7$\\pm$2.5 & 2.6 \\\\\nWG & 66.9$\\pm$0.2 & 65.9 & 68.9$\\pm$0.4 & 33.3 \\\\\nMMLU$^\\ast$ & 42.7$\\pm$1.4 & 38.6 & 40.7$\\pm$1.3 & $>$100 \\\\\nGSM8K & 7.0$\\pm$1.6 & 5.8 & 7.5$\\pm$0.1 & 70.6 \\\\\nBoolQ$^\\dagger$ & 67.7$\\pm$7.5 & 64.5$\\pm$11.5 & 73.7 & 34.8 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize $^\\ast$MMLU $K{=}4$ systematically exceeds E2E across all 3 seeds; attributable to $K{=}4$'s near-uniform per-layer sparsity (std=0.003) matching uniform eval allocation. Independently confirmed: removing the predictor's middle-layer valley yields MMLU=44.0\\% (Appendix~\\ref{app:constraint}).\n$^\\dagger$BoolQ exhibits high inter-seed variance for both $K{=}4$ (std=7.5) and $K{=}1$ (std=11.5); gap closure unreliable.}\n\\end{table}\n\n\\section{Per-Layer Sparsity Constraint Analysis}\n\\label{app:constraint}\n\nTo test the causal role of the KL predictor's learned per-layer allocation, we evaluate two inference-time interventions at 30\\% overall sparsity (seed 42, uniform allocation baseline):\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity constraint analysis. \\emph{Protect late}: cap L22--L28 sparsity $\\leq$30\\%; \\emph{Remove valley}: override L14--L18 sparsity to 30\\%. Budget redistributed to maintain 30\\% overall.}\n\\label{tab:constraint}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & PPL & ARC-c & MMLU & GSM8K \\\\\n\\midrule\nKL baseline (s42) & 8.82 & 40.8 & 40.6 & 7.4 \\\\\nProtect late layers & 9.26 & 42.4 & 40.7 & 6.5 \\\\\nRemove valley & 8.76 & 39.3 & 44.0 & 9.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nProtecting late layers (L22--L28) does not improve knowledge-intensive metrics despite reducing their sparsity from 48--57\\% to $\\leq$30\\%, while worsening PPL by 5.2\\%.\nConversely, removing the protection valley (forcing L14--L18 to 30\\% instead of 14--18\\%) improves MMLU by +3.4pp and GSM8K by +1.6pp at the cost of ARC-c $-$1.5pp.\nThe KL predictor's learned allocation thus represents a task-dependent trade-off---prioritizing commonsense reasoning via middle-layer protection---rather than a uniformly optimal pattern.\nThis allocation trade-off also explains the $K{=}4$ MMLU anomaly (\\S\\ref{app:k4_downstream}): $K{=}4$'s near-uniform learned sparsity (std=0.003) inherently removes the valley, producing MMLU=43.5 comparable to the remove-valley condition (44.0).\n\n\\section{Per-Layer Sparsity Distribution}\n\\label{app:perlayer_sparsity}\n\nThe KL predictor at 30\\% target sparsity learns a non-uniform per-layer allocation that differs markedly from magnitude-based selection.\nAggregate sparsity is similar across broad regions (early L0--L7: KL 28.1\\% vs.\\ magnitude 27.5\\%; late L24--L31: 44.9\\% vs.\\ 47.2\\%), but middle layers (L8--L23) exhibit high internal variance despite similar averages (28.2\\% vs.\\ 27.3\\%).\nTable~\\ref{tab:perlayer_sparsity} highlights three sub-ranges.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-layer sparsity sub-ranges: KL predictor vs.\\ magnitude (LLaMA-3.1-8B, 30\\%, uniform allocation). Ranges denote min--max across layers in each group.}\n\\label{tab:perlayer_sparsity}\n\\begin{tabular}{lccc}\n\\toprule\nLayer Range & KL (\\%) & Mag (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nL8--L12 (high pruning) & 32--36 & 25--26 & $+$7 to $+$10 \\\\\nL14--L18 (protection valley) & 14--18 & 28--30 & $-$8 to $-$16 \\\\\nL22--L28 (aggressive pruning) & 48--57 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{C4 Training Data Control}\n\\label{app:c4_control}\n\nTo test whether WikiText-103's narrow domain drives the knowledge-task regression (\\S\\ref{sec:experiments}), we train the KL predictor on C4~\\cite{raffel2020c4} (diverse web text) under identical hyperparameters (1000 steps, 30\\% uniform, s42).\n\n\\begin{table}[h]\n\\centering\n\\caption{C4-trained vs.\\ WikiText-trained KL predictor (LLaMA-3.1-8B, 30\\% uniform, s42).}\n\\label{tab:c4_control}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccccc}\n\\toprule\nTraining Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\\n\\midrule\nWikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)\nC4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe C4-trained predictor achieves comparable MMLU (40.0\\% vs.\\ 40.6\\%) but worse GSM8K (4.1\\% vs.\\ 7.4\\%) and higher PPL (11.55 vs.\\ 8.82), despite training on more diverse text.\nThis rules out training data composition as the primary cause of knowledge-task regression and supports the hypothesis that forward KL's mode-covering property structurally under-protects rare reasoning-critical activations. % exp_id: c4_control_eval\n\n\\section{Per-Layer Coupling Breadth Analysis}\n\\label{app:k_curve}\n\nWe vary the number of layers coupled per training step ($K$) from 1 (pure per-layer) to 32 (end-to-end), evaluating all predictors under TEAL uniform allocation at 30\\% sparsity on LLaMA-3.1-8B.\n\n\\begin{table}[h]\n\\centering\n\\caption{K-curve: coupling breadth vs.\\ predictor quality (30\\%, TEAL uniform, LLaMA-3.1-8B). All values are 3-seed mean$\\pm$std (s42/s123/s456) except $K{=}1$ downstream (single seed). ``---'' = not evaluated.}\n\\label{tab:k_curve}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{cccccccc}\n\\toprule\n$K$ & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\n1 & 9.05$\\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & --- & --- \\\\\n2 & 10.75$\\pm$0.15 & 39.7$\\pm$1.2 & 63.2$\\pm$1.7 & 38.3$\\pm$3.2 & 2.8$\\pm$0.6 & 66.5$\\pm$1.0 & 73.5$\\pm$0.7 \\\\\n4 & 8.89$\\pm$0.01 & 40.0$\\pm$1.2 & 66.9$\\pm$0.2 & 42.7$\\pm$1.4 & 7.0$\\pm$1.6 & 67.8$\\pm$1.0 & 74.5$\\pm$0.5 \\\\\n8 & 9.00$\\pm$0.06 & 40.7$\\pm$1.0 & 68.7$\\pm$1.3 & 40.4$\\pm$0.6 & 6.8$\\pm$1.3 & 69.0$\\pm$1.1 & 75.1$\\pm$1.1 \\\\\n16 & 8.67$\\pm$0.02 & 41.9$\\pm$1.1 & 68.5$\\pm$0.9 & 40.9$\\pm$2.9 & 8.5$\\pm$1.2 & 70.1$\\pm$0.4 & 75.0$\\pm$0.8 \\\\\n32 (E2E) & 8.81$\\pm$0.02 & 43.7$\\pm$2.5 & 68.9$\\pm$0.4 & 40.7$\\pm$1.3 & 7.5$\\pm$0.1 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nPPL exhibits a non-monotonic U-shape (Figure~\\ref{fig:k_curve_ppl}): $K{=}2$ is worst (10.75$\\pm$0.15), likely due to insufficient per-layer updates (${\\sim}$62 updates/layer vs.\\ ${\\sim}$250 at $K{=}8$). $K{=}16$ achieves the lowest PPL (8.67$\\pm$0.02), marginally better than E2E (8.81$\\pm$0.02). $K{=}16$ MMLU exhibits high seed variance (std=2.9; s42=44.0, s123=40.0, s456=38.7), with the 3-seed mean (40.9) indistinguishable from E2E (40.7$\\pm$1.3).\nThe signal type gap ($K{=}1$ KL 9.05 vs.\\ per-layer MSE 18.52$\\pm$1.68) of 9.47 PPL dwarfs the coupling breadth range within KL (best $K{=}16$ 8.67 vs.\\ worst $K{=}2$ 10.75 = 2.08 PPL), reinforcing that output-distribution alignment, not coupling scope, is the primary quality lever for PPL at this sparsity level. % exp_id: k_curve_k2_3seed, k_curve_k8_3seed, k_curve_k16_3seed, perlayer_kl_30_3seed, perlayer_kl_k4_3seed\n\n\\section{Licenses}\n\\label{app:licenses}\n\nLLaMA-3.1-8B is released under the Llama 3.1 Community License Agreement.\nMistral-7B-v0.3 is released under the Apache 2.0 License.\nQwen-2.5-14B is released under the Apache 2.0 License.\nWikiText-103 and WikiText-2~\\cite{merity2017pointer} are released under the Creative Commons Attribution-ShareAlike License (CC BY-SA 3.0).\nAll evaluation benchmarks (ARC, WinoGrande, MMLU, GSM8K, HellaSwag, PIQA) are publicly available under their respective licenses.\nOur code will be released under the MIT License upon acceptance.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 611,
        "oldLines": 7,
        "newStart": 611,
        "newLines": 7,
        "lines": [
          " Training Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\",
          " \\midrule",
          " WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)",
          "-C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.24 / 75.03 \\\\ % exp_id: c4_kl30_s42_eval",
          "+C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.2 / 75.0 \\\\ % exp_id: c4_kl30_s42_eval (HS=69.24→69.2, PIQA=75.03→75.0 rounded)",
          " \\bottomrule",
          " \\end{tabular}}",
          " \\end{table}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 179_

Now let me verify the edits and check for any remaining inconsistencies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "3c6ad7d0-be64-4de9-91b1-7c8de40140d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyayBPH9kjWH8nXuKURcyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 129973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 872
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 180_

<details open><summary>🔧 Tool call — Grep · `toolu_01FTQ4FBBkrBJrLdmdwunJw4`</summary>

```json
{
  "pattern": "11\\.84",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "9a10d510-d038-4a13-a1a1-05c87a0de3ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyayBPH9kjWH8nXuKURcyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 129973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 872
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-24T02:26:12.267Z_

<details><summary>↩ Tool result · `toolu_01FTQ4FBBkrBJrLdmdwunJw4`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "0721249c-8665-41cb-ace8-800eb0682c99",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---


### Tool call

_source line 182_

<details open><summary>🔧 Tool call — Read · `toolu_01E9FsXTqT2pcUuu7ABKFKX7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": 60,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "0c3e08ca-4fa7-4e29-beee-5a07a8fcfbf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyayBPH9kjWH8nXuKURcyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 129973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 872
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-24T02:26:12.898Z_

<details><summary>↩ Tool result · `toolu_01E9FsXTqT2pcUuu7ABKFKX7`</summary>

```text
60	\multirow{5}{*}{50\%}
61	& TEAL uniform & 23.90 & 27.47 & 54.38 & \textbf{29.26} & 1.74 \\ % exp_id: teal50_uniform
62	& BCE (2700 steps)$^\ast$ & 28.13$\pm$0.20 & 27.6$\pm$0.6 & 51.8$\pm$0.6 & 26.1$\pm$0.5 & 2.1$\pm$0.2 \\ % exp_id: bce50_3seed
63	& MSE uniform & 229.26 & 25.00 & 50.59 & 23.79 & 1.59 \\ % exp_id: mse50_uniform_s42
64	& KL global (Ours) & \textbf{11.79$\pm$0.07} & \textbf{36.5$\pm$3.3} & \textbf{63.9$\pm$0.4} & 28.3$\pm$0.7 & \textbf{2.3$\pm$1.1} \\ % exp_id: bench_kl50_global (s42 PPL=11.79), kl50_global_s123_reeval (s123 PPL=11.72), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456 PPL=11.86)
65	& KL uniform & 11.92$\pm$0.07 & 33.8$\pm$1.2 & 62.9$\pm$0.1 & 28.0$\pm$0.6 & 2.2$\pm$0.1 \\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456
66	\bottomrule
67	\end{tabular}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "bb43950c-1a3b-484f-8bb9-cc9749d51c4a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\multirow{5}{*}{50\\%}\n& TEAL uniform & 23.90 & 27.47 & 54.38 & \\textbf{29.26} & 1.74 \\\\ % exp_id: teal50_uniform\n& BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed\n& MSE uniform & 229.26 & 25.00 & 50.59 & 23.79 & 1.59 \\\\ % exp_id: mse50_uniform_s42\n& KL global (Ours) & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & 28.3$\\pm$0.7 & \\textbf{2.3$\\pm$1.1} \\\\ % exp_id: bench_kl50_global (s42 PPL=11.79), kl50_global_s123_reeval (s123 PPL=11.72), kl50_global_s123_downstream_v2 (s123 downstream), kl50_global_s456_eval (s456 PPL=11.86)\n& KL uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456\n\\bottomrule\n\\end{tabular}}",
      "numLines": 8,
      "startLine": 60,
      "totalLines": 197
    }
  }
}
```

</details>

---


### Assistant

_source line 184_

All "11.84" references are gone. Let me also verify the appendix edits and check for any cross-references to the old downstream values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "f32e993d-9693-4a0a-a496-5a8ee87e4d9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7jSsvJCnAc4yrLUakD7Yi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 130845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 860
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 185_

<details open><summary>🔧 Tool call — Grep · `toolu_01VMHv2ZyeTJ8p9FGJivY8Gj`</summary>

```json
{
  "pattern": "36\\.3.*3\\.2|63\\.8.*0\\.3|2\\.7.*1\\.3",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "5744eff5-dbd9-46e4-8b58-77cc8566d147",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7jSsvJCnAc4yrLUakD7Yi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 130845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 860
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 186 · 2026-05-24T02:26:24.092Z_

<details><summary>↩ Tool result · `toolu_01VMHv2ZyeTJ8p9FGJivY8Gj`</summary>

```text
paper/experiments.tex:158:[Omitted long matching line]
paper/appendix.tex:542:MMLU$^\ast$ & 42.7$\pm$1.4 & 38.6 & 40.7$\pm$1.3 & $>$100 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "b5f693aa-4434-493f-bf25-c2f4d1837e4d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:158:[Omitted long matching line]\npaper/appendix.tex:542:MMLU$^\\ast$ & 42.7$\\pm$1.4 & 38.6 & 40.7$\\pm$1.3 & $>$100 \\\\",
    "numLines": 2
  }
}
```

</details>

---


### Tool call

_source line 187_

<details open><summary>🔧 Tool call — Read · `toolu_01Gam2SEPbxTHNDbGAZTzBTJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": 610,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "8b70eab8-f250-413f-841a-37f348b13620",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7jSsvJCnAc4yrLUakD7Yi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 130845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 860
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 188 · 2026-05-24T02:26:24.582Z_

<details><summary>↩ Tool result · `toolu_01Gam2SEPbxTHNDbGAZTzBTJ`</summary>

```text
610	\toprule
611	Training Data & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\
612	\midrule
613	WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)
614	C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.2 / 75.0 \\ % exp_id: c4_kl30_s42_eval (HS=69.24→69.2, PIQA=75.03→75.0 rounded)
615	\bottomrule
616	\end{tabular}}
617	\end{table}
618	
619	The C4-trained predictor achieves comparable MMLU (40.0\% vs.\ 40.6\%) but worse GSM8K (4.1\% vs.\ 7.4\%) and higher PPL (11.55 vs.\ 8.82), despite training on more diverse text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "861dfc1d-6fc6-4694-9623-b246765aad4b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "\\toprule\nTraining Data & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS / PIQA \\\\\n\\midrule\nWikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)\nC4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.2 / 75.0 \\\\ % exp_id: c4_kl30_s42_eval (HS=69.24→69.2, PIQA=75.03→75.0 rounded)\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe C4-trained predictor achieves comparable MMLU (40.0\\% vs.\\ 40.6\\%) but worse GSM8K (4.1\\% vs.\\ 7.4\\%) and higher PPL (11.55 vs.\\ 8.82), despite training on more diverse text.",
      "numLines": 10,
      "startLine": 610,
      "totalLines": 672
    }
  }
}
```

</details>

---


### Assistant

_source line 189_

<details><summary>Logged reasoning block</summary>

```text
Let me check the grep results for old values. It found:
1. experiments.tex:158 — let me check what this line says
2. appendix.tex:542 — this is about MMLU K=4 analysis, not related to Fix 1

Let me read line 158 of experiments.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "bc638a81-b767-44c6-9853-8f0c7988dea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SQXfy45PdX1o1ooza1s2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 131705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 190_

<details open><summary>🔧 Tool call — Read · `toolu_013cGfkPeXGkJVskaR7WKjov`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": 155,
  "limit": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "bac613a5-0ca3-438a-9ced-515f4813bf87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012SQXfy45PdX1o1ooza1s2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 131705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-24T02:26:29.081Z_

<details><summary>↩ Tool result · `toolu_013cGfkPeXGkJVskaR7WKjov`</summary>

```text
155	\paragraph{Per-Layer KL: Exploratory Decomposition of Signal Type and Coupling Scope.}
156	\label{sec:perlayer}
157	To isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.
158	At $K{=}1$, per-layer KL achieves 9.05$\pm$0.02, within 2.7\% of end-to-end KL (8.81$\pm$0.02), while per-layer MSE degrades to 18.52$\pm$1.68 ($2.05\times$ worse). For PPL, signal type\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} may account for a substantial portion of the gap---an upper bound, as $K{=}1$ conflates coupling removal with train--inference mismatch. A 3-seed $K{=}4$ control\footnote{Actual sparsity 29.6\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds this (Appendix~\ref{app:k4_downstream}): \emph{coupling-dominated}---ARC-c (97\% residual gap) and WG (67\%) indicate genuine cross-layer benefits; \emph{mismatch-dominated}---PPL (67\% closure) and GSM8K (71\%) largely close; \emph{anomalous}---MMLU exceeds E2E (42.7$\pm$1.4 vs.\ 40.7$\pm$1.3), explained by $K{=}4$'s near-uniform allocation matching uniform inference (Appendix~\ref{app:constraint}). % exp_id: perlayer_kl_30_3seed, perlayer_kl_downstream, mse30_downstream_decomp, perlayer_kl_k4_3seed
159	At 50\%, partial coupling ($K{=}4$: 44.23) is \emph{worse} than $K{=}1$ (34.85) while E2E achieves 11.79, suggesting gradient interference under tight capacity; the decomposition is interpretable only at 30\%. % exp_id: perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "f16e8e56-d0b6-4778-9a80-e0a9f343d12c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\paragraph{Per-Layer KL: Exploratory Decomposition of Signal Type and Coupling Scope.}\n\\label{sec:perlayer}\nTo isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.\nAt $K{=}1$, per-layer KL achieves 9.05$\\pm$0.02, within 2.7\\% of end-to-end KL (8.81$\\pm$0.02), while per-layer MSE degrades to 18.52$\\pm$1.68 ($2.05\\times$ worse). For PPL, signal type\\footnote{We use ``signal type'' as shorthand for the training objective's optimization target (output distribution vs.\\ intermediate activations); this dimension also entails differences in gradient flow topology and optimization landscape that are not independently controlled.} may account for a substantial portion of the gap---an upper bound, as $K{=}1$ conflates coupling removal with train--inference mismatch. A 3-seed $K{=}4$ control\\footnote{Actual sparsity 29.6\\%; per-layer sparsity std=0.003 (near-uniform).} partially deconfounds this (Appendix~\\ref{app:k4_downstream}): \\emph{coupling-dominated}---ARC-c (97\\% residual gap) and WG (67\\%) indicate genuine cross-layer benefits; \\emph{mismatch-dominated}---PPL (67\\% closure) and GSM8K (71\\%) largely close; \\emph{anomalous}---MMLU exceeds E2E (42.7$\\pm$1.4 vs.\\ 40.7$\\pm$1.3), explained by $K{=}4$'s near-uniform allocation matching uniform inference (Appendix~\\ref{app:constraint}). % exp_id: perlayer_kl_30_3seed, perlayer_kl_downstream, mse30_downstream_decomp, perlayer_kl_k4_3seed\nAt 50\\%, partial coupling ($K{=}4$: 44.23) is \\emph{worse} than $K{=}1$ (34.85) while E2E achieves 11.79, suggesting gradient interference under tight capacity; the decomposition is interpretable only at 30\\%. % exp_id: perlayer_kl_k4_50_s42, perlayer_kl_50_s42, bench_kl50_global\n",
      "numLines": 6,
      "startLine": 155,
      "totalLines": 197
    }
  }
}
```

</details>

---


### Assistant

_source line 192_

<details><summary>Logged reasoning block</summary>

```text
The grep matched line 158 because of "2.7\%" in "within 2.7\% of end-to-end KL". This is a percentage comparison (9.05 vs 8.81), not a downstream metric — no change needed.

And line 159 now correctly shows "11.79" (which I already fixed).

Let me also check the appendix table phase at the corrected line:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "23f3138d-5c66-44d6-805d-b6d7d1cb432c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB3iFjDtWusgAu9CLXJYSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 132510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 861
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 193_

<details open><summary>🔧 Tool call — Read · `toolu_01YatB88g13TUcuKgmFWGUWt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": 346,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "0a090bf5-378c-47fc-aeae-1975bba0f4a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB3iFjDtWusgAu9CLXJYSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 132510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 861
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-24T02:26:34.144Z_

<details><summary>↩ Tool result · `toolu_01YatB88g13TUcuKgmFWGUWt`</summary>

```text
346	& Global & 8.96$\pm$0.02 & 35.7$\pm$9.5$^\ast$ \\ % exp_id: kl30_3seed_global
347	& Uniform & \textbf{8.81$\pm$0.02} & \textbf{40.7$\pm$1.3} \\ % exp_id: bench_kl30_uniform
348	\midrule
349	\multirow{2}{*}{50\%}
350	& Global & \textbf{11.79$\pm$0.07} & \textbf{28.3$\pm$0.7} \\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval
351	& Uniform & 11.92$\pm$0.07 & 28.0$\pm$0.6 \\ % exp_id: multi_seed_kl50_uniform
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	Table~\ref{tab:phase_full} extends Table~\ref{tab:phase} with all downstream metrics.
357	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "68b171bb-56f1-4a63-805e-388958fb7367",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "& Global & 8.96$\\pm$0.02 & 35.7$\\pm$9.5$^\\ast$ \\\\ % exp_id: kl30_3seed_global\n& Uniform & \\textbf{8.81$\\pm$0.02} & \\textbf{40.7$\\pm$1.3} \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{28.3$\\pm$0.7} \\\\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval\n& Uniform & 11.92$\\pm$0.07 & 28.0$\\pm$0.6 \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:phase_full} extends Table~\\ref{tab:phase} with all downstream metrics.\n",
      "numLines": 12,
      "startLine": 346,
      "totalLines": 672
    }
  }
}
```

</details>

---


### Tool call

_source line 195_

<details open><summary>🔧 Tool call — Read · `toolu_01FCNBGeTKepp15up7xNS647`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": 383,
  "limit": 12
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "ef4b2af1-be06-4e4a-bf9b-aac68110ccb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB3iFjDtWusgAu9CLXJYSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 132510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 861
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-24T02:26:34.614Z_

<details><summary>↩ Tool result · `toolu_01FCNBGeTKepp15up7xNS647`</summary>

```text
383	& Global & \textbf{10.80} & \textbf{39.2} & \textbf{64.6} & 30.4 & \textbf{3.0} \\
384	& Uniform & 10.95 & 37.6 & 63.6 & \textbf{30.6} & 2.7 \\
385	\midrule
386	\multirow{2}{*}{50\%}
387	& Global & \textbf{11.79$\pm$0.07} & \textbf{36.5$\pm$3.3} & \textbf{63.9$\pm$0.4} & \textbf{28.3$\pm$0.7} & \textbf{2.3$\pm$1.1} \\
388	& Uniform & 11.92$\pm$0.07 & 33.8$\pm$1.2 & 62.9$\pm$0.1 & 28.0$\pm$0.6 & 2.2$\pm$0.1 \\
389	\bottomrule
390	\end{tabular}
391	\end{table*}
392	
393	
394	\section{Mask Pattern Visualization}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "ffdc6aaa-7d57-4930-ba01-f9d84cddaadd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "& Global & \\textbf{10.80} & \\textbf{39.2} & \\textbf{64.6} & 30.4 & \\textbf{3.0} \\\\\n& Uniform & 10.95 & 37.6 & 63.6 & \\textbf{30.6} & 2.7 \\\\\n\\midrule\n\\multirow{2}{*}{50\\%}\n& Global & \\textbf{11.79$\\pm$0.07} & \\textbf{36.5$\\pm$3.3} & \\textbf{63.9$\\pm$0.4} & \\textbf{28.3$\\pm$0.7} & \\textbf{2.3$\\pm$1.1} \\\\\n& Uniform & 11.92$\\pm$0.07 & 33.8$\\pm$1.2 & 62.9$\\pm$0.1 & 28.0$\\pm$0.6 & 2.2$\\pm$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Mask Pattern Visualization}",
      "numLines": 12,
      "startLine": 383,
      "totalLines": 672
    }
  }
}
```

</details>

---


### Assistant

_source line 197_

All 4 Fix 1 locations are updated. Now let me also check if the abstract or other files reference the KL 50% global PPL or GSM8K values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "cb4d79f5-6922-459f-ae1d-0001fce40591",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JAY2nSXgfYHWmsvLPb3hLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 133371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 198_

<details open><summary>🔧 Tool call — Read · `toolu_018tAnHpkTaP3R3GNjYLbwok`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "84fa3932-9cfc-4cfa-95b3-5e8b0477e77c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JAY2nSXgfYHWmsvLPb3hLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 133371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1029
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-24T02:26:39.286Z_

<details><summary>↩ Tool result · `toolu_018tAnHpkTaP3R3GNjYLbwok`</summary>

```text
1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with directional commonsense gains ($n{=}3$) but knowledge-intensive regression (MMLU $-$5.2pp on 8B; GSM8K $-$20.1pp on 14B); post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) may account for a substantial portion of the PPL gap at moderate sparsity (30\%) (upper bound; \S\ref{sec:perlayer}).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "c38f8f20-b0c0-4aae-81a0-1d2f3ea9077d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex",
      "content": "Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.\nWe train lightweight predictors ($<$1\\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.\nOn LLaMA-3.1-8B at 30\\% sparsity, the KL predictor reduces perplexity by 14.5\\% over TEAL at matched sparsity, with directional commonsense gains ($n{=}3$) but knowledge-intensive regression (MMLU $-$5.2pp on 8B; GSM8K $-$20.1pp on 14B); post-hoc compensation (+67.2M params) becomes redundant.\nOutput-distribution optimization yields masks that diverge 46--68\\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\\leq$0.65pp; 3-seed, 30\\%).\nSignal type (output-distribution vs.\\ intermediate loss) may account for a substantial portion of the PPL gap at moderate sparsity (30\\%) (upper bound; \\S\\ref{sec:perlayer}).\nOn downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).\nCross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.\nThis is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---


### Assistant

_source line 200_

<details><summary>Logged reasoning block</summary>

```text
The abstract doesn't reference KL 50% global PPL or its downstream values directly. The "14.5%" and "8.81 vs 10.30" in the intro are for 30% sparsity. No changes needed in abstract.

Let me also check the introduction and conclusion for any references to the changed values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "9b0cc52f-4357-423c-9cf0-4aaeff24ed69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125bqpB6zSCaZro9KRdDqZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 134400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 685
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 201_

<details open><summary>🔧 Tool call — Read · `toolu_01Hn6BaAavWobNEL5DcEvZ1D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "21257fcb-0330-4450-869d-b20d9eb2cd8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125bqpB6zSCaZro9KRdDqZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 134400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 685
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 202 · 2026-05-24T02:26:43.330Z_

<details><summary>↩ Tool result · `toolu_01Hn6BaAavWobNEL5DcEvZ1D`</summary>

```text
1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (mean per-layer Jaccard distance).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to PPL but meaningfully to downstream fidelity (\S\ref{sec:perlayer}).
12	
13	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
14	At 30\% sparsity under uniform allocation, the predictor reduces TEAL's perplexity by 14.5\% at matched sparsity (8.81 vs.\ 10.30, both at 28.5\%) with downstream (MMLU 40.7$\pm$1.3\% vs.\ 65.3\% dense, 3-seed); global top-$k$ amplifies cross-seed variance ($7.3\times$).
15	At 50\%, the perplexity advantage widens (50\% over TEAL), but downstream reasoning collapses regardless of method.
16	
17	Cross-architecture evaluation on Mistral-7B-v0.3~\cite{jiang2023mistral} (3-seed) confirms the PPL advantage ($-$17.3\%) with directional commonsense gains but tied MMLU; preliminary evaluation on Qwen-2.5-14B~\cite{qwen2024qwen25} shows consistent PPL improvement but reasoning decline (GSM8K $-$20.1pp, $\sigma$=5.2pp; MMLU $-$2.8pp).
18	This paper is primarily an empirical study characterizing how the training objective shapes sparsity prediction quality across allocation strategies, sparsity levels, and model scales. The central finding---that output-distribution alignment consistently and substantially outperforms per-neuron classification for learned sparsity---is the paper's contribution. Without sparse kernel support, the predictor adds 6.4\% latency overhead; wall-clock speedup is not addressed (Appendix~\ref{app:latency}).
19	While individual components (KL divergence, Gumbel-Sigmoid relaxation) are established techniques, their application to contextual activation sparsity prediction has not been explored, and the resulting empirical behaviors are non-obvious.
20	
21	Our contributions are:
22	\begin{itemize}[nosep,leftmargin=*]
23	\item \emph{Empirical:} Output-distribution alignment ranking across five losses, with exploratory per-layer KL decomposition into signal type (may account for most of the PPL gap; upper bound) and coupling scope (task-dependent; $K{=}4$-corrected; \S\ref{sec:perlayer});
24	\item \emph{Empirical:} Cross-scale evidence at 7--14B confirming output-distribution losses outperform intermediate losses regardless of coupling scope (\S\ref{sec:experiments}).
25	\item \emph{Practical:} Target-swap ablation suggests KL-discovered mask targets transfer to BCE; coupling refines downstream fidelity beyond PPL (\S\ref{sec:perlayer}).
26	\item \emph{Practical:} These mask patterns render post-hoc compensation (+67.2M params) redundant at both tested sparsity levels (\S\ref{sec:compensation}).
27	\end{itemize}
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{fig1_overview.pdf}
32	\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}
33	\label{fig:overview}
34	\end{figure}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "4b9720c9-afbe-4ec6-b8ff-d093ec1b6ea1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nHow the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.\nLearned sparsity predictors~\\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.\nYet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.\nThis mismatch between per-neuron training and global inference allocation has not been formally analyzed.\nUnlike MaskLLM~\\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.\n\nGradient analysis reveals a structural asymmetry: BCE's gradient $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\\S\\ref{sec:method:gradient}).\nKL's coupled gradients discover neuron importance patterns that diverge 68\\% from magnitude-based masks (mean per-layer Jaccard distance).\nA target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\\pm$0.20. Coupling contributes marginally to PPL but meaningfully to downstream fidelity (\\S\\ref{sec:perlayer}).\n\nWe instantiate a lightweight predictor (75.9M params, $<$1\\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}.\nAt 30\\% sparsity under uniform allocation, the predictor reduces TEAL's perplexity by 14.5\\% at matched sparsity (8.81 vs.\\ 10.30, both at 28.5\\%) with downstream (MMLU 40.7$\\pm$1.3\\% vs.\\ 65.3\\% dense, 3-seed); global top-$k$ amplifies cross-seed variance ($7.3\\times$).\nAt 50\\%, the perplexity advantage widens (50\\% over TEAL), but downstream reasoning collapses regardless of method.\n\nCross-architecture evaluation on Mistral-7B-v0.3~\\cite{jiang2023mistral} (3-seed) confirms the PPL advantage ($-$17.3\\%) with directional commonsense gains but tied MMLU; preliminary evaluation on Qwen-2.5-14B~\\cite{qwen2024qwen25} shows consistent PPL improvement but reasoning decline (GSM8K $-$20.1pp, $\\sigma$=5.2pp; MMLU $-$2.8pp).\nThis paper is primarily an empirical study characterizing how the training objective shapes sparsity prediction quality across allocation strategies, sparsity levels, and model scales. The central finding---that output-distribution alignment consistently and substantially outperforms per-neuron classification for learned sparsity---is the paper's contribution. Without sparse kernel support, the predictor adds 6.4\\% latency overhead; wall-clock speedup is not addressed (Appendix~\\ref{app:latency}).\nWhile individual components (KL divergence, Gumbel-Sigmoid relaxation) are established techniques, their application to contextual activation sparsity prediction has not been explored, and the resulting empirical behaviors are non-obvious.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\emph{Empirical:} Output-distribution alignment ranking across five losses, with exploratory per-layer KL decomposition into signal type (may account for most of the PPL gap; upper bound) and coupling scope (task-dependent; $K{=}4$-corrected; \\S\\ref{sec:perlayer});\n\\item \\emph{Empirical:} Cross-scale evidence at 7--14B confirming output-distribution losses outperform intermediate losses regardless of coupling scope (\\S\\ref{sec:experiments}).\n\\item \\emph{Practical:} Target-swap ablation suggests KL-discovered mask targets transfer to BCE; coupling refines downstream fidelity beyond PPL (\\S\\ref{sec:perlayer}).\n\\item \\emph{Practical:} These mask patterns render post-hoc compensation (+67.2M params) redundant at both tested sparsity levels (\\S\\ref{sec:compensation}).\n\\end{itemize}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_overview.pdf}\n\\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}\n\\label{fig:overview}\n\\end{figure}\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---


### Assistant

_source line 203_

<details><summary>Logged reasoning block</summary>

```text
The introduction at line 15 says "At 50\%, the perplexity advantage widens (50\% over TEAL), but downstream reasoning collapses regardless of method." This doesn't reference specific numbers.

Line 17 mentions GSM8K -20.1pp for Qwen-14B. Let me verify this. From the Qwen-14B data:
- TEAL 30% uniform GSM8K: 52.1 (from qwen14b_teal30_uniform_gsm8k: 0.5208)
- KL 30% uniform GSM8K: 32.0±5.2 (from the paper)


The delta checks out at -20.1pp. Now I'm looking at the individual seed values for the KL runs to understand where that ±5.2 range comes from, since I'm seeing different results across seeds.

All the fixes through Fix 4 are complete. For Fix 5, I need to do some analysis. Let me verify a few key claims in the text: the 50% reduction comparison still holds since it's comparing uniform methods unrelated to Fix 1. The KL vs BCE PPL claim of 11.79 vs 28.13 checks out with the benchmark data showing 11.7933. I'm also verifying the multiplier claim at line 74 of experiments.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "52de4289-39c8-4b53-8975-a083bf2c02cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TdCSzx1YFzTkwVuqiMJDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 135085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1650
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 204_

All edits complete. Let me verify there are no remaining stale references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "4325b879-ab89-40f5-8440-6fd0cbfc67e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TdCSzx1YFzTkwVuqiMJDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 135085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1650
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 205_

<details open><summary>🔧 Tool call — Grep · `toolu_01QFn9qRxyk6UrRU6JeYxM9Y`</summary>

```json
{
  "pattern": "11\\.84|70\\.85|74\\.81|75\\.03|69\\.24",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "3d0dec27-3002-4c56-a899-caf27abc6869",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TdCSzx1YFzTkwVuqiMJDR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 135085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1650
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 206 · 2026-05-24T02:27:01.784Z_

<details><summary>↩ Tool result · `toolu_01QFn9qRxyk6UrRU6JeYxM9Y`</summary>

```text
paper/appendix.tex:613:WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)
paper/appendix.tex:614:C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.2 / 75.0 \\ % exp_id: c4_kl30_s42_eval (HS=69.24→69.2, PIQA=75.03→75.0 rounded)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "5859e1e0-5389-4542-938c-60ffd99f7a9d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/appendix.tex:613:WikiText-103 & 8.82 & 40.78 & 68.59 & 40.6 & 7.35 & 70.9 / 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa (HS=70.85→70.9, PIQA=74.81→74.8 rounded to match OOD table)\npaper/appendix.tex:614:C4 & 11.55 & 43.09 & 68.67 & 39.95 & 4.09 & 69.2 / 75.0 \\\\ % exp_id: c4_kl30_s42_eval (HS=69.24→69.2, PIQA=75.03→75.0 rounded)",
    "numLines": 2
  }
}
```

</details>

---


### Assistant

_source line 207_

<details><summary>Logged reasoning block</summary>

```text
The old values only appear in the comments (noting the change history), not in the visible text. The actual displayed values are all updated. 

Let me now verify the OOD downstream table still matches (it should, since we rounded the C4 control table to match it):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "984d6f4e-7578-4ffb-b186-eb907902d605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3xQVvHLgGVSmqjrShQV5t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 136735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 208_

Clean — old values only in comments. Let me verify cross-table consistency one more time.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "62e192a5-8adc-4e5a-bae6-79721bd9a0a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3xQVvHLgGVSmqjrShQV5t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 136735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 209_

<details open><summary>🔧 Tool call — Read · `toolu_01LXkEt7LWCvsXshRowGMTn1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": 192,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "9768dbbd-4234-4c1b-badb-2851a61c530a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3xQVvHLgGVSmqjrShQV5t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 136735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-24T02:27:06.517Z_

<details><summary>↩ Tool result · `toolu_01LXkEt7LWCvsXshRowGMTn1`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "d0e1a69a-95a4-4ec8-be4f-da7696e80620",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
      "content": "\\toprule\nCalibration & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\\\\n\\midrule\nWikiText & 40.8 & 68.6 & 40.6 & 7.4 & 70.9 & 74.8 \\\\ % exp_id: bench_kl30_uniform, kl30_uniform_hellaswag_piqa\nC4 (OOD) & 40.4 & 69.3 & 41.4 & 6.3 & 70.7 & 74.0 \\\\ % exp_id: c4_ood_downstream_kl30\n\\midrule\n$\\Delta$ & $-$0.4 & +0.7 & +0.8 & $-$1.1 & $-$0.2 & $-$0.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 10,
      "startLine": 192,
      "totalLines": 672
    }
  }
}
```

</details>

---


### Assistant

_source line 211_

OOD downstream table WikiText row: HS=70.9, PIQA=74.8 — matches the C4 control table now.

---

## 修改汇总

### Fix 1: Table 2 — KL 50% global 行 (4处)

从 registry 重新计算 3-seed mean±std：

| Metric | 旧值 | 新值 | 数据来源 |
|--------|------|------|---------|
| PPL | 11.84±0.15 | 11.79±0.07 | s42=11.79, s123=11.72, s456=11.86 |
| ARC-c | 36.3±3.2 | 36.5±3.3 | s42=32.85, s123=39.16, s456=37.54 |
| WG | 63.8±0.3 | 63.9±0.4 | s42=63.46, s123=64.01, s456=64.17 |
| MMLU | 28.3±0.7 | 28.3±0.7 | 不变 |
| GSM8K | 2.7±1.3 | 2.3±1.1 | s42=1.29, s123=3.41, s456=2.12 |

修改文件：
- `experiments.tex:64` — Table 2
- `experiments.tex:159` — text "E2E achieves 11.84→11.79"
- `appendix.tex:350` — Table phase
- `appendix.tex:387` — Table phase_full

### Fix 2: C4 control 表 WikiText 行 HS/PIQA
- 70.85 → 70.9, 74.81 → 74.8（与 OOD downstream 表一致）
- `appendix.tex:613`

### Fix 3: C4 control 表 C4 行
- 69.24 → 69.2, 75.03 → 75.0（统一 1 位小数）
- `appendix.tex:614`

### Fix 4: "148× compression" for Qwen14B
- **当前论文中不存在 "148×"**，无需修改
- SSH 确认 Qwen-2.5-14B: `intermediate_size=13824`, `d_ff/d_b = 13824/128 = 108×`
- LLaMA `14336/128 = 112×` 正确
- 如需在论文中添加此信息，应使用 108×

### Fix 5: Extended downstream 表 TEAL 30% uniform PIQA
- **建议保留 72.80（不修改）**
- Registry `teal_30pct_uniform_multiseed_eval` 的 key 是 `piqa=0.7198`（无 _acc/_acc_norm 后缀）
- 同一实验的 `hellaswag=0.6331` 确认是 acc_norm（HS acc 通常 ~0.49）
- PIQA 在 lm-eval-harness 中默认 metric 是 acc（非 acc_norm），所以 0.7198 很可能是 piqa_acc
- piqa_acc(71.98) + ~0.82pp = piqa_acc_norm(72.80)，与论文一致
- 服务器上无原始 results.json 可验证
- 如需确认，需重跑 TEAL 30% uniform 的 HS/PIQA eval

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "uuid": "14ed8156-b254-4727-a538-efc36861ad0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jZLEXXe7T7fH24XtUXhPm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 137728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 489
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 212_

OOD downstream table WikiText row: HS=70.9, PIQA=74.8 — matches the C4 control table now.

---

## 修改汇总

### Fix 1: Table 2 — KL 50% global 行 (4处)

从 registry 重新计算 3-seed mean±std：

| Metric | 旧值 | 新值 | 数据来源 |
|--------|------|------|---------|
| PPL | 11.84±0.15 | 11.79±0.07 | s42=11.79, s123=11.72, s456=11.86 |
| ARC-c | 36.3±3.2 | 36.5±3.3 | s42=32.85, s123=39.16, s456=37.54 |
| WG | 63.8±0.3 | 63.9±0.4 | s42=63.46, s123=64.01, s456=64.17 |
| MMLU | 28.3±0.7 | 28.3±0.7 | 不变 |
| GSM8K | 2.7±1.3 | 2.3±1.1 | s42=1.29, s123=3.41, s456=2.12 |

修改文件：
- `experiments.tex:64` — Table 2
- `experiments.tex:159` — text "E2E achieves 11.84→11.79"
- `appendix.tex:350` — Table phase
- `appendix.tex:387` — Table phase_full

### Fix 2: C4 control 表 WikiText 行 HS/PIQA
- 70.85 → 70.9, 74.81 → 74.8（与 OOD downstream 表一致）
- `appendix.tex:613`

### Fix 3: C4 control 表 C4 行
- 69.24 → 69.2, 75.03 → 75.0（统一 1 位小数）
- `appendix.tex:614`

### Fix 4: "148× compression" for Qwen14B
- **当前论文中不存在 "148×"**，无需修改
- SSH 确认 Qwen-2.5-14B: `intermediate_size=13824`, `d_ff/d_b = 13824/128 = 108×`
- LLaMA `14336/128 = 112×` 正确
- 如需在论文中添加此信息，应使用 108×

### Fix 5: Extended downstream 表 TEAL 30% uniform PIQA
- **建议保留 72.80（不修改）**
- Registry `teal_30pct_uniform_multiseed_eval` 的 key 是 `piqa=0.7198`（无 _acc/_acc_norm 后缀）
- 同一实验的 `hellaswag=0.6331` 确认是 acc_norm（HS acc 通常 ~0.49）
- PIQA 在 lm-eval-harness 中默认 metric 是 acc（非 acc_norm），所以 0.7198 很可能是 piqa_acc
- piqa_acc(71.98) + ~0.82pp = piqa_acc_norm(72.80)，与论文一致
- 服务器上无原始 results.json 可验证
- 如需确认，需重跑 TEAL 30% uniform 的 HS/PIQA eval

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 974668,
  "duration_api_ms": 966337,
  "num_turns": 79,
  "stop_reason": "end_turn",
  "session_id": "c3531263-9e9c-43e4-8f45-2fbded6acba7",
  "total_cost_usd": 4.320242000000001,
  "usage": {
    "input_tokens": 52,
    "cache_creation_input_tokens": 126376,
    "cache_read_input_tokens": 4696526,
    "output_tokens": 47171,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 126376,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 932,
        "cache_read_input_tokens": 137728,
        "cache_creation_input_tokens": 489,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 489
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2529,
      "outputTokens": 13,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002594,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 52,
      "outputTokens": 47171,
      "cacheReadInputTokens": 4696526,
      "cacheCreationInputTokens": 126376,
      "webSearchRequests": 0,
      "costUSD": 4.317648000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9d66b29f-3479-4922-907a-8be43919acfa"
}
```

</details>

---
