# experiment mistral folio seed789 only

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mistral-folio-seed789-only_20260522T104840_result.json`
- **Structured JSON:** [`823bd52a917819c93bbe.json`](../../sessions/82/823bd52a917819c93bbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed=789 运行正常，已完成 2/204 题。

## 汇报

### 1. PID 575732 — KILLED OK

### 2. seed=789 新进程
- **PID: 576938**
- 日志：`/tmp/mistral_folio_seed789_nohup.log`
- 输出：`results/multi_seed/mistral_folio_seed789/`
- 当前进度：2/204 题，HTTP 200 正常

### 3. 已有 seeds 数据（Mistral-7B × FOLIO-204, K=12）

| Seed | 来源 | N | SC | SICA | Δ (SICA−SC) |
|------|------|---:|-----:|------:|------:|
| 123 | exp052 | 204 | 53.92% (110) | 57.35% (117) | **+3.43pp** |
| 456 | exp053 | 204 | 56.37% (115) | 55.88% (114) | **−0.49pp** |
| 789 | 运行中 | — | — | — | — |

**seed=42 FOLIO 数据不存在。** 搜索了所有可能路径（multi_seed、exp010、frontier、d135），均未找到。exp033 是无 seed（`--seed=None`）的早期 baseline，不等价于 seed=42。

### 4. 预计完成时间
- exp052 (seed=123) 耗时 4914s ≈ 82min
- exp053 (seed=456) 耗时 4847s ≈ 81min
- seed=789 启动于 18:49 → 预计 **~20:11 UTC** 完成（约 80 min）

---
