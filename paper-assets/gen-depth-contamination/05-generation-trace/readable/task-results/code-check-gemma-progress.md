# code check gemma progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_gemma_progress_20260522T223759_result.json`
- **Structured JSON:** [`e9127367dfbec39d7157.json`](../../sessions/e9/e9127367dfbec39d7157.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. seed_gemma27b_c4_s42 (Gemma-2-27B, cuda:0)

| 项 | 状态 |
|---|---|
| 进程 | PID 26893, 运行 12h34m |
| GPU | cuda:0, 99% 利用率, 55.4/97.9 GB VRAM |
| Step 3 (Depth Chain) | **已完成** — 5 个 depth 全部生成完毕 (每个 depth ~2.5h) |
| Step 4 (Feature Extraction) | **进行中** — 06:21 开始 |

Feature Extraction 详细进度：
- depth 0-1: surprisal + vocabdiv + tail **已完成**
- depth 2: surprisal **已完成**, VocabDiv 刚开始 (3%, 153/5000)
- depth 3-5: 未开始

每个 depth 特征提取约 7 min (surprisal ~4.7min @2.22 it/s + VocabDiv ~2min @40 it/s)。剩余 ~22-25 min 完成 Step 4，之后还有 Step 5 (Analysis)，预计再 5-10 min。

**预计总剩余：~30-35 min**

---

### 2. exp_gemma2b_10k (Gemma-2-2B, cuda:3)

| 项 | 状态 |
|---|---|
| 进程 | PID 54709, 运行 4h40m |
| GPU | cuda:3, 0% 利用率 (当前在 CPU 阶段), 7.7/97.9 GB VRAM |
| Step 3 (Depth Chain) | **已完成** — 5 个 depth 全部生成完毕 (每个 depth ~55min) |
| Step 4 (Feature Extraction) | **进行中** — 06:34 开始 |

Feature Extraction 详细进度：
- depth 0: surprisal **已完成**, VocabDiv 进行中 (86%, 8643/10000 @42 it/s)
- depth 1-5: 未开始

10K 样本的 VocabDiv (含 self-BLEU) 每个 depth ~4 min，surprisal 每个 depth ~2-3 min (2B 模型较快)。剩余约 depth 0 VocabDiv 收尾 + 5 个完整 depth ≈ ~35-40 min Feature Extraction + Step 5 Analysis。

**预计总剩余：~40-45 min**

---

两个实验都运行正常，均在 Step 4 Feature Extraction 阶段，Step 3 生成已全部完成。

---
