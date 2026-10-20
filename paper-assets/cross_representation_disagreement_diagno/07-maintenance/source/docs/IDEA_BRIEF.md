# Idea Brief: Cross-Representation Disagreement as Diagnostic: Empirical Evidence for Formalization Error Localization and Targeted Repair in Neurosymbolic Reasoning


- **Idea ID**: `idea_009`
- **Created**: 2026-05-14
- **Approved**: 2026-05-14
- **Source**: foreign:be-idea-gen-0509-3
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026; conference in Budapest, Hungary) — PRIMARY target, 15-day sprint for scoped empirical study, AAAI 2027 (abstract deadline July 25, submission August 1, 2026; conference Feb 16-23, 2027 in Montreal) — SECONDARY target for the FULL framework paper with learned taxonomy, expanded analysis, and additional model coverage if EMNLP scope proves too narrow

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Symbolic Reasoning.

Direction: Neurosymbolic reasoning — combining neural models with symbolic systems (logic programs, knowledge graphs, formal verification, constraint solvers). NOT limited to LLM-only reasoning — explicitly seek methods that integrate external symbolic components. Also in-scope: structured mathematical reasoning, program-aided reasoning, theorem prover integration.

Contribution type: METHOD ONLY. Must propose a new hybrid algorithm, training objective, or inference pipeline that combines neural + symbolic components. Pure prompting tricks (vanilla CoT, self-consistency) are out of scope.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Neurosymbolic methods are often inference-heavy not training-heavy — budget accordingly.
2. Time: ≤16 days. Use existing open checkpoints (Qwen3, Llama-3.x, DeepSeek-R1 distills) + off-the-shelf solvers (Z3, Prolog, SymPy, Lean4).
3. Eval: MATH, AIME 2024/2025, GPQA Diamond, ProofWriter, FOLIO, LogiQA, ARC-Challenge, BBH.

Look for: lightweight symbolic verifiers as post-hoc filters, neural-guided symbolic search, structured output → formal checker pipelines, hybrid neuro-symbolic distillation. Avoid: pure prompt engineering, vanilla CoT.

Tag: direction=neurosymbolic_reasoning, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Core Problem

Neurosymbolic reasoning pipelines suffer from FORMALIZATION ERRORS as their dominant failure mode—the LLM's translation from natural language to a formal representation introduces subtle corruptions (lost quantifier scope, flattened relations, incorrect operator precedence). Current approaches either SELECT one representation (HybridMind, Adaptive Selection, Adaptive LLM-Symbolic Reasoning), VERIFY within one representation (VeriCoT, VERGE), perform WITHIN-REPRESENTATION roundtrip verification (Roundtrip Verification), INTERLEAVE verification during generation requiring fine-tuning (Pushing the Boundaries), FILTER inconsistent solutions without diagnosis (Prove), or FILTER CoT-PoT disagreements without diagnosing error type or attempting targeted repair (Liang et al., 2024). Recent empirical work ('Do LLMs Game Formalization?', Kim et al. 2026) confirms that different formalization pipelines exhibit qualitatively distinct failure modes—GPT-5 fabricates axioms during proving while DeepSeek-R1 mistranslates premises during formalization—yet no method exploits cross-representation disagreement patterns to CATEGORIZE the error type and guide TARGETED REPAIR of the failing component. The diagnostic signal available when the SAME problem is formalized into MULTIPLE DISTINCT representations (e.g., FOL vs. executable code) that DISAGREE remains underexploited: the disagreement pattern reveals which aspect of the formalization is corrupted and what type of repair is needed. Critically, same-model cross-representation disagreement can only catch FORMALIZATION-SPECIFIC errors (where the translation to a particular formal language fails), not specification misunderstanding errors where the model's comprehension of the problem is itself wrong—producing false agreement across both representations (Denisov-Blanch et al. 2026; Kim et al. ICML 2025). This boundary condition is itself an important empirical finding.

## Opportunity / Why Now

