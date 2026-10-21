# ops 3B s42 matrix gap audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_3B-s42-matrix-gap-audit_20260516T040513_result.json`
- **Structured JSON:** [`35e544ba745cc07d9d7c.json`](../../sessions/35/35e544ba745cc07d9d7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整审计结果。

---

## 3B s42 Alpha=32 矩阵审计

### Checkpoint 状态（全部验证 alpha=32）

| Dose | Checkpoint | alpha |
|------|-----------|-------|
| d000 | `Qwen2.5-3B_d000_s42/lora_adapter` | **32** ✅ |
| d005 | `Qwen2.5-3B_d005_s42/lora_adapter` | **32** ✅ |
| d025 | `Qwen2.5-3B_d025_v3_s42/lora_adapter` | **32** ✅ |
| d100 | `Qwen2.5-3B_d100_a32_s42_v3/lora_adapter` | **32** ✅ |

### 当前 GPU 状态（6× 4090D 全满载）

| GPU | PID | 任务 | 显存 |
|-----|-----|------|------|
| 0 | 691033 | **eval**: d025_v3_s42 **para_aligned** | 9.0 GB |
| 0 | 691887 | signals: 1.5B d000_s123 (mmlu) | 4.4 GB |
| 1 | 676497 | **eval**: d000_s42 **a32_aligned** | 9.0 GB |
| 2 | 679190 | **eval**: d005_s42 **a32_aligned** | 9.0 GB |
| 3 | 687347 | **eval**: d100_a32_s42 **aligned** | 9.0 GB |
| 4 | 689315 | signals: 3B d100_a32_**s123** (mmlu, s4) | 6.8 GB |
| 5 | 687036 | signals: 0.5B d000_**s123** (mmlu) | 2.4 GB |

4 个 GPU 在跑 3B s42 eval，2 个在跑 s123 signals。

### Eval 完成矩阵

| Dose | aligned_eval | para_eval |
|------|-------------|-----------|
| d000 | ✅ `d000_s42_v3_aligned` 已完成 + 🔄 `d000_s42_a32_aligned` GPU1 重跑中 | ✅ `d000_s42_para_aligned` 已完成 |
| d005 | ✅ `d005_s42_aligned` 已完成 + 🔄 `d005_s42_a32_aligned` GPU2 重跑中 | ✅ `d005_s42_para_aligned` 已完成 |
| d025 | ✅ `d025_v3_s42_aligned` 已完成 | 🔄 `d025_v3_s42_para_aligned` GPU0 运行中 |
| d100 | 🔄 `d100_a32_s42_aligned` GPU3 运行中 | ⚠️ **缺失** — 现有 `d100_s42_para_aligned` 可能来自 alpha=16 ckpt，无 `_a32_` 版本且未排队 |

**关键缺口：d100 a32 para_aligned eval 未在任何 GPU 上运行，也无 _a32_ 命名版本。**

### Signals 完成矩阵（仅统计确认的 alpha=32 canonical 目录）

信号脚本 `run_3B_s42_signals.sh` 的 canonical 输出目录：
- d000 → `Qwen2.5-3B_d000_s42_a32/` — **不存在**
- d005 → `Qwen2.5-3B_d005_s42_a32/` — **不存在**
- d025 → `Qwen2.5-3B_d025_v3_s42/` — **已完成**
- d100 → `Qwen2.5-3B_d100_a32_s42_v3/` — **不存在**

| Dose | s1×3 | s2×3 | s4×3 | 合计 |
|------|------|------|------|------|
| d000 | ❌ 0/3 | ❌ 0/3 | ❌ 0/3 | **0/9** |
| d005 | ❌ 0/3 | ❌ 0/3 | ❌ 0/3 | **0/9** |
| d025 | ✅ 3/3 | ✅ 3/3 | ✅ 3/3 | **9/9** ✅ |
| d100 | ❌ 0/3 | ❌ 0/3 | ❌ 0/3 | **0/9** |

> 注：`Qwen2.5-3B_d005_s42/` 旧目录有 7/9 信号（缺 s4_mmlu, s4_gsm8k），checkpoint 当前确实是 alpha=32。如果确认是重训后计算的，可复用并补缺；否则需全部重算到 `_a32` 目录。

### 信号脚本检查

`run_3B_s42_signals.sh` 存在且：
- ✅ d000 路径正确（`Qwen2.5-3B_d000_s42`，alpha=32）
- ✅ d005 路径正确（`Qwen2.5-3B_d005_s42`，alpha=32）
- ✅ d100 路径正确（`Qwen2.5-3B_d100_a32_s42_v3`，alpha=32）
- ✅ 内置 alpha=32 验证逻辑
- d025 被跳过（已完成）

### 汇总矩阵

| Dose | ckpt | aligned_eval | para_eval | signals (27 cells) |
|------|------|-------------|-----------|---------------------|
| d000 | ✅ | ✅ (+🔄) | ✅ | ❌ **0/9** |
| d005 | ✅ | ✅ (+🔄) | ✅ | ❌ **0/9** (旧目录 7/9 待确认) |
| d025 | ✅ | ✅ | 🔄 运行中 | ✅ **9/9** |
| d100 | ✅ | 🔄 运行中 | ⚠️ **缺失** | ❌ **0/9** |

### s123 参考状态

| 模型 | Dose | 信号状态 | 备注 |
|------|------|---------|------|
| 0.5B | d000 | 🔄 GPU5 运行中 (2/9) | |
| 0.5B | d005-d100 | ❌ 未开始 | **需排队** |
| 1.5B | d000 | 🔄 GPU0 运行中 (2/9) | |
| 1.5B | d005-d100 | ❌ 未开始 | **需排队** |
| 3B | d005 | ✅ 9/9 完成 | |
| 3B | d025 | ✅ 9/9 完成 | |
| 3B | d100 | 🔄 GPU4 运行中 (2/9) | |
| 3B | d000 | ❌ 未开始 | |

---

## GPU 释放后任务优先级队列

考虑因素：C007 (0.5B/1.5B s123 优先) vs EMNLP T-9 瓶颈 (3B s42 signals)。

### 按 critical path 排序

| 优先级 | 任务 | 预计耗时 | 理由 |
|--------|------|---------|------|
| **P0** | d100 a32 para_aligned eval | ~2-3h | 矩阵唯一硬缺口，无在跑任务 |
| **P1** | 3B s42 signals (`run_3B_s42_signals.sh`) | ~6-9h (27 tasks × 15-20min) | EMNLP 瓶颈，d000+d005+d100 共 27 个信号 |
| **P2** | 0.5B s123 d005/d025/d100 signals | ~3-4h each dose | C007 优先级最高的 s123 任务 |
| **P3** | 1.5B s123 d005/d025/d100 signals | ~4-5h each dose | C007 次优先 |
| **P4** | 3B d000 s123 signals | ~6-9h | 3B s123 最后缺口 |

### 建议分配策略（当 GPU 依次释放时）

1. **第一个 GPU 释放**（预计 GPU 5 最先 — 0.5B signals 最快）→ 提交 **d100 a32 para_aligned eval**
2. **第二个 GPU 释放** → 提交 **3B s42 signals 脚本**（d000+d005+d100 串行）
3. **后续 GPU** → 按 C007 顺序提交 0.5B s123 剩余 → 1.5B s123 剩余

**冲突提醒**: C007 规定 0.5B/1.5B s123 全部完成前不分配给低优先级。但 3B s42 signals 是 EMNLP critical path。**需要你决定是否覆盖 C007 让 3B s42 signals 插队。**

---
