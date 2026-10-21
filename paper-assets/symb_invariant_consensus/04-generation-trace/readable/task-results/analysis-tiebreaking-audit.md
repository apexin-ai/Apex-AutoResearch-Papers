# analysis tiebreaking audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tiebreaking-audit_20260523T184453_result.json`
- **Structured JSON:** [`9a6204cf0cba1fd00e25.json`](../../sessions/9a/9a6204cf0cba1fd00e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 SICA "mismatch" 都是 frequency tiebreaking（代码的实际行为），不是 bug。

## 审计结论

### 1. 当前代码的 tiebreaking 方法

| 方法 | 实现位置 | Tiebreaking 逻辑 |
|------|----------|------------------|
| **SC** | `baselines/self_consistency.py:20` | `max(sorted(groups.keys()), key=...)` → **alphabetical** ✓ |
| **SICA** | `sica/scorer.py:82-98` | score → frequency → alphabetical（三级） |

### 2. 每个 seed 实验的 SC tiebreaking 验证

**全部 23 个实验均使用 alphabetical tiebreaking ✓**

| 实验组 | Seeds | Tie 数 | 验证结果 |
|--------|-------|--------|----------|
| Mistral PW | 42/123/456/789 | 34/29/21/30 | 全部 ALPHABETICAL ✓ |
| LLaMA PW | 42/123/456/789 | 10/32/8/36 | 全部 ALPHABETICAL ✓ |
| Qwen2.5 PW | 123/456/789 | 18/19/12 | 全部 ALPHABETICAL ✓ |
| Qwen3 PW | 123/456/789 | 0/0/0 | 无 tie，N/A ✓ |
| Mistral FOLIO | 123/456/789 | 11/2/10 | 全部 ALPHABETICAL ✓ |
| LLaMA FOLIO | 123/456/789 | 14/4/7 | 全部 ALPHABETICAL ✓ |
| Qwen2.5 FOLIO | 123/456/789 | 2/8/5 | 全部 ALPHABETICAL ✓ |

### 3. SICA tiebreaking

SICA 的 verify 脚本报了 30 个 "MISMATCH"，但经逐条核实，**全部是 frequency tiebreaking 导致的预期行为**（score 相同时按出现频率选，再按 alphabetical 兜底），与代码 `scorer.py:94-97` 完全一致。无真实 mismatch。

### 4. 结论

- **SC tiebreaking：无需修复。** 所有 seed（含 seed42）的存储结果都已使用 alphabetical tiebreaking。
- **SICA tiebreaking：使用 score→frequency→alphabetical 三级策略，**不是纯 alphabetical。这是设计选择，如果论文要求 SICA 也用纯 alphabetical tiebreaking（仅在 score tie 时），需修改 `sica/scorer.py:94-97` 并重算受影响的 ~30 个问题。影响预计极小（tie case 占比 <1%，且大多数 frequency 和 alphabetical 结果一致）。

---
