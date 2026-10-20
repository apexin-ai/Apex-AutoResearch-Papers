# Paper Framing — exec-sim-repair-verifier

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25, 2026)
- Fallback: EMNLP 2026 Findings
- Extended fallback: ICSE 2027 (Jun 23 abstract, Jun 30 paper)
- Deadline: ARR May 25, 2026 (9 days remaining)

## D116 Framing Pivot (2026-05-16)

**前 framing**: "CLS scales where generation fails" (CLS advocacy)
**新 framing**: "The Formulation Design Space for Neural Code Verification" (empirical characterization)

核心转变：不再主张任何 formulation 普遍更好，而是 characterize 何时用什么。
最强贡献重新定位：
1. CWM 失败模式是 **tokenizer/model-specific** 而非 formulation-inherent（Qwen 93% unparseable vs DeepSeek 11.8%）
2. Error complementarity: CLS/CWM 有系统性互补错误模式，oracle ensemble +2-3pp
3. 复杂度是 formulation 选择的关键维度（func-level 等价，repo-level 分化）

## Core Claims (revised per D116)

1. **Formulation Equivalence at Low Complexity**: At function-level, CLS, CWM, and TRAJ achieve statistically equivalent accuracy across two model families (Qwen3: 88.4/87.2/86.3%; DeepSeek: 86.9/86.8/84.2%). Formulation choice does not matter when execution outputs are short and structured.

2. **Complexity-Dependent Divergence (Model-Contingent)**: At repo-level, formulation effectiveness depends on model/tokenizer properties:
   - Qwen3: CLS dominates CWM by 19-26pp due to 54-93% unparseable rate (tokenizer-specific CWM collapse)
   - DeepSeek: ⏳ **PENDING** — results determine narrative direction:
     - If CLS > CWM: "complexity-dependent advantage is consistent across model families"
     - If CWM ≥ CLS: "advantage is model/tokenizer-contingent; CWM works when tokenizer supports structured generation"
   - Either outcome supports the design space characterization framing

3. **Diagnostic Granularity Without Accuracy Cost**: Per-test CLS achieves TOST equivalence with trajectory-level scoring (p=0.007, ±2pp margin, Qwen3) while providing per-test failure localization. Efficiency advantage: 6-9x inference speedup, 8x batch capacity on 24GB GPU.

## Story Spine (D116 revision)

**Problem**: Execution-free verification for code repair can be formulated in multiple ways (per-test classification, execution output generation, trajectory-level scoring), but no systematic comparison exists. Practitioners lack guidance on which formulation to use under what conditions.

**Existing approaches & gaps**: Code World Models generate execution outputs but suffer from format compliance failures at scale. Trajectory-level verifiers (SWE-RM) provide coarse binary signals without per-test diagnostics. Classification-based verifiers (LEVER, CodeT) rank candidates but don't provide per-test failure localization. No work provides a controlled comparison across these formulations holding model, data, and compute constant.

**Our contribution**: We present the first controlled comparison of three verification formulations (CLS, CWM, TRAJ) across 2 model families, 2 complexity levels, and multiple seeds. Key findings:
1. Formulations are equivalent at function-level (null result establishing baseline)
2. Formulations diverge at repo-level in a model-contingent manner
3. CWM failure at repo-level is tokenizer-specific (not formulation-inherent): unparseable rate drops from 93% (Qwen) to [X]% (DeepSeek)
4. CLS and CWM exhibit complementary error patterns (oracle ensemble: 90.63%)
5. Per-test CLS matches trajectory-level accuracy while providing diagnostic granularity at 6-9x lower inference cost

**Headline result template (dual-path)**:
- Path A (CLS > CWM on DeepSeek): "Classification consistently outperforms generation at repo-level across model families, but the magnitude depends on tokenizer-specific format compliance. We characterize when and why each formulation succeeds."
- Path B (CWM ≥ CLS on DeepSeek): "No single formulation dominates: CLS wins on Qwen (tokenizer-induced CWM collapse) while CWM matches/exceeds CLS on DeepSeek. The formulation design space is model-contingent, and we provide the empirical characterization needed to navigate it."

## Venue Fit Risks

1. **Novelty concern (Dream consensus)**: "Classification > generation when outputs are complex" is predictable. Mitigation: novelty is in (a) empirical demonstration that it's tokenizer-specific not formulation-inherent, (b) error complementarity analysis, (c) systematic controlled comparison methodology. Frame as "empirical characterization with actionable insights" not "method contribution."

2. **EMNLP vs SE venue**: Mitigation: (a) process vs outcome supervision parallel (Lightman et al., 2023; Uesato et al., 2022), (b) general NLP methodology insight about classification vs generation.

3. **CWM comparison fairness**: Original CWM is 32B with mid-training on execution traces; we compare 4-8B LoRA. Mitigation: explicitly scope as "same-size LoRA comparison" and discuss that generation may need more capacity. This limitation actually strengthens the practical guidance: "at practical deployment sizes (4-8B), classification is the safer choice."

4. **Re-repair null result**: Downstream utility unvalidated. Mitigation: frame efficiency + diagnostic granularity as the practical benefit, not re-repair. Re-repair is future work.

## Anticipated Reviewer Concerns & Mitigations (updated per Dream)

| Concern | Mitigation |
|---------|------------|
| "Limited novelty — obvious that classification is easier" | Func-level null result proves it's NOT trivially easier; advantage is complexity+tokenizer-dependent. Strongest novelty: CWM failure is tokenizer-specific |
| "CWM comparison unfair (4-8B LoRA vs 32B full)" | Explicitly scope as same-size comparison; discuss scale as limitation; practical guidance framing |
| "Single-seed repo-level" | Multi-seed replication (2 seeds × 2 formulations × DeepSeek, running) |
| "Cross-model validation incomplete" | DeepSeek repo experiments (running); whichever direction supports the design space characterization |
| "No downstream utility" | Efficiency benefit (6-9x) is practical; re-repair honestly framed as future work |
| "Claims outrun evidence" | D116: remove all advocacy language; report what evidence supports, nothing more |
| "Process vs outcome supervision parallel" | Add Lightman et al. 2023, Uesato et al. 2022 to Related Work |

## Related Work Additions Needed (Dream feedback)
- Process vs outcome supervision: Lightman et al. 2023, Uesato et al. 2022 (CLS vs TRAJ parallel)
- CodeRL, AlphaCode, Reflexion (verification-in-the-loop repair)
- Predictive mutation testing literature (per-test binary classification precedent)
