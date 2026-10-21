# fix s3 constat itemcount bug

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_s3_constat_itemcount_bug_20260515T205253_result.json`
- **Structured JSON:** [`d9d65bbea39226b00571.json`](../../sessions/d9/d9d65bbea39226b00571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有已有产出格式正确。以下是完整报告。

---

## 1. Bug 根因分析

**文件**: `exp002/signals/s3_constat.py:49-51`（同时影响 `exp002/signal_constat.py`）

**根因**: `_load_per_item_correctness()` 返回 flat `list[bool]`，丢弃了 per_item 的 `index` 字段。随后在 line 49-51 做等长校验：

```python
n_items = len(orig_seeds[0])  # e.g. 1172 for arc_challenge
for vec in orig_seeds + para_seeds:
    if len(vec) != n_items:  # para has 697 → boom
        raise ValueError(f"Item count mismatch: expected {n_items}, got {len(vec)}")
```

**数据事实**: paraphrase eval 只包含成功 paraphrase 的 item 子集：

| benchmark | aligned (orig) | para_aligned | 覆盖率 |
|-----------|---------------|-------------|--------|
| mmlu | 14042 | 6596 | 47% |
| gsm8k | 1319 | 228 | 17% |
| arc_challenge | 1172 | 697 | 59% |

**修复**: 改 `_load_per_item_correctness` 返回 `dict[int, bool]`（`index -> correct`），用 set intersection 找共有 item，只对交集计算 gap score。两个文件均已修复并验证通过。

## 2. v6 已完成产出清单

| signal | benchmark | items | 状态 |
|--------|-----------|-------|------|
| s1_embedding | mmlu | 14042 | ✅ |
| s1_embedding | gsm8k | 1319 | ✅ |
| s1_embedding | arc_challenge | 1172 | ✅ |
| s2_minkpp | mmlu | 14042 | ✅ |
| s2_minkpp | gsm8k | 1319 | ✅ |
| s2_minkpp | arc_challenge | 1172 | ✅ |
| s3_constat | mmlu | — | ❌ bug（已修复，待重跑） |
| s3_constat | gsm8k | — | ❌ bug（已修复，待重跑） |
| s3_constat | arc_challenge | — | ❌ bug（已修复，待重跑） |
| s4_selfcritique | mmlu | — | ⏳ PID 630891 运行中（~15%, GPU 3） |
| s4_selfcritique | gsm8k | — | ❌ 未运行（被 s4/mmlu 阻塞） |
| s4_selfcritique | arc_challenge | — | ❌ 未运行 |

## 3. 需要重跑的 signal×benchmark

| signal | benchmark | 预估 items | 备注 |
|--------|-----------|-----------|------|
| s3_constat | mmlu | 6596 | 无需 GPU，纯计算 |
| s3_constat | gsm8k | 228 | 无需 GPU，纯计算 |
| s3_constat | arc_challenge | 697 | 无需 GPU，纯计算 |
| s4_selfcritique | mmlu | ~14042 | 当前 PID 630891 仍在跑，可等其完成 |
| s4_selfcritique | gsm8k | ~1319 | 需 GPU |
| s4_selfcritique | arc_challenge | ~1172 | 需 GPU |

**s3_constat 可立即重跑**（不占 GPU，只读 eval_results.json 做减法）。s4 中 mmlu 正在 GPU 3 上进行，剩余两个 benchmark 需等 mmlu 完成后继续，或调度到其他空闲 GPU。

---
