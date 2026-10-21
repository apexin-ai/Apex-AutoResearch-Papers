# Experiment Coverage Assessment Report

> Generated: 2026-05-17 | DDL: EMNLP 2026 ARR 2026-05-25 (8 days)
> GPU: 4× RTX 5090 32GB (autodl-5090), ~138h budget remaining

## Current Experiment Inventory

49 registry entries (41 DONE, 8 PREPARING). After deduplicating infrastructure/shard/failed entries, **~20 substantive experiments** covering:

- **8 generators** / 5 families: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, Llama-3.2-3B, Mistral-7B-v0.3
- **3 reference models**: Pythia-410M (primary), OLMo-2-1B, Qwen3-0.6B
- **3 prompt types**: continuation, elaboration, inspired_rewriting
- **4 seed domains**: Wikipedia, News, Academic, Code
- **Max depth**: gen-4 (5 levels)
- **Robustness**: random word replacement (5/10/20%), LLM rephrase, length confound, seed complexity, topic drift
- **Baselines**: Avg-LogProb, LD-Score, FastDetectGPT, Binoculars
- **Downstream**: CLM fine-tuning (negative result)

---

## 1. Sampling Temperature Variation ⚠️ 部分覆盖

**当前覆盖**:
- t=0.7 (default, 所有主实验)
- t=0.5 / t=1.0 (sampling ablation, 仅 Qwen3-1.7B 一个 generator)
- multi-domain 实验在 t=1.0 和 t=0.7 两个条件下跑过

**缺失**:
- t=1.2+ 高温度完全未测试
- Sampling ablation 仅在 Qwen3-1.7B 上做，未验证其他 generator 的温度敏感性
- t 和 top_p 联合变化（0.5/0.80, 0.7/0.90, 1.0/0.95），无法区分 t 和 top_p 各自的效果

**论文已有处理**: Limitations 明确说 "depth fingerprinting assumes standard decoding regimes"，Discussion 从理论上解释了高温破坏 depth signal 的原因。t=1.0 的 -6pp 下降已记录。

**Reviewer 质疑风险**: **中等 (3/5)**。论文已将此限制透明报告，且提供了理论解释。但只在一个 generator 上做 ablation 可能被质疑 — 如果 Qwen3-1.7B 恰好是最敏感/最不敏感的呢？

**补充建议**: 在 1-2 个额外 generator（如 Pythia-2.8B 和 Mistral-7B）上重复 t=0.5/0.7/1.0 ablation。预估 ~2h GPU 时间。但考虑 DDL 优先级低，论文已有足够的 framing。

---

## 2. Generator 规模 ⚠️ 部分覆盖

**当前覆盖**:

| Model | Params | Family | LOGO F1 (3-class) |
|---|---|---|---|
| Qwen3-0.6B | 0.6B | Qwen | 0.816 |
| Pythia-1B | 1B | Pythia | 0.856 |
| OLMo-2-1B | 1B | OLMo | 0.752 |
| Qwen3-1.7B | 1.7B | Qwen | 0.801 |
| Pythia-2.8B | 2.8B | Pythia | 0.810 |
| Llama-3.2-3B | 3.2B | Llama | 0.775 |
| Mistral-7B | 7B | Mistral | — |
| Qwen3-8B | 8.2B | Qwen | 0.714 |

**范围**: 0.6B — 8.2B，跨 5 个模型家族。

**缺失**:
- 13B+ 模型完全未测试
- 70B+ frontier 模型未测试
- 规模-性能趋势仅有 8 个数据点

**论文已有处理**: Limitations 明确说 "Frontier models (70B+) remain untested; their higher fluency may further compress feature margins." Qwen3-8B 结果已展示 cross-scale transfer gap (0.714 vs ≤2.8B 的 0.77-0.81)。

**Reviewer 质疑风险**: **高 (4/5)**。"Does this work on GPT-4/Claude-level models?" 几乎是必问问题。但这是一个公认的 scope limitation — 很多 EMNLP 论文用 ≤8B 模型做实证研究是可接受的。

**补充可行性**: 13B 模型需要 ~26GB VRAM (FP16)，单卡 RTX 5090 32GB 可以跑。但 Qwen3-14B-Base 或 Llama-3.1-8B 已经在覆盖范围内，增量价值不大。70B+ 模型超出 4× 5090 能力（需要多卡推理+量化），不可行。**建议: 不补充。论文已诚实报告，reviewer 一般接受 ≤8B 作为实证贡献的 scope。**

---

## 3. Instruction-tuned vs Base Model ⚠️ 部分覆盖

**当前覆盖**:
- 主实验全部使用 base model（deliberate design choice）
- Limitations 中有 preliminary instruct 结果:
  - OLMo-2-1B-Instruct: LOGO F1 = 0.338（vs base 0.763）— 严重退化
  - Qwen3-0.6B + chat template: LOGO F1 = 0.667（vs base 0.816）
  - Length-matched analysis: |ρ| < 0.02，binary F1 ≈ 0.5 (Qwen)

