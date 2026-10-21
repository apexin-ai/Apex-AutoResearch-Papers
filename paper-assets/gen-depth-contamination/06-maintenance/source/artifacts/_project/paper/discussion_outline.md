# Discussion & Conclusion Outline

> 基于 Route B (K*=2) 框架，2+1 claim 结构。
> 标注 [PENDING] 的内容依赖 exp-006 / exp-015 未出结果。

---

## 6. Discussion

### 6.1 K* 的理论意义：Empirical Measurement vs Information-Theoretic Bound

**要点**：
- K*_empirical 是 K*_theory 的保守下界（lower bound），不是 exact measurement。DPI 保证 K*_theory 有限（Prop. 2）；我们在 15D feature projection 上测量 K*_empirical=2。更丰富的特征空间或更强分类器只可能使 K*_empirical 上移，不会下降。
- 必须明确承认 theory-practice gap：DPI 操作在 full joint distribution 上；K*_empirical 取决于 feature choice 和 threshold θ。措辞："K*_empirical provides a feature-dependent lower bound on the information-theoretic K*_theory."
- 引用 exp-003 decoding ablation 佐证 K* 捕捉的是 channel properties（greedy/nuc-p0.9/T0.7 均 K*=2 at θ=0.60），而非分类器 artifact。θ-sensitivity table（exp-003: θ=0.55→K*=3, θ=0.65→K*=2, θ=0.70→K*=1）进一步说明 K* 是 threshold-parameterized continuum。
- 与 He et al. (2025) entropy decline 的 cross-modal parallel：他们在 diffusion model 上观察到 generalization score 指数衰减，我们在 text 上观察到 AUC 快速衰减至 chance，现象一致，K* 提供了 operational cutoff。

**引用实验**：Table 1 (bootstrap CI), exp-003 θ-sensitivity table, theory_framework.md Prop 1-2。

### 6.2 K*=2 的实践含义：Three-Level Schema

**要点**：
- K*=2 意味着对 1.5B-scale models + standard decoding，depth-aware curation 只需区分三类：human (depth 0) / first-generation synthetic (depth 1) / multi-generation synthetic (depth ≥2)。这足以捕获关键质量边界。
- 0v1 近乎完美区分（AUC>0.99）= 现有 binary detector 已解决的问题。1v2 是唯一需要 ordinal estimation 的边界。depth≥2 文本信息论上不可细分，统一处理即可。
- [PENDING] exp-006 graduated filtering 结果将量化这个 3-class schema 相比 binary 的下游收益（MMLU/HellaSwag）。即使 exp-006 未完成，理论论证仍成立：binary filtering 在 threshold 附近丢信息，3-class 提供 soft gradation。
- 对 Drayson et al. (2025) 的直接推论：他们的 SIR weighting $w \propto (1-q)^b$ 是 K*=1 的特例。K*=2 说明至少可以从 gen-1 中进一步分离 gen-2+ 以获得更 calibrated 的权重。

**引用实验**：Table 1 (0v1 vs 1v2 AUC gap), [PENDING] exp-006 downstream results。

### 6.3 Generation Mode as Confound

**要点**：
- Rewrite mode 的 1v2 AUC (0.6957) 比 continuation (0.6112) 高 8.4pp，但 rewrite 的跨模型 transfer 只有 61-63% retention（vs continuation 80-92%）。
- Interpretation：rewrite 的 instruction-following 注入 mode-specific style artifacts（top feature 是 freq_entropy 而非 surp_d1_std），放大了 depth signal 但降低了泛化性。
- 这构成 detectability-generalizability tradeoff：rewrite 在单模型内更 discriminable 但跨模型不泛化；continuation 信号较弱但跨模型稳健。
- 对后续研究的建议：(1) 任何跨模型 depth estimation 工作应以 continuation mode 为 canonical condition；(2) 基于 rewrite mode 的结果不应直接泛化到其他模型。
- cont→rw 89% vs rw→cont 82% 不对称性证明 continuation features 是 rewrite 的通用子集。

