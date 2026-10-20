# analysis exp 077 completion check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-077-completion-check_20260519T213554_result.json`
- **Structured JSON:** [`416a7ef3c4a0896dcc79.json`](../../sessions/41/416a7ef3c4a0896dcc79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## exp-077 结果汇总

**状态**: 完成 (204/204)，conclusion = **negative**

| 方法 | Fleiss' κ | Effective K | 名义 K |
|------|----------|-------------|--------|
| Self-Consistency | **0.4384** | **2.02** | 10 |
| LLM-Debate | **0.1549** | **4.44** | 12 |
| Diverse-Prompt | **0.4030** | **2.21** | 12 |

**关键发现**:
- SC 和 Diverse-Prompt 表现相似：κ~0.4（moderate agreement），Eff-K~2，确认 independence bottleneck — 名义上 10-12 个 rater 实际只等价于 2 个独立 rater
- **Debate 是异类**：κ=0.15（slight agreement），Eff-K=4.44。但这不代表 Debate 的独立性更好——低 κ 反映的是 debate 过程中的 disagreement amplification，而非真正的独立推理
- 假设"三种方式均 κ>0.4"被 **falsified**，independence bottleneck 不是跨所有聚合方式的统一通病

---
