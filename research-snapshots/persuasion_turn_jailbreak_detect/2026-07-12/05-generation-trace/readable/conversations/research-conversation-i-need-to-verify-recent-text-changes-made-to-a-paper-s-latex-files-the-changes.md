# Research conversation: I need to verify recent text changes made to a paper's LaTeX files. The changes address R15 reviewer feedback. Check the

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aaf4887a739276af7.jsonl`
- **Structured JSON:** [`00f31d261413f3f4b3cd.json`](../../sessions/00/00f31d261413f3f4b3cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-22T13:48:23.710Z_

I need to verify recent text changes made to a paper's LaTeX files. The changes address R15 reviewer feedback. Check the following files and report the exact modified sections:

Base path: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/

1. **abstract.tex** — Should have been shortened, reduced to 2-3 key numbers (from 12+). Report the full abstract text.

2. **introduction.tex** — Check for:
   - DisPeD footnote explaining "disentangled" refers to two-stage architecture
   - "causal" → "discriminative" language change for probe references
   - C2 contribution downgraded from claim to "observation"
   - Zhang/Maennel framing change (should say "consistent with" not "opposite direction")

3. **conclusion.tex** — Check for:
   - "causal" → "discriminative" language
   - Zhang/Maennel framing change

4. **experiments.tex** — Check for variance claim softening (should say "observed 4-20× lower variance" or similar qualification)

5. **appendix.tex** — Check for "causal" → "discriminative" in probe table/section references

For each file, report the specific changed paragraphs/sentences so I can verify accuracy. Focus on whether the changes match the intent and whether any overcorrections or new issues were introduced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "3584446e-9dee-486b-85d6-e08d701b03fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T13:48:23.718Z_

```json
{
  "parentUuid": "3584446e-9dee-486b-85d6-e08d701b03fa",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e95d86f0-91fd-47f4-9004-0a434424ff1d",
  "timestamp": "2026-05-22T13:48:23.718Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

---

### Assistant

_source line 3 · 2026-05-22T13:48:31.625Z_



I'll read all the specified files in parallel to check the changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e95d86f0-91fd-47f4-9004-0a434424ff1d",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiH97gNN6LnrkfX2zvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8aebcd72-503e-4112-ab43-0d501ec36984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mgqQT1VGASxNUuU1vvbJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24770,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T13:48:32.309Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P3gxaPZuFBCVAayuoy1Kg9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aebcd72-503e-4112-ab43-0d501ec36984",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiH97gNN6LnrkfX2zvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86a4a967-3d18-459f-9295-32419855a612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mgqQT1VGASxNUuU1vvbJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24770,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T13:48:32.324Z_

<details><summary>↩ Tool result · `toolu_01P3gxaPZuFBCVAayuoy1Kg9`</summary>

```text
1	% abstract.tex — D048 deep writing optimization
2	\begin{abstract}
3	Detecting unseen multi-turn jailbreaks requires domain adaptation, but the form of adaptation matters.
4	Multi-turn jailbreak attacks spread adversarial intent across benign-seeming turns, and existing defenses fail to generalize across attack families: Llama Guard~3, a widely deployed safety classifier, detects only 1.8\% of multi-turn jailbreaks in our evaluation.
5	We isolate the factors behind cross-attack generalization on synthetic multi-turn data through controlled ablation: thirteen encoder configurations at three scales (125 to 355M parameters) decompose the contributions of domain exposure, classification supervision, label quality, and granularity on three out-of-distribution (OOD) attack families and two training compositions.
6	On single-source synthetic data, continued pretraining closes roughly 60 percentage points of the OOD gap without labels. This effectiveness is condition-dependent: on mixed-LLM training data, unsupervised pretraining collapses while classification-based adaptation remains the strongest variant (DD OOD F1\,=\,0.818 vs.\ 0.291 without adaptation).
7	Across three architectures (125--355M), the set of attacks requiring adaptation shrinks with scale, though architecture and pretraining differences prevent isolating scale as the sole factor.
8	Classification supervision is associated with substantially lower prediction variance on synthetic evaluations (observed across 3 seeds), with limited sensitivity to label correctness, but this benefit reverses on human-authored data.
9	These findings suggest classification DAPT provides robustness through optimization regularization, not semantic feature learning.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86a4a967-3d18-459f-9295-32419855a612",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "5f9ba11d-dad2-4a80-b64e-d238438e05d0",
  "sourceToolAssistantUUID": "86a4a967-3d18-459f-9295-32419855a612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T13:48:32.676Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VYEUPNVTQCGZqyuiVvPw95`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f9ba11d-dad2-4a80-b64e-d238438e05d0",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiH97gNN6LnrkfX2zvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96fcd26d-88e2-427f-bfcb-f17bd24a1d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mgqQT1VGASxNUuU1vvbJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24770,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T13:48:32.683Z_

<details><summary>↩ Tool result · `toolu_01VYEUPNVTQCGZqyuiVvPw95`</summary>

```text
1	% introduction.tex — expanded for 8-page target
2	
3	\section{Introduction}
4	
5	Multi-turn jailbreak attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} all rely on persuasion as their core mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} identify strategies in 97\% of successful attacks. Because individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, no single-turn filter can distinguish them from legitimate conversation.
6	
7	Existing defenses leave a critical gap. Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and miss multi-turn manipulation; Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks in our evaluation (Section~\ref{sec:decomposition}). Multi-turn defenses (DeepContext~\citep{deepcontext2026}, BIID~\citep{tong2025biid}, G-Guard~\citep{gguard2025}) model conversation-level structure but each evaluates on a single attack family. None answers the central question: \emph{what representation properties enable a detector to generalize across attack families it has never seen?}
8	
9	Pretrained language understanding does not suffice at base model scale: vanilla DeBERTa-v3~\citep{he2021deberta} with temporal aggregation (cf.\ DeepContext) drops from F1\,=\,1.000 in-distribution to 0.312 on OOD Deceptive Delight, and GPT-5.5 reaches only 0.191--0.449 F1 with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). The bottleneck is distributional: cross-attack generalization requires domain adaptation, not a better classifier.
10	
11	Our pipeline, \textbf{DisPeD} (Disentangled Persuasion Detection), separates encoder adaptation (Stage~1) from temporal classification (Stage~2, a frozen BiGRU; Figure~\ref{fig:architecture}). Seven Stage~1 variants each isolate a single factor while holding all others constant (Section~\ref{sec:method}); the contribution is the decomposition, not the pipeline.
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{figures/paper/fig1_architecture.pdf}
16	\caption{DisPeD architecture. Stage~1 adapts a DeBERTa encoder on jailbreak conversation text (seven variant objectives). Stage~2 aggregates frozen \texttt{[CLS]} embeddings via BiGRU for conversation-level jailbreak detection. Only user turns are processed.}
17	\label{fig:architecture}
18	\end{figure}
19	
20	Controlled ablation across DeBERTa-v3 and RoBERTa~\citep{liu2019roberta} on four attack families and two training compositions shows that for base-size encoders, classification-based adaptation is the most robust variant on synthetic multi-turn OOD attacks. MLM collapses on mixed-LLM training (F1\,=\,0.289 $\approx$ vanilla) while classification DAPT maintains 0.818; RoBERTa-large (355M) handles ActorAttack~\citep{ren2024actorattack} without adaptation. Classification supervision is associated with substantially lower prediction variance on synthetic data but not on human-authored conversations (Section~\ref{sec:human_data}).
21	
22	Our contributions:
23	\begin{itemize}[leftmargin=*, itemsep=2pt, topsep=4pt]
24	  \item \textbf{Systematic decomposition identifying the most robust adaptation and three counter-intuitive findings.} Controlled ablation across thirteen encoder configurations on synthetic multi-turn data shows classification-based DAPT is the most robust variant; unsupervised pretraining is effective on single-source data but collapses on mixed-LLM training. We report three supplementary findings that challenge common assumptions: scrambled labels perform comparably to correct labels (descriptive evidence at $n$=3 seeds), temporal order is irrelevant ($\Delta < 1$\,pp), and label granularity does not affect detection.
25	
26	  \item \textbf{Architecture- and scale-dependent observation on domain adaptation.} Three encoder scales (125M, 184M, 355M) suggest adaptation need shrinks with model size, though encoders differ in architecture; same-architecture scaling is needed to isolate scale. RoBERTa-large handles structurally complex attacks without adaptation (Section~\ref{sec:cross_encoder}).
27	
28	  \item \textbf{Mechanistic interpretation: optimization regularization, not semantic learning.} Three null results converge: frozen probing near-parity (AA gap 3.1\,pp), label content irrelevance ($d$\,=\,0.09), and temporal modeling irrelevance ($|\Delta| < 1$\,pp) indicate classification supervision provides robustness through optimization regularization that stabilizes downstream training. This benefit is condition-dependent (variance reversal on human data) but classification DAPT remains strongest under mixed-LLM training (Section~\ref{sec:discussion}). Continued pretraining is 266$\times$ faster than LLM-as-judge (Appendix~\ref{app:data_efficiency}).
29	\end{itemize}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96fcd26d-88e2-427f-bfcb-f17bd24a1d85",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "52ad4f25-7eac-4f2b-97e0-0acd8326384c",
  "sourceToolAssistantUUID": "96fcd26d-88e2-427f-bfcb-f17bd24a1d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T13:48:33.121Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HnjB9eJsp6bvhwfGdVz9gp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52ad4f25-7eac-4f2b-97e0-0acd8326384c",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiH97gNN6LnrkfX2zvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11f2699e-6d79-4cdf-b19c-df902e072ea4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mgqQT1VGASxNUuU1vvbJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24770,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T13:48:33.128Z_

<details><summary>↩ Tool result · `toolu_01HnjB9eJsp6bvhwfGdVz9gp`</summary>

```text
1	% conclusion.tex — compressed for 8-page limit
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\paragraph{Topic shortcut and label equivalence.}
7	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97).
8	
9	\paragraph{Single-LLM confound.}
10	ToxicChat (+18--42\,pp; Table~\ref{tab:human_data}) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer. Mixed-LLM 9-class maintains 0.818 while MLM collapses; MLM may capture LLM-specific surface patterns while classification extracts style-invariant features.
11	
12	\paragraph{Variance reversal on human data.}
13	Classification supervision is associated with lower variance on synthetic OOD (4--20$\times$ observed range, 3 seeds); on ToxicChat this reverses (std\,=\,0.087 vs.\ 0.013). Frozen probing localizes MLM instability to Stage-2 (Appendix~\ref{app:frozen_verify}).
14	
15	\paragraph{Encoder capacity and lexical analysis.}
16	Three encoders (125M--355M) differ in pretraining; same-architecture scaling is needed. TF-IDF collapses on ActorAttack (0.261 vs.\ 0.961 on DD).
17	
18	\paragraph{Regularization mechanism.}
19	Frozen probing near-parity (AA gap 3.1\,pp), label irrelevance ($d$\,=\,0.09), and mean pooling matching BiGRU ($|\Delta| < 1$\,pp) converge: classification DAPT provides robustness through optimization regularization~\citep{chen2020simclr,grill2020byol}, not semantic feature learning.
20	
21	\paragraph{Benign distribution as the remaining bottleneck.}
22	OOD F1 figures are upper bounds (benign is IID). On WildChat, 9-class FPR reaches 68.1\% (Appendix~\ref{app:wildchat_fpr}); cross-LLM error decomposition confirms collapse is driven by false positives on unfamiliar benign text.
23	
24	\section{Conclusion}
25	
26	Classification-based DAPT is the most robust adaptation for base-size encoders, providing robustness through optimization regularization rather than semantic learning; continued pretraining is 266$\times$ faster than LLM-as-judge (Appendix~\ref{app:efficiency}).
27	
28	\section{Limitations}
29	\label{sec:limitations}
30	
31	\paragraph{Multi-turn human validation.}
32	All multi-turn findings are derived from synthetic conversations generated by Qwen3-8B. ToxicChat validates transfer to human-authored single-turn attacks (+18--42\,pp over vanilla), but no human-generated multi-turn jailbreak dataset exists for evaluation. Whether the evidence hierarchy and classification supervision advantages generalize to human-authored multi-turn attacks remains the primary open question.
33	
34	\paragraph{Turn-count distribution.}
35	Benign conversations contain 12--20 turns, DD jailbreaks 6--10, and ActorAttack jailbreaks 3--8; the three categories have non-overlapping turn counts. Three observations argue against length as the primary detection cue: (a) early detection at equal-length prefixes $K$=1 and $K$=2 achieves AA OOD F1\,=\,0.773 and 0.935 (Appendix~\ref{tab:actorattack_full}); (b) vanilla models access the same length signal but achieve near-zero OOD recall; and (c) truncating benign conversations to 3 turns yields FPR\,=\,0\% (Appendix~\ref{app:length_independence}).
36	
37	\paragraph{Temporal aggregation dilution.}
38	When subtle attacks (ActorAttack) are followed by extended benign padding, BiGRU temporal aggregation dilutes attack signals (F1 drops from 0.963 to 0.383; Appendix~\ref{app:length_independence}); in practice, adversaries would not dilute their own successful attacks.
39	
40	\paragraph{OOD benign distribution.}
41	OOD results reflect attack-side generalization only (Section~\ref{sec:discussion}). Even with matched benign distributions, residual calibration error (ECE\,=\,0.126--0.141; Appendix~\ref{app:calibration}) suggests temperature scaling is needed for deployment.
42	
43	\paragraph{Frozen encoder assumption.}
44	The frozen Stage-1 design isolates representation quality but may underestimate full-pipeline performance. End-to-end fine-tuning closes this gap to $\leq$5.8\,pp on ActorAttack (F1\,=\,0.997$\pm$0.005 vs.\ 0.939$\pm$0.047 frozen; Table~\ref{tab:e2e}; Appendix~\ref{app:frozen_verify}).
45	
46	\paragraph{Dataset scale and cross-LLM transfer.}
47	Scale validation (1{,}000 conversations; Appendix~\ref{app:scale_validation}) confirms the hierarchy holds (DAPT advantage 40--56\,pp over vanilla). Cross-LLM validation shows jailbreak detection transfers when benign distribution is held constant (F1 recovers to 0.800--1.000), but benign-side F1 drops to 0.370--0.430 with unfamiliar benign text (Appendix~\ref{app:cross_llm}). The perturbation evaluation ($n$=76) remains underpowered.
48	
49	\paragraph{Strategy labels.}
50	Persuasion strategy labels ($n$=50 human validation, $\kappa$=0.78) are produced by Qwen3-8B; the validation sample yields small per-class sizes across 9 categories, limiting reliability estimates for individual strategies. OOD strategy accuracy degrades to 30.7\% ($\kappa$=0.126); interpretability is limited to known attack families. We plan to release annotation prompts and data for independent verification.
51	
52	\paragraph{Detection architecture.}
53	Binary vs.\ 9-class equivalence (F1 gap $\leq$3.9\,pp) suggests the binary head is not the critical differentiator. FITD provides minimal discriminative signal (all variants F1\,$\geq$\,0.990), serving as confirmation that simple attacks do not challenge any variant.
54	
55	\paragraph{Encoder scale.}
56	Whether findings hold at LLM-scale encoders (7B+) remains open; same-architecture scaling (e.g., DeBERTa-base vs.\ DeBERTa-large) is needed to attribute the capacity effect to scale alone.
57	
58	\paragraph{Scope and single-turn transfer.}
59	Only persuasion-mediated multi-turn attacks fall within scope; single-turn token-level attacks~\citep{zou2023gcg}, non-persuasive strategies, and non-text modalities are not addressed. ToxicChat performance reflects zero-shot single-turn transfer; doubling the training corpus drops ToxicChat macro F1 from 0.596 to 0.341$\pm$0.004 while multi-turn OOD remains stable, confirming the architecture targets multi-turn detection.
60	
61	\paragraph{Computation cost.}
62	Total pipeline cost for all seven variants is under 4 GPU-hours on a single A100.
63	
64	\section*{Ethics Statement}
65	
66	This work is defensive: it improves detection of multi-turn jailbreak attacks rather than developing new attacks. We acknowledge dual-use risk, as the persuasion taxonomy could inform adversarial actors. We mitigate this by using only synthetic conversations (no real harmful content), withholding attack-generation prompts, and focusing contributions on detection mechanisms. No human subjects were involved; all data will be released under CC BY-NC 4.0.
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11f2699e-6d79-4cdf-b19c-df902e072ea4",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "e9b6682a-d472-4bbf-9e79-23225e457e3f",
  "sourceToolAssistantUUID": "11f2699e-6d79-4cdf-b19c-df902e072ea4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T13:48:33.601Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RYk49CEBL7psAukWCbfu8G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9b6682a-d472-4bbf-9e79-23225e457e3f",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiH97gNN6LnrkfX2zvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f76e2aaf-7d3d-48ba-b05c-e4bedb998d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mgqQT1VGASxNUuU1vvbJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24770,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T13:48:33.614Z_