**引用实验**：Table 1 (Qwen-rw vs Qwen-cont), Table 2 (transfer matrix), Table 3 (top features)。

### 6.4 Depth Signal 的 Text-Intrinsic vs Model-Specific 分解

**要点**：
- Pythia↔OLMo（同为 continuation mode，不同架构）91-92% accuracy retention → depth signal 大约 70-85% text-intrinsic。
- 剩余 15-30% model-specific component 可能包括：(1) surprisal features 使用的 reference model 与 generating model 的 overlap；(2) 模型特有的 tokenization artifacts。
- 措辞约束：只能说 "mode-conditioned consistency with architecture residuals"，不能说 "universal"——因为我们只测了 3 个模型族（Pythia/OLMo/Qwen），且都是 ≤1.5B scale。
- Top-3 features（surp_d1_std, surp_std, surp_d2_std）在所有 continuation-mode 模型中共享，Spearman ρ≥0.85。共享机制：每次生成步骤平滑 token-level surprisal landscape，降低其方差。
- Limitation: depth-pair level 一致性较弱（τ~0.37 at 1v2），aggregate ranking 的高一致性不代表 boundary-level precision 相同。

**引用实验**：Table 2 (transfer retention), Table 3 (feature ρ), exp-005 τ matrix。

### 6.5 Limitations

逐条列出，每条 2-3 句，坦诚承认：

**(a) 模型规模 ≤1.5B**
- 所有实验使用 Pythia-1.4B, OLMo-1B, Qwen2.5-7B-Instruct（generation 用 7B，features 在 1.5B scale 上提取）。K* 是否随模型规模变化是 open question——更大模型可能产生更 subtle 的 depth artifacts，使 K* 上移。
- Dream review 提到 7B K*≥3 证据 fragile（CI lower 仅超 θ 0.15pp），当前论文不含 7B K* 结果，但应 flag scale limitation。

**(b) Prompt-chain vs retrain-chain**
- 所有实验使用 prompt-chain（each generation independently generated from previous output）。Retrain-chain（LoRA fine-tune per generation）更接近真实 web contamination 循环。
- Prompt-chain 是 upper bound estimate：如果 prompt-chain 下 K*=2，retrain-chain（更强的 distributional drift）K* 只可能更小或相同。
- 但 prompt-chain 的 Markov assumption (A2) 在 retrain-chain 下不严格成立。

**(c) θ=0.60 阈值**
- θ 是最关键的设计选择。AUC=0.60 仅比 chance (0.50) 高 10pp。选择基于 permutation test null distribution 的分离，但没有 information-theoretic principled derivation。
- θ-sensitivity：θ=0.55→K*=3, θ=0.60→K*=2, θ=0.70→K*=1（exp-003 data）。定性 gradient 稳健，但绝对 K* 值依赖 θ。
- 措辞建议："K* should be interpreted as parameterized by θ; we report θ=0.60 as our primary operating point and provide sensitivity analysis."

**(d) Qwen-cont CI 边缘**
- Qwen-cont 1v2 CI lower (0.6015) 仅超过 θ=0.60 0.15pp。虽然 permutation p=0.002，但 bootstrap margin 极窄。
- 承认这是 "robust but not trivially so"（experiments_c1.tex 已有此措辞）。如果样本量翻倍，CI 会收窄——当前 margin 部分反映样本量限制。

**(e) 英语/C4 单一 domain**
- 仅实验于 C4 英语 web text。K* 可能随 domain（code, scientific, dialogue）和语言变化。
- 这是 explicit scope boundary，不是 methodology flaw。

**(f) [PENDING] Learned representations comparison**
- exp-015 (neural probe) 尚未运行。如果 learned representations 的 K* 高于 hand-crafted features，说明 15D projection 是 K*=2 的部分原因。如果相同，则加强 information-theoretic impossibility 论证。

