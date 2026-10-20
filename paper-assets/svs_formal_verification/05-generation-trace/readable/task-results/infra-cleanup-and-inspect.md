# infra cleanup and inspect

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cleanup_and_inspect_20260514T135624_result.json`
- **Structured JSON:** [`e4b47a05a09d735ed4f2.json`](../../sessions/e4/e4b47a05a09d735ed4f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

### 汇总

**Step 1:** 全部 rescorer/entailment 进程已 kill（65104/65325/65879/66105 + 残留 64853/64858），ALL_CLEAN。

**Step 2 原始输出：**
```
TOP KEYS: list len=46
PROBLEM KEYS: ['problem_id', 'gold_label', 'selected_answer', 'sc_answer', 'group_scores', 'correct_svs', 'correct_sc', 'chain_verifications']
PREMISES: NOT FOUND
GOLD: True
```

数据是 list（46 个 problem），每个 problem 没有 `chains`/`sampled_chains`/`premises` 字段，核心字段是 `chain_verifications`（脚本未展开此字段因为它不匹配 `chains` 的 key 名）。

**Step 3:** `46`

---
