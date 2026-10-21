# analysis bootstrap cis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-cis_20260516T132633_result.json`
- **Structured JSON:** [`8c6b9eaad103ac532aae.json`](../../sessions/8c/8c6b9eaad103ac532aae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `/root/autodl-tmp/event-gated-adaptive-horizon/analysis/bootstrap_cis.json`。

**核心发现：**

**1. NVE — exp_008d (CIVO trigger)**
- 3 个 checkpoint (35K-55K)，NVE 从 1.71 上升到 4.13
- Bootstrap CI: **mean=2.64 [1.71, 4.13]** (n=3，CI 宽，覆盖全部数据点)
- 说明 CIVO trigger 的 value overestimation 是 baseline 的 1.7-4.1 倍

**2. NVE — exp_018 (Full-SGS)**
- 所有 11/11 步的 metrics 与 baseline_s1 完全一致（NVE=1.0），exp_018 的 metrics.jsonl 包含的是 baseline 的原始日志数据

**3. Seed Variability (baseline_s1 seed1 vs exp_009d_s0 seed0)**
- 全程 mean diff = **183.8 [136.2, 234.0]**（seed1 显著高于 seed0）
- 最后 10 个 checkpoint (415K-505K) 收窄到 **21.6 [11.5, 31.4]**，差距仍显著但幅度小很多

**4. Cheetah Baseline (exp_010a)**
- ve_ratio 全程: **0.613 [0.555, 0.664]**
- 最后 10 checkpoint: **0.722 [0.705, 0.742]** — value 略低估 eval_return
- eval_return 最后 10 checkpoint: **803.2 [779.0, 826.3]**

---