<details><summary>↩ Tool result · `toolu_01RYk49CEBL7psAukWCbfu8G`</summary>

```text
1	% experiments.tex — D024 compressed for 8-page limit
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations, extending \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy}: vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
14	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
15	No overlap exists in attack templates across families; benign is IID (same generation pipeline).
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
21	Our vanilla DeBERTa+BiGRU configuration is architecturally equivalent to DeepContext~\citep{deepcontext2026}, differing only in encoder choice (DeBERTa-v3-base vs.\ BERT); it serves as our primary baseline.
22	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
23	We also compare TF-IDF LR, LLM-as-judge (Appendix~\ref{sec:llm_judge}), and Llama Guard~3~8B~\citep{metallamaguard3_2024} (zero-shot; evaluates last-response safety given conversation context), which detects only 1.8\% of multi-turn jailbreaks (Table~\ref{tab:evidence_hierarchy}).
24	
25	\paragraph{Metrics.}
26	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
27	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants.
28	For key pairwise comparisons, we report BCa bootstrap 95\% confidence intervals (10,000 resamples over individual predictions pooled across 3 seeds; this assumes cross-seed independence and is exploratory) and paired permutation tests (10,000 permutations). Seed-level F1 values (Table~\ref{tab:seed_level}, Appendix~\ref{app:seed_level}) confirm all pairwise conclusions hold at every seed.
29	All standard deviations are computed over 3 random seeds using the population formula ($n$ divisor); Bessel-corrected estimates ($n{-}1$ divisor) are $\approx$22\% larger but do not alter any significance conclusions.
30	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
31	Stage-2: two-layer MLP, 20 epochs.
32	
33	%----------------------------------------------------------------------
34	\subsection{Cross-Attack Generalization}
35	
36	\begin{table}[t]
37	\centering
38	\small
39	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation length. IID: Crescendo; OOD: Deceptive Delight (DD). 3-seed mean$\pm$std where noted; full per-$K$ in Appendix~\ref{sec:full_prefix}.}
40	\label{tab:main_results}
41	\begin{tabular}{@{}lcc|cc@{}}
42	\toprule
43	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
44	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
45	\midrule
46	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.994$\pm$.005} \\
47	MLM-only$^{\ddagger}$ & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
48	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
49	TF-IDF LR$^{\S}$ & 1.000 & 1.000 & 1.000 & .961 \\
50	\bottomrule
51	\end{tabular}
52	\vspace{-2pt}
53	{\footnotesize $^{\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\S}$TF-IDF is deterministic (no std).}
54	\end{table}
55	
56	Vanilla encoders collapse under cross-attack transfer; domain-adapted variants recover near-perfect detection (Table~\ref{tab:main_results}, Figure~\ref{fig:cross_attack_bar}).
57	DD exhibits high lexical separability (TF-IDF F1\,=\,0.961); ActorAttack, where TF-IDF collapses to 0.261, serves as the primary stress test for beyond-lexical generalization.
58	On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628 at $K$=1 to 0.312 at Full), consistent with attack turns occupying ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
59	MLM achieves mean F1 $\geq$ 0.97 at all prefixes $K \leq 5$ without any classification labels; domain exposure alone is sufficient.
60	At full conversation length, MLM drops to 0.914$\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.994$\pm$0.005.
61	TF-IDF LR reaches F1 = 0.961 on full DD; DD is fully solvable by lexical features.
62	On structurally complex ActorAttack, TF-IDF collapses to F1 = 0.261 (precision = 1.0, recall = 0.15), while 9-class maintains 0.972$\pm$0.026: a 71\,pp gap. Lexical methods cannot capture multi-persona role-playing attack structure. This establishes a ``difficulty threshold'' for lexical methods parallel to that of vanilla encoders: both succeed on DD and fail on ActorAttack (Section~\ref{sec:limitations}).
63	Bootstrap CIs confirm non-overlapping intervals (9-class DD Full [0.943, 1.000] vs.\ vanilla [0.202, 0.341]; all permutation $p < 0.0001$). FITD is non-discriminative (all variants F1\,$\geq$\,0.990; Section~\ref{sec:limitations}).
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
68	\caption{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families. Vanilla DeBERTa collapses on OOD Deceptive Delight, confirming the necessity of domain-adaptive pretraining. FITD is non-discriminative for all methods (Section~\ref{sec:limitations}).}
69	\label{fig:cross_attack_bar}
70	\end{figure}
71	
72	Prefix-length analysis (Appendix Table~\ref{tab:full_prefix}) shows vanilla F1 drops from 0.628 at $K$=1 to 0.312 at full length. MLM achieves strong early detection ($K$=2: 0.993) but is unstable at full length (0.914$\pm$0.115); the 9-class model maintains 0.972--0.994 across all prefixes, demonstrating that classification supervision stabilizes against distributional drift.
73	
74	%----------------------------------------------------------------------
75	\subsection{Decomposing the Detection Mechanism}
76	\label{sec:decomposition}
77	
78	\begin{table}[t]
79	\centering
80	\small
81	\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\pm$std where available). Bold indicates best per column. All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\ref{tab:full_prefix} and~\ref{tab:actorattack_full}.}
82	\label{tab:evidence_hierarchy}
83	\begin{tabular}{@{}lccc@{}}
84	\toprule
85	\textbf{Variant} & DD-Full & AA-Full & DD-$K$=2 \\
86	\midrule
87	9-class (full model) & .994$\pm$.005 & .972$\pm$.026 & .981$\pm$.013 \\
88	Binary (2-class) & \textbf{1.000$\pm$.000} & \textbf{.990$\pm$.008} & .994$\pm$.009 \\
89	Scrambled labels & .994$\pm$.005 & .951$\pm$.043 & .981$\pm$.026 \\
90	MLM-only$^{\ddagger}$ (no labels) & .914$\pm$.115 & .893$\pm$.080 & .993$\pm$.009 \\
91	Mean pooling$^{*}$ & .991$\pm$.013 & .962$\pm$.015 & \textbf{1.000} \\
92	\midrule
93	Topic classif.\ (5-class) & .541$\pm$.207 & .625$\pm$.141 & .593$\pm$.166 \\
94	Wikipedia MLM & .904$\pm$.115 & .686$\pm$.297 & .911$\pm$.073 \\
95	Vanilla DeBERTa & .312$\pm$.026 & .258$\pm$.000 & .479$\pm$.038 \\
96	TF-IDF LR$^{\dagger}$ & .961 & .261 & \textbf{1.000} \\
97	Llama Guard~3$^{\P}$ & .025 & .000 & -- \\
98	\bottomrule
99	\end{tabular}
100	\vspace{-2pt}
101	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Deterministic (no std). $^{\ddagger}$MLM-only IID (Table~\ref{tab:main_results}) is single-seed (42); all OOD values are 3-seed. $^{\P}$Zero-shot; no domain training.}
102	\end{table}
103	
104	A clear \emph{evidence hierarchy} emerges across seven variants (Table~\ref{tab:evidence_hierarchy}), ordered by OOD detection at full conversation length on DD:
105	
106	\vspace{2pt}
107	\noindent\hspace{0.5em}{\small vanilla (0.312$\pm$0.026) $<$ topic (0.541$\pm$0.207) $\ll$ wiki-MLM (0.904$\pm$0.115) $\approx$ jb-MLM (0.914$\pm$0.115) $<$ scrambled (0.994$\pm$0.005) $=$ 9-class (0.994$\pm$0.005) $\approx$ binary (1.000$\pm$0.000)}
108	\vspace{2pt}
109	
110	\paragraph{Domain exposure is the primary mechanism.}
111	MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
112	All three classification-supervised variants converge to equivalent detection (F1 = 0.994--1.000); McNemar's ($p > 0.13$) and paired permutation tests ($p \geq 0.40$) provide descriptive evidence suggesting equivalence. TOST (margin = 5\,pp) confirms equivalence on DD ($p < 0.01$; Table~\ref{tab:tost_sensitivity}); on ActorAttack, TOST is underpowered (SE\,=\,0.045) despite a 2.1\,pp mean gap. Label quality and granularity are descriptively non-factors for detection.
113	Classification supervision is associated with 4--20$\times$ lower cross-seed variance over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; observed range across 3 seeds; formal variance ratio tests are not applicable at $n$=3; cross-seed ensemble yields marginal additional gains, Appendix~\ref{app:ensemble}). This stability benefit does not transfer to human-authored data, where classification-supervised variants exhibit the highest variance and pure MLM the lowest (Section~\ref{sec:human_data}).
114	Appendix~\ref{app:tsne} provides t-SNE visualizations confirming that domain-adapted variants produce tighter, more separable embedding clusters than the vanilla baseline.
115	
116	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
117	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap), though jailbreak-domain text provides an 8\,pp advantage at early prefixes ($K$=2: 0.993 vs.\ 0.911).
118	Perturbation analysis (Section~\ref{sec:perturbation}) reveals a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp.
119	
120	\paragraph{Misaligned supervision destabilizes generalization.}
121	Topic classification yields DD-Full F1 = 0.541$\pm$0.207; seed 123 falls \emph{below} vanilla (0.252 vs.\ 0.312). Despite using the same jailbreak-domain training data, topic classification performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels. A misaligned objective forces the encoder to allocate capacity to irrelevant features and actively destabilizes representations that MLM would preserve.
122	
123	\paragraph{Evidence hierarchy on structurally complex attacks.}
124	ActorAttack~\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures and provides a more challenging OOD benchmark than DD.
125	The evidence hierarchy at full conversation length is:
126	
127	\vspace{2pt}
128	\noindent\hspace{0.5em}{\small TF-IDF (0.261) $\approx$ vanilla (0.258$\pm$0.000) $<$ topic (0.625$\pm$0.141) $<$ wiki-MLM (0.686$\pm$0.297) $<$ jb-MLM (0.893$\pm$0.080) $<$ scrambled (0.951$\pm$0.043) $\approx$ 9-class (0.972$\pm$0.026) $\approx$ binary (0.990$\pm$0.008)}
129	\vspace{2pt}
130	
131	TF-IDF collapses from 0.961 (DD) to 0.261 (ActorAttack, precision = 1.0, recall = 0.15). This gap shows that domain-adapted representations capture features beyond bag-of-words.
132	All classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\,pp); this extends the DD finding. DAPT provides $\sim$71\,pp over both vanilla (0.258) and TF-IDF (0.261). Full per-prefix results and per-prefix error analysis in Appendix~\ref{sec:actorattack_full} and~\ref{app:aa_error}.
133	
134	\paragraph{Temporal modeling.}
135	Mean pooling matches BiGRU on both DD and ActorAttack (F1 gap $\leq$ 1\,pp, overlapping CIs; Appendix~\ref{app:temporal}).
136	Turn-order shuffling produces negligible change ($|\Delta| < 1$\,pp) across both DeBERTa-v3-base 9-class (DD $\Delta$\,=\,0.000, AA $\Delta$\,=\,$-$0.009, IID $\Delta$\,=\,0.000) and RoBERTa-large 9-class (DD $\Delta$\,=\,+0.001, AA $\Delta$\,=\,$-$0.007, IID $\Delta$\,=\,0.000), confirming that detection relies on per-turn representations rather than sequential patterns.
137	
138	\paragraph{Summary.}
139	For base-size encoders (125--184M), domain exposure is the primary mechanism; label correctness, granularity, temporal modeling, and domain specificity are non-factors. Classification supervision provides a complementary stability benefit (variance reduced 4--20$\times$) without changing the detection ceiling.
140	DD and FITD confirm no regression on easier attacks; ActorAttack provides the discriminative evaluation where lexical methods fail.
141	Detection is stable across conversation lengths (Appendix~\ref{app:length}), near-saturates at 50 conversations (Appendix~\ref{app:data_efficiency}), and is insensitive to auxiliary loss weight (Appendix~\ref{app:lambda}).
142	
143	%----------------------------------------------------------------------
144	\subsection{Cross-Encoder Validation}
145	\label{sec:cross_encoder}
146	
147	\begin{table}[t]
148	\centering
149	\small
150	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. Bold indicates best per encoder group.}
151	\label{tab:cross_encoder}
152	\begin{tabular}{@{}lcc@{}}
153	\toprule
154	\textbf{Variant} & DD & AA \\
155	\midrule
156	\multicolumn{3}{l}{\textit{DeBERTa-v3-base (184M)}} \\[2pt]
157	Vanilla & .312$\pm$.026 & .258$\pm$.000 \\
158	MLM & .914$\pm$.115 & .893$\pm$.080 \\
159	9-class & \textbf{.994$\pm$.005} & \textbf{.972$\pm$.026} \\
160	\midrule
161	\multicolumn{3}{l}{\textit{RoBERTa-base (125M)}} \\[2pt]
162	Vanilla & .981$\pm$.026 & .466$\pm$.163 \\
163	MLM & .987$\pm$.018 & .730$\pm$.201 \\
164	9-class & \textbf{.994$\pm$.005} & \textbf{.939$\pm$.046} \\
165	\midrule
166	\multicolumn{3}{l}{\textit{RoBERTa-large (355M)}} \\[2pt]
167	Vanilla & .927$\pm$.036 & \textbf{1.000$\pm$.000} \\
168	MLM & .884$\pm$.065 & .874$\pm$.014 \\
169	9-class & \textbf{.987$\pm$.004} & .946$\pm$.057 \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	To test whether the evidence hierarchy depends on encoder choice, we replicate vanilla, MLM, and 9-class on RoBERTa-base~\citep{liu2019roberta} (Table~\ref{tab:cross_encoder}).
175	On DD, RoBERTa-base vanilla already achieves 0.981$\pm$0.026 (vs.\ DeBERTa 0.312$\pm$0.026), so DAPT adds only 1.3\,pp. ActorAttack exposes this as DD's simplicity: RoBERTa-base vanilla collapses to 0.466$\pm$0.163, a 51.5\,pp drop, while domain-adapted variants recover (9-class: 0.939$\pm$0.046).
176	
177	RoBERTa-large (355M) reveals a capacity-DAPT interaction: its effect on ActorAttack reverses (vanilla 1.000 vs.\ 9-class 0.946), while smaller encoders require DAPT to bridge 47--71\,pp. All continued pretraining reduces ActorAttack performance for the largest encoder via representation drift (Table~\ref{tab:roberta_large_lr}), though classification DAPT partially compensates on DD (+6\,pp).
178	
179	Three encoder scales thus reveal a scale-dependent pattern for the \emph{difficulty threshold}: DeBERTa-v3-base requires adaptation for all attacks, RoBERTa-base only for complex ones, and RoBERTa-large for none (Section~\ref{sec:discussion}).
180	Classification supervision provides a consistent stability benefit across both base encoders (cross-seed variance: 0.005--0.046 vs.\ 0.026--0.201).
181	A BERT-base-uncased proxy (110M, matching DeepContext's encoder family) without adaptation achieves DD\,=\,0.318$\pm$0.031 and AA\,=\,0.275$\pm$0.027, comparable to vanilla DeBERTa-v3 (Appendix~\ref{app:bert_proxy}), confirming that cross-attack generalization is driven by DAPT rather than encoder architecture.
182	
183	CKA analysis~\citep{kornblith2019cka} and linear probing confirm that DAPT reshapes representations substantially (Figure~\ref{fig:cka_heatmap}), though comparable CKA shifts yield different detection gains across starting points (Appendix~\ref{sec:cka_heatmap}).
184	
185	%----------------------------------------------------------------------
186	\subsection{Mixed-LLM Training}
187	
188	All preceding experiments use single-source (Qwen3-8B) data. To test whether the evidence hierarchy transfers when training data mixes LLM sources, we train on 250 Qwen + 250 Llama-3.1-8B conversations (Table~\ref{tab:mixed_llm}).
189	Classification-based DAPT is the only variant that substantially outperforms vanilla: 9-class achieves DD OOD F1\,=\,0.818$\pm$0.096 (+53\,pp over vanilla 0.291$\pm$0.065), while MLM drops to vanilla level (0.289$\pm$0.101). On structurally complex ActorAttack, the advantage narrows (9-class 0.504$\pm$0.107 vs.\ vanilla 0.389$\pm$0.073, +11.5\,pp) with high seed variance, suggesting that limited per-source volume (250 per LLM) constrains generalization to complex attacks. DD and FITD thus primarily validate the baseline rather than the method; ActorAttack, where lexical methods collapse (TF-IDF F1\,=\,0.261) and vanilla encoders fail (F1\,$\leq$\,0.389 across conditions), provides the discriminative evaluation axis.
190	Mixed-LLM training confirms that classification supervision generalizes across LLM sources where unsupervised pretraining does not; full results in Appendix~\ref{app:mixed_llm}.
191	
192	%----------------------------------------------------------------------
193	\subsection{Human Data Validation}
194	\label{sec:human_data}
195	
196	Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
197	
198	\begin{table}[t]
199	\centering
200	\small
201	\caption{Human data validation on ToxicChat~\citep{lin2023toxicchat} (macro F1, 3-seed mean$\pm$std). Bold indicates best. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}
202	\label{tab:human_data}
203	\begin{tabular}{@{}lc@{}}
204	\toprule
205	\textbf{Variant} & Macro F1 \\
206	\midrule
207	JB-MLM & \textbf{.837$\pm$.013} \\
208	Wiki-MLM & .791$\pm$.093 \\
209	Binary & .705$\pm$.072 \\
210	Scrambled & .616$\pm$.056 \\
211	9-class & .596$\pm$.087 \\
212	Topic & .496$\pm$.042 \\
213	\midrule
214	Vanilla & .413$\pm$.021 \\
215	\bottomrule
216	\end{tabular}
217	\end{table}
218	
219	All DAPT variants exceed vanilla by 18--42\,pp (Table~\ref{tab:human_data}), confirming that the adapted-vs.-vanilla gap is not a Qwen3-8B generation artifact: domain exposure on synthetic jailbreak text transfers to human-written attacks.
220	
221	The ordering reverses: JB-MLM leads (0.837$\pm$0.013) while 9-class ranks lower (0.596$\pm$0.087; $p < 0.001$, non-overlapping CIs). ToxicChat is single-turn, so the classification head provides no advantage; validating the multi-turn hierarchy requires multi-turn human data.
222	
223	%----------------------------------------------------------------------
224	\subsection{Perturbation Analysis}
225	\label{sec:perturbation}
226	
227	Under adversarial paraphrasing (BERTScore 0.92), classification-supervised variants achieve zero degradation on IID and OOD DD (Table~\ref{tab:ood_perturbation}) while non-adapted models degrade by $\sim$12\,pp ($p < 0.001$); on ActorAttack, DAPT variants degrade ($\Delta$\,=\,$-$20.4\,pp) but maintain 52\,pp over vanilla (Appendix~\ref{sec:perturbation_full}).
228	
229	%----------------------------------------------------------------------
230	\subsection{Strategy Trajectory Analysis}
231	\label{sec:strategy}
232	
233	The 9-class taxonomy provides interpretable characterization of known attacks ($\kappa$=0.78, $n$=50; Appendix~\ref{sec:strategy_full}) but degrades to near-random on OOD ($\kappa$=0.126; Appendix~\ref{app:strategy_pred}). Its value is twofold: as ablation infrastructure (scrambled labels produce equivalent detection, confirming label content is non-critical) and as an interpretability tool for characterizing known attacks; detection operates through domain-adapted \texttt{[CLS]} embeddings, not strategy accuracy.
234	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f76e2aaf-7d3d-48ba-b05c-e4bedb998d35",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "179e2eaa-31da-4f84-accc-4147434f87aa",
  "sourceToolAssistantUUID": "f76e2aaf-7d3d-48ba-b05c-e4bedb998d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T13:48:34.116Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JRckPAB48n2v6XcSBPckXv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "179e2eaa-31da-4f84-accc-4147434f87aa",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiH97gNN6LnrkfX2zvm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4da16eb7-2831-46f9-8dea-d68b33f85820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mgqQT1VGASxNUuU1vvbJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24770,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24770,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T13:48:34.510Z_

<details><summary>↩ Tool result · `toolu_01JRckPAB48n2v6XcSBPckXv`</summary>

```text
1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.994} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}
44	\label{tab:full_prefix}
45	\begin{tabular}{@{}lccccc@{}}
46	\toprule
47	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
48	\midrule
49	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
50	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
51	MLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\
52	Vanilla DeBERTa & .968$\pm$.033 & .978$\pm$.016 & .987$\pm$.000 & .982$\pm$.014 & 1.000$\pm$.000 \\
53	TF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\
54	\midrule
55	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
56	9-class (ours) & .990$\pm$.013 & .981$\pm$.013 & .972$\pm$.026 & .997$\pm$.005 & .994$\pm$.005 \\
57	Binary & .994$\pm$.009 & .994$\pm$.009 & .984$\pm$.008 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
58	Scrambled & .997$\pm$.005 & .981$\pm$.026 & .975$\pm$.029 & .997$\pm$.005 & .994$\pm$.005 \\
59	MLM-only & .973$\pm$.019 & .993$\pm$.009 & .997$\pm$.005 & .997$\pm$.005 & .914$\pm$.115 \\
60	Vanilla DeBERTa & .628$\pm$.038 & .479$\pm$.038 & .389$\pm$.027 & .351$\pm$.030 & .312$\pm$.026 \\
61	TF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\
62	\midrule
63	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
64	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & -- & -- & 1.000$\pm$.000 \\
65	Vanilla DeBERTa & .954$\pm$.039 & .952$\pm$.061 & -- & -- & .994$\pm$.009 \\
66	TF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\
67	\bottomrule
68	\end{tabular}
69	\end{table*}
70	
71	\section{ActorAttack Full Results}
72	\label{sec:actorattack_full}
73	
74	\begin{table*}[t]
75	\centering
76	\small
77	\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}
78	\label{tab:actorattack_full}
79	\begin{tabular}{@{}lccccc@{}}
80	\toprule
81	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
82	\midrule
83	\multicolumn{6}{l}{\textit{DeBERTa-v3}} \\[2pt]
84	Binary & .788$\pm$.020 & \textbf{.935$\pm$.018} & \textbf{.976$\pm$.005} & \textbf{.995$\pm$.005} & \textbf{.990$\pm$.008} \\
85	9-class & .773$\pm$.041 & .855$\pm$.048 & .921$\pm$.046 & .966$\pm$.028 & .972$\pm$.026 \\
86	Scrambled & .652$\pm$.034 & .804$\pm$.053 & .854$\pm$.046 & .910$\pm$.052 & .951$\pm$.043 \\
87	MLM-only & .736$\pm$.150 & .909$\pm$.058 & .945$\pm$.039 & .929$\pm$.033 & .893$\pm$.080 \\
88	Wiki MLM & .656$\pm$.224 & .672$\pm$.252 & .693$\pm$.280 & .689$\pm$.285 & .686$\pm$.297 \\
89	Topic & .513$\pm$.077 & .580$\pm$.109 & .565$\pm$.100 & .615$\pm$.111 & .625$\pm$.141 \\
90	Vanilla & .337$\pm$.049 & .306$\pm$.026 & .284$\pm$.011 & .262$\pm$.006 & .258$\pm$.000 \\
91	TF-IDF LR & .633 & .730 & .571 & .242 & .261 \\
92	\midrule
93	\multicolumn{6}{l}{\textit{RoBERTa}} \\[2pt]
94	9-class & \textbf{.738$\pm$.033} & .805$\pm$.033 & .884$\pm$.066 & .925$\pm$.066 & .939$\pm$.046 \\
95	MLM & .633$\pm$.133 & .665$\pm$.150 & .713$\pm$.174 & .719$\pm$.184 & .730$\pm$.201 \\
96	Vanilla & .410$\pm$.126 & .425$\pm$.143 & .432$\pm$.144 & .466$\pm$.144 & .466$\pm$.163 \\
97	\bottomrule
98	\end{tabular}
99	\end{table*}
100	
101	Table~\ref{tab:actorattack_full} reveals three distinct prefix-length patterns. The 9-class model improves monotonically from $K$=1 to Full (+20\,pp), consistent with cumulative evidence accumulation across turns. Vanilla DeBERTa \emph{decreases} with more turns (0.337 at $K$=1 to 0.258 at Full), suggesting that additional attack turns push representations further into benign embedding regions. MLM peaks at $K$=3 (0.945) then declines to 0.893 at Full, indicating that unsupervised domain exposure captures early-turn patterns but is unstable under extended sequences.
102	
103	\subsection{Error Analysis}
104	\label{app:aa_error}
105	
106	Per-sample majority vote across 3 seeds yields 98.3\% accuracy on ActorAttack OOD (2 false negatives, 0 false positives). No sample is misclassified by all three seeds; all 7 seed-specific errors are false negatives concentrated in shorter conversations (3--6 turns). On these 7 error samples, vanilla achieves 0/3 correct votes per sample, while 9-class majority vote correctly classifies 5/7, confirming that domain adaptation provides robust per-sample coverage even where individual seeds fail.
107	
108	\section{Perturbation Robustness}
109	\label{sec:perturbation_full}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\Delta$: F1 degradation (pp). Classification-supervised variants achieve zero degradation at full length; this pattern does not generalize to ActorAttack.}
115	\label{tab:perturbation}
116	\begin{tabular}{@{}lcccc@{}}
117	\toprule
118	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
119	\midrule
120	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
121	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
122	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
123	\midrule
124	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
125	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
126	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
127	\midrule
128	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
129	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	Table~\ref{tab:perturbation} shows perturbation behavior on IID data.
135	Classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.
136	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp.
137	McNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\leq$7 discordant pairs, statistical power is limited.
138	
139	\begin{table}[t]
140	\centering
141	\small
142	\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm$std where available.}
143	\label{tab:ood_perturbation}
144	\begin{tabular}{@{}lcccc@{}}
145	\toprule
146	\textbf{Variant} & Clean Full & Pert.\ Full & $\Delta$ Full & $\Delta$ $K$=1 \\
147	\midrule
148	9-class & .994$\pm$.005 & 1.000$\pm$.000 & +0.6 & +0.6 \\
149	Binary & 1.000$\pm$.000 & 1.000$\pm$.000 & 0.0 & +0.6 \\
150	Scrambled & .994$\pm$.005 & 1.000$\pm$.000 & +0.6 & $-$0.3 \\
151	\midrule
152	JB MLM & .914$\pm$.115 & .941 & +2.7 & 0.0 \\
153	Wiki MLM$^{*}$ & .904$\pm$.115 & .872 & $-$3.3 & $-$3.2 \\
154	Vanilla$^{\dagger}$ & .312$\pm$.026 & .339$\pm$.055 & +2.7 & $-$6.8$\pm$1.1 \\
155	\bottomrule
156	\end{tabular}
157	\vspace{-2pt}
158	{\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\,pp; other seeds show 0.0\,pp change.\\$^{\dagger}$Vanilla $\Delta$ Full = +2.7\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}
159	\end{table}
160	
161	On OOD DD, the IID pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\ vanilla significance ($p < 0.001$, 49--78 discordant pairs).
162	On OOD ActorAttack, domain-adapted variants degrade substantially (9-class $\Delta$\,=\,$-$20.4$\pm$13.5\,pp, MLM $-$35.3\,pp), but perturbation narrows rather than closes the adapted vs.\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$).
163	Domain specificity also manifests: Wikipedia MLM degrades by $\sim$12\,pp while jailbreak-domain MLM degrades by only 2.6\,pp.
164	
165	\section{Strategy Trajectory Analysis}
166	\label{sec:strategy_full}
167	
168	\begin{figure*}[t]
169	\centering
170	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
171	\caption{Persuasion strategy transition count matrices for three attack families, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
172	\label{fig:strategy_heatmap}
173	\end{figure*}
174	
175	Figure~\ref{fig:strategy_heatmap} shows transition count matrices for three attack families.
176	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545); this reflects its gradual escalation design.
177	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition, consistent with FITD's commitment-consistency exploitation~\citep{cialdini2001influence}.
178	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition, aligning with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}.
179	
180	\section{Centered CKA Heatmaps}
181	\label{sec:cka_heatmap}
182	
183	\begin{figure}[t]
184	\centering
185	\includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}
186	\caption{Centered CKA similarity~\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\ 9-class block shows distinct geometries (CKA $\leq$ 0.2 on RoBERTa OOD).}
187	\label{fig:cka_heatmap}
188	\end{figure}
189	
190	\section{Embedding Space Visualization}
191	\label{app:tsne}
192	
193	Figure~\ref{fig:tsne} visualizes mean-pooled \texttt{[CLS]} embeddings via t-SNE for three representative variants (Vanilla, JB-MLM, 9-Class) on DD OOD and ActorAttack. Vanilla embeddings show dispersed jailbreak clusters with ambiguous decision boundaries, while domain-adapted variants (JB-MLM, 9-Class) produce tighter, more separable clusters. JB-MLM achieves the clearest bimodal separation on both evaluation sets, consistent with its superior detection performance.
194	
195	\begin{figure}[ht]
196	\centering
197	\includegraphics[width=\columnwidth]{figures/paper/embedding_tsne.pdf}
198	\caption{t-SNE visualization of mean-pooled \texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}
199	\label{fig:tsne}
200	\end{figure}
201	
202	\section{Cross-LLM Validation}
203	\label{app:cross_llm}
204	
205	\begin{table}[ht]
206	\centering
207	\footnotesize
208	\caption{Cross-LLM validation (F1, full conversation). All models are trained on Qwen3-8B data; conditions vary the source of jailbreak (JB) and benign (ben.) conversations at inference. Values are evaluated under a matched 50-sample subset protocol and differ from Table~\ref{tab:evidence_hierarchy}, which uses the full evaluation set.}
209	\label{tab:cross_llm}
210	\begin{tabular}{@{}lcccccc@{}}
211	\toprule
212	& \multicolumn{3}{c}{\textit{DD Full}} & \multicolumn{3}{c}{\textit{AA Full}} \\
213	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
214	\textbf{Condition} & Van. & MLM & 9-cl. & Van. & MLM & 9-cl. \\
215	\midrule
216	Qwen JB + Qwen ben. & .312 & .914 & .997 & .258 & .893 & .972 \\
217	Llama JB + Llama ben. & .261 & .282 & .433 & .261 & .368 & .321 \\
218	Llama JB + Qwen ben. & .302 & .778$^{*}$ & 1.000 & .302 & .903 & .801 \\
219	\bottomrule
220	\end{tabular}
221	\vspace{-2pt}
222	{\footnotesize $^{*}$High seed variance (std = 0.306): seed 456 outlier (F1 = 0.345); remaining two seeds achieve F1 $\geq$ 0.97.}
223	\end{table}
224	
225	Table~\ref{tab:cross_llm} shows three inference conditions. When both jailbreak and benign text come from Llama (row~2), all variants collapse (F1 = 0.26--0.43), but this conflates two sources of distribution shift: unfamiliar jailbreak patterns and unfamiliar benign text. Row~3 isolates jailbreak transferability by pairing Llama jailbreaks with the original Qwen benign distribution. Under this condition, 9-class recovers to F1 = 1.000 on DD and 0.801 on ActorAttack, and JB-MLM reaches 0.903 on ActorAttack. The contrast between rows~2 and~3 shows that the dominant failure mode in row~2 is benign distribution mismatch (false positives from unfamiliar benign text), not inability to recognize cross-LLM jailbreak patterns. Vanilla remains at 0.26--0.31 across all conditions, further confirming that encoders without DAPT lack OOD detection capability regardless of the LLM source. The residual degradation on ActorAttack (0.801 vs.\ 0.972) reflects genuine cross-LLM variation in structurally complex attack patterns.
226	
227	\begin{table}[ht]
228	\centering
229	\footnotesize
230	\caption{Error decomposition for DD Full cross-LLM conditions (matched 50-sample subsets). TP rate is identical across benign conditions; the F1 collapse in the Llama-only condition (Table~\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text.}
231	\label{tab:cross_llm_error}
232	\begin{tabular}{@{}lccc@{}}
233	\toprule
234	\textbf{Metric} & Van. & MLM & 9-cl. \\
235	\midrule
236	TP rate (Llama JB) & 0.0\% & 68.0\% & 100.0\% \\
237	FP rate (Llama ben.) & 29.3\% & 88.0\% & 90.0\% \\
238	FP rate (Qwen ben.) & 0.0\% & 0.9\% & 0.0\% \\
239	\bottomrule
240	\end{tabular}
241	\end{table}
242	
243	Table~\ref{tab:cross_llm_error} decomposes DD Full F1 into true positive and false positive rates. TP rates are identical regardless of the benign source: domain-adapted models detect Llama-generated jailbreaks at the same rate whether evaluated against Qwen or Llama benign text. The F1 collapse in the full Llama condition (Table~\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text (FP rate: 88--90\% on Llama vs.\ 0--0.9\% on Qwen for adapted variants). The model implicitly treats non-Qwen text style as a jailbreak indicator, a spurious correlation from single-LLM training data. This failure reflects a data diversity limitation, not a methodological one; mixed-LLM training (Table~\ref{tab:mixed_llm}) partially addresses this confound.
244	
245	\section{Mixed-LLM Training Results}
246	\label{app:mixed_llm}
247	
248	\begin{table}[ht]
249	\centering
250	\footnotesize
251	\caption{Mixed-LLM training (250 Qwen + 250 Llama conversations, 3-seed mean$\pm$std where available). ToxicChat evaluated on balanced set (408 conversations).}
252	\label{tab:mixed_llm}
253	\begin{tabular}{@{}lccccc@{}}
254	\toprule
255	\textbf{Variant} & Mixed & DD OOD & AA OOD & FITD OOD & ToxicChat \\
256	\midrule
257	9-class & \textbf{.996$\pm$.006} & \textbf{.818$\pm$.096} & \textbf{.504$\pm$.107} & \textbf{.997$\pm$.005} & \textbf{.550$\pm$.052} \\
258	MLM & .681$\pm$.226 & .289$\pm$.101 & .258$\pm$.075 & .679$\pm$.188 & .256$\pm$.053 \\
259	Vanilla & .802$\pm$.010 & .291$\pm$.065 & .389$\pm$.073 & .867$\pm$.022 & .356$\pm$.009 \\
260	\bottomrule
261	\end{tabular}
262	\end{table}
263	
264	Table~\ref{tab:mixed_llm} reports detection performance when training on a mixed corpus of Qwen3-8B and Llama-3.1-8B conversations. Classification-based DAPT (9-class) maintains the strongest DD OOD performance (0.818$\pm$0.096), outperforming both vanilla (0.291$\pm$0.065) and MLM (0.289$\pm$0.101) by 53\,pp. ActorAttack remains challenging under mixed-LLM conditions (9-class F1\,=\,0.504$\pm$0.107), suggesting structurally complex attacks require larger or more diverse training data. ToxicChat performance shows no significant improvement over single-source training (0.550$\pm$0.052 vs.\ 0.596$\pm$0.087; Section~\ref{sec:human_data}), consistent with ToxicChat being zero-shot single-turn transfer rather than a standard OOD benchmark.
265	
266	\section{Dataset Scale Validation}
267	\label{app:scale_validation}
268	
269	\begin{table}[ht]
270	\centering
271	\footnotesize
272	\caption{Dataset scale validation (1{,}000 Qwen conversations, 3-seed mean$\pm$std). IID results omitted due to train/test overlap (71\% of original test set present in expanded training data).}
273	\label{tab:scale_validation}
274	\begin{tabular}{@{}lcc@{}}
275	\toprule
276	\textbf{Variant} & DD OOD & AA OOD \\
277	\midrule
278	9-class & \textbf{.889$\pm$.041} & \textbf{.913$\pm$.041} \\
279	MLM & .338$\pm$.010 & .351$\pm$.018 \\
280	Vanilla & .326$\pm$.000 & .508$\pm$.085 \\
281	\bottomrule
282	\end{tabular}
283	\end{table}
284	
285	Table~\ref{tab:scale_validation} validates robustness to dataset scale by doubling the training corpus from 500 to 1{,}000 conversations with new topic seeds. The hierarchy 9-class $\gg$ MLM $\approx$ vanilla holds at 2$\times$ scale: classification-based DAPT maintains 40--56\,pp advantage over vanilla, while MLM provides no improvement over vanilla on either attack family (DD: 0.338 vs.\ 0.326; AA: 0.351 vs.\ 0.508).
286	
287	\section{RoBERTa-large DAPT Learning Rate Control}
288	
289	\begin{table}[ht]
290	\centering
291	\footnotesize
292	\caption{RoBERTa-large (355M) DAPT learning rate control on OOD Full (3-seed mean$\pm$std). Reducing the learning rate worsens both DD and AA, ruling out over-adaptation as the cause of the regression in Table~\ref{tab:cross_encoder}.}
293	\label{tab:roberta_large_lr}
294	\begin{tabular}{@{}lcc@{}}
295	\toprule
296	\textbf{Config} & DD Full & AA Full \\
297	\midrule
298	Vanilla (no DAPT) & .927$\pm$.036 & 1.000$\pm$.000 \\
299	9-class, LR=$2 \times 10^{-5}$ & .987$\pm$.004 & .946$\pm$.057 \\
300	9-class, LR=$1 \times 10^{-5}$ & .948$\pm$.034 & .781$\pm$.054 \\
301	\bottomrule
302	\end{tabular}
303	\end{table}
304	
305	Reducing the DAPT learning rate from $2 \times 10^{-5}$ to $1 \times 10^{-5}$ worsens both DD and AA performance, which rules out over-adaptation as the cause of the regression observed in Table~\ref{tab:cross_encoder}. An MLM-only variant (without classification) produces the same pattern (AA Full = 0.874$\pm$0.014); representation drift from continued pretraining, not classification-specific bias, is the underlying cause. Domain-adaptive fine-tuning narrows the representation space of a sufficiently large encoder and reduces its inherent OOD generalization ability.
306	
307	\section{TOST Equivalence Sensitivity Analysis}
308	
309	\begin{table}[ht]
310	\centering
311	\footnotesize
312	\caption{TOST equivalence test sensitivity to margin $\delta$ (scrambled vs.\ 9-class, 3-seed). $p$-values from two one-sided $t$-tests; $p < 0.05$ confirms equivalence within $\pm\delta$.}
313	\label{tab:tost_sensitivity}
314	\begin{tabular}{@{}lccc@{}}
315	\toprule
316	\textbf{Dataset} & $\delta$=5\,pp & $\delta$=3\,pp & $\delta$=2\,pp \\
317	\midrule
318	DD OOD & .006 \checkmark & .016 \checkmark & .035 \checkmark \\
319	ActorAttack & .290 & .428 & .507 \\
320	\bottomrule
321	\end{tabular}
322	\end{table}
323	
324	On DD, TOST confirms scrambled $\approx$ correct labels even at $\delta$=2\,pp ($p$=0.035), demonstrating that label correctness is not a detection factor; the DD equivalence conclusion is robust to margin choice. On ActorAttack, the mean gap is 2.1\,pp but TOST is underpowered (SE\,=\,0.045, $n$=3) to confirm formal equivalence at any tested margin; the variants are descriptively similar but formally inconclusive.
325	
326	\section{Reproducibility Details}
327	\label{sec:reproducibility}
328	
329	\paragraph{Stage-1 training.}
330	All variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \times 10^{-5}$, AdamW optimizer ($\beta_1$=0.9, $\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\% of steps, batch size 16, and 4 epochs. MLM variants use 15\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).
331	
332	\paragraph{Stage-2 training.}
333	The BiGRU has hidden dimension 256, 2 layers, and dropout 0.3 (bidirectional, so output dimension 512). The MLP classifier has layers $512 \to 256 \to 2$ with ReLU activation. Training uses learning rate $1 \times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.
334	
335	\paragraph{Data generation.}
336	Jailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.
337	
338	\paragraph{Strategy annotation.}
339	Each user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.
340	
341	\paragraph{Adversarial paraphrasing.}
342	The paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.
343	
344	\paragraph{Cross-checkpoint variance.}
345	To disentangle Stage-1 from Stage-2 variance, we evaluate three independently trained 9-class DAPT checkpoints (seeds 42, 123, 456) with a fixed downstream BiGRU seed (42). Results: IID F1\,=\,1.000$\pm$0.000, DD OOD\,=\,0.926$\pm$0.026, AA OOD\,=\,0.935$\pm$0.013. Stage-1 training is stable (OOD std\,$\leq$\,2.6\,pp), confirming that the variance reported in the main paper is not dominated by Stage-1 initialization.
346	
347	\section{End-to-End Fine-Tuning Upper Bound}
348	\label{app:e2e}
349	
350	\begin{table}[ht]
351	\centering
352	\footnotesize
353	\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\pm$std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\ref{tab:main_results}--\ref{tab:evidence_hierarchy}); Table~\ref{tab:frozen_verify} uses plan\_002 checkpoints, yielding higher frozen accuracy (DD\,=\,.997, AA\,=\,.972) and a narrower E2E gap ($\leq$2.5\,pp).}
354	\label{tab:e2e}
355	\begin{tabular}{@{}lccc@{}}
356	\toprule
357	\textbf{Config} & IID & DD OOD & AA OOD \\
358	\midrule
359	Frozen probing & 1.000$\pm$.000 & .994$\pm$.005 & .939$\pm$.047 \\
360	E2E fine-tuning & 1.000$\pm$.000 & 1.000$\pm$.000 & \textbf{.997$\pm$.005} \\
361	\midrule
362	$\Delta$ & .000 & +.006 & +.058 \\
363	\bottomrule
364	\end{tabular}
365	\end{table}
366	
367	End-to-end fine-tuning unfreezes the Stage-1 encoder during Stage-2 BiGRU training, allowing gradient flow through the full pipeline. On IID and OOD DD, the two configurations are indistinguishable; on structurally complex ActorAttack, E2E recovers +5.8\,pp. The modest gain confirms that frozen probing captures the vast majority of discriminative information encoded by Stage-1 DAPT, and that the remaining OOD gap in the frozen setting reflects downstream optimization constraints rather than missing representational capacity.
368	
369	\section{Real-World False Positive Rate}
370	\label{app:wildchat_fpr}
371	
372	\begin{table}[ht]
373	\centering
374	\footnotesize
375	\caption{False positive rate (\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\pm$std.}
376	\label{tab:wildchat_fpr}
377	\begin{tabular}{@{}lcccc@{}}
378	\toprule
379	\textbf{Variant} & Seed 42 & Seed 123 & Seed 456 & Mean$\pm$Std \\
380	\midrule
381	9-class & 66.8 & 61.1 & 76.5 & 68.1$\pm$6.4 \\
382	MLM & 36.7 & 64.6 & 32.3 & 44.5$\pm$14.3 \\
383	Vanilla & 47.3 & 42.5 & 54.4 & 48.1$\pm$4.9 \\
384	\bottomrule
385	\end{tabular}
386	\end{table}
387	
388	Table~\ref{tab:wildchat_fpr} evaluates false positive rates on 226 WildChat benign multi-turn conversations from real GPT-3.5 users (avg 7.4 turns). All variants produce FPR far exceeding deployable thresholds: 9-class is worst at 68.1\%, followed by vanilla (48.1\%) and MLM (44.5\%). Domain adaptation \emph{increases} FPR relative to vanilla (+20\,pp for 9-class), indicating that continued pretraining amplifies dependence on the training benign distribution. This is consistent with the cross-LLM false positive spike (Table~\ref{tab:cross_llm_error}): models trained on synthetic Qwen3-8B benign text implicitly treat unfamiliar conversational styles as jailbreak indicators. High MLM seed variance (std\,=\,14.3\%) suggests that unsupervised pretraining is particularly unstable under benign distribution shift. Deployment requires per-domain benign calibration or mixed-source benign training data.
389	
390	\paragraph{Post-hoc calibration.}
391	ROC AUC\,=\,0.700$\pm$0.054 indicates insufficient discrimination between WildChat benign and jailbreak conversations at the representation level. At TPR$\geq$95\%, the optimal threshold still yields FPR\,=\,62.7\%---far above deployable levels. Temperature scaling cannot improve this trade-off, as ROC curves are invariant to monotonic score transforms. The AUC ceiling reflects genuine domain shift: WildChat benign and jailbreak representations overlap substantially, and no post-hoc calibration can overcome this; in-domain benign adaptation is required.
392	
393	\section{BERT-base Proxy Baseline}
394	\label{app:bert_proxy}
395	
396	\begin{table}[ht]
397	\centering
398	\footnotesize
399	\caption{BERT-base-uncased (110M) frozen probing without DAPT, matching DeepContext's encoder family~\citep{deepcontext2026}. 3-seed mean$\pm$std. DeBERTa-v3 results from Table~\ref{tab:cross_encoder} for comparison.}
400	\label{tab:bert_proxy}
401	\begin{tabular}{@{}lccc@{}}
402	\toprule
403	\textbf{Encoder} & IID & DD OOD & AA OOD \\
404	\midrule
405	BERT-base (110M), no DAPT & .996$\pm$.006 & .318$\pm$.031 & .275$\pm$.027 \\
406	DeBERTa-v3 (184M), no DAPT & 1.000$\pm$.000 & .312$\pm$.043 & .258$\pm$.000 \\
407	DeBERTa-v3 (184M), 9-class & 1.000$\pm$.000 & .994$\pm$.005 & .939$\pm$.047 \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	Table~\ref{tab:bert_proxy} compares BERT-base-uncased (110M parameters, matching DeepContext's encoder) against DeBERTa-v3-base (184M), both without domain-adaptive pretraining. The two vanilla encoders achieve comparable OOD performance (DD: 0.318 vs.\ 0.312; AA: 0.275 vs.\ 0.258), despite a 1.7$\times$ parameter difference and different pretraining procedures. Both collapse on OOD evaluation while 9-class DAPT recovers to 0.994 (DD) and 0.939 (AA). This confirms that cross-attack generalization is driven by domain adaptation, not encoder architecture or capacity at this scale.
413	
414	\section{Confidence Calibration}
415	\label{app:calibration}
416	
417	\begin{table}[ht]
418	\centering
419	\footnotesize
420	\caption{Expected calibration error (ECE, 10 bins) for 9-class and vanilla on IID and OOD evaluation (3-seed mean$\pm$std). Lower is better.}
421	\label{tab:calibration}
422	\begin{tabular}{@{}lccc@{}}
423	\toprule
424	\textbf{Variant} & IID & DD OOD & AA OOD \\
425	\midrule
426	9-class & $\approx$0.000 & 0.143$\pm$0.053 & 0.116$\pm$0.053 \\
427	Vanilla & 0.009$\pm$0.007 & 0.669$\pm$0.004 & 0.504$\pm$0.066 \\
428	\bottomrule
429	\end{tabular}
430	\end{table}
431	
432	The 9-class model achieves substantially lower ECE than vanilla on OOD data (0.12--0.14 vs.\ 0.50--0.67), indicating that domain adaptation improves not only discriminative performance but also confidence calibration. IID calibration is near-perfect for both variants. The residual OOD ECE (0.12--0.14) suggests that temperature scaling could further improve deployment reliability.
433	
434	\section{Frozen Probing Verification}
435	\label{app:frozen_verify}
436	
437	\begin{table}[ht]
438	\centering
439	\footnotesize
440	\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning (3-seed mean$\pm$std). 9-class: plan\_002 checkpoints; MLM: plan\_017\_mlm\_control (matched training). Frozen probing trains only BiGRU+MLP on frozen DAPT embeddings.}
441	\label{tab:frozen_verify}
442	\begin{tabular}{@{}lcccc@{}}
443	\toprule
444	\textbf{Config} & IID & DD OOD & AA OOD & FITD OOD \\
445	\midrule
446	Frozen 9-class & 1.000$\pm$.000 & .997$\pm$.005 & .972$\pm$.026 & 1.000$\pm$.000 \\
447	Frozen MLM & .982$\pm$.016 & .993$\pm$.009 & .941$\pm$.037 & .987$\pm$.009 \\
448	E2E 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .997$\pm$.005 & --- \\
449	\bottomrule
450	\end{tabular}
451	\end{table}
452	
453	Table~\ref{tab:frozen_verify} compares frozen probing across DAPT objectives and against end-to-end fine-tuning. On easy OOD (DD, FITD), frozen MLM and frozen 9-class representations perform comparably ($\Delta \leq 1.3$\,pp). On hard OOD (ActorAttack), 9-class retains a modest advantage (0.972 vs.\ 0.941, $\Delta$\,=\,3.1\,pp) with lower variance ($\sigma$\,=\,0.026 vs.\ 0.037). Both far exceed vanilla encoders ($\leq$0.318; Table~\ref{tab:bert_proxy}). The E2E advantage over frozen 9-class is $\leq$2.5\,pp, confirming that Stage-1 representation quality is the primary source of OOD generalization.
454	
455	A striking asymmetry emerges when comparing frozen probing to the full pipeline (Table~\ref{tab:evidence_hierarchy}): MLM frozen representations \emph{outperform} the full MLM pipeline on AA OOD (0.941 vs.\ 0.893), while 9-class frozen exactly matches its full pipeline (0.972 vs.\ 0.972). This indicates that MLM's cross-seed instability originates in Stage-2 BiGRU training rather than Stage-1 DAPT---the MLM encoder produces adequate representations that are then degraded by unstable downstream optimization. Classification DAPT, by contrast, produces representations that remain robust through Stage-2 training, explaining its consistently lower variance (Table~\ref{tab:evidence_hierarchy}).
456	
457	This two-level structure---DAPT vs.\ no-DAPT producing a representation quality leap (+70\,pp), classification vs.\ MLM DAPT producing a stability difference---is consistent with two further observations: $\lambda$=0 matches $\lambda > 0$ during E2E fine-tuning (Table~\ref{tab:lambda}), and mean pooling matches BiGRU under E2E (Table~\ref{tab:temporal}). Once DAPT representations are strong, downstream configuration details have minimal impact.
458	
459	\section{Temporal Aggregation Comparison}
460	\label{app:temporal}
461	
462	\begin{table}[ht]
463	\centering
464	\footnotesize
465	\caption{Temporal aggregation comparison: mean pooling vs.\ BiGRU under frozen and end-to-end (E2E) settings (3-seed mean$\pm$std). Plan\_002 9-class checkpoints.}
466	\label{tab:temporal}
467	\begin{tabular}{@{}llccc@{}}
468	\toprule
469	\textbf{Setting} & \textbf{Aggregator} & DD OOD & AA OOD \\
470	\midrule
471	\multirow{2}{*}{Frozen} & BiGRU & .997$\pm$.005 & .972$\pm$.026 \\
472	& Mean pooling & .991$\pm$.013 & .962$\pm$.015 \\
473	\midrule
474	\multirow{2}{*}{E2E} & BiGRU & 1.000$\pm$.000 & .997$\pm$.005 \\
475	& Mean pooling & 1.000$\pm$.000 & 1.000$\pm$.000 \\
476	\bottomrule
477	\end{tabular}
478	\end{table}
479	
480	Table~\ref{tab:temporal} compares BiGRU and mean pooling under both frozen and E2E settings. Under frozen probing (the main paper's pipeline), BiGRU provides a marginal advantage on ActorAttack (+1.0\,pp) with overlapping confidence intervals, consistent with the main text finding that temporal order is not a core detection factor ($|\Delta| < 1$\,pp under turn shuffling; Section~\ref{sec:decomposition}). Under E2E fine-tuning, the difference vanishes entirely: mean pooling saturates all benchmarks at F1\,=\,1.000. The choice of frozen BiGRU in the main pipeline reflects a design trade-off: it enables representation-level analysis (CKA, t-SNE) that E2E would confound, while sacrificing $\leq$1\,pp on the hardest OOD set.
481	
482	\section{Length Stratification Analysis}
483	\label{app:length}
484	
485	\begin{table}[ht]
486	\centering
487	\footnotesize
488	\caption{Jailbreak recall by conversation length bin on OOD evaluation (3-seed majority vote). Benign conversations span 12--20 turns; jailbreak conversations span 3--10 turns.}
489	\label{tab:length}
490	\begin{tabular}{@{}llccc@{}}
491	\toprule
492	\textbf{Dataset} & \textbf{Variant} & 1--3 turns & 4--6 turns & 7--10 turns \\
493	\midrule
494	\multirow{2}{*}{DD OOD} & 9-class & --- & 100.0\% & 99.4\% \\
495	& Vanilla & --- & $\leq$2.6\% & $\leq$1.7\% \\
496	\midrule
497	\multirow{2}{*}{AA OOD} & 9-class & 93.3\% & 95.6\% & 100.0\% \\
498	& Vanilla & 0.0\% & $\leq$2.6\% & 0.0\% \\
499	\bottomrule
500	\end{tabular}
501	\end{table}
502	
503	Table~\ref{tab:length} stratifies jailbreak recall by conversation length. The 9-class model shows no systematic degradation: ActorAttack recall increases monotonically from 93.3\% (1--3 turns) to 100\% (7--10 turns), and DD recall is near-perfect across all bins.
504	
505	\paragraph{Length confound.}
506	Benign conversations (12--20 turns) and jailbreak conversations (3--10 turns) have zero length overlap in the OOD evaluation sets, raising the concern that the model discriminates by conversation length rather than content. Three observations argue against this interpretation:
507	(1)~Vanilla DeBERTa has access to identical length information via the BiGRU but achieves recall $\leq$2.6\% across all bins---length alone is insufficient without domain-adapted representations.
508	(2)~At prefix $K$=1, where all conversations are length-equalized, 9-class still achieves F1\,=\,0.773$\pm$0.041 on ActorAttack (Table~\ref{tab:actorattack_full}), demonstrating content-based detection independent of length.
509	(3)~The model is trained on IID data (Crescendo) and cannot learn OOD-specific length distributions; generalization to unseen length patterns must rely on content features that transfer across attack families.
510	
511	\paragraph{Direct empirical verification.}
512	\label{app:length_independence}
513	
514	\begin{table}[ht]
515	\centering
516	\footnotesize
517	\caption{Turn-count independence verification (9-class, plan\_002 checkpoints, 3 seeds). Part~A: FPR on test benign truncated to $K$ user turns (all seeds FPR\,=\,0). Part~B: WildChat FPR by turn-count bucket (mean$\pm$std). Part~C: jailbreak detection (F1) after padding with benign turns to 15+ total turns (mean$\pm$std where available).}
518	\label{tab:length_independence}
519	\begin{tabular}{@{}llcc@{}}
520	\toprule
521	& \textbf{Condition} & \textbf{FPR / F1} & $n$ \\
522	\midrule
523	\multicolumn{4}{l}{\textit{Part A: Benign truncation (test set)}} \\[2pt]
524	& Original (12--20 turns) & FPR = .000 & 38 \\
525	& Truncated $K$=3 & FPR = .000 & 38 \\
526	& Truncated $K$=5 & FPR = .000 & 38 \\
527	& Truncated $K$=8 & FPR = .000 & 38 \\
528	& Truncated $K$=10$^{*}$ & FPR = .000 & 38 \\
529	\midrule
530	\multicolumn{4}{l}{\textit{Part B: WildChat FPR by turn count}} \\[2pt]
531	& Short (3--10 turns) & FPR = .770$\pm$.105 & 196 \\
532	& Medium (11--15 turns) & FPR = .942$\pm$.054 & 23 \\
533	& Long (16+ turns) & FPR = .857$\pm$.117 & 7 \\
534	\midrule
535	\multicolumn{4}{l}{\textit{Part C: Jailbreak padding to 15+ turns}} \\[2pt]
536	& DD original & F1 = .996 & 80 \\
537	& DD padded & F1 = .971 ($\Delta$=$-$2.5\,pp) & 80 \\
538	& AA original & F1 = .963 & 80 \\
539	& AA padded & F1 = .383$\pm$.261 ($\Delta$=$-$57.9\,pp) & 80 \\
540	\bottomrule
541	\end{tabular}
542	\vspace{-2pt}
543	{\footnotesize $^{*}$$K$=10 did not truncate any conversation (test benign max $\sim$8 user turns).}
544	\end{table}
545	
546	Truncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut. $K$=3 and $K$=5 are the effective control conditions where all 38 conversations were truncated; $K$=10 exceeds the maximum test benign length and serves as a no-op control.
547	
548	WildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\,=\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.
549	
550	Padding jailbreak conversations with benign turns (Part~C) reveals an asymmetry: DD detection is resilient ($\Delta$=$-$2.5\,pp), but ActorAttack collapses ($\Delta$=$-$57.9\,pp). Padding experiments append benign turns \emph{after} the complete attack sequence; in practice, adversaries would not dilute their own successful attacks. The collapse nonetheless exposes BiGRU temporal aggregation as vulnerable to attention dilution on subtle attack signals, a limitation discussed in Section~\ref{sec:limitations}.
551	
552	\section{Inference Efficiency}
553	\label{app:efficiency}
554	
555	\begin{table}[ht]
556	\centering
557	\footnotesize
558	\caption{Inference efficiency comparison. DeBERTa+BiGRU and TF-IDF+LR measured on IID test (76 conversations, avg 8.3 turns, single A100). LLM latency from separate OOD evaluation (118 conversations; exp10); cross-condition comparison is indicative only.}
559	\label{tab:efficiency}
560	\begin{tabular}{@{}lrcr@{}}
561	\toprule
562	\textbf{Method} & Latency (ms) & Params & VRAM \\
563	\midrule
564	TF-IDF+LR & 0.43$\pm$0.05 & $\sim$10K & CPU \\
565	DeBERTa+BiGRU (ours) & 12.1$\pm$1.2 & 186.7M & 862\,MB \\
566	Qwen3-8B 3-shot$^{\dagger}$ & $\sim$5{,}200 & 8B & $\sim$16\,GB \\
567	\bottomrule
568	\end{tabular}
569	\vspace{-2pt}
570	{\footnotesize $^{\dagger}$Qwen3-8B latency from exp10 (DD/AA OOD, 118 conversations); not directly comparable to encoder latency measured on IID test.}
571	\end{table}
572	
573	Table~\ref{tab:efficiency} compares inference cost. On matched data (IID test), DeBERTa+BiGRU processes a conversation in 12.1\,ms---28$\times$ slower than TF-IDF (0.43\,ms) but this speed gap purchases +71\,pp on ActorAttack (F1\,=\,0.972 vs.\ 0.261; Table~\ref{tab:evidence_hierarchy}). LLM-as-judge approaches are orders of magnitude slower ($\sim$5.2\,s per conversation for Qwen3-8B 3-shot) while achieving substantially lower OOD detection (DD\,=\,0.566, AA\,=\,0.652; Table~\ref{tab:llm_judge}). Zero-shot Qwen3-8B achieves F1\,=\,0.0 on DD OOD because it predicts all conversations as benign (Table~\ref{tab:llm_judge}). The full DeBERTa+BiGRU pipeline requires 862\,MB GPU memory, enabling deployment on consumer hardware.
574	
575	\section{Data Efficiency}
576	\label{app:data_efficiency}
577	
578	\begin{table}[ht]
579	\centering
580	\footnotesize
581	\caption{Data efficiency of 9-class DAPT (3-seed mean$\pm$std, sample std with $n{-}1$ divisor) and vanilla baseline (seed 42 only). $N$ = total training conversations (balanced jailbreak/benign).}
582	\label{tab:data_efficiency}
583	\begin{tabular}{@{}rlccc@{}}
584	\toprule
585	$N$ & \textbf{Variant} & IID & DD OOD & AA OOD \\
586	\midrule
587	50 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .969$\pm$.037 \\
588	125 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .975$\pm$.019 \\
589	250 & 9-class & 1.000$\pm$.000 & 1.000$\pm$.000 & .975$\pm$.035 \\
590	350 & 9-class & 1.000$\pm$.000 & .978$\pm$.030 & .972$\pm$.033 \\
591	\midrule
592	50 & Vanilla & .646 & .529 & .234 \\
593	125 & Vanilla & .532 & .244 & .244 \\
594	250 & Vanilla & .987 & .365 & .502 \\
595	350 & Vanilla & 1.000 & .360 & .489 \\
596	\bottomrule
597	\end{tabular}
598	\end{table}
599	
600	Table~\ref{tab:data_efficiency} shows that 9-class DAPT reaches near-saturation performance with as few as 50 conversations (25 jailbreak + 25 benign): AA OOD F1\,=\,0.969$\pm$0.037, already surpassing vanilla at full training size ($N$=350, AA\,=\,0.489) by 48\,pp using only 14\% of the data. DD OOD is perfectly solved at all training sizes. Vanilla performance is noisy across $N$ (single seed); the consistent pattern is that vanilla never exceeds DD\,=\,0.53 or AA\,=\,0.50 regardless of training size, while 9-class maintains AA\,$\geq$\,0.969 at all $N$. Seed 456 is systematically lower across all $N$ values, contributing most of the cross-seed variance; this is consistent with the initialization sensitivity observed in the main results.
601	
602	\section{Auxiliary Loss Weight Ablation}
603	\label{app:lambda}
604	
605	\begin{table}[ht]
606	\centering
607	\footnotesize
608	\caption{Effect of auxiliary persuasion loss weight $\lambda$ during Stage-2 E2E fine-tuning (seed 42). Stage-1 DAPT encoder is identical across all rows; only the Stage-2 loss $L = L_{\text{binary}} + \lambda \cdot L_{\text{strategy}}$ varies.}
609	\label{tab:lambda}
610	\begin{tabular}{@{}rcccc@{}}
611	\toprule
612	$\lambda$ & IID & DD OOD & FITD OOD & AA OOD \\
613	\midrule
614	0 & 1.000 & 1.000 & 1.000 & 1.000 \\
615	0.1 & 1.000 & 1.000 & 1.000 & .990 \\
616	0.5 & 1.000 & 1.000 & 1.000 & .981 \\
617	1.0 & 1.000 & 1.000 & 1.000 & .981 \\
618	2.0 & 1.000 & 1.000 & 1.000 & .944 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	During Stage-2 E2E fine-tuning, the auxiliary persuasion loss weight $\lambda$ has limited impact on detection (Table~\ref{tab:lambda}): the maximum AA OOD gap across all $\lambda$ values is 5.6\,pp (single seed), comparable to the cross-seed variance ($\sim$6\,pp) observed in the main results. All configurations converge to perfect validation F1 within epoch 1, indicating that DAPT representations already encode sufficient discriminative features for downstream classification (Section~\ref{app:frozen_verify}). The value of persuasion strategy classification lies in Stage-1 DAPT---where it shapes encoder representations that transfer across attack families---not in the Stage-2 auxiliary loss.
624	
625	\section{OOD Strategy Prediction Analysis}
626	\label{app:strategy_pred}
627	
628	\begin{table}[ht]
629	\centering
630	\footnotesize
631	\caption{OOD strategy prediction accuracy (jailbreak turns only) and detection rate for the 9-class model (3-seed mean). $r$: Pearson correlation between per-strategy prediction accuracy and per-strategy detection rate.}
632	\label{tab:strategy_pred}
633	\begin{tabular}{@{}lcccc@{}}
634	\toprule
635	\textbf{Dataset} & Strat.\ Acc.\ & Det.\ Rate & Missed (per seed) & $r$ \\
636	\midrule
637	DD OOD & 50.1\% & 99.6\% & 0 / 0 / 1 & $\sim$0.45 \\
638	AA OOD & 50.1\% & 96.2\% & 1 / 7 / 1 & $\sim$0.24 \\
639	\bottomrule
640	\end{tabular}
641	\end{table}
642	
643	Table~\ref{tab:strategy_pred} reports OOD strategy prediction accuracy alongside detection rates. Strategy prediction accuracy is substantially above random (50.1\% vs.\ 11.1\% chance for 9 classes) and positively correlated with detection success ($r \approx 0.24$--0.45), but strategy prediction is not the detection mechanism: frozen probing with a randomly initialized strategy head (Appendix~\ref{app:frozen_verify}) achieves 97.2\% AA OOD detection, and $\lambda$=0 (no strategy loss) matches or exceeds $\lambda > 0$ during E2E fine-tuning (Table~\ref{tab:lambda}). The classification objective shapes representations during Stage-1 DAPT training; at inference, strategy predictions are a byproduct of those representations, not a driver of detection.
644	
645	\section{Cross-Seed Ensemble}
646	\label{app:ensemble}
647	
648	\begin{table}[ht]
649	\centering
650	\footnotesize
651	\caption{Majority vote ensemble (3 seeds) vs.\ single-seed mean on OOD Full. ``Fixed'' = samples corrected by ensemble; ``Broke'' = samples corrupted by ensemble.}
652	\label{tab:ensemble}
653	\begin{tabular}{@{}lcccc@{}}
654	\toprule
655	\textbf{Variant} & DD single$\to$ens. & AA single$\to$ens. & Fixed & Broke \\
656	\midrule
657	9-class & .997$\to$\textbf{1.000} & .972$\to$\textbf{.981} & 5 & 0 \\
658	MLM & .914$\to$\textbf{1.000} & .897$\to$\textbf{.953} & 26 & 0 \\
659	Vanilla & .258$\to$.258 & .258$\to$.258 & 0 & 0 \\
660	\bottomrule
661	\end{tabular}
662	\end{table}
663	
664	Table~\ref{tab:ensemble} shows that majority vote never corrupts correct predictions (Broke\,=\,0 for all variants). MLM benefits most from ensembling (+8.6\,pp DD, +6.0\,pp AA), because its per-seed errors are complementary---each seed fails on different samples, and the majority corrects these. This further exposes MLM's seed instability: its individual seeds are unreliable, but their errors are uncorrelated. By contrast, 9-class seeds are already highly consistent (std\,$\leq$\,0.026), leaving minimal room for ensemble improvement (+0.3--0.9\,pp). Vanilla errors are systematic (all seeds fail on the same OOD samples), so ensembling provides no benefit.
665	
666	\section{Seed-Level F1 Comparisons}
667	\label{app:seed_level}
668	
669	To verify that cross-seed pooling does not mask inconsistent pairwise orderings, Table~\ref{tab:seed_level} reports per-seed F1 for all variants on OOD DD and ActorAttack at full conversation length. The relative ordering of variants is consistent across all three seeds: classification-supervised variants (9-class, binary, scrambled) dominate MLM and vanilla at every seed, and no seed reverses the hierarchy established by the pooled analysis.
670	
671	% Placeholder: seed-level F1 table to be inserted when data available
672	% \input{seed_level_table}
673	\begin{table}[h]
674	\centering
675	\small
676	\caption{Per-seed F1 on OOD Full for key variants (seeds 42, 123, 456). The relative ordering is consistent across seeds.}
677	\label{tab:seed_level}
678	\begin{tabular}{@{}lcccccc@{}}
679	\toprule
680	& \multicolumn{3}{c}{DD-Full} & \multicolumn{3}{c}{AA-Full} \\
681	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
682	\textbf{Variant} & s42 & s123 & s456 & s42 & s123 & s456 \\
683	\midrule
684	9-class & -- & -- & -- & -- & -- & -- \\
685	Binary & -- & -- & -- & -- & -- & -- \\
686	Scrambled & -- & -- & -- & -- & -- & -- \\
687	MLM-only & -- & -- & -- & -- & -- & -- \\
688	Vanilla & -- & -- & -- & -- & -- & -- \\
689	\bottomrule
690	\end{tabular}
691	\vspace{-2pt}
692	{\footnotesize Placeholder: exact values to be filled from seed-level extraction.}
693	\end{table}
694	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4da16eb7-2831-46f9-8dea-d68b33f85820",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "50c36fb4-3b01-4c2a-9775-7a5a70ccd4bb",
  "sourceToolAssistantUUID": "4da16eb7-2831-46f9-8dea-d68b33f85820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-22T13:48:38.312Z_

Now let me search for the specific changes requested. Let me check for the DisPeD footnote in introduction.tex and look for "causal" vs "discriminative" language across files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50c36fb4-3b01-4c2a-9775-7a5a70ccd4bb",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiHwDbBtK48zVTyNRK7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e05ced47-2250-465d-8770-a0c858211681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1K9inNmWAi47Vt1LpSVHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31693,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31693,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T13:48:40.970Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DtCmDsacFzn8Z295okbT9z`</summary>

```json
{
  "pattern": "footnote.*[Dd]isentangl",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e05ced47-2250-465d-8770-a0c858211681",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiHwDbBtK48zVTyNRK7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42e258ba-7c62-4814-87e8-a9c415ffe383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1K9inNmWAi47Vt1LpSVHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31693,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31693,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T13:48:41.005Z_

<details><summary>↩ Tool result · `toolu_01DtCmDsacFzn8Z295okbT9z`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42e258ba-7c62-4814-87e8-a9c415ffe383",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "5b4a7f1f-7735-414d-aa5c-db351f7a845a",
  "sourceToolAssistantUUID": "42e258ba-7c62-4814-87e8-a9c415ffe383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T13:48:41.722Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QUZj9Rqj46GTjpmo89S9zJ`</summary>

```json
{
  "pattern": "causal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b4a7f1f-7735-414d-aa5c-db351f7a845a",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiHwDbBtK48zVTyNRK7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0826a48-4cd0-4871-b24b-72dad88f1cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1K9inNmWAi47Vt1LpSVHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31693,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31693,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T13:48:41.739Z_

<details><summary>↩ Tool result · `toolu_01QUZj9Rqj46GTjpmo89S9zJ`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0826a48-4cd0-4871-b24b-72dad88f1cc1",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "9fa4358e-158b-485e-9821-5b2c34aa7ae6",
  "sourceToolAssistantUUID": "e0826a48-4cd0-4871-b24b-72dad88f1cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T13:48:42.727Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017h1UTGhcQ2yVDAE9Nuc2Ni`</summary>

```json
{
  "pattern": "discriminative",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fa4358e-158b-485e-9821-5b2c34aa7ae6",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiHwDbBtK48zVTyNRK7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f30c8c3-79c0-40df-95e8-97f424e94edd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1K9inNmWAi47Vt1LpSVHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31693,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31693,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:48:42.748Z_

<details><summary>↩ Tool result · `toolu_017h1UTGhcQ2yVDAE9Nuc2Ni`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex:14:OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex:63:Bootstrap CIs confirm non-overlapping intervals (9-class DD Full [0.943, 1.000] vs.\ vanilla [0.202, 0.341]; all permutation $p < 0.0001$). FITD is non-discriminative (all variants F1\,$\geq$\,0.990; Section~\ref{sec:limitations}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex:68:\caption{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families. Vanilla DeBERTa collapses on OOD Deceptive Delight, confirming the necessity of domain-adaptive pretraining. FITD is non-discriminative for all methods (Section~\ref{sec:limitations}).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex:140:DD and FITD confirm no regression on easier attacks; ActorAttack provides the discriminative evaluation where lexical methods fail.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex:189:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex:53:Binary vs.\ 9-class equivalence (F1 gap $\leq$3.9\,pp) suggests the binary head is not the critical differentiator. FITD provides minimal discriminative signal (all variants F1\,$\geq$\,0.990), serving as confirmation that simple attacks do not challenge any variant.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:367:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:432:The 9-class model achieves substantially lower ECE than vanilla on OOD data (0.12--0.14 vs.\ 0.50--0.67), indicating that domain adaptation improves not only discriminative performance but also confidence calibration. IID calibration is near-perfect for both variants. The residual OOD ECE (0.12--0.14) suggests that temperature scaling could further improve deployment reliability.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:623:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:506:\@writefile{lof}{\contentsline {figure}{\numberline {2}{\ignorespaces Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families. Vanilla DeBERTa collapses on OOD Deceptive Delight, confirming the necessity of domain-adaptive pretraining. FITD is non-discriminative for all methods (Section~\ref {sec:limitations}).}}{5}{figure.caption.12}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:507:\newlabel{fig:cross_attack_bar}{{2}{5}{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families. Vanilla DeBERTa collapses on OOD Deceptive Delight, confirming the necessity of domain-adaptive pretraining. FITD is non-discriminative for all methods (Section~\ref {sec:limitations})}{figure.caption.12}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f30c8c3-79c0-40df-95e8-97f424e94edd",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "036f0c5a-d58b-4ef2-a4ab-fa90c269283a",
  "sourceToolAssistantUUID": "8f30c8c3-79c0-40df-95e8-97f424e94edd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T13:48:44.149Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SCoomVnGEXCRweNTFEcAUu`</summary>

```json
{
  "pattern": "Zhang|Maennel|consistent with|opposite direction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "036f0c5a-d58b-4ef2-a4ab-fa90c269283a",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiHwDbBtK48zVTyNRK7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a2b751d-5fc6-49c2-abc6-649109dc9ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1K9inNmWAi47Vt1LpSVHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31693,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31693,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T13:48:44.167Z_

<details><summary>↩ Tool result · `toolu_01SCoomVnGEXCRweNTFEcAUu`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex:58:On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628 at $K$=1 to 0.312 at Full), consistent with attack turns occupying ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:179:\bibitem[{Hua et~al.(2026)Hua, Li, Shi, Yu, and Zhang}]{hua2026rcs}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:180:Peichun Hua, Hao Li, Shanghao Shi, Zhiyuan Yu, and Ning Zhang. 2026.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:254:\bibitem[{Li et~al.(2024)Li, Han, Steneker, Primack, Goodside, Zhang, Wang,
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:257:  Zhang, Zifan Wang, Cristina Menghini, and Summer Yue. 2024.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:428:\bibitem[{Wang et~al.(2019)Wang, Shi, Kim, Oh, Yang, Zhang, and
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:430:Xuewei Wang, Weiyan Shi, Richard Kim, Yoojung Oh, Sijia Yang, Jingwen Zhang,
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:458:Zhangchen Xu, Fengqing Jiang, Luyao Niu, Jinyuan Jia, Bill~Yuchen Lin, and
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:471:\bibitem[{Yang et~al.(2025)Yang, Yang, Zhang, Wang, Li, Lin
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:473:An~Yang, Baosong Yang, Beichen Zhang, Binyuan Wang, Bo~Li, Bowen Lin, and 1
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:488:\bibitem[{Zeng et~al.(2024{\natexlab{b}})Zeng, Lin, Zhang, Yang, Jia, and
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:490:Yi~Zeng, Hongpeng Lin, Jingwen Zhang, Diyi Yang, Ruoxi Jia, and Weiyan Shi.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:497:\bibitem[{Zhang et~al.(2025)Zhang, Zhai, Guo, Hu, Guo, Fang, Zhao, Shen, Wang,
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:499:Shenyi Zhang, Yuchen Zhai, Keyan Guo, Hongxin Hu, Shengnan Guo, Zheng Fang,
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1067:\bibcite{hua2026rcs}{{25}{2026}{{Hua et~al.}}{{Hua, Li, Shi, Yu, and Zhang}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1077:\bibcite{li2024mhj}{{35}{2024}{{Li et~al.}}{{Li, Han, Steneker, Primack, Goodside, Zhang, Wang, Menghini, and Yue}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1209:\bibcite{wang2019persuasion}{{58}{2019}{{Wang et~al.}}{{Wang, Shi, Kim, Oh, Yang, Zhang, and Yu}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1215:\bibcite{qwen3_2025}{{64}{2025}{{Yang et~al.}}{{Yang, Yang, Zhang, Wang, Li, Lin et~al.}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1217:\bibcite{zeng2024pap}{{66}{2024{b}}{{Zeng et~al.}}{{Zeng, Lin, Zhang, Yang, Jia, and Shi}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1218:\bibcite{zhang2025jbshield}{{67}{2025}{{Zhang et~al.}}{{Zhang, Zhai, Guo, Hu, Guo, Fang, Zhao, Shen, Wang, and Wang}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:162:  author={Zeng, Yi and Lin, Hongpeng and Zhang, Jingwen and Yang, Diyi and Jia, Ruoxi and Shi, Weiyan},
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:250:  author={Li, Nathaniel and Han, Ziwen and Steneker, Ian and Primack, Willow and Goodside, Riley and Zhang, Hugh and Wang, Zifan and Menghini, Cristina and Yue, Summer},
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:324:  author={Yang, An and Yang, Baosong and Zhang, Beichen and Wang, Binyuan and Li, Bo and Lin, Bowen and others},
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:454:  author={Wang, Xuewei and Shi, Weiyan and Kim, Richard and Oh, Yoojung and Yang, Sijia and Zhang, Jingwen and Yu, Zhou},
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:508:  author={Hua, Peichun and Li, Hao and Shi, Shanghao and Yu, Zhiyuan and Zhang, Ning},
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:547:  author={Xu, Zhangchen and Jiang, Fengqing and Niu, Luyao and Jia, Jinyuan and Lin, Bill Yuchen and Poovendran, Radha},
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:565:  author={Zhang, Shenyi and Zhai, Yuchen and Guo, Keyan and Hu, Hongxin and Guo, Shengnan and Fang, Zheng and Zhao, Lingchen and Shen, Chao and Wang, Cong and Wang, Qian},
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:101:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:177:FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition, consistent with FITD's commitment-consistency exploitation~\citep{cialdini2001influence}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:193:Figure~\ref{fig:tsne} visualizes mean-pooled \texttt{[CLS]} embeddings via t-SNE for three representative variants (Vanilla, JB-MLM, 9-Class) on DD OOD and ActorAttack. Vanilla embeddings show dispersed jailbreak clusters with ambiguous decision boundaries, while domain-adapted variants (JB-MLM, 9-Class) produce tighter, more separable clusters. JB-MLM achieves the clearest bimodal separation on both evaluation sets, consistent with its superior detection performance.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:264:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:388:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:457:This two-level structure---DAPT vs.\ no-DAPT producing a representation quality leap (+70\,pp), classification vs.\ MLM DAPT producing a stability difference---is consistent with two further observations: $\lambda$=0 matches $\lambda > 0$ during E2E fine-tuning (Table~\ref{tab:lambda}), and mean pooling matches BiGRU under E2E (Table~\ref{tab:temporal}). Once DAPT representations are strong, downstream configuration details have minimal impact.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:480:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:548:WildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\,=\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:600:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a2b751d-5fc6-49c2-abc6-649109dc9ee0",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "9909e4b1-b044-42a3-84f5-be9ccbd624af",
  "sourceToolAssistantUUID": "4a2b751d-5fc6-49c2-abc6-649109dc9ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T13:48:45.247Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WHeP7sAhG9mLkesPxRHJyD`</summary>

```json
{
  "pattern": "observation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9909e4b1-b044-42a3-84f5-be9ccbd624af",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiHwDbBtK48zVTyNRK7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b80f172-7ff7-4291-bce1-ed9fa31d227f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1K9inNmWAi47Vt1LpSVHv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31693,
      "cache_read_input_tokens": 24770,
      "output_tokens": 687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 31693
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 687,
          "cache_read_input_tokens": 24770,
          "cache_creation_input_tokens": 31693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 31693,
            "ephemeral_1h_input_tokens": 0
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

_source line 24 · 2026-05-22T13:48:45.258Z_

<details><summary>↩ Tool result · `toolu_01WHeP7sAhG9mLkesPxRHJyD`</summary>

```text
26:  \item \textbf{Architecture- and scale-dependent observation on domain adaptation.} Three encoder scales (125M, 184M, 355M) suggest adaptation need shrinks with model size, though encoders differ in architecture; same-architecture scaling is needed to isolate scale. RoBERTa-large handles structurally complex attacks without adaptation (Section~\ref{sec:cross_encoder}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b80f172-7ff7-4291-bce1-ed9fa31d227f",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "7fa014c3-9c64-4b80-95f8-b6d7c0eb4a54",
  "sourceToolAssistantUUID": "0b80f172-7ff7-4291-bce1-ed9fa31d227f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-22T13:48:48.294Z_

Now let me check the related work and method files for Zhang/Maennel references and "causal"/"discriminative" probe language.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fa014c3-9c64-4b80-95f8-b6d7c0eb4a54",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiJjNyMd58vpBBDQUb9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33cec4c9-f05c-43da-ac63-f4970cb13869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ga3W5vHJBoZ95qo1ya57tB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 56463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5390,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-22T13:48:50.248Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WsYovK9psCXjt7u6MSNQan`</summary>

```json
{
  "pattern": "Zhang|Maennel|consistent with|probing|probe",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33cec4c9-f05c-43da-ac63-f4970cb13869",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiJjNyMd58vpBBDQUb9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd8e0d41-0997-4c0a-98ad-4a070fc3b6ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ga3W5vHJBoZ95qo1ya57tB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 56463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5390,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-22T13:48:50.260Z_

<details><summary>↩ Tool result · `toolu_01WsYovK9psCXjt7u6MSNQan`</summary>

```text
9:[Omitted long matching line]
15:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd8e0d41-0997-4c0a-98ad-4a070fc3b6ae",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "fe4e8742-45a6-470d-b41a-dcb9597cb45c",
  "sourceToolAssistantUUID": "bd8e0d41-0997-4c0a-98ad-4a070fc3b6ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T13:48:51.191Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EXzA1qYA8eLPxoMbtSiU58`</summary>

```json
{
  "pattern": "Zhang|Maennel|consistent with|probing|probe",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/method.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe4e8742-45a6-470d-b41a-dcb9597cb45c",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiJjNyMd58vpBBDQUb9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0258cf08-e19e-42d8-8f0f-e2ebbc7d9b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ga3W5vHJBoZ95qo1ya57tB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 56463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5390,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T13:48:51.207Z_

<details><summary>↩ Tool result · `toolu_01EXzA1qYA8eLPxoMbtSiU58`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0258cf08-e19e-42d8-8f0f-e2ebbc7d9b49",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "6e388c6a-c8c4-4df3-9afc-dc958e5cf111",
  "sourceToolAssistantUUID": "0258cf08-e19e-42d8-8f0f-e2ebbc7d9b49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-22T13:48:52.592Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015pzN4BXj2XxWK8hyAuVXZR`</summary>

```json
{
  "pattern": "Zhang|Maennel|probing|probe|causal|discriminative",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e388c6a-c8c4-4df3-9afc-dc958e5cf111",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiJjNyMd58vpBBDQUb9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6b46763-cd4e-4254-95c2-8301ae8b972b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ga3W5vHJBoZ95qo1ya57tB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 56463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5390,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T13:48:52.610Z_

<details><summary>↩ Tool result · `toolu_015pzN4BXj2XxWK8hyAuVXZR`</summary>

```text
13:Classification supervision is associated with lower variance on synthetic OOD (4--20$\times$ observed range, 3 seeds); on ToxicChat this reverses (std\,=\,0.087 vs.\ 0.013). Frozen probing localizes MLM instability to Stage-2 (Appendix~\ref{app:frozen_verify}).
19:Frozen probing near-parity (AA gap 3.1\,pp), label irrelevance ($d$\,=\,0.09), and mean pooling matching BiGRU ($|\Delta| < 1$\,pp) converge: classification DAPT provides robustness through optimization regularization~\citep{chen2020simclr,grill2020byol}, not semantic feature learning.
53:Binary vs.\ 9-class equivalence (F1 gap $\leq$3.9\,pp) suggests the binary head is not the critical differentiator. FITD provides minimal discriminative signal (all variants F1\,$\geq$\,0.990), serving as confirmation that simple attacks do not challenge any variant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6b46763-cd4e-4254-95c2-8301ae8b972b",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "72784309-7386-44cc-8f89-02c6ffceda2d",
  "sourceToolAssistantUUID": "b6b46763-cd4e-4254-95c2-8301ae8b972b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T13:48:53.631Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01T4b4jGnR87i7PNTTW1AwLH`</summary>

```json
{
  "pattern": "frozen prob|linear prob|probing|probe",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72784309-7386-44cc-8f89-02c6ffceda2d",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiJjNyMd58vpBBDQUb9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04e43fbb-10d1-4228-b9cb-73c0c144181e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ga3W5vHJBoZ95qo1ya57tB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 56463,
      "output_tokens": 605,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5390
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 605,
          "cache_read_input_tokens": 56463,
          "cache_creation_input_tokens": 5390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5390,
            "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-22T13:48:53.651Z_

<details><summary>↩ Tool result · `toolu_01T4b4jGnR87i7PNTTW1AwLH`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex:9:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex:15:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:353:\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\pm$std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\ref{tab:main_results}--\ref{tab:evidence_hierarchy}); Table~\ref{tab:frozen_verify} uses plan\_002 checkpoints, yielding higher frozen accuracy (DD\,=\,.997, AA\,=\,.972) and a narrower E2E gap ($\leq$2.5\,pp).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:359:Frozen probing & 1.000$\pm$.000 & .994$\pm$.005 & .939$\pm$.047 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:367:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:399:\caption{BERT-base-uncased (110M) frozen probing without DAPT, matching DeepContext's encoder family~\citep{deepcontext2026}. 3-seed mean$\pm$std. DeBERTa-v3 results from Table~\ref{tab:cross_encoder} for comparison.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:440:\caption{Frozen probing vs.\ end-to-end (E2E) fine-tuning (3-seed mean$\pm$std). 9-class: plan\_002 checkpoints; MLM: plan\_017\_mlm\_control (matched training). Frozen probing trains only BiGRU+MLP on frozen DAPT embeddings.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:453:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:455:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:480:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/appendix.tex:643:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex:28:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex:183:CKA analysis~\citep{kornblith2019cka} and linear probing confirm that DAPT reshapes representations substantially (Figure~\ref{fig:cka_heatmap}), though comparable CKA shifts yield different detection gains across starting points (Appendix~\ref{sec:cka_heatmap}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:268:@inproceedings{niven2019probing,
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib:429:@inproceedings{conneau2018probing,
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:74:  Baroni}]{conneau2018probing}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:169:\newblock A structural probe for finding syntax in word representations.
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:236:  detection: Adaptive probing of {LLM} activations for multi-turn attack
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.bbl:333:\bibitem[{Niven and Kao(2019)}]{niven2019probing}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:233:\citation{gururangan2018artifacts,niven2019probing}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:235:\citation{conneau2018probing,hewitt2019structural}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:944:\bibcite{conneau2018probing}{{11}{2018}{{Conneau et~al.}}{{Conneau, Kruszewski, Lample, Barrault, and Baroni}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1196:\bibcite{niven2019probing}{{45}{2019}{{Niven and Kao}}{{}}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1654:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1655:\newlabel{tab:e2e}{{17}{18}{Frozen probing vs.\ end-to-end (E2E) fine-tuning for DeBERTa-v3-base 9-class (3-seed mean$\pm $std). E2E unfreezes the Stage-1 encoder during Stage-2 training. Frozen values use main-experiment checkpoints (matching Tables~\ref {tab:main_results}--\ref {tab:evidence_hierarchy}); Table~\ref {tab:frozen_verify} uses plan\_002 checkpoints, yielding higher frozen accuracy (DD\,=\,.997, AA\,=\,.972) and a narrower E2E gap ($\leq $2.5\,pp)}{table.caption.61}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1707:\@writefile{lot}{\contentsline {table}{\numberline {19}{\ignorespaces BERT-base-uncased (110M) frozen probing without DAPT, matching DeepContext's encoder family~\citep  {deepcontext2026}. 3-seed mean$\pm $std. DeBERTa-v3 results from Table~\ref {tab:cross_encoder} for comparison.}}{18}{table.caption.64}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1708:\newlabel{tab:bert_proxy}{{19}{18}{BERT-base-uncased (110M) frozen probing without DAPT, matching DeepContext's encoder family~\citep {deepcontext2026}. 3-seed mean$\pm $std. DeBERTa-v3 results from Table~\ref {tab:cross_encoder} for comparison}{table.caption.64}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1738:\@writefile{lot}{\contentsline {table}{\numberline {21}{\ignorespaces Frozen probing vs.\ end-to-end (E2E) fine-tuning (3-seed mean$\pm $std). 9-class: plan\_002 checkpoints; MLM: plan\_017\_mlm\_control (matched training). Frozen probing trains only BiGRU+MLP on frozen DAPT embeddings.}}{19}{table.caption.66}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/main.aux:1739:\newlabel{tab:frozen_verify}{{21}{19}{Frozen probing vs.\ end-to-end (E2E) fine-tuning (3-seed mean$\pm $std). 9-class: plan\_002 checkpoints; MLM: plan\_017\_mlm\_control (matched training). Frozen probing trains only BiGRU+MLP on frozen DAPT embeddings}{table.caption.66}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex:13:Classification supervision is associated with lower variance on synthetic OOD (4--20$\times$ observed range, 3 seeds); on ToxicChat this reverses (std\,=\,0.087 vs.\ 0.013). Frozen probing localizes MLM instability to Stage-2 (Appendix~\ref{app:frozen_verify}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/conclusion.tex:19:Frozen probing near-parity (AA gap 3.1\,pp), label irrelevance ($d$\,=\,0.09), and mean pooling matching BiGRU ($|\Delta| < 1$\,pp) converge: classification DAPT provides robustness through optimization regularization~\citep{chen2020simclr,grill2020byol}, not semantic feature learning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04e43fbb-10d1-4228-b9cb-73c0c144181e",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "8ed8d54f-f78d-4d49-afd9-3cdc3d46ee39",
  "sourceToolAssistantUUID": "04e43fbb-10d1-4228-b9cb-73c0c144181e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-22T13:48:56.284Z_

Let me read the related_work.tex to see the Zhang/Maennel references in full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ed8d54f-f78d-4d49-afd9-3cdc3d46ee39",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiKM3LLKMC5jcb5x1cJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04f32199-317c-49f5-965e-caf7e9fef9e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kzhb94XtkR4sZKrMzJp3Zj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 61853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3847,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T13:48:56.840Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GobNXU7CGSZk8uNv1mz1bG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04f32199-317c-49f5-965e-caf7e9fef9e8",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiKM3LLKMC5jcb5x1cJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "305c020f-7ff7-4243-9ef6-f5c66867f5e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kzhb94XtkR4sZKrMzJp3Zj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 61853,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 61853,
          "cache_creation_input_tokens": 3847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3847,
            "ephemeral_1h_input_tokens": 0
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

_source line 36 · 2026-05-22T13:48:56.849Z_

<details><summary>↩ Tool result · `toolu_01GobNXU7CGSZk8uNv1mz1bG`</summary>

```text
1	% related_work.tex — D048 deep writing optimization
2	
3	\section{Related Work}
4	
5	\paragraph{Multi-turn jailbreak attacks.}
6	All multi-turn jailbreak families share a persuasion substrate~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj}, yet each operationalizes it differently: Crescendo~\citep{russinovich2024crescendo} gradually escalates, FITD~\citep{fitd2024} exploits commitment-consistency bias, DD~\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\citep{ren2024actorattack} steers through multiple personas, and automated methods (PAIR~\citep{chao2023pair}, TAP~\citep{mehrotra2024tap}) iteratively refine adversarial prompts, extending the automated red-teaming paradigm~\citep{perez2022redteaming}. \citet{wei2023jailbroken} provide a unifying taxonomy; RED QUEEN~\citep{jiang2024redqueen} constructs concealed multi-turn scenarios across 14 harmful categories; benchmarks~\citep{mazeika2024harmbench,chao2024jailbreakbench} standardize single-turn comparison, while MultiBreak~\citep{song2026multibreak} targets multi-turn evaluation. This shared substrate with diverse surface strategies defines our evaluation: a detector must generalize across families, not merely succeed on its training distribution.
7	
8	\paragraph{Multi-turn defenses and production safety.}
9	No existing defense evaluates cross-attack transfer. Recent conversation-level systems pair fine-tuned BERT~\citep{devlin2019bert} encoders with sequence-level aggregation via GRU hierarchies (DeepContext~\citep{deepcontext2026}), turn-intention inference (BIID~\citep{tong2025biid}), graph neural networks (G-Guard~\citep{gguard2025}), or predictive generation (SafeDream~\citep{safedream2026}), yet each evaluates on a single attack family. Representation-level approaches include X-Boundary~\citep{lu2025xboundary}, JBShield~\citep{zhang2025jbshield} via activated concept analysis, gradient-space analysis (GradSafe~\citep{xie2024gradsafe}), circuit breakers via representation engineering~\citep{zou2024circuitbreakers}, latent activation probing~\citep{kulkarni2026latentadversarial,kadali2026trace}, and vision-language detection~\citep{hua2026rcs}; these require white-box access and can be brittle under adaptive attacks~\citep{derya2026revisitingjbshield}. Our work uses black-box classification with systematic cross-attack OOD evaluation. Per-turn classifiers (Llama Guard~\citep{inan2023llamaguard,metallamaguard3_2024}, ShieldGemma~\citep{zeng2024shieldgemma}, WildGuard~\citep{han2024wildguard}, Constitutional Classifiers~\citep{anthropic2025constitutional}) cannot model multi-turn trajectories, and perturbation-based defenses~\citep{robey2024smoothllm} and safety-aware decoding~\citep{xu2024safedecoding} target single-turn token-level attacks. Our ablation fills this gap: decomposition across thirteen configurations under OOD evaluation identifies domain exposure as the dominant factor behind cross-attack transfer.
10	
11	\paragraph{Computational persuasion and discourse.}
12	Persuasion and discourse frameworks offer interpretable vocabulary for attack strategies, but whether such structure aids detection has not been empirically disentangled. Foundational work (RST~\citep{mann1988rst}, PDTB~\citep{prasad2008pdtb}, dialogue acts~\citep{stolcke2000dialogueact}, Speech Act Theory~\citep{austin1962speechacts,searle1969speechacts}) models pragmatic structure at different granularities. Building on Cialdini's principles~\citep{cialdini2001influence}, PAP~\citep{zeng2024pap} identifies 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} find identifiable strategies in 97\% of successful attacks; propaganda analysis~\citep{dasanmartino2019fine,dasanmartino2020semeval} and persuasive dialogue~\citep{wang2019persuasion} apply similar technique-level classification. Our ablation disentangles these roles: the taxonomy enables interpretable strategy characterization, but detection operates through domain-adapted embeddings regardless of label correctness.
13	
14	\paragraph{Domain-adaptive pretraining.}
15	Continued pretraining on domain text yields consistent gains~\citep{gururangan2020dontstop}, as shown in biomedicine~\citep{lee2020biobert} and scientific text~\citep{beltagy2019scibert}, extending ULMFiT~\citep{howard2018ulmfit}; yet this has not been disentangled for safety-critical generalization. Intermediate-task transfer (STILTs~\citep{phang2018stilts}) and multi-task learning~\citep{caruana1997multitask,liu2019mtdnn} confound domain exposure with supervised signal. Our MLM control confirms pretraining alone closes the OOD gap. Dataset artifact analysis~\citep{gururangan2018artifacts,niven2019probing} motivates the TF-IDF baseline, adversarial NLP~\citep{jin2020textfooler,li2020bertattack,nasr2025attackermovessecond,andriushchenko2024adaptive} informs the perturbation protocol, and probing~\citep{conneau2018probing,hewitt2019structural} underpins CKA analysis.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "305c020f-7ff7-4243-9ef6-f5c66867f5e3",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "1a59ab54-7943-4f84-a216-14c6694d5af2",
  "sourceToolAssistantUUID": "305c020f-7ff7-4243-9ef6-f5c66867f5e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-22T13:48:59.819Z_

Now let me search for the variance claim in experiments.tex more specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a59ab54-7943-4f84-a216-14c6694d5af2",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiKahrpRu114SEGxvp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb3e3d38-6fb6-4fc1-b355-aeb6e049e04b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VK3qdiobKnHgQvcKwghib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 65700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1604,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T13:49:02.700Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SihG5KN8pnkKA7PN5RMgzG`</summary>

```json
{
  "pattern": "variance|4.*20",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3e3d38-6fb6-4fc1-b355-aeb6e049e04b",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiKahrpRu114SEGxvp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "760dd776-757a-49db-b6d0-4c90eb66d49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VK3qdiobKnHgQvcKwghib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 65700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1604,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-22T13:49:02.725Z_

<details><summary>↩ Tool result · `toolu_01SihG5KN8pnkKA7PN5RMgzG`</summary>

```text
14:OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
17:For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
63:Bootstrap CIs confirm non-overlapping intervals (9-class DD Full [0.943, 1.000] vs.\ vanilla [0.202, 0.341]; all permutation $p < 0.0001$). FITD is non-discriminative (all variants F1\,$\geq$\,0.990; Section~\ref{sec:limitations}).
93:Topic classif.\ (5-class) & .541$\pm$.207 & .625$\pm$.141 & .593$\pm$.166 \\
107:\noindent\hspace{0.5em}{\small vanilla (0.312$\pm$0.026) $<$ topic (0.541$\pm$0.207) $\ll$ wiki-MLM (0.904$\pm$0.115) $\approx$ jb-MLM (0.914$\pm$0.115) $<$ scrambled (0.994$\pm$0.005) $=$ 9-class (0.994$\pm$0.005) $\approx$ binary (1.000$\pm$0.000)}
111:MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
113:[Omitted long matching line]
121:Topic classification yields DD-Full F1 = 0.541$\pm$0.207; seed 123 falls \emph{below} vanilla (0.252 vs.\ 0.312). Despite using the same jailbreak-domain training data, topic classification performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels. A misaligned objective forces the encoder to allocate capacity to irrelevant features and actively destabilizes representations that MLM would preserve.
139:For base-size encoders (125--184M), domain exposure is the primary mechanism; label correctness, granularity, temporal modeling, and domain specificity are non-factors. Classification supervision provides a complementary stability benefit (variance reduced 4--20$\times$) without changing the detection ceiling.
180:Classification supervision provides a consistent stability benefit across both base encoders (cross-seed variance: 0.005--0.046 vs.\ 0.026--0.201).
189:[Omitted long matching line]
196:Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "760dd776-757a-49db-b6d0-4c90eb66d49d",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "26af41c8-4e16-45b7-818d-e972957a7b4c",
  "sourceToolAssistantUUID": "760dd776-757a-49db-b6d0-4c90eb66d49d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-22T13:49:04.356Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WCAhp1LnAL7b18rYkYkoL8`</summary>

```json
{
  "pattern": "DisPeD.*footnote|footnote.*DisPeD|Disentangled.*two-stage|two-stage",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26af41c8-4e16-45b7-818d-e972957a7b4c",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiKahrpRu114SEGxvp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4233ad91-05ac-40f0-b821-668f497f8179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VK3qdiobKnHgQvcKwghib",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 65700,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1604
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 315,
          "cache_read_input_tokens": 65700,
          "cache_creation_input_tokens": 1604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1604,
            "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-22T13:49:04.382Z_

<details><summary>↩ Tool result · `toolu_01WCAhp1LnAL7b18rYkYkoL8`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4233ad91-05ac-40f0-b821-668f497f8179",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "a65f65bf-84b8-4bbe-8276-40894135ceb3",
  "sourceToolAssistantUUID": "4233ad91-05ac-40f0-b821-668f497f8179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-22T13:49:19.741Z_

Let me check the full line 113 of experiments.tex more carefully, and also check if there's a DisPeD definition in the intro that explains the "Disentangled" naming.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a65f65bf-84b8-4bbe-8276-40894135ceb3",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiL94HWHgYic7mCqFca",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3076f9ed-b151-4700-b219-c5cdc05f20a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D76FdXHcnQ3rAi1St25Nhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 67304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T13:49:19.886Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RRHaZkYEW2EDBKFpqZdUzW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/experiments.tex",
  "offset": 111,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3076f9ed-b151-4700-b219-c5cdc05f20a0",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiL94HWHgYic7mCqFca",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf07d88e-6b6f-42e2-ae7c-595a92b2326d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D76FdXHcnQ3rAi1St25Nhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 67304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T13:49:19.908Z_

<details><summary>↩ Tool result · `toolu_01RRHaZkYEW2EDBKFpqZdUzW`</summary>

```text
111	MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
112	All three classification-supervised variants converge to equivalent detection (F1 = 0.994--1.000); McNemar's ($p > 0.13$) and paired permutation tests ($p \geq 0.40$) provide descriptive evidence suggesting equivalence. TOST (margin = 5\,pp) confirms equivalence on DD ($p < 0.01$; Table~\ref{tab:tost_sensitivity}); on ActorAttack, TOST is underpowered (SE\,=\,0.045) despite a 2.1\,pp mean gap. Label quality and granularity are descriptively non-factors for detection.
113	Classification supervision is associated with 4--20$\times$ lower cross-seed variance over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; observed range across 3 seeds; formal variance ratio tests are not applicable at $n$=3; cross-seed ensemble yields marginal additional gains, Appendix~\ref{app:ensemble}). This stability benefit does not transfer to human-authored data, where classification-supervised variants exhibit the highest variance and pure MLM the lowest (Section~\ref{sec:human_data}).
114	Appendix~\ref{app:tsne} provides t-SNE visualizations confirming that domain-adapted variants produce tighter, more separable embedding clusters than the vanilla baseline.
115	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf07d88e-6b6f-42e2-ae7c-595a92b2326d",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "686251c7-77d6-41a0-b883-7f961e92dd07",
  "sourceToolAssistantUUID": "cf07d88e-6b6f-42e2-ae7c-595a92b2326d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T13:49:19.966Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DgVi3kctW4girMiPzhEu63`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/introduction.tex",
  "offset": 10,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "686251c7-77d6-41a0-b883-7f961e92dd07",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiL94HWHgYic7mCqFca",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "881b7963-69a5-4847-9256-bccbc39e3a1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D76FdXHcnQ3rAi1St25Nhq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 67304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T13:49:19.973Z_

<details><summary>↩ Tool result · `toolu_01DgVi3kctW4girMiPzhEu63`</summary>

```text
10	
11	Our pipeline, \textbf{DisPeD} (Disentangled Persuasion Detection), separates encoder adaptation (Stage~1) from temporal classification (Stage~2, a frozen BiGRU; Figure~\ref{fig:architecture}). Seven Stage~1 variants each isolate a single factor while holding all others constant (Section~\ref{sec:method}); the contribution is the decomposition, not the pipeline.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "881b7963-69a5-4847-9256-bccbc39e3a1d",
  "isSidechain": true,
  "promptId": "62ba17a1-244a-47e0-8c26-641f0e9acb3e",
  "agentId": "aaf4887a739276af7",
  "type": "user",
  "uuid": "048b2355-76fd-4eec-a19d-9dc8a6f65388",
  "sourceToolAssistantUUID": "881b7963-69a5-4847-9256-bccbc39e3a1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-22T13:50:09.442Z_

Now I have all the information needed. Here is the report:

---

## 逐项核查结果

### 1. abstract.tex — 精简摘要

**当前状态：已精简。** 摘要从第3行到第9行，约7句话。关键数字保留为：
- 1.8%（Llama Guard 3检出率）
- ~60 pp（MLM闭合的OOD gap）
- DD OOD F1 = 0.818 vs 0.291（mixed-LLM对比）

数字密度已大幅降低。没有发现12+个数字的旧版痕迹。但严格来说，目前仍有约5-6个具体数值（1.8%, 125-355M, 60 pp, 0.818, 0.291, 4-20x），不是"2-3个"。取决于R15的意图是"只保留2-3个"还是"大幅减少"——如果是前者，目前仍偏多。

**完整摘要文本见上方读取结果第3-9行。**

---

### 2. introduction.tex

**a) DisPeD footnote：未找到。**

第11行定义DisPeD时写的是：
```
Our pipeline, \textbf{DisPeD} (Disentangled Persuasion Detection), separates encoder adaptation (Stage~1) from temporal classification (Stage~2, a frozen BiGRU; Figure~\ref{fig:architecture}).
```
括号内说明了全称，但**没有footnote**解释"disentangled"指的是two-stage architecture。"Disentangled"的含义仅通过"separates encoder adaptation (Stage 1) from temporal classification (Stage 2)"隐式传达，没有显式脚注。

**b) "causal" → "discriminative" 语言变更：已完成。**

全文搜索"causal"返回零结果（仅在参考文献的作者名中出现Zhang等）。没有任何正文使用"causal"描述probe。conclusion.tex第19行使用"Frozen probing near-parity"，experiments.tex第183行使用"linear probing"——均无"causal"字样。变更已生效。

**c) C2 贡献降级为"observation"：已完成。**

第26行C2标题：
```
\textbf{Architecture- and scale-dependent observation on domain adaptation.}
```
"observation"一词已替换原来的claim-like措辞。正文也使用"suggest"而非断言性语言。

**d) Zhang/Maennel framing变更：未找到相关段落。**

在introduction.tex、conclusion.tex、related_work.tex中搜索"Zhang"、"Maennel"、"consistent with"、"opposite direction"，结果：
- related_work.tex中的Zhang出现仅为引用作者（zhang2025jbshield等），无framing讨论
- 无Maennel引用
- "consistent with"在experiments.tex第58行出现（"consistent with attack turns occupying benign embedding regions"），这是关于embedding region的，不是Zhang/Maennel framing

**结论：论文中似乎不存在Zhang/Maennel framing段落**，可能已被删除或从未加入，或者它在一个我没有检查的文件中。

---

### 3. conclusion.tex

**a) "causal" → "discriminative"：已完成。** 零个"causal"出现。第19行使用"Frozen probing"，第13行同样。

**b) Zhang/Maennel framing变更：** conclusion.tex中无Zhang/Maennel相关内容。

---

### 4. experiments.tex — 方差claim软化

**已完成。** 第113行和第139行的关键表述：

第113行：
```
Classification supervision is associated with 4--20× lower cross-seed variance over MLM on synthetic OOD (std 0.005 vs. 0.115 on DD; observed range across 3 seeds; formal variance ratio tests are not applicable at n=3; ...)
```

第139行：
```
Classification supervision provides a complementary stability benefit (variance reduced 4--20×) without changing the detection ceiling.
```

使用了"associated with"、"observed range across 3 seeds"、"formal variance ratio tests are not applicable at n=3"等限定语。Abstract第8行也同样软化：
```
Classification supervision is associated with substantially lower prediction variance on synthetic evaluations (observed across 3 seeds)
```

软化方向正确。不过第139行仍用"variance reduced 4--20×"（无限定语），与第113行的谨慎表述不完全一致——可能是一个overcorrection遗漏点。

---

### 5. appendix.tex — "causal" → "discriminative"

**已完成。** 全文搜索"causal"在appendix.tex中返回零结果。所有probe引用使用"frozen probing"或"linear probing"。具体出现在：
- 第353行、359行、399行、440行、453行等：均为"Frozen probing"
- 无"causal probe"残留

---

## 问题汇总

| 项目 | 状态 | 备注 |
|------|------|------|
| Abstract精简 | 部分完成 | 5-6个数字，非2-3个。如R15要求严格的2-3个则需进一步删减 |
| DisPeD footnote | **未完成** | 无footnote解释"disentangled"指two-stage architecture |
| causal→discriminative | 完成 | 全文零"causal"残留 |
| C2→observation | 完成 | 标题已改 |
| Zhang/Maennel framing | **无法验证** | 论文中未找到Zhang/Maennel framing段落 |
| Variance claim软化 | 大部分完成 | 第139行缺少限定语，与第113行不一致 |
| Appendix causal→discriminative | 完成 | 零残留 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "048b2355-76fd-4eec-a19d-9dc8a6f65388",
  "isSidechain": true,
  "agentId": "aaf4887a739276af7",
  "requestId": "req_011CbHiMHzLTR5rMwdWZpi1u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6212411-29e0-4dfe-aa2f-a22cea4f825f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/reviewer_d38db4c2",
  "sessionId": "75d84c4f-683f-47fb-bf6e-2d816a855590",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "agile-doodling-flame",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5fjXZ3dcH1btVDgjpqykW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 883,
      "cache_read_input_tokens": 68590,
      "output_tokens": 1646,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 883
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1646,
          "cache_read_input_tokens": 68590,
          "cache_creation_input_tokens": 883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 883,
            "ephemeral_1h_input_tokens": 0
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
