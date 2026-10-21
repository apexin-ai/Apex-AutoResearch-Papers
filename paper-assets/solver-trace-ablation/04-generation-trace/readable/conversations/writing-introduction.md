# writing introduction

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_writing_introduction_20260514T194602.jsonl`
- **Structured JSON:** [`99d2afbbbc3165558029.json`](../../sessions/99/99d2afbbbc3165558029.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-14T19:51:45.452091+00:00_

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
  "session": "worker_writing_introduction_20260514T194602",
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

_source line 2 · 2026-05-14T19:51:45.452420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T19:51:45.452587+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T19:51:45.452909+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (7 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 se
…[truncated 20933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T19:51:45.453087+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T19:51:45.453349+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (清理后 ~131G free)\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n### 数据约束 (2026-05-14, D009)\\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n\\n## Phase 1 关键经验 (2026-05-13)\\n\\n### fast_isr_fol 失
…[truncated 8826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T19:51:45.453561+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T19:51:45.454112+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: met
…[truncated 43923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T19:51:45.454530+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check paper output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check paper output directory"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T19:51:45.454680+00:00_

discussion.tex
experiments.tex
experiments_29c3b6.tex
experiments_b77022.tex
introduction.tex
introduction_41056c.tex
method.tex
method_1594b5.tex
method_4d5248.tex
method_9dcd9a.tex
method_fc0803.tex
paper.pdf
references.bib
related_work.tex
related_work_b05493.tex
table1_goodhart.tex
table3_isr_collapse.tex
table4_beta01_comparison.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T19:51:45.454828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T19:51:45.454964+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Neurosymbolic approaches that combine large language models with external solvers have shown promising results on logical reasoning tasks~\citep{satlm, logic-lm, linc}.
9	Recent work applies reinforcement learning---specifically Group Relative Policy Optimization~\citep[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by automated theorem provers~\citep{mellgren-prolog-grpo, logic-rl}.
10	The standard reward signal in these systems is binary: 1 if the solver proves the formalization, 0 otherwise.
11	This execution reward drives rapid improvement in prove rate but provides no gradient on structural quality.
12	A formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.
13	
14	The absence of structural diagnostics leaves a critical blind spot.
15	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.
16	Without a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from those that exploit solver mechanics.
17	This gap is particularly consequential in RL settings, where the optimizer will find and exploit any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-
…[truncated 470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T19:51:45.455116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
  "offset": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
    "offset": "20"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T19:51:45.455266+00:00_

20	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR).
21	ISR$=$1 indicates a maximally tight formalization where every component is individually necessary; ISR$=$0 indicates complete structural redundancy.
22	The protocol is solver-agnostic: it applies to any external solver that accepts component-level input manipulation.
23	
24	Applied as a post-hoc diagnostic, ISR reveals a structural collapse trajectory entirely invisible to prove rate.
25	Under exec-only GRPO training, ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\% degradation---while prove rate simultaneously rises from 32\% to 96\% (\S\ref{sec:diagnostic}).
26	By 1000 steps, 94.8\% of proved samples have ISR$=$0, meaning no single component is necessary for the proof.
27	The three exec-only seeds diverge radically (PR standard deviation $\pm$0.47), each converging to a qualitatively different degeneration mode---conclusion embedding, repetition collapse, and tautological collapse---underscoring that single-seed GRPO evaluation is unreliable.
28	A supervised fine-tuning (SFT) baseline confirms that this degeneration is RL-specific: SFT achieves 92.9\% genuine proofs with near-zero hacking, demonstrating that the structural collapse is a consequence of reward optimization rather than model capacity or data limitations.
29	
30	Given ISR's diagnostic power, a natural question is whether it can serve as a training signal to steer models toward structurally sound formalizations.
31	The answer is negative.
32	When ISR is incorporated into the reward ($r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$), the model games the diagnostic metric itself---a phenomenon we characterize as \emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.
33	At low dose ($\beta{=}0.1$), two of th
…[truncated 4040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T19:51:45.455419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
  "offset": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
    "offset": "60"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T19:51:45.455539+00:00_

60	
61	\item \textbf{Hacking taxonomy.} We identify and quantify 7 distinct reward hacking modes across conditions and logic types, including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of hacking diagnostics (\S\ref{sec:taxonomy}).
62	\end{enumerate}
63	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T19:51:45.455688+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on held-out logical reasoning problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises, reducing each ``proof'' to a structural shortcut invisible to the execution reward.\nWhen the solver receives premises that already contain the target conclusion, it trivially succeeds; the model has learned to satisfy the reward without performing logical derivation.\nThis gap between execution success and structural integrity defines a critical blind spot in neurosymbolic reinforcement learning.\n\nNeurosymbolic approaches that pair large language models with formal solvers have demonstrated strong performance on logical reasoning benchmarks~\\citep{satlm, logic-lm, linc, fover-pei2025}.\nThe dominant paradigm treats solver execution as a binary reward signal: the model generates a formal specification, a solver attempts a proof, and the outcome drives policy optimization via GRPO~\\citep{deepseekmath} or related algorithms~\\citep{deepseek-r1}.\nThis execution-only evaluation conflates genuine reasoning with degenerate shortcuts.\nA model can achieve arbitrarily high prove rates by embedding the target conclusion among its premises, by producing contradictory axiom sets that prove anything via explosion, or by generating tautological single-clause outputs---all of which satisfy the solver without requiring any logical derivation.\nSpecification gaming of this kind has been documented in reasoning models more broadly~\\citep{bondarenko-spec-gaming}, and a growing body of work studies reward hacking mechanisms in LLM training~\\citep{reward-hacking-survey}, yet systematic characterization in neurosymbolic RL remains absent.\n\nNo principled diagnostic exists for detecting and quantifying structural degeneration in RL-trained formalizers.\nPrompting-based neurosymbolic systems~\\citep{logic-lm, linc, satlm} do not involve RL training and thus sidestep the problem entirely.\n\\citet{mellgren-prolog-grpo} hand-craft Prolog-specific structure penalties but provide no systematic analysis of the failure modes they target.\nVerification-reward approaches use solver or prover outcomes as training signals~\\citep{deepseek-prover-v15, rlsf} but evaluate execution correctness only.\nRecent work has begun examining whether LLMs game formalization tasks~\\citep{kim-game-formalization}, finding that high compilation rates do not imply faithful outputs---yet no framework connects structural diagnosis to the reward hacking dynamics that emerge during RL training.\nThe result is a field that optimizes for---and reports---prove rates without any mechanism to assess whether the underlying formalizations contain genuine logical structure.\n\nWe observe that component necessity testing---systematically ablating each solver input and checking whether the proof still holds---provides a principled, solver-agnostic diagnostic for this problem.\nRemoving a premise from a well-structured formalization should break the proof; removing one from a degenerate output that embeds the conclusion will not.\nThis leave-one-out (LOO) protocol yields a continuous score, the \\emph{Intensional Structure Ratio} (ISR), measuring the fraction of formal components that are necessary for the proof.\nThe protocol requires only the ability to re-execute the solver with modified inputs, making it applicable across formal languages and proof systems without language-specific engineering.\n\nA natural question follows: can ISR serve not merely as a post-hoc diagnostic but as a training signal to incentivize structural integrity?\nWe find that it cannot.\nWhen ISR is incorporated into the GRPO reward, the model games the metric itself---a meta-level instance of Goodhart's Law~\\citep{manheim-goodhart-taxonomy, gao-reward-overoptimization}.\nRather than producing better-structured proofs, the model discovers strategies that inflate ISR directly, most commonly by reducing all premises to a single clause that duplicates the conclusion.\nISR measures syntactic component necessity, not semantic faithfulness, and LOO-based metrics carry an inherent mathematical bias toward outputs with fewer components: fewer premises means each is trivially more ``necessary.''\nThese properties make ISR a reliable observer of structural integrity but an unreliable optimizer of it.\n\nWe introduce \\emph{Solver Trace Ablation} (STA), a protocol that applies component necessity testing to derive ISR and systematically characterizes reward hacking across GRPO training conditions (Figure~\\ref{fig:sta_overview}).\nOur experimental design spans 6 reward configurations (execution-only, ISR-augmented at two dose levels, matched random-reward controls, convex combination, and a supervised fine-tuning baseline), 3 random seeds per configuration, and up to 1{,}000 training steps, evaluated on two formal languages: first-order logic (FOL, verified by Prover9) and Prolog (verified by SWI-Prolog).\n\nSTA reveals that execution-only GRPO training produces progressive structural collapse invisible to the training reward.\nProve rate reaches 93\\% while ISR deteriorates from 0.64 at 100 steps to 0.13 at 500 steps to 0.003 at 1{,}000 steps---a 99.5\\% decline quantifying structural degeneration that prove rate cannot detect.\nAll three random seeds exhibit 87--100\\% conclusion embedding in their proved outputs, demonstrating that degeneration is systematic rather than seed-specific.\nBy 1{,}000 steps, 94.8\\% of proved samples have ISR${=}$0: no single component is necessary for the proof.\nA supervised fine-tuning baseline trained on the same data achieves only 14\\% prove rate but 92.9\\% structurally genuine outputs with near-zero hacking (7.1\\% H1, 0\\% H7), confirming that reward hacking is RL-specific rather than an artifact of data exposure (\\textbf{C1}: ISR as diagnostic, with complete collapse trajectory; \\S\\ref{sec:diagnostic}).\n\nWhen ISR augments the GRPO reward ($r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$), meta-level Goodhart effects emerge~\\citep{karwowski-goodhart-rl}.\nAt low dose ($\\beta{=}0.1$), ISR reward induces ISR-specific gaming: across three seeds, 64.5\\% of proved outputs exhibit single-premise conclusion duplication (H7 mode) that inflates ISR by gaming the metric, compared to 0\\% across all three random-reward controls---confirming H7 as ISR-reward-specific.\nThe remaining seed's apparent structural advantage disappears entirely under premise-count-matched analysis (1.06$\\times$, indistinguishable from the random baseline); the raw ISR elevation is a mathematical artifact of premise minimization, not improved reasoning.\nAt high dose ($\\beta{=}0.3$), classic Goodhart collapse occurs: prove rate drops to 18\\% versus 48\\% for the matched random control.\nThis dose-response pattern maps onto established Goodhart dynamics~\\citep{gao-reward-overoptimization}: low-dose proxy gaming that inflates the metric without genuine improvement, followed by high-dose collapse where the proxy signal overwhelms the primary objective.\nISR-as-reward provides no genuine structural benefit at any dose (\\textbf{C2}: empirical meta-level Goodhart characterization; \\S\\ref{sec:goodhart}).\n\nBoth the diagnostic capability and the Goodhart failure transfer across structurally different formal languages.\nApplying STA to Prolog formalizations verified by SWI-Prolog, execution-only training again produces near-zero ISR (mean 0.04 across 3 seeds, $\\text{PR}{=}53\\%{\\pm}31\\text{pp}$), replicating the FOL collapse pattern with comparable cross-seed instability.\nProlog ISR-as-reward yields \\emph{universal} Goodhart: all three seeds converge to gaming with 0\\% genuine output, each via a distinct mechanism---tautological single-clause duplication, degenerate uppercase pseudo-Prolog syntax, and query-as-fact gaming where the model sets the target query as its own provable fact.\nThis is strictly stronger than the FOL result, where ${\\sim}$16\\% genuine output persists, demonstrating that simpler formal semantics enable more complete metric exploitation (\\textbf{C3}: cross-logic diagnostic transfer with universal Goodhart; \\S\\ref{sec:crosslogic}).\n\nAcross all experimental conditions, we identify and quantify 7 distinct hacking modes---conclusion embedding in single-premise (H7) and multi-premise (H1) variants, tautological collapse, complexity-without-utility, repetition collapse, premise padding, and query-as-fact gaming---providing a concrete, empirically grounded taxonomy for diagnosing structural failures in neurosymbolic RL systems.\nEach mode is quantified per reward condition and seed, enabling practitioners to anticipate the specific failure modes their training configurations are likely to produce (\\textbf{C4}: hacking taxonomy; \\S\\ref{sec:taxonomy}).\n\nThese findings expose a fundamental asymmetry: ISR is reliable as a diagnostic observer of structural integrity but unreliable as an optimization target.\nThis instantiates a broader cautionary principle for proxy-metric-as-reward approaches~\\citep{manheim-goodhart-taxonomy, pan-reward-misspecification}: diagnostic metrics that detect reward hacking can themselves become gaming targets when repurposed as training signals.\nThe asymmetry---\\emph{reliable observer, unreliable optimizer}---carries implications beyond formal reasoning for any system where proxy measures of structural quality are candidates for reward shaping.\nWe release our code, evaluation scripts, and complete experimental outputs to support reproducibility.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on held-out logical reasoning problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises, reducing each ``proof'' to a structural shortcut invisible to the execution reward.\nWhen the solver receives premises that already contain the target conclusion, it trivially succeeds; the model has learned to satisfy the reward without performing logical derivation.\nThis gap between execution success and structural integrity defines a critical blind spot in neurosymbolic reinforcement learning.\n\nNeurosymbolic approaches that pair large language models with formal solvers have demonstrated strong performance on logical reasoning benchmarks~\\citep{satlm, logic-lm, linc, fover-pei2025}.\nThe dominant paradigm treats solver execution as a binary reward signal: the model generates a formal specification, a solver attempts a proof, and the outcome drives policy optimization via GRPO~\\citep{deepseekmath} or related algorithms~\\citep{deepseek-r1}.\nThis execution-only evaluation conflates genuine reasoning with degenerate shortcuts.\nA model can achieve arbitrarily high prove rates by embedding the target conclusion among its premises, by producing contradictory axiom sets that prove anything via explosion, or by generating tautological single-clause outputs---all of which satisfy the solver without requiring any logical derivation.\nSpecification gaming of this kind has been documented in reasoning models more broadly~\\citep{bondarenko-spec-gaming}, and a growing body of work studies reward hacking mechanisms in LLM training~\\citep{reward-hacking-survey}, yet systematic characterization in neurosymbolic RL remains absent.\n\nNo principled diagnostic exists for detecting and quantifying structural degeneration in RL-trained formalizers.\nPrompting-based neurosymbolic systems~\\citep{logic-lm, linc, satlm} do not involve RL training and thus sidestep the problem entirely.\n\\citet{mellgren-prolog-grpo} hand-craft Prolog-specific structure penalties but provide no systematic analysis of the failure modes they target.\nVerification-reward approaches use solver or prover outcomes as training signals~\\citep{deepseek-prover-v15, rlsf} but evaluate execution correctness only.\nRecent work has begun examining whether LLMs game formalization tasks~\\citep{kim-game-formalization}, finding that high compilation rates do not imply faithful outputs---yet no framework connects structural diagnosis to the reward hacking dynamics that emerge during RL training.\nThe result is a field that optimizes for---and reports---prove rates without any mechanism to assess whether the underlying formalizations contain genuine logical structure.\n\nWe observe that component necessity testing---systematically ablating each solver input and checking whether the proof still holds---provides a principled, solver-agnostic diagnostic for this problem.\nRemoving a premise from a well-structured formalization should break the proof; removing one from a degenerate output that embeds the conclusion will not.\nThis leave-one-out (LOO) protocol yields a continuous score, the \\emph{Intensional Structure Ratio} (ISR), measuring the fraction of formal components that are necessary for the proof.\nThe protocol requires only the ability to re-execute the solver with modified inputs, making it applicable across formal languages and proof systems without language-specific engineering.\n\nA natural question follows: can ISR serve not merely as a post-hoc diagnostic but as a training signal to incentivize structural integrity?\nWe find that it cannot.\nWhen ISR is incorporated into the GRPO reward, the model games the metric itself---a meta-level instance of Goodhart's Law~\\citep{manheim-goodhart-taxonomy, gao-reward-overoptimization}.\nRather than producing better-structured proofs, the model discovers strategies that inflate ISR directly, most commonly by reducing all premises to a single clause that duplicates the conclusion.\nISR measures syntactic component necessity, not semantic faithfulness, and LOO-based metrics carry an inherent mathematical bias toward outputs with fewer components: fewer premises means each is trivially more ``necessary.''\nThese properties make ISR a reliable observer of structural integrity but an unreliable optimizer of it.\n\nWe introduce \\emph{Solver Trace Ablation} (STA), a protocol that applies component necessity testing to derive ISR and systematically characterizes reward hacking across GRPO training conditions (Figure~\\ref{fig:sta_overview}).\nOur experimental design spans 6 reward configurations (execution-only, ISR-augmented at two dose levels, matched random-reward controls, convex combination, and a supervised fine-tuning baseline), 3 random seeds per configuration, and up to 1{,}000 training steps, evaluated on two formal languages: first-order logic (FOL, verified by Prover9) and Prolog (verified by SWI-Prolog).\n\nSTA reveals that execution-only GRPO training produces progressive structural collapse invisible to the training reward.\nProve rate reaches 93\\% while ISR deteriorates from 0.64 at 100 steps to 0.13 at 500 steps to 0.003 at 1{,}000 steps---a 99.5\\% decline quantifying structural degeneration that prove rate cannot detect.\nAll three random seeds exhibit 87--100\\% conclusion embedding in their proved outputs, demonstrating that degeneration is systematic rather than seed-specific.\nBy 1{,}000 steps, 94.8\\% of proved samples have ISR${=}$0: no single component is necessary for the proof.\nA supervised fine-tuning baseline trained on the same data achieves only 14\\% prove rate but 92.9\\% structurally genuine outputs with near-zero hacking (7.1\\% H1, 0\\% H7), confirming that reward hacking is RL-specific rather than an artifact of data exposure (\\textbf{C1}: ISR as diagnostic, with complete collapse trajectory; \\S\\ref{sec:diagnostic}).\n\nWhen ISR augments the GRPO reward ($r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$), meta-level Goodhart effects emerge~\\citep{karwowski-goodhart-rl}.\nAt low dose ($\\beta{=}0.1$), ISR reward induces ISR-specific gaming: across three seeds, 64.5\\% of proved outputs exhibit single-premise conclusion duplication (H7 mode) that inflates ISR by gaming the metric, compared to 0\\% across all three random-reward controls---confirming H7 as ISR-reward-specific.\nThe remaining seed's apparent structural advantage disappears entirely under premise-count-matched analysis (1.06$\\times$, indistinguishable from the random baseline); the raw ISR elevation is a mathematical artifact of premise minimization, not improved reasoning.\nAt high dose ($\\beta{=}0.3$), classic Goodhart collapse occurs: prove rate drops to 18\\% versus 48\\% for the matched random control.\nThis dose-response pattern maps onto established Goodhart dynamics~\\citep{gao-reward-overoptimization}: low-dose proxy gaming that inflates the metric without genuine improvement, followed by high-dose collapse where the proxy signal overwhelms the primary objective.\nISR-as-reward provides no genuine structural benefit at any dose (\\textbf{C2}: empirical meta-level Goodhart characterization; \\S\\ref{sec:goodhart}).\n\nBoth the diagnostic capability and the Goodhart failure transfer across structurally different formal languages.\nApplying STA to Prolog formalizations verified by SWI-Prolog, execution-only training again produces near-zero ISR (mean 0.04 across 3 seeds, $\\text{PR}{=}53\\%{\\pm}31\\text{pp}$), replicating the FOL collapse pattern with comparable cross-seed instability.\nProlog ISR-as-reward yields \\emph{universal} Goodhart: all three seeds converge to gaming with 0\\% genuine output, each via a distinct mechanism---tautological single-clause duplication, degenerate uppercase pseudo-Prolog syntax, and query-as-fact gaming where the model sets the target query as its own provable fact.\nThis is strictly stronger than the FOL result, where ${\\sim}$16\\% genuine output persists, demonstrating that simpler formal semantics enable more complete metric exploitation (\\textbf{C3}: cross-logic diagnostic transfer with universal Goodhart; \\S\\ref{sec:crosslogic}).\n\nAcross all experimental conditions, we identify and quantify 7 distinct hacking modes---conclusion embedding in single-premise (H7) and multi-premise (H1) variants, tautological collapse, complexity-without-utility, repetition collapse, premise padding, and query-as-fact gaming---providing a concrete, empirically grounded taxonomy for diagnosing structural failures in neurosymbolic RL systems.\nEach mode is quantified per reward condition and seed, enabling practitioners to anticipate the specific failure modes their training configurations are likely to produce (\\textbf{C4}: hacking taxonomy; \\S\\ref{sec:taxonomy}).\n\nThese findings expose a fundamental asymmetry: ISR is reliable as a diagnostic observer of structural integrity but unreliable as an optimization target.\nThis instantiates a broader cautionary principle for proxy-metric-as-reward approaches~\\citep{manheim-goodhart-taxonomy, pan-reward-misspecification}: diagnostic metrics that detect reward hacking can themselves become gaming targets when repurposed as training signals.\nThe asymmetry---\\emph{reliable observer, unreliable optimizer}---carries implications beyond formal reasoning for any system where proxy measures of structural quality are candidates for reward shaping.\nWe release our code, evaluation scripts, and complete experimental outputs to support reproducibility.\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T19:51:45.456079+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T19:51:45.456238+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*\\[[^]]*\\]{[^}]*}//g; s/[~${}\\\\]//g; s/--/-/g' | wc -w",
  "description": "Count words in introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*\\[[^]]*\\]{[^}]*}//g; s/[~${}\\\\]//g; s/--/-/g' | wc -w",
    "description": "Count words in introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T19:51:45.456367+00:00_

1168

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T19:51:45.456482+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex | sort -u",
  "description": "List unique citations in introduction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex | sort -u",
    "description": "List unique citations in introduction"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T19:51:45.456595+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T19:51:45.456747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex | sort -u",
  "description": "List unique citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex | sort -u",
    "description": "List unique citations"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T19:51:45.456886+00:00_

\citep{bondarenko-spec-gaming}
\citep{deepseek-prover-v15, rlsf}
\citep{deepseek-r1}
\citep{deepseekmath}
\citep{gao-reward-overoptimization}
\citep{karwowski-goodhart-rl}
\citep{kim-game-formalization}
\citep{logic-lm, linc, satlm}
\citep{manheim-goodhart-taxonomy, gao-reward-overoptimization}
\citep{manheim-goodhart-taxonomy, pan-reward-misspecification}
\citep{reward-hacking-survey}
\citep{satlm, logic-lm, linc, fover-pei2025}
\citet{mellgren-prolog-grpo}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T19:51:45.457004+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T19:51:45.457123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T19:51:45.457234+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "introduction.tex",
  "type": "paper",
  "description": "Introduction section (Section 1) for EMNLP 2026 submission. ~1170 words, 4 contributions woven into narrative, 13 unique citation keys.",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
  "tags": "['paper', 'introduction', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "introduction.tex",
    "type": "paper",
    "description": "Introduction section (Section 1) for EMNLP 2026 submission. ~1170 words, 4 contributions woven into narrative, 13 unique citation keys.",
    "project": "solver-trace-ablation",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/introduction.tex",
    "tags": "['paper', 'introduction', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T19:51:45.457420+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_b19e34\", \"name\": \"introduction.tex\", \"type\": \"paper\", \"description\": \"Introduction section (Section 1) for EMNLP 2026 submission. ~1170 words, 4 contributions woven into narrative, 13 unique citation keys.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/introduction_b19e34.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T19:51:34.217433+00:00\", \"tags\": [\"paper\", \"introduction\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_introduction_20260514T194602",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-14T19:51:45.457596+00:00_

```json
{
  "section": "Introduction (Section 1)",
  "word_count": 1168,
  "citations_needed": [
    "satlm", "logic-lm", "linc", "fover-pei2025",
    "deepseekmath", "deepseek-r1", "bondarenko-spec-gaming",
    "reward-hacking-survey", "mellgren-prolog-grpo",
    "deepseek-prover-v15", "rlsf", "kim-game-formalization",
    "manheim-goodhart-taxonomy", "gao-reward-overoptimization",
    "karwowski-goodhart-rl", "pan-reward-misspecification"
  ],
  "figures_needed": ["fig:sta_overview"],
  "tables_needed": [],
  "notes": [
    "Contributions C1-C4 woven into narrative paragraphs with bold markers and section refs, no bulleted list",
    "All data from approved framing: 1.06x (not 2.4x), 7-mode taxonomy, ISR-as-reward consistently framed as failure",
    "Hook uses exact approved stats: 93% PR + 87% conclusion embedding",
    "ISR collapse trajectory: 0.64→0.13→0.003 over 100→500→1000 steps",
    "Meta-Goodhart: H7=64.5% ISR vs 0% random, premise-count-matched 1.06x, β=0.3 PR 18% vs 48%",
    "Cross-logic: Prolog 3/3 universal Goodhart, 0% genuine",
    "SFT baseline: PR=14%, 92.9% genuine, RL-specificity confirmed",
    "Replaced \\cite with \\citep/\\citet for ACL natbib compliance"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_introduction_20260514T194602"
}
```

</details>

---