Six lines of evidence converge: (1) Prove (2024) shows code execution can verify NL reasoning (up to 18% gain on GSM8K), but only filters—doesn't diagnose or repair; (2) VeriCoT (2025) shows FOL formalization can verify CoT steps, but within one representation only; (3) Roundtrip Verification (April 2026, arXiv 2604.25031) demonstrates that diagnosis-guided repair of formalization errors raises equivalence from 45-61% to 83-85%, but operates entirely within a single representation on a narrow domain; (4) Kim et al. (April 2026, arXiv 2604.19459) empirically demonstrate that different models exhibit qualitatively distinct formalization error modes—internally consistent but semantically wrong outputs can evade within-representation detection entirely; (5) Cao et al. (Jan 2026, arXiv 2601.22642) show interleaved formal verification improves 7B/14B models by 10-14% but requires fine-tuning, limiting applicability; (6) Liang et al. (2024, arXiv 2410.05318) show that CoT-PoT disagreement is a useful filtering signal, achieving SOTA on GSM8K and MATH with trained verifiers—but they FILTER (discard disagreeing solutions) rather than DIAGNOSE the error type or attempt REPAIR, and their approach requires training specialized verifiers (Math-Rev, Code-Rev), whereas ours operates at inference time with no model modification. The gap: nobody uses cross-representation disagreement patterns as a diagnostic signal enabling CATEGORIZED error diagnosis and TARGETED repair at inference time without model modification. Roundtrip Verification proves diagnosis-guided repair works within one representation; Liang et al. prove CoT-PoT disagreement is informative; we extend both insights across representations with error categorization, gaining complementary error coverage since different formalisms fail on different problem aspects. However, we acknowledge upfront that correlated failures from specification misunderstanding (Denisov-Blanch et al. 2026; Kim et al. ICML 2025) will produce false agreement that our approach cannot detect—characterizing this boundary is itself a contribution. Open-weight models like Qwen3-32B (56.3% on AIME 2025, 66.8% on GPQA Diamond in thinking mode per the official Qwen3 Technical Report, arXiv 2505.09388) provide substantial headroom for improvement through better error correction.

## Landscape (SOTA & Limitations)

Logic-LM (EMNLP 2023) established NL-to-symbolic-to-solver pipelines. LINC (EMNLP 2023) showed FOL+theorem provers outperform CoT on ProofWriter by 26% (GPT-4). Adaptive Selection (arXiv 2025) routes to best formal language achieving 96% on mixed sets but commits to one formalization. Adaptive LLM-Symbolic Reasoning (EACL 2026, arXiv 2510.06774) introduces dynamic multi-paradigm solver composition achieving 27% over GPT-4o, but ROUTES to one solver rather than comparing outputs across solvers. HybridMind (NeurIPS 2025) meta-selects between NL and symbolic reasoning (4.4% over GPT-4o on FOLIO, 1.3% on MATH) but selects one path. VERGE (Jan 2026) uses MCS-based atomic claim verification within FOL achieving 18.7% uplift via error localization, but operates within a single FOL representation. VeriCoT (2025) formalizes CoT steps to FOL for verification but doesn't use disagreement diagnostically. Prove (2024) uses programs-as-verifiers for math self-consistency (18% gain on GSM8K, 8% on MATH-500) but only filters—no diagnosis or repair; code available at github.com/declare-lab/PROVE. SymCode (2025) reframes math as SymPy code generation but is code-only. Chain-of-Reasoning (2025) combines NLR/AR/SR paradigms with progressive training but uses voting not disagreement. Logitext (arXiv 2602.18095, Feb 2026) treats LLM reasoning as Satisfiability Modulo Theory, integrating LLM-evaluated natural language text constraints with SMT solving for joint textual-logical reasoning on content moderation, LegalBench, and Super-NLI—relevant as an alternative SMT integration paradigm but does not compare across representations diagnostically. MATH-VF (arXiv 2505.20869) uses a formalizer-critic architecture integrating CAS and SMT solvers for step-wise mathematical verification on MATH-500 and ProcessBench—relevant as it combines multiple formal verification tools but operates within a single verification pipeline rather than exploiting cross-representation disagreement.

