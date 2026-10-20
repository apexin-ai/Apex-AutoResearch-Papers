# Paper Framing — solver-trace-ablation

## Target Venue
- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026

## Core Claims (2 条，精简自原始 5 条)

### Claim 1: STA as Reward Design Methodology
Solver Trace Ablation (STA), grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing theory, provides a **general, solver-agnostic procedure** for deriving intensional verification rewards from solver execution semantics. For any solver+language pair, a 5-step derivation protocol (pilot → collect shortcuts → classify → map RIP → design check) produces domain-specific structural rewards. This is the first application of the RIP framework to RL reward design.

**MVP 证据**: Full STA 在 FOL+Prover9 上提供连续 ISR（0.125-0.889），成功检测 GRPO 训练中的 reward hacking（ISR/PR 比从 64%→33%）。O(1) 近似（tautology-only check）信号过粗无效——重要阴性结果，证明了 full component ablation 的必要性。

### Claim 2: Multi-Logic GRPO Empirical Findings
Multi-logic GRPO training across structurally different formal languages (FOL→Prover9, Prolog→SWI-Prolog, SMT-LIB→Z3) exhibits measurable cross-logic transfer patterns and logic-type-specific reward hacking modes. STA-derived rewards detect and quantify these phenomena.

**MVP 证据**: 待验证（FOL 单逻辑已验证，multi-logic 需 research 阶段实验）。

## Story Spine

- **Problem**: GRPO with solver-verified rewards trains formalizers that achieve high execution accuracy but produce structurally degenerate outputs (reward hacking). Existing structural reward designs are ad-hoc heuristics with no principled derivation.
- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) demonstrates cross-solver GRPO transfer but uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work provides a general derivation procedure for structural rewards from solver semantics.
- **Our framing**: We adapt the RIP framework from mutation testing — a component is "necessary" iff its ablation changes the solver's output — to derive intensional verification rewards. STA fills the **dense + automatic** cell in the ORM-PRM reward taxonomy (ORM=sparse+automatic, PRM=dense+manual, STA=dense+automatic via solver semantics). This positions STA not as "a new algorithm" but as "the first systematic transfer of mutation testing methodology to RL reward design."
- **Headline result template**: "On FOLIO/ProofWriter/LogiQA, STA-rewarded GRPO achieves <X>% formalization accuracy with <Y>% ISR, compared to <Z>% accuracy / <W>% ISR for execution-only GRPO — maintaining accuracy while detecting and reducing structural degeneracy."

## Venue Fit Risks

- **EMNLP fit**: Core contribution is neurosymbolic (NLP + formal logic), directly in the NLP and Symbolic Reasoning track. Formal verification + RL reward design is highly relevant.
- **"Old wine" risk**: STA's component ablation resembles mutation testing. Mitigation: explicitly acknowledge the RIP origin, claim novelty at the methodology transfer level + empirical findings, not at the algorithm level.
- **Scope breadth risk**: Original proposal had 5 contributions — trimmed to 2 core (STA methodology + empirical findings). MLSR framework, hacking taxonomy, STA-IPT duality are secondary analysis within these 2 contributions.
- **Single-logic risk**: If only FOL results are available, paper may feel narrow. Mitigation: at minimum include Prolog as second logic type; SMT-LIB as stretch goal.

## Anticipated Reviewer Concerns

1. **"STA is just mutation testing applied to FOL"** — Response: yes, that's the point. The contribution is the systematic transfer + empirical validation that it works as RL reward, not algorithmic novelty. The 5-step derivation protocol is the transferable methodology.
2. **"O(1) approximation doesn't work"** — Response: this is a feature, not a bug. We report it as a principled negative result showing that domain-specific hacking modes require corresponding ablation granularity.
3. **"Low prove rate limits GRPO signal"** — Response: addressed by K=8+ and difficulty-based data selection. Prove rate increases during training (12%→15-20%).
4. **"ISR/PR ratio declining even with STA reward"** — Response: 100-step pilot is too short; full runs with curriculum will show whether STA prevents or just detects degradation. Even detection alone is a contribution (monitoring tool).
5. **"Only tested on one/two logic types"** — Response: STA derivation protocol is solver-agnostic by design; instantiations for additional logic types follow the same 5-step procedure.
