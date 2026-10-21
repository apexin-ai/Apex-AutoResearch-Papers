# Appendix 交叉引用审查

## 统计
- 主文引用 appendix 次数：64
- 唯一 label 数：33
- 所有 label 均存在：**是**

## 逐条审查

| # | 主文位置 | 引用 label | 主文语境 | Appendix 内容摘要 | 评估 |
|---|---------|-----------|---------|-----------------|------|
| 1 | introduction.tex:L8 | `sec:mechanistic` | "hidden-state probe...AUROC 0.63–0.88; Appendix" | §How Self-Verification Fails: ESJ/MRSC/LSC probes, hidden-state probe, introspection boundary（~30行正文 + Table） | ✅ 充分 |
| 2 | introduction.tex:L11 | `app:re_extension` | "RE reveals a distinct bottleneck (40% zero-F1)" | §Exploratory Extension to RE: diagnostic framework, QE, selection, scale ablation, free-form decoding（~90行，多表） | ✅ 充分 |
| 3 | introduction.tex:L14 | `app:re_extension` | "RE F1 confounded by entity span errors" | 同上 | ✅ 充分 |
| 4 | introduction.tex:L28 | `sec:mechanistic` | "Hidden-state probes reveal introspection boundary" | 同#1 | ✅ 充分 |
| 5 | method.tex:L6 | `app:notation` | "notation in Appendix" | §Notation: Table with all symbols（27行，完整符号表） | ✅ 充分 |
| 6 | method.tex:L8 | `app:supervised_combination` | "LP mean weight 0.78" | §Supervised and Model-Internal Signal Analysis: LR/MLP/RF classifiers, DeBERTa verifier, grid-search（~12行详细分析） | ✅ 充分 |
| 7 | method.tex:L33 | `app:fk_independence` | "FK independence analysis" | ¶FK independence permutation test: 3 configs, Table with t-stats, split-half r（~25行） | ✅ 充分 |
| 8 | method.tex:L56 | `app:additional` | "exclude instances with no gold annotations" | §Additional Analyses: signal heatmap, per-relation diagnostic, capability stratification, length analysis, WNUT（~130行，多表多图） | ✅ 充分 |
| 9 | method.tex:L80 | `app:mbr_proof` | "proof in Appendix" | §MBR Framework and Proof: formal proof of Proposition 1（~25行，完整证明） | ✅ 充分 |
| 10 | diagnostic.tex:L8 | `app:notation` | "notation in Appendix" | 同#5 | ✅ 充分 |
| 11 | diagnostic.tex:L10 | `app:supervised_combination` | "LP mean weight 0.78, structural zero weight" | 同#6 | ✅ 充分 |
| 12 | diagnostic.tex:L22 | `app:token_signal` | "length normalization +4.6 F1 points" | §Token-Level Signal Comparison: mean vs cumulative LP, +4.6pp, Wilcoxon test（~8行） | ✅ 充分 |
| 13 | diagnostic.tex:L34 | `app:fk_independence` | "FK independence" | 同#7 | ✅ 充分 |
| 14 | diagnostic.tex:L41 | `app:additional` | "instance exclusion" | 同#8 | ✅ 充分 |
| 15 | experiments_main.tex:L13 | `app:training` | "LoRA fine-tuned...training details" | §Training Configuration: Table with all hyperparameters, prompt template, constrained decoding details（~50行） | ✅ 充分 |
| 16 | experiments_main.tex:L13 | `app:epoch_confound` | "Few-NERD uses 3 epochs vs 5" | §Epoch Confound Analysis: Few-NERD 3v5, SciERC 3/5/10 epoch curve, 2 tables（~70行） | ✅ 充分 |
| 17 | experiments_main.tex:L14 | `app:n_scaling` | "N∈{16,32,64} for scaling" | §N-Scaling Detailed Analysis: signal quality vs N, ranking stability, inverse scaling, theta sweep tables（~140行，多表） | ✅ 充分 |
| 18 | experiments_main.tex:L29 | `app:re_extension` | "RE in Appendix" | 同#2 | ✅ 充分 |
| 19 | experiments_main.tex:L50 | `app:bootstrap_signal` | "bootstrap CIs confirm the gap" | §Bootstrap CI for Signal Comparisons: individual CIs, pairwise Δρ, seed-replication analysis（~45行，2 tables） | ✅ 充分 |
| 20 | experiments_main.tex:L51 | `app:bootstrap_signal` | "Holm-Bonferroni p_adj=0.013" | 同#19 | ✅ 充分 |
| 21 | experiments_main.tex:L76 | `app:epoch_confound` | "5-epoch degeneracy 26%" | 同#16 | ✅ 充分 |
| 22 | experiments_main.tex:L78 | `app:pertype` | "per-type MV degradation ρ=0.90" | §Per-Type MV Analysis: 8 entity types, pretrained vs finetuned comparison, Table（~30行） | ✅ 充分 |
| 23 | experiments_main.tex:L81 | `app:per_type_lp` | "per-type LP ρ=-0.881" | §Per-Entity-Type LP Selection: Few-NERD/CoNLL/SciERC per-type tables, degeneracy-headroom correlation（~70行，3 tables） | ✅ 充分 |
| 24 | experiments_main.tex:L86 | `app:per_type_lp` | "per-type LP (figure caption)" | 同#23 | ✅ 充分 |
| 25 | experiments_main.tex:L91 | `app:re_extension` | "RE framework extends, 40% zero-F1" | 同#2 | ✅ 充分 |
| 26 | experiments_main.tex:L96 | `app:calibration` | "signal rankings robust; calibration" | §Calibration Analysis: reliability diagrams, ECE values（~12行 + figure） | ✅ 充分 |
| 27 | experiments_main.tex:L103 | `app:theta_sweep` | "θ stable in [0.15, 0.35]" | §Entity Construction Threshold Sensitivity: 8-point sweep × 3 datasets, Table（~45行） | ✅ 充分 |
| 28 | experiments_main.tex:L105 | `app:holm` | "global k=57 Holm-Bonferroni" | §Holm-Bonferroni Enumeration: complete 57-test table with raw p and p_adj（~90行） | ✅ 充分 |
| 29 | experiments_main.tex:L107 | `app:epoch_confound` | "5-epoch LP gains collapse" | 同#16 | ✅ 充分 |
| 30 | experiments_main.tex:L113 | `app:freeform_ablation` | "decoding modes" | §Free-Form Decoding Ablation: 3-panel table, LP distribution, selection F1, QE comparison（~110行） | ✅ 充分 |
| 31 | experiments_main.tex:L114 | `app:n_scaling` | "Qwen2.5-7B N=32 +3.85pp" | 同#17 | ✅ 充分 |
| 32 | single_signal.tex:L6 | `app:logprob_ties` | "60% LP range below 0.041 nats" | §Log-Probability Score Compression: CDF figure, tied fraction table, ε sweep, non-tied subset（~90行，多表多图） | ✅ 充分 |
| 33 | single_signal.tex:L6 | `app:freeform_ablation` | "free-form decoding yields identical LP" | 同#30 | ✅ 充分 |
| 34 | single_signal.tex:L39 | `app:bootstrap_signal` | "MDE ≈1.5pp" | 同#19 | ✅ 充分 |
| 35 | single_signal.tex:L40 | `app:bootstrap_signal` | "bootstrap CIs reported" | 同#19 | ✅ 充分 |
| 36 | single_signal.tex:L49 | `app:per_type_lp` | "per-type ρ=-0.881" | 同#23 | ✅ 充分 |
| 37 | single_signal.tex:L52 | `sec:mechanistic` | "Mechanistic evidence paragraph header" | 同#1 | ✅ 充分 |
| 38 | single_signal.tex:L53 | `app:esj` | "ESJ AUROC 0.50–0.55 on Qwen3-8B" | §Cross-Dataset Entailment Self-Judgment: 3-dataset ESJ vs agreement Table（~20行） | ✅ 充分 |
| 39 | single_signal.tex:L56 | `app:esj` | "cross-model ESJ validation" | 同#38 | ✅ 充分 |
| 40 | adaptive.tex:L9 | `sec:mechanistic` | "self-verification methods in Appendix" | 同#1 | ✅ 充分 |
| 41 | adaptive.tex:L9 | `app:method_coverage` | "Full coverage in Appendix" | §Method Coverage Matrix: 7-method × 5-dataset/model table（~25行） | ✅ 充分 |
| 42 | adaptive.tex:L21 | `app:dals` | "DALS +0.71pp" | §Degeneracy-Aware LP Selection: DALS algorithm, 3-dataset results, LOO τ sensitivity（~15行） | ✅ 充分 |
| 43 | adaptive.tex:L23 | `app:supervised_combination` | "LR/MLP/RF -0.4 to -3.1pp" | 同#6 | ✅ 充分 |
| 44 | adaptive.tex:L39 | `app:verifier_transfer` | "cross-dataset transfer -0.76 to -1.02pp" | §Entity-Level Verifier Transfer: LightGBM AUC, OOF gains, cross-dataset negative transfer（~8行） | ✅ 充分 |
| 45 | discussion.tex:L5 | `app:freeform_ablation` | "decoding modes" | 同#30 | ✅ 充分 |
| 46 | mechanistic.tex:L5 | `app:self_verification` | "full results in Appendix" | §Entity-Level Self-Verification Probes: ESJ/MRSC/LSC details, Table with metrics（~45行） | ✅ 充分 |
| 47 | mechanistic.tex:L21 | `app:hidden_probe` | "GroupKFold CV details" | §Hidden State Probes: linear/MLP probe, cross-dataset, token-level aggregator（~35行 + Table） | ✅ 充分 |
| 48 | mechanistic.tex:L24 | `app:hidden_probe` | "MLP probe 13.9% oracle gap" | 同#47 | ✅ 充分 |
| 49 | theory.tex:L5 | `app:mbr_proof` | "MBR proof" | 同#9 | ✅ 充分 |
| 50 | theory.tex:L7 | `app:fewnerd_epsilon` | "LP compression threshold ε=0.05" | ¶Few-NERD LP compression threshold sensitivity: elbow analysis（~45行） | ✅ 充分 |
| 51 | theory.tex:L12 | `app:frontier_sc` | "GPT-5.5 parse failures" | §Frontier Model Self-Consistency: 4-model comparison table, parse failure handling, entity matching methodology（~40行） | ✅ 充分 |
| 52 | theory.tex:L13 | `app:cross_scale` | "degeneracy model-family-dependent" | §Cross-Scale and Cross-Family Comparison: 10-row cross-scale table, few-shot analysis, degeneracy comparison, 4B ablation（~100行，多表） | ✅ 充分 |
| 53 | theory.tex:L23 | `app:n_scaling` | "40 of 58 inverse transitions" | 同#17 | ✅ 充分 |
| 54 | theory.tex:L25 | `app:degen_inverse` | "degeneracy vs inverse scaling OR=0.109" | ¶Degeneracy and inverse scaling: stratified table, 6 settings, Fisher exact test（~30行 + Table） | ✅ 充分 |
| 55 | theory.tex:L26 | `app:fs_error` | "few-shot QE improves but not construction" | §Few-Shot Error Correlation Analysis: error overlap Jaccard, entity entropy comparison（~10行） | ✅ 充分 |
| 56 | theory.tex:L33 | `app:bound_proof` | "proof of degeneracy decomposition" | §Degeneracy Decomposition: definitions, full proof, numerical verification table（~50行） | ✅ 充分 |
| 57 | theory.tex:L50 | `app:alpha_crit` | "Proposition entity selection bound" | §Entity Selection Bound: Proof and Validation: proposition, proof, α_crit table（~60行） | ✅ 充分 |
| 58 | theoretical.tex:L6 | `app:bound_proof` | "proof in Appendix" | 同#56 | ✅ 充分 |
| 59 | checklist.tex:L24 | `app:training` | "datasets cited, training framework" | 同#15 | ✅ 充分 |
| 60 | checklist.tex:L36 | `app:training` | "dataset characteristics" | 同#15 | ✅ 充分 |
| 61 | checklist.tex:L48 | `app:training` | "computing infrastructure" | 同#15 | ✅ 充分 |
| 62 | checklist.tex:L51 | `app:training` | "hyperparameters" | 同#15 | ✅ 充分 |
| 63 | checklist.tex:L57 | `app:training` | "LLaMA Factory, XGrammar" | 同#15 | ✅ 充分 |
| 64 | checklist.tex:L68 | `app:ai-assistants` | "AI assistants disclosure" | §Use of AI Assistants: Claude usage for code/writing/literature（~12行） | ✅ 充分 |

