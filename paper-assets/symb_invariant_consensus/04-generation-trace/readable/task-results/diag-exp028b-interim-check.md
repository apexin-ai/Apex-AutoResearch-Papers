# diag exp028b interim check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp028b-interim-check_20260518T230802_result.json`
- **Structured JSON:** [`d787676140496317a23e.json`](../../sessions/d7/d787676140496317a23e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已拿到。汇总如下：

---

## exp-028b (Qwen3-14B thinking mode) — Interim Report

### 进度
- **60/204** (正在跑 folio_59)，59 个已完成并写入 results JSON
- 已跑 2.5h，avg 152s/problem
- **ETA: ~6.1h** (预计约 13:10 UTC 完成)

### Interim Metrics (59/204)

| Metric | SC (K=12) | SICA | Delta |
|--------|-----------|------|-------|
| **Overall** | **83.05%** (49/59) | **86.44%** (51/59) | **+3.39 pp** |

### Per Answer Type

| GT | n | SC | SICA | Delta | Overrides |
|----|---|----|------|-------|-----------|
| True | 21 | 76.2% | 81.0% | +4.8 pp | 1 |
| False | 16 | 75.0% | 81.2% | +6.2 pp | 1 |
| Unknown | 23 | 95.7% | 95.7% | +0.0 pp | 0 |

### Override Analysis
- Total overrides: **2** (100% precision)
- `folio_19`: GT=True, SC=Unknown → SICA=True (**GAIN**)
- `folio_20`: GT=False, SC=Unknown → SICA=False (**GAIN**)
- Harmful overrides: **0**
- Net gain: **+2 problems**

### 其他指标
- Extraction rate: 91.1%
- Contradiction rate: 1.1% (11/59 problems had contradictions)
- Avg unique constraints per problem: ~25.7

---

## exp-051 (Mistral K sensitivity)

- **K=4 正在跑**：32/204，avg 11.7s/problem，ETA ~34 min
- 使用 localhost:8000 (与 exp-028b 的 localhost:8003 不冲突)
- K=8, K=16, K=20 目录已存在（可能已完成或待跑）

---

### 关键观察

1. SICA delta **+3.39 pp** 在 Qwen3-14B thinking mode 上表现稳健，override precision 100% (2/2)
2. 增益主要来自 True/False 类型（各 +4.8/+6.2 pp），Unknown 类型 SC 已经很强 (95.7%)，SICA 无额外增益
3. 两次 override 都是 SC 投出 Unknown 但 SICA 通过约束纠正为正确答案，符合预期机制
4. 152s/problem 的速度偏慢（thinking mode 的 trace 生成耗时较长），全部跑完约需 8.6h 总时间

---
