# analysis bootstrap ci

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci_20260515T073104_result.json`
- **Structured JSON:** [`52ad6e3878872348a152.json`](../../sessions/52/52ad6e3878872348a152.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 设置 | macro-F1 | 95% CI |
|------|----------|--------|
| **6-gen LOGO** | 0.788 | [0.783, 0.793] |
| **5-gen LOGO** | 0.803 | [0.798, 0.809] |

**6-gen 每个 generator held-out：**

| Generator | F1 | 95% CI |
|-----------|-----|--------|
| pythia-1b | 0.828 | [0.818, 0.839] |
| pythia-2.8b | 0.817 | [0.805, 0.828] |
| qwen3-0.6b | 0.800 | [0.788, 0.811] |
| qwen3-1.7b | 0.793 | [0.781, 0.805] |
| olmo-2-1b | 0.786 | [0.774, 0.797] |
| qwen3-8b | 0.708 | [0.695, 0.722] |

结果已保存至 `/root/gen-depth-fingerprint/results/bootstrap_ci_results.json`。两个目标值验证通过（差异均 < 0.005）。19.7 秒完成 1000 次 bootstrap × 11 folds。

---
