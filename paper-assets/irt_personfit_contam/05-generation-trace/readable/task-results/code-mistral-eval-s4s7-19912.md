# code mistral eval s4s7 19912

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral-eval-s4s7-19912_20260521T145553_result.json`
- **Structured JSON:** [`69f1f6be9e3b0841fb10.json`](../../sessions/69/69f1f6be9e3b0841fb10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 seed 全部完成。汇总结果：

## Mistral Clean s4-s7 Eval 结果

| Seed | Accuracy | lz* | theta_mle | n_items |
|------|----------|-----|-----------|---------|
| clean_s4 | 0.5105 | 3.9558 | -1.1693 | 14042 |
| clean_s5 | 0.5231 | 4.4910 | -1.1000 | 14042 |
| clean_s6 | 0.5128 | 5.5030 | -1.1405 | 14042 |
| clean_s7 | 0.5284 | 5.8982 | -1.0755 | 14042 |

所有 clean condition 的 seen_items=0（符合预期），accuracy 在 0.51-0.53 范围内，lz* 在 3.96-5.90 范围内（正值表示 response pattern 比 IRT 模型预期更一致）。

---
