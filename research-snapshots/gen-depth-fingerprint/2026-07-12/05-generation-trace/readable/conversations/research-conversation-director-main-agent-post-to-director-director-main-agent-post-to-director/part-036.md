# Research conversation: [系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director  — Part 36 of 46

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

[← Part 35](part-035.md) · [Transcript overview](../research-conversation-director-main-agent-post-to-director-director-main-agent-post-to-director.md) · [Part 37 →](part-037.md) · [Structured JSON](../../../sessions/23/233efc253e1583c5469f.json)

## Round 329

### Assistant

_source line 6855 · 2026-05-18T23:55:49.839Z_

还差几行。继续压缩新增文本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40eba718-b95f-4053-88b0-afbccfa4b83b",
  "isSidechain": false,
  "requestId": "req_011CbAwKq4Z2ZRbepA9fBhkH",
  "type": "assistant",
  "uuid": "ffae3cd4-211b-41be-81f6-afe7c14ebce6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HARfcL7HDDYQCJj42di3ZD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 136092,
      "output_tokens": 2434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2434,
          "cache_read_input_tokens": 136092,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
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

_source line 6856 · 2026-05-18T23:55:51.922Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014UXp6cJF5qakbW1ht4FRq4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex",
  "old_string": "Our experiments use three overlapping generator subsets reflecting the chronological expansion of the study: the original 5-generator set (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B) for cross-model chains, a 6-generator set (adding Qwen3-8B) for appendix analyses, and the full 8-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3) for single-generator LOGO.\nEach table notes its subset.",
  "new_string": "Three overlapping generator subsets are used: the original 5-generator set (Pythia, OLMo, Qwen) for cross-model chains, a 6-generator set (adding Qwen3-8B) for appendix analyses, and the full 8-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3) for single-generator LOGO; each table notes its subset."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffae3cd4-211b-41be-81f6-afe7c14ebce6",
  "isSidechain": false,
  "requestId": "req_011CbAwKq4Z2ZRbepA9fBhkH",
  "type": "assistant",
  "uuid": "9b0ee87f-0766-4eee-bae7-3f627df02f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HARfcL7HDDYQCJj42di3ZD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 136092,
      "output_tokens": 2434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2434,
          "cache_read_input_tokens": 136092,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
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

_source line 6857 · 2026-05-18T23:55:57.616Z_

<details><summary>↩ Tool result · `toolu_01XzW2XyPxCZg1D5pTEQTeuq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efaccc7c-7f40-4105-bbaf-4e7aa6e2f0e0",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "283edb23-2e1b-46e8-8dc0-88873e0d93e6",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
    "oldString": "The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count.\nThis is consistent with depth profiling serving a diagnostic rather than prescriptive role: it characterizes provenance without prescribing curation strategy.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering.",
    "newString": "The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count, consistent with depth profiling serving a diagnostic rather than prescriptive role.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\nUnder fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.\nSampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nDDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).\n\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\nPer-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.\nCross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.\n\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.\n\nThe negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count.\nThis is consistent with depth profiling serving a diagnostic rather than prescriptive role: it characterizes provenance without prescribing curation strategy.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering.\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 6,
        "newStart": 19,
        "newLines": 5,
        "lines": [
          " Depth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).",
          " Instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.",
          " ",
          "-The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count.",
          "-This is consistent with depth profiling serving a diagnostic rather than prescriptive role: it characterizes provenance without prescribing curation strategy.",
          "+The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count, consistent with depth profiling serving a diagnostic rather than prescriptive role.",
          " The practical value lies in corpus-level depth auditing rather than sample-level filtering."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "efaccc7c-7f40-4105-bbaf-4e7aa6e2f0e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool result

_source line 6858 · 2026-05-18T23:55:51.952Z_

<details><summary>↩ Tool result · `toolu_014UXp6cJF5qakbW1ht4FRq4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b0ee87f-0766-4eee-bae7-3f627df02f61",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "36e1a77d-7857-4ae0-a618-3659841bea7c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex",
    "oldString": "Our experiments use three overlapping generator subsets reflecting the chronological expansion of the study: the original 5-generator set (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B) for cross-model chains, a 6-generator set (adding Qwen3-8B) for appendix analyses, and the full 8-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3) for single-generator LOGO.\nEach table notes its subset.",
    "newString": "Three overlapping generator subsets are used: the original 5-generator set (Pythia, OLMo, Qwen) for cross-model chains, a 6-generator set (adding Qwen3-8B) for appendix analyses, and the full 8-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3) for single-generator LOGO; each table notes its subset.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 8,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " \\subsection{Evaluation Protocol}",
          " \\label{sec:evaluation}",
          " ",
          "-Our experiments use three overlapping generator subsets reflecting the chronological expansion of the study: the original 5-generator set (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B) for cross-model chains, a 6-generator set (adding Qwen3-8B) for appendix analyses, and the full 8-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3) for single-generator LOGO.",
          "-Each table notes its subset.",
          "+Three overlapping generator subsets are used: the original 5-generator set (Pythia, OLMo, Qwen) for cross-model chains, a 6-generator set (adding Qwen3-8B) for appendix analyses, and the full 8-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3) for single-generator LOGO; each table notes its subset.",
          " ",
          " \\paragraph{Cross-validation.}",
          " To evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the eight generators is held out for testing and the remaining seven provide training data."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9b0ee87f-0766-4eee-bae7-3f627df02f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6859 · 2026-05-18T23:55:53.654Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GLXMz7xTJJL87MQokMSrsa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex",
  "old_string": "TTR and hapax ratio are strongly correlated ($r = 0.97$), reducing effective feature dimensionality to approximately five.\nBoth are retained because LOFO confirms marginal positive contribution from each, and the DDR partition is defined by depth-sensitivity properties ($\\rho$, $d$), not by feature independence.",
  "new_string": "TTR and hapax ratio are strongly correlated ($r = 0.97$), reducing effective dimensionality to ${\\sim}$5; both are retained because LOFO confirms positive contribution from each and the DDR partition is defined by depth-sensitivity ($\\rho$, $d$), not feature independence."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36e1a77d-7857-4ae0-a618-3659841bea7c",
  "isSidechain": false,
  "requestId": "req_011CbAwKq4Z2ZRbepA9fBhkH",
  "type": "assistant",
  "uuid": "61287336-428c-41e5-a7ae-90f42f9741e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HARfcL7HDDYQCJj42di3ZD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 136092,
      "output_tokens": 2434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2434,
          "cache_read_input_tokens": 136092,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
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

_source line 6860 · 2026-05-18T23:55:53.664Z_

