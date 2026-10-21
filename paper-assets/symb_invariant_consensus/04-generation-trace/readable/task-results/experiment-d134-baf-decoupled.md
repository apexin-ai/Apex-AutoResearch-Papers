# experiment d134 baf decoupled

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d134-baf-decoupled_20260521T084208_result.json`
- **Structured JSON:** [`0bcb8f38c9314334aee0.json`](../../sessions/0b/0bcb8f38c9314334aee0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

**exp-d134-baf-decoupled 结论**

| 条件 | SICA Acc | BR mean | BR median | 截断比例 |
|------|----------|---------|-----------|---------|
| Full trace | 59.31% | 2.787 | 2.158 | 0% |
| Trunc-conservative | 53.92% | 2.490 | 1.620 | 4.3% |
| Trunc-standard | 54.41% | 2.655 | 1.789 | 18.9% |
| Trunc-aggressive | 53.92% | 2.255 | 1.909 | 35.3% |

**关键发现：**
- **BR 无显著降低**：所有三种截断策略的 Wilcoxon signed-rank test 均不显著（p=0.12/0.55/0.26），配对比较中 BR 下降/上升的题目数近乎对半（如 aggressive 27↓ vs 25↑）
- **准确率显著下降**：截断后 SICA 准确率下降约 5pp（McNemar p<0.013），尤其 conservative 策略有 11 题从对变错、0 题从错变对
- **结论**：简单截断 CoT 答案句再做约束提取不能有效缓解 SCB——confirmation bias 已渗透到推理过程中间步骤，而非仅存在于最终结论句。截断反而丢失了有价值的约束信息，导致准确率净损失

结果写入：
- 服务器：`/root/symb_invariant_consensus/results/exp_d134_baf_decoupled/results.json`
- 本地：`artifacts/baf_decoupled_results.json`

---
