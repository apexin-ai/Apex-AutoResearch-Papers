# research seed dependent value overestimation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed-dependent-value-overestimation_20260514T142751_result.json`
- **Structured JSON:** [`d2acd60fa81bb8385b19.json`](../../sessions/d2/d2acd60fa81bb8385b19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已追加 5 篇论文到 `literature_map.yaml`（总数 28→33）。按三个搜索角度的覆盖情况：

**角度 1 — Seed/initialization sensitivity in value overestimation**
- **Henderson et al. 2018** (AAAI): 证明相同超参下不同 seed 产生统计显著的性能分布差异
- **Hussing et al. 2024** (RLC): value divergence 的发生与 optimizer momentum 和初始化相关，onset timing 不固定

**角度 2 — Dreamer-family training instability**
- **Qiao et al. 2023** (ECAI 2024): 直接在 DreamerV2 上验证 primacy bias，发现 world model 的 primacy bias 比 agent 的更关键 — 最高相关度
- **Barkley & Fridovich-Keil 2024** (ICML 2025): synthetic rollout 在不同环境下不一致地降低性能，overestimation 是贡献因素之一

**角度 3 — Value overestimation as delayed failure**
- **Nikishin et al. 2022** (ICML): primacy bias 导致 initially fine → eventually pathological 的渐进退化模式，collapse timing seed-dependent

**Gap 分析**: 搜索确认 "seed-dependent value overestimation in MBRL" 没有被任何论文作为核心主题研究。现有工作分别讨论了 seed variance（Henderson）、delayed collapse via primacy bias（Nikishin, Qiao）、imagination-induced overestimation（Barkley），但没有论文将这三者关联起来解释 "为什么同一配置下某些 seed collapse 而其他 seed 不会"。这是一个 novelty signal — 我们的实验（seed 0 稳定 vs seed 2 borderline collapse）是对这一现象的直接观测。

---
