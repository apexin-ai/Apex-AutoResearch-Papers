# code verify vanilla aa ood std

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-vanilla-aa-ood-std_20260520T135947_result.json`
- **Structured JSON:** [`9b6f8a33692e966f23d9.json`](../../sessions/9b/9b6f8a33692e966f23d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

## 报告：DeBERTa vanilla AA OOD = 0.258±0.000 的来源

### 1. 0.258 的实际来源

**`exp2_actorattack_ood.json` → variant `vanilla` → `full` metric**，不是 exp16。

论文 `paper/experiments.tex:135` 引用了这个值：
> "DAPT provides ~71pp over both vanilla (0.258) and TF-IDF (0.261)"

以及排序公式（同文件）：
> "TF-IDF (0.26) ≈ vanilla (0.26±0.00) < topic (0.63±0.14) < ..."

### 2. std=0.000 — 算术上正确，但底层数据异常

exp2 vanilla per-seed `full` 原始值：

| Seed | full F1 |
|------|---------|
| 42 | 0.25750696933492634 |
| 123 | 0.25750696933492634 |
| 456 | 0.25750696933492634 |
| **mean** | **0.2575 (≈0.258)** |
| **std** | **0.0** |

三个 seed 的 full F1 **完全相同**，所以 std=0.0 在数学上没错。但早期检测指标 k=1 有差异（0.388 / 0.353 / 0.271），说明 3 个 checkpoint 不同。推测原因：vanilla 模型无 domain adaptation，面对 ActorAttack 全对话时 3 个 seed 都退化到相同的预测模式（几乎全判为同一类），导致 F1 收敛到同一值。

### 3. exp16 的正确 vanilla AA OOD 值

来源：`exp16_balanced_ood_reeval.json` → aggregated → vanilla → aa_ood

| Seed | AA OOD F1 (balanced, n=118) |
|------|---------------------------|
| 42 | 0.346 |
| 123 | 0.330 |
| 456 | 0.492 |
| **mean** | **0.389** |
| **std** | **0.073** |

### 4. 与 0.258 的混淆可能

exp16 的 **MLM** AA OOD 恰好也约等于 0.258：
- per_seed_f1: [0.197, 0.364, 0.213]
- mean = 0.258, std = **0.075**（不是 0.000）

### 结论

| | 值 | 来源 | std |
|--|---|------|-----|
| "0.258±0.000" | exp2 vanilla full | `exp2_actorattack_ood.json` | 0.000（3 seed 退化到相同预测） |
| exp16 vanilla AA OOD (正确) | 0.389±0.073 | `exp16_balanced_ood_reeval.json` | per-seed: 0.346/0.330/0.492 |
| exp16 MLM AA OOD（易混淆） | 0.258±0.075 | `exp16_balanced_ood_reeval.json` | per-seed: 0.197/0.364/0.213 |

**0.258±0.000 来自 exp2（旧实验），不是 exp16 的 vanilla。** 如果论文需要引用 exp16 DeBERTa vanilla 的 AA OOD，正确值是 **0.389±0.073**。

---