<details><summary>↩ Tool result · `toolu_01GLXMz7xTJJL87MQokMSrsa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61287336-428c-41e5-a7ae-90f42f9741e8",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "440b016f-9d85-45a3-a89a-24ac5a35be5e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex",
    "oldString": "TTR and hapax ratio are strongly correlated ($r = 0.97$), reducing effective feature dimensionality to approximately five.\nBoth are retained because LOFO confirms marginal positive contribution from each, and the DDR partition is defined by depth-sensitivity properties ($\\rho$, $d$), not by feature independence.",
    "newString": "TTR and hapax ratio are strongly correlated ($r = 0.97$), reducing effective dimensionality to ${\\sim}$5; both are retained because LOFO confirms positive contribution from each and the DDR partition is defined by depth-sensitivity ($\\rho$, $d$), not feature independence.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 72,
        "oldLines": 8,
        "newStart": 72,
        "newLines": 7,
        "lines": [
          " We adopt $|\\rho| < 0.10$ as a practical threshold for near-zero monotonic association (Figure~\\ref{fig:feature-drift}).",
          " This differential behavior, consistent with recursive generation shifting the location of the NLL distribution while shape features show an order-of-magnitude smaller effect, motivates combining both feature types.",
          " As shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.",
          "-TTR and hapax ratio are strongly correlated ($r = 0.97$), reducing effective feature dimensionality to approximately five.",
          "-Both are retained because LOFO confirms marginal positive contribution from each, and the DDR partition is defined by depth-sensitivity properties ($\\rho$, $d$), not by feature independence.",
          "+TTR and hapax ratio are strongly correlated ($r = 0.97$), reducing effective dimensionality to ${\\sim}$5; both are retained because LOFO confirms positive contribution from each and the DDR partition is defined by depth-sensitivity ($\\rho$, $d$), not feature independence.",
          " ",
          " \\subsection{Evaluation Protocol}",
          " \\label{sec:evaluation}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "61287336-428c-41e5-a7ae-90f42f9741e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6861 · 2026-05-18T23:55:55.598Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01R8x1bYTw9HLETez4QUzGUz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
  "old_string": "Under fixed temperature $\\tau$ and nucleus $p$, the softmax output distribution's shape (variance, tail behavior) is constrained by the decoding configuration.\nIterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable to the reference model), but shape parameters are anchored by the fixed sampling regime.",
  "new_string": "Under fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "440b016f-9d85-45a3-a89a-24ac5a35be5e",
  "isSidechain": false,
  "requestId": "req_011CbAwKq4Z2ZRbepA9fBhkH",
  "type": "assistant",
  "uuid": "e20f1fad-2f24-4ff7-acc2-8aad706dc503",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HARfcL7HDDYQCJj42di3ZD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 136092,
      "output_tokens": 2434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2434,
          "cache_read_input_tokens": 136092,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
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

_source line 6862 · 2026-05-18T23:55:55.606Z_

<details><summary>↩ Tool result · `toolu_01R8x1bYTw9HLETez4QUzGUz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e20f1fad-2f24-4ff7-acc2-8aad706dc503",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "4dcbacd6-eea3-4ede-b499-911dc82d25aa",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
    "oldString": "Under fixed temperature $\\tau$ and nucleus $p$, the softmax output distribution's shape (variance, tail behavior) is constrained by the decoding configuration.\nIterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable to the reference model), but shape parameters are anchored by the fixed sampling regime.",
    "newString": "Under fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\nUnder fixed temperature $\\tau$ and nucleus $p$, the softmax output distribution's shape (variance, tail behavior) is constrained by the decoding configuration.\nIterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable to the reference model), but shape parameters are anchored by the fixed sampling regime.\nSampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nDDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).\n\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\nPer-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.\nCross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.\n\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.\n\nThe negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count.\nThis is consistent with depth profiling serving a diagnostic rather than prescriptive role: it characterizes provenance without prescribing curation strategy.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 8,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Discussion}",
          " \\label{sec:discussion}",
          " ",
          "-Under fixed temperature $\\tau$ and nucleus $p$, the softmax output distribution's shape (variance, tail behavior) is constrained by the decoding configuration.",
          "-Iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable to the reference model), but shape parameters are anchored by the fixed sampling regime.",
          "+Under fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.",
          " Sampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).",
          " DDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.",
          " Entropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$)."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "e20f1fad-2f24-4ff7-acc2-8aad706dc503",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6863 · 2026-05-18T23:55:57.604Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XzW2XyPxCZg1D5pTEQTeuq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
  "old_string": "The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count.\nThis is consistent with depth profiling serving a diagnostic rather than prescriptive role: it characterizes provenance without prescribing curation strategy.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering.",
  "new_string": "The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count, consistent with depth profiling serving a diagnostic rather than prescriptive role.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dcbacd6-eea3-4ede-b499-911dc82d25aa",
  "isSidechain": false,
  "requestId": "req_011CbAwKq4Z2ZRbepA9fBhkH",
  "type": "assistant",
  "uuid": "efaccc7c-7f40-4105-bbaf-4e7aa6e2f0e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HARfcL7HDDYQCJj42di3ZD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 136092,
      "output_tokens": 2434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2434,
          "cache_read_input_tokens": 136092,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 244
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

_source line 6864_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-18。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R19 审稿修复 — 统一写作 Pass  投稿目标：EMNLP 2026 ARR，DDL 2025-05-25。引用不用验证。  以下修改需要一次 unified pass…",
  "leafUuid": "283edb23-2e1b-46e8-8dc0-88873e0d93e6",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 6865_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Tool call

_source line 6866 · 2026-05-18T23:56:02.036Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MczUQR6p8GG1nJNfAm8LYi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -2 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -2",
  "description": "Compile and check",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "283edb23-2e1b-46e8-8dc0-88873e0d93e6",
  "isSidechain": false,
  "requestId": "req_011CbAwNezQArxsyukJ3B39A",
  "type": "assistant",
  "uuid": "d2d44753-32db-4512-842e-a893b9d08c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165DSHoRN8ZU47hfpFbsXrg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 136336,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2707,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 136336,
          "cache_creation_input_tokens": 2707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2707
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

_source line 6867 · 2026-05-18T23:56:03.809Z_

<details><summary>↩ Tool result · `toolu_01MczUQR6p8GG1nJNfAm8LYi`</summary>

```text
Output written on main.pdf (25 pages, 2781763 bytes).
Transcript written on main.log.
Output written on main.pdf (25 pages, 2781745 bytes).
Transcript written on main.log.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2d44753-32db-4512-842e-a893b9d08c83",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "370bb557-0997-41ca-9b84-1e0cc7756038",
  "toolUseResult": {
    "stdout": "Output written on main.pdf (25 pages, 2781763 bytes).\nTranscript written on main.log.\nOutput written on main.pdf (25 pages, 2781745 bytes).\nTranscript written on main.log.",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d2d44753-32db-4512-842e-a893b9d08c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6868 · 2026-05-18T23:56:07.090Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TgCYXCJb26YmyktA9beBBA`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && grep \"\\\\\\\\newlabel{sec:conclusion}\" main.aux",
  "description": "Check Conclusion page"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "370bb557-0997-41ca-9b84-1e0cc7756038",
  "isSidechain": false,
  "requestId": "req_011CbAwP7B1ADFTFEu7HNQRz",
  "type": "assistant",
  "uuid": "e8750b68-dabd-4a6a-84ee-a6a1aff36e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrWtVeLTMtPvQrsw6r6r3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 139043,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 139043,
          "cache_creation_input_tokens": 287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 287
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

_source line 6869 · 2026-05-18T23:56:07.142Z_

<details><summary>↩ Tool result · `toolu_01TgCYXCJb26YmyktA9beBBA`</summary>

