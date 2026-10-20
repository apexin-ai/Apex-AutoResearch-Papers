# writing results skeleton

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_results-skeleton_20260514T054846_result.json`
- **Structured JSON:** [`a74a3d06f00eb0177569.json`](../../sessions/a7/a74a3d06f00eb0177569.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§5 Results 骨架已写入 `docs/paper/results.tex`（v12, provenance 15/15 coverage）。

结构：
- **§5.1 Experimental Overview** — 模型/数据/指标简要 recap，指向 §4
- **§5.2 Strategy-Dependent Severity (C1)** — aggregate II 对比表 + "emergent phase-strategy interaction" framing
- **§5.3 Phase-Modulated Amplification (C2)** — 8行主表（4 sparsity × 2 strategy），per-phase median II + gradient + CI；sub-exponential growth rate
- **§5.4 Phase-Strategy Crossover (C3)** — crossover 现象独立 subsection，heatmap 图引用，framing 用 attention redistribution 解释而非 "importance limitation"
- **§5.5 Cross-Model Replication (C5)** — Qwen 对比表 + placeholder 叙述段落，措辞用 "qualitatively reproduces"，明确声明同架构限制
- **§5.6 Statistical Validation** — bootstrap CI 表 + forest plot + permutation test，引用 Appendix

所有数值用 `\placeholder{exp_id: xxx, metric: yyy}` 标记，bf16 数据到手后可批量替换。保留了 `sec:crossover`、`tab:bootstrap` 等跨文件引用的 label。

---