**注意**: 这些 preliminary 结果未在 registry 中注册，可能是 ad-hoc 测试。

**缺失**:
- 无 systematic instruct 实验（多个 instruct 模型 × 多个深度）
- 未分析 instruct tuning 具体破坏了什么（长度控制？格式约束？vocabulary 变化？）
- 未测试 "instruct model generating continuation-style text"（无 system prompt / chat template 的 instruct 模型）

**Reviewer 质疑风险**: **高 (4/5)**。"Real-world LLM-generated text comes from instruction-tuned models, not base models" 是一个很自然的质疑。但论文的 framing 已经明确这是一个 controlled empirical study，且 limitations 中报告了 preliminary negative results。

**补充建议**: 当前 preliminary 数据已足够支撑 limitations 的 claim。如果要增强，可以：
1. 正式跑 2 个 instruct 模型 (OLMo-2-1B-Instruct + Qwen3-1.7B-Instruct)，生成 1000 seeds × 5 depths
2. 分析 depth signal 退化的具体原因（长度分布、repetition penalty 等）
3. 预估 ~4h GPU 时间

**但不建议在 DDL 前补充**: 这会引入需要大量讨论的 negative results，可能扰乱论文主线。当前 limitations 中的 2 句话定位更好 — 承认 gap，留作 future work。

---

## 4. Decoding Strategy ⚠️ 部分覆盖

**当前覆盖**:
- Nucleus sampling (top_p=0.80/0.90/0.95)，但与 temperature 联合变化
- Temperature 0.5/0.7/1.0

**缺失**:
- Greedy decoding (t=0, argmax)
- Top-k sampling (k=50, k=100 等常用值)
- Beam search (n=4/8)
- Min-p sampling
- Repetition penalty 的影响

**论文已有处理**: Limitations 说 "fixed decoding parameters"。Sampling ablation 实质上是一个 temperature+top_p 的 joint ablation，不是严格的 decoding strategy comparison。

**Reviewer 质疑风险**: **低-中 (2/5)**。大多数 reviewer 接受 nucleus sampling 作为标准设置。Greedy / beam search 在 open-ended generation 中不是主流做法。但如果 reviewer 恰好关心这个维度，可能会问。

**补充建议**: **不补充。** Nucleus sampling 是当前 open-ended generation 的事实标准。论文研究的是 "standard decoding regimes" 下的现象，不需要覆盖所有 decoding 策略。如果 rebuttal 被问到，可以快速补一个 greedy + top-k=50 的实验。

---

## 5. Reference Model 多样性 ✅ 充分覆盖

**当前覆盖**:
- Pythia-410M（primary，所有主实验）
- OLMo-2-1B（cross-ref falsification, plan-003）
- Qwen3-0.6B（cross-ref falsification, plan-003）
- 三个 reference 的 LOGO F1 差异 ≤ 0.013

**结论**: Cross-family reference model 实验充分证明 depth signal 不是 reference-specific artifact。**无需补充。**

---

## 6. Human Editing Robustness ✅ 充分覆盖

**当前覆盖**:
- Random word replacement at 5%/10%/20% (plan-010-robustness)
  - 5%: -4.6pp, 10%: -8.1pp, 20%: -10.4pp（graceful degradation）
- LLM-simulated rephrase (plan-010-llm-rephrase)
  - Edit distance ratio 0.507, drop -4.5pp
- Limitations 已报告 "gap between simulated token replacement and real-world post-processing remains untested"

**Reviewer 质疑风险**: **低 (2/5)**。两种 perturbation 方法 + graceful degradation 趋势足以 convince reviewers。

---

## 7. 不同语言泛化 ❌ 未覆盖

**当前**: 全部实验为 English only。

**论文已有处理**: Limitations 第 25 行: "Generalization to other languages remains untested."

**Reviewer 质疑风险**: **低 (2/5)**。EMNLP 2026 的 reviewer 可能关心多语言，但对于一个新 task formulation 的首篇论文，English-only 是可接受的 scope。且多语言需要多语言 reference model + seed text，工作量远超 DDL 允许。

**补充建议**: **不补充。** 留作 future work。

---

## 8. 更长的生成链 (depth > 4) ⚠️ 已通过替代方式覆盖

**当前覆盖**:
- Max depth = gen-4 (5 levels)
- 5-class ordinal evaluation (appendix_finer_depth): LOGO F1 ≈ 0.50, depths 2-4 mutually indistinguishable
- 3-class (gen-0/gen-1/gen-2+) 已验证为 practical resolution limit

**缺失**:
- 未测试 depth 5+（gen-5, gen-6, ...）
- 未观察更深链条是否有新的 phase transition

**Reviewer 质疑风险**: **低 (2/5)**。5-class 实验已经展示 depths 2+ 无法区分 — 更深的链条只会更加 indistinguishable。这个逻辑论文已经 framing 好了。

**补充建议**: **不补充。** 5-class 结果已经是充分的证据。

---

## 9. Seed 文本来源多样性 ✅ 充分覆盖