## 问题列表（按严重程度排序）

### 缺失的引用目标
无。所有 33 个唯一 label 均在 appendix.tex 中定义。

### 内容不足的 appendix 章节
无。所有被引用的章节均包含实质性内容（表格、图表、证明或详细分析）。

### 潜在注意事项

1. **`sec:mechanistic` 使用 `sec:` 前缀而非 `app:` 前缀** — 该 section 位于 appendix.tex 内（L607），但 label 使用 `\label{sec:mechanistic}` 而非 `\label{app:mechanistic}`。这不会导致编译错误（LaTeX 不区分前缀），但与 appendix 其他 section 的命名惯例不一致。同时，mechanistic.tex 主文文件中也存在完全相同的内容（标题、段落、数据完全一致），说明该 section 既在主文中有独立文件，也在 appendix 中有副本。如果两者都被 `\input` 编译，会产生 **duplicate label 警告**。需确认 main.tex 的 `\input` 顺序中是否只引用了其中一个。

2. **diagnostic.tex 与 method.tex 内容重叠** — diagnostic.tex 和 method.tex 均定义了 `\section{...}\label{sec:method}` 和 `\label{sec:formulation}` 等 label，内容高度重叠但不完全相同。如果两个文件同时被编译，会产生 duplicate label。需确认只有一个被 `\input`。

3. **theoretical.tex 与 theory.tex 内容重叠** — theoretical.tex（9行，精简版 degeneracy bound）和 theory.tex（51行，完整 scaling analysis）均存在，且 theoretical.tex 定义了 `\label{thm:degeneracy_bound}`，theory.tex L30 也定义了同名 label。需确认编译时只使用其中一个。

### 建议
- 确认 main.tex 的 `\input` 列表中没有同时引用重叠文件（method/diagnostic、theoretical/theory、mechanistic 主文版/appendix 版）
- 考虑将 `sec:mechanistic` 重命名为 `app:mechanistic` 以保持命名一致性（可选，不影响编译正确性）
