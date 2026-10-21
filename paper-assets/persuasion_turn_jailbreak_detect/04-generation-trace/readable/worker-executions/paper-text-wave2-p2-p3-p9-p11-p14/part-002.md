# paper text wave2 p2 p3 p9 p11 p14 — Part 2 of 2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../paper-text-wave2-p2-p3-p9-p11-p14.md) · [Structured JSON](../../../sessions/7a/7a671b7bfcde81f81baa.json)

## Before a recorded user message

### Tool call

_source line 194_

<details open><summary>🔧 Tool call — Bash · `toolu_01XKKxiyGJvrdUx2FTjMey8c`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-f', '8', '-l', '9', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\x0c')\npage8 = pages[0]\npage9 = pages[1] if len(pages) >= 2 else ''\nif 'preliminary two-step protocol' in page8:\n    print('Conclusion ends on page 8 ✓')\nelse:\n    print('Conclusion still spills to page 9 ✗')\n    print('Page 9 starts with:', page9.strip()[:150])\n\"",
  "description": "Check if Conclusion fits on page 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "3be30954-1c00-422a-ba3c-2c715bd0cae8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFaURxTKsiqxjhWBJUYTkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 107936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 742
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

_source line 195 · 2026-05-22T14:16:23.121Z_

<details><summary>↩ Tool result · `toolu_01XKKxiyGJvrdUx2FTjMey8c`</summary>