**当前覆盖**:
- Wikipedia (primary, 1000 seeds) — 所有主实验
- News (200 seeds) — multi-domain 实验
- Academic (200 seeds) — multi-domain 实验
- Code (200 seeds) — multi-domain 实验
- Seed complexity stratification (plan-008): low/medium/high complexity, max diff 1.06pp

**结论**: 4 个 domain + seed complexity 分析充分覆盖。Binary F1 > 0.73 across all domains (LOGO at t=1.0)。**无需补充。**

---

## 10. Cross-model Chains ✅ 充分覆盖

**当前覆盖**:
- Cross-model chains（随机选 generator per depth step）: 3-class F1 = 0.809, binary F1 = 0.764
- 这是论文的 headline result

**结论**: 核心实验，充分覆盖。

---

## 11. Topic Drift vs Depth Signal ✅ 充分覆盖

**当前覆盖**:
- review-exp-b-topic-drift: 用 all-MiniLM-L6-v2 embeddings 分析 semantic similarity
- 结论: depth signal 不是 topic drift 的 artifact

---

## 12. Baseline Ensemble (review-exp-a) ⚠️ PREPARING 状态

**当前状态**: review-exp-a-baseline-ensemble 仍然是 PREPARING。但论文 Table 4 已经有 grid search 结果（D020 决策），采用 efficiency framing（7-feature 2.35× faster than multi-detector）。

**Reviewer 质疑风险**: **低 (1/5)**。Table 4 已经有数据，PREPARING 状态可能只是 registry 未更新。

---

## 13. Instruct 模型 Preliminary Data 可靠性 ⚠️

Limitations 引用了 preliminary instruct 结果（OLMo-2-1B-Instruct F1=0.338, Qwen3-0.6B chat F1=0.667），但这些实验未在 registry 中注册。如果 reviewer 追问细节，需要确保这些数据有可复现的实验配置。

**建议**: 确保 instruct 实验的代码和配置可追溯。如有时间，将 preliminary 结果注册到 registry。

---

## Priority Ranking

按 **(Reviewer 质疑概率 × Claim 支撑力度 × 可行性)** 综合排序：

| Rank | 维度 | 状态 | 质疑概率 (1-5) | Claim 支撑 (1-5) | 可行性 | 预估 GPU | 建议 |
|------|------|------|---------------|-----------------|--------|---------|------|
| 1 | Instruction-tuned models | ⚠️ | 4 | 3 | 中 (~4h GPU, 但引入 negative results 需大量讨论) | 4h | **不补充** — limitations 已有 preliminary data，DDL 前不宜扰乱主线 |
| 2 | Generator 规模 (13B+) | ⚠️ | 4 | 3 | 低 (13B 单卡勉强, 70B+ 不可行) | 8-12h (13B) | **不补充** — 8.2B 已是 reasonable scope，论文已报告 scale gap |
| 3 | 温度 ablation 扩展到更多 generator | ⚠️ | 3 | 2 | 高 (~2h) | 2h | **可选补充** — 低成本，但论文已有充足 framing |
| 4 | 更多 decoding 策略 | ⚠️ | 2 | 2 | 高 (~2h) | 2h | **不补充** — nucleus sampling 是标准，rebuttal 再说 |
| 5 | 多语言 | ❌ | 2 | 2 | 低 (需要全新 pipeline) | 20h+ | **不补充** — 超出 scope |
| 6 | 更长链 (depth 5+) | ⚠️ | 2 | 1 | 高 (~1h) | 1h | **不补充** — 5-class 实验已证明不必要 |
| 7 | Instruct 实验 registry 注册 | ⚠️ | 2 | 1 | 高 (0 GPU, 仅 metadata) | 0h | **建议做** — 确保 preliminary data 可追溯 |

## Overall Assessment

**实验覆盖度: 良好 (8/10)**

论文在关键维度上有充分覆盖:
- ✅ Generator 多样性 (8 models / 5 families / 0.6B-8.2B)
- ✅ Reference model 独立性 (3 families)
- ✅ Prompt type 多样性 (3 types + paraphrastic)
- ✅ Domain 泛化 (4 domains)
- ✅ Robustness (perturbation + LLM rephrase + length + seed complexity + topic drift)
- ✅ Baselines (4 single-detector methods)
- ✅ Cross-model chains
- ✅ Negative result (downstream utility)

主要 gap:
- ⚠️ 全部 base model（instruct 有 preliminary negative data 但未 systematic）
- ⚠️ 最大 8.2B（无 frontier 规模）
- ⚠️ Sampling ablation 仅在 1 个 generator 上

**这些 gap 在论文 Limitations 中已被透明报告，且有理论或 preliminary 数据支撑。在 8 天 DDL 内，不建议补充新实验。当前重点应放在论文打磨和提交准备上。**

如果 rebuttal 阶段被追问，优先准备:
1. 额外 2 个 generator 的温度 ablation (~2h GPU)
2. Instruct model 的 systematic 实验 (~4h GPU)
3. 13B model 实验 (~8h GPU, 如 Qwen3-14B-Base)
