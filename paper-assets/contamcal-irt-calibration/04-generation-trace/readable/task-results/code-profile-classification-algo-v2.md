# code profile classification algo v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_profile-classification-algo-v2_20260519T174128_result.json`
- **Structured JSON:** [`52ef10786862bee7e6f9.json`](../../sessions/52/52ef10786862bee7e6f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出：

**1. `profile_classifier.py`** — 独立分类模块，`classify_profile()` 接收 5 个 dosage 精度，返回 pattern + confidence + reasoning。决策树与 bootstrap 脚本的 `classify_vec` 完全一致。

**2. `algorithm1_pseudocode.tex`** — `algorithmic` 环境伪代码，4 个可调参数 (τ=1pp, σ=5pp, ρ=0.3, λ=0.5pp)，可直接 `\input` 到论文。

**3. `classification_criteria.yaml`** — 形式化规格：输入/派生特征/阈值/条件/决策顺序。

**验证结果**（5/5 全部通过）：

| Model | Pattern | Confidence |
|---|---|---|
| Phi-4 | Immune | 0.915 |
| Qwen-14B | U-collapse | 0.937 |
| Qwen-7B | V-recovery | 0.632 |
| Gemma-2 | Benefit | 1.000 |
| OLMo-2 | Benefit-sat | 0.750 |

V-recovery 的 confidence 较低 (0.632) 符合预期——delta 只有 -1.78pp，离 Immune 边界较近，V-dip 幅度不大。这正好说明分类器的 confidence 校准合理。

---
