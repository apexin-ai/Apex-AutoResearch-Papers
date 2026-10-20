# code fix token ratio mixing

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_token_ratio_mixing_20260516T033427_result.json`
- **Structured JSON:** [`552b72426b4f972572f4.json`](../../sessions/55/552b72426b4f972572f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。变更摘要：

**`mix_data`** — 不再按行数子采样 real data，改为：计算 synthetic 总 token 数 → 由 `synthetic_ratio` 公式推导 real 的 target token 数 → 随机打乱 real 行后贪心选取直到 token 预算满。

**`split_real_pool`** — 不再按行数等分，改为：统计每行 token 数 → 累积到 `target_per_gen` 时切分，保证每代 real data 的 token 总量近似相等。

**`main()`** — 在 pipeline 启动时加载一次 Pythia tokenizer，传给两个函数复用。

验证结果：ratio=0.5 实际 0.4991，ratio=0.8 实际 0.7989，误差 <0.2%。

---
