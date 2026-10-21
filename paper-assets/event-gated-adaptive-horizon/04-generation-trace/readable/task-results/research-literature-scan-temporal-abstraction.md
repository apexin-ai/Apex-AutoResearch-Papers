# research literature scan temporal abstraction

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan-temporal-abstraction_20260515T041851_result.json`
- **Structured JSON:** [`6c85be56a1c125025e2c.json`](../../sessions/6c/6c85be56a1c125025e2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新（72 → 76 篇）。

## 扫描总结

**核心结论：没有找到直接竞争者。** 无论文诊断 dt_embedding → delusional critic → stochastic collapse 这一因果链。CoRL 2025/2026 亦无相关投稿。

### 最相关的 5 篇新发现/确认论文：

1. **Palenicek 2025** "Diminishing Return of Value Expansion Methods" (RLC 2025) — 即使使用 oracle dynamics，更长 rollout horizon 的收益也递减。直接支持我们 "dt=1 imagination 足够" 的结论，因为瓶颈在 value estimation 而非 model accuracy。**强烈建议引用。**

2. **Nhu 2025 TAWM** (ICML 2025, 已在 map) — 最近的方法学重叠：显式 Δt conditioning，但用于 MPC 而非 imagination-based actor-critic，且结论相反（Δt conditioning 有益）。强化了我们贡献的独特性。

3. **Kim 2025 DEAS** (arXiv 2510.07730) — 独立证据：action sequences（temporal extension）在 actor-critic 中导致 value overestimation，通过 detached value learning 缓解。不同场景但相同因果模式。

4. **Li 2025 LS-Imagine** (ICLR 2025 Oral, 已在 map) — 扩展 Dreamer imagination horizon 的并发工作，但用 goal-conditioned jumps 而非 dt-embedding，可能避开了我们发现的 value overestimation。

5. **Luo 2025 VPL** (IJCAI 2025) — 自适应 pessimism 调节 overestimation，可作为我们 dt=1 方案的互补缓解手段。

### 领域趋势确认
学界正在收敛到**层级化**方案（THICK, Hieros, HWM, SPlaTES, MetaController）解决世界模型中的 temporal abstraction，回避 flat variable-dt 方法。我们的诊断论文解释了 **为什么** flat dt 方法失败，为这一经验趋势提供理论基础。

---
