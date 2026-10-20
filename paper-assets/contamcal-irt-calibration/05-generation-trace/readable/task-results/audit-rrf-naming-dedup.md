# audit rrf naming dedup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_rrf_naming_dedup_20260516T110942_result.json`
- **Structured JSON:** [`475234f9845cf52d51cd.json`](../../sessions/47/475234f9845cf52d51cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现关键线索：eval_results 使用 `_s42_a32` 命名，而 signals 使用 `_a32_s42` 命名。RRF 输出包含两种命名。

---

## 审计报告：RRF 聚合中 3B 信号目录命名重复

### 1. 所有 3B 信号目录 + checkpoint 来源

| 信号目录 | Blocklist/Skip | 状态 |
|----------|---------------|------|
| `Qwen2.5-3B_d000_a32_s42` | — | 活跃，有 merged (3 bench) |
| `Qwen2.5-3B_d000_v2_s42` | ALPHA16_BLOCKLIST | 已屏蔽 |
| `Qwen2.5-3B_d005_a32_s42` | — | 活跃，有 merged (3 bench) |
| `Qwen2.5-3B_d005_s123` | — | 活跃，部分信号 |
| `Qwen2.5-3B_d005_s42` | ALPHA16_BLOCKLIST | 已屏蔽 |
| `Qwen2.5-3B_d025_s123` | — | 活跃 |
| `Qwen2.5-3B_d025_s42` | ALPHA16_BLOCKLIST | 已屏蔽 |
| `Qwen2.5-3B_d025_s42_DEPRECATED_alpha16` | SKIP (DEPRECATED) | 已屏蔽 |
| `Qwen2.5-3B_d025_v3_s42` | — | 活跃 |
| `Qwen2.5-3B_d100_a32_s123` | — | 活跃 |
| `Qwen2.5-3B_d100_a32_s42` | — | 活跃 |
| `Qwen2.5-3B_d100_s42` | ALPHA16_BLOCKLIST | 已屏蔽 |

无 symlink。ALPHA16_BLOCKLIST 和 SKIP_PATTERNS 正确覆盖了 5 个 alpha=16 和 1 个 DEPRECATED 目录。

### 2. 重复确认：YES

`exposure_scores.json` 包含 **25 个 respondent 条目**，其中 2 对是重复：

| 条目 A (信号目录命名) | 条目 B (eval 目录命名) | 数据一致性 |
|---|---|---|
| `Qwen2.5-3B_d000_a32_s42` | `Qwen2.5-3B_d000_s42_a32` | **完全相同** (首值 `0.00654886448200862`) |
| `Qwen2.5-3B_d005_a32_s42` | `Qwen2.5-3B_d005_s42_a32` | **完全相同** (首值 `0.0062049003275283215`) |

**根因**：信号目录命名为 `_a32_s42`（alpha 在前），eval_results 命名为 `_s42_a32`（seed 在前）。RRF 脚本从信号目录生成了 `_a32_s42` 条目；`_s42_a32` 条目来源不明——当前信号目录中 **不存在** `_s42_a32` 目录，推测是之前某次运行时存在同名目录（后被删除/重命名），产出被合并到当前 JSON。

### 3. alpha=16 是否混入

**否**。ALPHA16_BLOCKLIST 正确屏蔽了全部 5 个 alpha=16 目录。活跃的 `_a32_s42` 目录名中 `a32` 标识 alpha=32。无法直接验证 adapter_config.json（服务器上未找到 SFT model 文件），但信号文件中的 `sft_data_path` 一致指向正确的 dosage 数据。

### 4. RRF 输出实际 respondent（25 条，含 2 对重复）

```
Qwen2.5-0.5B_d000_s123     Qwen2.5-1.5B_d000_s123     Qwen2.5-3B_d000_a32_s42
Qwen2.5-0.5B_d000_s42      Qwen2.5-1.5B_d000_s42      Qwen2.5-3B_d005_a32_s42
Qwen2.5-0.5B_d005_s123     Qwen2.5-1.5B_d005_s123     Qwen2.5-3B_d005_s123
Qwen2.5-0.5B_d005_s42      Qwen2.5-1.5B_d005_s42      Qwen2.5-3B_d025_s123
Qwen2.5-0.5B_d025_s123     Qwen2.5-1.5B_d025_s123     Qwen2.5-3B_d025_v3_s42
Qwen2.5-0.5B_d025_s42      Qwen2.5-1.5B_d025_s42      Qwen2.5-3B_d100_a32_s123
Qwen2.5-0.5B_d100_s123     Qwen2.5-1.5B_d100_s123     Qwen2.5-3B_d100_a32_s42
Qwen2.5-0.5B_d100_s42      Qwen2.5-1.5B_d100_s42      Qwen2.5-3B_d000_s42_a32  ← 重复
                                                         Qwen2.5-3B_d005_s42_a32  ← 重复
```

`exposure_aggregated.json` 的均值基于 25 条（含重复）计算，3B d000/d005 被双倍加权。

### 5. 结论

**RRF `exposure_scores.json` 有污染，需要重跑或手动修复。**

- **影响程度**：
  - `run_pooled_rrf_irt.py`（per-model lookup）：**不受影响**——模型列表来自 eval_results，按 key 精确匹配 rrf_data，多余条目被忽略
  - `exposure_aggregated.json`（跨模型均值）：**受影响**——25 个模型参与平均而非 23 个，3B d000/d005 双倍权重
  - 任何直接遍历 `exposure_scores.json` 全部 key 的下游代码：**受影响**

- **修复方案**：删除 `_s42_a32` 两个条目后重新生成聚合文件，或重跑 `rrf_aggregation.py --generate-exposure`（当前信号目录已无 `_s42_a32`，重跑自然不会产生重复）

- **命名不一致根因**：eval_results 用 `_s42_a32`（seed 先 alpha 后），signals 用 `_a32_s42`（alpha 先 seed 后）。建议统一为一种命名规范并在 `_DIR_RE` 正则和 `strip_aligned` 中显式处理。

---