**Closest prior work**: Liang et al. (2024, arXiv 2410.05318, 'Improving LLM Reasoning through Scaling Inference Computation with Collaborative Verification', withdrawn from ICLR 2025) is the most directly related work. They generate both CoT and PoT for the same math problem and use CoT-PoT answer agreement as a filtering signal, discarding solutions where the two representations disagree. They train specialized verifiers (Math-Rev, Code-Rev) using SimPO on datasets of correct/incorrect solutions, achieving 95.6% on GSM8K and 76.9% on MATH with Qwen-72B. Key differences from our work: (a) they FILTER (discard disagreeing solutions) while we DIAGNOSE (categorize the error type using the disagreement pattern) and REPAIR (feed diagnostic signal back to the LLM for targeted correction of the failing component); (b) they require training verifiers on labeled data, while our approach operates purely at inference time; (c) they operate on math only, while we evaluate across logic, math, science, and commonsense domains; (d) we characterize WHEN cross-representation disagreement is informative vs. when correlated failures produce uninformative agreement. Their results demonstrate that cross-representation disagreement IS informative—our contribution extends this from filtering to diagnosis and repair.

Pushing the Boundaries (arXiv 2601.22642, Jan 2026) dynamically interleaves formal logic verification during generation, achieving 10-14% improvements on 6 benchmarks with 7B/14B models—but requires fine-tuning, making it complementary to (not competing with) our inference-time approach. Do LLMs Game Formalization? (arXiv 2604.19459, April 2026, VerifAI-2 Workshop at ICLR 2026) evaluates faithfulness of FOL formalization on 303 problems, finding GPT-5 and DeepSeek-R1 exhibit qualitatively different unfaithfulness patterns—GPT-5 fabricates axioms while DeepSeek-R1 mistranslates premises. This directly supports our premise that cross-representation comparison can catch errors invisible to within-representation checks. Roundtrip Verification (arXiv 2604.25031, April 2026) diagnoses formalization errors via NL-to-formal-to-NL-to-formal roundtrip, raising equivalence from 45-61% to 83-85% on 150 traffic rules. Key difference: theirs is WITHIN-representation on a narrow domain; ours is CROSS-representation on general reasoning tasks. ARc (arXiv 2511.09008) uses redundant formalizations for compliance verification (99% soundness) but targets soundness guarantee, not error diagnosis. FregeLogic (SemEval 2026) uses LLM disagreement for Z3 tiebreaking but only as routing. Cross-Model Disagreement (arXiv Mar 2026) establishes disagreement as correctness proxy between neural models but not across symbolic representations. Co-Sight (arXiv 2510.21557) uses conflict-aware meta-verification between LLM agents but operates on cross-model, not cross-representation disagreement.

**Correlated failure literature**: Consensus is Not Verification (arXiv 2603.06612, Denisov-Blanch et al. 2026) demonstrates that LLM errors are strongly correlated and consensus aggregation fails to improve truthfulness—even reinforcing shared misconceptions. Correlated Errors in LLMs (ICML 2025, arXiv 2506.07962, Kim et al.) shows 60% error agreement across different models, with larger and more accurate models exhibiting MORE correlated errors. These findings directly inform our approach: same-model cross-representation disagreement will miss specification misunderstanding errors that propagate identically to both representations. Our complementarity analysis quantifies exactly when and how often this occurs, and our cross-model ablation tests whether model diversity recovers diagnostic coverage for this error class.

The critical gap remains: no method treats cross-representation disagreement as a diagnostic signal for formalization error CATEGORIZATION and TARGETED REPAIR. Liang et al. proved disagreement is informative for filtering; we extend this to diagnosis and repair.

## Proposed Approach

This is scoped as an EMNLP 2026 submission (ARR May 25 deadline) presenting empirical evidence that cross-representation disagreement enables formalization error localization and targeted repair. The method is deliberately simple and inference-time-only, requiring no fine-tuning.