```text
Conclusion ends on page 8 ✓
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "c9c3627d-9b50-4c0b-a79e-80fd8ab54700",
  "tool_use_result": {
    "stdout": "Conclusion ends on page 8 ✓",
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

_source line 196_

Main text now fits within 8 pages. Let me do a final compilation check for warnings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "ebe36ecd-936e-4831-85c7-c3652250da1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqsVkMW24zU7AB2QxU7QYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 108678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
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

_source line 197_

<details open><summary>🔧 Tool call — Bash · `toolu_01P8TKiessgEuRKtvBqjaq1T`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"undefined|Warning.*citation|Error|Output written\" | head -10",
  "description": "Final compilation check"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "b414c47a-a2d8-4ef6-a371-6657b9e53a12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqsVkMW24zU7AB2QxU7QYd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 108678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
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

_source line 198 · 2026-05-22T14:16:28.281Z_

<details><summary>↩ Tool result · `toolu_01P8TKiessgEuRKtvBqjaq1T`</summary>

```text
Output written on main.pdf (26 pages, 535151 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "79f2098d-d7ee-4d22-874b-d27de7d66f0b",
  "tool_use_result": {
    "stdout": "Output written on main.pdf (26 pages, 535151 bytes).",
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

_source line 199_

Clean compilation, no citation warnings, 26 pages total (8 main + references + appendix).

Let me do a final review of all changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "2bb13a99-4325-432a-b8a7-32b53d415600",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwwsTTLKdiBjwdFQkN2GfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 108996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

_source line 200_

<details open><summary>🔧 Tool call — Read · `toolu_01SadQgQtAiAN8AfpKyKsp3E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "ba6c8bc0-9f86-439f-9bde-95faae9def30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwwsTTLKdiBjwdFQkN2GfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 108996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

_source line 201 · 2026-05-22T14:16:32.553Z_

<details><summary>↩ Tool result · `toolu_01SadQgQtAiAN8AfpKyKsp3E`</summary>

```text
1	% abstract.tex — D073 Phase 2 revision
2	\begin{abstract}
3	What representation properties of encoder adaptation enable cross-attack generalization in multi-turn jailbreak detection?
4	Multi-turn attacks spread adversarial intent across benign-seeming turns, evading existing defenses: Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks.
5	We decompose cross-attack generalization through controlled ablation of thirteen encoder configurations on synthetic multi-turn data.
6	A surprising finding emerges: \emph{any} deterministic label partition---including scrambled labels---triggers discriminative compression sufficient for template-attack generalization, with a complexity-dependent boundary on structurally complex attacks.
7	On synthetic multi-turn data, classification-based domain adaptation recovers OOD detection (F1\,=\,0.97--1.0 vs.\ vanilla 0.28--0.31) and remains robust under mixed-LLM training where unsupervised pretraining collapses; however, this advantage reverses on human-authored single-turn data.
8	Orthogonal to attack-side generalization, benign distribution shift is a practical bottleneck: few-shot benign adaptation reduces false-positive rates below deployment thresholds on two independent sources.
9	These findings decompose multi-turn jailbreak generalization into two orthogonal axes---attack-side (discriminative compression) and benign-side (few-shot adaptation)---with 24.3$\times$ inference speedup over LLM-as-judge.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "c0274a1e-d362-4e1c-aa16-dfbb547e9aa9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex",
      "content": "% abstract.tex — D073 Phase 2 revision\n\\begin{abstract}\nWhat representation properties of encoder adaptation enable cross-attack generalization in multi-turn jailbreak detection?\nMulti-turn attacks spread adversarial intent across benign-seeming turns, evading existing defenses: Llama Guard~3 detects only 1.8\\% of multi-turn jailbreaks.\nWe decompose cross-attack generalization through controlled ablation of thirteen encoder configurations on synthetic multi-turn data.\nA surprising finding emerges: \\emph{any} deterministic label partition---including scrambled labels---triggers discriminative compression sufficient for template-attack generalization, with a complexity-dependent boundary on structurally complex attacks.\nOn synthetic multi-turn data, classification-based domain adaptation recovers OOD detection (F1\\,=\\,0.97--1.0 vs.\\ vanilla 0.28--0.31) and remains robust under mixed-LLM training where unsupervised pretraining collapses; however, this advantage reverses on human-authored single-turn data.\nOrthogonal to attack-side generalization, benign distribution shift is a practical bottleneck: few-shot benign adaptation reduces false-positive rates below deployment thresholds on two independent sources.\nThese findings decompose multi-turn jailbreak generalization into two orthogonal axes---attack-side (discriminative compression) and benign-side (few-shot adaptation)---with 24.3$\\times$ inference speedup over LLM-as-judge.\n\\end{abstract}\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---


### Tool call

_source line 202_

<details open><summary>🔧 Tool call — Read · `toolu_014MsnKr2BFtRG7i57kTvDba`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "d359c6b3-b173-4391-85d9-9e1ffccfb940",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwwsTTLKdiBjwdFQkN2GfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 108996,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

_source line 203 · 2026-05-22T14:16:32.872Z_

<details><summary>↩ Tool result · `toolu_014MsnKr2BFtRG7i57kTvDba`</summary>

```text
1	% conclusion.tex — D073 Phase 2 revision (page-compressed)
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\paragraph{Confounds and transferability.}
7	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97). ToxicChat (+18--42\,pp; Table~\ref{tab:human_data}) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer; mixed-LLM 9-class maintains DD F1\,=\,0.818$\pm$0.096 while MLM collapses to vanilla level (Appendix~\ref{app:mixed_llm}). Dataset composition---not sample count---is the primary determinant (Appendix~\ref{app:scale_validation}). Prompt optimization improves LLM-as-judge OOD detection but does not close the gap with encoder-based methods (Appendix~\ref{app:prompt_opt}).
8	
9	\paragraph{Evidence for discriminative compression.}
10	Classification DAPT compresses the feature space into few discriminative dimensions (participation ratio 3.7--9.4 vs.\ 25--32 for MLM/vanilla) with 3--5 orders of magnitude higher separability (Fisher 2.6--19.7 vs.\ $<$0.001; Appendix~\ref{app:representation}). Scrambled labels produce comparable compression (Fisher\,=\,2.6), consistent with \citet{zhang2021understanding}'s framework for how classification modifies representations, with two domain-specific findings: (i)~domain-relevant label partitioning is necessary (topic labels insufficient), and (ii)~compression localizes to 3 SVD dimensions in layers 8--12 (Fisher 15$\times$ vanilla at peak; Appendix~\ref{app:layerwise}), with early layers remaining label-independent as in \citet{maennel2020random}. A discriminative probe confirms: 3 SVD components of 9-class layer-10 representations achieve perfect AA OOD detection (F1\,=\,1.000) vs.\ MLM 0.636 with all 768 dimensions (Appendix~\ref{app:discriminative_probe}). The complexity-dependent boundary persists ($d < 0.1$ on DD/FITD; $d$\,=\,0.44 on AA). Frozen probing near-parity (AA gap 3.1\,pp) confirms discriminative structure is established in Stage-1.
11	
12	\paragraph{Condition-specific advantage.}
13	The evidence hierarchy is specific to multi-turn synthetic evaluation. On ToxicChat (single-turn human data), JB-MLM leads (0.837) while 9-class ranks lower (0.596): 77\% from false positives. Truncating synthetic conversations to a single turn \emph{widens} the 9-class advantage ($\bar{\Delta}$\,=\,+1.6\,pp $\to$ +6.0\,pp; Appendix~\ref{app:truncated}), implicating distributional differences between synthetic and human text rather than multi-turn structure. Variance reverses (classification std\,=\,0.087 vs.\ MLM\,=\,0.013); practitioners facing single-turn human data should consider MLM DAPT.
14	
15	\paragraph{Two-axis generalization.}
16	OOD F1 reflects attack-side generalization under IID benign conditions. The orthogonal challenge is benign-side shift: DAPT increases WildChat FPR from 48.1\% to 68.1\% (Appendix~\ref{app:wildchat_fpr}). Ten target-domain conversations reduce it to 0\% (Appendix~\ref{app:benign_mixed}); OASST2 confirms the pattern (FPR 57.5\%\,$\rightarrow$\,1.0\%$\pm$0.5\% at $N$\,=\,25; Appendix~\ref{app:oasst2}).
17	
18	\section{Conclusion}
19	
20	On synthetic multi-turn data, thirteen encoder configurations decompose jailbreak generalization into attack-side (classification DAPT via discriminative compression; MLM collapses under mixed-LLM data) and benign-side (FPR 65--68\%\,$\rightarrow$\,0--1.5\% via 10--25 conversations) axes. Any deterministic partition suffices for template attacks ($d < 0.1$), with a complexity-dependent boundary on ActorAttack ($d$\,=\,0.44). At 24.3$\times$ speedup over LLM-as-judge, these suggest a preliminary two-step protocol.
21	
22	\section{Limitations}
23	\label{sec:limitations}
24	
25	All multi-turn findings derive from synthetic conversations generated by Qwen3-8B (350 training, 76--118 test per family); preliminary mixed-LLM training (Appendix~\ref{app:mixed_llm}) suggests this limitation is addressable. Most pairwise comparisons rely on 3 seeds; key scrambled-vs.-correct comparisons are extended to 10 seeds (Appendix~\ref{app:seed_level}). ToxicChat validates transfer to human-authored single-turn attacks (+18--42\,pp over vanilla), but the evidence hierarchy reverses on this data (Section~\ref{sec:discussion}), and no human-generated multi-turn jailbreak dataset exists.
26	
27	OOD results reflect attack-side generalization only; benign data is IID, so OOD F1 figures are upper bounds. On WildChat, 9-class FPR reaches 68.1\%; 10 target-domain conversations eliminate it ($n$\,=\,49). OASST2 confirms the pattern but requires 25--50 conversations for comparable reduction (FPR\,=\,1.0\%$\pm$0.5\% at $N$\,=\,25, 3 seeds; Appendix~\ref{app:oasst2}); validation on additional platforms is needed. Residual calibration error (ECE\,=\,0.126--0.141; Appendix~\ref{app:calibration}) suggests temperature scaling is needed for deployment.
28	
29	Benign-only adaptation addresses human-population distribution shift (WildChat, OASST2) but not cross-LLM distribution shift: adapting on Llama-origin benign conversations reduces FPR but collapses Llama jailbreak detection, as the model conflates LLM-specific style features with benign class membership (Appendix~\ref{app:cross_llm}). Three encoders (125M--355M) differ in architecture and pretraining; same-architecture scaling is needed to isolate the capacity effect. Only persuasion-mediated multi-turn attacks fall within scope; single-turn token-level attacks~\citep{zou2023gcg}, non-persuasive strategies, and non-text modalities are not addressed. Total pipeline cost is under 4 GPU-hours on a single A100.
30	
31	\section*{Ethics Statement}
32	
33	This work is defensive: it improves detection of multi-turn jailbreak attacks rather than developing new attacks. We acknowledge dual-use risk, as the persuasion taxonomy could inform adversarial actors. We mitigate this by using only synthetic conversations (no real harmful content) and withholding attack-generation prompts. Detection code, model weights, and evaluation data will be released under CC BY-NC 4.0. No human subjects were involved.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "be72f758-beb6-4bdc-846c-6e90ae03e811",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex",
      "content": "% conclusion.tex — D073 Phase 2 revision (page-compressed)\n\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Confounds and transferability.}\nThree observations argue against a topic shortcut: unstable topic OOD (F1\\,=\\,0.541$\\pm$0.207), scrambled labels within 3.9\\,pp, and label-free MLM detection (F1\\,$\\geq$\\,0.97). ToxicChat (+18--42\\,pp; Table~\\ref{tab:human_data}) and cross-LLM experiments (Appendix~\\ref{app:cross_llm}) confirm transfer; mixed-LLM 9-class maintains DD F1\\,=\\,0.818$\\pm$0.096 while MLM collapses to vanilla level (Appendix~\\ref{app:mixed_llm}). Dataset composition---not sample count---is the primary determinant (Appendix~\\ref{app:scale_validation}). Prompt optimization improves LLM-as-judge OOD detection but does not close the gap with encoder-based methods (Appendix~\\ref{app:prompt_opt}).\n\n\\paragraph{Evidence for discriminative compression.}\nClassification DAPT compresses the feature space into few discriminative dimensions (participation ratio 3.7--9.4 vs.\\ 25--32 for MLM/vanilla) with 3--5 orders of magnitude higher separability (Fisher 2.6--19.7 vs.\\ $<$0.001; Appendix~\\ref{app:representation}). Scrambled labels produce comparable compression (Fisher\\,=\\,2.6), consistent with \\citet{zhang2021understanding}'s framework for how classification modifies representations, with two domain-specific findings: (i)~domain-relevant label partitioning is necessary (topic labels insufficient), and (ii)~compression localizes to 3 SVD dimensions in layers 8--12 (Fisher 15$\\times$ vanilla at peak; Appendix~\\ref{app:layerwise}), with early layers remaining label-independent as in \\citet{maennel2020random}. A discriminative probe confirms: 3 SVD components of 9-class layer-10 representations achieve perfect AA OOD detection (F1\\,=\\,1.000) vs.\\ MLM 0.636 with all 768 dimensions (Appendix~\\ref{app:discriminative_probe}). The complexity-dependent boundary persists ($d < 0.1$ on DD/FITD; $d$\\,=\\,0.44 on AA). Frozen probing near-parity (AA gap 3.1\\,pp) confirms discriminative structure is established in Stage-1.\n\n\\paragraph{Condition-specific advantage.}\nThe evidence hierarchy is specific to multi-turn synthetic evaluation. On ToxicChat (single-turn human data), JB-MLM leads (0.837) while 9-class ranks lower (0.596): 77\\% from false positives. Truncating synthetic conversations to a single turn \\emph{widens} the 9-class advantage ($\\bar{\\Delta}$\\,=\\,+1.6\\,pp $\\to$ +6.0\\,pp; Appendix~\\ref{app:truncated}), implicating distributional differences between synthetic and human text rather than multi-turn structure. Variance reverses (classification std\\,=\\,0.087 vs.\\ MLM\\,=\\,0.013); practitioners facing single-turn human data should consider MLM DAPT.\n\n\\paragraph{Two-axis generalization.}\nOOD F1 reflects attack-side generalization under IID benign conditions. The orthogonal challenge is benign-side shift: DAPT increases WildChat FPR from 48.1\\% to 68.1\\% (Appendix~\\ref{app:wildchat_fpr}). Ten target-domain conversations reduce it to 0\\% (Appendix~\\ref{app:benign_mixed}); OASST2 confirms the pattern (FPR 57.5\\%\\,$\\rightarrow$\\,1.0\\%$\\pm$0.5\\% at $N$\\,=\\,25; Appendix~\\ref{app:oasst2}).\n\n\\section{Conclusion}\n\nOn synthetic multi-turn data, thirteen encoder configurations decompose jailbreak generalization into attack-side (classification DAPT via discriminative compression; MLM collapses under mixed-LLM data) and benign-side (FPR 65--68\\%\\,$\\rightarrow$\\,0--1.5\\% via 10--25 conversations) axes. Any deterministic partition suffices for template attacks ($d < 0.1$), with a complexity-dependent boundary on ActorAttack ($d$\\,=\\,0.44). At 24.3$\\times$ speedup over LLM-as-judge, these suggest a preliminary two-step protocol.\n\n\\section{Limitations}\n\\label{sec:limitations}\n\nAll multi-turn findings derive from synthetic conversations generated by Qwen3-8B (350 training, 76--118 test per family); preliminary mixed-LLM training (Appendix~\\ref{app:mixed_llm}) suggests this limitation is addressable. Most pairwise comparisons rely on 3 seeds; key scrambled-vs.-correct comparisons are extended to 10 seeds (Appendix~\\ref{app:seed_level}). ToxicChat validates transfer to human-authored single-turn attacks (+18--42\\,pp over vanilla), but the evidence hierarchy reverses on this data (Section~\\ref{sec:discussion}), and no human-generated multi-turn jailbreak dataset exists.\n\nOOD results reflect attack-side generalization only; benign data is IID, so OOD F1 figures are upper bounds. On WildChat, 9-class FPR reaches 68.1\\%; 10 target-domain conversations eliminate it ($n$\\,=\\,49). OASST2 confirms the pattern but requires 25--50 conversations for comparable reduction (FPR\\,=\\,1.0\\%$\\pm$0.5\\% at $N$\\,=\\,25, 3 seeds; Appendix~\\ref{app:oasst2}); validation on additional platforms is needed. Residual calibration error (ECE\\,=\\,0.126--0.141; Appendix~\\ref{app:calibration}) suggests temperature scaling is needed for deployment.\n\nBenign-only adaptation addresses human-population distribution shift (WildChat, OASST2) but not cross-LLM distribution shift: adapting on Llama-origin benign conversations reduces FPR but collapses Llama jailbreak detection, as the model conflates LLM-specific style features with benign class membership (Appendix~\\ref{app:cross_llm}). Three encoders (125M--355M) differ in architecture and pretraining; same-architecture scaling is needed to isolate the capacity effect. Only persuasion-mediated multi-turn attacks fall within scope; single-turn token-level attacks~\\citep{zou2023gcg}, non-persuasive strategies, and non-text modalities are not addressed. Total pipeline cost is under 4 GPU-hours on a single A100.\n\n\\section*{Ethics Statement}\n\nThis work is defensive: it improves detection of multi-turn jailbreak attacks rather than developing new attacks. We acknowledge dual-use risk, as the persuasion taxonomy could inform adversarial actors. We mitigate this by using only synthetic conversations (no real harmful content) and withholding attack-generation prompts. Detection code, model weights, and evaluation data will be released under CC BY-NC 4.0. No human subjects were involved.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---


### Assistant

_source line 204_

All edits are in place. Here's a summary of what was done:

**P11 (references):** Added `hsu2024improved` and `li2025m2s` to `references.bib`. Cited Hsu et al. in related work's single-turn defenses list. Cited M2S as a complementary approach in the same paragraph. TrajGuard and SAE Mitigators were already cited.

**P2 (scope limiting):**
- `abstract.tex`: Added "On synthetic multi-turn data," before the classification DAPT claim
- `introduction.tex`: Changed "Two-step adaptation protocol" → "Preliminary two-step adaptation protocol" with "On the synthetic benchmark" qualifier
- `conclusion.tex`: Added "On synthetic multi-turn data" scope; changed "yields a two-step protocol" → "suggest a preliminary two-step protocol"

**P3 (Mixed-LLM downgrade):**
- Reframed subsection as "exploratory cross-LLM condition"
- Added AA F1=0.504 falls below trivial all-benign baseline (~0.808)
- Added cross-LLM style confound sentence citing Appendix cross_llm

**P9 (length confound):**
- Added to Summary paragraph: length difference noted (12–20 vs 3–10 turns) with three controls (truncation 0% FPR, single-turn F1=0.773, padding −57.9pp on AA)

**P14 (scrambled labels):**
- Code confirms multi-permutation: each of the 10 TOST seeds generates an independent random permutation via `scramble_strategies(data, seed)`. Added clarifying parenthetical "(each using an independent random permutation)" to the TOST description.

**P15 (strategy annotation prompt):**
- Skipped. No separate prompt file exists; strategies are assigned during generation (embedded in `generate_crescendo_v2.py`). Appendix already describes the process and promises release.

**Page budget:** Conclusion ends on page 8. Limitations/Ethics/References on page 9+. Main text ≤ 8 pages confirmed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "uuid": "0ed5a561-58bf-4bd1-ad15-817919f975ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kq2h99Jrgre3szEVdNwxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2688,
      "cache_read_input_tokens": 109155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2688
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

_source line 205_

All edits are in place. Here's a summary of what was done:

**P11 (references):** Added `hsu2024improved` and `li2025m2s` to `references.bib`. Cited Hsu et al. in related work's single-turn defenses list. Cited M2S as a complementary approach in the same paragraph. TrajGuard and SAE Mitigators were already cited.

**P2 (scope limiting):**
- `abstract.tex`: Added "On synthetic multi-turn data," before the classification DAPT claim
- `introduction.tex`: Changed "Two-step adaptation protocol" → "Preliminary two-step adaptation protocol" with "On the synthetic benchmark" qualifier
- `conclusion.tex`: Added "On synthetic multi-turn data" scope; changed "yields a two-step protocol" → "suggest a preliminary two-step protocol"

**P3 (Mixed-LLM downgrade):**
- Reframed subsection as "exploratory cross-LLM condition"
- Added AA F1=0.504 falls below trivial all-benign baseline (~0.808)
- Added cross-LLM style confound sentence citing Appendix cross_llm

**P9 (length confound):**
- Added to Summary paragraph: length difference noted (12–20 vs 3–10 turns) with three controls (truncation 0% FPR, single-turn F1=0.773, padding −57.9pp on AA)

**P14 (scrambled labels):**
- Code confirms multi-permutation: each of the 10 TOST seeds generates an independent random permutation via `scramble_strategies(data, seed)`. Added clarifying parenthetical "(each using an independent random permutation)" to the TOST description.

**P15 (strategy annotation prompt):**
- Skipped. No separate prompt file exists; strategies are assigned during generation (embedded in `generate_crescendo_v2.py`). Appendix already describes the process and promises release.

**Page budget:** Conclusion ends on page 8. Limitations/Ethics/References on page 9+. Main text ≤ 8 pages confirmed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 467205,
  "duration_api_ms": 453707,
  "num_turns": 76,
  "stop_reason": "end_turn",
  "session_id": "62775f4c-2fa3-4a61-aeff-0cf16cbe837a",
  "total_cost_usd": 3.4574269999999996,
  "usage": {
    "input_tokens": 56,
    "cache_creation_input_tokens": 100002,
    "cache_read_input_tokens": 4584029,
    "output_tokens": 21510,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 100002,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 510,
        "cache_read_input_tokens": 109155,
        "cache_creation_input_tokens": 2688,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2688
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2195,
      "outputTokens": 35,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0023699999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 56,
      "outputTokens": 21510,
      "cacheReadInputTokens": 4584029,
      "cacheCreationInputTokens": 100002,
      "webSearchRequests": 0,
      "costUSD": 3.4550569999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e814bab5-f0c3-43da-b1ae-80869af8fd1a"
}
```

</details>

---
