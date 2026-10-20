# paper intro rewrite d056

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_intro-rewrite-d056_20260517T234428.jsonl`
- **Structured JSON:** [`c159361ca3aa1ba008ea.json`](../../sessions/c1/c159361ca3aa1ba008ea.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-17T23:48:07.392663+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T23:48:07.392982+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T23:48:07.393165+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T23:48:07.393491+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper_framing.md\", \"content\": \"# Paper Framing — recovery_aware_struct_prune\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 submission)\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight (Recovery Capacity Gradient)\\nStructural pruning criterion determines post-RLVR recovery capacity of reasoning LLMs. We discover a **recovery capacity gradient** across pruning methods during GRPO training: CKA-only (pure representational diversity preservation) enables **active super-recovery** from transient RL instability, while gradient-based importance scoring progressively destroys this capacity.\\n\\nThe gradient: **CKA-only > Random > Standard > RASP**\\n\\nMechanism: Gradient importance scoring (used in Standard and RASP) removes structures that are \\\"unimportant\\\" by gradient metrics but **representationally unique** — precisely the diversity that RL exploration requires. CKA-only scoring removes only truly redundant structures (high pairwise similarity), preserving the full representational vocabulary that enables policy recovery from training perturbations.\\n\\nSeparately, GRPO reward-accuracy decoupling is primarily an **in-distribution saturation effect**: on GSM8K (saturated), reward rises but accuracy is unchanged; on MATH-500 (unsaturated), GRPO provides only marginal improvement for pruned models (+2-3pp), far below unpruned baseline (73.6%).\\n\\n## Core Claims (2 + 1 observation)\\n\\n### C1: GRPO reward-accuracy decoupling is in-distribution specific (saturation effect)\\nGRPO does not improve reasoning accuracy on saturated benchmarks for ANY model: unpruned (81.27% = SFT 81.27%, identical 1072/1319), Standard-pruned (58.91% vs SFT 59.29%), RASP-pruned (60.65% vs SFT 61.49%). Reward rises dramatically (unpruned: 0→0.661) but accuracy is unchanged on GSM8K.\\n\\nOn MATH-500 (unsaturated OOD benchmar
…[truncated 11893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T23:48:07.393682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T23:48:07.393891+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large Language Models (LLMs) trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong mathematical reasoning~\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.
5	Structured pruning, which removes entire attention heads or MLP channels, provides a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
6	Because structured pruning at moderate sparsity severely degrades reasoning ability, a post-pruning recovery stage is essential.
7	The standard compression pipeline therefore proceeds in three stages: prune, recover via Supervised Fine-Tuning (SFT), then align via RLVR to restore reasoning quality.
8	This final alignment step appears straightforward: on an unpruned DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, 100 steps of Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) raises the reward from 0 to 0.661.
9	Yet accuracy on GSM8K~\citep{cobbe2021gsm8k} remains exactly 81.27\%, with 1,072 of 1,319 test problems producing identical correct answers before and after alignment.
10	The reward improvement is an illusion: GRPO learns to produce outputs that score higher rewards without solving additional problems.
11	
12	This observation has immediate practical consequences for the compression pipeline.
13	\citet{selfhealing2025} report that RLVR-based recovery restores pruned reasoning models to 95\%+ of original performance at 25\% compression, establishing RLVR as the preferred recovery paradigm.
14	However, their evaluation reports only final-checkpoint accuracy and does not document per-step training dynamics during GRPO.
15	If GRPO reward gains fail to reflect genuine reasoning improvement even on unpruned models, the claim that RLVR ``recovers'' pruned models demands scrutiny.
16	The problem becomes a
…[truncated 4006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T23:48:07.394227+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\nThe choice of which structures to prune from a reasoning LLM determines whether the model can sustain reinforcement learning alignment.\nCurrent compression pipelines treat this choice as independent of downstream training: structured pruning removes entire attention heads or MLP channels to reduce memory and latency~\\citep{llmpruner2023,graspprune2026}, Supervised Fine-Tuning (SFT) recovers task accuracy, and Reinforcement Learning with Verifiable Rewards (RLVR) restores reasoning quality~\\citep{deepseek2025r1,shao2024grpo}.\nEach stage is optimized in isolation.\nWe show that this separation fails: the pruning criterion fundamentally controls what we term \\textbf{recovery capacity}, the model's ability to recover from the instability that RL training introduces.\n\nTwo findings expose this failure.\nFirst, GRPO reward gains on GSM8K~\\citep{cobbe2021gsm8k} do not reflect genuine reasoning improvement.\nOn an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, 100 steps of Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) raise the reward from 0 to 0.661, yet accuracy remains exactly 81.27\\%, with 1,072 of 1,319 test problems producing identical correct answers before and after alignment.\nThe same pattern holds for pruned models: Standard-pruned accuracy is 58.91\\% after GRPO versus 59.29\\% after SFT.\nThis decoupling is an in-distribution saturation effect.\nGSM8K accuracy is near ceiling, so reward optimization reshapes output format without solving new problems.\nOn MATH-500, an unsaturated out-of-distribution benchmark, GRPO provides only marginal gains for pruned models (+2--3 percentage points), far below the unpruned baseline of 73.6\\%.\nSecond, GRPO training on pruned models can trigger complete collapse: gradient norms approach zero and the model stops producing diverse outputs.\n\\citet{selfhealing2025} claim that RLVR recovers pruned reasoning models to 95\\%+ of original performance, but their evaluation uses a single pruning method and reports only final-checkpoint accuracy without per-step training dynamics.\n\nExisting structured pruning methods for reasoning LLMs optimize for post-pruning quality without studying downstream alignment.\nGRASPrune~\\citep{graspprune2026} introduces global gating for budgeted compression.\nRESP~\\citep{resp2025} uses reasoning-trace calibration.\nLLM-Pruner~\\citep{llmpruner2023} and Bonsai~\\citep{bonsai2025} target general LLM compression.\nPASER~\\citep{paser2025} optimizes recovery data selection, and PAT~\\citep{pat2025} proposes pruning-aware tuning.\nNone compare multiple pruning criteria under RL alignment.\n\\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations: RL compresses solution paths while SFT expands them.\nThis divergence suggests that pruning decisions could substantially affect RL trainability, yet no prior work has tested this hypothesis.\n\nWe present the first controlled comparison of four structural pruning criteria under identical GRPO training on DeepSeek-R1-Distill-Qwen-7B at 20\\% structured sparsity.\nThe four criteria span a spectrum of representational diversity preservation: CKA-only scoring removes only structures with high pairwise Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}) overlap and preserves all representationally unique structures; Random scoring provides an unbiased baseline; Standard importance-only scoring removes structures with lowest gradient-based importance; and Recovery-Aware Structured Pruning (\\rasp{}) combines importance with CKA-based functional overlap in a composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$.\nThese four methods reveal a \\textbf{recovery capacity gradient} during GRPO.\nCKA-only pruning enables \\textbf{active super-recovery}: the fraction of zero-standard-deviation outputs drops from 0.35 to 0.125, \\emph{below} the initial baseline of 0.175, with reward reaching 0.308.\nRandom pruning stagnates after partial recovery (reward 0.190).\nStandard pruning exhibits borderline collapse with a transient dip at step 60 (reward 0.065).\nRASP collapses permanently at step 10 (reward 0.021).\nThe ordering (CKA-only $>$ Random $>$ Standard $>$ RASP) follows the degree of preserved representational diversity.\nGradient importance scoring, the industry standard, removes structures scored ``unimportant'' by gradient metrics that are in fact representationally unique, and thereby destroys the exploration diversity that RL training requires.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We show that GRPO reward-accuracy decoupling on pruned and unpruned models is primarily an in-distribution saturation effect: reward rises while accuracy remains unchanged on GSM8K (near ceiling); on MATH-500 (unsaturated), GRPO provides only marginal out-of-distribution improvement for pruned models (\\S\\ref{sec:grpo_failure}).\n    \\item We discover a recovery capacity gradient across four pruning criteria under GRPO training: CKA-only enables active super-recovery (output diversity drops 29\\% below initial baseline), Random stagnates, Standard exhibits borderline collapse, and RASP collapses permanently. This gradient is predicted by preserved representational diversity and reveals that gradient importance scoring is actively harmful for post-pruning RL alignment (\\S\\ref{sec:collapse_analysis}).\n    \\item We observe that SFT partially equalizes all scoring methods (59--64\\%, $p>0.1$ for most pairs) and that a universal 30\\% sparsity cliff collapses all methods. The 20--25\\% sparsity range is therefore the operating regime where pruning criterion determines RL trainability (\\S\\ref{sec:tradeoff}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\nThe choice of which structures to prune from a reasoning LLM determines whether the model can sustain reinforcement learning alignment.\nCurrent compression pipelines treat this choice as independent of downstream training: structured pruning removes entire attention heads or MLP channels to reduce memory and latency~\\citep{llmpruner2023,graspprune2026}, Supervised Fine-Tuning (SFT) recovers task accuracy, and Reinforcement Learning with Verifiable Rewards (RLVR) restores reasoning quality~\\citep{deepseek2025r1,shao2024grpo}.\nEach stage is optimized in isolation.\nWe show that this separation fails: the pruning criterion fundamentally controls what we term \\textbf{recovery capacity}, the model's ability to recover from the instability that RL training introduces.\n\nTwo findings expose this failure.\nFirst, GRPO reward gains on GSM8K~\\citep{cobbe2021gsm8k} do not reflect genuine reasoning improvement.\nOn an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, 100 steps of Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) raise the reward from 0 to 0.661, yet accuracy remains exactly 81.27\\%, with 1,072 of 1,319 test problems producing identical correct answers before and after alignment.\nThe same pattern holds for pruned models: Standard-pruned accuracy is 58.91\\% after GRPO versus 59.29\\% after SFT.\nThis decoupling is an in-distribution saturation effect.\nGSM8K accuracy is near ceiling, so reward optimization reshapes output format without solving new problems.\nOn MATH-500, an unsaturated out-of-distribution benchmark, GRPO provides only marginal gains for pruned models (+2--3 percentage points), far below the unpruned baseline of 73.6\\%.\nSecond, GRPO training on pruned models can trigger complete collapse: gradient norms approach zero and the model stops producing diverse outputs.\n\\citet{selfhealing2025} claim that RLVR recovers pruned reasoning models to 95\\%+ of original performance, but their evaluation uses a single pruning method and reports only final-checkpoint accuracy without per-step training dynamics.\n\nExisting structured pruning methods for reasoning LLMs optimize for post-pruning quality without studying downstream alignment.\nGRASPrune~\\citep{graspprune2026} introduces global gating for budgeted compression.\nRESP~\\citep{resp2025} uses reasoning-trace calibration.\nLLM-Pruner~\\citep{llmpruner2023} and Bonsai~\\citep{bonsai2025} target general LLM compression.\nPASER~\\citep{paser2025} optimizes recovery data selection, and PAT~\\citep{pat2025} proposes pruning-aware tuning.\nNone compare multiple pruning criteria under RL alignment.\n\\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations: RL compresses solution paths while SFT expands them.\nThis divergence suggests that pruning decisions could substantially affect RL trainability, yet no prior work has tested this hypothesis.\n\nWe present the first controlled comparison of four structural pruning criteria under identical GRPO training on DeepSeek-R1-Distill-Qwen-7B at 20\\% structured sparsity.\nThe four criteria span a spectrum of representational diversity preservation: CKA-only scoring removes only structures with high pairwise Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}) overlap and preserves all representationally unique structures; Random scoring provides an unbiased baseline; Standard importance-only scoring removes structures with lowest gradient-based importance; and Recovery-Aware Structured Pruning (\\rasp{}) combines importance with CKA-based functional overlap in a composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$.\nThese four methods reveal a \\textbf{recovery capacity gradient} during GRPO.\nCKA-only pruning enables \\textbf{active super-recovery}: the fraction of zero-standard-deviation outputs drops from 0.35 to 0.125, \\emph{below} the initial baseline of 0.175, with reward reaching 0.308.\nRandom pruning stagnates after partial recovery (reward 0.190).\nStandard pruning exhibits borderline collapse with a transient dip at step 60 (reward 0.065).\nRASP collapses permanently at step 10 (reward 0.021).\nThe ordering (CKA-only $>$ Random $>$ Standard $>$ RASP) follows the degree of preserved representational diversity.\nGradient importance scoring, the industry standard, removes structures scored ``unimportant'' by gradient metrics that are in fact representationally unique, and thereby destroys the exploration diversity that RL training requires.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We show that GRPO reward-accuracy decoupling on pruned and unpruned models is primarily an in-distribution saturation effect: reward rises while accuracy remains unchanged on GSM8K (near ceiling); on MATH-500 (unsaturated), GRPO provides only marginal out-of-distribution improvement for pruned models (\\S\\ref{sec:grpo_failure}).\n    \\item We discover a recovery capacity gradient across four pruning criteria under GRPO training: CKA-only enables active super-recovery (output diversity drops 29\\% below initial baseline), Random stagnates, Standard exhibits borderline collapse, and RASP collapses permanently. This gradient is predicted by preserved representational diversity and reveals that gradient importance scoring is actively harmful for post-pruning RL alignment (\\S\\ref{sec:collapse_analysis}).\n    \\item We observe that SFT partially equalizes all scoring methods (59--64\\%, $p>0.1$ for most pairs) and that a universal 30\\% sparsity cliff collapses all methods. The 20--25\\% sparsity range is therefore the operating regime where pruning criterion determines RL trainability (\\S\\ref{sec:tradeoff}).\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T23:48:07.394619+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T23:48:07.394820+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
  "description": "Check for em-dash violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
    "description": "Check for em-dash violations"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T23:48:07.394966+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T23:48:07.395095+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
  "description": "Check for explanatory en-dash violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
    "description": "Check for explanatory en-dash violations"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T23:48:07.395221+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T23:48:07.395389+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
  "description": "Check for -ing participial phrase patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
    "description": "Check for -ing participial phrase patterns"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T23:48:07.395515+00:00_

14:GSM8K accuracy is near ceiling, so reward optimization reshapes output format without solving new problems.
36:Gradient importance scoring, the industry standard, removes structures scored ``unimportant'' by gradient metrics that are in fact representationally unique, and thereby destroys the exploration diversity that RL training requires.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-17T23:48:07.395713+00:00_

No violations. Both `ing,` hits are false positives (line 14 is `without + gerund`, line 36 is a noun appositive).

Introduction rewritten and saved. Key changes from D045:

- **Hook**: opens with "pruning criterion determines RL recovery capacity" instead of generic LLM intro
- **C1**: redefined from "universal decoupling" to **in-distribution saturation effect** (GSM8K ceiling + MATH-500 marginal gains)
- **C2 (main)**: **Recovery Capacity Gradient** across 4 methods (CKA-only > Random > Standard > RASP), with CKA-only super-recovery as the headline result
- **C3**: SFT equalization + 30% sparsity cliff as observation, establishing 20-25% operating regime
- **Core mechanism**: gradient importance scoring destroys representationally unique structures needed for RL exploration
- All existing citations preserved, no new ones fabricated, no AI style violations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_intro-rewrite-d056_20260517T234428"
}
```

</details>

---
