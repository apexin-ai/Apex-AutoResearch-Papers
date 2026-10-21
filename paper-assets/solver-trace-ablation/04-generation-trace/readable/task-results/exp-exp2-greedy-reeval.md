# exp exp2 greedy reeval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp2-greedy-reeval_20260514T220504_result.json`
- **Structured JSON:** [`f6b147727c5f95c8c4ad.json`](../../sessions/f6/f6b147727c5f95c8c4ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**EXP-2 已完成。** 注册表 `plan001-exec-only-s43-r4` 已包含 greedy 和 sampling 对比结果，checkpoint 已按 C003 删除。

汇总：

| 指标 | Greedy (T=0) | Sampling (T=0.7) | Δ |
|------|-------------|-------------------|---|
| PR | 0.13 | 0.14 | -0.01 |
| ISR* | 0 | 0 | 0 |
| H1% | 100% (13/13) | 100% (14/14) | — |
| H7% | 0% | 0% | — |
| Genuine% | 0% | 0% | — |
| Mean components (proved) | 18.92 | 18.5 | +0.42 |

结论：**s43 collapse is decoding-invariant**。两种解码策略下 ISR*=0、H1=100%、genuine=0%，PR 仅差 1pp。~85% 的输入触达 max_new_tokens（长重复 clause 输出），~15% 能解析的样本包含 conclusion verbatim 在 14-30 premises 中（n_necessary=0 → ISR=0）。

注册表注释中提到的报告文件 `exp2_s43_greedy_vs_sample.txt` 不存在于服务器上（可能未实际写入）。如果需要生成该报告文件，可以从注册表数据生成。否则无需进一步操作。

---
