# analysis action trajectory cpu

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_action_trajectory_cpu_20260518T135614_result.json`
- **Structured JSON:** [`9bb39201cbacf9d9fb15.json`](../../sessions/9b/9bb39201cbacf9d9fb15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**Bootstrap CI on Per-Head Effect Size:**
- Per-head d (instruction 24h): **0.0271** [0.0258, 0.0285]
- Per-head d (control 8h): **0.0514** [0.0478, 0.0551]
- Difference (ctrl - inst): **0.0244**, 95% CI [0.0203, 0.0281] — **显著排除 0**
- Task-level paired t-test: t=7.356, **p=0.0018**，所有 5 个 task 都是 ctrl > inst
- 结论：每个 control head 个体效应是 instruction head 的 ~1.9 倍。Instruction heads 通过 24 heads 的集体协调实现更大总效应 (d=0.651 vs 0.411)，而非个体强度。

**Temporal Coherence Proxy:**
- Per-dim CV：instruction ablation (1.30) < control (2.74) — instruction ablation 产生更一致的扰动
- Cross-task I²：instruction (0.87) > control (0.78) — instruction ablation 效应更依赖任务内容
- 符合 instruction heads 介导结构化、语言依赖计算的预期
- 注意：精确的 within-demo autocorrelation 需要 per-timestep 原始数据（未保存在 JSON 中）

结果保存在 `/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json`。

---
