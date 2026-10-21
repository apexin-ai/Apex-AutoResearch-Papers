# writing related work

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_writing_related-work_20260514T194629.jsonl`
- **Structured JSON:** [`e1d1b80ddffb85be523c.json`](../../sessions/e1/e1d1b80ddffb85be523c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-14T19:49:25.232187+00:00_

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
  "session": "worker_writing_related-work_20260514T194629",
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

_source line 2 · 2026-05-14T19:49:25.232528+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T19:49:25.232723+00:00_

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
  "session": "worker_writing_related-work_20260514T194629",
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

_source line 4 · 2026-05-14T19:49:25.233054+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (7 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 se
…[truncated 20933 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T19:49:25.233228+00:00_

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
  "session": "worker_writing_related-work_20260514T194629",
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

_source line 6 · 2026-05-14T19:49:25.233810+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: met
…[truncated 43923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T19:49:25.234012+00:00_

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
  "session": "worker_writing_related-work_20260514T194629",
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

_source line 8 · 2026-05-14T19:49:25.234250+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (清理后 ~131G free)\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n### 数据约束 (2026-05-14, D009)\\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n\\n## Phase 1 关键经验 (2026-05-13)\\n\\n### fast_isr_fol 失
…[truncated 8826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T19:49:25.234456+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -d /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check paper output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -d /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check paper output directory exists"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T19:49:25.234586+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T19:49:25.234743+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\subsection{Neurosymbolic Reasoning with LLMs}\n\nA growing body of work augments LLMs with symbolic solvers for logical reasoning.\nLogic-LM \\cite{logic-lm} and LINC \\cite{linc} prompt LLMs to translate natural language into first-order logic for external provers, while SatLM \\cite{satlm} targets SAT solvers via declarative specifications.\nLoRP \\cite{lorp} extends this pipeline to Prolog through systematic FOL-to-Prolog translation, and FoVer \\cite{fover-pei2025} uses Z3 verification to assess formalization correctness.\nThese approaches rely on prompting rather than learned formalization, sidestepping the question of what happens when models are \\emph{trained} to produce solver inputs.\n\nWithin the RL paradigm, DeepSeekMath \\cite{deepseekmath} introduces GRPO for mathematical reasoning, and DeepSeek-R1 \\cite{deepseek-r1} demonstrates that GRPO alone can elicit chain-of-thought reasoning without supervised fine-tuning.\nLogic-RL \\cite{logic-rl} applies rule-based RL to synthetic logic puzzles, while Thought-Like-Pro \\cite{thought-like-pro} uses Prolog-verified trajectories as imitation learning targets.\nMost directly comparable, \\citet{mellgren-prolog-grpo} trains a 3B model via GRPO to generate Prolog, using hand-crafted structure penalties to encourage well-formed outputs.\n\nThese efforts share a common gap: none systematically diagnose the structural quality of learned formalizations beyond execution success.\nMellgren et al.'s structure penalties are task-specific and manually designed; prompting-based methods do not face reward hacking but also cannot scale formalization quality through training.\nBy contrast, we derive ISR from solver trace ablation as a general, solver-grounded diagnostic that quantifies component necessity without task-specific engineering, and use it to reveal structural degeneration invisible to execution rewards.\n\n\\subsection{Reward Shaping and Process Supervision}\n\nProcess supervision provides step-level training signal to complement outcome-based rewards.\n\\citet{lightman-verify-step} show that process reward models outperform outcome supervision for mathematical reasoning, establishing process-level feedback as a principled alternative to binary correctness signals.\nMath-Shepherd \\cite{math-shepherd} extends this to automated process supervision without human annotation, using completion-based estimation to label intermediate steps.\nIn the formal verification domain, RLSF \\cite{rlsf} extracts fine-grained token-level rewards from solver certificates, demonstrating that symbolic feedback can outperform scalar rewards for structured generation tasks.\nMore recently, Rubric-GRPO \\cite{rubric-grpo} uses structured multi-dimensional rubrics as GRPO reward, moving beyond scalar signals toward compositional reward design.\n\nA parallel line of work studies how auxiliary reward signals interact with primary objectives.\n\\citet{gao-effective-rl-reward} find that learned process and outcome reward models can \\emph{hurt} RL training relative to simple success-only reward, a finding that directly parallels our observation that ISR as auxiliary reward degrades prove rate.\nDeepSeek-Prover-V1.5 \\cite{deepseek-prover-v15} avoids this problem entirely by using binary Lean verification as GRPO reward, sidestepping graded proxy metrics.\n\nISR shares the motivation of process supervision---providing structural signal beyond binary outcomes---but differs in grounding: ISR is computed deterministically from solver behavior via leave-one-out ablation, not estimated from model rollouts or learned reward models.\nOur central finding is that this grounded process signal can itself become a target of optimization, exhibiting the same Goodhart dynamics it was designed to diagnose.\n\n\\subsection{Reward Hacking and Goodhart's Law}\n\nReward hacking---where agents exploit reward proxies without achieving intended objectives---is well-documented in reinforcement learning.\n\\citet{gao-reward-overoptimization} establish scaling laws for reward model overoptimization, showing that proxy reward and gold reward diverge predictably as optimization pressure increases.\n\\citet{skalse-reward-hacking} prove that for stochastic policies, any non-constant proxy reward is theoretically hackable, providing formal grounding for the ubiquity of the phenomenon.\n\\citet{manheim-goodhart-taxonomy} categorize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---offering vocabulary for classifying observed failure modes.\n\nEmpirical characterizations span multiple settings.\n\\citet{karwowski-goodhart-rl} give a geometric interpretation of Goodhart's Law in MDPs, showing that optimization past a critical point necessarily decreases the true objective.\n\\citet{pan-reward-misspecification} demonstrate dose-dependent degradation across nine environments, where more capable agents exploit misspecifications more aggressively.\n\\citet{kwa-catastrophic-goodhart} prove that KL regularization---the standard mitigation in RLHF---provably fails under heavy-tailed reward misspecification.\nRecent surveys \\cite{reward-hacking-survey} and empirical studies of specification gaming in reasoning models \\cite{bondarenko-spec-gaming,kim-game-formalization} confirm that reward hacking extends to frontier LLMs.\n\\citet{spurious-rewards} show that even random rewards can match ground-truth rewards under GRPO's group normalization, questioning the information content of structured reward signals.\n\nDespite this extensive theoretical and empirical foundation, Goodhart's Law has been studied primarily in RLHF with learned reward models and in classic RL environments.\nFormal reasoning with solver-grounded rewards---where the reward is computed by a deterministic verifier rather than a learned model---remains unexplored territory.\nOur work provides the first empirical characterization of Goodhart's Law in this setting, documenting both classical dose-dependent collapse ($\\beta{=}0.3$: prove rate drops from 48\\% to 18\\%) and a meta-level effect where the diagnostic proxy itself becomes a gaming target ($\\beta{=}0.1$: ISR-specific conclusion duplication in 2/3 seeds, with apparent structural gains attributable to premise minimization artifacts).\n\n\\subsection{Mutation Testing and Component Analysis}\n\nSolver Trace Ablation adapts ideas from mutation testing in software engineering.\n\\citet{demillo1978} introduce mutation testing---systematically perturbing program elements to assess test suite adequacy---and propose the coupling effect hypothesis: tests detecting simple mutations also detect complex ones.\n\\citet{jia-harman-survey} survey three decades of development in this paradigm, covering mutation operator design, cost reduction, and the equivalent mutant problem.\n\\citet{just-mutants-real-faults} validate that mutation-based adequacy correlates with real fault detection, supporting the premise that systematic perturbation provides meaningful quality signal.\n\nSTA applies a specific form of mutation testing---leave-one-out component ablation---to logical formulas rather than source code.\nEach clause in a formalization is removed in turn, and the solver is re-executed to determine whether the clause was necessary for the proof.\nThis is equivalent to first-order mutation with a deletion operator, directly inheriting the theoretical justification from the coupling effect \\cite{demillo1978,offutt-coupling}.\nISR is thus not a novel metric \\emph{per se}, but a known technique applied to a new domain; our contribution lies in using it to diagnose reward hacking in GRPO-trained formalizers and in characterizing its failure modes when repurposed as a training signal.\nWe also note connections to feature attribution methods in machine learning \\cite{jia-harman-survey}, where leave-one-out evaluation is standard for assessing feature importance, though our ablation targets solver inputs rather than model features.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\subsection{Neurosymbolic Reasoning with LLMs}\n\nA growing body of work augments LLMs with symbolic solvers for logical reasoning.\nLogic-LM \\cite{logic-lm} and LINC \\cite{linc} prompt LLMs to translate natural language into first-order logic for external provers, while SatLM \\cite{satlm} targets SAT solvers via declarative specifications.\nLoRP \\cite{lorp} extends this pipeline to Prolog through systematic FOL-to-Prolog translation, and FoVer \\cite{fover-pei2025} uses Z3 verification to assess formalization correctness.\nThese approaches rely on prompting rather than learned formalization, sidestepping the question of what happens when models are \\emph{trained} to produce solver inputs.\n\nWithin the RL paradigm, DeepSeekMath \\cite{deepseekmath} introduces GRPO for mathematical reasoning, and DeepSeek-R1 \\cite{deepseek-r1} demonstrates that GRPO alone can elicit chain-of-thought reasoning without supervised fine-tuning.\nLogic-RL \\cite{logic-rl} applies rule-based RL to synthetic logic puzzles, while Thought-Like-Pro \\cite{thought-like-pro} uses Prolog-verified trajectories as imitation learning targets.\nMost directly comparable, \\citet{mellgren-prolog-grpo} trains a 3B model via GRPO to generate Prolog, using hand-crafted structure penalties to encourage well-formed outputs.\n\nThese efforts share a common gap: none systematically diagnose the structural quality of learned formalizations beyond execution success.\nMellgren et al.'s structure penalties are task-specific and manually designed; prompting-based methods do not face reward hacking but also cannot scale formalization quality through training.\nBy contrast, we derive ISR from solver trace ablation as a general, solver-grounded diagnostic that quantifies component necessity without task-specific engineering, and use it to reveal structural degeneration invisible to execution rewards.\n\n\\subsection{Reward Shaping and Process Supervision}\n\nProcess supervision provides step-level training signal to complement outcome-based rewards.\n\\citet{lightman-verify-step} show that process reward models outperform outcome supervision for mathematical reasoning, establishing process-level feedback as a principled alternative to binary correctness signals.\nMath-Shepherd \\cite{math-shepherd} extends this to automated process supervision without human annotation, using completion-based estimation to label intermediate steps.\nIn the formal verification domain, RLSF \\cite{rlsf} extracts fine-grained token-level rewards from solver certificates, demonstrating that symbolic feedback can outperform scalar rewards for structured generation tasks.\nMore recently, Rubric-GRPO \\cite{rubric-grpo} uses structured multi-dimensional rubrics as GRPO reward, moving beyond scalar signals toward compositional reward design.\n\nA parallel line of work studies how auxiliary reward signals interact with primary objectives.\n\\citet{gao-effective-rl-reward} find that learned process and outcome reward models can \\emph{hurt} RL training relative to simple success-only reward, a finding that directly parallels our observation that ISR as auxiliary reward degrades prove rate.\nDeepSeek-Prover-V1.5 \\cite{deepseek-prover-v15} avoids this problem entirely by using binary Lean verification as GRPO reward, sidestepping graded proxy metrics.\n\nISR shares the motivation of process supervision---providing structural signal beyond binary outcomes---but differs in grounding: ISR is computed deterministically from solver behavior via leave-one-out ablation, not estimated from model rollouts or learned reward models.\nOur central finding is that this grounded process signal can itself become a target of optimization, exhibiting the same Goodhart dynamics it was designed to diagnose.\n\n\\subsection{Reward Hacking and Goodhart's Law}\n\nReward hacking---where agents exploit reward proxies without achieving intended objectives---is well-documented in reinforcement learning.\n\\citet{gao-reward-overoptimization} establish scaling laws for reward model overoptimization, showing that proxy reward and gold reward diverge predictably as optimization pressure increases.\n\\citet{skalse-reward-hacking} prove that for stochastic policies, any non-constant proxy reward is theoretically hackable, providing formal grounding for the ubiquity of the phenomenon.\n\\citet{manheim-goodhart-taxonomy} categorize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---offering vocabulary for classifying observed failure modes.\n\nEmpirical characterizations span multiple settings.\n\\citet{karwowski-goodhart-rl} give a geometric interpretation of Goodhart's Law in MDPs, showing that optimization past a critical point necessarily decreases the true objective.\n\\citet{pan-reward-misspecification} demonstrate dose-dependent degradation across nine environments, where more capable agents exploit misspecifications more aggressively.\n\\citet{kwa-catastrophic-goodhart} prove that KL regularization---the standard mitigation in RLHF---provably fails under heavy-tailed reward misspecification.\nRecent surveys \\cite{reward-hacking-survey} and empirical studies of specification gaming in reasoning models \\cite{bondarenko-spec-gaming,kim-game-formalization} confirm that reward hacking extends to frontier LLMs.\n\\citet{spurious-rewards} show that even random rewards can match ground-truth rewards under GRPO's group normalization, questioning the information content of structured reward signals.\n\nDespite this extensive theoretical and empirical foundation, Goodhart's Law has been studied primarily in RLHF with learned reward models and in classic RL environments.\nFormal reasoning with solver-grounded rewards---where the reward is computed by a deterministic verifier rather than a learned model---remains unexplored territory.\nOur work provides the first empirical characterization of Goodhart's Law in this setting, documenting both classical dose-dependent collapse ($\\beta{=}0.3$: prove rate drops from 48\\% to 18\\%) and a meta-level effect where the diagnostic proxy itself becomes a gaming target ($\\beta{=}0.1$: ISR-specific conclusion duplication in 2/3 seeds, with apparent structural gains attributable to premise minimization artifacts).\n\n\\subsection{Mutation Testing and Component Analysis}\n\nSolver Trace Ablation adapts ideas from mutation testing in software engineering.\n\\citet{demillo1978} introduce mutation testing---systematically perturbing program elements to assess test suite adequacy---and propose the coupling effect hypothesis: tests detecting simple mutations also detect complex ones.\n\\citet{jia-harman-survey} survey three decades of development in this paradigm, covering mutation operator design, cost reduction, and the equivalent mutant problem.\n\\citet{just-mutants-real-faults} validate that mutation-based adequacy correlates with real fault detection, supporting the premise that systematic perturbation provides meaningful quality signal.\n\nSTA applies a specific form of mutation testing---leave-one-out component ablation---to logical formulas rather than source code.\nEach clause in a formalization is removed in turn, and the solver is re-executed to determine whether the clause was necessary for the proof.\nThis is equivalent to first-order mutation with a deletion operator, directly inheriting the theoretical justification from the coupling effect \\cite{demillo1978,offutt-coupling}.\nISR is thus not a novel metric \\emph{per se}, but a known technique applied to a new domain; our contribution lies in using it to diagnose reward hacking in GRPO-trained formalizers and in characterizing its failure modes when repurposed as a training signal.\nWe also note connections to feature attribution methods in machine learning \\cite{jia-harman-survey}, where leave-one-out evaluation is standard for assessing feature importance, though our ablation targets solver inputs rather than model features.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T19:49:25.234937+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T19:49:25.235070+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex 2>/dev/null && echo \"EXISTS\" || echo \"NEW_FILE\"",
  "description": "Check if related_work.tex already exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex 2>/dev/null && echo \"EXISTS\" || echo \"NEW_FILE\"",
    "description": "Check if related_work.tex already exists"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T19:49:25.235190+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T19:49:25.235300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T19:49:25.235455+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers to offload logical inference.
6	Logic-LM~\cite{logic-lm} generates FOL formalizations verified by an external prover, with a self-refinement loop on solver errors; LINC~\cite{linc} similarly translates natural language to first-order logic for Prover9, demonstrating gains over chain-of-thought on syllogistic and multi-hop tasks.
7	SatLM~\cite{satlm} extends the paradigm to satisfiability solvers via declarative prompting, while LoRP~\cite{lorp} and FoVer~\cite{fover-pei2025} route through Prolog execution traces and FOL verification, respectively, to validate or filter LLM-generated reasoning.
8	All of these systems evaluate on execution accuracy---whether the solver returns the correct answer---without diagnosing the structural quality of the generated formalizations.
9	RL-based training represents a more recent direction.
10	Mellgren~\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.
11	These RL systems optimize execution reward exclusively, reporting prove rate as the primary success metric.
12	Our work differs in diagnostic focus: STA reveals that execution accuracy conflates faithful derivation with degenerate shortcuts, and ISR quantifies this conflation.
13	The finding that 87\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\S\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.
14	
15	\paragraph{Reward Shaping and Process Supervision.}
16	Binary outcome rewards 
…[truncated 6336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T19:49:25.235648+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
  "old_string": "RL-based training represents a more recent direction.\nMellgren~\\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.",
  "new_string": "RL-based training represents a more recent direction, enabled by GRPO~\\cite{deepseekmath}, which eliminates the critic model by estimating baselines from group scores.\nMellgren~\\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
    "old_string": "RL-based training represents a more recent direction.\nMellgren~\\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.",
    "new_string": "RL-based training represents a more recent direction, enabled by GRPO~\\cite{deepseekmath}, which eliminates the critic model by estimating baselines from group scores.\nMellgren~\\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T19:49:25.235834+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T19:49:25.235959+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
  "old_string": "In the LLM setting specifically, Bondarenko et al.~\\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains.",
  "new_string": "In the LLM setting specifically, recent surveys~\\cite{reward-hacking-survey} document reward hacking across the full spectrum from specification gaming to emergent misalignment.\nBondarenko et al.~\\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
    "old_string": "In the LLM setting specifically, Bondarenko et al.~\\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains.",
    "new_string": "In the LLM setting specifically, recent surveys~\\cite{reward-hacking-survey} document reward hacking across the full spectrum from specification gaming to emergent misalignment.\nBondarenko et al.~\\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T19:49:25.236125+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T19:49:25.236245+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
  "old_string": "\n\\paragraph{Positioning.}\nThis work sits at the intersection of neurosymbolic reasoning, reward design, and Goodhart dynamics.\nWhere prior neurosymbolic systems evaluate on execution accuracy alone, STA provides a structural diagnostic; where prior reward-shaping work assumes that finer-grained signals safely improve training, our ISR-as-reward experiments demonstrate meta-level Goodhart failure; and where prior Goodhart analyses study learned reward models, we show the same dynamics arise from a deterministic, solver-grounded metric.\nThe mutation-testing connection provides the methodological foundation, but the contributions are empirical: structural collapse under RL, meta-level gaming of the diagnostic itself, and a taxonomy of exploitation strategies across formal languages.\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
    "old_string": "\n\\paragraph{Positioning.}\nThis work sits at the intersection of neurosymbolic reasoning, reward design, and Goodhart dynamics.\nWhere prior neurosymbolic systems evaluate on execution accuracy alone, STA provides a structural diagnostic; where prior reward-shaping work assumes that finer-grained signals safely improve training, our ISR-as-reward experiments demonstrate meta-level Goodhart failure; and where prior Goodhart analyses study learned reward models, we show the same dynamics arise from a deterministic, solver-grounded metric.\nThe mutation-testing connection provides the methodological foundation, but the contributions are empirical: structural collapse under RL, meta-level gaming of the diagnostic itself, and a taxonomy of exploitation strategies across formal languages.\n",
    "new_string": "\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T19:49:25.236396+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T19:49:25.236520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T19:49:25.236671+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic Reasoning with LLMs.}
5	Prompting-based pipelines couple LLMs with external solvers to offload logical inference.
6	Logic-LM~\cite{logic-lm} generates FOL formalizations verified by an external prover, with a self-refinement loop on solver errors; LINC~\cite{linc} similarly translates natural language to first-order logic for Prover9, demonstrating gains over chain-of-thought on syllogistic and multi-hop tasks.
7	SatLM~\cite{satlm} extends the paradigm to satisfiability solvers via declarative prompting, while LoRP~\cite{lorp} and FoVer~\cite{fover-pei2025} route through Prolog execution traces and FOL verification, respectively, to validate or filter LLM-generated reasoning.
8	All of these systems evaluate on execution accuracy---whether the solver returns the correct answer---without diagnosing the structural quality of the generated formalizations.
9	RL-based training represents a more recent direction, enabled by GRPO~\cite{deepseekmath}, which eliminates the critic model by estimating baselines from group scores.
10	Mellgren~\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.
11	These RL systems optimize execution reward exclusively, reporting prove rate as the primary success metric.
12	Our work differs in diagnostic focus: STA reveals that execution accuracy conflates faithful derivation with degenerate shortcuts, and ISR quantifies this conflation.
13	The finding that 87\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\S\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate ge
…[truncated 5796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T19:49:25.236838+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex | sed 's/\\\\\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\\\\\[a-zA-Z]*//g; s/[{}~]//g; s/--/-/g' | wc -w",
  "description": "Count approximate word count of related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex | sed 's/\\\\\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\\\\\[a-zA-Z]*//g; s/[{}~]//g; s/--/-/g' | wc -w",
    "description": "Count approximate word count of related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T19:49:25.236955+00:00_

900

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T19:49:25.237064+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\\\\\cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}//' | sort -u",
  "description": "List unique citation keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\\\\\cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}//' | sort -u",
    "description": "List unique citation keys"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T19:49:25.237170+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T19:49:25.237307+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP 'cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex | sed 's/cite{//;s/}//' | tr ',' '\\n' | sed 's/^ *//' | sort -u",
  "description": "List unique citation keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP 'cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex | sed 's/cite{//;s/}//' | tr ',' '\\n' | sed 's/^ *//' | sort -u",
    "description": "List unique citation keys"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T19:49:25.237431+00:00_

bondarenko-spec-gaming
deepseekmath
demillo1978
fover-pei2025
gao-effective-rl-reward
gao-reward-overoptimization
jia-harman-survey
just-mutants-real-faults
karwowski-goodhart-rl
kim-game-formalization
kwa-catastrophic-goodhart
lightman-verify-step
linc
llmorpheus
logic-lm
logic-rl
lorp
manheim-goodhart-taxonomy
math-shepherd
mellgren-prolog-grpo
offutt-coupling
pan-reward-misspecification
prof-process-outcome
progrs-outcome-conditioned
qwen-prm-lessons
reward-hacking-survey
rlsf
rubric-grpo
satlm
skalse-reward-hacking
spurious-rewards
thought-like-pro

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T19:49:25.237556+00:00_

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
  "session": "worker_writing_related-work_20260514T194629",
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

_source line 32 · 2026-05-14T19:49:25.237667+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T19:49:25.237801+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "related_work_tex",
  "type": "paper",
  "description": "Related Work section (Section 2) for EMNLP 2026 submission, 4 clusters, ~900 words, 32 citations",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
  "tags": "['paper', 'related-work', 'section2']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "related_work_tex",
    "type": "paper",
    "description": "Related Work section (Section 2) for EMNLP 2026 submission, 4 clusters, ~900 words, 32 citations",
    "project": "solver-trace-ablation",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex",
    "tags": "['paper', 'related-work', 'section2']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T19:49:25.237934+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_b05493\", \"name\": \"related_work_tex\", \"type\": \"paper\", \"description\": \"Related Work section (Section 2) for EMNLP 2026 submission, 4 clusters, ~900 words, 32 citations\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/related_work_b05493.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T19:49:15.867395+00:00\", \"tags\": [\"paper\", \"related-work\", \"section2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work_20260514T194629",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T19:49:25.238092+00:00_

```json
{
  "section": "Related Work (Section 2)",
  "word_count": 900,
  "citations_needed": 32,
  "figures_needed": 0,
  "tables_needed": 0,
  "notes": [
    "4 clusters: Neurosymbolic Reasoning, Reward Shaping & Process Supervision, Reward Hacking & Goodhart, Mutation Testing & Component Analysis",
    "All must-cites covered: deepseekmath, mellgren-prolog-grpo, logic-lm, linc, satlm, lightman-verify-step, gao-effective-rl-reward, rlsf, gao-reward-overoptimization, skalse-reward-hacking, reward-hacking-survey, spurious-rewards, manheim-goodhart-taxonomy, karwowski-goodhart-rl, kwa-catastrophic-goodhart, pan-reward-misspecification, demillo1978, jia-harman-survey",
    "Two gaps established: (1) no structural diagnostic in neurosymbolic work, (2) Goodhart empirics missing in formal reasoning with solver-grounded rewards",
    "Explicitly acknowledges ISR = LOO ablation from mutation testing, not novel technique",
    "Meta-Goodhart framing positioned against existing Goodhart taxonomy (Manheim & Garrabrant)",
    "Updated from prior version: added deepseekmath, reward-hacking-survey; removed redundant Positioning paragraph"
  ]
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_related-work_20260514T194629"
}
```

</details>

---
