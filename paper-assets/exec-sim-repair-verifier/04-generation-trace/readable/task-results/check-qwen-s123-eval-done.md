# check qwen s123 eval done

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-s123-eval-done_20260522T111847_result.json`
- **Structured JSON:** [`ece4d6b9286bb88f089a.json`](../../sessions/ec/ece4d6b9286bb88f089a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。无 cron 需要删除。

## 结果汇总

| 指标 | 值 |
|------|-----|
| **accuracy** | **67.33%** |
| majority baseline | 72.96% |
| gap vs majority | **-5.62pp** |
| f1_macro | 55.67 |
| f1_fail / f1_pass | 32.94 / 78.41 |
| unparseable_count | 6257 / 9784 (**63.95%**) |
| checkpoint | step-6633 (final) |

**Conclusion: negative.** Qwen3-8B CWM s123 未超过 majority baseline，且 unparseable rate 高达 64%——模型基本没学会生成可解析的 CWM 格式输出。accuracy 67.33% 低于 majority baseline 72.96% 约 5.6pp，说明大量 unparseable 样本被 fallback 为 pass 后仍无法弥补。

对论文 Table 3 的影响：这个 seed 的 Qwen CWM 结果不理想，与 DeepSeek CWM 的 cross-model generalization story 可能需要重新审视。

---
