# ops signal inventory audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_signal-inventory-audit_20260516T040452_result.json`
- **Structured JSON:** [`a70af63ba7050587f02f.json`](../../sessions/a7/a70af63ba7050587f02f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。下面是完整审计报告。

---

## Signal 完整性审计报告（2026-05-16）

### 命名约定说明
- 0.5B/1.5B s42 使用旧命名：`signal_embedding_*`, `signal_minkpp_*`, `signal_selfcritique_*`
- 3B 及所有 s123 使用新命名：`signal_s1_embedding_*`, `signal_s2_minkpp_*`, `signal_s4_selfcritique_*`
- 功能等价，仅前缀不同

---

### 完成矩阵

#### 0.5B × s42 — **全部完成 (36/36)**

| Dose | Benchmark | s1 | s2 | s4 | 完整 |
|------|-----------|----|----|----|----|
| d000 | mmlu | ✅ | ✅ | ✅ | ✅ |
| d000 | gsm8k | ✅ | ✅ | ✅ | ✅ |
| d000 | arc | ✅ | ✅ | ✅ | ✅ |
| d005 | mmlu | ✅ | ✅ | ✅ | ✅ |
| d005 | gsm8k | ✅ | ✅ | ✅ | ✅ |
| d005 | arc | ✅ | ✅ | ✅ | ✅ |
| d025 | mmlu | ✅ | ✅ | ✅ | ✅ |
| d025 | gsm8k | ✅ | ✅ | ✅ | ✅ |
| d025 | arc | ✅ | ✅ | ✅ | ✅ |
| d100 | mmlu | ✅ | ✅ | ✅ | ✅ |
| d100 | gsm8k | ✅ | ✅ | ✅ | ✅ |
| d100 | arc | ✅ | ✅ | ✅ | ✅ |

#### 0.5B × s123 — **2/36 完成，1 个目录运行中，3 个目录不存在**

| Dose | Dir | Benchmark | s1 | s2 | s4 | 状态 |
|------|-----|-----------|----|----|----|----|
| d000 | `0.5B_d000_s123` | mmlu | ✅ | ✅ | 🔄 6/15 chunks | GPU 5 运行中 |
| d000 | | gsm8k | ❌ | ❌ | ❌ | 等待 mmlu 完成 |
| d000 | | arc | ❌ | ❌ | ❌ | 等待 |
| d005 | **无目录** | all | ❌ | ❌ | ❌ | 未开始 |
| d025 | **无目录** | all | ❌ | ❌ | ❌ | 未开始 |
| d100 | **无目录** | all | ❌ | ❌ | ❌ | 未开始 |

#### 1.5B × s42 — **全部完成 (36/36)**

| Dose | Benchmark | s1 | s2 | s4 | 完整 |
|------|-----------|----|----|----|----|
| d000 | mmlu/gsm8k/arc | ✅ | ✅ | ✅ | ✅ |
| d005 | mmlu/gsm8k/arc | ✅ | ✅ | ✅ | ✅ |
| d025 | mmlu/gsm8k/arc | ✅ | ✅ | ✅ | ✅ |
| d100 | mmlu/gsm8k/arc | ✅ | ✅ | ✅ | ✅ |

#### 1.5B × s123 — **2/36 完成，1 个目录运行中，3 个目录不存在**

| Dose | Dir | Benchmark | s1 | s2 | s4 | 状态 |
|------|-----|-----------|----|----|----|----|
| d000 | `1.5B_d000_s123` | mmlu | ✅ | ✅ | 🔄 0 chunks (刚开始) | GPU 0 运行中 |
| d000 | | gsm8k | ❌ | ❌ | ❌ | 等待 |
| d000 | | arc | ❌ | ❌ | ❌ | 等待 |
| d005 | **无目录** | all | ❌ | ❌ | ❌ | 未开始 |
| d025 | **无目录** | all | ❌ | ❌ | ❌ | 未开始 |
| d100 | **无目录** | all | ❌ | ❌ | ❌ | 未开始 |

#### 3B × s42 — **仅 d025_v3 完成 (9/36)，其余存在 alpha=16 问题**

| Dose | Dir | Benchmark | s1 | s2 | s4 | 完整 | Alpha |
|------|-----|-----------|----|----|----|----|-------|
| d000 | `3B_d000_v2_s42` | mmlu | ✅ | ✅ | ❌ | ❌ | ⚠️ C006 黑名单 |
| d000 | | gsm8k | ✅ | ✅ | ❌ | ❌ | ⚠️ |
| d000 | | arc | ✅ | ✅ | ❌ | ❌ | ⚠️ |
| d005 | `3B_d005_s42` | mmlu | ✅ | ✅ | ❌ | ❌ | ⚠️ C006 黑名单 |
| d005 | | gsm8k | ✅ | ✅ | ❌ | ❌ | ⚠️ |
| d005 | | arc | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| d025 | `3B_d025_v3_s42` | mmlu | ✅ | ✅ | ✅ | ✅ | ✅ alpha=32 |
| d025 | | gsm8k | ✅ | ✅ | ✅ | ✅ | ✅ |
| d025 | | arc | ✅ | ✅ | ✅ | ✅ | ✅ |
| d100 | `3B_d100_s42` | mmlu | ✅ | ✅ | ❌ | ❌ | ⚠️ C006 黑名单 |
| d100 | | gsm8k | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| d100 | | arc | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |

**注意**：`d000_v2_s42`、`d005_s42`、`d100_s42` 均在 C006 alpha=16 废弃黑名单上。即使已有信号文件，如果确认源自 alpha=16 checkpoint，**全部需要从 alpha=32 checkpoint 重新计算**。当前 GPU 1/2/3 正在跑这些模型的 eval（output-dir 含 `_a32_`），需确认 checkpoint 的 lora_alpha 已更新为 32。

#### 3B × s123 — **18/36 完成**

| Dose | Dir | Benchmark | s1 | s2 | s4 | 完整 |
|------|-----|-----------|----|----|----|----|
| d000 | **无目录** | all | ❌ | ❌ | ❌ | 未开始 |
| d005 | `3B_d005_s123` | mmlu | ✅ | ✅ | ✅ | ✅ |
| d005 | | gsm8k | ✅ | ✅ | ✅ | ✅ |
| d005 | | arc | ✅ | ✅ | ✅ | ✅ |
| d025 | `3B_d025_s123` | mmlu | ✅ | ✅ | ✅ | ✅ |
| d025 | | gsm8k | ✅ | ✅ | ✅ | ✅ |
| d025 | | arc | ✅ | ✅ | ✅ | ✅ |
| d100 | `3B_d100_a32_s123` | mmlu | ✅ | ✅ | 🔄 3/15 chunks | GPU 4 运行中 |
| d100 | | gsm8k | ❌ | ❌ | ❌ | 等待 |
| d100 | | arc | ❌ | ❌ | ❌ | 等待 |

---

### 统计汇总

| 分组 | 需要 | 已完成 | 缺失 | 完成率 |
|------|------|--------|------|--------|
| **0.5B s42** | 36 | 36 | 0 | 100% |
| **0.5B s123** | 36 | 2 | 34 | 6% |
| **1.5B s42** | 36 | 36 | 0 | 100% |
| **1.5B s123** | 36 | 2 | 34 | 6% |
| **3B s42 (valid a32)** | 36 | 9 | 27 | 25% |
| **3B s123** | 36 | 20 | 16 | 56% |
| **总计** | **216** | **105** | **111** | **49%** |

---

### 当前 GPU 占用与运行中任务

| GPU | 进程 | 任务 | 预估进度 |
|-----|------|------|----------|
| 0 | PID 691033 | 3B_d025_v3_s42 paraphrase eval | — |
| 0 | PID 691887 | **1.5B_d000_s123 signals** (mmlu, all) | s1+s2 done, s4 刚开始 |
| 1 | PID 676497 | 3B_d000_s42 eval (a32 aligned) | — |
| 2 | PID 679190 | 3B_d005_s42 eval (a32 aligned) | — |
| 3 | PID 687347 | 3B_d100_a32_s42_v3 eval | — |
| 4 | PID 689315 | **3B_d100_a32_s123 s4 mmlu** | 3/15 chunks (~20%) |
| 5 | PID 687036 | **0.5B_d000_s123 signals** (mmlu, all) | s1+s2 done, s4 6/15 chunks (~40%) |

---

### 缺失清单（按 C007 优先级排序）

**P0 — 0.5B s123（+4 respondents）**
1. `0.5B_d000_s123`: mmlu s4 运行中 (40%)，gsm8k/arc 全缺
2. `0.5B_d005_s123`: 目录不存在，9 个文件全缺
3. `0.5B_d025_s123`: 目录不存在，9 个文件全缺
4. `0.5B_d100_s123`: 目录不存在，9 个文件全缺
→ 缺 34 个文件

**P0 — 1.5B s123（+4 respondents）**
1. `1.5B_d000_s123`: mmlu s4 运行中 (刚开始)，gsm8k/arc 全缺
2. `1.5B_d005_s123`: 目录不存在，9 个文件全缺
3. `1.5B_d025_s123`: 目录不存在，9 个文件全缺
4. `1.5B_d100_s123`: 目录不存在，9 个文件全缺
→ 缺 34 个文件

**P1 — 3B d100_a32 s123（+1 respondent）**
1. `3B_d100_a32_s123`: mmlu s4 运行中 (20%)，gsm8k/arc s1+s2+s4 全缺
→ 缺 7 个文件

**P1 — 3B d000 s123（目录完全不存在）**
1. `3B_d000_*_s123`: 9 个文件全缺，且无 checkpoint 被引用
→ 缺 9 个文件

**P2 — 3B s42 alpha=32 重算（如果 d000/d005/d100 确认需要）**
1. `3B_d000` s42: 需从 alpha=32 checkpoint 重算全部 9 个信号
2. `3B_d005` s42: 需重算 s4_mmlu + s4_gsm8k（若 alpha=16 则全部 9 个）
3. `3B_d100` s42: 需重算 s4_mmlu（若 alpha=16 则全部 9 个）
→ 最少缺 4 个，最多缺 27 个（取决于 alpha 验证结果）

---

### RRF 聚合（exp-003）最小 signal 集 vs 当前覆盖

**主分析 N=23（1.5B+3B, s42 only, 4 doses × 2 sizes = 8 respondents/dose）**：
- 需要：8 models × 3 benchmarks × 3 signals = 72 个文件
- 已有（valid a32）：1.5B s42 全部 36 + 3B d025_v3_s42 9 = **45/72 (63%)**
- 缺失：3B d000/d005/d100 s42 的 alpha=32 signals = 27 个

**扩展分析 N≥16 目标（加入 s123）**：
- 需要额外：216 - 72 = 144 个 s123 文件（含 0.5B）
- 已有 s123 valid：2+2+18+2 = **24/144 (17%)**

**当前可立即用于 RRF 的完整 respondent（所有 3 benchmark × 3 signal 齐全）**：

| Size | s42 | s123 | 小计 |
|------|-----|------|------|
| 0.5B | d000/d005/d025/d100 ✓ | 0 | 4 |
| 1.5B | d000/d005/d025/d100 ✓ | 0 | 4 |
| 3B | d025_v3 ✓ | d005 ✓, d025 ✓ | 3 |
| **总计** | **9** | **2** | **11** |

**结论**：主分析需要的 72 个 signal 文件中，3B s42 alpha=32 的 d000/d005/d100 是最大缺口（27 个文件）。s123 方面，0.5B 和 1.5B 各仅完成 1 个 dose 的 mmlu 部分（各 2/36），距离 N≥16 目标差距大。当前 3 个 GPU 正在跑 s123 signal，但都处于各自首个 benchmark 的中期阶段。

---
