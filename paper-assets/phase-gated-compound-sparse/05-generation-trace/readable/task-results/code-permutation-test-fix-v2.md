# code permutation test fix v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_permutation-test-fix-v2_20260514T065952_result.json`
- **Structured JSON:** [`39593effda6afadf9d91.json`](../../sessions/39/39593effda6afadf9d91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bf16 rand s030 目录为空，所以 random 正确地回退到了 `v6_random_s030_r3`（fp16 fallback）。importance 使用了 bf16 数据。这符合预期的优先级逻辑。

**验证结果**：

| 修复项 | 验证 |
|--------|------|
| Bug 1: bf16 优先 | imp 使用 `bf16_ds_imp_s030`，bf16 无数据时回退 v6 |
| Bug 2: EPS=0.01 | 5 个 problem 被 EPS 过滤（ratio n=44 vs diff n=49） |
| n_filtered_eps | 输出中已报告 `eps_filtered=5` |
| difference statistic | p=0.0001 (median/mean)，与 ratio 统计量一致 |
| ratio statistic | 74.1x, p=0.0003 (***) |
| CLI --sparsity-levels | 支持 `0.30` 格式，正确转换为 `s030` |

---