```text
\newlabel{sec:conclusion}{{6}{9}{Conclusion}{section.6}{}}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8750b68-dabd-4a6a-84ee-a6a1aff36e62",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "8ad8013a-44b1-4139-8fc4-f7f6c2a08b8e",
  "toolUseResult": {
    "stdout": "\\newlabel{sec:conclusion}{{6}{9}{Conclusion}{section.6}{}}",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e8750b68-dabd-4a6a-84ee-a6a1aff36e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Assistant

_source line 6870 · 2026-05-18T23:56:30.238Z_

<details><summary>Logged reasoning block</summary>

```text
Still page 9. I need to cut more aggressively. Let me check how far into page 9 the Conclusion starts — if it's just barely over the boundary, I need just a few more lines.

Let me look at where the Discussion ends and Conclusion begins. If Discussion takes up most of page 8 and spills slightly onto page 9, that's where the problem is.

Let me think about what else I can cut:

1. The "a priori" statement in method.tex: "Features were designed a priori from these two complementary theoretical perspectives; no larger candidate set was explored or filtered." — Could I make this even shorter? "The seven features were selected a priori; no larger candidate set was explored."


2. In method.tex, the entropy_min description — I've already tightened the wording but it's still taking up space. Could I compress it further?
3. The entropy_std sentence in Discussion is already fairly tight, so that's probably not where the savings are.
4. In Results, I could try merging the length confound and QLoRA discussions into a single point rather than treating them separately.

But stepping back, the real issue is that my edits shifted Conclusion from page 8 to page 9. Let me trace through what I actually added versus removed. I'm adding scattered content across multiple sections — a priori, TTR/hapax, generator subset, expanded discussion opening, downstream material, QLoRA — while cutting an interpretive sentence or two from results. The net effect is probably around 2-3 lines of new content, which is enough to push the page break. So rather than hunting for individual sentences to trim, I should look for one or two places where I can consolidate ideas more efficiently.

The downstream paragraph in Discussion is a good candidate — I can compress it into a single sentence that captures the key insight about diagnostic versus prescriptive value. Similarly, the DDR phenomenon sentence is a bit wordy; I can tighten it by removing some of the parenthetical detail without losing the core claim about parameter-dependence. Either of these moves would save roughly a line each, which should bring Conclusion back to page 8.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ad8013a-44b1-4139-8fc4-f7f6c2a08b8e",
  "isSidechain": false,
  "requestId": "req_011CbAwPMRVzewXJ4eWwQoEe",
  "type": "assistant",
  "uuid": "226addd8-41e0-489e-a10b-a21c1150948d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqXhajoVX2VXnhVpJ6uGFD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 139330,
      "output_tokens": 1569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1569,
          "cache_read_input_tokens": 139330,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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

_source line 6871 · 2026-05-18T23:56:30.243Z_

继续精简。目标再省 3-4 行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "226addd8-41e0-489e-a10b-a21c1150948d",
  "isSidechain": false,
  "requestId": "req_011CbAwPMRVzewXJ4eWwQoEe",
  "type": "assistant",
  "uuid": "20b06ae5-5bd8-4e9c-bbfc-0e5319d3435d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqXhajoVX2VXnhVpJ6uGFD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 139330,
      "output_tokens": 1569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1569,
          "cache_read_input_tokens": 139330,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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

_source line 6872 · 2026-05-18T23:56:32.101Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Rg2o1E1iyhiY6aL2DhSZpk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
  "old_string": "The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count, consistent with depth profiling serving a diagnostic rather than prescriptive role.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering.",
  "new_string": "The negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20b06ae5-5bd8-4e9c-bbfc-0e5319d3435d",
  "isSidechain": false,
  "requestId": "req_011CbAwPMRVzewXJ4eWwQoEe",
  "type": "assistant",
  "uuid": "973e5a5c-2162-4b26-94ee-7f9b2cac9629",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqXhajoVX2VXnhVpJ6uGFD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 139330,
      "output_tokens": 1569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1569,
          "cache_read_input_tokens": 139330,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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

_source line 6873 · 2026-05-18T23:56:34.833Z_

