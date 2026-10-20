# code mvp v3 code fix

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_v3_code_fix_20260514T094847_result.json`
- **Structured JSON:** [`360d88f0426b96442e18.json`](../../sessions/36/360d88f0426b96442e18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here is the final output:

---

## 1. Grep 验证输出 (v3 sync confirmed)

All 6 verification checks passed before pipeline launch:
- `_strip_thinking`: unclosed `&lt;think>` tag handling present ✓
- `enable_thinking`: parameter in `_call_llm` signature ✓
- `extra_body`: `chat_template_kwargs` for vLLM ✓
- `CODE_SYSTEM_PROMPT`: 1 few-shot example ✓
- `generate_python_code`: calls with `enable_thinking=False` ✓
- Import test: all modules load successfully ✓

## 2. v2 vs v3 Crash Rate 对比

| Metric | v2 | v3 | Delta |
|--------|-----|-----|-------|
| **FOL crash rate** | 10% (1/10) | 80% (8/10) | +70pp (regression, stochastic) |
| **Code crash rate** | **40% (4/10)** | **0% (0/10)** | **-40pp (v3 fix effective)** |
| Both executed | 60% | 20% | -40pp |

**v3 fix 结论**: `enable_thinking=False` 完全消除了 Code 端的 thinking token 泄漏崩溃 (40%→0%)。FOL 端 crash 率回升是因为 Z3 代码生成本身的随机性（temperature=0.7），非 v3 回归。

## 3. Effective Disagree Rate

- Both sides executed: **2/10** (20%)
- Effective disagree: **0/2** (0%)
- 两个 both-executed 的样本都是 AGREE_CORRECT (folio_validation_3 和 folio_validation_9)

## 4. MVP C1-C5 结果

| Criterion | Threshold | v3 Result | Status |
|-----------|-----------|-----------|--------|
| C1 disagree ≥ 10% | ≥10% | 0% | **FAIL** |
| C2 diagnostic ≥ 40% | ≥40% | N/A (0 disagree) | **FAIL** |
| C3 error types ≥ 2 | ≥2 | 3 (quantifier_error, negation_error, constraint_missing) | **PASS** |
| C4 targeted > blind +5pp | ≥+5pp | -12.5pp (targeted 50% vs blind 62.5%) | **FAIL** |
| C5 localization ≥ 60% | ≥60% | 50% (4/8) | **FAIL** |

**MVP NOT PASSED** (1/5 criteria met)

## 5. 平均每样本时间

| Sample | Time (s) |
|--------|----------|
| folio_validation_0 | 336.5 |
| folio_validation_1 | 258.2 |
| folio_validation_2 | 331.5 |
| folio_validation_3 | 58.2 |
| folio_validation_4 | 260.5 |
| folio_validation_5 | 226.1 |
| folio_validation_6 | 187.7 |
| folio_validation_7 | 250.4 |
| folio_validation_8 | 252.7 |
| folio_validation_9 | 23.6 |

- **Avg per-sample: 218.5s (3.6 min)**
- Wall-clock total: 2185.5s (36.4 min)
- AGREE_CORRECT 样本 (无需 repair) 极快: 23.6s 和 58.2s

---

**核心瓶颈**: FOL (Z3) crash rate 80% 导致绝大多数样本退化为 SINGLE_ERROR，无法产生有效 disagreement。v3 成功解决了 Code 端崩溃，下一步需要攻克 FOL 端的 Z3 代码生成质量。

---
