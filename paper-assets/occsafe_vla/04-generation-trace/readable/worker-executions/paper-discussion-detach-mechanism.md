# paper discussion detach mechanism

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_paper_discussion_detach_mechanism_20260523T101456.log`
- **Structured JSON:** [`1a576298a19dac4d9c8c.json`](../../sessions/1a/1a576298a19dac4d9c8c.json)

## Before a recorded user message

38 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__read_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "dedf3831-fd20-49ef-876d-c15cf6e06626",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779546000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0184687c-af46-4ad3-b82b-1e6909adf07a",
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "ac801b86-09ed-4805-b968-6cd1309d8465",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoicV3tfrnCMrp59L8D3fu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_014Ck1tKPDLmH5pWcxCto7LS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/.claude/skills/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "f2248245-de44-4e44-beb5-bc2893ef5bdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoicV3tfrnCMrp59L8D3fu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
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

_source line 6 · 2026-05-23T10:15:05.491Z_

<details><summary>↩ Tool result · reported error · `toolu_014Ck1tKPDLmH5pWcxCto7LS`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "9790d272-8bbf-4173-b54c-6b835074983f",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_0114caMdS5D5xji1EfTGRYWc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "9fadac82-3831-4527-8c65-20370d21c309",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoicV3tfrnCMrp59L8D3fu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
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

_source line 8 · 2026-05-23T10:15:06.330Z_

<details><summary>↩ Tool result · `toolu_0114caMdS5D5xji1EfTGRYWc`</summary>

```text
1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\subsection{Why Does Gradient Flow Improve Collision Avoidance?}
6	\label{sec:why_gradient}
7	
8	The ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \emph{improves} CAR above Vanilla, but that its \emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.
9	
10	\textbf{Hypothesis 1: Anti-overfitting regularization.}
11	Auxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.
12	
13	\textbf{Hypothesis 2: Optimization landscape smoothing.}
14	The auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.
15	
16	\textbf{Hypothesis 3: Gradient diversity.}
17	When fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.
18	
19	All three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.
20	
21	\subsection{Why Is Detach Harmful?}
22	\label{sec:why_detach}
23	
24	Detach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\sigma = 0.163$ vs.\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.
25	
26	The primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \texttt{stop\_gradient}, the encoder receives gradients from $\mathcal{L}_\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.
27	
28	Gradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm in the Detach configuration to disentangle the normalization artifact from the gradient-flow effect.
29	
30	The TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.
31	
32	\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}
33	\label{sec:cutoff_temporal}
34	
35	The Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).
36	
37	This pattern connects to the candidate mechanisms in Section~\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.
38	
39	The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.
40	
41	The current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \textit{[Results to be added upon completion of 3-seed runs.]}
42	
43	\subsection{Implications for VLA Safety}
44	\label{sec:implications}
45	
46	\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.
47	
48	\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.
49	
50	\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.
51	
52	\subsection{Limitations}
53	\label{sec:limitations}
54	
55	\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.
56	
57	\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.
58	
59	\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.
60	
61	\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\sigma = 0.039$, 4 seeds), Full OCC ($\sigma = 0.032$, 3 seeds), and Random OCC ($\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\sigma = 0.002$), its TSR variance ($\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.
62	
63	The variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.
64	
65	\subsection{Depth vs.\ BEV Occupancy}
66	\label{sec:depth_discussion}
67	
68	The Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.
69	
70	The directional ordering (Full OCC $>$ Random OCC $>$ Depth $\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.
71	
72	The Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\sigma = 0.039$ vs.\ Vanilla's $\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.
73	
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "6454e0ab-e463-4aeb-9bb8-7711d672a080",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
      "content": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nGradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm in the Detach configuration to disentangle the normalization artifact from the gradient-flow effect.\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\nThe current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \\textit{[Results to be added upon completion of 3-seed runs.]}\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\\sigma = 0.039$, 4 seeds), Full OCC ($\\sigma = 0.032$, 3 seeds), and Random OCC ($\\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\\sigma = 0.002$), its TSR variance ($\\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.\n\nThe variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThe Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.\n\nThe directional ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.\n\nThe Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.\n\n",
      "numLines": 74,
      "startLine": 1,
      "totalLines": 74
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FwwkyevZAbXadtbykKQNi9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "eca89ca3-ea62-41be-95bd-3a62bea1d868",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoicV3tfrnCMrp59L8D3fu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
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

_source line 10 · 2026-05-23T10:15:07.010Z_

<details><summary>↩ Tool result · `toolu_01FwwkyevZAbXadtbykKQNi9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "5e8e70b6-fecf-42f1-8503-a57134657d68",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 20
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the paper_framing.md and also look for the paper-writing-norms skill in the correct location.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "abd7fa27-98cf-46aa-9dfd-1e4d047ab3f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1RtYnt5crstDYrNFHC4qY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4833,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4833
      },
      "output_tokens": 21,
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FQBzsxYgttrMJG663ZHYqd`</summary>

```json
{
  "project": "occsafe_vla",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "d7af8f88-cc30-40c3-8c3d-4027e7869a94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1RtYnt5crstDYrNFHC4qY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4833,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4833
      },
      "output_tokens": 21,
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

_source line 13 · 2026-05-23T10:15:12.814Z_

<details><summary>↩ Tool result · `toolu_01FQBzsxYgttrMJG663ZHYqd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md\", \"content\": \"# OccSafe-VLA — Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-22 22:15 UTC | 状态: Draft (3-seed ablation complete, depth 4-seed complete, Path B confirmed (D022))\\n\\n## Architecture Facts (from code, verified)\\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\\n- **FocalLoss**: α=0.25, γ=2.0\\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\\n- **LoRA**: rank=32, alpha=16, dropout=0.0\\n- **GPU**: 4× RTX PRO 6000 98GB per server\\n- **训练时间**: ~12.9h/run @ 1.08 it/s\\n\\n### 叙事含义\\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\\n  比\\\"仅改善 DINOv2\\\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \\\"lightweight auxiliary\\\" 叙事\\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\\\"放手\\\"让 action loss 主导，\\n  可论证为\\\"先学空间结构，再精化动作\\\"的课程学习效果\\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\\n\\n### DepthHead (新增, 2026-05-22)\\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\\n- **参数量**: ~1.2M（与 OccHead 同量级）\\n\\n## Core Insight (D019 修正, 2026-05-22)\\n\\n**原始假设（已部分推翻）**：BEV occupancy 迫使 vision encoder 发展 3D 空间感知 → safety emergence。\\n\\n**D017 发现**：辅助任务的梯度流提供正则化效应。\\n\\n**D019 修正后的 Core Insight**：VLA fine-tuning 中，辅助任务的**梯度流**是**必要条件**——\\n缺少梯度流（Detach）不仅无法提供正则化收益，反而**主动损害**模型的 collision avoidance（-3.4pp）\\n和 task execution 稳定性（TSR σ=0.163 vs <0.050）。梯度流条件（Full OCC, Random OCC）\\n保持与 Vanilla 可比的 CAR（差异 0.9-1.7pp，在 seed variance 内），\\n但不提供显著的正向收益。**梯度流是\\\"防止损害\\\"的必要条件，非\\\"提供收益\\\"的充分条件。**\\n\\nBEV 空间内容仅有边际贡献（Full OCC 0.797 vs Random OCC 0.789，差异 0.8pp，在 σ≈0.031 内）。\\n\\n**待验证**：Depth（egocentric, 与操作视角对齐）是否比 BEV（allocentric）和 Random 提供更有效的空间信号？\\n\\n## Framing Strategy (D019 修正)\\n\\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\\n\\n**核心叙事转变 (D019)**：从\\\"梯度流提供正则化收益\\\"→\\\"梯度流是防止辅助 head 损害的必要条件\\\"\\n\\n**Title（暂定）**: \\\"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\\\"\\n\\n**3-Contribution 结构（D019 修正）**：\\n- **C1 (核心发现)**: Auxiliary gradient flow 是防止 VLA safety 退化的必要条件\\n  - 正面证据: Full OCC/Random OCC ≈ Vanilla（梯度流不损害）\\n  - 反面证据: Detach < Vanilla（-3.4pp CAR, TSR σ=0.163 不稳定）\\n  - 空间内容次要: Full OCC ≈ Random OCC（0.8pp 差异，3 seeds each）\\n- **C2 (方法论贡献)**: 首个 5+ condition factorial study design for VLA safety mechanism analysis\\n- **C3 (实用贡献)**: 如果附加辅助 head，必须保留梯度流，否则会损害模型\\n\\n## Core Contribution Evidence (D019 修正, 3-seed 数据)\\n\\n### C1: Auxiliary Gradient Flow = Necessary Condition (Not Sufficient)\\n\\n**Evidence (4 conditions @50K, 50r, all 3 seeds)**:\\n| 条件 | Seeds | TSR | CAR | vs Vanilla CAR |\\n|------|-------|-----|-----|---------------|\\n| Full OCC | 3 | 0.894±0.050 | **0.797**±0.032 | **+1.7pp** |\\n| Random OCC | 3 | 0.869±0.029 | 0.789±0.031 | **+0.9pp** |\\n| Vanilla | 3 | 0.907±0.009 | 0.780±0.012 | baseline |\\n| Detach OCC | 3 | 0.812±0.163 | 0.746±0.002 | **-3.4pp** |\\n\\n**关键变化（D019 vs D017）**：\\n- Random OCC 3-seed 均值从 0.806 (2-seed) 降至 0.789 (3-seed)，s2 CAR=0.754 拉低\\n- Detach OCC 3-seed 暴露 TSR 不稳定性（s2 TSR=0.624，全面崩溃）\\n- Full OCC > Random OCC（翻转！2-seed 时 Random>Full，3-seed 后 Full>Random）\\n- 梯度流条件与 Vanilla 的差距缩小（0.9-1.7pp vs 之前 1.7-2.6pp），不再显著\\n\\n**Detach 系统性弱点（per-task 分析，3 seeds）**：\\n- T3 CAR: 0.200, 0.140, 0.000 — 三 seed 均低，系统性失败\\n- T5 TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040 — 三 seed 均低\\n- s2 TSR 全面崩溃（10/10 tasks 均退化），但 CAR 不变（0.748 vs 0.746/0.744）\\n\\n**Status**: ✅ 4 conditions 3-seed 数据齐全。Depth 4-seed complete, Path B confirmed (D022)。Cutoff eval 进行中。\\n\\n### Claim 2 (Mechanism): Gradient Flow is Necessary\\n梯度流是辅助任务不损害 safety 的必要条件。Detach(0.746) < Vanilla(0.780) → 切断梯度流有害。\\n**新增**: Detach TSR 不稳定性（σ=0.163）进一步证实梯度流必要性。\\n\\n### Claim 3: Spatial Content Secondary to Gradient Flow Presence\\nFull OCC (0.797) 和 Random OCC (0.789) 差异仅 0.8pp（3 seeds each），\\n远小于 Detach 退化（-3.4pp）。梯度流的存在/缺失是主要因素，空间内容次要。\\n**注意**: 3-seed 数据中 Full OCC > Random OCC（D017 时 Random > Full），\\n但差异太小不改变结论。\\n\\n### Claim 4 (Depth Comparison): ✅ Confirmed (D022)\\nDepth CAR = 0.780 = Vanilla exactly (4 seeds), confirms spatial content is secondary to gradient flow.\\nPath B confirmed: egocentric depth supervision offers no advantage over no auxiliary supervision at all.\\n\\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\\n\\n**【Pass（必须同时满足）】**\\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\\n2. Depth 4-seed mean TSR ≥ 0.870\\n\\n**【Fail（满足任一）】**\\n1. Depth 4-seed mean CAR < 0.780\\n2. Depth 4-seed mean TSR < 0.870\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\\n### RC2 [HIGH]: \\\"Why Not Just Use CBF?\\\" — Defense: zero inference cost + complementarity\\n### RC3 [HIGH]: Depth Ablation — Pending results\\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\\n\\n## Framing Risk Ranking (D019 更新)\\n\\n| 排名 | 风险 | 概率 | 应对 |\\n|------|------|------|------|\\n| **1** | Depth ≈ Random ≈ OCC（空间内容完全无用） | 40-50% | 论文已转为\\\"必要条件\\\"分析，此结果强化叙事 |\\n| **2** | 高 seed 方差致条件间差异不显著 | 25-30% | Detach 退化是稳健发现；gradient-flow vs Vanilla 差异确实不显著 |\\n| **3** | Depth 结果异常 | 15-20% | Path C framing |\\n\", \"total_chars\": 5450, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "915b10fd-3229-41dd-90d7-7a02b1b5b13e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md\\\", \\\"content\\\": \\\"# OccSafe-VLA — Paper Framing\\\\n\\\\n> 维护者: Director | 最后更新: 2026-05-22 22:15 UTC | 状态: Draft (3-seed ablation complete, depth 4-seed complete, Path B confirmed (D022))\\\\n\\\\n## Architecture Facts (from code, verified)\\\\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\\\\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\\\\n- **FocalLoss**: α=0.25, γ=2.0\\\\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\\\\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\\\\n- **LoRA**: rank=32, alpha=16, dropout=0.0\\\\n- **GPU**: 4× RTX PRO 6000 98GB per server\\\\n- **训练时间**: ~12.9h/run @ 1.08 it/s\\\\n\\\\n### 叙事含义\\\\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\\\\n  比\\\\\\\"仅改善 DINOv2\\\\\\\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\\\\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \\\\\\\"lightweight auxiliary\\\\\\\" 叙事\\\\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\\\\\\\"放手\\\\\\\"让 action loss 主导，\\\\n  可论证为\\\\\\\"先学空间结构，再精化动作\\\\\\\"的课程学习效果\\\\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\\\\n\\\\n### DepthHead (新增, 2026-05-22)\\\\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\\\\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\\\\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\\\\n- **参数量**: ~1.2M（与 OccHead 同量级）\\\\n\\\\n## Core Insight (D019 修正, 2026-05-22)\\\\n\\\\n**原始假设（已部分推翻）**：BEV occupancy 迫使 vision encoder 发展 3D 空间感知 → safety emergence。\\\\n\\\\n**D017 发现**：辅助任务的梯度流提供正则化效应。\\\\n\\\\n**D019 修正后的 Core Insight**：VLA fine-tuning 中，辅助任务的**梯度流**是**必要条件**——\\\\n缺少梯度流（Detach）不仅无法提供正则化收益，反而**主动损害**模型的 collision avoidance（-3.4pp）\\\\n和 task execution 稳定性（TSR σ=0.163 vs <0.050）。梯度流条件（Full OCC, Random OCC）\\\\n保持与 Vanilla 可比的 CAR（差异 0.9-1.7pp，在 seed variance 内），\\\\n但不提供显著的正向收益。**梯度流是\\\\\\\"防止损害\\\\\\\"的必要条件，非\\\\\\\"提供收益\\\\\\\"的充分条件。**\\\\n\\\\nBEV 空间内容仅有边际贡献（Full OCC 0.797 vs Random OCC 0.789，差异 0.8pp，在 σ≈0.031 内）。\\\\n\\\\n**待验证**：Depth（egocentric, 与操作视角对齐）是否比 BEV（allocentric）和 Random 提供更有效的空间信号？\\\\n\\\\n## Framing Strategy (D019 修正)\\\\n\\\\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\\\\n\\\\n**核心叙事转变 (D019)**：从\\\\\\\"梯度流提供正则化收益\\\\\\\"→\\\\\\\"梯度流是防止辅助 head 损害的必要条件\\\\\\\"\\\\n\\\\n**Title（暂定）**: \\\\\\\"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\\\\\\\"\\\\n\\\\n**3-Contribution 结构（D019 修正）**：\\\\n- **C1 (核心发现)**: Auxiliary gradient flow 是防止 VLA safety 退化的必要条件\\\\n  - 正面证据: Full OCC/Random OCC ≈ Vanilla（梯度流不损害）\\\\n  - 反面证据: Detach < Vanilla（-3.4pp CAR, TSR σ=0.163 不稳定）\\\\n  - 空间内容次要: Full OCC ≈ Random OCC（0.8pp 差异，3 seeds each）\\\\n- **C2 (方法论贡献)**: 首个 5+ condition factorial study design for VLA safety mechanism analysis\\\\n- **C3 (实用贡献)**: 如果附加辅助 head，必须保留梯度流，否则会损害模型\\\\n\\\\n## Core Contribution Evidence (D019 修正, 3-seed 数据)\\\\n\\\\n### C1: Auxiliary Gradient Flow = Necessary Condition (Not Sufficient)\\\\n\\\\n**Evidence (4 conditions @50K, 50r, all 3 seeds)**:\\\\n| 条件 | Seeds | TSR | CAR | vs Vanilla CAR |\\\\n|------|-------|-----|-----|---------------|\\\\n| Full OCC | 3 | 0.894±0.050 | **0.797**±0.032 | **+1.7pp** |\\\\n| Random OCC | 3 | 0.869±0.029 | 0.789±0.031 | **+0.9pp** |\\\\n| Vanilla | 3 | 0.907±0.009 | 0.780±0.012 | baseline |\\\\n| Detach OCC | 3 | 0.812±0.163 | 0.746±0.002 | **-3.4pp** |\\\\n\\\\n**关键变化（D019 vs D017）**：\\\\n- Random OCC 3-seed 均值从 0.806 (2-seed) 降至 0.789 (3-seed)，s2 CAR=0.754 拉低\\\\n- Detach OCC 3-seed 暴露 TSR 不稳定性（s2 TSR=0.624，全面崩溃）\\\\n- Full OCC > Random OCC（翻转！2-seed 时 Random>Full，3-seed 后 Full>Random）\\\\n- 梯度流条件与 Vanilla 的差距缩小（0.9-1.7pp vs 之前 1.7-2.6pp），不再显著\\\\n\\\\n**Detach 系统性弱点（per-task 分析，3 seeds）**：\\\\n- T3 CAR: 0.200, 0.140, 0.000 — 三 seed 均低，系统性失败\\\\n- T5 TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040 — 三 seed 均低\\\\n- s2 TSR 全面崩溃（10/10 tasks 均退化），但 CAR 不变（0.748 vs 0.746/0.744）\\\\n\\\\n**Status**: ✅ 4 conditions 3-seed 数据齐全。Depth 4-seed complete, Path B confirmed (D022)。Cutoff eval 进行中。\\\\n\\\\n### Claim 2 (Mechanism): Gradient Flow is Necessary\\\\n梯度流是辅助任务不损害 safety 的必要条件。Detach(0.746) < Vanilla(0.780) → 切断梯度流有害。\\\\n**新增**: Detach TSR 不稳定性（σ=0.163）进一步证实梯度流必要性。\\\\n\\\\n### Claim 3: Spatial Content Secondary to Gradient Flow Presence\\\\nFull OCC (0.797) 和 Random OCC (0.789) 差异仅 0.8pp（3 seeds each），\\\\n远小于 Detach 退化（-3.4pp）。梯度流的存在/缺失是主要因素，空间内容次要。\\\\n**注意**: 3-seed 数据中 Full OCC > Random OCC（D017 时 Random > Full），\\\\n但差异太小不改变结论。\\\\n\\\\n### Claim 4 (Depth Comparison): ✅ Confirmed (D022)\\\\nDepth CAR = 0.780 = Vanilla exactly (4 seeds), confirms spatial content is secondary to gradient flow.\\\\nPath B confirmed: egocentric depth supervision offers no advantage over no auxiliary supervision at all.\\\\n\\\\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\\\\n\\\\n**【Pass（必须同时满足）】**\\\\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\\\\n2. Depth 4-seed mean TSR ≥ 0.870\\\\n\\\\n**【Fail（满足任一）】**\\\\n1. Depth 4-seed mean CAR < 0.780\\\\n2. Depth 4-seed mean TSR < 0.870\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\\\\n### RC2 [HIGH]: \\\\\\\"Why Not Just Use CBF?\\\\\\\" — Defense: zero inference cost + complementarity\\\\n### RC3 [HIGH]: Depth Ablation — Pending results\\\\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\\\\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\\\\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\\\\n\\\\n## Framing Risk Ranking (D019 更新)\\\\n\\\\n| 排名 | 风险 | 概率 | 应对 |\\\\n|------|------|------|------|\\\\n| **1** | Depth ≈ Random ≈ OCC（空间内容完全无用） | 40-50% | 论文已转为\\\\\\\"必要条件\\\\\\\"分析，此结果强化叙事 |\\\\n| **2** | 高 seed 方差致条件间差异不显著 | 25-30% | Detach 退化是稳健发现；gradient-flow vs Vanilla 差异确实不显著 |\\\\n| **3** | Depth 结果异常 | 15-20% | Path C framing |\\\\n\\\", \\\"total_chars\\\": 5450, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper_framing.md\", \"content\": \"# OccSafe-VLA — Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-22 22:15 UTC | 状态: Draft (3-seed ablation complete, depth 4-seed complete, Path B confirmed (D022))\\n\\n## Architecture Facts (from code, verified)\\n- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）\\n- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。\\n- **FocalLoss**: α=0.25, γ=2.0\\n- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)\\n- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）\\n- **LoRA**: rank=32, alpha=16, dropout=0.0\\n- **GPU**: 4× RTX PRO 6000 98GB per server\\n- **训练时间**: ~12.9h/run @ 1.08 it/s\\n\\n### 叙事含义\\n- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。\\n  比\\\"仅改善 DINOv2\\\"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。\\n- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 \\\"lightweight auxiliary\\\" 叙事\\n- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐\\\"放手\\\"让 action loss 主导，\\n  可论证为\\\"先学空间结构，再精化动作\\\"的课程学习效果\\n- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守\\n\\n### DepthHead (新增, 2026-05-22)\\n- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）\\n- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）\\n- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64\\n- **参数量**: ~1.2M（与 OccHead 同量级）\\n\\n## Core Insight (D019 修正, 2026-05-22)\\n\\n**原始假设（已部分推翻）**：BEV occupancy 迫使 vision encoder 发展 3D 空间感知 → safety emergence。\\n\\n**D017 发现**：辅助任务的梯度流提供正则化效应。\\n\\n**D019 修正后的 Core Insight**：VLA fine-tuning 中，辅助任务的**梯度流**是**必要条件**——\\n缺少梯度流（Detach）不仅无法提供正则化收益，反而**主动损害**模型的 collision avoidance（-3.4pp）\\n和 task execution 稳定性（TSR σ=0.163 vs <0.050）。梯度流条件（Full OCC, Random OCC）\\n保持与 Vanilla 可比的 CAR（差异 0.9-1.7pp，在 seed variance 内），\\n但不提供显著的正向收益。**梯度流是\\\"防止损害\\\"的必要条件，非\\\"提供收益\\\"的充分条件。**\\n\\nBEV 空间内容仅有边际贡献（Full OCC 0.797 vs Random OCC 0.789，差异 0.8pp，在 σ≈0.031 内）。\\n\\n**待验证**：Depth（egocentric, 与操作视角对齐）是否比 BEV（allocentric）和 Random 提供更有效的空间信号？\\n\\n## Framing Strategy (D019 修正)\\n\\n**确定路线: Option B 分析论文**（Reviewer 审查通过）\\n\\n**核心叙事转变 (D019)**：从\\\"梯度流提供正则化收益\\\"→\\\"梯度流是防止辅助 head 损害的必要条件\\\"\\n\\n**Title（暂定）**: \\\"Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis\\\"\\n\\n**3-Contribution 结构（D019 修正）**：\\n- **C1 (核心发现)**: Auxiliary gradient flow 是防止 VLA safety 退化的必要条件\\n  - 正面证据: Full OCC/Random OCC ≈ Vanilla（梯度流不损害）\\n  - 反面证据: Detach < Vanilla（-3.4pp CAR, TSR σ=0.163 不稳定）\\n  - 空间内容次要: Full OCC ≈ Random OCC（0.8pp 差异，3 seeds each）\\n- **C2 (方法论贡献)**: 首个 5+ condition factorial study design for VLA safety mechanism analysis\\n- **C3 (实用贡献)**: 如果附加辅助 head，必须保留梯度流，否则会损害模型\\n\\n## Core Contribution Evidence (D019 修正, 3-seed 数据)\\n\\n### C1: Auxiliary Gradient Flow = Necessary Condition (Not Sufficient)\\n\\n**Evidence (4 conditions @50K, 50r, all 3 seeds)**:\\n| 条件 | Seeds | TSR | CAR | vs Vanilla CAR |\\n|------|-------|-----|-----|---------------|\\n| Full OCC | 3 | 0.894±0.050 | **0.797**±0.032 | **+1.7pp** |\\n| Random OCC | 3 | 0.869±0.029 | 0.789±0.031 | **+0.9pp** |\\n| Vanilla | 3 | 0.907±0.009 | 0.780±0.012 | baseline |\\n| Detach OCC | 3 | 0.812±0.163 | 0.746±0.002 | **-3.4pp** |\\n\\n**关键变化（D019 vs D017）**：\\n- Random OCC 3-seed 均值从 0.806 (2-seed) 降至 0.789 (3-seed)，s2 CAR=0.754 拉低\\n- Detach OCC 3-seed 暴露 TSR 不稳定性（s2 TSR=0.624，全面崩溃）\\n- Full OCC > Random OCC（翻转！2-seed 时 Random>Full，3-seed 后 Full>Random）\\n- 梯度流条件与 Vanilla 的差距缩小（0.9-1.7pp vs 之前 1.7-2.6pp），不再显著\\n\\n**Detach 系统性弱点（per-task 分析，3 seeds）**：\\n- T3 CAR: 0.200, 0.140, 0.000 — 三 seed 均低，系统性失败\\n- T5 TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040 — 三 seed 均低\\n- s2 TSR 全面崩溃（10/10 tasks 均退化），但 CAR 不变（0.748 vs 0.746/0.744）\\n\\n**Status**: ✅ 4 conditions 3-seed 数据齐全。Depth 4-seed complete, Path B confirmed (D022)。Cutoff eval 进行中。\\n\\n### Claim 2 (Mechanism): Gradient Flow is Necessary\\n梯度流是辅助任务不损害 safety 的必要条件。Detach(0.746) < Vanilla(0.780) → 切断梯度流有害。\\n**新增**: Detach TSR 不稳定性（σ=0.163）进一步证实梯度流必要性。\\n\\n### Claim 3: Spatial Content Secondary to Gradient Flow Presence\\nFull OCC (0.797) 和 Random OCC (0.789) 差异仅 0.8pp（3 seeds each），\\n远小于 Detach 退化（-3.4pp）。梯度流的存在/缺失是主要因素，空间内容次要。\\n**注意**: 3-seed 数据中 Full OCC > Random OCC（D017 时 Random > Full），\\n但差异太小不改变结论。\\n\\n### Claim 4 (Depth Comparison): ✅ Confirmed (D022)\\nDepth CAR = 0.780 = Vanilla exactly (4 seeds), confirms spatial content is secondary to gradient flow.\\nPath B confirmed: egocentric depth supervision offers no advantage over no auxiliary supervision at all.\\n\\n## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）\\n\\n**【Pass（必须同时满足）】**\\n1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）\\n2. Depth 4-seed mean TSR ≥ 0.870\\n\\n**【Fail（满足任一）】**\\n1. Depth 4-seed mean CAR < 0.780\\n2. Depth 4-seed mean TSR < 0.870\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED\\n### RC2 [HIGH]: \\\"Why Not Just Use CBF?\\\" — Defense: zero inference cost + complementarity\\n### RC3 [HIGH]: Depth Ablation — Pending results\\n### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations\\n### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations\\n### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI\\n\\n## Framing Risk Ranking (D019 更新)\\n\\n| 排名 | 风险 | 概率 | 应对 |\\n|------|------|------|------|\\n| **1** | Depth ≈ Random ≈ OCC（空间内容完全无用） | 40-50% | 论文已转为\\\"必要条件\\\"分析，此结果强化叙事 |\\n| **2** | 高 seed 方差致条件间差异不显著 | 25-30% | Detach 退化是稳健发现；gradient-flow vs Vanilla 差异确实不显著 |\\n| **3** | Depth 结果异常 | 15-20% | Path C framing |\\n\", \"total_chars\": 5450, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_015xAE46HancJVD51vf9N9cx`</summary>

```json
{
  "pattern": "**/paper-writing-norms.skill.md",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "6a5f5c78-95b3-42ec-9de9-5afb9dffd6a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1RtYnt5crstDYrNFHC4qY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4833,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4833
      },
      "output_tokens": 21,
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

_source line 15 · 2026-05-23T10:15:13.844Z_

<details><summary>↩ Tool result · `toolu_015xAE46HancJVD51vf9N9cx`</summary>

```text
/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "d917cca3-db90-4f88-979c-753c1e73ae23",
  "tool_use_result": {
    "filenames": [
      "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
    ],
    "durationMs": 461,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper-writing-norms skill.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "309a16f0-4151-428a-b4ac-d026bc4f2d74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qMoYDDSi7Jg3u6YwMovar",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3593,
      "cache_read_input_tokens": 28745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3593
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_0133kLKnVYRjqiUHUNRWbWdR`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "d30d68d0-8875-4f36-a395-1312965f91ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qMoYDDSi7Jg3u6YwMovar",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3593,
      "cache_read_input_tokens": 28745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3593
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

_source line 18 · 2026-05-23T10:15:16.553Z_

<details><summary>↩ Tool result · `toolu_0133kLKnVYRjqiUHUNRWbWdR`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "9607a038-dd98-4141-9932-3e946b7c43b0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
````

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me analyze the discussion.tex carefully for the three tasks.

**Task 1: Data compliance check**

I need to check all references to gradient data in the discussion.tex. The conditions with actual gradient data are:
- Random OCC (s2)
- Depth (implicit from gradient analysis)
- Detach (s2)

Conditions WITHOUT gradient data:
- Full OCC (retrain in progress)
- Vanilla (retrain in progress)
- Cutoff (no gradient analysis)

Let me scan line by line:


Line 8 references CAR values for Full OCC, Random OCC, and Vanilla—these are performance metrics, not gradient claims, so that's fine. Line 11 discusses hypotheses without making gradient data claims. Line 28 compares gradient norms across Random OCC, Depth, and Detach—all conditions where gradient analysis was actually performed, so this checks out.

The next section acknowledges that a complete four-condition comparison is still pending from ongoing retraining runs. The orthogonality observation about action and occupancy gradients comes from the available gradient data (Random OCC and Detach s2). There's also mention of a planned experiment swapping BatchNorm for LayerNorm in the Detach configuration to isolate whether the normalization itself or the gradient flow is driving the effect.

Line 70 presents an architectural hypothesis about why the occupancy head might produce stronger gradients than the depth head—larger convolutional decoder versus lighter architecture—but I should be careful here. This reads as speculative reasoning rather than a claim about measured gradient magnitudes, though it could be misread as implying I have direct gradient comparisons between the two heads.

Looking at what gradient data actually exists: Random OCC (s2), Depth (from the gradient analysis), and Detach (s2) all have gradient information. Since Depth does have gradient data and the hypothesis is framed as "one possibility" rather than a definitive claim, this seems acceptable. Let me continue checking for other problematic references. OCC and Depth are both gradient-flow conditions with data, while Detach serves as the comparison point—all three have the necessary gradient information to support the claim. The compliance check seems solid after that L28 correction.

Now I need to add a paragraph about the BatchNorm hypothesis right after the gradient analysis section.  The key points are that BatchNorm layers in the auxiliary head accumulate running statistics from the encoder's features regardless of gradient flow, and the dormant OCC head acts as an unoptimized computational drain on the encoder. I should frame this as a hypothesis rather than a confirmed mechanism, and use the Detach+LN experiment as a way to test whether BatchNorm is actually the culprit. I'll avoid pulling in gradient data from Full OCC or Vanilla since those aren't relevant to this specific mechanism.

Let me continue from where the draft left off. The encoder can't adapt to the shifted batch statistics under stop_gradient, so the auxiliary head becomes a parasitic pathway that perturbs feature distributions while the encoder optimizes only for action loss. The hypothesis predicts that swapping BatchNorm for LayerNorm—which normalizes per-sample and doesn't maintain running statistics—should eliminate this interference. The Detach+LN experiment is designed to test exactly this, and if LayerNorm restores performance to Vanilla levels, it would confirm BatchNorm contamination as the mechanism. what's already covered versus what needs to be added. Line 26 establishes BatchNorm as the primary mechanism and explains how stop_gradient prevents adaptation, but the task wants me to emphasize the running statistics being influenced by the OCC head's output, frame it more as a hypothesis, and highlight the Detach+LayerNorm experiment as a discriminating test—which is actually mentioned briefly in Line 28 but deserves more prominence in the enhanced paragraph. I need to distinguish between the general forward-pass interference mechanism, which is well-supported, and the specific BatchNorm contamination hypothesis, which requires more careful framing. The new paragraph should present the BN pathway as a plausible explanation within that broader framework, drawing on the Detach+LN experiment as suggestive evidence rather than proof. I'll insert this between the gradient analysis and TSR instability sections to build the argument progressively. tering their batch-level distributional properties without the encoder having any mechanism to compensate. If this hypothesis holds, the degradation we see with Detach is fundamentally a normalization artifact rather than evidence that gradient flow itself provides training benefits. To test this, I'd replace the auxiliary head's BatchNorm layers with LayerNorm, which normalizes per-sample without maintaining running statistics across the batch dimension. The pending results from this experiment should clarify whether BatchNorm interference is the primary culprit or if the gradient-flow effect is genuine and independent of normalization.

Now I'm refining the hypothesis about BatchNorm contamination—the auxiliary head's normalization layers continuously update their running statistics regardless of gradient routing, creating an asymmetric coupling where the encoder can't adapt to the distributional shifts these statistics impose.

To test this, I'm proposing a discriminating experiment: replacing BatchNorm with LayerNorm in the auxiliary head, since LayerNorm normalizes per-sample and doesn't maintain cross-batch statistics. If LayerNorm restores performance to Vanilla levels, it confirms BatchNorm interference as the primary mechanism; if performance remains degraded, the gradient-flow effect is genuine and independent of normalization.

Now I need to check for redundancy—the end of L28 already mentions this LayerNorm experiment, so I should remove that sentence to avoid repeating myself. Then I'll verify consistency across the hypotheses and other sections to make sure this new mechanism discussion doesn't contradict anything.

Looking at the practical recommendation in L46, it states the empirical finding about gradient flow without claiming a specific mechanism, so it holds regardless of whether the BatchNorm hypothesis pans out. I should also scan for any loose uses of "significantly" that aren't backed by statistical tests—L46 uses it descriptively rather than statistically, which is fine.

Now I'm ready to execute the edits: remove the trailing sentence about the LN experiment from L28 to avoid repeating what the new paragraph will cover, then insert the BatchNorm hypothesis paragraph right after. I'm identifying where to make the edit—the last sentence about replacing BatchNorm with LayerNorm should be removed since the new paragraph will cover that more thoroughly, and I'll insert the new content as a separate paragraph between the gradient analysis and the TSR instability sections.

Now I'm reconsidering whether the claim about forward-pass interference is stated too definitively. The Detach experiment shows that cutting gradients hurts performance, which supports the idea that gradients matter, but it doesn't definitively prove forward-pass interference is the primary mechanism versus simply the absence of beneficial gradient signals. The BatchNorm hypothesis specifically needs framing as exploratory, and the Detach+LayerNorm experiment is designed to test whether normalization is the culprit.

But looking back at the task, I'm asked to insert a new paragraph about BatchNorm analysis between L28 and L30, not to modify L26. Let me focus on that specific request and also verify the gradient data references throughout the document. I should also check whether "significantly" appears in the text—I'm seeing it around line 46 in the context of CAR improvements.

The phrasing there uses "significantly" without a statistical test backing it up, just a parenthetical note about cross-seed variance. The task explicitly says not to use "significantly" without statistical verification, so I should replace it with something like "meaningfully" or "substantially" to be more precise. I should also watch out for em-dashes since the writing guidelines discourage them.

My plan is to remove the trailing sentence from L28 about ongoing experiments, insert the new batch normalization hypothesis paragraph right after it, and then swap out "significantly" in L46 for "meaningfully" to avoid the statistical language issue.

For the actual edits, I'll use the old_string/new_string pattern. The cleanest approach is to replace the sentence about ongoing experiments through the start of the next paragraph with my new content, keeping the structure intact so the flow remains natural. orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective.

We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm layers maintain running statistics that update at every forward pass, accumulating information from the auxiliary pathway's activations across training iterations. Meanwhile, the encoder receives no auxiliary gradient to adapt to this distributional shift, so the 1.2M-parameter auxiliary head acts as an unoptimized parasitic pathway—it perturbs batch-level statistics while the encoder, trained only on action loss, has no way to compensate. To test this, we're replacing the auxiliary head's BatchNorm with LayerNorm, which normalizes per-sample without maintaining cross-batch running statistics, and we're waiting on results to see if this restores performance to the Vanilla baseline.

The TSR instability reveals... I'm noticing some em-dash inconsistencies in the existing text, but since those aren't part of my edits, I'll leave them as is. Let me do a final check on the lines I'm actually modifying to make sure they comply with the gradient data constraint—the CAR comparisons are fine since they're about model performance, not gradient mechanics, and the diagnostic methods I mention are just acknowledging what would be needed to distinguish between hypotheses, not claiming gradient data exists.

Now I need to locate the exact text I'm replacing. Looking at the paragraph around line 28, I can see it discusses gradient analysis at convergence and the orthogonality of the auxiliary task, ending with a sentence about replacing BatchNorm with LayerNorm in the Detach configuration. That's the sentence I need to swap out for my new paragraph about TSR instability. I'm working through the edits to clean up the paragraph structure—removing the sentence about the LayerNorm experiments and creating a clear break before the TSR instability discussion begins.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "02f82d75-6a9c-43db-a501-c72e21d03264",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECwLnGxbYu7WcegYus369p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 32338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

_source line 20_

Now I have all the context. Let me execute the three tasks.

**Task 1: Data compliance scan**

Scanning all gradient data references in discussion.tex:

- **L28**: "In two gradient-flow conditions analyzed thus far (Random OCC, Depth)" — correct, both have gradient data. Compares against Detach — also has data. "A complete four-condition comparison awaits the completion of ongoing retraining runs" — correctly hedges. **PASS**
- **L28 end**: "Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm" — refers to planned experiment, not data claim. **PASS**
- **L26**: "The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics" — architectural fact, not gradient data claim. **PASS**
- **L46**: "does not significantly improve CAR beyond Vanilla" — uses "significantly" without statistical test. **FIX NEEDED**
- **L70**: "the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals" — stated as hypothesis ("One possibility is"), not data claim. **PASS**

One issue found: "significantly" on L46. Fixing that plus inserting the new paragraph now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "ec54adc0-d0ad-4a08-921d-b7728aae5e6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECwLnGxbYu7WcegYus369p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 32338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01E7Nw1ugXtJNzqNQ4HVt5LN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm in the Detach configuration to disentangle the normalization artifact from the gradient-flow effect.\n\nThe TSR instability reveals",
  "new_string": "We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}\n\nThe TSR instability reveals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "f8370b9e-4da6-4034-b09b-c2105baf3bba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECwLnGxbYu7WcegYus369p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 32338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

_source line 22 · 2026-05-23T10:17:53.784Z_

<details><summary>↩ Tool result · `toolu_01E7Nw1ugXtJNzqNQ4HVt5LN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "2d991cf7-93b6-4bf7-9ed3-8bbde04182a1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "oldString": "Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm in the Detach configuration to disentangle the normalization artifact from the gradient-flow effect.\n\nThe TSR instability reveals",
    "newString": "We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}\n\nThe TSR instability reveals",
    "originalFile": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nGradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm in the Detach configuration to disentangle the normalization artifact from the gradient-flow effect.\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\nThe current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \\textit{[Results to be added upon completion of 3-seed runs.]}\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\\sigma = 0.039$, 4 seeds), Full OCC ($\\sigma = 0.032$, 3 seeds), and Random OCC ($\\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\\sigma = 0.002$), its TSR variance ($\\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.\n\nThe variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThe Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.\n\nThe directional ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.\n\nThe Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.\n\n",
    "structuredPatch": [
      {
        "oldStart": 25,
        "oldLines": 7,
        "newStart": 25,
        "newLines": 7,
        "lines": [
          " ",
          " The primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.",
          " ",
          "-Gradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. Ongoing experiments replace the auxiliary head's BatchNorm with LayerNorm in the Detach configuration to disentangle the normalization artifact from the gradient-flow effect.",
          "+Gradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}",
          " ",
          " The TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.",
          " "
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01RbtjNggRv3puYzY3JvDZrf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "does not significantly improve CAR beyond Vanilla",
  "new_string": "does not improve CAR beyond Vanilla"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "653c34f5-83a7-42a0-8170-7fe9e2fe829f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECwLnGxbYu7WcegYus369p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5602,
      "cache_read_input_tokens": 32338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5602
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

_source line 24 · 2026-05-23T10:17:54.602Z_

<details><summary>↩ Tool result · `toolu_01RbtjNggRv3puYzY3JvDZrf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "bd3f5ae7-4087-4307-acaa-04763264229e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "oldString": "does not significantly improve CAR beyond Vanilla",
    "newString": "does not improve CAR beyond Vanilla",
    "originalFile": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nGradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\nThe current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \\textit{[Results to be added upon completion of 3-seed runs.]}\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\\sigma = 0.039$, 4 seeds), Full OCC ($\\sigma = 0.032$, 3 seeds), and Random OCC ($\\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\\sigma = 0.002$), its TSR variance ($\\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.\n\nThe variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThe Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.\n\nThe directional ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.\n\nThe Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.\n\n",
    "structuredPatch": [
      {
        "oldStart": 43,
        "oldLines": 7,
        "newStart": 43,
        "newLines": 7,
        "lines": [
          " \\subsection{Implications for VLA Safety}",
          " \\label{sec:implications}",
          " ",
          "-\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not significantly improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.",
          "+\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.",
          " ",
          " \\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.",
          " "
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

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the edits by reading the modified file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "26ef65fd-b3c5-4d87-9265-70a8463156a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyZW5HUuGq2aoM7oFHGrZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7914,
      "cache_read_input_tokens": 37940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7914
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

_source line 26_

Let me verify the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "1a272835-13b9-4731-bec9-3f98cc2bc416",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyZW5HUuGq2aoM7oFHGrZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7914,
      "cache_read_input_tokens": 37940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7914
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01EZZPcTFpiQn5qTtSa1tqKW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "offset": 21,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "e9aaabdd-ebbf-423b-8d41-fc76b7009890",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyZW5HUuGq2aoM7oFHGrZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7914,
      "cache_read_input_tokens": 37940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7914
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

_source line 28 · 2026-05-23T10:17:58.558Z_

<details><summary>↩ Tool result · `toolu_01EZZPcTFpiQn5qTtSa1tqKW`</summary>

```text
21	\subsection{Why Is Detach Harmful?}
22	\label{sec:why_detach}
23	
24	Detach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\sigma = 0.163$ vs.\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.
25	
26	The primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \texttt{stop\_gradient}, the encoder receives gradients from $\mathcal{L}_\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.
27	
28	Gradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \textit{[Detach+LN results pending (plan\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}
29	
30	The TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.
31	
32	\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}
33	\label{sec:cutoff_temporal}
34	
35	The Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).
36	
37	This pattern connects to the candidate mechanisms in Section~\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.
38	
39	The TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.
40	
41	The current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \textit{[Results to be added upon completion of 3-seed runs.]}
42	
43	\subsection{Implications for VLA Safety}
44	\label{sec:implications}
45	
46	\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.
47	
48	\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.
49	
50	\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.
51	
52	\subsection{Limitations}
53	\label{sec:limitations}
54	
55	\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "518990a0-f804-4c86-99e1-96e52e3d7f35",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
      "content": "\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nGradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\nThe current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \\textit{[Results to be added upon completion of 3-seed runs.]}\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.",
      "numLines": 35,
      "startLine": 21,
      "totalLines": 74
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01RjjE56bbs2kCxoLiLUbuuv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "offset": 45,
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
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "e6cd7479-fe64-4959-945c-f1979c30e44e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyZW5HUuGq2aoM7oFHGrZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7914,
      "cache_read_input_tokens": 37940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7914
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

_source line 30 · 2026-05-23T10:17:59.076Z_

<details><summary>↩ Tool result · `toolu_01RjjE56bbs2kCxoLiLUbuuv`</summary>

```text
45	
46	\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.
47	
48	\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.
49	
50	\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.
51	
52	\subsection{Limitations}
53	\label{sec:limitations}
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "64f2e6b8-0873-434c-80a3-8f74b947e4ea",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
      "content": "\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n",
      "numLines": 10,
      "startLine": 45,
      "totalLines": 74
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
I see a problem: the new BN hypothesis paragraph got concatenated into the same line as L28 (the gradient analysis paragraph). It should be a separate paragraph. Let me look at the text more carefully.

In line 28, after "...rather than a competing signal for the action objective." the new text "We hypothesize that..." starts on the same line without a paragraph break. I need to add a paragraph break between the gradient analysis and the BN hypothesis.

Let me fix this by adding a blank line before "We hypothesize".
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "bd79a13e-b05b-4f06-94f2-6925ff40fe48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mtkw3hscQoBDuBXsEtJJCj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3045,
      "cache_read_input_tokens": 45854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3045
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

_source line 32_

The new paragraph got concatenated into L28 instead of being a separate paragraph. Let me fix the paragraph break.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "a3247ae8-1b50-4711-845e-0a135f539bc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mtkw3hscQoBDuBXsEtJJCj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3045,
      "cache_read_input_tokens": 45854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3045
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01VaXhYLh9Z4H2dZStpUAQLi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "rather than a competing signal for the action objective. We hypothesize that the specific mechanism",
  "new_string": "rather than a competing signal for the action objective.\n\nWe hypothesize that the specific mechanism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "02f2e826-2ad0-49cd-b60d-780235b1ca37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mtkw3hscQoBDuBXsEtJJCj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3045,
      "cache_read_input_tokens": 45854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3045
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

_source line 34 · 2026-05-23T10:18:08.018Z_

<details><summary>↩ Tool result · `toolu_01VaXhYLh9Z4H2dZStpUAQLi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "4ca66898-a14e-4d57-98df-c155d6b94379",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "oldString": "rather than a competing signal for the action objective. We hypothesize that the specific mechanism",
    "newString": "rather than a competing signal for the action objective.\n\nWe hypothesize that the specific mechanism",
    "originalFile": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\subsection{Why Does Gradient Flow Improve Collision Avoidance?}\n\\label{sec:why_gradient}\n\nThe ablation results reveal a consistent pattern: conditions with auxiliary gradient flow through the vision encoder (Full OCC at 0.797 CAR, Random OCC at 0.789) remain comparable to Vanilla (0.780), while Detach OCC (0.746) falls well below all others. The dominant effect is not that gradient flow \\emph{improves} CAR above Vanilla, but that its \\emph{absence} degrades CAR below Vanilla. Three candidate mechanisms can explain this ``damage prevention'' pattern.\n\n\\textbf{Hypothesis 1: Anti-overfitting regularization.}\nAuxiliary gradients prevent the vision encoder from overfitting to the action prediction objective, preserving more general spatial features in the DINOv2 and SigLIP representations. Multi-task learning theory predicts this effect: shared representations trained on multiple objectives retain broader feature diversity than those specialized to a single task~\\cite{caruana1997multitask, ruder2017overview}. Lippl and Lindsey~\\cite{lippl2024implicit} show that multi-task training in overparameterized networks induces $\\ell_{1,2}$ mixed-norm regularization that encourages feature sharing, while single-task fine-tuning exhibits nested feature selection that discards unused pretrained features. Under this hypothesis, Random OCC and Full OCC both regularize because both supply non-trivial gradients through the encoder---the label content matters less than the gradient signal itself. The observation that Full OCC (0.797) and Random OCC (0.789) achieve nearly identical CAR (0.8pp difference, 3 seeds each) is consistent with this account. However, the current data more strongly support a ``damage prevention'' framing than a ``positive regularization'' framing: gradient-flow conditions do not clearly exceed Vanilla, but their absence clearly harms performance.\n\n\\textbf{Hypothesis 2: Optimization landscape smoothing.}\nThe auxiliary loss modifies the curvature of the total loss landscape, steering LoRA adapter updates away from sharp minima of the action loss alone. Sharp minima generalize poorly under distribution shift~\\cite{foret2021sam}, and SafeLIBERO evaluation introduces a distributional shift (obstacles absent during training, present at test time). If the auxiliary loss flattens the loss surface, the resulting adapter weights may produce policies that degrade more gracefully when the scene layout differs from training. This hypothesis predicts that \\emph{any} auxiliary loss with comparable gradient magnitude should help, which aligns with Random OCC's strong performance. A direct test would compare the Hessian spectra of Vanilla and auxiliary-trained checkpoints; we leave this analysis to future work.\n\n\\textbf{Hypothesis 3: Gradient diversity.}\nWhen fine-tuning with action loss alone, encoder gradients are dominated by a single objective, which may cause gradient alignment across batches and reduce the effective rank of weight updates. An auxiliary task provides an independent gradient direction that maintains update diversity. Unlike Hypothesis~1, which focuses on feature preservation, this hypothesis emphasizes the optimization dynamics: auxiliary gradients break correlations in the update trajectory rather than preserving specific features. The distinction is testable by measuring gradient cosine similarity between the action and auxiliary heads across training steps.\n\nAll three hypotheses predict that gradient flow is necessary (Detach should underperform) and that label content is secondary to gradient presence (Random should match Full OCC). The current data cannot distinguish between them---doing so requires gradient-level diagnostics (Hypothesis~3), loss landscape analysis (Hypothesis~2), or representational probing (Hypothesis~1). We present all three to guide future mechanistic investigation.\n\n\\subsection{Why Is Detach Harmful?}\n\\label{sec:why_detach}\n\nDetach OCC produces the lowest CAR (0.746) among all conditions, falling 3.4 percentage points below Vanilla (0.780), and exhibits uniquely high TSR variance ($\\sigma = 0.163$ vs.\\ $< 0.050$ for all other conditions). This result may appear surprising: the Detach condition has identical architecture and forward computation to Full OCC, differing only in gradient routing.\n\nThe primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nGradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}\n\nThe Cutoff condition---which applies occupancy supervision for the first 35{,}000 steps then removes it---provides a temporal dissection of the gradient flow effect. Cutoff achieves overall CAR of 0.783 (2 seeds), comparable to Vanilla (0.780), but its per-task profile reveals a critical asymmetry: Task~3 CAR (0.66) is the highest of any condition, while Task~5 CAR (0.00) is the lowest---a complete failure on the hardest safety task, worse even than Detach OCC (0.05).\n\nThis pattern connects to the candidate mechanisms in Section~\\ref{sec:why_gradient}. Under the anti-overfitting hypothesis, removing auxiliary gradients after 35{,}000 steps allows the encoder to re-specialize toward action prediction during the final 15{,}000 steps, losing the feature diversity that continuous gradient flow preserves. Under the optimization landscape hypothesis, the loss surface may sharpen once the auxiliary loss is removed, allowing the encoder to settle into a sharper minimum during late training. Both accounts predict that collision avoidance on the most physically constrained tasks---where the policy must maintain precise clearance---would be most sensitive to late-stage gradient withdrawal, consistent with the Task~5 result.\n\nThe TSR--CAR dissociation further constrains the mechanism. Cutoff achieves the highest TSR among all conditions (0.915 vs.\\ 0.907 Vanilla), indicating that early-phase auxiliary training durably improves motor learning. Collision avoidance on the hardest tasks, however, appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla (0.783 vs.\\ 0.780), but its Task~5 CAR collapses to 0.00. This temporal asymmetry suggests that task completion and collision avoidance depend on different aspects of encoder representation: motor skill may be encoded in features that stabilize early, while obstacle clearance depends on features that require ongoing auxiliary gradient support to maintain.\n\nThe current analysis tests a single temporal schedule (gradient flow for the first 35{,}000 of 50{,}000 steps). Two additional conditions are in progress to map the dose-response relationship more precisely. A Cutoff@25K condition disables gradient flow after 25{,}000 steps to identify the minimum exposure duration required for the auxiliary signal to take effect. A reverse cutoff condition withholds auxiliary gradients during early training and enables them only during the final phase; this tests whether late-stage gradient flow alone is sufficient. Together with the existing Cutoff@35K data, these conditions will trace the temporal sensitivity curve and determine whether the critical window lies in early training, late training, or spans the full schedule. \\textit{[Results to be added upon completion of 3-seed runs.]}\n\n\\subsection{Implications for VLA Safety}\n\\label{sec:implications}\n\n\\textbf{Practical recommendation.} The central finding is a necessary condition rather than a benefit: if practitioners attach an auxiliary head to the vision encoder during VLA fine-tuning, gradients \\emph{must} flow through the encoder. Blocking gradient flow (Detach) degrades CAR by 3.4pp below the no-auxiliary baseline and destabilizes task execution. With gradient flow maintained, the auxiliary head does not improve CAR beyond Vanilla (differences of 0.0--1.7pp, within cross-seed variance), but it does not harm it either---and no ground-truth spatial labels are required (Random OCC matches Full OCC at 0.8pp difference). The auxiliary head is discarded after training, adding zero inference cost.\n\n\\textbf{Complementarity with runtime safety.} Our approach modifies the training signal to produce policies that collide less frequently, but provides no formal safety guarantee for any individual episode. Runtime constraint methods such as CBF-based action filtering~\\cite{hu2025vlsa, raja2024ogmcbf} offer per-step guarantees but add inference cost and require access to obstacle geometry. These two strategies are complementary: auxiliary-task training reduces the frequency of unsafe action proposals, while runtime filtering can catch the remaining violations. A natural extension is to construct a barrier function that operates on the spatial features already learned by the occupancy-trained encoder, avoiding the need for explicit geometric representations at test time.\n\n\\textbf{Zero inference cost.} Unlike existing VLA safety methods that add modules at inference~\\cite{hu2025vlsa, zhang2025safevla, zhai2026cofreevla}, auxiliary spatial supervision modifies only the training phase. The auxiliary head is discarded after training, so the deployed model has identical latency, memory footprint, and computational cost to the Vanilla baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Single architecture.} All experiments use OpenVLA-OFT with LoRA rank 32. Whether the gradient-flow regularization effect transfers to other VLA architectures (e.g., RT-2~\\cite{brohan2023rt2}), other adapter configurations, or full fine-tuning remains untested.\n\n\\textbf{Single benchmark.} We evaluate on SafeLIBERO Level~I, which tests 10 tabletop manipulation tasks with static obstacles. The results may not generalize to dynamic obstacles, multi-step tasks (Level~II), or real-world deployment where sim-to-real transfer introduces additional distributional shift.\n\n\\textbf{Effect size.} The overall CAR difference between gradient-flow conditions and Vanilla is 0.0--1.7 percentage points, a modest effect within cross-seed variance. The Detach degradation ($-$3.4pp) is more substantial and consistent. Per-task analysis shows larger effects on physically constrained tasks where the baseline CAR is low, but these are also the tasks with the highest seed variance.\n\n\\textbf{Seed sensitivity is a systemic property of auxiliary supervision.} All auxiliary conditions exhibit higher cross-seed CAR variance than Vanilla: Depth ($\\sigma = 0.039$, 4 seeds), Full OCC ($\\sigma = 0.032$, 3 seeds), and Random OCC ($\\sigma = 0.031$, 3 seeds) all exceed Vanilla ($\\sigma = 0.012$, 3 seeds) by a factor of 2.6--3.1$\\times$. This amplified variance is not specific to any label type or auxiliary architecture---it appears across structured occupancy, random binary, and egocentric depth labels alike---suggesting that the auxiliary gradient signal itself introduces optimization sensitivity to initialization. The Detach condition is an extreme case: while its CAR variance is minimal ($\\sigma = 0.002$), its TSR variance ($\\sigma = 0.163$) is an order of magnitude higher than any other condition, driven by one seed with broad performance collapse.\n\nThe variance amplification is most pronounced on hard tasks. On Task~3, per-seed CAR ranges span 0.58 (Depth: 0.20--0.78), 0.54 (Random OCC: 0.26--0.54), and 0.52 (Full OCC: 0.28--0.80), compared to 0.22 for Vanilla (0.26--0.48). On Task~6, Depth ranges from 0.16 to 0.84 across 4 seeds. These per-task ranges exceed the overall condition means, meaning that seed selection can reverse the relative ordering of conditions on any individual task. The consistent overall ordering (Full OCC $>$ Random OCC $>$ Vanilla) is directionally stable but the gaps (1.7pp and 0.9pp) are not statistically significant at conventional levels with 3--4 seeds. Scaling to 5+ seeds per condition would clarify whether these gaps reflect real advantages or sampling noise. The Detach--Vanilla gap ($-$3.4pp) remains the most robust finding, with non-overlapping ranges across all 3 seeds of each condition.\n\n\\subsection{Depth vs.\\ BEV Occupancy}\n\\label{sec:depth_discussion}\n\nThe Depth condition (4 seeds) achieves CAR of 0.780---identical to Vanilla and below both OCC conditions (Full OCC 0.797, Random OCC 0.789). This result resolves the spatial reference frame question: egocentric depth supervision, despite providing per-pixel geometric information directly aligned with collision avoidance, offers no advantage over no auxiliary supervision at all. Combined with Random OCC's comparable performance using random binary labels, the data suggest that three distinct auxiliary label types---allocentric occupancy, egocentric depth, and random noise---all yield CAR within 1.7pp of Vanilla when gradient flow is maintained.\n\nThe directional ordering (Full OCC $>$ Random OCC $>$ Depth $\\approx$ Vanilla), though not statistically significant with 3--4 seeds, raises the question of why OCC-based heads outperform the depth head despite using an equivalent gradient flow mechanism. One possibility is architectural: the BEV occupancy head uses a larger convolutional decoder that produces stronger gradient signals through the encoder, while the depth head's lighter architecture generates weaker gradients. Under the gradient diversity hypothesis (Section~\\ref{sec:why_gradient}), stronger auxiliary gradients would maintain greater update diversity, producing a larger---though still modest---effect on CAR. An alternative explanation is that the BEV projection introduces a coordinate transformation that forces the encoder to develop viewpoint-invariant features, providing a form of data augmentation absent in the egocentric depth task. Both accounts predict the observed ordering without requiring that spatial content itself drives the effect.\n\nThe Depth condition also confirms that auxiliary supervision systematically amplifies seed-dependent variance ($\\sigma = 0.039$ vs.\\ Vanilla's $\\sigma = 0.012$), consistent with the pattern observed for Full OCC and Random OCC. This variance amplification appears independent of label content or spatial reference frame, further supporting the interpretation that the gradient flow mechanism---not the spatial signal---is the operative factor in both the mean effect and the variance effect of auxiliary supervision.\n\n",
    "structuredPatch": [
      {
        "oldStart": 25,
        "oldLines": 8,
        "newStart": 25,
        "newLines": 10,
        "lines": [
          " ",
          " The primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.",
          " ",
          "-Gradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective. We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}",
          "+Gradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective.",
          " ",
          "+We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}",
          "+",
          " The TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.",
          " ",
          " \\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}"
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

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_013MHs28pxABpcjsdp7Uuwiy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "offset": 26,
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
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "003437c5-c1e3-41a5-9bbd-494664fcd084",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QhDMZptTy7Skw1ki6xuz7p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 387,
      "cache_read_input_tokens": 48899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 387
      },
      "output_tokens": 70,
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

_source line 36 · 2026-05-23T10:18:15.569Z_

<details><summary>↩ Tool result · `toolu_013MHs28pxABpcjsdp7Uuwiy`</summary>

```text
26	The primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \texttt{stop\_gradient}, the encoder receives gradients from $\mathcal{L}_\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.
27	
28	Gradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective.
29	
30	We hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \textit{[Detach+LN results pending (plan\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}
31	
32	The TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.
33	
34	\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}
35	\label{sec:cutoff_temporal}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "1a3b8057-4aba-4c88-8789-7b5a037dbbf3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
      "content": "The primary mechanism is forward-pass interference without compensating gradient signal. The auxiliary head contains BatchNorm2d layers that consume encoder feature statistics during the forward pass, modifying the batch-level statistics that the encoder representations are conditioned on. In the Full OCC and Random OCC conditions, the auxiliary loss sends gradients back through the encoder that allow it to adapt to these statistics---effectively co-optimizing the shared representations. With \\texttt{stop\\_gradient}, the encoder receives gradients from $\\mathcal{L}_\\text{action}$ alone and cannot adapt to the statistical perturbation introduced by the auxiliary head's forward computation. The encoder bears the cost of the auxiliary pathway (altered batch statistics, additional forward computation) without receiving the auxiliary-task training benefit that gradient flow provides. The 3.4pp CAR deficit relative to Vanilla, consistent across 3 seeds ($\\sigma = 0.002$), confirms that gradient flow is a necessary condition for the auxiliary task to avoid harming performance.\n\nGradient analysis at convergence provides complementary evidence. In two gradient-flow conditions analyzed thus far (Random OCC, Depth), the action gradient norm at the encoder is substantially higher than in the Detach condition. A complete four-condition comparison awaits the completion of ongoing retraining runs. This pattern is consistent with the forward-pass interference account: the auxiliary head's BatchNorm layers perturb encoder feature statistics, and without compensating auxiliary gradients, the encoder converges to a region where action gradients are attenuated. Action and occupancy gradients are approximately orthogonal (cosine similarity near zero); this orthogonality implies that the auxiliary task provides an independent gradient direction rather than a competing signal for the action objective.\n\nWe hypothesize that the specific mechanism is BatchNorm contamination in the auxiliary head. The head's two BatchNorm2d layers maintain running mean and variance buffers that are updated at every forward pass, regardless of gradient routing. In the Detach configuration, these running statistics accumulate information from the auxiliary pathway's activations across all training iterations, yet the encoder receives no auxiliary gradient that would allow it to adapt to the resulting distributional shift. The 1.2M-parameter auxiliary head thereby functions as an unoptimized parasitic pathway: it consumes encoder features and perturbs their batch-level statistics, while the encoder, trained on action loss alone, has no mechanism to compensate for the perturbation. If this account is correct, the Detach degradation reflects a normalization artifact rather than evidence that gradient flow per se provides a training benefit. A discriminating test replaces the auxiliary head's BatchNorm2d with LayerNorm, which normalizes per-sample and does not maintain cross-batch running statistics. \\textit{[Detach+LN results pending (plan\\_027, 3 seeds); if LN restores CAR to Vanilla level, BN interference is confirmed as the primary mechanism; if Detach+LN CAR remains below Vanilla, the gradient-flow effect is genuine and independent of normalization.]}\n\nThe TSR instability reveals a second consequence of gradient detachment. One Detach seed (seed~44) exhibits TSR = 0.624---a uniform collapse across all ten tasks---while its CAR (0.748) remains comparable to the other two seeds (0.746, 0.744). This dissociation suggests that the forward-pass interference affects action prediction and collision behavior through partially independent pathways: action learning is sensitive to initialization under detached gradients, while collision behavior (as measured by CAR) remains stable. Per-task analysis reveals two systematic weaknesses of the Detach condition across all seeds: Task~3 (CAR: 0.200, 0.140, 0.000) and Task~5 (TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040), indicating that gradient detachment consistently impairs performance on physically constrained tasks.\n\n\\subsection{Cutoff Reveals Temporal Requirements of Gradient Flow}\n\\label{sec:cutoff_temporal}",
      "numLines": 10,
      "startLine": 26,
      "totalLines": 76
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

Structure is correct now: L28 (gradient analysis) → L30 (new BN hypothesis paragraph) → L32 (TSR instability). All three are separate paragraphs.

**汇报：**

**(1) 数据合规检查**
- L28 梯度引用：只引用 Random OCC 和 Depth（有数据）vs Detach（有数据），并标注"A complete four-condition comparison awaits..."。**合规，无需修正。**
- L46 "significantly"：无统计检验支撑，已改为 "does not improve CAR beyond Vanilla"（后面括号已提供数值解释）。
- 未发现引用 Full OCC / Vanilla / Cutoff 梯度数据的违规声明。

**(2) 新增段落**
- 位置：§5.2 L30，介于梯度分析段落 (L28) 和 TSR instability 段落 (L32) 之间。
- 内容：BatchNorm contamination hypothesis。具体阐述 BN running statistics 在 Detach 模式下的不对称耦合机制（1.2M 参数的 parasitic pathway），明确标记为 hypothesis ("We hypothesize", "If this account is correct")，末尾以 italic 标注 Detach+LN (plan_027) 作为 discriminating test 及两种结果的解释。
- 删除了原 L28 末尾 "Ongoing experiments replace..." 句（已被新段落更完整地覆盖）。
- 未引用 Full OCC 或 Vanilla 梯度数据。

**(3) 一致性**
- 与 §5.1 三个 hypothesis 一致：新段落提出 BN 作为 forward-pass interference 的具体机制，不与三个宏观假说冲突。
- 与 §5.3 cutoff 分析无交叉。
- 与 §5.4 practical recommendation 一致：recommendation 基于经验发现（"gradients must flow"），不依赖于 BN vs gradient-flow 的机制区分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "uuid": "50086638-de24-481f-a4ec-aa48db20120a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lgk5M3a6JTWn8utfC9WQQH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 49286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1067
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

_source line 38_

Structure is correct now: L28 (gradient analysis) → L30 (new BN hypothesis paragraph) → L32 (TSR instability). All three are separate paragraphs.

**汇报：**

**(1) 数据合规检查**
- L28 梯度引用：只引用 Random OCC 和 Depth（有数据）vs Detach（有数据），并标注"A complete four-condition comparison awaits..."。**合规，无需修正。**
- L46 "significantly"：无统计检验支撑，已改为 "does not improve CAR beyond Vanilla"（后面括号已提供数值解释）。
- 未发现引用 Full OCC / Vanilla / Cutoff 梯度数据的违规声明。

**(2) 新增段落**
- 位置：§5.2 L30，介于梯度分析段落 (L28) 和 TSR instability 段落 (L32) 之间。
- 内容：BatchNorm contamination hypothesis。具体阐述 BN running statistics 在 Detach 模式下的不对称耦合机制（1.2M 参数的 parasitic pathway），明确标记为 hypothesis ("We hypothesize", "If this account is correct")，末尾以 italic 标注 Detach+LN (plan_027) 作为 discriminating test 及两种结果的解释。
- 删除了原 L28 末尾 "Ongoing experiments replace..." 句（已被新段落更完整地覆盖）。
- 未引用 Full OCC 或 Vanilla 梯度数据。

**(3) 一致性**
- 与 §5.1 三个 hypothesis 一致：新段落提出 BN 作为 forward-pass interference 的具体机制，不与三个宏观假说冲突。
- 与 §5.3 cutoff 分析无交叉。
- 与 §5.4 practical recommendation 一致：recommendation 基于经验发现（"gradients must flow"），不依赖于 BN vs gradient-flow 的机制区分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 209713,
  "duration_api_ms": 210330,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "cc31fcc1-ac9e-4fe3-81f4-4fdf1a9a2313",
  "total_cost_usd": 0.6190485,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 38512,
    "cache_read_input_tokens": 278815,
    "output_tokens": 9476,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38512,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 571,
        "cache_read_input_tokens": 49286,
        "cache_creation_input_tokens": 1067,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1067
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1871,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001986,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 9476,
      "cacheReadInputTokens": 278815,
      "cacheCreationInputTokens": 38512,
      "webSearchRequests": 0,
      "costUSD": 0.6170625000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a153f1ca-5949-481e-8007-8db9995250c4"
}
```

</details>

---
