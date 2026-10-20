# code qwen3 tiebreaking fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen3-tiebreaking-fix_20260524T112203_result.json`
- **Structured JSON:** [`3c1af86f7f5ffafb1e3c.json`](../../sessions/3c/3c1af86f7f5ffafb1e3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## Part 1: Tiebreaking 代码对比结论

`run_full_mvp.py` 和 `run_cross_dataset_replication.py` **调用同一个** `SelfConsistency().run()` 方法（`baselines/self_consistency.py`）。当前实现用 `max(sorted(groups.keys()), key=...)` — 即 **alphabetical tiebreaking**。

差异不在两个脚本之间，而是在 `SelfConsistency` 类的**修改前后**。旧版使用插入序（非确定性），后被修复为 alphabetical。`_fix_tiebreaking.py` 和 `sc_tiebreak_revalidation.py` 的存在佐证了这一修复历史。

## Part 2: 其他模型多种子验证

| 模型 | 数据集 | Seeds | Tiebreaking | 状态 |
|------|--------|-------|-------------|------|
| Mistral-7B | PW | 42/123/456/789 | ALPHABETICAL | 全部正确 |
| LLaMA-8B | PW | 42/123/456/789 | ALPHABETICAL | 全部正确（seed42 n=223, seed456 n=184 不完整但 tiebreaking 正确）|
| Qwen2.5-14B | PW | 123/456/789 | ALPHABETICAL | 全部正确 |
| **Qwen3-14B** | PW | 123/456/789 | ALPHABETICAL | **全部正确，0 mismatch** |
| **Qwen3-14B** | PW | 42 (exp033) | **MISMATCH** | **9 个 tie 选错** |

## Part 3: 修正脚本 + 试运行结果

`/root/symb_invariant_consensus/fix_qwen3_tiebreaking.py` 已就绪。

**exp033 (Qwen3 seed42) 试运行结果**：
- 9 个 question 的 SC answer 变化（全部是 6:6 tie，旧版选了 Unknown，alphabetical 选 False/True）
- SC: 85.00% → **85.83%** (+0.83pp)
- SICA: 85.67%（不变）
- Δ(SICA-SC): +0.67pp → **-0.17pp**
- 7 个 GAINED, 2 个 LOST

**Qwen3 多种子 (seed123/456/789): 0 个变化，无需修正。**

核心结论：Reviewer 的 concern 只影响 exp033 (seed42)。三个多种子实验在 `SelfConsistency` 修复后运行，已经是 alphabetical。

---
