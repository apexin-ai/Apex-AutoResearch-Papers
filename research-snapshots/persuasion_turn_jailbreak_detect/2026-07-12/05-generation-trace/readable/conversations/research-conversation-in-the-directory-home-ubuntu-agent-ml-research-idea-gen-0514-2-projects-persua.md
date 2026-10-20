# Research conversation: In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/, 

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7d27cf508177364a.jsonl`
- **Structured JSON:** [`5eceffb85d9acb4b0431.json`](../../sessions/5e/5eceffb85d9acb4b0431.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-21T05:03:19.373Z_

In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/, search for how the OOD evaluation's benign/negative class is constructed. Look in experiments.tex and appendix.tex for mentions of "OOD", "benign", "negative", "test set", "evaluation" related to how the OOD evaluation split works. Also search for "WildChat" and "FPR" and "62.7" or "false positive". I need to understand if the OOD benign data is the same distribution as training benign data. Report exact text and line numbers. Search breadth: very thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "1a0887be-7378-4141-8704-44774ed24769",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T05:03:23.018Z_

I'll search thoroughly through the paper directory to understand how the OOD evaluation's benign/negative class is constructed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a0887be-7378-4141-8704-44774ed24769",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8S4n24Fgb6ZnKKJ3qx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ac7f862c-040b-4a2c-a843-a52fcbdd5588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XWBM1Gk7pRvKPvFkW8zTva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 15450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 590,
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

_source line 3 · 2026-05-21T05:03:23.364Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014jXWoWiF7ig1j3a4vrWRHA`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac7f862c-040b-4a2c-a843-a52fcbdd5588",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8S4n24Fgb6ZnKKJ3qx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b62c63d-43e9-462e-bef5-dee50bb950dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XWBM1Gk7pRvKPvFkW8zTva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 15450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 590,
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

_source line 4 · 2026-05-21T05:03:23.385Z_

<details><summary>↩ Tool result · `toolu_014jXWoWiF7ig1j3a4vrWRHA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b62c63d-43e9-462e-bef5-dee50bb950dc",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "93ed2b02-d922-4429-8d77-120b69828e6b",
  "sourceToolAssistantUUID": "8b62c63d-43e9-462e-bef5-dee50bb950dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T05:03:23.504Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014hjLRUscWrVbZsmB5fCDxZ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93ed2b02-d922-4429-8d77-120b69828e6b",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8S4n24Fgb6ZnKKJ3qx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c65fd014-404c-4386-967e-c28f24e182b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XWBM1Gk7pRvKPvFkW8zTva",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 15450,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 590
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 15450,
          "cache_creation_input_tokens": 590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 590,
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

_source line 6 · 2026-05-21T05:03:23.707Z_

<details><summary>↩ Tool result · `toolu_014hjLRUscWrVbZsmB5fCDxZ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c65fd014-404c-4386-967e-c28f24e182b7",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "1efe5e9a-8b25-4390-93b1-a961fbc0f25d",
  "sourceToolAssistantUUID": "c65fd014-404c-4386-967e-c28f24e182b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-21T05:03:25.239Z_

Now let me search for OOD, benign, negative, WildChat, FPR, and related terms in the relevant files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1efe5e9a-8b25-4390-93b1-a961fbc0f25d",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SDrTswCWigGwWTT7k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "06445c6d-cc3f-4f53-a983-d37583836658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019LpzExygPcajaVLuePBrTb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 16040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1851,
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

