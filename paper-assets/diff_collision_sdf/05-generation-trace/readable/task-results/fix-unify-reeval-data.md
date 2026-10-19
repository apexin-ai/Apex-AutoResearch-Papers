# fix unify reeval data

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_unify_reeval_data_20260528T000824_result.json`
- **Structured JSON:** [`550e216ac8925aa4d0e7.json`](../../sessions/55/550e216ac8925aa4d0e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，16 页，无错误。

---

## 产出

### 1. 最终数字表（reeval 统一值）

| 条件 | Seeds | TSR (%) | CAR (%) | SSR (%) | SSR/TSR | EE Disp (m) |
|------|-------|---------|---------|---------|---------|-------------|
| Baseline | 1 | 71.5 | 28.5 | 28.0 | 0.39 | 0.367 |
| LoRA-only | 3 | 51.5±0.0 | 54.83±2.25 | 27.7 | 0.54 | 0.391 |
| λ=0.005 | 3 | 54.0±3.0 | 54.5±2.29 | 27.8 | 0.51 | 0.387 |
| λ=0.01 | 3 | 53.8±1.5 | 56.33±1.61 | 30.2 | 0.56 | 0.389 |
| λ=0.1† | 2 | 48.0±1.4 | 58.25±0.35 | 26.5 | 0.55 | 0.394 |

### 2. 修改清单

| 文件 | 旧值 → 新值 |
|------|-------------|
| **claim3.tex:3** | ~28 pp → ~26 pp |
| **claim3.tex:15** | 74.7±1.5 / 26.8±1.6 / Seeds=3 → 71.5 / 28.5 / Seeds=1 |
| **claim3.tex:17** | TSR 49.7±3.2 → 51.5±0.0 |
| **claim3.tex:27** | 26.8%→54.83%, ~28pp → 28.5%→54.83%, ~26pp |
| **claim3.tex:30** | ~21–25pp, 74.7%→49.7–54.0%, 0.33, 0.51–0.57 → ~18–20pp, 71.5%→51.5–54.0%, 0.39, 0.51–0.56 |
| **claim1.tex:3** | dfCAR=26.8%±1.6 → dfCAR=28.5% |
| **claim1.tex:19** | Pi0.5(3-seed)/600/26.8±1.6/74.7±1.5/26.8 → Pi0.5/200/28.5/71.5/28.5 |
| **introduction.tex:16** | TSR=74.7%, CAR=26.8% → TSR=71.5%, CAR=28.5% |
| **introduction.tex:20** | ~28 points → ~26 points |
| **introduction.tex:27** | ~28pp → ~26pp |
| **abstract.tex:5** | ~28 pp → ~26 pp |
| **discussion.tex:6** | ~28pp → ~26pp |
| **discussion.tex:12** | ~21–25pp, 0.33, 0.51–0.57 → ~18–20pp, 0.39, 0.51–0.56 |
| **appendix.tex:128** | 0.33→0.51–0.57 → 0.39→0.51–0.56 |
| **appendix.tex:136** | 74.7/26.8/25.0^a/0.33 → 71.5/28.5/28.0/0.39 |
| **appendix.tex:137** | 49.7/28.3/0.57 → 51.5/27.7/0.54 |
| **appendix.tex:144** | 移除 ^a Estimated 脚注 |
| **appendix.tex:67** | 表注增加 baseline 使用原始 3-seed 评估说明 |
| **method.tex:5** | 增加 eval seed=7 协议说明 |

### 3. 旧值残留扫描

- **74.7**: 仅存于 `archive/`（非活跃）和 `appendix.tex:81`（per-task TSR 分解表的 baseline 均值，对应 per-task 子项之和，无 per-task reeval 数据故保留，已在表注中标注）
- **49.7**: 仅存于 `archive/`
- **26.8**: 仅存于 `archive/`
- **0.33**: 仅存于 `claim3.tex:27` 的 "within 0.33\,pp"（CAR 差值 54.83−54.5，正确）

### 4. 编译结果

`latexmk -pdf main.tex` 成功，输出 16 页 PDF，无错误无警告。

---
