# code wikievents flatten redryrun

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_flatten_redryrun_20260517T153849_result.json`
- **Structured JSON:** [`bdf783a145a1fd75e4c3.json`](../../sessions/bd/bdf783a145a1fd75e4c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

---

## 完成情况

### Step 1: 碰撞率验证 ✓
- 全名 baseline: 96.1% → **最终方案 3.9%** (< 10% 目标)
- 策略: leaf (非 Unspecified) + Mid.Unspecified + 6 个手动 override
- 残余碰撞: 仅 `Infection.Unspecified` / `Injury.Unspecified` 共享首 token "In"

### Step 2: 更新文件 ✓
- `ontology_constraints_wikievents.json`: event_types 和 event_constraints key 改为短名，保留 `event_type_mapping` (full→short)
- `run_constrained_extraction.py`: load_wikievents_data 加载时映射 gold event types
- prompt (无需改): `event_extraction.py` 已从 spec 读取 event_types
- violation_checker (无需改): 直接读 ontology JSON 中的短名

### Step 3: Parse Fix ✓
- WikiEvents default `max_new_tokens` 改为 4096

### Step 4: Dry Run 结果

| Metric | Unconstrained | Constrained |
|--------|:---:|:---:|
| Parse success | 90% | **100%** |
| EV | 38.5% | **0%** |
| RoV | 59.8% | 55.5% |
| AC | 0% | 12.2% |

### 门控判断: **CONDITIONAL PASS**

- ✓ EV → 0%, Parse → 100%
- ✗ RoV 未大幅下降 (55.5% vs 59.8%)

**原因**: XGrammar `accept_token` assertion failure 导致 fallback 到 grammar-only 模式，semantic role masking 未生效。这是 constraint processor 状态同步问题，非 flatten 引起。

**建议**: 不宜直接上全量。下一步需修复 semantic masking 与 XGrammar 的状态同步问题。

---
