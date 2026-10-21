# fix mvp2 grpo ced

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mvp2_grpo_ced_20260514T075819_result.json`
- **Structured JSON:** [`b70abd8d60432fa6bbe7.json`](../../sessions/b7/b70abd8d60432fa6bbe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。

## 修复摘要

**文件**: `/root/autodl-tmp/freige/training/grpo_trainer.py`

**改动 6 行**，2 处位置：

| 行号 | 函数 | 修复 |
|------|------|------|
| 98-100 | `f1_reward_fn` gold_set 构造 | `g.get("head", "").lower()` → `str(g.get("head") or "").lower()` |
| 199-201 | `CEDRewardWrapper.__call__` gold_map 构造 | 同上 |

**根因**：`dict.get(key, default)` 在 key 存在但值为 `None` 时返回 `None` 而非 default。`or ""` 确保 `None` 被降级为空字符串，`str()` 兜底非字符串类型。

**未改动**：`pred_set` 构造和 `verbalize` 调用已使用安全模式 `str(p.get(...) or "")`，`format_reward_fn` 不调用 `.lower()`——均无需修复。

---
