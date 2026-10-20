# analysis multiseed structural

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed-structural_20260514T183904_result.json`
- **Structured JSON:** [`37e6ed1402bb19958f5a.json`](../../sessions/37/37e6ed1402bb19958f5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Multi-seed Structural Baseline 验证结果 (seeds=42, 123, 456)

### 1. Non-NLP Baseline (In-domain SWE-Agent)

| Model | macro_f1 | std |
|-------|----------|-----|
| RF | **0.9951** | ±0.0000 |
| GB | **0.9951** | ±0.0000 |

三个 seed 结果完全一致，std=0。

### 2. Cross-Agent Structural (OH all non-abstain)

| Model | macro_f1 | std |
|-------|----------|-----|
| GB | **0.9678** | ±0.0015 |
| RF | 0.9116 | ±0.0190 |

GB 非常稳定 (±0.0015)。RF 有些波动 (±0.019) 但整体水平稳定。

### 3. Cross-Agent Structural (OH conf≥2)

| Model | macro_f1 | std |
|-------|----------|-----|
| RF | **0.9959** | ±0.0012 |
| GB | **0.9923** | ±0.0005 |

高置信度子集结果极其稳定。

### Reviewer 回复要点
- 所有 structural baseline 的 multi-seed std 极小（≤0.019），结果高度可复现
- In-domain RF/GB 的 0.9951 完全不受 seed 影响——说明数据本身的 structural signal 就是高度可分的
- Cross-agent GB 是最稳定的模型 (std≤0.0015)

结果已保存到 `/root/autodl-tmp/agent_progress_probe/artifacts/multiseed_structural_results.json`，实验 `multiseed-structural` 已注册为 DONE。

---