**Dual Formalization Pipeline**: For each NL reasoning problem, generate TWO complementary formalizations simultaneously, domain-adapted: (A) Logic reasoning (FOLIO, ProofWriter, LogiQA): formalize as both FOL (verified via Z3) AND executable Python constraint code; (B) Mathematical reasoning (MATH Level 5, AIME 2024, AIME 2025): formalize as both NL chain-of-thought AND executable SymPy/Python code; (C) Science/knowledge (GPQA Diamond): formalize as CoT + Python verification code where applicable; (D) Commonsense/mixed reasoning (ARC-Challenge, BBH): formalize as CoT + Python code, with explicit analysis of when dual formalization provides limited additional signal.

**Model Selection**: Qwen3-32B (thinking mode, Apache 2.0) as the PRIMARY model—baseline accuracy of ~70% on AIME 2024 and 56.3% on AIME 2025 (pass@1, official Qwen3 Technical Report arXiv 2505.09388, Table 13), ~66.8% on GPQA Diamond, and estimated 75-85% on FOLIO/ProofWriter provides genuine headroom, especially on the harder AIME 2025 benchmark where nearly half of problems are answered incorrectly. Qwen3-8B as a lower-capability ablation. Both via API (Qwen Cloud at ~$0.08/M input tokens). **Cross-model ablation**: DeepSeek V4 Pro generating one representation while Qwen3-32B generates the other, to test whether model diversity improves diagnostic coverage by reducing correlated failures from shared model biases (promotional pricing $0.435/M input through May 31, 2026). This ablation directly addresses the concern from the correlated failure literature that same-model biases propagate to both representations.

**Disagreement Detection and Categorization**: When representations disagree (code execution produces answer A but Z3/theorem prover yields B, or SymPy result differs from CoT derivation), categorize the disagreement using a RULE-BASED TAXONOMY (not learned—practical for the timeline): (1) Logic domain: quantifier scope mismatch, negation handling error, relational arity error, missing/extra constraint, predicate grounding error; (2) Math domain: operator precedence error, type confusion (integer vs. real), boundary condition miss, symbolic simplification divergence, variable scope error. Categorization uses pattern matching on the disagreement evidence (e.g., Z3 returns unsat while code returns True likely indicates missing constraint or negation error).

**Targeted Repair**: Feed the diagnosed error type plus evidence from the AGREEING representation back to the LLM for targeted repair of only the failing component. Compare against blind regeneration (same compute budget, no diagnostic signal). Max 2 repair rounds for efficiency.

**Correlated Failure Analysis**: We explicitly acknowledge and empirically characterize the limitation that same-model formalization errors are partially correlated (Denisov-Blanch et al. 2026; Kim et al. ICML 2025). When the model misunderstands the problem SPECIFICATION (not the formalization), both representations will be wrong in the same way, producing FALSE AGREEMENT rather than diagnostic disagreement. Our approach catches FORMALIZATION-SPECIFIC errors (quantifier scope in FOL, loop bounds in Python, operator precedence in SymPy) but not specification-level errors. We quantify: (a) what fraction of errors produce disagreement (formalization-specific, catchable); (b) what fraction produce false agreement (specification-level, uncatchable by our method); (c) whether the cross-model ablation (Qwen3-32B + DeepSeek V4 Pro) reduces false agreement by introducing model diversity. This analysis is itself a contribution—characterizing the boundary between formalization errors and specification errors in neurosymbolic pipelines.

**Evaluation**: 9 benchmarks covering 4 reasoning domains: FOLIO, ProofWriter, LogiQA (logic), MATH Level 5 (hard subset—replacing MATH-500 which is near-saturated at ~95-97% for Qwen3-32B in thinking mode), AIME 2024, AIME 2025 (math), GPQA Diamond (science/knowledge), ARC-Challenge, BBH (commonsense/mixed). For AIME 2025 (56.3% baseline), the headroom story is strongest. For ARC-Challenge and BBH, we explicitly analyze when and why cross-representation disagreement provides limited diagnostic value—this negative/diagnostic result is itself a contribution, characterizing the boundary conditions of the approach.

