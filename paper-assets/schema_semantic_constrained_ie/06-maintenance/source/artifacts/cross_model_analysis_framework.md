# Cross-Model (Llama vs Qwen3) Analysis Framework

## 1. 推荐表格 Layout

**Table X: Cross-Model Generalization on SciERC (551 samples, 7 relations)**

| Model | Mode | DR↓ | RV↓ | ET↓ | ΔDR (rel.) | E-F1 | R-F1 | ΔR-F1 |
|-------|------|-----|-----|-----|------------|------|------|-------|
| Qwen3-8B | unconstrained | 15.37 | 1.39 | 0.40 | — | 31.01 | 8.23 | — |
| | full_s1 | 0.93 | 0 | 0 | **↓94%** | 30.98 | 8.36 | +0.13 |
| Llama-3.1-8B | unconstrained | 13.30 | 0.50 | 0 | — | 23.56 | 2.68 | — |
| | full_s1 | ? | ? | ? | **↓?%** | ? | ? | ? |

设计要点：
- **主指标列**: DR/RV/ET + ΔDR relative reduction（论文核心 claim 是 violation elimination，不是 F1）
- **F1 列靠右**: 作为 control variable，验证"零质量代价"
- **ΔDR 用相对百分比**（↓94%），不用绝对 pp 差——跨模型 baseline 不同，相对降幅才可比
- 若空间允许，grammar_only 行可加入作为 ablation，否则放 appendix

## 2. 叙事策略

**核心论证：方法有效性与模型无关，F1 基线差异不影响 claim。**

三层论证：

**(a) Violation reduction 是 model-agnostic 的。** 两模型 baseline violation 都 >>5% (Qwen3 15.37%, Llama 13.30%)，OntoCoDec 对两者施加相同约束编译流程（零代码修改）。如果 Llama full_s1 DR 也降到 <2%，则 relative reduction 一致性直接支撑 Claim 3（composable constraint framework 的 model-agnostic 性）。

**(b) F1 差异是 expected 且 irrelevant to the claim。** 两模型都是 zero-shot、8B 参数。Llama R-F1=2.68% vs Qwen3 8.23% 反映 instruction-following 能力差异，不影响约束层有效性。论文中用一句话解释："F1 differences reflect base model capability in zero-shot IE, not constraint effectiveness."

**(c) 不同 violation profile 增强 evidence。** Llama ET=0%（Qwen3 0.4%）, RV=0.5%（Qwen3 1.39%）——说明不同模型的违规模式不同，但 OntoCoDec 都能处理。若 Llama DR baseline 更低 (13.3% vs 15.37%)，则 full_s1 的绝对残余可能更低，进一步验证 "effectiveness scales with violation severity"。

**避免的陷阱：**
- 不要把两模型的 F1 横向比较——不是 apple-to-apple
- 不要 claim "Llama 上也有 F1 提升"——单 seed 无统计效力
- 如果 Llama ΔR-F1 为负，定位为 "within noise" 而非回避

## 3. Llama full_s1 结果到达后的分析 Checklist

- [ ] **DR reduction ratio**: 计算 ΔDR%，与 Qwen3 ↓94% 对比。目标 >80% 即可支撑 claim
- [ ] **RV/ET 是否归零**: grammar 层应保证 →0%，若非零则有 bug
- [ ] **R-F1 delta**: 计算 ΔR-F1 pp。±1pp 以内 = F1-neutral；若 >-2pp 需讨论
- [ ] **Per-relation DR**: 检查 Compare/Feature-of 等高违规 relation 的 Llama 表现
- [ ] **CF rate**: 如 Llama 也出现 CF 升高，强化"CF 是 semantic 层的系统性副作用"证据
- [ ] **Constraint tightness 一致性**: SciERC 约束对两模型相同，tightness↔DR 关系应一致
- [ ] **统计检验**: McNemar test (paired per-triple violation/non-violation) 验证 DR 降幅显著性。N=551 samples，bootstrap CI 不必要（McNemar 足够）
- [ ] **写入 paper_framing.md**: 更新 C5 回应和 Risk #2