<details><summary>↩ Tool result · `toolu_01QGgs68tQfSjsK6NC1bKZs6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2500e11-73de-46a1-83b4-0ba4542fb80f",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "29bab8f6-b4ef-4d62-b3c9-1d7a1dbada36",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex",
    "oldString": "Features were designed a priori from these two complementary theoretical perspectives; no larger candidate set was explored or filtered.",
    "newString": "The seven features were selected a priori; no larger candidate set was explored.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 40,
        "oldLines": 7,
        "newStart": 40,
        "newLines": 7,
        "lines": [
          " Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.",
          " Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes); Figure~\\ref{fig:framework} provides an overview.",
          " This two-pronged design is not post-hoc: it follows directly from the observation that recursive generation exhibits a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).",
          "-Features were designed a priori from these two complementary theoretical perspectives; no larger candidate set was explored or filtered.",
          "+The seven features were selected a priori; no larger candidate set was explored.",
          " ",
          " We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a2500e11-73de-46a1-83b4-0ba4542fb80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool result

_source line 6874 · 2026-05-18T23:56:32.116Z_

<details><summary>↩ Tool result · `toolu_01Rg2o1E1iyhiY6aL2DhSZpk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "973e5a5c-2162-4b26-94ee-7f9b2cac9629",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "6db9777a-1c31-4dd4-a6b8-d3f839744842",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
    "oldString": "The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count, consistent with depth profiling serving a diagnostic rather than prescriptive role.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering.",
    "newString": "The negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\nUnder fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.\nSampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nDDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).\n\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\nPer-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.\nCross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.\n\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.\n\nThe negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count, consistent with depth profiling serving a diagnostic rather than prescriptive role.\nThe practical value lies in corpus-level depth auditing rather than sample-level filtering.\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 5,
        "newStart": 19,
        "newLines": 4,
        "lines": [
          " Depth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).",
          " Instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.",
          " ",
          "-The negative downstream result (Appendix~\\ref{app:downstream}) indicates that depth composition alone does not determine training utility at fixed sample count, consistent with depth profiling serving a diagnostic rather than prescriptive role.",
          "-The practical value lies in corpus-level depth auditing rather than sample-level filtering.",
          "+The negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "973e5a5c-2162-4b26-94ee-7f9b2cac9629",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6875 · 2026-05-18T23:56:33.547Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WBfmoSWpg9P1N5X7aS8gtk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
  "old_string": "DDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.",
  "new_string": "DDR is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6db9777a-1c31-4dd4-a6b8-d3f839744842",
  "isSidechain": false,
  "requestId": "req_011CbAwPMRVzewXJ4eWwQoEe",
  "type": "assistant",
  "uuid": "11724601-46f5-406a-a1ab-8a54ffd1c562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqXhajoVX2VXnhVpJ6uGFD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 139330,
      "output_tokens": 1569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1569,
          "cache_read_input_tokens": 139330,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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

_source line 6876 · 2026-05-18T23:56:33.556Z_

<details><summary>↩ Tool result · `toolu_01WBfmoSWpg9P1N5X7aS8gtk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11724601-46f5-406a-a1ab-8a54ffd1c562",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "1af5aa20-6260-473b-8915-c80c347a72ed",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
    "oldString": "DDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.",
    "newString": "DDR is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\nUnder fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.\nSampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nDDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).\n\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\nPer-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.\nCross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.\n\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.\n\nThe negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " ",
          " Under fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.",
          " Sampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).",
          "-DDR as characterized here is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation independent of decoding conditions.",
          "+DDR is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation.",
          " Entropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).",
          " Semantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "11724601-46f5-406a-a1ab-8a54ffd1c562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6877 · 2026-05-18T23:56:34.824Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QGgs68tQfSjsK6NC1bKZs6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex",
  "old_string": "Features were designed a priori from these two complementary theoretical perspectives; no larger candidate set was explored or filtered.",
  "new_string": "The seven features were selected a priori; no larger candidate set was explored."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1af5aa20-6260-473b-8915-c80c347a72ed",
  "isSidechain": false,
  "requestId": "req_011CbAwPMRVzewXJ4eWwQoEe",
  "type": "assistant",
  "uuid": "a2500e11-73de-46a1-83b4-0ba4542fb80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqXhajoVX2VXnhVpJ6uGFD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 139330,
      "output_tokens": 1569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1569,
          "cache_read_input_tokens": 139330,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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

_source line 6878 · 2026-05-18T23:56:34.886Z_

```json
{
  "parentUuid": "29bab8f6-b4ef-4d62-b3c9-1d7a1dbada36",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3f1fac2c-e7cf-4d10-8429-bc5e87049b96",
  "timestamp": "2026-05-18T23:56:34.886Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

---


### Runtime record

_source line 6879_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-18。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R19 审稿修复 — 统一写作 Pass  投稿目标：EMNLP 2026 ARR，DDL 2025-05-25。引用不用验证。  以下修改需要一次 unified pass…",
  "leafUuid": "3f1fac2c-e7cf-4d10-8429-bc5e87049b96",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 6880_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Tool call

_source line 6881 · 2026-05-18T23:56:46.696Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LESVK6LNMzjjyLTy7R3DiD`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -2 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -2",
  "description": "Compile and check",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f1fac2c-e7cf-4d10-8429-bc5e87049b96",
  "isSidechain": false,
  "requestId": "req_011CbAwRQ4K2LbwBqvb3kz96",
  "type": "assistant",
  "uuid": "dfee5a5a-5b61-422d-9a2c-328bc41b3890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmWjYkgMcjepm1SK8BX97C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1878,
      "cache_read_input_tokens": 139532,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 139532,
          "cache_creation_input_tokens": 1878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1878
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

_source line 6882 · 2026-05-18T23:56:48.470Z_

<details><summary>↩ Tool result · `toolu_01LESVK6LNMzjjyLTy7R3DiD`</summary>

```text
Output written on main.pdf (25 pages, 2781691 bytes).
Transcript written on main.log.
Output written on main.pdf (25 pages, 2781606 bytes).
Transcript written on main.log.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfee5a5a-5b61-422d-9a2c-328bc41b3890",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "3cbd5a8f-ded5-45ae-a196-47f0eb736fb9",
  "toolUseResult": {
    "stdout": "Output written on main.pdf (25 pages, 2781691 bytes).\nTranscript written on main.log.\nOutput written on main.pdf (25 pages, 2781606 bytes).\nTranscript written on main.log.",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dfee5a5a-5b61-422d-9a2c-328bc41b3890",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6883 · 2026-05-18T23:56:51.328Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0197dhMK62keJvXDEBsTbuqj`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && grep \"\\\\\\\\newlabel{sec:conclusion}\" main.aux",
  "description": "Check Conclusion page"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cbd5a8f-ded5-45ae-a196-47f0eb736fb9",
  "isSidechain": false,
  "requestId": "req_011CbAwSQ8Z1d1SJDMyQjJii",
  "type": "assistant",
  "uuid": "40730f6c-48be-48f1-b5f8-349f9468a4ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLN6qNfT72LMF9ErHZtqM5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 141410,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 141410,
          "cache_creation_input_tokens": 287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 287
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

_source line 6884 · 2026-05-18T23:56:51.375Z_

<details><summary>↩ Tool result · `toolu_0197dhMK62keJvXDEBsTbuqj`</summary>

```text
\newlabel{sec:conclusion}{{6}{9}{Conclusion}{section.6}{}}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40730f6c-48be-48f1-b5f8-349f9468a4ab",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "18b0f17a-d863-40f5-8dbf-88abc12a72be",
  "toolUseResult": {
    "stdout": "\\newlabel{sec:conclusion}{{6}{9}{Conclusion}{section.6}{}}",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "40730f6c-48be-48f1-b5f8-349f9468a4ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Assistant

_source line 6885 · 2026-05-18T23:56:55.258Z_

<details><summary>Logged reasoning block</summary>

```text
Still page 9. I need to be more aggressive. Let me look at what I can cut from Discussion and Method that's not from this round of edits — the original text might also have room for trimming.

Let me re-read Discussion to see what's expendable:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18b0f17a-d863-40f5-8dbf-88abc12a72be",
  "isSidechain": false,
  "requestId": "req_011CbAwScYRkV2JgMWAu73r2",
  "type": "assistant",
  "uuid": "a425e128-a69d-437a-8d26-1f5c527e8c5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjShr2PsPtRLR83ukepbxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 141697,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 141697,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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

_source line 6886 · 2026-05-18T23:56:55.964Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YQhmaz3N9LnSeqp1d7t3kB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a425e128-a69d-437a-8d26-1f5c527e8c5a",
  "isSidechain": false,
  "requestId": "req_011CbAwScYRkV2JgMWAu73r2",
  "type": "assistant",
  "uuid": "7e163c2b-e51a-4e95-95a8-2bc027c9e413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjShr2PsPtRLR83ukepbxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 141697,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 141697,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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

_source line 6887 · 2026-05-18T23:56:55.968Z_

<details><summary>↩ Tool result · `toolu_01YQhmaz3N9LnSeqp1d7t3kB`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	Under fixed temperature $\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.
5	Sampling ablation supports this ($t \in [0.5, 0.7]$: ${\leq}0.3$\,pp degradation; $t = 1.0$: $-6$\,pp; Appendix~\ref{app:sampling-sensitivity}).
6	DDR is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation.
7	Entropy std ($|\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\rho| > 0.60$) and the near-stationary tail decay ($|\rho| = 0.04$).
8	Semantic-preservation constraints attenuate drift (elaboration F1\,=\,0.730 vs.\ continuation 0.781; Appendix~\ref{app:prompt-type}), consistent with \citet{broken_telephone}; cross-type transfer remains viable (F1\,=\,0.753).
9	
10	Document-level gen-1 per-class F1\,=\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\sqrt{n})$ error scaling).
11	The primary difficulty is distinguishing gen-1 from gen-2+: 86\% of binary errors are false negatives, with depth-2 error rate 48\% vs.\ 20\% for depth-4 (Appendix~\ref{app:error-analysis}).
12	This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\% vs.\ Pythia-1B 18\%).
13	Per-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\,pp; reference-family bias is limited.
14	Cross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.
15	
16	Model collapse \cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \emph{retrained} on their own outputs, losing distributional coverage through parameter updates.
17	DDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.
18	Three classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\,=\,0.905 (Appendix~\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.
19	Depth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\% edit distance) causes comparable degradation to 5\% random word replacement (Appendix~\ref{app:human-edit}).
20	Instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\,=\,0.338 vs.\ 0.763 base); this justifies our restriction to base models.
21	
22	The negative downstream result (Appendix~\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e163c2b-e51a-4e95-95a8-2bc027c9e413",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "4d0e922e-379a-4537-ae25-7fc337c9e771",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\nUnder fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.\nSampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nDDR is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation.\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).\n\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\nPer-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.\nCross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.\n\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.\n\nThe negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "7e163c2b-e51a-4e95-95a8-2bc027c9e413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool result

_source line 6888 · 2026-05-18T23:56:56.286Z_

<details><summary>↩ Tool result · `toolu_0161px6CTMcxY1Cy7tg5fUrm`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced generation depth classification and documented a differential depth response across eight base-model generators from five families: recursive generation is consistent with a systematic location shift in the token-level NLL distribution, with shape features showing an order-of-magnitude smaller effect, detectable with a lightweight 7-feature ensemble (binary F1\,=\,0.764 on cross-model chains, 0.694 under LOGO).
5	Equivalence testing (TOST $\pm$2\%, $p < 0.001$) confirms that depth-aware data selection yields training utility equivalent to random subsampling at equal sample count: the detected distributional shift does not translate to downstream perplexity degradation.
6	Two boundaries remain: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.
7	All code, data, and trained models will be released upon publication.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0aecf88c-3df4-4b84-9704-93d4d1dc9a3b",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "0c12a7b3-8df7-4152-862a-2dbbffa5c069",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced generation depth classification and documented a differential depth response across eight base-model generators from five families: recursive generation is consistent with a systematic location shift in the token-level NLL distribution, with shape features showing an order-of-magnitude smaller effect, detectable with a lightweight 7-feature ensemble (binary F1\\,=\\,0.764 on cross-model chains, 0.694 under LOGO).\nEquivalence testing (TOST $\\pm$2\\%, $p < 0.001$) confirms that depth-aware data selection yields training utility equivalent to random subsampling at equal sample count: the detected distributional shift does not translate to downstream perplexity degradation.\nTwo boundaries remain: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.\nAll code, data, and trained models will be released upon publication.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "0aecf88c-3df4-4b84-9704-93d4d1dc9a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6889 · 2026-05-18T23:56:56.275Z_

<details open><summary>🔧 Tool call — Read · `toolu_0161px6CTMcxY1Cy7tg5fUrm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d0e922e-379a-4537-ae25-7fc337c9e771",
  "isSidechain": false,
  "requestId": "req_011CbAwScYRkV2JgMWAu73r2",
  "type": "assistant",
  "uuid": "0aecf88c-3df4-4b84-9704-93d4d1dc9a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjShr2PsPtRLR83ukepbxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 141697,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 141697,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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

_source line 6890 · 2026-05-18T23:57:14.268Z_

<details><summary>Logged reasoning block</summary>

```text
Let me think about what I can tighten further. The Discussion is about 22 lines. The Conclusion is about 8 lines (4 sentences). The issue is that Discussion + Conclusion together are too long for page 8.

Let me look for redundancies:

1. Discussion L13: "Per-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\,pp; reference-family bias is limited." — This is already covered in Results §4.2 (cross-family reference models). 

Could be shortened: "Cross-reference experiments confirm limited reference-family bias (F1 within 0.013\,pp; Table~\ref{tab:cross-ref})."

2. Discussion L19: "Depth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\% edit distance) causes comparable degradation to 5\% random word replacement (Appendix~\ref{app:human-edit})." — This is interesting but detailed. Could be shortened.

3. Discussion L12: "This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\% vs.\ Pythia-1B 18\%)." — The generator-size effect is important but I'm repeating the mechanism explanation. Could trim the DDR explanation since it's already in Results.

Looking at the proposed compression, I'm cutting the specific error rates and consolidating the reference-family bias finding into a single statement. The key insight is that DDR explains the asymmetry and larger models show worse overlap, but I don't need both the mechanism and the exact percentages.

For the depth signal point, I'm removing the parenthetical edit distance detail since the core claim—that structure matters more than surface tokens—stands on its own with just the regeneration and word replacement comparison.

That's another half line saved. Combined with the earlier cuts, I'm now at roughly two lines of space recovered, which should be enough to fit everything within the page limit.

Now I'm looking at the cross-temperature section. I can compress it by using notation more efficiently and cutting the redundant statement about matched or lower temperature at test time, since that's already implied by the degradation pattern shown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c12a7b3-8df7-4152-862a-2dbbffa5c069",
  "isSidechain": false,
  "requestId": "req_011CbAwSyrLEZd7spvJYbKeT",
  "type": "assistant",
  "uuid": "b47756e2-750b-4d35-ab17-2e8a16d9332f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Yy4Fb493Yu1haUmRTvvf7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1563,
      "cache_read_input_tokens": 141899,
      "output_tokens": 1987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1987,
          "cache_read_input_tokens": 141899,
          "cache_creation_input_tokens": 1563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1563
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

_source line 6891 · 2026-05-18T23:57:14.433Z_

Discussion 中有原有文本可收紧：Results 中已有详细数据的条目在 Discussion 中可精简。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b47756e2-750b-4d35-ab17-2e8a16d9332f",
  "isSidechain": false,
  "requestId": "req_011CbAwSyrLEZd7spvJYbKeT",
  "type": "assistant",
  "uuid": "a337cb48-9152-49c8-a180-ee39e091093e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Yy4Fb493Yu1haUmRTvvf7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1563,
      "cache_read_input_tokens": 141899,
      "output_tokens": 1987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1987,
          "cache_read_input_tokens": 141899,
          "cache_creation_input_tokens": 1563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1563
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

_source line 6892 · 2026-05-18T23:57:16.996Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011NCrwLgb545Pbk7Nf2WNci`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
  "old_string": "This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\nPer-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.",
  "new_string": "This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap.\nCross-reference experiments confirm limited reference-family bias (F1 within 0.013\\,pp; Table~\\ref{tab:cross-ref})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a337cb48-9152-49c8-a180-ee39e091093e",
  "isSidechain": false,
  "requestId": "req_011CbAwSyrLEZd7spvJYbKeT",
  "type": "assistant",
  "uuid": "6ad00851-c7c2-43d6-bf68-2e4026681985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Yy4Fb493Yu1haUmRTvvf7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1563,
      "cache_read_input_tokens": 141899,
      "output_tokens": 1987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1987,
          "cache_read_input_tokens": 141899,
          "cache_creation_input_tokens": 1563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1563
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

_source line 6893 · 2026-05-18T23:57:20.483Z_

<details><summary>↩ Tool result · `toolu_01NtM5uvG1orsgPdUdbdQiFf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc15d7e4-4742-4910-a177-3685f9f43cd7",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "506eaf03-ca01-4b9b-b45b-02de2c686eb6",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
    "oldString": "Depth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).",
    "newString": "Depth signal resides in generative structure: LLM-simulated sentence regeneration causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\nUnder fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.\nSampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nDDR is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation.\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).\n\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap.\nCross-reference experiments confirm limited reference-family bias (F1 within 0.013\\,pp; Table~\\ref{tab:cross-ref}).\nCross-temperature transfer degrades substantially when test-time temperature exceeds training ($t{=}0.7 \\rightarrow$ mismatch: F1 from 0.789 to 0.418; Appendix~\\ref{app:cross-temp}); depth fingerprinting assumes matched or lower temperature.\n\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.\n\nThe negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering.\n",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 16,
        "newLines": 7,
        "lines": [
          " Model collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.",
          " DDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.",
          " Three classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.",
          "-Depth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).",
          "+Depth signal resides in generative structure: LLM-simulated sentence regeneration causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).",
          " Instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.",
          " ",
          " The negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "cc15d7e4-4742-4910-a177-3685f9f43cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool result

_source line 6894 · 2026-05-18T23:57:17.012Z_

<details><summary>↩ Tool result · `toolu_011NCrwLgb545Pbk7Nf2WNci`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ad00851-c7c2-43d6-bf68-2e4026681985",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "9bde45ea-43d6-49ea-aac1-ebd70b55a49c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
    "oldString": "This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\nPer-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.",
    "newString": "This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap.\nCross-reference experiments confirm limited reference-family bias (F1 within 0.013\\,pp; Table~\\ref{tab:cross-ref}).",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\nUnder fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.\nSampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nDDR is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation.\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).\n\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\nPer-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.\nCross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.\n\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.\n\nThe negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering.\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 8,
        "newStart": 9,
        "newLines": 8,
        "lines": [
          " ",
          " Document-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).",
          " The primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).",
          "-This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).",
          "-Per-generator F1 is highest for Pythia generators (0.718--0.724), which share the same architecture family as the Pythia-410M reference model; however, cross-reference experiments (Table~\\ref{tab:cross-ref}) show that alternative references (OLMo, Qwen) yield F1 within 0.013\\,pp; reference-family bias is limited.",
          "+This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap.",
          "+Cross-reference experiments confirm limited reference-family bias (F1 within 0.013\\,pp; Table~\\ref{tab:cross-ref}).",
          " Cross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.",
          " ",
          " Model collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "6ad00851-c7c2-43d6-bf68-2e4026681985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6895 · 2026-05-18T23:57:19.161Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013SuyB1bLmuyXVkFs68MKWA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
  "old_string": "Cross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.",
  "new_string": "Cross-temperature transfer degrades substantially when test-time temperature exceeds training ($t{=}0.7 \\rightarrow$ mismatch: F1 from 0.789 to 0.418; Appendix~\\ref{app:cross-temp}); depth fingerprinting assumes matched or lower temperature."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bde45ea-43d6-49ea-aac1-ebd70b55a49c",
  "isSidechain": false,
  "requestId": "req_011CbAwSyrLEZd7spvJYbKeT",
  "type": "assistant",
  "uuid": "5881f709-855e-4570-b2c9-a71344323af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Yy4Fb493Yu1haUmRTvvf7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1563,
      "cache_read_input_tokens": 141899,
      "output_tokens": 1987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1987,
          "cache_read_input_tokens": 141899,
          "cache_creation_input_tokens": 1563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1563
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

_source line 6896 · 2026-05-18T23:57:19.173Z_

<details><summary>↩ Tool result · `toolu_013SuyB1bLmuyXVkFs68MKWA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5881f709-855e-4570-b2c9-a71344323af2",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "a33d00b0-43da-40a8-9f9f-6856e489fed6",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
    "oldString": "Cross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.",
    "newString": "Cross-temperature transfer degrades substantially when test-time temperature exceeds training ($t{=}0.7 \\rightarrow$ mismatch: F1 from 0.789 to 0.418; Appendix~\\ref{app:cross-temp}); depth fingerprinting assumes matched or lower temperature.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\nUnder fixed temperature $\\tau$ and nucleus $p$, iterative conditioning shifts the input distribution's location (mean NLL decreases as text becomes more predictable), but shape parameters (variance, tail behavior) are anchored by the fixed sampling regime.\nSampling ablation supports this ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nDDR is a parameter-dependent phenomenon (modulated by temperature and prompt type), not an intrinsic property of recursive generation.\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}; cross-type transfer remains viable (F1\\,=\\,0.753).\n\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap.\nCross-reference experiments confirm limited reference-family bias (F1 within 0.013\\,pp; Table~\\ref{tab:cross-ref}).\nCross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.\n\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features.\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), evidence that richer signal exists beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base); this justifies our restriction to base models.\n\nThe negative downstream result (Appendix~\\ref{app:downstream}) confirms that depth profiling serves a diagnostic rather than prescriptive role: the practical value lies in corpus-level auditing, not sample-level filtering.\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 7,
        "newStart": 11,
        "newLines": 7,
        "lines": [
          " The primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).",
          " This asymmetry follows from DDR: the first recursive step produces the smallest location shift; larger generators exacerbate the overlap.",
          " Cross-reference experiments confirm limited reference-family bias (F1 within 0.013\\,pp; Table~\\ref{tab:cross-ref}).",
          "-Cross-temperature transfer shows substantial degradation when test-time temperature exceeds training-time settings: Qwen3-1.7B binary F1 drops from 0.789 (matched $t{=}0.7$) to 0.418 under temperature mismatch (Appendix~\\ref{app:cross-temp}). Depth fingerprinting assumes matched or lower temperature at test time.",
          "+Cross-temperature transfer degrades substantially when test-time temperature exceeds training ($t{=}0.7 \\rightarrow$ mismatch: F1 from 0.789 to 0.418; Appendix~\\ref{app:cross-temp}); depth fingerprinting assumes matched or lower temperature.",
          " ",
          " Model collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, losing distributional coverage through parameter updates.",
          " DDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and affects shape features an order of magnitude less than central-tendency features."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5881f709-855e-4570-b2c9-a71344323af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6897 · 2026-05-18T23:57:20.472Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NtM5uvG1orsgPdUdbdQiFf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
  "old_string": "Depth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).",
  "new_string": "Depth signal resides in generative structure: LLM-simulated sentence regeneration causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a33d00b0-43da-40a8-9f9f-6856e489fed6",
  "isSidechain": false,
  "requestId": "req_011CbAwSyrLEZd7spvJYbKeT",
  "type": "assistant",
  "uuid": "cc15d7e4-4742-4910-a177-3685f9f43cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Yy4Fb493Yu1haUmRTvvf7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1563,
      "cache_read_input_tokens": 141899,
      "output_tokens": 1987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1987,
          "cache_read_input_tokens": 141899,
          "cache_creation_input_tokens": 1563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1563
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

_source line 6898_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-18。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R19 审稿修复 — 统一写作 Pass  投稿目标：EMNLP 2026 ARR，DDL 2025-05-25。引用不用验证。  以下修改需要一次 unified pass…",
  "leafUuid": "506eaf03-ca01-4b9b-b45b-02de2c686eb6",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 6899_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Tool call

_source line 6900 · 2026-05-18T23:57:25.139Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MpVtv1ks6hWkLDCj7uD13p`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -2 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -2",
  "description": "Compile and check",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "506eaf03-ca01-4b9b-b45b-02de2c686eb6",
  "isSidechain": false,
  "requestId": "req_011CbAwUpSqyE8JFpGBRDFC8",
  "type": "assistant",
  "uuid": "bde2270c-2b85-4faa-bdef-8b45ace66da1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bRM5iKWnbuQR2P43MnR2g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2192,
      "cache_read_input_tokens": 143462,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2192,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 143462,
          "cache_creation_input_tokens": 2192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2192
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

_source line 6901 · 2026-05-18T23:57:28.038Z_

<details><summary>↩ Tool result · `toolu_01MpVtv1ks6hWkLDCj7uD13p`</summary>

```text
Output written on main.pdf (25 pages, 2781096 bytes).
Transcript written on main.log.
Output written on main.pdf (25 pages, 2781070 bytes).
Transcript written on main.log.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bde2270c-2b85-4faa-bdef-8b45ace66da1",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "e1759d5c-c186-47af-888c-f2cd86f6d336",
  "toolUseResult": {
    "stdout": "Output written on main.pdf (25 pages, 2781096 bytes).\nTranscript written on main.log.\nOutput written on main.pdf (25 pages, 2781070 bytes).\nTranscript written on main.log.",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bde2270c-2b85-4faa-bdef-8b45ace66da1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6902 · 2026-05-18T23:57:31.725Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VfA8B84y29jagkMSM5RtnP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper && grep \"\\\\\\\\newlabel{sec:conclusion}\" main.aux",
  "description": "Check Conclusion page"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1759d5c-c186-47af-888c-f2cd86f6d336",
  "isSidechain": false,
  "requestId": "req_011CbAwVKN9TY9QNT3YeJix4",
  "type": "assistant",
  "uuid": "4e0ba5da-d019-49ce-89ee-e6fe707f92ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WabnyXRJE2SW4HpEtADVdb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 145654,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 145654,
          "cache_creation_input_tokens": 287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 287
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

_source line 6903 · 2026-05-18T23:57:31.771Z_

<details><summary>↩ Tool result · `toolu_01VfA8B84y29jagkMSM5RtnP`</summary>

```text
\newlabel{sec:conclusion}{{6}{9}{Conclusion}{section.6}{}}
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e0ba5da-d019-49ce-89ee-e6fe707f92ab",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "e9466f41-b999-4c14-b6d7-3b3064747095",
  "toolUseResult": {
    "stdout": "\\newlabel{sec:conclusion}{{6}{9}{Conclusion}{section.6}{}}",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4e0ba5da-d019-49ce-89ee-e6fe707f92ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 6904 · 2026-05-18T23:57:31.773Z_

```json
{
  "parentUuid": "e9466f41-b999-4c14-b6d7-3b3064747095",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cfbcba15-3ae4-4221-86b3-ceda0e7d49c2",
  "timestamp": "2026-05-18T23:57:31.773Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

---


### Assistant

_source line 6905 · 2026-05-18T23:57:51.430Z_

<details><summary>Logged reasoning block</summary>

```text
Still page 9! This is very stubborn. Let me think about what's happening. The Conclusion is likely just a few lines onto page 9. Let me check if I can shorten Conclusion itself, or find more to cut from Discussion/Results.

Actually, let me check if the issue is float placement — maybe a figure or table is being placed differently. Let me also check the page numbers for all sections and see if the layout shifted.

Let me think more broadly. Perhaps I should check what's at the bottom of page 8. If Discussion ends near the bottom and there's just not enough room for the Conclusion section header + 4 lines, I might need to be more creative.
 
I'm weighing my options here: I could trim the Conclusion further, use negative spacing to squeeze things tighter, cut more from Discussion, or investigate whether a float is pushing content down. Let me actually look at the rendered PDF to see what's happening with the layout. I think the quickest path is to shorten the Conclusion itself — it's currently four sentences, and I can condense that third sentence about instruction tuning and frontier-scale models into something more concise.

Wait, but the real problem is that Discussion is already filling page 8 completely, so trimming Conclusion won't help much. I need to be more aggressive and pull content up from earlier sections like Method or Results. Let me examine the Method section for anything I can cut. Actually, let me step back and check the exact page layout — I need to see how much space is left on page 8 and whether Discussion is the actual bottleneck here. Converting to images will give me a clear picture of what's happening.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfbcba15-3ae4-4221-86b3-ceda0e7d49c2",
  "isSidechain": false,
  "requestId": "req_011CbAwVcZzrAHypoZXi5njF",
  "type": "assistant",
  "uuid": "76ee71a7-3f0a-4d69-900a-0edda5f97df1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WowjRQvrZYXEJCJA5yJbPi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 145941,
      "output_tokens": 638,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 638,
          "cache_read_input_tokens": 145941,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 305
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

_source line 6906 · 2026-05-18T23:57:51.431Z_

Layout 仍然紧张。查看 PDF 布局了解 page 8 底部的精确状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76ee71a7-3f0a-4d69-900a-0edda5f97df1",
  "isSidechain": false,
  "requestId": "req_011CbAwVcZzrAHypoZXi5njF",
  "type": "assistant",
  "uuid": "17a38cc0-73a5-4eae-8e87-1726bc4a6462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WowjRQvrZYXEJCJA5yJbPi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 145941,
      "output_tokens": 638,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 638,
          "cache_read_input_tokens": 145941,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 305
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

_source line 6907 · 2026-05-18T23:57:51.565Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018BNXcF86cq5jtSPfzC5paZ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17a38cc0-73a5-4eae-8e87-1726bc4a6462",
  "isSidechain": false,
  "requestId": "req_011CbAwVcZzrAHypoZXi5njF",
  "type": "assistant",
  "uuid": "4b901c98-9da8-45df-8beb-c1e7095b8d5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WowjRQvrZYXEJCJA5yJbPi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 145941,
      "output_tokens": 638,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 638,
          "cache_read_input_tokens": 145941,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 305
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

_source line 6908 · 2026-05-18T23:57:51.577Z_

<details><summary>↩ Tool result · `toolu_018BNXcF86cq5jtSPfzC5paZ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b901c98-9da8-45df-8beb-c1e7095b8d5d",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "2617e162-92e3-44c2-9361-54721609edc5",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "4b901c98-9da8-45df-8beb-c1e7095b8d5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 6909 · 2026-05-18T23:57:55.662Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01NUrjh5GxstJbB294CXKVdZ`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf",
  "pages": "8-9",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2617e162-92e3-44c2-9361-54721609edc5",
  "isSidechain": false,
  "requestId": "req_011CbAwX4aTVf1pavMTKyPXC",
  "type": "assistant",
  "uuid": "149f7ceb-9b74-468a-8e50-c48f449a69f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyETKeMqLDc85H6vAquCQ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 146246,
      "output_tokens": 139,
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
          "input_tokens": 3,
          "output_tokens": 139,
          "cache_read_input_tokens": 146246,
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


### Large event (continued)

````text
### Tool result

_source line 6910 · 2026-05-18T23:57:56.704Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01NUrjh5GxstJbB294CXKVdZ`&lt;/summary>

```text
Error: result (1,355,560 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/29d8b308-43be-4df5-b301-2fd1aaa58448/tool-results/mcp-agent-ml-research-pdf_to_images-1779148676671.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/29d8b308-43be-4df5-b301-2fd1aaa58448/tool-results/mcp-agent-ml-research-pdf_to_images-1779148676671.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "149f7ceb-9b74-468a-8e50-c48f449a69f4",
  "isSidechain": false,
  "promptId": "2900965e-5fa6-4049-be73-4189986755f2",
  "type": "user",
  "uuid": "d4e6b658-57a9-4764-9a6f-24470ee2c025",
  "toolUseResult": "Error: result (1,355,560 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/29d8b308-43be-4df5-b301-2fd1aaa58448/tool-results/mcp-agent-ml-research-pdf_to_images-1779148676671.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/29d8b308-43be-4df5-b301-2fd1aaa58448/tool-results/mcp-agent-ml-research-pdf_to_images-1779148676671.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/_pdf_images/main_p8.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAAeNDUlEQVR4nOydCZxO1f/HB0lC4ldRSJuKUlSIkELak5RQon5RFCFLlvpXspedZF/Hvs2YsQ1mmJUZ62AMs2CYfcyM2Zfn//F8/87/9jzP3OdhzB1mPu/XvOb13HPPPffs5/u559xznUyEEEIIIYQQQoixOBV3BAghhBBCCCGElDqoRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBiNNSihBBCCCGEEEKMhlqUEEIIIYQQQojRUIsSQgghhBBCCDEaalFCCCGEEEIIIUZDLUoIIYQQQgghxGioRQkhhBBCCCGEGA21KCGEEEIIIYQQo6EWJYQQQgghhBBi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eDF+shYDVK5cmdLo0qWL2yNGyAWXS5cutUS7ceNGUFBQsmTJgiORLl06Ys6YMSMhUm1gYGBgYGAQ5zBcNAnhhx9+sIT06NHjzTffdHjk22+/RRf8/vvvY/zRf/75p06dOp988kmM3+An+ETPnj3j+isWtGzZMh6y5oy9e/daQooXL/7FF18kSGIcULNmzZIlS6rL27dvw0kGDhxoifbbb7/973//00NWrFhRrlw5+e9PZo8ePUqrfvvttxOQiwYks6NGjaL3Xb58Wd2tXr16pUqV5P9nn33WqVMnuGucZCBwiIiIkOVNpI2E5MqVi8tnn33WEhNp06tXLz1H7733HhxeLwEDAwMDAwODxwmGiyZdPHjwAGV9165dviIsXboU9RGtER161qxZisoeOHBg7Nixw4YNk/VShZMnT06aNGnEiBH/+te/7t696/asgbRp04Y3vP7667zhzJkz8+fP58/WrVu5e/z48Tlz5nC5Z88eecMff/whZ95Wr149btw4eCz/edXChQv79+8/Y8aMa9eueU3qjRs3UHC3b99uCefNEydOHDx48MqVK+/fvy9JikEatmzZEh4eTsy1a9dK1gTr1q3LmTPnrVu3/CzzeMChQ4fSp0+fCM/Xkap27drpIZCuJ598MsoHmzVrRnvzesueWeq3ZcuWtIeE5aIByWyDBg3y5s2r34Vj05t+//13/sPl+B8UFFS1atXEfJB79+7dwkXbt28vIcWKFZOd1ZaYP/30k4WZFy1a9MUXX4ynhBq43TStmTNn/vnnnwmdkAAAsTx79uzffvvNORqZXbRo0Z07dwL1XcpwyZIlgXqbV8QyzQzEX3755d69ewOYawOvYIT69ttv7eE0Tsp/zZo1P/74o2gmviAaiAXbtm2TUSDRggwi+VGQHNIZERHxzTffEAely+FVXk9z8Mj69esDkFCDxAHDRZMuYG4hISEOEY4cOQKRQ2v85JNPfvnlF/FRPmXKlMmTJ589e3bx4sXowZBPiYxMyZo164ULF5BBqI+NGjVyew5wLl++nDeMGjWKN/z9998IJi4hqPKU6KnvvPMO/3lhlixZkiVLNnXq1Oeff55wEnDlypXmzZujpB47dqxatWpo814XSebOnZsmTRrLocG+fft27dqVj54/f7527doVKlQgeW6PrhCtNMBdW7VqxYCB+CtRooSegL/++otC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wMAgsWG4qIGBgYGBgYGBgYGBgUFiw3BRAwMDAwMDAzccOHBg8uTJSZ2L/8PFixdHjBixa9eusN5at27dhAkTEihLXhAbG5twiV+7du3IkSPUjJfIxAy39pIRIhOPpMX+/funTZuWEClfunTpn1D4999/nW/9/vvvEXzuwoULixcv/uyzz+bMmUPK0SiBwc0Pw0UNPOH06dNJnYV44X8WInjxzJkzUc/MjQxGoCtXrrhEuHr1KoNNouUn4ZDcRToxgaVy/vx5j5H//vvvBM1MPHGr9ej4Y9myZRUqVPD5fPfcc09S5+X/8PXXX5OfGjVqhPUW+eetJHFIfvLkyTZt2mzZssUWvnfv3vgnDgvt2bPniy+++NVXX3Xu3Jk/jh496v7K+PHj77zzztq1azdp0qTF9ejXr1/8s5S0iEw8kgo///xzpUqVyPADDzyQEOnPmDGjYcOGPgupU6cuWrRocQv8kTdvXgnXp5kuX7785Zdf5s6d++233w73W4cOHapZs+a6des+/PBDkn3kkUeiWhSDmxaGi94kiI2Nff/99+VvRqY+ffq0bdu2devW9evXHz16tC0yxiLjYuPGjV9++eXq1atv2LDBFoHRupqGhx566MiRI3qETZs2vfPOO7zLr61atQqWK96SOIwKDJZ//fVX375969atq1Im/Pnnn3/rrbdmzpwJydHfHThwYLSMBvhViRIlUK/eXyGrH3/8cbly5R5++OGo5OHGx8SJExGJDBky/Pbbb85fZXx69tlnM2bM+MMPPyR+9qKLX375JWXKlF26dEnqjNzomD59erNmzbJkyfL999+7x1y/fj22C+bUo48+mjh5CwtomNdeey1PnjzvvvtuUucl+WH37t1R5KKRTQvq+PPPPzGvMbLDemvIkCEvvPCC91mVaOHEiRNPPPGEk3aiUW+77TbG63imz1iP6laP06ZNK1iwoPuSFL3AFwTh1uoNiMjEI+rwLue///57wnFRwb333ssnsAlt4QcOHICXjh8/Xh6XLFny3nvvSeQIuGjlypVbtmwpfzO8klQ8s21wi8Bw0ZsBGzdubNq0qVrOgjCgiOVvFE2uXLl0nXLx4sWSJUsyJMvjwoULM2fObKOjderUuUsDQ13A75KIjF4///xzwAjdu3eXCB988IEKnD17NiEwAUbos2fPbtu2rUePHmnTps2bN++ePXv0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
```

---
