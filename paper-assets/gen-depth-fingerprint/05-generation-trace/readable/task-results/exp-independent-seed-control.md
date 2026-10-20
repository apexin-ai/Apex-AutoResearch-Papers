# exp independent seed control

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_independent-seed-control_20260517T223544_result.json`
- **Structured JSON:** [`faddc2c3122337795f4b.json`](../../sessions/fa/faddc2c3122337795f4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验全部完成。结果汇报：

## exp_051_independent_seed 结果

| Setting | Train→Test | Binary F1 | 95% CI |
|---------|-----------|-----------|--------|
| Independent seeds | Pythia→OLMo | **0.6945** | [0.6727, 0.7167] |
| Independent seeds | OLMo→Pythia | **0.6660** | [0.6429, 0.6893] |
| Independent seeds (avg) | bidirectional | **0.6803** | |
| Shared seeds (ref) | LOGO avg | 0.694 | [0.688, 0.700] |

**Delta vs shared-seed: -0.014**

**结论：Topic fingerprint leakage 被排除。** 独立 seed 集（两个模型完全不共享 Wikipedia 文章）下的 cross-generator binary F1 (0.680) 与 shared-seed LOGO baseline (0.694) 高度可比（差异仅 -1.4%，在 CI 范围内）。这证明 classifier 学到的是 generative depth 信号，而非 topic identity。

---
