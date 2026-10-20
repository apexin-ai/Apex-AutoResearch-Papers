# code detrending utility

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_detrending_utility_20260514T213045_result.json`
- **Structured JSON:** [`fdfea49d73bdaf1a5e15.json`](../../sessions/fd/fdfea49d73bdaf1a5e15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两种方法都成功运行。

## 报告

### 工具状态
`analysis/detrending_utils.py` 已部署到服务器，两种 detrending 方法均通过 dry-run。

### Dry-run 结果摘要（rep_42）

**First-differencing:**

| Canary | Downstream | Raw lag | DT lag | DT \|r\| | Lag preserved |
|--------|-----------|---------|--------|---------|---------------|
| token_entropy | distinct_1 | -1 | **-1** | 0.995 | YES |
| token_entropy | distinct_2 | -1 | **-1** | 0.978 | YES |
| ece | distinct_1 | -2 | **-2** | 0.986 | YES |
| token_entropy | perplexity | -5 | 1 | 0.889 | NO |
| ece | perplexity | 5 | 1 | 0.873 | NO |

**token_entropy→distinct_1 的 detrended lag 仍为 -1**，|r|=0.995，关系非常稳健。token_entropy→distinct_2 同样保持 lag=-1。

perplexity 相关的 pair 在 detrending 后 lag 不稳定——raw 时 lag=-5 或 +5 打到边界，说明 raw 结果本身就不可靠（共同单调趋势驱动），detrending 后回到短 lag 范围，这正是预期行为。

### Edge cases

1. **HP filter 在 T=11 下的行为**：λ=6.25 时 HP 结果和 first_diff 大致一致，但端点效应显著。HP cycle 对 ece→distinct_1 的 lag 从 -2 变为 -1（first_diff 保持 -2）。建议正式分析时对 λ∈{1, 3, 6.25, 10} 做 robustness check。

2. **Raw lag 打边界（±5）**：token_entropy→perplexity 和 ece→perplexity 的 raw peak lag 在 ±5 边界，这是共同单调趋势的典型伪相关信号。Detrending 后 lag 回到合理范围，验证了 detrending 的必要性。

3. **First_diff 后 T=10**：max_lag 被 cap 到 5（=10//2），极端 lag 只有 5 个 overlap 点，相关系数不稳定。α-sweep 数据如果代数更多会更可靠。

---
