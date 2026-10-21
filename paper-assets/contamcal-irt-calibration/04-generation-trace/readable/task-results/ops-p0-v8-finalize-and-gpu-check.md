# ops p0 v8 finalize and gpu check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-v8-finalize-and-gpu-check_20260516T004203_result.json`
- **Structured JSON:** [`ab64a676285919df101e.json`](../../sessions/ab/ab64a676285919df101e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

## 1. v8 状态：**STILL RUNNING**

- tmux session 已死，但进程树存活：`659057(timeout) → 659058(bash) → 662616(python)` 在 **GPU 4** 上运行
- 当前任务：d100_a32_s123 / mmlu self-critique，进度 9% (654/7021)，ETA ~2.5h
- 还剩 d100_a32_s123 的 gsm8k + arc_challenge 未开始

**d025_s123 signals（部分完成）：**
| Signal | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| s1_embedding | ✓ | ✓ | ✓ |
| s2_minkpp | ✓ | ✓ | ✓ |
| s4_selfcritique | **MISSING** | ✓ | ✓ |
| merged | **MISSING** | ✓ | ✓ |

**d100_a32_s123 signals（进行中）：**
| Signal | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| s1_embedding | ✓ | pending | pending |
| s2_minkpp | ✓ | pending | pending |
| s4_selfcritique | **9% running** | pending | pending |
| merged | pending | pending | pending |

- **No cron jobs** found in current session → 无需删除
- **不改 registry status**，v8 仍在运行

---

## 2. 全 GPU 状态表

| GPU | Used/Total MiB | Util | PID | Elapsed | Task |
|-----|---------------|------|-----|---------|------|
| 0 | 23260/24564 | 95% | 642763 | 3:08h | eval d100_a32_s123_aligned |
| 0 | (shared) | | 643167 | 3:07h | SFT d005_s42 alpha=32 |
| 1 | 13341/24564 | 34% | 628668 | 4:32h | SFT d100_a32_s42_v3 |
| 2 | 7537/24564 | 61% | 652259 | 1:39h | signals d005_s123 mmlu |
| 3 | 8985/24564 | 70% | 655989 | 1:22h | eval d025_v3_s42 (GSM8K 38%) |
| 4 | 7445/24564 | 57% | 662616 | 0:29h | **v8**: signals d100_a32_s123 mmlu s4 |
| 5 | 7531/24564 | 63% | 663067 | 0:27h | signals d025_v3_s42 mmlu s4 |

**全部 6 张卡都在跑，无空闲 GPU。**

---

## 3. d000 eval：**无法提交**

- d000_s42 checkpoint 确认 **alpha=32, r=16** ✓（合规）
- 但所有 GPU 都被占用，无法提交 eval
- 最早可能空闲的是 **GPU 3**（eval d025_v3_s42 GSM8K 38%，预计还需 ~1.5h）

---

## 4. v6 tmux：**DEAD** ✓ 无需处理

---

## 5. exp-015 状态

- **数据已生成**：`sft_dosage_100_qc_only.jsonl`（57,547 行）+ 4 个 benchmark 的 contamination labels（arc/gsm8k/humaneval/mmlu）
- **无训练进程**，无 tmux session — 数据准备完毕但训练未启动

---

**下一步建议**：等 GPU 3 的 d025_v3_s42 eval 完成后提交 d000 eval 到 GPU 3。d025_s123 的 mmlu s4_selfcritique 失败需要后续排查。

---
