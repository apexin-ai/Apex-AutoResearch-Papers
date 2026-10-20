# train ablation supcon

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ablation-supcon_20260514T161233_result.json`
- **Structured JSON:** [`97653885524d1d36dfdd.json`](../../sessions/97/97653885524d1d36dfdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SupCon 消融实验完成

| λ | macro_f1 | f1_stag | f1_prog | accuracy | sep_ratio |
|---|----------|---------|---------|----------|-----------|
| **0.0 (baseline)** | 0.9055 | 0.8593 | 0.9518 | 0.9282 | 2.87 |
| 0.1 | 0.9063 | 0.8611 | 0.9516 | 0.9282 | 4.43 |
| 0.5 | 0.9076 | 0.8624 | 0.9529 | 0.9298 | 5.01 |
| **1.0** | **0.9326** | **0.9017** | **0.9636** | **0.9468** | **7.49** |

**关键发现**：
- λ=1.0 效果最佳：macro_f1 从 0.9055 → 0.9326 (**+2.71pp**)，f1_stag 从 0.8593 → 0.9017 (**+4.24pp**)
- 分离度随 λ 单调递增：2.87 → 7.49（**2.6x**），SupCon 有效拉开了类间距离
- SupCon 对少数类（stagnation）提升最大，说明 contrastive learning 帮助模型学到更判别性的表示
- λ=0.1/0.5 对 F1 影响微小但分离度已显著提升，λ=1.0 时 F1 和分离度均有质变

实验产出已保存至 `ablation-supcon/` 目录，registry 已更新为 DONE。

---
