# code cross condition compare

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-condition-compare_20260516T140753_result.json`
- **Structured JSON:** [`2a0ea97dde176c6532d5.json`](../../sessions/2a/2a0ea97dde176c6532d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本正常工作，baseline 数据还没写 JSON 所以 pairwise 对比暂未触发。

---

## 当前状态汇总

### 1. compare_conditions.py 更新完成
- 修复了 `_get_metrics_list` 支持 `metrics_per_generation` 键
- 添加了 `compare_two_conditions()` 函数（逐代 metrics 对比 + Vendi 衰退速率对比）
- `main()` 中自动对比 3 对条件: single_reward vs no_curation, carr vs fixed_weight, carr vs single_reward

### 2. Quick Probe 03 (single_reward) — 全部 3 代完成

| Gen | quality | vendi | self_bleu | nn_dist | ppl |
|-----|---------|-------|-----------|---------|-----|
| 0 | 0.1123 | 107.54 | 0.0059 | 0.7088 | 10.60 |
| 1 | 0.1138 | 106.73 | 0.0091 | 0.7065 | 9.73 |
| 2 | 0.1109 | 107.25 | 0.0062 | 0.7054 | 9.72 |

**Vendi 变化: -0.28%**（3 代内几乎没有 collapse）。P1 FAIL — 5% 阈值远未达到。

### 3. Baseline no_curation — Gen 0 完成，Gen 1 生成中 (1296/2000)

| Gen | quality | vendi | self_bleu | nn_dist | ppl |
|-----|---------|-------|-----------|---------|-----|
| 0 | 0.1107 | 105.42 | 0.0044 | 0.7005 | 9.19 |

Gen 1 还需完成生成 → 训练 → eval，再做完 Gen 2，预计 40-60 分钟后出完整结果。

### 4. 初步 Gen 0 对比 (从日志)

| Metric | single_reward | no_curation | diff |
|--------|--------------|-------------|------|
| quality | 0.1123 | 0.1107 | +0.0016 |
| vendi | 107.54 | 105.42 | +2.12 |
| self_bleu | 0.0059 | 0.0044 | +0.0015 |
| nn_dist | 0.7088 | 0.7005 | +0.0083 |
| ppl | 10.60 | 9.19 | +1.41 |

Gen 0 时 single_reward 多样性略高于 no_curation（Vendi 107.5 vs 105.4），需要看后续代差异是否扩大。

要设置轮询等 baseline 完成吗？

---
