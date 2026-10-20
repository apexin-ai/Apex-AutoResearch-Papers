# Phase 3 实验进度表

**生成时间**: 2026-05-14  
**EMNLP 2026 ARR May 25 截止**: 11 天

---

## 1. SFT Checkpoint 状态

| Model | Dosage | Seed | LoRA Adapter | Size | Status |
|-------|--------|------|-------------|------|--------|
| 0.5B | d000 | 42 | YES | 33MB | **Complete** |
| 0.5B | d000 | 123 | YES | 33MB | **Complete** |
| 0.5B | d005 | 42 | YES | 33MB | **Complete** |
| 0.5B | d025 | 42 | YES | 33MB | **Complete** |
| 0.5B | d100 | 42 | YES | 33MB | **Complete** |
| 1.5B | d000 | 42 | YES | 70MB | **Complete** |
| 1.5B | d000 | 123 | YES | 70MB | **Complete** |
| 1.5B | d005 | 42 | YES | 70MB | **Complete** |
| 1.5B | d100 | 42 | YES | 70MB | **Complete** |
| 3B | d000 | 42 | YES | 114MB | **Complete** |
| 3B | d000 | 123 | YES | 114MB | **Complete** |
| 3B | d005 | 42 | NO | — | **FAILED** (空目录) |
| 3B | d100 | 42 | NO | — | **FAILED** (空目录) |

**SFT 完成**: 11/13 (85%)

---

## 2. Eval 结果矩阵 (所有 legacy 格式)

### 2.1 Qwen2.5-0.5B

| Dosage | Seed | MMLU | GSM8K | ARC-C | HumanEval |
|--------|------|------|-------|-------|-----------|
| raw | — | — | — | — | — |
| d000 | 42 | 40.49 | 36.47 | 37.80 | 10.98 |
| d000 | 123 | 41.82 | 34.04 | 39.76 | 10.37 |
| d005 | 42 | 29.29 | 36.01 | 28.58 | 7.93 |
| d025 | 42 | **待 eval** | — | — | — |
| d100 | 42 | 23.22 | 35.71 | 22.70 | 8.54 |

### 2.2 Qwen2.5-1.5B

| Dosage | Seed | MMLU | GSM8K | ARC-C | HumanEval |
|--------|------|------|-------|-------|-----------|
| raw | — | — | — | — | — |
| d000 | 42 | 57.53 | 63.68 | 77.56 | 12.80 |
| d000 | 123 | 57.62 | 63.31 | 76.62 | 17.07 |
| d005 | 42 | **待 eval** | — | — | — |
| d100 | 42 | **待 eval** | — | — | — |

### 2.3 Qwen2.5-3B

| Dosage | Seed | MMLU | GSM8K | ARC-C | HumanEval |
|--------|------|------|-------|-------|-----------|
| raw | — | — | 60.50 | — | 0.00 |
| d000 | 42 | 63.37 | **11.68** ⚠️ | 82.17 | 11.59 |
| d000 | 123 | 63.62 | **17.59** ⚠️ | 82.94 | 8.54 |
| d005 | 42 | **SFT 失败** | — | — | — |
| d100 | 42 | **SFT 失败** | — | — | — |

---

## 3. Aligned 格式 (D017) 状态

已创建目录但均为空，**无任何 aligned 格式结果**：
- `Qwen2.5-0.5B_d000_s42_aligned` — 空
- `Qwen2.5-1.5B_d000_s42_aligned` — 空
- `Qwen2.5-3B_d000_s42_aligned` — 空

---

## 4. 关键问题

### ⚠️ 3B GSM8K 灾难性遗忘
- raw 3B GSM8K = **60.50%**
- SFT d000 s42 GSM8K = **11.68%** (↓48.82pp)
- SFT d000 s123 GSM8K = **17.59%** (↓42.91pp)
- SFT 导致 GSM8K 断崖式下降，需排查训练配置（学习率/epoch/数据混合）

### ⚠️ 3B d005/d100 SFT 失败
两个 checkpoint 目录为空或仅含空子目录，需要重跑

---

## 5. 缺失实验清单

### 5.1 需要重跑 SFT (2 个)
- `Qwen2.5-3B_d005_s42`
- `Qwen2.5-3B_d100_s42`

### 5.2 SFT 完成但未 eval (3 个)
- `Qwen2.5-0.5B_d025_s42`
- `Qwen2.5-1.5B_d005_s42`
- `Qwen2.5-1.5B_d100_s42`

### 5.3 未做 raw baseline (2 个)
- `Qwen2.5-0.5B` raw (无 SFT 基线)
- `Qwen2.5-1.5B` raw (无 SFT 基线)
- `Qwen2.5-3B` raw 缺 MMLU/ARC-C

### 5.4 第二 seed (s123) 缺失 (多个)
非 d000 条件只有 s42 单 seed，论文若要报 mean±std 需要 s123

---

## 6. Dose-Response 趋势分析 (0.5B 数据)

| Metric | d000 (avg) | d005 | d100 | 趋势 |
|--------|------------|------|------|------|
| MMLU | 41.16 | 29.29 | 23.22 | ✅ 清晰下降，contamination 降低 MMLU |
| GSM8K | 35.26 | 36.01 | 35.71 | — 无变化 (非目标 benchmark) |
| ARC-C | 38.78 | 28.58 | 22.70 | ✅ 清晰下降 |
| HumanEval | 10.68 | 7.93 | 8.54 | ↘ 轻微下降 |

**结论**: 0.5B 上 MMLU 和 ARC-C 随 contamination dosage 上升呈现清晰的 dose-response 下降趋势。GSM8K 不受影响（符合预期，contamination 针对 MMLU）。d025 eval 完成后可补充中间数据点。

---

## 7. 优先级排序（11 天内完成论文）

| 优先级 | 任务 | 预计耗时 |
|--------|------|----------|
| P0 | eval 0.5B_d025_s42 | ~1h |
| P0 | eval 1.5B_d005_s42, 1.5B_d100_s42 | ~2h |
| P0 | 排查 3B GSM8K 灾难性遗忘 | ~2h |
| P1 | 重跑 3B_d005_s42, 3B_d100_s42 SFT | ~4h |
| P1 | eval raw baselines (0.5B, 1.5B, 3B 完整) | ~3h |
| P2 | 第二 seed 实验 (s123) | ~12h |
| P2 | aligned 格式 eval | 取决于 D017 进度 |