**Baselines** (4 focused): (a) Self-consistency / majority voting (standard); (b) Prove (filtering via program verification, open-source code available); (c) Single-representation verification + blind regeneration (to isolate the value of cross-representation diagnosis vs. simply having two attempts); (d) CoT-PoT filtering a la Liang et al. (2024)—reimplemented without trained verifiers, using only answer-match filtering, to isolate our contribution of diagnosis+repair vs. simple filtering.

**Key Analyses**: (1) Disagreement rate by benchmark and problem difficulty; (2) What fraction of disagreements are diagnostically informative (i.e., one representation is correct); (3) Error type distribution across benchmarks; (4) Targeted repair success rate vs. blind regeneration; (5) Complementarity analysis: when representations fail independently vs. exhibit correlated failures, including false agreement rate where both representations are wrong but agree; (6) Compute-normalized comparison (does the diagnostic signal justify the cost of dual formalization?); (7) Cross-model ablation: does using different models for each representation reduce correlated failures and improve diagnostic coverage?

**For baselines without open-source code** (if we include HybridMind or VERGE in extended comparison), we implement core methodology from paper descriptions and note this limitation transparently.

## Resource Estimate

- **auto_research**: {'api_cost': '$200-400 (more exploration of prompt variants for formalization quality, cross-model ablation)', 'claude_api_cost': '$150-300 (estimated 1500-3000 agent turns for end-to-end pipeline, experiments, paper drafting)', 'estimated_total_cost': '$350-700', 'gpu_hours': '~0h', 'gpu_utilization': 'None.', 'risk_note': 'Agent can build pipeline and run experiments autonomously, but error taxonomy quality and paper framing need human review before submission.', 'speed_bottleneck': 'API rate limits. Can parallelize across Qwen Cloud and DeepSeek API.', 'team': '0 (initial 1h setup + daily 30min review of results)', 'timeline': '8-12 days with API access'}
- **human_in_loop**: {'api_cost': '$150-250', 'claude_api_cost': '$80-150 (estimated ~800-1500 agent turns for pipeline implementation, prompt engineering, result analysis)', 'estimated_total_cost': '$230-400', 'gpu_hours': '~0h', 'gpu_utilization': 'None.', 'risk_note': 'Tight timeline. Primary risk is pipeline debugging time. Mitigated by using open-source Prove code as a starting point and keeping the method simple. Cross-model ablation adds experimental complexity but uses the same pipeline infrastructure.', 'team': '1 researcher full-time, reviewing pipeline outputs and error categorizations daily', 'timeline': '12-15 days'}
- **manual**: {'api_cost': '$120-200 (Qwen3-32B at ~$0.08/M input via Qwen Cloud: 9 benchmarks x ~500-1500 problems x 2 formalizations x ~2000 tokens = ~35M tokens input + ~18M output per run, with 2 repair rounds = ~$60-90 for Qwen3-32B; Qwen3-8B: ~$15-25; DeepSeek V4 Pro cross-model ablation at promotional $0.435/M input: ~$30-50; Liang et al. baseline reimplementation: ~$10-15)', 'estimated_total_cost': '$120-200 (API only)', 'gpu_hours': '~0h (all inference via API; Z3 and Python execution are CPU-only)', 'gpu_utilization': 'None. Fully API-based.', 'team': '1-2 researchers working full-time', 'timeline': '15 days (May 10-25, 2026) for EMNLP ARR submission'}

## Key References

- Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning (Findings of EMNLP 2023)
- LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers (EMNLP 2023)
- HybridMind: Meta Selection of Natural Language and Symbolic Language for Enhanced LLM Reasoning (NeurIPS 2025)
- Adaptive Selection of Symbolic Languages for Improving LLM Logical Reasoning (arXiv 2025)
- Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)
- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv Jan 2026)
- VERUS-LM: A Versatile Framework for Combining LLMs with Symbolic Reasoning (arXiv Jan 2026, 2501.14540)
- Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning (arXiv 2024)
- Improving LLM Reasoning through Scaling Inference Computation with Collaborative Verification (Liang et al., arXiv 2410.05318, 2024, withdrawn from ICLR 2025)
- VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (2025)
- SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation (arXiv 2025)
- Chain-of-Reasoning: Towards Unified Mathematical Reasoning in Large Language Models via a Multi-Paradigm Perspective (arXiv Jan 2025)
- Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031, April 2026)
- A Neurosymbolic Approach to Natural Language Formalization and Verification (arXiv 2511.09008, Nov 2025)
- Cross-Model Disagreement as a Label-Free Correctness Signal (arXiv Mar 2026)
- Intermediate Languages Matter: Formal Choice Drives Neurosymbolic LLM Reasoning (arXiv 2025)
- FregeLogic at SemEval 2026 Task 11: Hybrid Neuro-Symbolic Architecture for Syllogistic Validity (SemEval 2026)
- FoVer: First-Order Logic Verification for Natural Language Reasoning (TACL 2025)
- LogiConBench: Benchmarking Logical Consistencies of LLMs (ICLR 2026)
- Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification (arXiv 2601.22642, Jan 2026)
- Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, April 2026, VerifAI-2 Workshop at ICLR 2026)
- Co-Sight: Enhancing LLM-Based Agents via Conflict-Aware Meta-Verification and Trustworthy Reasoning with Structured Facts (arXiv 2510.21557, Oct 2025)
- Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness (Denisov-Blanch et al., arXiv 2603.06612, 2026)
- Correlated Errors in Large Language Models (Kim et al., ICML 2025, arXiv 2506.07962)
- Neurosymbolic Language Reasoning as Satisfiability Modulo Theory (Logitext, arXiv 2602.18095, Feb 2026)
- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (MATH-VF, arXiv 2505.20869)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally well-structured proposal with honest limitation acknowledgment (correlated failures, commonsense domain weakness), clean differentiation from 25+ related works, domain-adapted evaluation plan, and explicit success/failure criteria. The best-written idea I've reviewed in this batch.", 'score': 5}**/5
  - feasibility: **{'rationale': "API-only approach eliminates GPU concerns entirely. Qwen Cloud ($0.08/M) and DeepSeek V4 Pro ($0.435/M promotional) are verified and affordable. Rule-based taxonomy avoids training. 15-day timeline is very aggressive for 9 benchmarks but achievable given the method's simplicity (no fine-tuning, existing eval scripts, open-source Prove baseline).", 'score': 4}**/5
  - impact: **{'rationale': 'Solid empirical contribution for EMNLP Findings but unlikely transformative. Expected improvements are modest (2-5% absolute on hard benchmarks). The negative results (when cross-representation disagreement fails) and complementarity analysis are useful but incremental. Main conference acceptance depends on strength of empirical results.', 'score': 3}**/5
  - novelty: **{'rationale': 'Confirmed via extensive search: no prior work combines cross-representation disagreement for error CATEGORIZATION + TARGETED REPAIR. Cleanly differentiated from Liang et al. (filter only), Roundtrip Verification (within-representation), and VERGE (single-representation MCS). A well-motivated novel combination rather than a radical new paradigm.', 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 25.0%
**终审自评 (Y)**: 35.0%
**出口三重共识 (Z)**: 33.0%
**Z 区间**: [28.0%, 38.0%]
**真实提升 (Z-X)**: +8.0 pp
**幻觉幅度 (Y-Z)**: +2.0 pp
**出口一致性**: 高
**出口三次评估**: [33.0, 34.0, 33.0]

### 优化方案 / 拒绝详情
【优化方案】

1. **[标题]** — 原标题未知完整形式，建议采用终稿标题 *"Cross-Representation Disagreement Diagnosis for LLM Reasoning: A Systematic Analysis and Lightweight Repair Framework"*，显式包含 "Systematic Analysis" 以锚定双轨定位 — 命中 **Significance / Contribution Type**（引导审稿人按 analysis paper 标准评判，降低对 method novelty 深度的苛求）

2. **[Motivation 段末尾 — 新增 framing sentence]** — 在动机段结尾加入一句锐利的范式对比："We argue that the gap between detection and action — the diagnostic step that determines *what* went wrong and *where* — is the missing piece in current multi-representation reasoning pipelines." 原 proposal 的 novelty 散落在各处，需要读完才能理解；这句话让审稿人在前两段即锁定 "detect-diagnose-repair" vs. "detect-then-discard/retry" 的对比 — 命中 **Novelty（第一印象效应）**

3. **[Core Thesis — 双轨定位重构]** — 原 proposal 自我定位偏向 "inference-time method"。重构为并列双贡献：(1) systematic empirical analysis of cross-representation disagreement patterns; (2) lightweight diagnostic-guided repair framework。将 disagreement pattern characterization 提升为与 repair 方法并列的第一等贡献 — 命中 **Novelty + Significance**（EMNLP 对 analysis paper 有明确接纳传统，双轨定位为 dual-outcome 提供结构性兜底）

4. **[Contributions §2 — 新增完整 Error Taxonomy]** — 原 proposal 仅提及 "rule-based heuristics" 未给出任何具体分类。新增四类错误体系（Translation Fidelity Loss / Execution Divergence / Representation Coverage Gap / Ambiguity-Induced Divergence），每类包含：操作性定义、disagreement pattern 签名、**差异化 repair 策略**（模板重翻译 / 实现 bug 修复 / 表征委托 / 盲重生成）。增加 "固定策略 vs. 按类型分派" 的消融验证 taxonomy 的规定性价值 — 命中 **Technical Soundness + Novelty**（从 "heuristics 完全未描述" 修复为 "可操作的分类体系 + 实证验证"）

5. **[Contributions §3 — 新增三层 Error Localization 机制]** — 原 proposal 的核心方法论缺口：当两种表征都成功执行但结果不一致时，如何判断哪一侧出错。新增分层决策逻辑：Layer 1（执行异常判定）→ Layer 2（稳定性投票 + 中间步骤 sanity check）→ Layer 3（ambiguous fallback 退化为盲重生成）。同时**明确 Layer 2 的局限**：稳定性≠正确性，对系统性错误（stable-but-wrong）无效，实验中按错误类型拆解定位准确率 — 命中 **Technical Soundness**（从 "核心环节缺失、任何认真 reviewer 会直接扣分" 修复为 "逻辑闭环 + 主动讨论局限"）

6. **[Contributions §3 — 新增 Repair vs. Selection 论证]** — 原 proposal 未考虑的关键问题：定位出错侧后为什么不直接选另一侧的答案（selection），而要额外做 repair？新增假设场景论证（两侧都有局部错误、正确侧格式不符、



## MVP Validation Results

- **Date**: 2026-05-15
- **Hypothesis Supported**: Yes

### Key Metrics

C1=39.6% (≥10% PASS), C2=86.8% (≥40% PASS), C3=3 types (≥2 PASS), C4=+5.2pp (>5pp PASS, margin 0.2pp), C5=85.4% (≥60% PASS). All-mode 5/5 PASS. Excl-Unknown 4/5 (C4 FAIL at +0.0pp).

### Summary

在 FOLIO 数据集 204 样本 + Qwen3-32B 上验证跨表征分歧诊断方法。核心假设得到支持：FOL(Z3) 与 Python Code 两种推理路径的分歧率 39.6%（C1），分歧中 86.8% 可诊断出具体错误类型（C2），覆盖 3 种错误类型（C3），错误定位准确率 85.4%（C5）。定向修复优于盲目重跑（C4）在 All-mode 下通过（+5.2pp）但 margin 极薄（0.2pp），Excl-Unknown 组未通过。C4 弱点需在 research 阶段通过改进 repair 机制或调整 paper framing 解决。

### Recommendation

GO — 核心诊断+定位假设强力成立。C4 repair 效用边际通过，作为已知弱点在 research 阶段通过以下路径解决：(1) 改进 repair prompt/机制拉大 targeted vs blind delta, (2) 分析 Unknown 样本为何驱动 C4 delta 可能产生有价值发现, (3) 必要时 reframe paper 聚焦 diagnosis+localization 而非 repair。建议立即进入 research 阶段，启动 post-MVP kickoff 流程。
