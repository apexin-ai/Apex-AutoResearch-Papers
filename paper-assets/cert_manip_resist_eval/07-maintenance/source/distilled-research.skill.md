# Distilled Research — Certifiable Manipulation Resistance for Multi-Judge LLM Eval

> 12 篇论文（8 深度+4 摘要），2025-2026。信息论评估、peer prediction、多智能体 scaling、错误相关性、对抗鲁棒性。

## 1. 信息论框架是领域共识
**7/8 深度论文**用 MI/Fano/DPI/f-散度。**高置信度**。
Kaneko2025 (NeurIPS spotlight): N_min≥log₂(1/ε)/I_max; Robertson2025-TVD-MI: 有界 f-散度保持多项式样本复杂度 (Thm 3.3)。
→ Baseline 必含 IT-based 方法；理论需 Fano 下界+可达性证明。

## 2. 跨 family 多样性 > 规模扩张
**6/12 篇直接验证**。**高置信度**。
Yang2026: 2 diverse ≥ 16 homogeneous (8×效率); Kim2025: same-company +6.6%, same-arch +7.6% error agreement; Turkmen2026: within ρ~0.7-0.8, cross ρ~0.4-0.5; Chen2026-BEI: cross-family 低 40-60%; Keppo2026: heterogeneity 破 collusion 22%→3%。
→ 必含 homo/hetero 对照组；报告 within vs cross-family ρ；推荐 3-5 跨 family judge。

## 3. Scaling 天花板
**5/12 篇**。**高置信度**。
Turkmen2026 Thm 4.4: error→Φ(Φ⁻¹(1-α)/√ρ); Yang2026: homo plateau N≈4; PEG: K=7 退化; Jung2026: scoring O(log N)。
→ 找 saturation point，报告 K_eff 或 K*。

## 4. 条件独立性假设是核心脆弱点
**4/12 篇**。**高置信度**。
PEG K=7 因独立性违反退化; Kim2025 证明错误系统相关; Qiu2026 collusion 分析有限。
→ 不假设条件独立；提供 ε=f(ρ) 退化曲线；用 Gaussian-copula 建模。

## 5. Baseline 与指标共识
**Baselines**: LLM-as-a-Judge 6/12, majority voting 4/12, peer prediction 3/12, top-k 2/12。
**Metrics**: accuracy 7/8, MI variants 4/8, ASR 3/12, Type-I/II 1/8。
**Datasets**: MMLU 3/12, ARC 2/12, multi-benchmark suites 4/12。
→ 最低：LLM-as-a-Judge + majority voting baseline; MMLU + ≥2 benchmarks; error rate + IT metric。

## 6. 竞品与空白
**竞品**: PEG (NeurIPS 2025) — dominant truthfulness 但假设独立无退化分析; Qiu2026 (ICLR 2026) — inverse scaling 但无 collusion 保证。
**空白（12 篇无一填补）**: (1) 单模型 IT bound→多 judge 组合的 formal extension; (2) 独立性违反的连续退化曲线; (3) performance vs robustness scaling duality; (4) adaptive attack 下多 judge 认证保证。

## 7. 有界 vs 无界散度
**2/12 直接证明，3/12 间接支持**。**中置信度**。
Robertson2025 Thm 3.3; Kaneko2025 Fano bound 隐含。
→ 机制设计选 TVD 等有界散度避免 KL；区分 polynomial vs exponential degradation。
