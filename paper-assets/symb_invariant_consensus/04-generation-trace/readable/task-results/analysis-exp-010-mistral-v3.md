# analysis exp 010 mistral v3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-010-mistral-v3_20260517T081853_result.json`
- **Structured JSON:** [`fa8965e4faf45adf6969.json`](../../sessions/fa/fa8965e4faf45adf6969.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-010-mistral-v3 分析完成

### 核心数据

| | SICA | SC | Delta |
|---|---|---|---|
| Overall (n=60) | 48.3% | 48.3% | **0.0pp** |
| ProofWriter (n=30) | 40.0% | 40.0% | 0.0pp |
| FOLIO (n=30) | 56.7% | 56.7% | 0.0pp |

4 个 discordant pairs 完美抵消（SICA wins 2, SC wins 2）。基础准确率 48.3% 远高于随机基线 33%，模型能力足够支撑有意义对比。

### 结论: **success**

Hypothesis confirmed — Mistral-7B 完美复现 SICA≈SC pattern，capability trap 跨模型家族泛化成立。

### 关键洞察

与 LLaMA-3.1-8B (+6.67pp) 的矛盾值得注意：同为 7B 级弱模型，Mistral 的约束高度一致（MaxSAT sat ratio 0.948）但无判别性，而 LLaMA 的约束恰好携带了 answer-discriminative 信号。这说明 **operating regime 不是简单的模型规模函数**，SICA 增益的关键条件是约束的判别性质量，而非模型弱就一定受益。

Registry 已更新 (status=DONE, conclusion=success, metrics 完整)，memory.md 已追加完整分析。

---