**引用实验**：exp-003 θ-sensitivity, Table 1 (Qwen-cont CI), exp-015 [PENDING]。

### 6.6 与 Drayson et al. (2025) 的对比定位

**要点**：
- Drayson et al. 是最直接的 prior work。他们训练 binary MGT detector (ModernBERT-150M, AUC .986 in-distribution) + SIR importance resampling 以防止 model collapse。
- 关键差异 axis 1（detection granularity）：他们做 binary（human vs synthetic），我们做 ordinal depth estimation。他们的 SIR 权重 $w \propto (1-q)^b$ 是 K*=1 special case。
- 关键差异 axis 2（目标）：他们防止 retrain-loop 中的 collapse；我们量化 recursive contamination 的 depth structure 并提供 depth-graduated curation。
- 关键差异 axis 3（scope）：他们用 encoder-only detector（黑盒分类）；我们用 interpretable 15D features 揭示 degradation ordering mechanism。
- 互补性：他们的 binary detector 可作为 first-stage filter（reject obvious synthetic），我们的 depth estimator 作为 second-stage refinement（对 gen-1 做 depth-aware weighting）。
- [PENDING] exp-006 将包含 binary-Drayson baseline 对比。

**引用**：Drayson et al. (2025), literature_positioning_notes.md 的 Related Work Draft。

### 6.7 Broader Impact

**要点**：
- **Data governance**：K* 为数据策展者提供 operational guidance——"对于 model X + decoding Y，depth ≥K* 的文本无需细分"。3-level schema (human/gen-1/gen-2+) 可嵌入 data pipeline 作为 quality tier annotation。
- **Benchmark contamination auditing**：如果 training data 含递归合成文本，benchmark performance 可能被 inflated。Depth estimation 可识别可疑 benchmark overlap 的代际来源，而非仅标记 "synthetic"。
- **Ethical consideration**：depth estimation 工具也可被 misuse——攻击者可用 depth labels 优化 adversarial paraphrasing 以逃避 depth-based 过滤。但 K*=2 本身限制了攻击面（depth ≥2 已不可辨别，无需 adversarial effort）。
- **Broader model collapse discourse**：采用 Schaeffer et al. (2025) taxonomy，K* 操作化了 Family B (distribution deformation, D4+D6) 的 discriminability boundary。这为 "model collapse" 的具体化提供了可测量、可复现的 operational quantity。
- 不应 overclaim：我们的结果限于 ≤1.5B 开源模型 + C4 英语。Frontier model (GPT-4, Claude) 和非英语场景需进一步研究。

**引用**：Schaeffer et al. (2025) taxonomy, Drayson et al. (2025) SIR framework。

---

## 7. Conclusion

### 7.1 核心贡献总结

**一句话 headline**：
> "We establish K*=2 as the generational discrimination boundary for recursive synthetic text under 1.5B-scale models with standard decoding: consecutive generations become statistically indistinguishable beyond depth 2, but the human/gen-1/gen-2+ trichotomy captures the critical quality boundary."

**C1' 总结**（3-4 句话）：
- 首次在受控实验中系统测量 K*_empirical。4 个模型配置（Pythia-1.4B, OLMo-1B, Qwen2.5-7B-Instruct rewrite/continuation）一致得出 K*=2（bootstrap 95% CI, permutation p≤0.002）。
- Cross-model transfer（Pythia↔OLMo 91-92% retention）表明 depth signal 约 70-85% text-intrinsic。
- Feature degradation ordering 在 continuation-mode 模型间高度一致（Spearman ρ≥0.85），共享机制为 surprisal landscape smoothing。
- Generation mode 是显著 confound（Δ=8.4pp），continuation mode 为 cross-model comparison 的 canonical condition。

