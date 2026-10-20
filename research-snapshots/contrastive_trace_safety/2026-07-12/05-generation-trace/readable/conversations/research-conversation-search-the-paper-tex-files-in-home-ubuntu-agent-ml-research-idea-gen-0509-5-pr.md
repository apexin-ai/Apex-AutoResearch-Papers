# Research conversation: Search the paper tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/pap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac17197ed6a690836.jsonl`
- **Structured JSON:** [`3153f19f8f1b98a7aecc.json`](../../sessions/31/3153f19f8f1b98a7aecc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-18T03:30:04.302Z_

Search the paper tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/ for Table 2 definition, R1-8B precision values, and bootstrap/resample references.

Specifically:
1. Find all .tex files in that directory
2. Search for "22.4", "0.224", "Table 2", "tabular", "R1-8B", "r1_8b" in those files
3. Search for "resample", "bootstrap", "1000", "10000", "10,000" in those files
4. Search for "window", "W=", "W =" in those files
5. Read the relevant sections of the tex file(s) that contain Table 2 - I need to see the full table definition with all numbers
6. Read sections about methodology (layer selection, window size) for R1-8B

Report back ALL the raw numbers and parameters you find. Be thorough - read enough context around each match.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fdc0542e-b5c3-4ed1-8bde-065d1e5a0b6e",
  "agentId": "ac17197ed6a690836",
  "type": "user",
  "uuid": "a22414d3-0a07-4086-9b45-1db686610eb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-18T03:30:05.741Z_

I'll help you search through the paper tex files for this information. Let me start by finding all .tex files and then searching for the specific terms you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a22414d3-0a07-4086-9b45-1db686610eb6",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9KtiqyK7U1pLjPWk8jT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "30c040aa-d523-48ac-bc98-a2989e09dc5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014iiQzWnF74pFQCxCkRVkyK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15650,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15650,
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

_source line 3 · 2026-05-18T03:30:05.881Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01T8CD81ZqtFzQdWGcid9vB6`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30c040aa-d523-48ac-bc98-a2989e09dc5c",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9KtiqyK7U1pLjPWk8jT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eaff9956-ad24-46e9-b111-48cf1e36983a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014iiQzWnF74pFQCxCkRVkyK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15650,
      "cache_read_input_tokens": 0,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15650
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15650,
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

_source line 4 · 2026-05-18T03:30:05.924Z_

<details><summary>↩ Tool result · `toolu_01T8CD81ZqtFzQdWGcid9vB6`</summary>

```text
docs/paper/main.tex
docs/paper/sections/limitations.tex
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/discussion.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/introduction.tex
docs/paper/sections/experiments.tex
docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaff9956-ad24-46e9-b111-48cf1e36983a",
  "isSidechain": true,
  "promptId": "fdc0542e-b5c3-4ed1-8bde-065d1e5a0b6e",
  "agentId": "ac17197ed6a690836",
  "type": "user",
  "uuid": "90720800-3a94-46a4-ae55-c8a0dcb41e3b",
  "sourceToolAssistantUUID": "eaff9956-ad24-46e9-b111-48cf1e36983a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-18T03:30:07.419Z_

Now let me search for the specific terms across these files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90720800-3a94-46a4-ae55-c8a0dcb41e3b",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9Ktqd1S8BNkSGPCBAcr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "88ca7d2d-18e1-4e45-a58b-b4e4794e5ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01671CQioUVZ6KpAs8jg3qQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 15650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1067,
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

_source line 6 · 2026-05-18T03:30:08.568Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FsrTP1qtTRkpVHm7VUydbZ`</summary>

```json
{
  "pattern": "22\\.4|0\\.224|Table 2|tabular|R1-8B|r1_8b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88ca7d2d-18e1-4e45-a58b-b4e4794e5ba9",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9Ktqd1S8BNkSGPCBAcr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bac60a2f-79af-44e9-b394-f1d47c8fcf50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01671CQioUVZ6KpAs8jg3qQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 15650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1067,
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

_source line 7 · 2026-05-18T03:30:08.592Z_

<details><summary>↩ Tool result · `toolu_01FsrTP1qtTRkpVHm7VUydbZ`</summary>

```text
docs/paper/acl.sty:130:    \begin{tabular}[t]{c}
docs/paper/acl.sty:136:    \end{tabular}}
docs/paper/acl.sty:154:  \def\And{\end{tabular}\hss \egroup \hskip 1in plus 2fil
docs/paper/acl.sty:155:           \hbox to 0pt\bgroup\hss \begin{tabular}[t]{c}\bfseries}%
docs/paper/acl.sty:156:  \def\AND{\end{tabular}\hss\egroup \hfil\hfil\egroup
docs/paper/acl.sty:159:             \hbox to 0pt\bgroup\hss \begin{tabular}[t]{c}\bfseries}
docs/paper/main.log:768:\OT1/ptm/m/n/10.95 On R1-8B, the modal-ity ad-van-tage (pre-ci-sion
docs/paper/main.log:773:\OT1/ptm/m/n/10.95 +22.4pp at $\OML/cmm/m/it/10.95 W[]\OT1/cmr/m/n/10.95 1$\OT1
docs/paper/main.log:901:[]\OT1/ptm/m/n/10.95 The weak-est test (rank 12, R1-8B FPR,
docs/paper/main.log:938:\OT1/ptm/m/n/10.95 times than R1-8B and R1-32B (19.7 steps at
docs/paper/main.log:1009:\OT1/ptm/m/n/10.95 (+22.4pp); the boot-strap mean (+21.9pp) dif-
docs/paper/main.log:1105: ; \OT1/cmr/m/n/10.95 200\OMS/cmsy/m/n/10.95 g$\OT1/ptm/m/n/10.95 ). Only R1-8B
docs/paper/sections/experiments.tex:7:[Omitted long matching line]
docs/paper/sections/experiments.tex:16:\begin{tabular}{lccc}
docs/paper/sections/experiments.tex:20:R1-8B & L14 (44\%) & L14 (44\%) & ${<}0.001$ \\
docs/paper/sections/experiments.tex:25:\end{tabular}
docs/paper/sections/experiments.tex:38:\begin{tabular}{llcrrrr}
docs/paper/sections/experiments.tex:42:R1-8B & L14 & 15 & +8.2 & +22.4 & $-$7.4 & 3/3 \\
docs/paper/sections/experiments.tex:47:\end{tabular}
docs/paper/sections/experiments.tex:65:\begin{tabular}{lcccc}
docs/paper/sections/experiments.tex:72:\end{tabular}
docs/paper/sections/experiments.tex:86:\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
docs/paper/sections/experiments.tex:95:\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}
docs/paper/sections/experiments.tex:107:\end{tabular}
docs/paper/sections/experiments.tex:114:[Omitted long matching line]
docs/paper/sections/discussion.tex:7:[Omitted long matching line]
docs/paper/sections/discussion.tex:13:[Omitted long matching line]
docs/paper/sections/method.tex:14:\begin{tabular}{lccccc}
docs/paper/sections/method.tex:18:R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
docs/paper/sections/method.tex:23:\end{tabular}}
docs/paper/sections/method.tex:24:\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}
docs/paper/sections/limitations.tex:10:All probing methods produce high false positive rates on safe traces at standard operating thresholds (39--52\% across methods on R1-8B). Current probes characterize the commitment phenomenon as a research tool rather than constitute production-ready detectors. The 85.5\% oracle gap between passive monitoring and active intervention shows that early detection via passive probing captures only a fraction of the theoretically available safety signal.
docs/paper/sections/appendix.tex:23:\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\% depth). OT-7B: biased metric selects L0 (0\%), unbiased consensus selects L16 (57\%). QwQ-32B: biased metric selects L2 (3\%), unbiased consensus selects L60 (94\%). R1-32B: biased metric selects L10 (16\%), unbiased consensus selects L63 (98\%). The bias is most extreme for 64-layer models, where the composite metric selects layers in the bottom 16\% of the network while all other metrics select layers above 94\%.
docs/paper/sections/appendix.tex:39:\begin{tabular}{clllcc}
docs/paper/sections/appendix.tex:43:1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \checkmark \\
docs/paper/sections/appendix.tex:52:10 & R1-8B  & Bal.\ Acc. & 0.005 & 0.0167 & \checkmark \\
docs/paper/sections/appendix.tex:54:12 & R1-8B  & FPR & 0.044 & 0.0500 & \checkmark \\
docs/paper/sections/appendix.tex:56:\end{tabular}
docs/paper/sections/appendix.tex:59:The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B showing the largest precision gap (+22.4pp). This reflects R1-8B's already-low text FPR (11.8\%), which leaves less room for HS improvement on this metric.
docs/paper/sections/appendix.tex:65:\cref{tab:window_full} reports the complete window size ablation across all four models and seven window sizes. The main text (\cref{sec:temporal}) presents R1-8B results; here we provide the full data.
docs/paper/sections/appendix.tex:73:\begin{tabular}{llccccc}
docs/paper/sections/appendix.tex:77:\multirow{7}{*}{R1-8B}
docs/paper/sections/appendix.tex:113:\end{tabular}}%
docs/paper/sections/appendix.tex:118:\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\% ($W{=}1$) to 81.0\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\% to 4.83\%). Coverage trades off against quality, dropping from 72.1\% to 48.8\%.
docs/paper/sections/appendix.tex:124:\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
docs/paper/sections/appendix.tex:126:\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.
docs/paper/sections/appendix.tex:131:\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
docs/paper/sections/appendix.tex:135:\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
docs/paper/sections/appendix.tex:137:\begin{tabular}{lcccc}
docs/paper/sections/appendix.tex:149:\end{tabular}
docs/paper/sections/appendix.tex:168:\begin{tabular}{lcccc}
docs/paper/sections/appendix.tex:181:\end{tabular}
docs/paper/sections/appendix.tex:184:After correction of a layer selection bug, layer 16 (57\% depth) is selected. It achieves the highest balanced accuracy (68.2\%) among transformer layers and is consistent with the mid-depth pattern of R1-8B (44\%). Layer 0 (embedding) has a higher crossing rate (53.2\% vs.\ 31.9\%) but lower accuracy.
docs/paper/sections/appendix.tex:193:\begin{tabular}{lcccc}
docs/paper/sections/appendix.tex:205:\end{tabular}
docs/paper/sections/appendix.tex:208:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
docs/paper/sections/appendix.tex:210:[Omitted long matching line]
docs/paper/sections/appendix.tex:224:\paragraph{Per-seed results for R1-8B (single-layer GRU).}
docs/paper/sections/appendix.tex:229:\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}
docs/paper/sections/appendix.tex:232:\begin{tabular}{lccc}
docs/paper/sections/appendix.tex:242:\end{tabular}
docs/paper/sections/appendix.tex:252:\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}
docs/paper/sections/appendix.tex:255:\begin{tabular}{llccccc}
docs/paper/sections/appendix.tex:283:\end{tabular}}%
docs/paper/sections/appendix.tex:289:[Omitted long matching line]
docs/paper/sections/appendix.tex:303:[Omitted long matching line]
docs/paper/sections/appendix.tex:305:[Omitted long matching line]
docs/paper/sections/appendix.tex:307:[Omitted long matching line]
docs/paper/sections/appendix.tex:315:[Omitted long matching line]
docs/paper/sections/appendix.tex:330:\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}
docs/paper/sections/appendix.tex:333:\begin{tabular}{llcc}
docs/paper/sections/appendix.tex:358:\end{tabular}
docs/paper/sections/appendix.tex:365:\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). The probe score sequences for these models show smoother transitions that never trigger the hazard function, consistent with the gradual commitment pattern. R1-8B's higher detection rate likely reflects its sharper probe score transitions at commitment boundaries.
docs/paper/sections/appendix.tex:386:[Omitted long matching line]
docs/paper/sections/appendix.tex:391:\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}
docs/paper/sections/appendix.tex:401:[Omitted long matching line]
docs/paper/sections/appendix.tex:406:\paragraph{BOCPD/CUSUM.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). Only R1-8B produces non-zero detection (best: $\lambda{=}10$, 93\% rate, +3.45 steps lead). CUSUM configurations universally underperform simple thresholding on lead time. The probe score sequences for 3/4 models show smooth transitions that never trigger the hazard function (\cref{app:bocpd_config}).
docs/paper/sections/appendix.tex:416:\paragraph{Cross-model transfer.} 17 configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers) all fail. Best PCA: R1-8B $\rightarrow$ QwQ-32B at 59.5\% (PCA-2048). Best direct: QwQ-32B $\rightarrow$ R1-32B at 67.3\% but 1\% crossing rate. Implementation details in \cref{app:transfer_details}.
docs/paper/sections/appendix.tex:427:[Omitted long matching line]
docs/paper/sections/appendix.tex:440:\begin{tabular}{lcccccc}
docs/paper/sections/appendix.tex:444:R1-8B & 0.497 & 0.436 & +0.058 & [$-$0.03, +0.15] & 0.185 & No \\
docs/paper/sections/appendix.tex:449:\end{tabular}
docs/paper/acl2023.sty:130:    \begin{tabular}[t]{c}
docs/paper/acl2023.sty:136:    \end{tabular}}
docs/paper/acl2023.sty:154:  \def\And{\end{tabular}\hss \egroup \hskip 1in plus 2fil
docs/paper/acl2023.sty:155:           \hbox to 0pt\bgroup\hss \begin{tabular}[t]{c}\bfseries}%
docs/paper/acl2023.sty:156:  \def\AND{\end{tabular}\hss\egroup \hfil\hfil\egroup
docs/paper/acl2023.sty:159:             \hbox to 0pt\bgroup\hss \begin{tabular}[t]{c}\bfseries}
docs/paper/main.aux:256:\@writefile{lot}{\contentsline {table}{\numberline {1}{\ignorespaces Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep  {deepseekr1}; QwQ-32B~\citep  {qwq} is a native reasoning model; OT-7B~\citep  {openthinker} is trained with STILL~\citep  {still} on Qwen2.5-7B. Data: HarmThoughts~\citep  {harmthoughts} with step-level CP annotations. Split: 60/20/20.}}{3}{table.caption.5}\protected@file@percent }
docs/paper/main.aux:258:\newlabel{tab:models}{{1}{3}{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep {deepseekr1}; QwQ-32B~\citep {qwq} is a native reasoning model; OT-7B~\citep {openthinker} is trained with STILL~\citep {still} on Qwen2.5-7B. Data: HarmThoughts~\citep {harmthoughts} with step-level CP annotations. Split: 60/20/20}{table.caption.5}{}}
docs/paper/main.aux:515:\@writefile{lof}{\contentsline {figure}{\numberline {1}{\ignorespaces Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}}{5}{figure.caption.14}\protected@file@percent }
docs/paper/main.aux:516:\newlabel{fig:window_ablation}{{1}{5}{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%}{figure.caption.14}{}}
docs/paper/main.aux:1165:\@writefile{toc}{\contentsline {paragraph}{R1-8B}{11}{section*.34}\protected@file@percent }
docs/paper/main.aux:1234:\@writefile{lot}{\contentsline {table}{\numberline {8}{\ignorespaces Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}}{12}{table.caption.39}\protected@file@percent }
docs/paper/main.aux:1235:\newlabel{tab:text_window}{{8}{12}{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline}{table.caption.39}{}}
docs/paper/main.aux:1340:\@writefile{lot}{\contentsline {table}{\numberline {11}{\ignorespaces R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}}{13}{table.caption.50}\protected@file@percent }
docs/paper/main.aux:1341:\newlabel{tab:gru_seeds}{{11}{13}{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point}{table.caption.50}{}}
docs/paper/main.aux:1344:\@writefile{toc}{\contentsline {paragraph}{Per-seed results for R1-8B (single-layer GRU).}{13}{table.caption.50}\protected@file@percent }
docs/paper/main.aux:1353:[Omitted long matching line]
docs/paper/main.aux:1354:\newlabel{tab:gru_multi_seeds}{{12}{13}{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values}{table.caption.52}{}}
docs/paper/main.aux:1505:\@writefile{lot}{\contentsline {table}{\numberline {13}{\ignorespaces Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}}{15}{table.caption.60}\protected@file@percent }
docs/paper/main.aux:1506:\newlabel{tab:cpd_sweep}{{13}{15}{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP}{table.caption.60}{}}
docs/paper/main.aux:1625:[Omitted long matching line]
docs/paper/main.aux:1626:\newlabel{fig:pareto_two_stage}{{2}{16}{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text {screen}}{=}3$, $W_{\text {confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss}{figure.caption.66}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bac60a2f-79af-44e9-b394-f1d47c8fcf50",
  "isSidechain": true,
  "promptId": "fdc0542e-b5c3-4ed1-8bde-065d1e5a0b6e",
  "agentId": "ac17197ed6a690836",
  "type": "user",
  "uuid": "a5cf53e0-a8cb-4bee-91e3-a60f219264d1",
  "sourceToolAssistantUUID": "bac60a2f-79af-44e9-b394-f1d47c8fcf50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T03:30:09.107Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015eX5EcWkPKFCfiEyQR1pE5`</summary>

```json
{
  "pattern": "resample|bootstrap|1000|10000|10,000",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5cf53e0-a8cb-4bee-91e3-a60f219264d1",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9Ktqd1S8BNkSGPCBAcr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa5df545-3478-456b-b4f8-e6627ab8f818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01671CQioUVZ6KpAs8jg3qQc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 15650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1067,
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

_source line 9 · 2026-05-18T03:30:09.120Z_

<details><summary>↩ Tool result · `toolu_015eX5EcWkPKFCfiEyQR1pE5`</summary>

```text
docs/paper/acl.sty:213: \sfcode`\.=1000\relax}
docs/paper/acl.sty:230: \sfcode`\.=1000\relax}
docs/paper/main.log:503:* \mag=1000
docs/paper/main.log:559:Underfull \hbox (badness 10000) in paragraph at lines 3--4
docs/paper/main.log:701:Underfull \hbox (badness 10000) in paragraph at lines 99--100
docs/paper/main.log:716:Underfull \hbox (badness 10000) in paragraph at lines 104--104
docs/paper/main.log:721:Underfull \hbox (badness 10000) in paragraph at lines 104--105
docs/paper/main.log:726:Underfull \hbox (badness 10000) in paragraph at lines 105--106
docs/paper/main.log:747:Underfull \hbox (badness 10000) in paragraph at lines 7--8
docs/paper/main.log:952:Underfull \hbox (badness 10000) in paragraph at lines 158--159
docs/paper/main.log:1025:Underfull \hbox (badness 10000) in paragraph at lines 220--221
docs/paper/main.log:1049:Underfull \hbox (badness 10000) in paragraph at lines 361--362
docs/paper/main.log:1086:Underfull \hbox (badness 10000) in paragraph at lines 406--407
docs/paper/main.log:1091:Underfull \hbox (badness 10000) in paragraph at lines 406--407
docs/paper/main.log:1096:Underfull \hbox (badness 10000) in paragraph at lines 406--407
docs/paper/main.log:1110:Underfull \hbox (badness 10000) in paragraph at lines 408--409
docs/paper/main.log:1185: 84i,15n,93p,2357b,658s stack positions out of 10000i,1000n,20000p,200000b,200000s
docs/paper/main.log:1206: 917 PDF objects out of 1000 (max. 8388607)
docs/paper/main.log:1208: 168 named destinations out of 1000 (max. 500000)
docs/paper/main.log:1209: 283 words of extra memory for PDF output out of 10000 (max. 10000000)
docs/paper/sections/experiments.tex:7:[Omitted long matching line]
docs/paper/sections/experiments.tex:48:\caption{HS vs.\ text at corrected layers. $\Delta$: HS$-$text difference (pp). HB: Holm-Bonferroni pass count ($\alpha{=}0.05$, 12 tests). Bootstrap: 1000 resamples, two-sided null-centered.}
docs/paper/sections/method.tex:52:[Omitted long matching line]
docs/paper/sections/appendix.tex:36:\caption{Holm-Bonferroni step-down correction for 12 hypothesis tests (4 models $\times$ 3 metrics). Each test uses a two-sided null-centered bootstrap (1000 resamples) on trace-level metric differences (HS minus text). All tests pass at $\alpha{=}0.05$.}
docs/paper/sections/appendix.tex:210:[Omitted long matching line]
docs/paper/sections/appendix.tex:438:\caption{HS vs.\ BGE-large (1024d) text probe precision. $\Delta$: HS minus BGE-large. Bootstrap: 1000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\alpha{=}0.05$).}
docs/paper/main.aux:426:\@writefile{lot}{\contentsline {table}{\numberline {3}{\ignorespaces HS vs.\ text at corrected layers. $\Delta $: HS$-$text difference (pp). HB: Holm-Bonferroni pass count ($\alpha {=}0.05$, 12 tests). Bootstrap: 1000 resamples, two-sided null-centered.}}{4}{table.caption.10}\protected@file@percent }
docs/paper/main.aux:427:\newlabel{tab:hs_vs_text}{{3}{4}{HS vs.\ text at corrected layers. $\Delta $: HS$-$text difference (pp). HB: Holm-Bonferroni pass count ($\alpha {=}0.05$, 12 tests). Bootstrap: 1000 resamples, two-sided null-centered}{table.caption.10}{}}
docs/paper/main.aux:1143:\@writefile{lot}{\contentsline {table}{\numberline {6}{\ignorespaces Holm-Bonferroni step-down correction for 12 hypothesis tests (4 models $\times $ 3 metrics). Each test uses a two-sided null-centered bootstrap (1000 resamples) on trace-level metric differences (HS minus text). All tests pass at $\alpha {=}0.05$.}}{11}{table.caption.32}\protected@file@percent }
docs/paper/main.aux:1144:\newlabel{tab:holm_bonferroni}{{6}{11}{Holm-Bonferroni step-down correction for 12 hypothesis tests (4 models $\times $ 3 metrics). Each test uses a two-sided null-centered bootstrap (1000 resamples) on trace-level metric differences (HS minus text). All tests pass at $\alpha {=}0.05$}{table.caption.32}{}}
docs/paper/main.aux:1253:\@LN{1000}{11}
docs/paper/main.aux:1785:\@writefile{lot}{\contentsline {table}{\numberline {14}{\ignorespaces HS vs.\ BGE-large (1024d) text probe precision. $\Delta $: HS minus BGE-large. Bootstrap: 1000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\alpha {=}0.05$).}}{17}{table.caption.76}\protected@file@percent }
docs/paper/main.aux:1786:\newlabel{tab:encoder_robustness}{{14}{17}{HS vs.\ BGE-large (1024d) text probe precision. $\Delta $: HS minus BGE-large. Bootstrap: 1000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\alpha {=}0.05$)}{table.caption.76}{}}
docs/paper/acl2023.sty:213: \sfcode`\.=1000\relax}
docs/paper/acl2023.sty:230: \sfcode`\.=1000\relax}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa5df545-3478-456b-b4f8-e6627ab8f818",
  "isSidechain": true,
  "promptId": "fdc0542e-b5c3-4ed1-8bde-065d1e5a0b6e",
  "agentId": "ac17197ed6a690836",
  "type": "user",
  "uuid": "5c0a2dc4-23cf-454b-a48f-b1296b503587",
  "sourceToolAssistantUUID": "aa5df545-3478-456b-b4f8-e6627ab8f818",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T03:30:09.378Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0146UqDKXeewNyizNMHQZGAb`</summary>

```json
{
  "pattern": "window|W\\s*=|W\\s*\\(",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c0a2dc4-23cf-454b-a48f-b1296b503587",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9Ktqd1S8BNkSGPCBAcr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ce28c72-0b46-4422-95cb-fed886ab0617",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01671CQioUVZ6KpAs8jg3qQc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 15650,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1067
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 390,
          "cache_read_input_tokens": 15650,
          "cache_creation_input_tokens": 1067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1067,
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

_source line 11 · 2026-05-18T03:30:09.421Z_

<details><summary>↩ Tool result · `toolu_0146UqDKXeewNyizNMHQZGAb`</summary>

```text
docs/paper/sections/experiments.tex:7:[Omitted long matching line]
docs/paper/sections/experiments.tex:77:[Omitted long matching line]
docs/paper/sections/experiments.tex:81:[Omitted long matching line]
docs/paper/sections/experiments.tex:86:\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
docs/paper/sections/experiments.tex:87:\label{fig:window_ablation}
docs/paper/sections/discussion.tex:7:[Omitted long matching line]
docs/paper/sections/discussion.tex:10:[Omitted long matching line]
docs/paper/sections/discussion.tex:13:[Omitted long matching line]
docs/paper/sections/method.tex:35:\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select per-model on validation. GRU sequence models are also evaluated (\cref{app:gru_details}).
docs/paper/sections/limitations.tex:4:Only $W{=}1$ passes Bonferroni correction for R1-32B, with only 25\% trace coverage (5 of 20 test traces detected). The dimensionality constraint of $51200 \times W$ features for $n{=}20$ traces prevents reliable evaluation at larger window sizes. Whether collecting more training traces would resolve this statistical limitation remains unknown.
docs/paper/sections/abstract.tex:1:[Omitted long matching line]
docs/paper/sections/appendix.tex:63:\label{app:window_ablation}
docs/paper/sections/appendix.tex:65:\cref{tab:window_full} reports the complete window size ablation across all four models and seven window sizes. The main text (\cref{sec:temporal}) presents R1-8B results; here we provide the full data.
docs/paper/sections/appendix.tex:71:\label{tab:window_full}
docs/paper/sections/appendix.tex:116:Key cross-model patterns emerge from the window ablation:
docs/paper/sections/appendix.tex:120:[Omitted long matching line]
docs/paper/sections/appendix.tex:122:\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\%) and highest precision (60.9\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).
docs/paper/sections/appendix.tex:124:\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
docs/paper/sections/appendix.tex:126:\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.
docs/paper/sections/appendix.tex:129:\label{app:text_window}
docs/paper/sections/appendix.tex:131:\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
docs/paper/sections/appendix.tex:135:\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
docs/paper/sections/appendix.tex:136:\label{tab:text_window}
docs/paper/sections/appendix.tex:152:[Omitted long matching line]
docs/paper/sections/appendix.tex:158:OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
docs/paper/sections/appendix.tex:186:\paragraph{Text probe window ablation.}
docs/paper/sections/appendix.tex:191:\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}
docs/paper/sections/appendix.tex:192:\label{tab:ot7b_text_window}
docs/paper/sections/appendix.tex:208:OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
docs/paper/sections/appendix.tex:384:We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window ($W_{\text{screen}}$) to flag candidate unsafe segments, followed by a longer confirmation window ($W_{\text{confirm}}$) applied only to flagged segments. A trace is classified as unsafe if at least $k$ steps exceed the threshold during the confirmation stage.
docs/paper/sections/appendix.tex:391:\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}
docs/paper/sections/appendix.tex:395:The marginal improvement suggests that fixed-window smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach adds configuration complexity (three hyperparameters vs. one) without proportional performance gain.
docs/paper/sections/appendix.tex:401:[Omitted long matching line]
docs/paper/main.aux:318:\@writefile{toc}{\contentsline {paragraph}{Temporal windowing.}{3}{section*.8}\protected@file@percent }
docs/paper/main.aux:515:\@writefile{lof}{\contentsline {figure}{\numberline {1}{\ignorespaces Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}}{5}{figure.caption.14}\protected@file@percent }
docs/paper/main.aux:516:\newlabel{fig:window_ablation}{{1}{5}{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%}{figure.caption.14}{}}
docs/paper/main.aux:517:\newlabel{fig:window_ablation@cref}{{[figure][1][]1}{[1][5][]5}{}{}{}}
docs/paper/main.aux:1157:\newlabel{app:window_ablation}{{D}{11}{Window Size Ablation Details}{appendix.D}{}}
docs/paper/main.aux:1158:\newlabel{app:window_ablation@cref}{{[section][4][]D}{[1][11][]11}{}{}{}}
docs/paper/main.aux:1182:\newlabel{tab:window_full}{{7}{11}{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models}{table.caption.33}{}}
docs/paper/main.aux:1183:\newlabel{tab:window_full@cref}{{[table][7][]7}{[1][11][]11}{}{}{}}
docs/paper/main.aux:1228:\newlabel{app:text_window}{{D.1}{12}{Text Probe Window Ablation}{subsection.D.1}{}}
docs/paper/main.aux:1229:\newlabel{app:text_window@cref}{{[subsection][1][4]D.1}{[1][12][]12}{}{}{}}
docs/paper/main.aux:1234:\@writefile{lot}{\contentsline {table}{\numberline {8}{\ignorespaces Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}}{12}{table.caption.39}\protected@file@percent }
docs/paper/main.aux:1235:\newlabel{tab:text_window}{{8}{12}{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline}{table.caption.39}{}}
docs/paper/main.aux:1236:\newlabel{tab:text_window@cref}{{[table][8][]8}{[1][12][]12}{}{}{}}
docs/paper/main.aux:1271:\@writefile{lot}{\contentsline {table}{\numberline {10}{\ignorespaces OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}}{12}{table.caption.43}\protected@file@percent }
docs/paper/main.aux:1272:\newlabel{tab:ot7b_text_window}{{10}{12}{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$}{table.caption.43}{}}
docs/paper/main.aux:1273:\newlabel{tab:ot7b_text_window@cref}{{[table][10][]10}{[1][12][]12}{}{}{}}
docs/paper/main.aux:1274:\@writefile{toc}{\contentsline {paragraph}{Text probe window ablation.}{12}{table.caption.43}\protected@file@percent }
docs/paper/main.aux:1625:[Omitted long matching line]
docs/paper/main.aux:1626:\newlabel{fig:pareto_two_stage}{{2}{16}{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text {screen}}{=}3$, $W_{\text {confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss}{figure.caption.66}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ce28c72-0b46-4422-95cb-fed886ab0617",
  "isSidechain": true,
  "promptId": "fdc0542e-b5c3-4ed1-8bde-065d1e5a0b6e",
  "agentId": "ac17197ed6a690836",
  "type": "user",
  "uuid": "1f12f682-1ba5-404d-9836-1221e8d46df4",
  "sourceToolAssistantUUID": "6ce28c72-0b46-4422-95cb-fed886ab0617",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-18T03:30:11.321Z_

Good, I found some key information. Now let me read the specific tex files to get the full Table 2 definition and more complete context:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f12f682-1ba5-404d-9836-1221e8d46df4",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9Ku6i7by9iFA9H3RqbA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "74b41575-fe6d-42b1-875b-8db3460e6dd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sm4FANJWmUFJf3Zc1hfnGH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11602,
      "cache_read_input_tokens": 16717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11602,
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

_source line 13 · 2026-05-18T03:30:12.105Z_

<details open><summary>🔧 Tool call — Read · `toolu_019EDM2EzbMhHpGKQptHmyZt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74b41575-fe6d-42b1-875b-8db3460e6dd4",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9Ku6i7by9iFA9H3RqbA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b83cbf02-9c83-4de8-aa75-6f8f1bb355a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sm4FANJWmUFJf3Zc1hfnGH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11602,
      "cache_read_input_tokens": 16717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11602,
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

_source line 14 · 2026-05-18T03:30:12.114Z_

<details><summary>↩ Tool result · `toolu_019EDM2EzbMhHpGKQptHmyZt`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.
4	
5	\subsection{Setup}\label{sec:setup}
6	
7	We study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \in \{1, 3, 5, 10, 15, 20, 25\}$ selected on validation. Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use a two-sided null-centered bootstrap (1000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence.
8	
9	\subsection{Layer Selection Results}\label{sec:layer-results}
10	
11	\cref{tab:layer_selection} shows that the biased composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B and L10 (16\%) for R1-32B. Four unbiased metrics (pure balanced accuracy, precision, inverse FPR, additive composite) converge on deep layers: L60 (94\%) and L63 (98\%). Metrics from two measurement families (accuracy-based and false-positive-based) agree. The mechanism is that shallow layers produce more volatile representations, inflating crossing rate independently of discriminative power (\cref{sec:layer-sensitivity}).
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\begin{tabular}{lccc}
17	\toprule
18	\textbf{Model} & \textbf{Biased}$^a$ & \textbf{Corrected}$^b$ & $p$ \textbf{(corr.)} \\
19	\midrule
20	R1-8B & L14 (44\%) & L14 (44\%) & ${<}0.001$ \\
21	OT-7B & L0 (0\%) & L16 (57\%) & ${<}0.001$ \\
22	QwQ-32B & L2 (3\%) & L60 (94\%) & ${<}0.005$ \\
23	R1-32B & L10 (16\%) & L63 (98\%) & ${<}0.001$ \\
24	\bottomrule
25	\end{tabular}
26	\caption{Layer selection sensitivity. $^a$\,bal\_acc $\times$ crossing\_rate. $^b$\,Consensus of four unbiased metrics. Rightmost: HS vs.\ text precision $p$-value at corrected layer. At biased layers, 32B $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ), both non-significant.}
27	\label{tab:layer_selection}
28	\end{table}
29	
30	The downstream impact is severe: at biased layers, only 5/12 tests survive Holm-Bonferroni correction (all from 7--8B models unaffected by the bias). At corrected layers, all 12 pass. Had we reported only biased-layer results, we would have concluded a scale-dependent HS advantage that is entirely a methodological artifact.
31	
32	\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\setlength{\tabcolsep}{4pt}
38	\begin{tabular}{llcrrrr}
39	\toprule
40	\textbf{Model} & \textbf{Layer} & $W$ & $\Delta$\textbf{BA} & $\Delta$\textbf{Prec} & $\Delta$\textbf{FPR} & \textbf{HB} \\
41	\midrule
42	R1-8B & L14 & 15 & +8.2 & +22.4 & $-$7.4 & 3/3 \\
43	OT-7B & L16 & 3 & +10.7 & +21.9 & $-$17.1 & 3/3 \\
44	QwQ & L60 & 3 & +15.4 & \textbf{+23.6} & $-$9.8 & 3/3 \\
45	R1-32B & L63 & 1 & \textbf{+18.7} & +15.4 & \textbf{$-$14.6} & 3/3 \\
46	\bottomrule
47	\end{tabular}
48	\caption{HS vs.\ text at corrected layers. $\Delta$: HS$-$text difference (pp). HB: Holm-Bonferroni pass count ($\alpha{=}0.05$, 12 tests). Bootstrap: 1000 resamples, two-sided null-centered.}
49	\label{tab:hs_vs_text}
50	\end{table}
51	
52	HS probes significantly outperform text probes on all four models across all three metrics (\cref{tab:hs_vs_text}). Precision gains range from +15.4pp (R1-32B) to +23.6pp (QwQ-32B). The advantage is consistent across architectures (Llama vs.\ Qwen) and training methods (R1 distillation vs.\ STILL). Control task selectivity confirms genuine safety signal: 12.5--19.7pp above chance across all models (\cref{app:control}).
53	
54	\paragraph{Dimensionality control.} PCA reduction of HS features to 384d (matching text encoder dimensionality, 79--92\% variance retained) preserves the precision advantage on all four models (+16.8 to +23.1pp, all $p{<}0.012$), with 10/12 Holm-Bonferroni tests passing. This confirms a modality effect rather than a capacity artifact. As a complementary robustness check, we replace MiniLM (384d) with BGE-large (1024d, a 2.7$\times$ stronger encoder). The HS advantage persists directionally on all four models and remains significant for OT-7B (+18.1pp, $p{<}0.001$); effect sizes narrow for the remaining models, consistent with the prediction in our Limitations that stronger encoders would reduce the gap (\cref{app:encoder_robustness}).
55	
56	\paragraph{Caveats.} R1-32B achieves significance only at $W{=}1$ with 25\% coverage (5/20 traces); at $W{\geq}3$, dimensionality ($51200 \times W$ for $n{=}20$) prevents significance. QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps vs.\ text 3.7--12.3 steps): higher precision at later detection. On benign traces, probes produce 39--52\% false alarm rates, indicating that current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in \cref{sec:32b-analysis}.
57	
58	\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
59	
60	R1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (\cref{tab:32b_divergence}), making training method the likely differentiator.
61	
62	\begin{table}[t]
63	\centering
64	\small
65	\begin{tabular}{lcccc}
66	\toprule
67	\textbf{Model} & \textbf{Cov.} & \textbf{Lead (steps)} & \textbf{HB} & \textbf{Pos.\ margin} \\
68	\midrule
69	R1-32B & 25\% & +11.7 to +13.3 & 3/3 ($W{=}1$) & +14.2pp \\
70	QwQ-32B & 74\% & $-$1.2 to +1.9 & 3/3 (all $W$) & $-$0.6pp \\
71	\bottomrule
72	\end{tabular}
73	\caption{32B cross-model divergence. R1-32B provides early warning with narrow coverage; QwQ-32B provides robust significance with poor lead time. Pos.\ margin: HS balanced accuracy minus position-only baseline.}
74	\label{tab:32b_divergence}
75	\end{table}
76	
77	R1-32B detects commitment 11--13 steps early with a +14.2pp margin over the position baseline, confirming genuine representational signal, but covers only 25\% of traces at the single significant window ($W{=}1$). QwQ-32B achieves statistical significance at all window sizes with 74\% coverage, but HS probes fire later than text probes (negative lead time) and the position baseline is competitive ($-$0.6pp). The divergence implies that per-model validation is essential: no single detection configuration generalizes even within the same architecture at the same scale, and a system validated on one 32B model would fail on the other.
78	
79	\subsection{Temporal Context}\label{sec:temporal}
80	
81	Temporal windowing ($W{>}1$) improves both modalities on all four models (\cref{fig:window_ablation}). Text precision improves +8 to +23pp from $W{=}1$ to $W{=}25$; HS precision improves +1.7 to +12.9pp. At 7--8B, the modality advantage (+22pp precision) exceeds the temporal improvement (+13pp). Both effects are complementary: the most robust deployment default is temporal windowing ($W{=}3$--$15$) combined with principled layer selection. Full per-model temporal ablations appear in \cref{app:temporal_details}.
82	
83	\begin{figure}[t]
84	\centering
85	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
86	\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
87	\label{fig:window_ablation}
88	\end{figure}
89	
90	\subsection{Negative Results}\label{sec:negative}
91	
92	\begin{table}[t]
93	\centering
94	\small
95	\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}
96	\toprule
97	\textbf{Method} & \textbf{Result} & \textbf{Limitation} \\
98	\midrule
99	BOCPD & 0\% det.\ on 3/4 models & Commitment gradual \\
100	CUSUM & $<$ threshold, all models & Same as BOCPD \\
101	Mahalanobis & $\Delta d \approx 0$ & Signal in minor PCs \\
102	RepE & QwQ 0.756; R1-32B 0.559$^a$ & Model-dependent \\
103	MLP & 3/4 worse than LR & Overfitting \\
104	CCS & No gain over supervised$^b$ & Alignment mismatch \\
105	Transfer & Best 59.5\% (PCA)$^c$ & Model-specific repr. \\
106	\bottomrule
107	\end{tabular}
108	\caption{Seven alternative approaches. $^a$\,RepE QwQ approaches supervised bal\_acc but precision is 0.512 vs.\ LR 0.700. $^b$\,Semi-supervised (requires CP labels). $^c$\,Best direct transfer 67.3\% but 1\% crossing rate.}
109	\label{tab:negative}
110	\end{table}
111	
112	Seven alternative methods produce inconsistent or limited results (\cref{tab:negative}). We prioritize precision over balanced accuracy as the primary evaluation criterion because false positives on pre-CP steps waste intervention resources (triggering unnecessary safety responses), while missed post-CP steps merely reduce coverage without causing immediate harm. This framing is critical for interpreting RepE results below.
113	
114	\paragraph{Change-point methods.} BOCPD~\citep{adams2007bayesian} achieves 0\% detection on 3/4 models because safety commitment is gradual rather than abrupt: the probe score sequence transitions smoothly over 5--15 steps without the discontinuity that BOCPD's hazard function requires. On R1-8B (the sole model with non-zero detection), the best BOCPD configuration ($\lambda{=}10$) achieves 93\% detection rate but with lower lead time (+3.5 steps) than simple thresholding (+4.9 steps). CUSUM similarly fails because cumulative evidence never exceeds the decision boundary on smooth transitions. The gradual nature of commitment is itself an empirical finding: it rules out the entire class of abrupt-change detectors and motivates the supervised probe approach that explicitly learns the transition boundary.
115	
116	\paragraph{RepE inconsistency.} RepE mean-difference directions~\citep{zou2023representation} illustrate why balanced accuracy alone is misleading. On QwQ-32B, RepE achieves 0.756 balanced accuracy (approaching supervised LR at 0.778), but its precision is 0.512 vs.\ LR 0.700 and its FPR is 0.309 vs.\ 0.120. The mean-difference direction captures enough signal to classify steps above chance, but fires indiscriminately on pre-CP steps, producing 2.6$\times$ more false alarms than supervised probes. On R1-32B, RepE nearly fails entirely (0.559 balanced accuracy). The inconsistency across two models sharing the same architecture confirms that a single linear direction computed from class means does not reliably capture safety commitment structure.
117	
118	Cross-model transfer produces no practical utility across 17 configurations; stronger alignment methods (CCA, model stitching~\cite{kornblith2019cka,bansal2021stitching}) remain unexplored. Detailed per-method analysis in \cref{app:negative_details}.
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b83cbf02-9c83-4de8-aa75-6f8f1bb355a7",
  "isSidechain": true,
  "promptId": "fdc0542e-b5c3-4ed1-8bde-065d1e5a0b6e",
  "agentId": "ac17197ed6a690836",
  "type": "user",
  "uuid": "6aa9f0da-67a0-494f-a938-85cabf7a5bce",
  "sourceToolAssistantUUID": "b83cbf02-9c83-4de8-aa75-6f8f1bb355a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T03:30:12.454Z_

