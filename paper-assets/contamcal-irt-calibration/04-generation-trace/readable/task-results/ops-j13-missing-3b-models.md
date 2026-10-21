# ops j13 missing 3b models

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_j13_missing_3b_models_20260517T085442_result.json`
- **Structured JSON:** [`58eb9f7b277a6b593ca0.json`](../../sessions/58/58eb9f7b277a6b593ca0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完毕。以下是结果：

## MODEL_WHITELIST（硬编码列表）

脚本 `run_mmlu_domain_gamma_no05b.py:68-82` 定义的 3B 模型只有 5 个：
```
Qwen2.5-3B_d005_s123
Qwen2.5-3B_d025_s123
Qwen2.5-3B_d025_v3_s42
Qwen2.5-3B_d100_a32_s123
Qwen2.5-3B_d100_a32_s42
```

缺失的 3 个模型全部**未列入白名单**。以下是逐个分析：

---

## 1. Qwen2.5-3B_d000_s42（a32 版本：`d000_a32_s42`）

| 步骤 | 状态 | 备注 |
|------|------|------|
| Signals | ✓ 完整 | `exp002/signals/Qwen2.5-3B_d000_a32_s42`（s1+s2+s4+merged） |
| RRF | ✓ | key = `Qwen2.5-3B_d000_a32_s42` |
| Eval | ✓ | dir = `Qwen2.5-3B_d000_s42_a32_aligned` |
| Whitelist | ✗ | 未列入 |
| **额外问题** | 命名冲突 | eval strip 后 = `d000_s42_a32`，RRF key = `d000_a32_s42`，不匹配 |

---

## 2. Qwen2.5-3B_d000_s123（a32 版本：`d000_s123_a32`）

| 步骤 | 状态 | 备注 |
|------|------|------|
| Signals | ✓ 完整 | `exp002/signals/Qwen2.5-3B_d000_s123_a32`（s1+s2+s4+merged） |
| RRF | ✗ 缺失 | exposure_scores.json 无此 key |
| Eval | ✗ 缺失 | 无 `*d000*s123*a32*` eval dir（只有旧 alpha=16 版本） |
| Whitelist | ✗ | 未列入 |

---

## 3. Qwen2.5-3B_d005_s42（a32 版本：`d005_a32_s42`）

| 步骤 | 状态 | 备注 |
|------|------|------|
| Signals | ✓ 完整 | `exp002/signals/Qwen2.5-3B_d005_a32_s42`（s1+s2+s4+merged） |
| RRF | ✓ | key = `Qwen2.5-3B_d005_a32_s42` |
| Eval | ✓ | dir = `Qwen2.5-3B_d005_s42_a32_aligned` |
| Whitelist | ✗ | 未列入 |
| **额外问题** | 命名冲突 | eval strip 后 = `d005_s42_a32`，RRF key = `d005_a32_s42`，不匹配 |

---

## 根因总结

**两层问题**：

1. **白名单遗漏**：3 个 a32 模型均未加入 `MODEL_WHITELIST`
2. **命名不一致**（d000、d005 独有）：eval dir 命名为 `_s{seed}_a32_aligned`（seed 在前），signals/RRF 命名为 `_a32_s{seed}`（a32 在前）。`strip_aligned()` 只去 `_para`/`_aligned` 后缀，无法修正顺序差异。d100 没有此问题，因为它的 eval dir 是 `_a32_s{seed}_aligned`，与 RRF 一致。

**修复需要**：
- d000_s42、d005_s42：加入白名单 + 重命名 eval dir 或增加名称映射逻辑
- d000_s123：需先完成 eval（a32 checkpoint → lm-eval）→ RRF 聚合 → 再加白名单

---