**C3 总结**（1-2 句话）：
- [PENDING] exp-006: "K*-aware graduated filtering, which exploits the human/gen-1/gen-2+ trichotomy, yields X% improvement over binary filtering on MMLU and HellaSwag at Y% synthetic injection rate."
- 如果 exp-006 未完成，替代措辞："The K*=2 boundary implies that even a coarse 3-class ordinal signal carries more information than binary detection at the critical gen-1/gen-2+ boundary, motivating graduated curation strategies."

### 7.2 Key Takeaway（面向 practitioner 的 actionable message）

- 对于使用 ≤1.5B 开源模型 + standard decoding 的数据策展：binary detection 已覆盖 0v1；额外的 1v2 depth estimation（从 binary 到 3-class）是唯一有回报的 ordinal refinement；更细的 depth 分级没有统计支撑。
- K* 是 model-dependent, decoding-dependent, threshold-dependent 的 operating point，不是 universal constant。不同部署场景应重新测量。

### 7.3 Future Work

**(a) Retrain-chain validation**
- Prompt-chain 是 controlled setting；retrain-chain（每代 full fine-tune 或 LoRA adapt）更接近真实 web contamination 循环。K* 在 retrain-chain 下可能不同（预期 ≤ prompt-chain K*）。需验证 prompt-chain K* 作为 upper bound 的假设。

**(b) 更大模型**
- 7B+ models 可能因更强的表达能力产生更 subtle 的 depth artifacts，使 K* 上移。Scale → K* 关系是重要的 open question。
- 初步 decoding ablation 暗示 high-temperature (T=0.7) 下 K* 可能变化，但需在更大规模验证。

**(c) 非英语和多 domain**
- C4 英语是单一 domain。K* 可能在 code (structured syntax)、scientific text (domain terminology)、dialogue (turn-taking structure) 上有不同值。
- 多语言 K* 地图（中/法/德/日）对全球 data governance 有实际价值。

**(d) Real-world deployment**
- 将 3-level schema 嵌入 production data pipeline 需要 (1) fast inference（当前 15D features 比 neural probe 快 32.5×），(2) 对 out-of-distribution generators 的鲁棒性评估（cross-model transfer 已给出初步答案），(3) 与 existing data curation systems (DSIR, DoReMi) 的集成。
- [PENDING] exp-006 Common Crawl validation 将提供初步 real-world evidence。

**(e) Neural MI estimators**
- 当前 K*_empirical 基于 15D hand-crafted features。Neural MI estimators（MINE, InfoNCE）可直接在 representation space 测量 $I(X_0; X_k)$，提供更紧的 K*_theory 估计。
- [PENDING] exp-015 (neural probe) 将给出 learned representation 的 K* 比较。

---

## 写作注意事项

1. **措辞校准**：
   - "K*=2 across all tested configurations" ✓ — 有 bootstrap CI + permutation p 支撑
   - "text-intrinsic depth signal" → 改为 "largely text-intrinsic (70-85%)" — 不说 100%
   - 不说 "universally K*=2" — 只说 "across all four tested configurations"
   - 不说 "significantly" 除非有统计检验支撑

2. **Qwen-rewrite 使用限制**：
   - Qwen-rewrite 数据只用于 generation mode analysis，不能支撑跨模型泛化 claim
   - 跨模型 claims 必须基于 continuation mode（Pythia/OLMo/Qwen-cont）

3. **[PENDING] 标记汇总**：
   - §6.2: exp-006 graduated filtering 下游 quantitative results
   - §6.5(f): exp-015 neural probe K* comparison
   - §6.6: exp-006 binary-Drayson baseline comparison
   - §7.1 C3 summary: exp-006 headline numbers
   - §7.3(d): exp-006 Common Crawl validation
   - §7.3(e): exp-015 neural probe results

4. **字数估计**：Discussion ~1500-1800 words, Conclusion ~400-500 words，共约 2 pages（8-page limit 下合理）。