<details open><summary>🔧 Tool call — Read · `toolu_018UvE4XaD8yK6WSguKiGXer`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aa9f0da-67a0-494f-a938-85cabf7a5bce",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9Ku6i7by9iFA9H3RqbA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cc1a8cb9-6f64-424e-a5ce-8ec8c27709d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sm4FANJWmUFJf3Zc1hfnGH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11602,
      "cache_read_input_tokens": 16717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11602,
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

_source line 16 · 2026-05-18T03:30:12.465Z_

<details><summary>↩ Tool result · `toolu_018UvE4XaD8yK6WSguKiGXer`</summary>

```text
1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Steps before CP are \emph{pre-commitment} ($y_t = 0$); steps at or after CP are \emph{post-commitment} ($y_t = 1$). The detection task produces a score $s_t \in [0, 1]$ estimating whether the model has passed its CP by step $t$.
8	
9	We study four reasoning models spanning two architectures and two scales (\cref{tab:models}).
10	
11	\begin{table}[t]
12	\centering
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{lccccc}
15	\toprule
16	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{$n$ (total\,/\,test)} \\
17	\midrule
18	R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
19	OT-7B & Qwen & 7B & 28 & 3584 & 228\,/\,47 \\
20	R1-32B & Qwen & 32B & 64 & 5120 & 100\,/\,20 \\
21	QwQ-32B & Qwen & 32B & 64 & 5120 & 95\,/\,19 \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}
25	\label{tab:models}
26	\end{table}
27	
28	\subsection{Probe Architecture}
29	\label{sec:probe-architecture}
30	
31	\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ from layer $\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\_iter${}=2000$) on binary CP labels. Layer selection is analyzed in \cref{sec:layer-sensitivity}.
32	
33	\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2 ($\mathbb{R}^{384}$). The same logistic regression is applied, providing a surface-level modality baseline.
34	
35	\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select per-model on validation. GRU sequence models are also evaluated (\cref{app:gru_details}).
36	
37	\subsection{Layer Selection Sensitivity}
38	\label{sec:layer-sensitivity}
39	
40	Layer selection is a researcher degree of freedom that can reverse modality comparison conclusions. A composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B, L10 (16\%) for R1-32B. The mechanism is that shallow layers produce more volatile representations, inflating crossing rate independently of discriminative power.
41	
42	A five-metric ablation reveals that four metrics from two measurement families (accuracy-based and false-positive-based) converge on deep layers: L60 (94\%) for QwQ-32B, L63 (98\%) for R1-32B. At these layers, all 12 Holm-Bonferroni tests pass; at biased layers, only 5/12 survive correction. Full per-layer results appear in \cref{app:layer_sweep}.
43	
44	\subsection{Baseline Methods}
45	\label{sec:baselines}
46	
47	We evaluate seven alternatives to contextualize probe performance (\cref{tab:negative}): BOCPD~\citep{adams2007bayesian} and CUSUM for change-point detection; Mahalanobis distance following TrajGuard~\citep{trajguard}; RepE mean-difference directions~\citep{zou2023representation}; two-layer MLP probes; CCS-adapted~\citep{burns2023discovering}; and cross-model transfer via PCA. A position-only baseline ($t/T$) controls for temporal artifacts. Detailed configurations in \cref{app:bocpd_config,app:transfer_details}.
48	
49	\subsection{Evaluation Protocol}
50	\label{sec:evaluation}
51	
52	We report balanced accuracy, precision, pre-CP FPR (step-level and trace-level), coverage, and lead time (steps between first detection and true CP). Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use two-sided null-centered bootstrap (1000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\citep{hewitt2019control} validates genuine representational structure (\cref{app:control}).
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc1a8cb9-6f64-424e-a5ce-8ec8c27709d3",
  "isSidechain": true,
  "promptId": "fdc0542e-b5c3-4ed1-8bde-065d1e5a0b6e",
  "agentId": "ac17197ed6a690836",
  "type": "user",
  "uuid": "b5801231-dabd-4627-976f-1d802acbd14f",
  "sourceToolAssistantUUID": "cc1a8cb9-6f64-424e-a5ce-8ec8c27709d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T03:30:12.597Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UnKAv6RhDaKSAGBQogemjs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "limit": 450
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5801231-dabd-4627-976f-1d802acbd14f",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9Ku6i7by9iFA9H3RqbA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ac19437-0eb4-4a69-8eba-4df7feb5e9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sm4FANJWmUFJf3Zc1hfnGH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 11602,
      "cache_read_input_tokens": 16717,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11602
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 288,
          "cache_read_input_tokens": 16717,
          "cache_creation_input_tokens": 11602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11602,
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

_source line 18 · 2026-05-18T03:30:12.960Z_

<details><summary>↩ Tool result · `toolu_01UnKAv6RhDaKSAGBQogemjs`</summary>

```text
1	\appendix
2	
3	\section{Responsible NLP Research Checklist}
4	\label{app:checklist}
5	
6	We address the ARR Responsible NLP Research requirements below.
7	
8	\begin{itemize}
9	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
10	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark.
11	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
12	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
13	    \item \textbf{Human subjects:} No human subjects research was conducted.
14	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
15	\end{itemize}
16	
17	
18	\section{Layer Sweep Results}
19	\label{app:layer_sweep}
20	
21	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. The four unbiased metrics converge on deep layers for all models.
22	
23	\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\% depth). OT-7B: biased metric selects L0 (0\%), unbiased consensus selects L16 (57\%). QwQ-32B: biased metric selects L2 (3\%), unbiased consensus selects L60 (94\%). R1-32B: biased metric selects L10 (16\%), unbiased consensus selects L63 (98\%). The bias is most extreme for 64-layer models, where the composite metric selects layers in the bottom 16\% of the network while all other metrics select layers above 94\%.
24	
25	\paragraph{Impact on modality comparison.} At the biased layers, HS vs.\ text precision $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant. At the corrected deep layers, all $p$-values fall below 0.005. The initially reported ``scale-dependent'' pattern (HS advantage at 7--8B but not 32B) was entirely an artifact of layer selection methodology, not a genuine property of model scale (\cref{sec:layer-results}).
26	
27	
28	\section{Holm-Bonferroni Step-Down Correction}
29	\label{app:holm_bonferroni}
30	
31	\cref{tab:holm_bonferroni} reports the full 12-test battery used to assess hidden-state superiority over text probes across all four models. Tests are ranked by $p$-value; each test $i$ (rank $i$ of $m{=}12$) must satisfy $p_i < \alpha / (m - i + 1)$ under the step-down procedure. All 12 tests pass at $\alpha{=}0.05$, controlling the family-wise error rate.
32	
33	\begin{table}[h]
34	\centering
35	\small
36	\caption{Holm-Bonferroni step-down correction for 12 hypothesis tests (4 models $\times$ 3 metrics). Each test uses a two-sided null-centered bootstrap (1000 resamples) on trace-level metric differences (HS minus text). All tests pass at $\alpha{=}0.05$.}
37	\label{tab:holm_bonferroni}
38	\setlength{\tabcolsep}{4pt}
39	\begin{tabular}{clllcc}
40	\toprule
41	\textbf{Rank} & \textbf{Model} & \textbf{Metric} & \textbf{$p$-val} & \textbf{Thresh.} & \textbf{Pass} \\
42	\midrule
43	1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \checkmark \\
44	2  & OT-7B  & Bal.\ Acc. & $<$0.001 & 0.0045 & \checkmark \\
45	3  & OT-7B  & Precision & $<$0.001 & 0.0050 & \checkmark \\
46	4  & OT-7B  & FPR & $<$0.001 & 0.0056 & \checkmark \\
47	5  & QwQ-32B & Bal.\ Acc. & $<$0.001 & 0.0063 & \checkmark \\
48	6  & QwQ-32B & Precision & $<$0.001 & 0.0071 & \checkmark \\
49	7  & R1-32B & Bal.\ Acc. & $<$0.001 & 0.0083 & \checkmark \\
50	8  & R1-32B & Precision & $<$0.001 & 0.0100 & \checkmark \\
51	9  & QwQ-32B & FPR & 0.004 & 0.0125 & \checkmark \\
52	10 & R1-8B  & Bal.\ Acc. & 0.005 & 0.0167 & \checkmark \\
53	11 & R1-32B & FPR & 0.007 & 0.0250 & \checkmark \\
54	12 & R1-8B  & FPR & 0.044 & 0.0500 & \checkmark \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B showing the largest precision gap (+22.4pp). This reflects R1-8B's already-low text FPR (11.8\%), which leaves less room for HS improvement on this metric.
60	
61	
62	\section{Window Size Ablation Details}
63	\label{app:window_ablation}
64	
65	\cref{tab:window_full} reports the complete window size ablation across all four models and seven window sizes. The main text (\cref{sec:temporal}) presents R1-8B results; here we provide the full data.
66	
67	\begin{table}[h]
68	\centering
69	\small
70	\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}
71	\label{tab:window_full}
72	\resizebox{\columnwidth}{!}{%
73	\begin{tabular}{llccccc}
74	\toprule
75	Model & $W$ & Bal.\ Acc. & Precision & FPR$_{\text{step}}$ & Coverage & Lead \\
76	\midrule
77	\multirow{7}{*}{R1-8B}
78	 & 1  & 77.8 & 69.3 & 9.65 & 72.1 & 13.8 \\
79	 & 3  & 79.0 & 72.3 & 8.50 & 69.8 & 12.1 \\
80	 & 5  & 78.1 & 72.6 & 8.09 & 65.1 & 8.3 \\
81	 & 10 & 79.3 & 74.3 & 7.61 & 55.8 & 10.0 \\
82	 & 15 & 80.2 & 77.7 & 6.39 & 51.2 & 7.2 \\
83	 & 20 & 80.7 & 78.6 & 6.12 & 53.5 & 7.4 \\
84	 & 25 & 81.0 & 82.2 & 4.83 & 48.8 & 8.1 \\
85	\midrule
86	\multirow{7}{*}{OT-7B}
87	 & 1  & 68.2 & 42.8 & 12.0 & 53.2 & 16.1 \\
88	 & 3  & \textbf{68.8} & 46.6 & 10.0 & 53.2 & 21.6 \\
89	 & 5  & 68.1 & 46.4 & 9.9 & 53.2 & 21.7 \\
90	 & 10 & 66.5 & 46.9 & 8.6 & 48.9 & 25.0 \\
91	 & 15 & 66.4 & 48.8 & 7.7 & 44.7 & 39.6 \\
92	 & 20 & 66.0 & \textbf{49.4} & \textbf{7.5} & 48.9 & 17.9 \\
93	 & 25 & 65.9 & 48.9 & 8.0 & 51.1 & 28.3 \\
94	\midrule
95	\multirow{7}{*}{R1-32B}
96	 & 1  & 71.8 & 54.9 & 32.03 & 80.0 & 12.9 \\
97	 & 3  & 72.5 & 56.0 & 30.64 & 80.0 & 11.4 \\
98	 & 5  & 73.1 & 57.5 & 28.41 & 75.0 & 11.1 \\
99	 & 10 & 73.7 & 60.9 & 23.40 & 70.0 & 10.8 \\
100	 & 15 & 72.1 & 59.1 & 24.51 & 70.0 & 10.9 \\
101	 & 20 & 69.6 & 56.3 & 26.18 & 65.0 & 9.6 \\
102	 & 25 & 70.3 & 56.6 & 26.46 & 70.0 & 10.7 \\
103	\midrule
104	\multirow{7}{*}{QwQ-32B}
105	 & 1  & 73.0 & 54.4 & 22.76 & 79.0 & 19.7 \\
106	 & 3  & 74.5 & 56.5 & 21.41 & 73.7 & 20.6 \\
107	 & 5  & 76.1 & 57.3 & 21.68 & 73.7 & 20.1 \\
108	 & 10 & 74.7 & 57.1 & 20.73 & 73.7 & 18.4 \\
109	 & 15 & 74.1 & 58.2 & 19.11 & 68.4 & 15.8 \\
110	 & 20 & 75.4 & 60.2 & 17.89 & 63.2 & 15.8 \\
111	 & 25 & 76.2 & 61.8 & 16.94 & 57.9 & 14.9 \\
112	\bottomrule
113	\end{tabular}}%
114	\end{table}
115	
116	Key cross-model patterns emerge from the window ablation:
117	
118	\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\% ($W{=}1$) to 81.0\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\% to 4.83\%). Coverage trades off against quality, dropping from 72.1\% to 48.8\%.
119	
120	\paragraph{OT-7B} exhibits a split temporal pattern at layer 16: balanced accuracy peaks at $W{=}3$ (68.8\%) and declines at larger windows ($-$2.9pp by $W{=}25$), while precision and FPR continue improving. Precision rises from 42.8\% ($W{=}1$) to 49.4\% ($W{=}20$), and FPR drops from 12.0\% to 7.5\% over the same range. The split indicates that larger windows reduce false alarms and sharpen positive predictions even as overall classification accuracy degrades. Lead times are shorter than old layer-0 estimates (16.1--39.6 steps) due to the corrected layer selection (\cref{app:ot7b_details}). OT-7B text probes improve monotonically across all metrics (\cref{app:ot7b_details}), so the accuracy saturation is specific to HS probes on this model.
121	
122	\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\%) and highest precision (60.9\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).
123	
124	\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
125	
126	\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.
127	
128	\subsection{Text Probe Window Ablation}
129	\label{app:text_window}
130	
131	\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
132	
133	\begin{table}[h]
134	\centering
135	\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
136	\label{tab:text_window}
137	\begin{tabular}{lcccc}
138	\toprule
139	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
140	\midrule
141	 1  & 64.7 & 41.6 & 25.8 & 95.4 \\
142	 3  & 66.9 & 44.8 & 23.1 & 90.7 \\
143	 5  & 69.2 & 48.5 & 20.4 & 84.9 \\
144	 10 & 72.1 & 54.3 & 16.7 & 74.4 \\
145	 15 & 74.3 & 58.9 & 14.2 & 67.4 \\
146	 20 & 75.8 & 62.1 & 12.5 & 62.8 \\
147	 25 & 76.7 & 64.8 & 11.8 & 58.1 \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	Text probes show monotonic improvement across all window sizes without the plateau observed in HS probes (which saturate around $W{=}15$). The absolute FPR reduction ($-$14.0pp) is nearly three times the HS reduction ($-$4.8pp), and accuracy gains (+12.0pp vs.\ +3.2pp) are four times larger. This asymmetry supports the interpretation that temporal context is the primary factor in commitment detection: text features, which encode less information per step, benefit proportionally more from observing the multi-step progression.
153	
154	
155	\section{OpenThinker-7B Detailed Results}
156	\label{app:ot7b_details}
157	
158	OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
159	
160	\paragraph{Layer sweep.}
161	
162	\begin{table}[h]
163	\centering
164	\small
165	\caption{OT-7B layer sweep. Score = balanced accuracy $\times$ crossing rate. Layer 16 (57\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}
166	\label{tab:ot7b_layer_sweep}
167	\setlength{\tabcolsep}{4pt}
168	\begin{tabular}{lcccc}
169	\toprule
170	Layer & Depth & Bal.\ Acc. & Cross.\ Rate & Score \\
171	\midrule
172	0 (embed.) & 0 & 66.7 & 53.2 & 35.5 \\
173	4 & 14 & 66.3 & 40.4 & 26.8 \\
174	8 & 29 & 66.4 & 25.5 & 17.0 \\
175	12 & 43 & 67.5 & 31.9 & 21.6 \\
176	16 & 57 & 68.2 & 31.9 & 21.8 \\
177	20 & 71 & 65.5 & 31.9 & 20.9 \\
178	24 & 86 & 66.9 & 29.8 & 19.9 \\
179	27 & 96 & 63.0 & 31.9 & 20.1 \\
180	\bottomrule
181	\end{tabular}
182	\end{table}
183	
184	After correction of a layer selection bug, layer 16 (57\% depth) is selected. It achieves the highest balanced accuracy (68.2\%) among transformer layers and is consistent with the mid-depth pattern of R1-8B (44\%). Layer 0 (embedding) has a higher crossing rate (53.2\% vs.\ 31.9\%) but lower accuracy.
185	
186	\paragraph{Text probe window ablation.}
187	
188	\begin{table}[h]
189	\centering
190	\small
191	\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}
192	\label{tab:ot7b_text_window}
193	\begin{tabular}{lcccc}
194	\toprule
195	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
196	\midrule
197	 1  & 58.1 & 24.5 & 34.5 & 63.8 \\
198	 3  & 57.9 & 25.4 & 27.1 & 74.5 \\
199	 5  & 56.9 & 24.7 & 25.5 & 70.2 \\
200	 10 & 58.3 & 27.0 & 22.2 & 70.2 \\
201	 15 & 58.9 & 28.3 & 20.0 & 66.0 \\
202	 20 & 60.9 & 31.6 & 17.6 & 66.0 \\
203	 25 & 61.4 & 32.9 & 16.1 & 66.0 \\
204	\bottomrule
205	\end{tabular}
206	\end{table}
207	
208	OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
209	
210	\paragraph{Bootstrap comparison (matched $W{=}3$).} To ensure a fair modality comparison, bootstrap tests use matched $W{=}3$ for both HS and text probes. At $W{=}3$, HS probes achieve 75.3\% trace-level balanced accuracy vs.\ 65.6\% for text (bootstrap $\Delta{=}$+10.7pp, 95\% CI [4.9, 16.3], $p{<}0.001$, survives Holm-Bonferroni). Precision: 55.8\% vs.\ 34.6\% (bootstrap $\Delta{=}$+21.9pp, 95\% CI [14.0, 29.6], $p{<}0.001$, survives Holm-Bonferroni). Pre-CP FPR: 10.0\% vs.\ 27.1\% (bootstrap $\Delta{=}{-}17.1$pp, 95\% CI [$-$22.2, $-$12.2], $p{<}0.001$, survives Holm-Bonferroni). All three metrics survive correction. The point-estimate precision gap (+21.2pp) closely matches R1-8B (+22.4pp); the bootstrap mean (+21.9pp) differs slightly due to resampling variance. Using each modality's optimal $W$ (HS at $W{=}3$, text at $W{=}25$) would introduce a confound because text would benefit from 8$\times$ more temporal context.
211	
212	
213	\section{GRU Training Details}
214	\label{app:gru_details}
215	
216	\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes.
217	
218	\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
219	
220	\paragraph{Training procedure.} We train with Adam (learning rate $1 \times 10^{-3}$, default $\beta_1{=}0.9$, $\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.
221	
222	\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\pm$ standard deviation.
223	
224	\paragraph{Per-seed results for R1-8B (single-layer GRU).}
225	
226	\begin{table}[h]
227	\centering
228	\small
229	\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}
230	\label{tab:gru_seeds}
231	\setlength{\tabcolsep}{4pt}
232	\begin{tabular}{lccc}
233	\toprule
234	Seed & Peak Acc. & Crossing Acc. & Lead (steps) \\
235	\midrule
236	1 & 85.2 & 74.3 & +4.8 \\
237	2 & 83.1 & 71.6 & +4.8 \\
238	3 & 83.4 & 70.4 & +0.9 \\
239	\midrule
240	Mean $\pm$ std & 83.9 $\pm$ 1.1 & 72.1 $\pm$ 2.0 & +3.5 $\pm$ 2.3 \\
241	\bottomrule
242	\end{tabular}
243	\end{table}
244	
245	The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.
246	
247	\paragraph{Multi-layer GRU and baseline comparison (60/20/20 protocol).}
248	
249	\begin{table}[h]
250	\centering
251	\scriptsize
252	\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}
253	\label{tab:gru_multi_seeds}
254	\resizebox{\columnwidth}{!}{%
255	\begin{tabular}{llccccc}
256	\toprule
257	Model & Seed & Acc & Prec & FPR & Cross.\% & Lead \\
258	\midrule
259	GRU-single & 42  & 0.845 & 0.657 & 0.139 & 72.1\% & 3.55 \\
260	GRU-single & 123 & 0.760 & 0.454 & 0.191 & 65.1\% & 7.39 \\
261	GRU-single & 456 & 0.792 & 0.474 & 0.203 & 67.4\% & 8.45 \\
262	\rowcolor{gray!10}
263	GRU-single & \textit{mean} & 0.799$\pm$0.035 & 0.528$\pm$0.091 & 0.178$\pm$0.028 & 68.2$\pm$2.9\% & 6.46$\pm$2.10 \\
264	\midrule
265	GRU-multi  & 42  & 0.824 & 0.616 & 0.164 & 74.4\% & 5.66 \\
266	GRU-multi  & 123 & 0.759 & 0.454 & 0.195 & 65.1\% & 6.43 \\
267	GRU-multi  & 456 & 0.784 & 0.460 & 0.207 & 65.1\% & 8.93 \\
268	\rowcolor{gray!10}
269	GRU-multi  & \textit{mean} & 0.789$\pm$0.027 & 0.510$\pm$0.075 & 0.189$\pm$0.018 & 68.2$\pm$4.4\% & 7.01$\pm$1.40 \\
270	\midrule
271	LR-single  & 42  & 0.841 & 0.693 & 0.097 & 46.5\% & $-$2.00 \\
272	LR-single  & 123 & 0.753 & 0.436 & 0.181 & 53.5\% & 5.26 \\
273	LR-single  & 456 & 0.814 & 0.512 & 0.146 & 41.9\% & 3.94 \\
274	\rowcolor{gray!10}
275	LR-single  & \textit{mean} & 0.803$\pm$0.037 & 0.547$\pm$0.108 & 0.141$\pm$0.035 & 47.3$\pm$4.8\% & 2.40$\pm$3.16 \\
276	\midrule
277	LR-multi   & 42  & 0.827 & 0.679 & 0.092 & 39.5\% & 1.06 \\
278	LR-multi   & 123 & 0.756 & 0.442 & 0.180 & 46.5\% & 7.30 \\
279	LR-multi   & 456 & 0.817 & 0.521 & 0.130 & 34.9\% & 4.00 \\
280	\rowcolor{gray!10}
281	LR-multi   & \textit{mean} & 0.800$\pm$0.032 & 0.547$\pm$0.099 & 0.134$\pm$0.036 & 40.3$\pm$4.8\% & 4.12$\pm$2.55 \\
282	\bottomrule
283	\end{tabular}}%
284	\end{table}
285	
286	Under this protocol, multi-layer GRU achieves the highest mean lead (7.01$\pm$1.40 steps) but at higher FPR than logistic regression baselines (0.189 vs.\ 0.134). The GRU advantage is concentrated in detection timing rather than classification accuracy, consistent with the main text finding that GRUs capture sequential dependencies that improve early detection. Lead time shows high variance across seeds (range 5.66--8.93 for GRU-multi), reinforcing that reported means should be interpreted cautiously.
287	
288	\paragraph{OT-7B multi-layer GRU (layers 13--19, 3 seeds).}
289	OT-7B GRU achieves 74.6$\pm$1.3\% balanced accuracy, 64.5$\pm$7.0\% coverage, +33.6$\pm$4.8 steps lead, and 27.4$\pm$6.1\% pre-CP FPR. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average ${\sim}$80 reasoning steps (vs.\ ${\sim}$30 for R1-8B and 32B models), so absolute lead times are not directly comparable. The FPR-lead tradeoff mirrors R1-8B: GRU FPR (27.4\%) is far above the LR probe at layer 16 (10.0\%), confirming that GRUs gain lead time at the cost of more false alarms across both 7-8B models.
290	
291	
292	\section{Control Task Methodology}
293	\label{app:control}
294	
295	We follow the selectivity framework of \cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.
296	
297	\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) across all steps while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:
298	\begin{equation}
299	    \text{Selectivity} = \text{Acc}_{\text{linguistic}} - \text{Acc}_{\text{control}}
300	\end{equation}
301	where $\text{Acc}_{\text{linguistic}}$ is the probe accuracy on true labels and $\text{Acc}_{\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information.
302	
303	\paragraph{Results.} We repeat the control experiment 5 times (10 for OT-7B) with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers are: R1-32B 19.7pp (layer 63), OT-7B 18.3pp (layer 16), QwQ-32B 14.4pp (layer 60), R1-8B 12.5pp (layer 14). All values exceed the 5pp threshold recommended by \cite{hewitt2019control}. R1-32B achieves the strongest selectivity (19.7pp) at the corrected layer, a 2.6$\times$ increase from 7.5pp at the biased layer L10. OT-7B achieves the second-highest selectivity at a mid-depth transformer layer (57\%), consistent with R1-8B's pattern at 44\% depth. On QwQ-32B, the position baseline accuracy (0.705) slightly exceeds the HS probe (0.667) at L60, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.
304	
305	\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 14.4pp at L60 (comparable to 15.3pp at L2), confirming that safety-specific signal persists at deep layers. R1-32B selectivity increases from 7.5pp at L10 to 19.7pp at L63, demonstrating that the corrected layer captures substantially more safety-relevant structure. The position baseline at L60 (0.705) still slightly exceeds the HS probe (0.667) for QwQ-32B, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.
306	
307	\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\% FPR compared to 8.1\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.
308	
309	
310	\section{Oracle Upper Bound Analysis}
311	\label{sec:oracle}
312	
313	We compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. This provides a theoretical ceiling on early detection performance.
314	
315	On R1-8B, the oracle achieves +31 steps mean lead time compared to +4.5 steps for the best learned probe (GRU), yielding an oracle gap of 85.5\%. This gap indicates that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. The learned probe captures the contemporaneous safety signal effectively (balanced accuracy 81--84\%) but cannot anticipate the commitment transition far in advance. Closing this gap will likely require causal intervention techniques (e.g., activation patching) rather than improvements to passive monitoring.
316	
317	
318	\section{BOCPD/CUSUM Configuration Sweep}
319	\label{app:bocpd_config}
320	
321	We sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.
322	
323	\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\lambda$ controls the prior probability of a change-point at each step ($P(\text{change}) = 1/\lambda$).
324	
325	\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.
326	
327	\begin{table}[h]
328	\centering
329	\small
330	\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}
331	\label{tab:cpd_sweep}
332	\setlength{\tabcolsep}{4pt}
333	\begin{tabular}{llcc}
334	\toprule
335	Method & Configuration & Det.\ Rate & Lead \\
336	\midrule
337	\multirow{5}{*}{BOCPD}
338	 & $\lambda = 5$   & 97 & +2.1 \\
339	 & $\lambda = 10$  & 93 & +3.5 \\
340	 & $\lambda = 20$  & 87 & +4.2 \\
341	 & $\lambda = 50$  & 72 & +5.8 \\
342	 & $\lambda = 100$ & 67.4 & +1.03 \\
343	\midrule
344	\multirow{10}{*}{CUSUM}
345	 & $\delta{=}0.3$, $h{=}3$ & 65.1 & +0.89 \\
346	 & $\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\
347	 & $\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\
348	 & $\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\
349	 & $\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\
350	 & $\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\
351	 & $\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\
352	 & $\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\
353	 & $\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\
354	 & $\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\
355	\midrule
356	Simple threshold & FCP baseline & 65.1 & +4.89 \\
357	\bottomrule
358	\end{tabular}
359	\end{table}
360	
361	The best BOCPD configuration ($\lambda{=}10$) achieves 93.0\% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1\% detection with superior lead (+4.89 steps). All CUSUM configurations underperform the simple threshold on lead time.
362	
363	These results reveal a coverage-timing tradeoff. BOCPD ($\lambda{=}10$) achieves 28pp higher detection rate than simple thresholding (93.0\% vs.\ 65.1\%), but with lower lead (+3.45 vs.\ +4.89 steps). The transition toward unsafe reasoning is gradual rather than abrupt, so change-point methods cannot exploit discontinuities for early warning. When missed detections are costly, BOCPD's coverage advantage justifies its use despite the timing penalty. When early intervention is the priority, simple thresholding provides better lead time.
364	
365	\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). The probe score sequences for these models show smoother transitions that never trigger the hazard function, consistent with the gradual commitment pattern. R1-8B's higher detection rate likely reflects its sharper probe score transitions at commitment boundaries.
366	
367	
368	\section{M002 Bug Disclosure}
369	\label{app:bug}
370	
371	We disclose a bug discovered during development that affected intermediate results for QwQ-32B.
372	
373	\paragraph{Issue.} In experiment M002 (text baseline evaluation), the QwQ-32B text probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive, producing a spuriously significant result ($p{=}0.001$ for HS vs. text FPR difference).
374	
375	\paragraph{Discovery and correction.} The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QwQ-32B and R1-32B modality comparisons at the originally selected layers (L2 and L10, chosen by the biased composite metric) showed no significant HS advantage: QwQ-32B accuracy $p{=}0.828$, precision $p{=}0.346$; R1-32B precision $p{=}0.050$ but no tests surviving Holm-Bonferroni. The subsequent discovery that these layer selections were themselves artifacts of metric bias (\cref{sec:layer-results}) led to the corrected-layer analysis reported in the main text, where all 12 tests pass Holm-Bonferroni at corrected deep layers (\cref{tab:hs_vs_text}).
376	
377	\paragraph{Impact on reported results.} All numbers reported in this paper use the corrected text embedding pipeline. The bug affected only QwQ-32B text probe features. The correction, combined with the separate layer selection correction (\cref{sec:layer-results}), means that early-stage intermediate results (non-significant 32B modality comparisons) reflected two compounding errors: incorrect text features and biased layer selection. Both are fully resolved in the final analysis.
378	
379	\paragraph{Commitment to transparency.} We report this bug to maintain scientific integrity. All code, including the git history showing the bug and its fix, will be released with the camera-ready version. Researchers reproducing our results can verify the correction independently.
380	
381	\section{Adaptive Two-Stage Detection}
382	\label{app:two_stage}
383	
384	We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window ($W_{\text{screen}}$) to flag candidate unsafe segments, followed by a longer confirmation window ($W_{\text{confirm}}$) applied only to flagged segments. A trace is classified as unsafe if at least $k$ steps exceed the threshold during the confirmation stage.
385	
386	We merge the validation and test partitions ($n{=}55$ total: 39 jailbreak, 16 benign) for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of $W_{\text{screen}} \in \{1, 3, 5\}$, $W_{\text{confirm}} \in \{10, 15, 20, 25\}$, and $k \in \{1, 3, 5\}$ on these R1-8B traces. \cref{fig:pareto_two_stage} shows the precision-coverage Pareto front for both methods. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) achieves 72.2\% precision at 76.9\% coverage, compared to 70.9\% precision at 76.9\% coverage for single-stage $W{=}15$. This +1.3pp precision gain at matched coverage represents a Pareto improvement, but the magnitude is marginal. At higher confirmation thresholds ($k{=}3$, $k{=}5$), two-stage detection trades coverage for small precision gains (up to 73.5\% precision at 38.5\% coverage with $k{=}5$), but these operating points are impractical due to excessive missed detections.
387	
388	\begin{figure}[h]
389	\centering
390	\includegraphics[width=0.85\columnwidth]{figures/pareto_two_stage.pdf}
391	\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}
392	\label{fig:pareto_two_stage}
393	\end{figure}
394	
395	The marginal improvement suggests that fixed-window smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach adds configuration complexity (three hyperparameters vs. one) without proportional performance gain.
396	
397	
398	\section{Temporal Ablation Details}
399	\label{app:temporal_details}
400	
401	Full per-model temporal ablations are reported in \cref{tab:window_full} (\cref{app:window_ablation}). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) with FPR halving (9.65\% to 4.83\%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at $W{=}3$ while precision and FPR continue improving at larger windows; (3) R1-32B peaks at $W{=}10$ then degrades, likely reflecting overfitting on the small dataset ($n{=}100$); (4) QwQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (\cref{app:text_window}) show monotonic improvement across all window sizes for both models tested, with larger marginal gains than HS probes (+12.0pp accuracy vs.\ +3.2pp for R1-8B). The asymmetry supports the interpretation that text features benefit proportionally more from temporal context because they encode less information per step.
402	
403	\section{Negative Results Details}
404	\label{app:negative_details}
405	
406	\paragraph{BOCPD/CUSUM.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). Only R1-8B produces non-zero detection (best: $\lambda{=}10$, 93\% rate, +3.45 steps lead). CUSUM configurations universally underperform simple thresholding on lead time. The probe score sequences for 3/4 models show smooth transitions that never trigger the hazard function (\cref{app:bocpd_config}).
407	
408	\paragraph{Mahalanobis distance.} Following TrajGuard~\cite{trajguard}, Mahalanobis distance from the pre-CP centroid produces $\Delta d \approx 0$ between pre-CP and post-CP steps. The discriminative signal resides in minor PCA components (explaining $<$5\% of total variance) rather than the principal directions that dominate the distance computation.
409	
410	\paragraph{RepE.} Mean-difference directions~\cite{zou2023representation} show inconsistent performance: QwQ-32B achieves 0.756 balanced accuracy (approaching supervised 0.778) but with substantially worse precision (0.512 vs.\ LR 0.700) and FPR (0.309 vs.\ 0.120). R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment structure in some models but not others, making it unreliable as a general-purpose method.
411	
412	\paragraph{MLP probes.} Two-layer MLPs ($d \rightarrow 128 \rightarrow 1$, ReLU) underperform logistic regression on 3/4 models. The commitment boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small training sets.
413	
414	\paragraph{CCS.} Contrast-Consistent Search~\cite{burns2023discovering} adapted with contrastive pairs from pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction, making it semi-supervised.
415	
416	\paragraph{Cross-model transfer.} 17 configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers) all fail. Best PCA: R1-8B $\rightarrow$ QwQ-32B at 59.5\% (PCA-2048). Best direct: QwQ-32B $\rightarrow$ R1-32B at 67.3\% but 1\% crossing rate. Implementation details in \cref{app:transfer_details}.
417	
418	\section{Cross-Model Transfer Implementation Details}
419	\label{app:transfer_details}
420	
421	We test whether safety probes transfer across models by projecting hidden states into a shared dimensionality space and applying cross-model classification.
422	
423	\paragraph{Method.} For each source-target model pair, we apply PCA independently to each model's hidden states, reducing to a shared dimensionality $d \in \{512, 1024, 2048\}$. PCA is fitted on the full dataset (including test traces) for each model separately, a setting favorable to transfer since it maximizes the quality of the projection. A logistic regression classifier (C=1.0, class\_weight=`balanced', max\_iter=2000, random\_state=42) trained on the source model's PCA-projected training data is then applied directly to the target model's PCA-projected test data. No cross-model alignment step (Procrustes rotation, CCA, or learned projection) is applied; PCA serves as a standard linear dimensionality reduction baseline.
424	
425	\paragraph{Same-dimension pairs.} For R1-32B and QwQ-32B (both 5120-d hidden states), we additionally test direct transfer without PCA: the source classifier is applied directly to the target model's raw hidden states. This tests whether same-architecture, same-dimensionality models share safety-relevant linear structure.
426	
427	\paragraph{Results.} All 17 transfer configurations (5 directional pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers for same-dimension pairs) fail to produce practically useful transfer. The best PCA result is R1-8B $\rightarrow$ QwQ-32B at 59.5\% balanced accuracy (PCA-2048). The best direct transfer (QwQ-32B $\rightarrow$ R1-32B) reaches 67.3\% balanced accuracy, which exceeds the within-model baseline of 65.2\%. However, this transfer direction achieves only 1\% crossing rate, meaning the transferred probe almost never triggers detection in practice, rendering it useless for deployment despite above-baseline accuracy. The complete failure under maximally favorable conditions (PCA fitted on full data, no train/test separation for projection) strengthens the conclusion that safety commitment is encoded in model-specific geometric configurations. PCA is a standard linear alignment baseline; its failure indicates that the problem lies in the representations themselves rather than in the choice of alignment method.
428	
429	
430	\section{Encoder Robustness Analysis}
431	\label{app:encoder_robustness}
432	
433	To test whether the HS advantage over text probes depends on the specific text encoder, we replace all-MiniLM-L6-v2 (384d) with BGE-large-en-v1.5 (1024d), a 2.7$\times$ higher-dimensional encoder with stronger semantic representations. \cref{tab:encoder_robustness} reports precision comparisons at each model's corrected layer.
434	
435	\begin{table}[h]
436	\centering
437	\small
438	\caption{HS vs.\ BGE-large (1024d) text probe precision. $\Delta$: HS minus BGE-large. Bootstrap: 1000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\alpha{=}0.05$).}
439	\label{tab:encoder_robustness}
440	\begin{tabular}{lcccccc}
441	\toprule
442	\textbf{Model} & \textbf{HS Prec} & \textbf{BGE Prec} & $\Delta$ & \textbf{95\% CI} & $p$ & \textbf{HB} \\
443	\midrule
444	R1-8B & 0.497 & 0.436 & +0.058 & [$-$0.03, +0.15] & 0.185 & No \\
445	OT-7B & 0.446 & 0.263 & +0.181 & [+0.09, +0.27] & ${<}0.001$ & Yes \\
446	R1-32B & 0.588 & 0.475 & +0.117 & [+0.01, +0.22] & 0.027 & No \\
447	QwQ-32B & 0.545 & 0.454 & +0.094 & [$-$0.03, +0.22] & 0.132 & No \\
448	\bottomrule
449	\end{tabular}
450	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ac19437-0eb4-4a69-8eba-4df7feb5e9e1",
  "isSidechain": true,
  "promptId": "fdc0542e-b5c3-4ed1-8bde-065d1e5a0b6e",
  "agentId": "ac17197ed6a690836",
  "type": "user",
  "uuid": "ee077c03-0027-40d7-a889-df6b9236432b",
  "sourceToolAssistantUUID": "8ac19437-0eb4-4a69-8eba-4df7feb5e9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-18T03:30:27.765Z_

