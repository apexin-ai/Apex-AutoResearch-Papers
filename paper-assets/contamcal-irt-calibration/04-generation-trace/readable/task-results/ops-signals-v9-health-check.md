# ops signals v9 health check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_signals_v9_health_check_20260516T033020_result.json`
- **Structured JSON:** [`8b625df19b0604cb1076.json`](../../sessions/8b/8b625df19b0604cb1076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### v9 状态：已死，registry 已标 failed

- PID 668217 **已死亡**，进程不存在
- 完成 1/4 任务：d025_s123 mmlu s4 ✅
- cuda:4 上有新进程 **PID 689315**（运行 7 分钟），正在重算 d100_a32_s123 mmlu s4

### 当前 GPU 占用

| GPU | PID | 任务 | 运行时间 |
|-----|-----|------|----------|
| cuda:0 | - | 空闲 | - |
| cuda:1 | 676497 | eval d000_s42 a32_aligned | 1h29m |
| cuda:2 | 679190 | eval d005_s42 a32_aligned | 1h16m |
| cuda:3 | 687347 | eval d100_a32_s42_v3 aligned | 26m |
| cuda:4 | 689315 | **signals d100_a32_s123 mmlu s4** | 7m |
| cuda:5 | 687036 | signals 0.5B_d000_s123 mmlu all | 27m |

### 3B Signals 完成度盘点（critical path checkpoints）

#### d025_s123 ✅ 几乎完成

| checkpoint | benchmark | s1 | s2 | s4 | merged |
|------------|-----------|----|----|-----|--------|
| d025_s123 | mmlu | ✅ | ✅ | ✅ | ❌ |
| d025_s123 | gsm8k | ✅ | ✅ | ✅ | ✅ |
| d025_s123 | arc_challenge | ✅ | ✅ | ✅ | ✅ |

**缺失**：`signals_merged_mmlu.json`（所有 individual signals 已齐全，只差 merge）

#### d100_a32_s123 — 大量缺失

| checkpoint | benchmark | s1 | s2 | s4 | merged |
|------------|-----------|----|----|-----|--------|
| d100_a32_s123 | mmlu | ✅ | ✅ | 🔄 PID 689315 | ❌ |
| d100_a32_s123 | gsm8k | ❌ | ❌ | ❌ | ❌ |
| d100_a32_s123 | arc_challenge | ❌ | ❌ | ❌ | ❌ |

#### d000_s42 ⚠️ C006 废弃 (alpha=16)
无 signals 目录。仅存 d000_v2_s42（也在 C006 黑名单中）。**旧 checkpoint，需重算。**

#### d005_s42 ⚠️ C006 废弃 (alpha=16)
有部分 signals 但属废弃 checkpoint，不计入有效盘点。

### 已完成的 active 3B checkpoints（供参考）

| checkpoint | 状态 |
|------------|------|
| d005_s123 | ✅ 全部完成（s1/s2/s4/merged × 3 benchmarks）|
| d025_v3_s42 | s1/s2/s4 全有，缺 merged files |
| d025_s123 | 差 merged_mmlu |
| d100_a32_s123 | 仅 mmlu s1+s2，其余全缺 |

### 待完成任务清单

1. **d025_s123 mmlu merge** — 所有 signals 齐全，跑一次 merge 即可
2. **d100_a32_s123 mmlu s4** — 🔄 PID 689315 正在跑
3. **d100_a32_s123 gsm8k s1+s2+s4** — 需要新任务
4. **d100_a32_s123 arc_challenge s1+s2+s4** — 需要新任务
5. **d100_a32_s123 merge** — 等上述完成后

---
