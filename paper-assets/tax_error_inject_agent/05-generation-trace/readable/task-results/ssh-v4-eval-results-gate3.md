# ssh v4 eval results gate3

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v4-eval-results-gate3_20260514T172952_result.json`
- **Structured JSON:** [`0d59788d68ff9679644e.json`](../../sessions/0d/0d59788d68ff9679644e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gate 3/4 判定结果：**BLOCKED**

### 三组成功率

| Model | Success Rate |
|-------|-------------|
| v4-vanilla | 29/47 = **61.7%** |
| v4-taxei | 29/47 = **61.7%** |
| v4-random | 31/47 = **66.0%** |

### Gate 判定

| Gate | 条件 | 结果 | 详情 |
|------|------|------|------|
| **3a** | TaxEI ≥ vanilla + 5pp | **FAIL** | diff = +0.0pp, McNemar p=1.000 (discordant=10) |
| **3b** | TaxEI > random | **FAIL** | diff = −4.3pp, McNemar p=0.754 (discordant=10) |
| **4** | Clean regression < 2pp | **PASS** | regression = −19.1pp (即 TaxEI 远超 baseline) |

### Per-task-type Breakdown (TaxEI vs Random vs Vanilla)

| Task Type | n | TaxEI | Random | Vanilla |
|-----------|---|-------|--------|---------|
| look_at_obj_in_light | 6 | **100%** | 100% | 83.3% |
| pick_and_place_simple | 8 | **62.5%** | 50.0% | 62.5% |
| pick_clean_then_place | 11 | 54.5% | 54.5% | 45.5% |
| pick_cool_then_place | 7 | 42.9% | **57.1%** | 57.1% |
| pick_heat_then_place | 8 | **87.5%** | 87.5% | 75.0% |
| pick_two_obj_and_place | 7 | 28.6% | **57.1%** | 57.1% |

### 关键发现

TaxEI 在 `pick_two_obj_and_place` 上严重退化（28.6% vs vanilla 57.1%），这完全抵消了它在 `look_at_obj_in_light` 和 `pick_heat` 上的微弱优势。TaxEI 和 vanilla 总分完全持平（61.7%），而 random injection 反而以 66.0% 领先。所有 McNemar 检验均无统计显著性。

---