Perfect! I've found all the key information. Let me compile the comprehensive findings for you.

## Summary of Findings

I've thoroughly searched the paper tex files and found all the requested information. Here are the complete details:

### **Table 2 Definition (HS vs. Text Comparison)**
Location: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex` lines 34-50

**Full Table 2 Content:**
```
Model    | Layer | W  | ΔBA  | ΔPrec | ΔFPR  | HB
---------|-------|----|----- |-------|-------|-----
R1-8B    | L14   | 15 | +8.2 | +22.4 | -7.4  | 3/3
OT-7B    | L16   | 3  | +10.7| +21.9 | -17.1 | 3/3
QwQ      | L60   | 3  | +15.4| +23.6 | -9.8  | 3/3
R1-32B   | L63   | 1  | +18.7| +15.4 | -14.6 | 3/3
```

**All R1-8B Precision Values Found:**
- **+22.4pp** - Main precision difference (HS vs. text) in Table 2
- **69.3%** - R1-8B HS precision at W=1 (baseline window)
- **82.2%** - R1-8B HS precision at W=25 (maximum window)
- **41.6%** - R1-8B text precision at W=1
- **64.8%** - R1-8B text precision at W=25
- **0.693** - Seed-level precision values in GRU results (seed 42)
- **11.8%** - R1-8B text FPR (mentioned as context for why FPR difference is smallest)

### **Bootstrap & Resample References**
Found in multiple locations:

1. **1000 resamples** - Standard bootstrap configuration
   - Location: experiments.tex line 7: "two-sided null-centered bootstrap (1000 resamples)"
   - Location: experiments.tex line 48: "Bootstrap: 1000 resamples, two-sided null-centered"
   - Location: appendix.tex line 36: "two-sided null-centered bootstrap (1000 resamples)"

2. **Holm-Bonferroni correction** with 12 tests (4 models × 3 metrics)
   - Location: experiments.tex line 7 and appendix.tex line 31

3. **No 10000 resamples found** - Only 1000 resamples used throughout

### **Window Size (W) Parameters for R1-8B**

From method.tex line 35:
- **Window sizes evaluated**: W ∈ {1, 3, 5, 10, 15, 20, 25}
- **R1-8B selected window**: **W=15** (from Table 2)

**Complete R1-8B window ablation (appendix.tex lines 77-84):**
```
W  | Bal. Acc. | Precision | FPR_step | Coverage | Lead
---|-----------|-----------|----------|----------|-------
1  | 77.8      | 69.3      | 9.65     | 72.1     | 13.8
3  | 79.0      | 72.3      | 8.50     | 69.8     | 12.1
5  | 78.1      | 72.6      | 8.09     | 65.1     | 8.3
10 | 79.3      | 74.3      | 7.61     | 55.8     | 10.0
15 | 80.2      | 77.7      | 6.39     | 51.2     | 7.2
20 | 80.7      | 78.6      | 6.12     | 53.5     | 7.4
25 | 81.0      | 82.2      | 4.83     | 48.8     | 8.1
```

### **R1-8B Layer Selection Details**

Location: experiments.tex lines 13-28 (Table 1 - Layer Selection)
- **Selected layer**: L14 (44% depth)
- **Biased metric selection**: L14 (same for R1-8B, unlike 32B models)
- **HS vs. text precision p-value at L14**: <0.001

### **Key Methodology Parameters**

From method.tex (lines 31-35):
- **Hidden-state probe**: L2-regularized logistic regression, balanced class weights, C=1.0
- **Text encoder**: all-MiniLM-L6-v2 (384d)
- **Detection threshold**: K=5 consecutive threshold crossings required
- **Statistical test**: Two-sided null-centered bootstrap with Holm-Bonferroni step-down correction
- **Alpha level**: α=0.05

### **Temporal Improvement Context**

From experiments.tex line 81:
- "At 7--8B, the modality advantage (+22pp precision) exceeds the temporal improvement (+13pp)"
- Figure 1 caption: "Temporal window effect on R1-8B HS probe (L14). Precision: 69.3% (W=1) to 82.2% (W=25); FPR: 9.65% to 4.8%."

All raw numbers and parameters have been extracted from the source files with exact line references for verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee077c03-0027-40d7-a889-df6b9236432b",
  "isSidechain": true,
  "agentId": "ac17197ed6a690836",
  "requestId": "req_011Cb9KuMnUGfo2xKsddqwVQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "73b7cf1a-481a-4258-8684-765c0bd51a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "75c13e9a-b023-4a8e-9cd6-6a9df909a830",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TAuFcg2d6kzr5P4k3BMKnU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 20747,
      "cache_read_input_tokens": 28319,
      "output_tokens": 1408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20747
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1408,
          "cache_read_input_tokens": 28319,
          "cache_creation_input_tokens": 20747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20747,
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
