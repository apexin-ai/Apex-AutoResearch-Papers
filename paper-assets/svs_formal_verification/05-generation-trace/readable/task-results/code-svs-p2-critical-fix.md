# code svs p2 critical fix

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_svs_p2_critical_fix_20260514T045638_result.json`
- **Structured JSON:** [`4fe9643f4786f4689717.json`](../../sessions/4f/4fe9643f4786f4689717.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**修改总结：**

1. **`types.py`** — `SVSResult` 新增 `chain_verifications: list[ChainVerification]` 字段
2. **`scoring.py`** — `select_answer` 收集所有 `ChainVerification` 到 `all_chain_verifications`，传入 `SVSResult`
3. **`run_mvp.py`** — P2 逻辑从循环论证（SVS 答对/答错的 group composite score）改为：按 gold label 分组每条链的 IC score，做 independent t-test + Cohen's d + bootstrap 95% CI + Mann-Whitney U，加 per-problem paired t-test / Wilcoxon 分析

Fix 2（IC 分母用 `total_claims`）和 Fix 3（CCLC 谓词重叠诊断 + trivially SAT 检测）已由另一个 Worker 完成，无需重复修改。

---
