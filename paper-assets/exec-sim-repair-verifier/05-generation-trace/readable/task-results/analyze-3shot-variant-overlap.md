# analyze 3shot variant overlap

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_3shot-variant-overlap_20260519T063438_result.json`
- **Structured JSON:** [`d5d9dc7622a55ddeca65.json`](../../sessions/d5/d5d9dc7622a55ddeca65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰：

## Ground Truth Distribution
resolved: 26/48, unresolved: 22/48

## Qwen3-8B correct (22 variants): 全部是 gt=unresolved
## DeepSeek correct (22 variants): 完全相同的 22 个 gt=unresolved variants

## Overlap Analysis
- intersection: 22 variants
- union: 22 variants
- **Jaccard: 22/22 = 1.0000 (完全重叠)**
- only Qwen3: 0
- only DeepSeek: 0

## Pattern Interpretation

两个模型正确预测的 22 个 variant **完全相同**，且全部是 gt=unresolved 的 variant。核心发现：

1. **两个模型在 variant level 上都是 0 TP、22 TN、0 FN、26 FP**。没有任何一个 gt=resolved variant 被成功预测为 resolved（因为 AND rule 要求所有 test 都预测 PASS，但两个模型都做不到）。
2. **22/48 = 45.83% 完全是因为所有 22 个 unresolved variant 恰好被判对了（TN）**，没有任何真正的 "resolve detection" 能力。
3. 两个模型 variant accuracy 相同不是巧合，而是结构性必然：AND rule 下，只要模型对任何一个 test 预测 FAIL，整个 variant 就被判 unresolved。两个模型虽然 per-test 行为差异很大（Qwen3 pass rate 67%, DeepSeek 31%），但都无法对任何 resolved variant 做到 100% PASS，所以所有 variant 都被预测为 unresolved，正确的恰好就是那 22 个 gt=unresolved。

**论文写法建议**：这个数字不应被呈现为"两个模型都达到了 45.83% variant accuracy"，而应点明 **3-shot baseline 在 variant level 上完全没有 resolve 检测能力（0% recall on resolved），45.83% 等于 unresolved 的 base rate（22/48）**。这反而强化了论文的 motivation：few-shot prompting 不足以完成这个任务。

---
