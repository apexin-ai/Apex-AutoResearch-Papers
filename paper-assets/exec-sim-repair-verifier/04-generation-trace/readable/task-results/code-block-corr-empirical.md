# code block corr empirical

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_block-corr-empirical_20260512T082738_result.json`
- **Structured JSON:** [`28ec6d9bec2cabc20c47.json`](../../sessions/28/28ec6d9bec2cabc20c47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果汇总：

## Block Correlation 验证结果

**结论：误差确实是 block-correlated，强有力支持 oracle 模拟的假设。**

| 指标 | 值 | 含义 |
|------|-----|------|
| **ICC** | 0.2329 | 同一 problem 内误差相关性显著 |
| **p-value** | 0.0000 (2000 次 permutation) | 远超显著性阈值 |
| **Design Effect (DEFF)** | 4.62 | 因 block correlation，有效样本量仅为名义的 1/4.6 |
| **All-correct problems** | 46 observed vs 12.8 expected (3.6x) | 模型对"简单"problem 倾向全对 |
| **Error rate std** | 0.1747 observed vs 0.0854 expected (2.05x) | 组间异质性远超 i.i.d. 预期 |

- 整体错误率 14.07%（266/1890），0 个 unparseable
- Shuffle baseline ICC ≈ 0.0002（基本为零），观测 ICC = 0.233 是 shuffle p99 (0.021) 的 11 倍
- 46/114 个 problem 全部预测正确，i.i.d. 下期望仅 12.8 个

---
