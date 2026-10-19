# ops p1 scan bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p1-scan-bjb1-18228_20260515T105458_result.json`
- **Structured JSON:** [`ec4ad7e2f95d38751f23.json`](../../sessions/ec/ec4ad7e2f95d38751f23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. obs-only-r3 — 已完成 (EXIT_CODE=0)

T6-T9 逐 task SR（从 T6 restart，10 rollouts each）：

| Task | 描述 | SR |
|------|------|----|
| T6 | next_to_the_cookie_box | **90%** (9/10) |
| T7 | on_the_stove | **0%** (0/10) |
| T8 | next_to_the_plate | **20%** (2/10) |
| T9 | on_the_wooden_cabinet | **0%** (0/10) |
| **Overall (T6-T9)** | | **27.5%** |

合并 parent T0-T5 的完整 10-task 结果：

| Task | SR |
|------|----|
| T0 | 90% |
| T1 | 100% |
| T2 | 0% |
| T3 | 40% |
| T4 | 10% |
| T5 | 0% |
| T6 | 90% |
| T7 | 0% |
| T8 | 20% |
| T9 | 0% |
| **Overall** | **35.0%** |

### 2. norm03-r2 (cuda:0) — 运行中，跑完 T3

已完成 T0-T3：T0=90%, T1=100%, T2=0%, T3=30%。正在跑 T4。

### 3. scalar-r2 (cuda:1) — 运行中，跑完 T7

从 T3 restart。已完成 T3-T7：T3=40%, T4=0%, T5=0%, T6=90%, T7=0%。正在跑 T8。

### 4. GPU 状态

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 23% | 4124 MiB | norm03-r2 运行中 |
| cuda:1 | 24% | 2005 MiB | scalar-r2 运行中 |
| cuda:2 | 0% | 1 MiB | **空闲** |
| cuda:3 | 0% | 1 MiB | **空闲** |

---