_source line 8 · 2026-05-21T05:03:25.729Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01F9Hhd2hyLgEgFdEebgnyFM`</summary>

```json
{
  "pattern": "OOD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06445c6d-cc3f-4f53-a983-d37583836658",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SDrTswCWigGwWTT7k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "401beff9-bb16-4dc4-8a9f-7aae2b5c4acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019LpzExygPcajaVLuePBrTb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 16040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1851,
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

_source line 9 · 2026-05-21T05:03:25.749Z_

<details><summary>↩ Tool result · `toolu_01F9Hhd2hyLgEgFdEebgnyFM`</summary>

```text
11:OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
13:The OOD benign set is IID (same generation pipeline as training); the OOD challenge is in distinguishing novel attack families from familiar benign conversations.
21:We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 (DD and ActorAttack) by predicting nearly all conversations as benign, and even 3-shot prompting reaches only 0.566 (DD) and 0.652 (ActorAttack). Content-level reasoning is insufficient for this task.
25:OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants.
37:\caption{Cross-attack generalization (F1) at $K$=2 and full conversation length. IID: Crescendo; OOD: Deceptive Delight (DD). 3-seed mean$\pm$std where noted; full per-$K$ in Appendix~\ref{sec:full_prefix}.}
41:& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
51:{\footnotesize $^{\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\S}$TF-IDF is deterministic (no std).}
57:On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628$\pm$0.038 at $K$=1 to 0.312$\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
67:\caption{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families. Vanilla DeBERTa collapses on OOD Deceptive Delight, confirming the necessity of domain-adaptive pretraining. FITD is non-discriminative for all methods (Section~\ref{sec:limitations}).}
80:\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\pm$std where available). Bold indicates best per column. All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\ref{tab:full_prefix} and~\ref{tab:actorattack_full}.}
99:{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Deterministic (no std). $^{\ddagger}$MLM-only IID (Table~\ref{tab:main_results}) is single-seed (42); all OOD values are 3-seed.}
102:A clear \emph{evidence hierarchy} emerges across seven variants (Table~\ref{tab:evidence_hierarchy}), ordered by OOD detection at full conversation length on DD:
111:Classification supervision reduces cross-seed variance 4--20$\times$ over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; observed across 3 seeds, suggestive but not conclusive; cross-seed ensemble yields marginal additional gains, Appendix~\ref{app:ensemble}). This stability benefit does not transfer to human-authored data, where classification-supervised variants exhibit the highest variance and pure MLM the lowest (Section~\ref{sec:human_data}).
122:ActorAttack~\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures and provides a more challenging OOD benchmark than DD.
148:\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. Bold indicates best per encoder group.}
187:[Omitted long matching line]
194:Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
225:Under adversarial paraphrasing (BERTScore 0.92), classification-supervised variants achieve zero degradation on IID and OOD DD (Table~\ref{tab:ood_perturbation}) while non-adapted models degrade by $\sim$12\,pp ($p < 0.001$); on ActorAttack, DAPT variants degrade ($\Delta$\,=\,$-$20.4\,pp) but maintain 52\,pp over vanilla (Appendix~\ref{sec:perturbation_full}).
231:The 9-class taxonomy provides interpretable characterization of known attacks ($\kappa$=0.78, $n$=50; Appendix~\ref{sec:strategy_full}) but degrades to near-random on OOD ($\kappa$=0.126; Appendix~\ref{app:strategy_pred}). Its value is as a training signal (scrambled labels produce equivalent detection) and IID characterization tool; detection operates through domain-adapted \texttt{[CLS]} embeddings, not strategy accuracy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "401beff9-bb16-4dc4-8a9f-7aae2b5c4acc",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "e2d0bd44-1b49-4a45-b726-e12881d6e579",
  "sourceToolAssistantUUID": "401beff9-bb16-4dc4-8a9f-7aae2b5c4acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T05:03:26.469Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DLdc54WZnt3imS4QifL94Y`</summary>

```json
{
  "pattern": "OOD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2d0bd44-1b49-4a45-b726-e12881d6e579",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SDrTswCWigGwWTT7k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35aa18fd-df22-45e5-92f8-0d149471222d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019LpzExygPcajaVLuePBrTb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 16040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1851,
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

_source line 11 · 2026-05-21T05:03:26.482Z_

<details><summary>↩ Tool result · `toolu_01DLdc54WZnt3imS4QifL94Y`</summary>

```text
11:\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
30:Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
33:On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
55:\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
63:\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
77:\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}
106:Per-sample majority vote across 3 seeds yields 98.3\% accuracy on ActorAttack OOD (2 false negatives, 0 false positives). No sample is misclassified by all three seeds; all 7 seed-specific errors are false negatives concentrated in shorter conversations (3--6 turns). On these 7 error samples, vanilla achieves 0/3 correct votes per sample, while 9-class majority vote correctly classifies 5/7, confirming that domain adaptation provides robust per-sample coverage even where individual seeds fail.
142:\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm$std where available.}
161:On OOD DD, the IID pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\ vanilla significance ($p < 0.001$, 49--78 discordant pairs).
162:On OOD ActorAttack, domain-adapted variants degrade substantially (9-class $\Delta$\,=\,$-$20.4$\pm$13.5\,pp, MLM $-$35.3\,pp), but perturbation narrows rather than closes the adapted vs.\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$).
186:\caption{Centered CKA similarity~\citep{kornblith2019cka} between encoder variants on IID and OOD data for DeBERTa-v3 and RoBERTa. Low off-diagonal values (vanilla vs.\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\ 9-class block shows distinct geometries (CKA $\leq$ 0.2 on RoBERTa OOD).}
193:Figure~\ref{fig:tsne} visualizes mean-pooled \texttt{[CLS]} embeddings via t-SNE for three representative variants (Vanilla, JB-MLM, 9-Class) on DD OOD and ActorAttack. Vanilla embeddings show dispersed jailbreak clusters with ambiguous decision boundaries, while domain-adapted variants (JB-MLM, 9-Class) produce tighter, more separable clusters. JB-MLM achieves the clearest bimodal separation on both evaluation sets, consistent with its superior detection performance.
198:\caption{t-SNE visualization of mean-pooled \texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}
225:[Omitted long matching line]
255:\textbf{Variant} & Mixed & DD OOD & AA OOD & FITD OOD & ToxicChat \\
264:[Omitted long matching line]
276:\textbf{Variant} & DD OOD & AA OOD \\
292:\caption{RoBERTa-large (355M) DAPT learning rate control on OOD Full (3-seed mean$\pm$std). Reducing the learning rate worsens both DD and AA, ruling out over-adaptation as the cause of the regression in Table~\ref{tab:cross_encoder}.}
305:[Omitted long matching line]
318:DD OOD & .006 \checkmark & .016 \checkmark & .035 \checkmark \\
345:To disentangle Stage-1 from Stage-2 variance, we evaluate three independently trained 9-class DAPT checkpoints (seeds 42, 123, 456) with a fixed downstream BiGRU seed (42). Results: IID F1\,=\,1.000$\pm$0.000, DD OOD\,=\,0.926$\pm$0.026, AA OOD\,=\,0.935$\pm$0.013. Stage-1 training is stable (OOD std\,$\leq$\,2.6\,pp), confirming that the variance reported in the main paper is not dominated by Stage-1 initialization.
357:\textbf{Config} & IID & DD OOD & AA OOD \\
367:[Omitted long matching line]
403:\textbf{Encoder} & IID & DD OOD & AA OOD \\
412:[Omitted long matching line]
420:\caption{Expected calibration error (ECE, 10 bins) for 9-class and vanilla on IID and OOD evaluation (3-seed mean$\pm$std). Lower is better.}
424:\textbf{Variant} & IID & DD OOD & AA OOD \\
432:The 9-class model achieves substantially lower ECE than vanilla on OOD data (0.12--0.14 vs.\ 0.50--0.67), indicating that domain adaptation improves not only discriminative performance but also confidence calibration. IID calibration is near-perfect for both variants. The residual OOD ECE (0.12--0.14) suggests that temperature scaling could further improve deployment reliability.
444:\textbf{Config} & IID & DD OOD & AA OOD & FITD OOD \\
453:[Omitted long matching line]
455:[Omitted long matching line]
469:\textbf{Setting} & \textbf{Aggregator} & DD OOD & AA OOD \\
480:[Omitted long matching line]
488:\caption{Jailbreak recall by conversation length bin on OOD evaluation (3-seed majority vote). Benign conversations span 12--20 turns; jailbreak conversations span 3--10 turns.}
494:\multirow{2}{*}{DD OOD} & 9-class & --- & 100.0\% & 99.4\% \\
497:\multirow{2}{*}{AA OOD} & 9-class & 93.3\% & 95.6\% & 100.0\% \\
506:Benign conversations (12--20 turns) and jailbreak conversations (3--10 turns) have zero length overlap in the OOD evaluation sets, raising the concern that the model discriminates by conversation length rather than content. Three observations argue against this interpretation:
509:(3)~The model is trained on IID data (Crescendo) and cannot learn OOD-specific length distributions; generalization to unseen length patterns must rely on content features that transfer across attack families.
558:\caption{Inference efficiency comparison. DeBERTa+BiGRU and TF-IDF+LR measured on IID test (76 conversations, avg 8.3 turns, single A100). LLM latency from separate OOD evaluation (118 conversations; exp10); cross-condition comparison is indicative only.}
570:{\footnotesize $^{\dagger}$Qwen3-8B latency from exp10 (DD/AA OOD, 118 conversations); not directly comparable to encoder latency measured on IID test.}
573:[Omitted long matching line]
585:$N$ & \textbf{Variant} & IID & DD OOD & AA OOD \\
600:[Omitted long matching line]
612:$\lambda$ & IID & DD OOD & FITD OOD & AA OOD \\
623:[Omitted long matching line]
625:\section{OOD Strategy Prediction Analysis}
631:\caption{OOD strategy prediction accuracy (jailbreak turns only) and detection rate for the 9-class model (3-seed mean). $r$: Pearson correlation between per-strategy prediction accuracy and per-strategy detection rate.}
637:DD OOD & 50.1\% & 99.6\% & 0 / 0 / 1 & $\sim$0.45 \\
638:AA OOD & 50.1\% & 96.2\% & 1 / 7 / 1 & $\sim$0.24 \\
643:[Omitted long matching line]
651:\caption{Majority vote ensemble (3 seeds) vs.\ single-seed mean on OOD Full. ``Fixed'' = samples corrected by ensemble; ``Broke'' = samples corrupted by ensemble.}
664:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35aa18fd-df22-45e5-92f8-0d149471222d",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "9a3bf398-6f75-4e6b-9074-f9d9c30a2be2",
  "sourceToolAssistantUUID": "35aa18fd-df22-45e5-92f8-0d149471222d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T05:03:26.989Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01482icvK3i1dugd9Mk1psuC`</summary>

```json
{
  "pattern": "benign",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a3bf398-6f75-4e6b-9074-f9d9c30a2be2",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SDrTswCWigGwWTT7k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb131701-fe44-45fc-b4cb-159c3c8feebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019LpzExygPcajaVLuePBrTb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 16040,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1851
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 500,
          "cache_read_input_tokens": 16040,
          "cache_creation_input_tokens": 1851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1851,
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

### Tool call

_source line 13 · 2026-05-21T05:03:27.000Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CxXzjpjBZEBPFUx9fNWfzp`</summary>

```json
{
  "pattern": "benign",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb131701-fe44-45fc-b4cb-159c3c8feebe",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SDrTswCWigGwWTT7k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "10f1502b-b234-447a-871f-291d3452f4d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019LpzExygPcajaVLuePBrTb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1851,
      "cache_read_input_tokens": 16040,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1851
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 500,
          "cache_read_input_tokens": 16040,
          "cache_creation_input_tokens": 1851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1851,
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

_source line 14 · 2026-05-21T05:03:27.007Z_

<details><summary>↩ Tool result · `toolu_01482icvK3i1dugd9Mk1psuC`</summary>

```text
9:The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
11:OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
13:The OOD benign set is IID (same generation pipeline as training); the OOD challenge is in distinguishing novel attack families from familiar benign conversations.
15:For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
21:We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 (DD and ActorAttack) by predicting nearly all conversations as benign, and even 3-shot prompting reaches only 0.566 (DD) and 0.652 (ActorAttack). Content-level reasoning is insufficient for this task.
57:On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628$\pm$0.038 at $K$=1 to 0.312$\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
194:Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb131701-fe44-45fc-b4cb-159c3c8feebe",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "e892f1bf-3136-4b92-9974-87666abba4e6",
  "sourceToolAssistantUUID": "cb131701-fe44-45fc-b4cb-159c3c8feebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T05:03:27.026Z_

<details><summary>↩ Tool result · `toolu_01CxXzjpjBZEBPFUx9fNWfzp`</summary>

```text
33:On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
101:[Omitted long matching line]
198:\caption{t-SNE visualization of mean-pooled \texttt{[CLS]} embeddings (perplexity=30) for Vanilla, JB-MLM, and 9-Class variants on DD OOD and ActorAttack (118 samples each; blue=benign, red=jailbreak).}
208:\caption{Cross-LLM validation (F1, full conversation). All models are trained on Qwen3-8B data; conditions vary the source of jailbreak (JB) and benign (ben.) conversations at inference. Values are evaluated under a matched 50-sample subset protocol and differ from Table~\ref{tab:evidence_hierarchy}, which uses the full evaluation set.}
225:[Omitted long matching line]
230:\caption{Error decomposition for DD Full cross-LLM conditions (matched 50-sample subsets). TP rate is identical across benign conditions; the F1 collapse in the Llama-only condition (Table~\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text.}
243:[Omitted long matching line]
375:\caption{False positive rate (\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\pm$std.}
388:[Omitted long matching line]
391:[Omitted long matching line]
517:\caption{Turn-count independence verification (9-class, plan\_002 checkpoints, 3 seeds). Part~A: FPR on test benign truncated to $K$ user turns (all seeds FPR\,=\,0). Part~B: WildChat FPR by turn-count bucket (mean$\pm$std). Part~C: jailbreak detection (F1) after padding with benign turns to 15+ total turns (mean$\pm$std where available).}
543:{\footnotesize $^{*}$$K$=10 did not truncate any conversation (test benign max $\sim$8 user turns).}
546:Truncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut. $K$=3 and $K$=5 are the effective control conditions where all 38 conversations were truncated; $K$=10 exceeds the maximum test benign length and serves as a no-op control.
550:[Omitted long matching line]
573:[Omitted long matching line]
581:\caption{Data efficiency of 9-class DAPT (3-seed mean$\pm$std, sample std with $n{-}1$ divisor) and vanilla baseline (seed 42 only). $N$ = total training conversations (balanced jailbreak/benign).}
600:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10f1502b-b234-447a-871f-291d3452f4d7",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "50f40010-1f10-4aa0-9b46-a745b804e101",
  "sourceToolAssistantUUID": "10f1502b-b234-447a-871f-291d3452f4d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T05:03:28.252Z_

Now let me search for "WildChat" and "FPR" and "62.7" more specifically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50f40010-1f10-4aa0-9b46-a745b804e101",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SU6xzzEazcsLCRs2t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85984e41-077b-4c23-a39e-baf71005d7e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FYk3kC8uwrC3wcspDyQ4Bf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5902,
      "cache_read_input_tokens": 17891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5902,
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

_source line 17 · 2026-05-21T05:03:29.516Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SkoRUNt8erQzAQzMsY6qoH`</summary>

```json
{
  "pattern": "WildChat|FPR|false positive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85984e41-077b-4c23-a39e-baf71005d7e5",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SU6xzzEazcsLCRs2t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6e0a2897-e822-475e-a8cc-6d33ad852ef9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FYk3kC8uwrC3wcspDyQ4Bf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5902,
      "cache_read_input_tokens": 17891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5902,
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

_source line 18 · 2026-05-21T05:03:29.528Z_

<details><summary>↩ Tool result · `toolu_01SkoRUNt8erQzAQzMsY6qoH`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e0a2897-e822-475e-a8cc-6d33ad852ef9",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "260be0d4-2a57-4be8-a4ec-e722866af40a",
  "sourceToolAssistantUUID": "6e0a2897-e822-475e-a8cc-6d33ad852ef9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T05:03:29.939Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VWhDEvNe7pZxA7g8m33KVB`</summary>

```json
{
  "pattern": "WildChat|FPR|false positive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "260be0d4-2a57-4be8-a4ec-e722866af40a",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SU6xzzEazcsLCRs2t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "baf00ee3-e644-4888-88c8-70fdda9a6e7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FYk3kC8uwrC3wcspDyQ4Bf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5902,
      "cache_read_input_tokens": 17891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5902,
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

_source line 20 · 2026-05-21T05:03:29.951Z_

<details><summary>↩ Tool result · `toolu_01VWhDEvNe7pZxA7g8m33KVB`</summary>

```text
103-\subsection{Error Analysis}
104-\label{app:aa_error}
105-
106:Per-sample majority vote across 3 seeds yields 98.3\% accuracy on ActorAttack OOD (2 false negatives, 0 false positives). No sample is misclassified by all three seeds; all 7 seed-specific errors are false negatives concentrated in shorter conversations (3--6 turns). On these 7 error samples, vanilla achieves 0/3 correct votes per sample, while 9-class majority vote correctly classifies 5/7, confirming that domain adaptation provides robust per-sample coverage even where individual seeds fail.
107-
108-\section{Perturbation Robustness}
109-\label{sec:perturbation_full}
--
222-{\footnotesize $^{*}$High seed variance (std = 0.306): seed 456 outlier (F1 = 0.345); remaining two seeds achieve F1 $\geq$ 0.97.}
223-\end{table}
224-
225:[Omitted long matching line]
226-
227-\begin{table}[ht]
228-\centering
229-\footnotesize
230:\caption{Error decomposition for DD Full cross-LLM conditions (matched 50-sample subsets). TP rate is identical across benign conditions; the F1 collapse in the Llama-only condition (Table~\ref{tab:cross_llm}, row~2) is driven entirely by false positives on unfamiliar benign text.}
231-\label{tab:cross_llm_error}
232-\begin{tabular}{@{}lccc@{}}
233-\toprule
--
240-\end{tabular}
241-\end{table}
242-
243:[Omitted long matching line]
244-
245-\section{Mixed-LLM Training Results}
246-\label{app:mixed_llm}
--
372-\begin{table}[ht]
373-\centering
374-\footnotesize
375:\caption{False positive rate (\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\pm$std.}
376-\label{tab:wildchat_fpr}
377-\begin{tabular}{@{}lcccc@{}}
378-\toprule
--
385-\end{tabular}
386-\end{table}
387-
388:[Omitted long matching line]
389-
390-\paragraph{Post-hoc calibration.}
391:[Omitted long matching line]
392-
393-\section{BERT-base Proxy Baseline}
394-\label{app:bert_proxy}
--
514-\begin{table}[ht]
515-\centering
516-\footnotesize
517:\caption{Turn-count independence verification (9-class, plan\_002 checkpoints, 3 seeds). Part~A: FPR on test benign truncated to $K$ user turns (all seeds FPR\,=\,0). Part~B: WildChat FPR by turn-count bucket (mean$\pm$std). Part~C: jailbreak detection (F1) after padding with benign turns to 15+ total turns (mean$\pm$std where available).}
518-\label{tab:length_independence}
519-\begin{tabular}{@{}llcc@{}}
520-\toprule
521:& \textbf{Condition} & \textbf{FPR / F1} & $n$ \\
522-\midrule
523-\multicolumn{4}{l}{\textit{Part A: Benign truncation (test set)}} \\[2pt]
524:& Original (12--20 turns) & FPR = .000 & 38 \\
525:& Truncated $K$=3 & FPR = .000 & 38 \\
526:& Truncated $K$=5 & FPR = .000 & 38 \\
527:& Truncated $K$=8 & FPR = .000 & 38 \\
528:& Truncated $K$=10$^{*}$ & FPR = .000 & 38 \\
529-\midrule
530:\multicolumn{4}{l}{\textit{Part B: WildChat FPR by turn count}} \\[2pt]
531:& Short (3--10 turns) & FPR = .770$\pm$.105 & 196 \\
532:& Medium (11--15 turns) & FPR = .942$\pm$.054 & 23 \\
533:& Long (16+ turns) & FPR = .857$\pm$.117 & 7 \\
534-\midrule
535-\multicolumn{4}{l}{\textit{Part C: Jailbreak padding to 15+ turns}} \\[2pt]
536-& DD original & F1 = .996 & 80 \\
--
543-{\footnotesize $^{*}$$K$=10 did not truncate any conversation (test benign max $\sim$8 user turns).}
544-\end{table}
545-
546:Truncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut. $K$=3 and $K$=5 are the effective control conditions where all 38 conversations were truncated; $K$=10 exceeds the maximum test benign length and serves as a no-op control.
547-
548:WildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\,=\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.
549-
550-[Omitted long context line]
551-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baf00ee3-e644-4888-88c8-70fdda9a6e7b",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "3520d8d0-9c3f-46bb-8357-e4d43019bd3d",
  "sourceToolAssistantUUID": "baf00ee3-e644-4888-88c8-70fdda9a6e7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T05:03:30.344Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017tB8fXTefH3HBAgoKTQ3eC`</summary>

```json
{
  "pattern": "62\\.7|62,7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3520d8d0-9c3f-46bb-8357-e4d43019bd3d",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SU6xzzEazcsLCRs2t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a199b91-dda9-45d9-8541-f170c14beb92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FYk3kC8uwrC3wcspDyQ4Bf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5902,
      "cache_read_input_tokens": 17891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5902,
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

_source line 22 · 2026-05-21T05:03:30.355Z_

<details><summary>↩ Tool result · `toolu_017tB8fXTefH3HBAgoKTQ3eC`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a199b91-dda9-45d9-8541-f170c14beb92",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "cfced36e-cf36-4a7d-9fa9-23d421860ab8",
  "sourceToolAssistantUUID": "9a199b91-dda9-45d9-8541-f170c14beb92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T05:03:30.705Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01WeyLwwD1rbLDj26a78UcNA`</summary>

```json
{
  "pattern": "62\\.7|62,7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfced36e-cf36-4a7d-9fa9-23d421860ab8",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8SU6xzzEazcsLCRs2t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b20972d0-e686-4515-9afc-3adbb4c83e84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FYk3kC8uwrC3wcspDyQ4Bf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5902,
      "cache_read_input_tokens": 17891,
      "output_tokens": 553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 553,
          "cache_read_input_tokens": 17891,
          "cache_creation_input_tokens": 5902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5902,
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

_source line 24 · 2026-05-21T05:03:30.723Z_

<details><summary>↩ Tool result · `toolu_01WeyLwwD1rbLDj26a78UcNA`</summary>

```text
391:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b20972d0-e686-4515-9afc-3adbb4c83e84",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "01503368-48c4-4b32-b61b-bc352ea8f31c",
  "sourceToolAssistantUUID": "b20972d0-e686-4515-9afc-3adbb4c83e84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-21T05:03:32.035Z_

Let me read the experiments.tex file more carefully to get the full context and exact line numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01503368-48c4-4b32-b61b-bc352ea8f31c",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8Sjs1FrMGEK2jDbGtE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fcfbf0d0-41d0-4bfa-81f7-a9352cabc70c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013GscGEGdZ7DoRmw3GDfH7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 23793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2254,
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

_source line 26 · 2026-05-21T05:03:32.845Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NfQpoCAwGH8yxnaBRU54pP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcfbf0d0-41d0-4bfa-81f7-a9352cabc70c",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8Sjs1FrMGEK2jDbGtE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e153ea9c-1da5-4052-9e3f-4bb9d6f00e73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013GscGEGdZ7DoRmw3GDfH7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 23793,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2254
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 114,
          "cache_read_input_tokens": 23793,
          "cache_creation_input_tokens": 2254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2254,
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

_source line 27 · 2026-05-21T05:03:32.858Z_

<details><summary>↩ Tool result · `toolu_01NfQpoCAwGH8yxnaBRU54pP`</summary>

```text
1	% experiments.tex — D024 compressed for 8-page limit
2	
3	\section{Experiments}
4	
5	\subsection{Setup}
6	
7	\paragraph{Data.}
8	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
9	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
10	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
11	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
12	No overlap exists in attack templates across families.
13	The OOD benign set is IID (same generation pipeline as training); the OOD challenge is in distinguishing novel attack families from familiar benign conversations.
14	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
15	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
16	
17	\paragraph{Models.}
18	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
19	Our vanilla DeBERTa+BiGRU configuration is architecturally equivalent to DeepContext~\citep{deepcontext2026}, differing only in encoder choice (DeBERTa-v3-base vs.\ BERT); it serves as our primary baseline.
20	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
21	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 (DD and ActorAttack) by predicting nearly all conversations as benign, and even 3-shot prompting reaches only 0.566 (DD) and 0.652 (ActorAttack). Content-level reasoning is insufficient for this task.
22	
23	\paragraph{Metrics.}
24	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
25	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants.
26	For key pairwise comparisons, we report BCa bootstrap 95\% confidence intervals (10,000 resamples over individual predictions pooled across seeds) and paired permutation tests (10,000 permutations). Bootstrap means may differ slightly from seed-averaged F1 due to the nonlinearity of F1 aggregation.
27	All standard deviations are computed over 3 random seeds using the population formula ($n$ divisor); Bessel-corrected estimates ($n{-}1$ divisor) are $\approx$22\% larger but do not alter any significance conclusions.
28	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
29	Stage-2: two-layer MLP, 20 epochs.
30	
31	%----------------------------------------------------------------------
32	\subsection{Cross-Attack Generalization}
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation length. IID: Crescendo; OOD: Deceptive Delight (DD). 3-seed mean$\pm$std where noted; full per-$K$ in Appendix~\ref{sec:full_prefix}.}
38	\label{tab:main_results}
39	\begin{tabular}{@{}lcc|cc@{}}
40	\toprule
41	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
42	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
43	\midrule
44	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.994$\pm$.005} \\
45	MLM-only$^{\ddagger}$ & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
46	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
47	TF-IDF LR$^{\S}$ & 1.000 & 1.000 & 1.000 & .961 \\
48	\bottomrule
49	\end{tabular}
50	\vspace{-2pt}
51	{\footnotesize $^{\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\S}$TF-IDF is deterministic (no std).}
52	\end{table}
53	
54	Vanilla encoders collapse under cross-attack transfer; domain-adapted variants recover near-perfect detection (Table~\ref{tab:main_results}, Figure~\ref{fig:cross_attack_bar}).
55	DD exhibits high lexical separability (TF-IDF F1\,=\,0.961); ActorAttack, where TF-IDF collapses to 0.261, serves as the primary stress test for beyond-lexical generalization.
56	All methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.
57	On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628$\pm$0.038 at $K$=1 to 0.312$\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
58	MLM achieves mean F1 $\geq$ 0.97 at all prefixes $K \leq 5$ without any classification labels; domain exposure alone is sufficient.
59	At full conversation length, MLM drops to 0.914$\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.994$\pm$0.005.
60	TF-IDF LR reaches F1 = 0.961 on full DD with near-perfect per-prefix performance ($K$=1--5: 0.994--1.000); DD is thus fully solvable by lexical features alone.
61	On structurally complex ActorAttack, TF-IDF collapses to F1 = 0.261 (precision = 1.0, recall = 0.15), while 9-class maintains 0.972$\pm$0.026: a 71\,pp gap. Lexical methods cannot capture multi-persona role-playing attack structure. This establishes a ``difficulty threshold'' for lexical methods parallel to that of vanilla encoders: both succeed on DD and fail on ActorAttack (Section~\ref{sec:limitations}).
62	Bootstrap CIs confirm non-overlapping intervals (9-class DD Full [0.943, 1.000] vs.\ vanilla [0.202, 0.341]; all permutation $p < 0.0001$). FITD is non-discriminative (all variants F1\,$\geq$\,0.990; Section~\ref{sec:limitations}).
63	
64	\begin{figure}[t]
65	\centering
66	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
67	\caption{Cross-attack overview (F1 at full conversation length). DisPeD (9-class) maintains near-perfect detection across IID and both OOD families. Vanilla DeBERTa collapses on OOD Deceptive Delight, confirming the necessity of domain-adaptive pretraining. FITD is non-discriminative for all methods (Section~\ref{sec:limitations}).}
68	\label{fig:cross_attack_bar}
69	\end{figure}
70	
71	Prefix-length analysis (Appendix Table~\ref{tab:full_prefix}) shows vanilla F1 drops from 0.628 at $K$=1 to 0.312 at full length. MLM achieves strong early detection ($K$=2: 0.993) but is unstable at full length (0.914$\pm$0.115); the 9-class model maintains 0.972--0.994 across all prefixes, demonstrating that classification supervision stabilizes against distributional drift.
72	
73	%----------------------------------------------------------------------
74	\subsection{Decomposing the Detection Mechanism}
75	\label{sec:decomposition}
76	
77	\begin{table}[t]
78	\centering
79	\small
80	\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\pm$std where available). Bold indicates best per column. All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\ref{tab:full_prefix} and~\ref{tab:actorattack_full}.}
81	\label{tab:evidence_hierarchy}
82	\begin{tabular}{@{}lccc@{}}
83	\toprule
84	\textbf{Variant} & DD-Full & AA-Full & DD-$K$=2 \\
85	\midrule
86	9-class (full model) & .994$\pm$.005 & .972$\pm$.026 & .981$\pm$.013 \\
87	Binary (2-class) & \textbf{1.000$\pm$.000} & \textbf{.990$\pm$.008} & .994$\pm$.009 \\
88	Scrambled labels & .994$\pm$.005 & .951$\pm$.043 & .981$\pm$.026 \\
89	MLM-only$^{\ddagger}$ (no labels) & .914$\pm$.115 & .893$\pm$.080 & .993$\pm$.009 \\
90	Mean pooling$^{*}$ & .991$\pm$.013 & .962$\pm$.015 & \textbf{1.000} \\
91	\midrule
92	Topic classif.\ (5-class) & .541$\pm$.207 & .625$\pm$.141 & .593$\pm$.166 \\
93	Wikipedia MLM & .904$\pm$.115 & .686$\pm$.297 & .911$\pm$.073 \\
94	Vanilla DeBERTa & .312$\pm$.026 & .258$\pm$.000 & .479$\pm$.038 \\
95	TF-IDF LR$^{\dagger}$ & .961 & .261 & \textbf{1.000} \\
96	\bottomrule
97	\end{tabular}
98	\vspace{-2pt}
99	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Deterministic (no std). $^{\ddagger}$MLM-only IID (Table~\ref{tab:main_results}) is single-seed (42); all OOD values are 3-seed.}
100	\end{table}
101	
102	A clear \emph{evidence hierarchy} emerges across seven variants (Table~\ref{tab:evidence_hierarchy}), ordered by OOD detection at full conversation length on DD:
103	
104	\vspace{2pt}
105	\noindent\hspace{0.5em}{\small vanilla (0.312$\pm$0.026) $<$ topic (0.541$\pm$0.207) $\ll$ wiki-MLM (0.904$\pm$0.115) $\approx$ jb-MLM (0.914$\pm$0.115) $<$ scrambled (0.994$\pm$0.005) $=$ 9-class (0.994$\pm$0.005) $\approx$ binary (1.000$\pm$0.000)}
106	\vspace{2pt}
107	
108	\paragraph{Domain exposure is the primary mechanism.}
109	MLM bridges $\sim$60\,pp from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without labels; this supports the DAPT interpretation~\citep{gururangan2020dontstop}. TF-IDF collapse on ActorAttack (0.261 vs.\ 9-class 0.972) confirms that domain-adapted representations capture features beyond lexical overlap.
110	All three classification-supervised variants converge to equivalent detection (F1 = 0.994--1.000); McNemar's ($p > 0.13$) and paired permutation tests ($p \geq 0.40$) confirm equivalence. TOST equivalence tests (margin = 5\,pp) confirm equivalence on DD ($p < 0.01$; Table~\ref{tab:tost_sensitivity}); on ActorAttack, TOST is underpowered (SE\,=\,0.045) despite a 2.1\,pp mean gap. Label quality and granularity are non-factors for detection.
111	Classification supervision reduces cross-seed variance 4--20$\times$ over MLM on synthetic OOD (std 0.005 vs.\ 0.115 on DD; observed across 3 seeds, suggestive but not conclusive; cross-seed ensemble yields marginal additional gains, Appendix~\ref{app:ensemble}). This stability benefit does not transfer to human-authored data, where classification-supervised variants exhibit the highest variance and pure MLM the lowest (Section~\ref{sec:human_data}).
112	Appendix~\ref{app:tsne} provides t-SNE visualizations confirming that domain-adapted variants produce tighter, more separable embedding clusters than the vanilla baseline.
113	
114	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
115	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap), though jailbreak-domain text provides an 8\,pp advantage at early prefixes ($K$=2: 0.993 vs.\ 0.911).
116	Perturbation analysis (Section~\ref{sec:perturbation}) reveals a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp.
117	
118	\paragraph{Misaligned supervision destabilizes generalization.}
119	Topic classification yields DD-Full F1 = 0.541$\pm$0.207; seed 123 falls \emph{below} vanilla (0.252 vs.\ 0.312). Despite using the same jailbreak-domain training data, topic classification performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels. A misaligned objective forces the encoder to allocate capacity to irrelevant features and actively destabilizes representations that MLM would preserve.
120	
121	\paragraph{Evidence hierarchy on structurally complex attacks.}
122	ActorAttack~\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures and provides a more challenging OOD benchmark than DD.
123	The evidence hierarchy at full conversation length is:
124	
125	\vspace{2pt}
126	\noindent\hspace{0.5em}{\small TF-IDF (0.261) $\approx$ vanilla (0.258$\pm$0.000) $<$ topic (0.625$\pm$0.141) $<$ wiki-MLM (0.686$\pm$0.297) $<$ jb-MLM (0.893$\pm$0.080) $<$ scrambled (0.951$\pm$0.043) $\approx$ 9-class (0.972$\pm$0.026) $\approx$ binary (0.990$\pm$0.008)}
127	\vspace{2pt}
128	
129	TF-IDF collapses from 0.961 (DD) to 0.261 (ActorAttack, precision = 1.0, recall = 0.15). This gap shows that domain-adapted representations capture features beyond bag-of-words.
130	All classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\,pp); this extends the DD finding. DAPT provides $\sim$71\,pp over both vanilla (0.258) and TF-IDF (0.261). Full per-prefix results and per-prefix error analysis in Appendix~\ref{sec:actorattack_full} and~\ref{app:aa_error}.
131	
132	\paragraph{Temporal modeling.}
133	Mean pooling matches BiGRU on both DD and ActorAttack (F1 gap $\leq$ 1\,pp, overlapping CIs; Appendix~\ref{app:temporal}).
134	Turn-order shuffling produces negligible change ($|\Delta| < 1$\,pp) across both DeBERTa-v3-base 9-class (DD $\Delta$\,=\,0.000, AA $\Delta$\,=\,$-$0.009, IID $\Delta$\,=\,0.000) and RoBERTa-large 9-class (DD $\Delta$\,=\,+0.001, AA $\Delta$\,=\,$-$0.007, IID $\Delta$\,=\,0.000), confirming that detection relies on per-turn representations rather than sequential patterns.
135	
136	\paragraph{Summary.}
137	For base-size encoders (125--184M), domain exposure is the primary mechanism; label correctness, granularity, temporal modeling, and domain specificity are non-factors. Classification supervision provides a complementary stability benefit (variance reduced 4--20$\times$) without changing the detection ceiling.
138	DD and FITD confirm no regression on easier attacks; ActorAttack provides the discriminative evaluation where lexical methods fail.
139	Detection is stable across conversation lengths (Appendix~\ref{app:length}), near-saturates at 50 conversations (Appendix~\ref{app:data_efficiency}), and is insensitive to auxiliary loss weight (Appendix~\ref{app:lambda}).
140	
141	%----------------------------------------------------------------------
142	\subsection{Cross-Encoder Validation}
143	\label{sec:cross_encoder}
144	
145	\begin{table}[t]
146	\centering
147	\small
148	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. Bold indicates best per encoder group.}
149	\label{tab:cross_encoder}
150	\begin{tabular}{@{}lcc@{}}
151	\toprule
152	\textbf{Variant} & DD & AA \\
153	\midrule
154	\multicolumn{3}{l}{\textit{DeBERTa-v3-base (184M)}} \\[2pt]
155	Vanilla & .312$\pm$.026 & .258$\pm$.000 \\
156	MLM & .914$\pm$.115 & .893$\pm$.080 \\
157	9-class & \textbf{.994$\pm$.005} & \textbf{.972$\pm$.026} \\
158	\midrule
159	\multicolumn{3}{l}{\textit{RoBERTa-base (125M)}} \\[2pt]
160	Vanilla & .981$\pm$.026 & .466$\pm$.163 \\
161	MLM & .987$\pm$.018 & .730$\pm$.201 \\
162	9-class & \textbf{.994$\pm$.005} & \textbf{.939$\pm$.046} \\
163	\midrule
164	\multicolumn{3}{l}{\textit{RoBERTa-large (355M)}} \\[2pt]
165	Vanilla & .927$\pm$.036 & \textbf{1.000$\pm$.000} \\
166	MLM & .884$\pm$.065 & .874$\pm$.014 \\
167	9-class & \textbf{.987$\pm$.004} & .946$\pm$.057 \\
168	\bottomrule
169	\end{tabular}
170	\end{table}
171	
172	To test whether the evidence hierarchy depends on encoder choice, we replicate vanilla, MLM, and 9-class on RoBERTa-base~\citep{liu2019roberta} (Table~\ref{tab:cross_encoder}).
173	On DD, RoBERTa-base vanilla already achieves 0.981$\pm$0.026 (vs.\ DeBERTa 0.312$\pm$0.026), so DAPT adds only 1.3\,pp. ActorAttack exposes this as DD's simplicity: RoBERTa-base vanilla collapses to 0.466$\pm$0.163, a 51.5\,pp drop, while domain-adapted variants recover (9-class: 0.939$\pm$0.046).
174	
175	RoBERTa-large (355M) reveals a capacity-DAPT interaction: its effect on ActorAttack reverses (vanilla 1.000 vs.\ 9-class 0.946), while smaller encoders require DAPT to bridge 47--71\,pp. All continued pretraining reduces ActorAttack performance for the largest encoder via representation drift (Table~\ref{tab:roberta_large_lr}), though classification DAPT partially compensates on DD (+6\,pp).
176	
177	Three encoder scales thus reveal a capacity-dependent observation for the \emph{difficulty threshold}: DeBERTa-v3-base requires adaptation for all attacks, RoBERTa-base only for complex ones, and RoBERTa-large for none (Section~\ref{sec:discussion}).
178	Classification supervision provides a consistent stability benefit across both base encoders (cross-seed variance: 0.005--0.046 vs.\ 0.026--0.201).
179	A BERT-base-uncased proxy (110M, matching DeepContext's encoder family) without adaptation achieves DD\,=\,0.318$\pm$0.031 and AA\,=\,0.275$\pm$0.027, comparable to vanilla DeBERTa-v3 (Appendix~\ref{app:bert_proxy}), confirming that cross-attack generalization is driven by DAPT rather than encoder architecture.
180	
181	CKA analysis~\citep{kornblith2019cka} and linear probing confirm that DAPT reshapes representations substantially (Figure~\ref{fig:cka_heatmap}), though comparable CKA shifts yield different detection gains across starting points (Appendix~\ref{sec:cka_heatmap}).
182	
183	%----------------------------------------------------------------------
184	\subsection{Mixed-LLM Training}
185	
186	All preceding experiments use single-source (Qwen3-8B) data. To test whether the evidence hierarchy transfers when training data mixes LLM sources, we train on 250 Qwen + 250 Llama-3.1-8B conversations (Table~\ref{tab:mixed_llm}).
187	Classification-based DAPT is the only variant that substantially outperforms vanilla: 9-class achieves DD OOD F1\,=\,0.818$\pm$0.096 (+53\,pp over vanilla 0.291$\pm$0.065), while MLM drops to vanilla level (0.289$\pm$0.101). On structurally complex ActorAttack, the advantage narrows (9-class 0.504$\pm$0.107 vs.\ vanilla 0.389$\pm$0.073, +11.5\,pp) with high seed variance, suggesting that limited per-source volume (250 per LLM) constrains generalization to complex attacks. DD and FITD thus primarily validate the baseline rather than the method; ActorAttack, where lexical methods collapse (TF-IDF F1\,=\,0.261) and vanilla encoders fail (F1\,$\leq$\,0.389 across conditions), provides the discriminative evaluation axis.
188	Mixed-LLM training confirms that classification supervision generalizes across LLM sources where unsupervised pretraining does not; full results in Appendix~\ref{app:mixed_llm}.
189	
190	%----------------------------------------------------------------------
191	\subsection{Human Data Validation}
192	\label{sec:human_data}
193	
194	Since both training and OOD evaluation data are Qwen3-8B-generated, we validate on ToxicChat~\citep{lin2023toxicchat} (204 human-written jailbreak attempts + 204 benign conversations from real LMSYS interactions).
195	
196	\begin{table}[t]
197	\centering
198	\small
199	\caption{Human data validation on ToxicChat~\citep{lin2023toxicchat} (macro F1, 3-seed mean$\pm$std). Bold indicates best. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}
200	\label{tab:human_data}
201	\begin{tabular}{@{}lc@{}}
202	\toprule
203	\textbf{Variant} & Macro F1 \\
204	\midrule
205	JB-MLM & \textbf{.837$\pm$.013} \\
206	Wiki-MLM & .791$\pm$.093 \\
207	Binary & .705$\pm$.072 \\
208	Scrambled & .616$\pm$.056 \\
209	9-class & .596$\pm$.087 \\
210	Topic & .496$\pm$.042 \\
211	\midrule
212	Vanilla & .413$\pm$.021 \\
213	\bottomrule
214	\end{tabular}
215	\end{table}
216	
217	All DAPT variants exceed vanilla by 18--42\,pp (Table~\ref{tab:human_data}), confirming that the adapted-vs.-vanilla gap is not a Qwen3-8B generation artifact: domain exposure on synthetic jailbreak text transfers to human-written attacks.
218	
219	The ordering reverses: JB-MLM leads (0.837$\pm$0.013) while 9-class ranks lower (0.596$\pm$0.087; $p < 0.001$, non-overlapping CIs). ToxicChat is single-turn, so the classification head provides no advantage; validating the multi-turn hierarchy requires multi-turn human data.
220	
221	%----------------------------------------------------------------------
222	\subsection{Perturbation Analysis}
223	\label{sec:perturbation}
224	
225	Under adversarial paraphrasing (BERTScore 0.92), classification-supervised variants achieve zero degradation on IID and OOD DD (Table~\ref{tab:ood_perturbation}) while non-adapted models degrade by $\sim$12\,pp ($p < 0.001$); on ActorAttack, DAPT variants degrade ($\Delta$\,=\,$-$20.4\,pp) but maintain 52\,pp over vanilla (Appendix~\ref{sec:perturbation_full}).
226	
227	%----------------------------------------------------------------------
228	\subsection{Strategy Trajectory Analysis}
229	\label{sec:strategy}
230	
231	The 9-class taxonomy provides interpretable characterization of known attacks ($\kappa$=0.78, $n$=50; Appendix~\ref{sec:strategy_full}) but degrades to near-random on OOD ($\kappa$=0.126; Appendix~\ref{app:strategy_pred}). Its value is as a training signal (scrambled labels produce equivalent detection) and IID characterization tool; detection operates through domain-adapted \texttt{[CLS]} embeddings, not strategy accuracy.
232	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e153ea9c-1da5-4052-9e3f-4bb9d6f00e73",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "91b60183-c887-41bb-a58e-6de37979900a",
  "sourceToolAssistantUUID": "e153ea9c-1da5-4052-9e3f-4bb9d6f00e73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T05:03:34.252Z_

Now let me read the appendix.tex file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91b60183-c887-41bb-a58e-6de37979900a",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8Su68ciJm6dsus45La",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "940b0dba-8edf-400b-8e3e-8ad89032cb52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019h1TNYHhTiSKsJPb3BhZ2t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7715,
      "cache_read_input_tokens": 26047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7715,
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

_source line 29 · 2026-05-21T05:03:35.087Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QugBG3ib6Z1J8qhE2NDLtv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "limit": 800
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "940b0dba-8edf-400b-8e3e-8ad89032cb52",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8Su68ciJm6dsus45La",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c5805f47-4280-4c47-8bff-2f1ba34c97d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019h1TNYHhTiSKsJPb3BhZ2t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7715,
      "cache_read_input_tokens": 26047,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 123,
          "cache_read_input_tokens": 26047,
          "cache_creation_input_tokens": 7715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7715,
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

_source line 30 · 2026-05-21T05:03:35.339Z_

<details><summary>↩ Tool result · `toolu_01QugBG3ib6Z1J8qhE2NDLtv`</summary>

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
35	The poor performance of content-level reasoning on unseen attack types underscores the necessity of trained classifiers with domain-adapted representations.
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
64	9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\
65	Vanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\
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
171	\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
172	\label{fig:strategy_heatmap}
173	\end{figure*}
174	
175	Figure~\ref{fig:strategy_heatmap} shows transition count matrices for three attack types.
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5805f47-4280-4c47-8bff-2f1ba34c97d8",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "40527206-7763-469e-bed3-6a14945fa6c3",
  "sourceToolAssistantUUID": "c5805f47-4280-4c47-8bff-2f1ba34c97d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-21T05:03:36.714Z_

Perfect! I found the key information. Let me search for more specific details about the benign construction and look for "62.7":

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40527206-7763-469e-bed3-6a14945fa6c3",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8T5afW1fY2GoWooujh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe2a8f8b-eb1a-4c0c-98ba-b17e6d809929",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AbCA5g9tPDfAE5HzH2W9k8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18261,
      "cache_read_input_tokens": 33762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18261,
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

_source line 32 · 2026-05-21T05:03:37.919Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012DKSwRV8d3oPPyGapf74Yg`</summary>

```json
{
  "command": "grep -n \"62\\.7\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe2a8f8b-eb1a-4c0c-98ba-b17e6d809929",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8T5afW1fY2GoWooujh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "64909321-e982-481e-ba63-563199242193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AbCA5g9tPDfAE5HzH2W9k8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18261,
      "cache_read_input_tokens": 33762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18261,
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

_source line 33 · 2026-05-21T05:03:37.965Z_

<details><summary>↩ Tool result · `toolu_012DKSwRV8d3oPPyGapf74Yg`</summary>

```text
391:ROC AUC\,=\,0.700$\pm$0.054 indicates insufficient discrimination between WildChat benign and jailbreak conversations at the representation level. At TPR$\geq$95\%, the optimal threshold still yields FPR\,=\,62.7\%---far above deployable levels. Temperature scaling cannot improve this trade-off, as ROC curves are invariant to monotonic score transforms. The AUC ceiling reflects genuine domain shift: WildChat benign and jailbreak representations overlap substantially, and no post-hoc calibration can overcome this; in-domain benign adaptation is required.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64909321-e982-481e-ba63-563199242193",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "5b4ab279-8a27-4b1d-94f1-9ab0fb93ef24",
  "sourceToolAssistantUUID": "64909321-e982-481e-ba63-563199242193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T05:03:38.328Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AtnPduLAcEc1E8VfBPYhLE`</summary>

```json
{
  "command": "grep -n \"topic-anchored\\|generation pipeline\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b4ab279-8a27-4b1d-94f1-9ab0fb93ef24",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8T5afW1fY2GoWooujh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "590fdd7e-f5c1-4cf3-8c8b-e80392408b4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AbCA5g9tPDfAE5HzH2W9k8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18261,
      "cache_read_input_tokens": 33762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18261,
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

_source line 35 · 2026-05-21T05:03:38.375Z_

<details><summary>↩ Tool result · `toolu_01AtnPduLAcEc1E8VfBPYhLE`</summary>

```text
9:The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13:The OOD benign set is IID (same generation pipeline as training); the OOD challenge is in distinguishing novel attack families from familiar benign conversations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "590fdd7e-f5c1-4cf3-8c8b-e80392408b4a",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "95b22cb3-5643-4056-863a-45de18df4f7e",
  "sourceToolAssistantUUID": "590fdd7e-f5c1-4cf3-8c8b-e80392408b4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T05:03:38.405Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RhHsSThjtu5YYEn4rwfywm`</summary>

```json
{
  "command": "grep -n \"topic-anchored\\|generation pipeline\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95b22cb3-5643-4056-863a-45de18df4f7e",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8T5afW1fY2GoWooujh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4048272-0fd7-4a79-91a5-818e40f48ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AbCA5g9tPDfAE5HzH2W9k8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18261,
      "cache_read_input_tokens": 33762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18261,
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

_source line 37 · 2026-05-21T05:03:38.460Z_

<details><summary>↩ Tool result · `toolu_01RhHsSThjtu5YYEn4rwfywm`</summary>

```text
336:Jailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4048272-0fd7-4a79-91a5-818e40f48ee0",
  "isSidechain": true,
  "promptId": "530b03d2-b700-4abb-8e4a-e171c236a9ec",
  "agentId": "a7d27cf508177364a",
  "type": "user",
  "uuid": "2fbc9611-e80c-41ed-958e-8bc904ac41d1",
  "sourceToolAssistantUUID": "a4048272-0fd7-4a79-91a5-818e40f48ee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T05:03:47.926Z_

Perfect! Now let me compile the comprehensive report with exact line numbers and text:

## Summary Report: OOD Benign Class Construction

I've found comprehensive information about how the OOD evaluation's benign/negative class is constructed. Here are the key findings:

### **Core Answer: Yes, OOD Benign Data IS the Same Distribution as Training Benign Data**

**Key Statement (experiments.tex, lines 9-13):**

Line 9: "The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign)."

**Line 11 (Critical):** "OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total."

**Line 13 (Explicit Confirmation):** "The OOD benign set is IID (same generation pipeline as training); the OOD challenge is in distinguishing novel attack families from familiar benign conversations."

### **Benign Data Generation Details (appendix.tex, line 336):**

"Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts."

All benign data (training, validation, test, and OOD) was generated by **Qwen3-8B** using the same "topic-anchored prompts" methodology with the same five domains.

### **WildChat and FPR 62.7% Reference (appendix.tex, line 391):**

"At TPR≥95%, the optimal threshold still yields FPR=62.7%---far above deployable levels."

This 62.7% FPR appears in the "Post-hoc calibration" section discussing **WildChat benign multi-turn conversations** (226 real GPT-3.5 user conversations). The paper notes that this high FPR indicates "genuine domain shift: WildChat benign and jailbreak representations overlap substantially, and no post-hoc calibration can overcome this; in-domain benign adaptation is required."

**Context of WildChat FPR Table (appendix.tex, lines 375-376):**

"False positive rate (%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1,000-conversation scale). 3-seed mean±std."

The table shows:
- 9-class: 68.1±6.4% FPR
- MLM: 44.5±14.3% FPR
- Vanilla: 48.1±4.9% FPR

### **Key Distinction: IID-test Benign vs. WildChat Benign**

The paper uses **two different benign datasets**:
1. **OOD evaluation benign**: The 38 IID-test benign conversations (from Qwen3-8B, same training pipeline) - used for OOD benchmarks on DD, AA, FITD
2. **Real-world validation benign**: 226 WildChat benign conversations (real GPT-3.5 user interactions) - used for deployment realistic evaluation, showing the 62.7% FPR problem

The "same generation pipeline as training" statement (line 13) refers to the synthetic OOD evaluation benign set, NOT WildChat.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fbc9611-e80c-41ed-958e-8bc904ac41d1",
  "isSidechain": true,
  "agentId": "a7d27cf508177364a",
  "requestId": "req_011CbF8TJvqcTmRXx3YqgPPo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ed26d56-dd45-4c1a-a96d-d7a7507d05b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/review_reviewer_2_c5464cc5",
  "sessionId": "395240ea-9adf-4cb6-9a13-54c4ea18c8ee",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MB1zXRNPT7BWSL95hkHcBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 52023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 766,
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
