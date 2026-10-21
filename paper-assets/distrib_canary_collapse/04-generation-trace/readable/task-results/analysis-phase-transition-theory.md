# analysis phase transition theory

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_transition_theory_20260520T091349_result.json`
- **Structured JSON:** [`c6fd6971613a3bcca92e.json`](../../sessions/c6/c6fd6971613a3bcca92e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有产出已注册。核心结论：

### D127 Phase Transition Analysis 完成

**1. Phase Transition Type: Steep Crossover (approaching first-order)**
- α=0.45→0.50 跳变：PermG 从 0/8 到 6/8，3 seed 全部一致
- Sigmoid fit: **α_c=0.476**, steepness k≥200, transition width Δα≈0.02
- 近乎开关式，但严格来说需更密采样才能 claim true discontinuity
- 论文建议用 "**sharp onset of causal detectability**" 或 "near-discontinuous onset"

**2. Sigmoid >> Power Law**
- Sigmoid R²=0.969, AIC=-8.90
- Power law R²=0.808, AIC=9.30
- ΔAIC=18.2，sigmoid 压倒性优势

**3. Model Scale: 无单调关系**
- Qwen-0.8B (7.0) ≈ Pythia-6.9B (7.0) > Pythia-410M (6.0) > 1.4B (4.0) > SmolLM3-3B (3.0)
- 弱化根因是 entropy trajectory shape（U 型/饱和），不是 model size
- ECE canary 在所有模型上比 entropy 更鲁棒

**4. vs Gu et al.**: α_c≈0.48 是 detection threshold 不是 collapse threshold；iterative compounding 下 effective contamination 在 α=0.45 和 0.50 几乎相同（99.88% vs 99.95%），但 PermG 从 0 跳到 6。两者互补但不可直接比较。

**5. 缺口**: α=0.60 无 canonical 数据，等 M046 canonical sweep。

图表位于 `westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts_phase_transition/`。

---
