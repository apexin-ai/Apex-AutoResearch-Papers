# code round7 seed level stats

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_round7-seed-level-stats_20260521T073134_result.json`
- **Structured JSON:** [`29fe3e8d6126e1227193.json`](../../sessions/29/29fe3e8d6126e1227193.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是结果摘要：

---

## Task 1: Per-seed F1 (full turn)

| Variant | DD s42 | DD s123 | DD s456 | AA s42 | AA s123 | AA s456 | FITD s42 | FITD s123 | FITD s456 |
|---------|--------|---------|---------|--------|---------|---------|----------|-----------|-----------|
| 9-Class | 1.000 | 1.000 | 0.990 | 0.990 | 0.935 | 0.990 | 1.000 | 1.000 | 1.000 |
| Binary | 1.000 | 1.000 | 1.000 | 0.981 | 0.990 | 1.000 | -- | -- | -- |
| Scrambled | 0.990 | 1.000 | 1.000 | 0.891 | 0.990 | 0.971 | -- | -- | -- |
| MLM+cls | 1.000 | 0.990 | 0.751 | 0.971 | 0.925 | 0.784 | 0.961 | 0.432 | 0.729 |
| Topic | 0.727 | 0.252 | 0.644 | 0.686 | 0.431 | 0.759 | -- | -- | -- |
| Vanilla | 0.284 | 0.305 | 0.348 | 0.258 | 0.258 | 0.258 | 0.871 | 0.855 | 0.919 |

FITD 数据 Binary/Scrambled/Topic 无评估结果，标 `--`。

## Task 2: Cohen's d (9-class vs Scrambled)

- **DD OOD**: d = **-0.003** (无差异，两者均接近 ceiling ~0.997)
- **AA OOD**: d = **0.587** (中等效应量，9-class 均值 0.972 vs scrambled 均值 0.951)
- n=3, CI 很宽

## Task 3: OOD Recall 关键发现

- **9-class**: attack recall 0.91–1.00, benign recall 1.00 across all OOD
- **Vanilla**: attack recall 仅 0.00–0.04 (DD/AA)，几乎无法检测攻击；benign recall 1.00（全预测 benign）
- **MLM+cls seed456**: attack recall 在 DD 仅 0.64，跨 seed 不稳定
- FITD recall 因 per_sample 与 exp25 数据不一致，vanilla/MLM 标注 N/A

## 产出文件

- **JSON**: `/root/persuasion_turn_jailbreak_detect/results/round7_seed_level_stats.json`
- **LaTeX**: `/root/persuasion_turn_jailbreak_detect/results/round7_seed_table.tex`
- **Script**: `/root/persuasion_turn_jailbreak_detect/scripts/extract_round7_stats.py`

---
