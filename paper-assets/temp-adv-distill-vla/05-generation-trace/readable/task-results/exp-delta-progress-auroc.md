# exp delta progress auroc

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_delta-progress-auroc_20260515T093158_result.json`
- **Structured JSON:** [`2226f5103b54983a56bb.json`](../../sessions/22/2226f5103b54983a56bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### Δprogress 指标（10 任务明细）

| Task | Δprogress AUROC | Δprogress IQR | Δprogress Spearman ρ |
|------|:-:|:-:|:-:|
| alphabet_soup | 0.5584 | 0.0091 | 0.0403 |
| bbq_sauce | 0.4940 | 0.0105 | -0.0046 |
| butter | 0.5483 | 0.0090 | 0.0237 |
| chocolate_pudding | 0.5570 | 0.0092 | 0.0353 |
| cream_cheese | 0.5361 | 0.0116 | 0.0283 |
| ketchup | 0.5404 | 0.0111 | 0.0249 |
| milk | 0.5164 | 0.0104 | 0.0084 |
| orange_juice | 0.5224 | 0.0112 | 0.0145 |
| salad_dressing | 0.5094 | 0.0116 | 0.0061 |
| tomato_sauce | 0.5426 | 0.0104 | 0.0315 |
| **MEAN** | **0.5325** | **0.0104** | **0.0208** |

### 修正后 baseline（10 任务明细）

| Task | SAL AUROC (correct: +arc_len) | TED AUROC | SAL AUROC (old bug: -arc_len in gate2_results.json) |
|------|:-:|:-:|:-:|
| alphabet_soup | 0.9961 | 0.6987 | 0.0039 |
| bbq_sauce | 0.9945 | 0.6345 | 0.0055 |
| butter | 0.9926 | 0.5563 | 0.0074 |
| chocolate_pudding | 0.9965 | 0.5948 | 0.0035 |
| cream_cheese | 0.9941 | 0.6916 | 0.0059 |
| ketchup | 0.9964 | 0.6284 | 0.0036 |
| milk | 0.9946 | 0.5940 | 0.0054 |
| orange_juice | 0.9937 | 0.6151 | 0.0063 |
| salad_dressing | 0.9955 | 0.5782 | 0.0045 |
| tomato_sauce | 0.9906 | 0.6003 | 0.0094 |
| **MEAN** | **0.9945** | **0.6192** | **0.0055** |

### SAL bug 修复详情

- **代码现状**：`gate2_evaluation.py` 中 `compute_sal()` 已经是 `sal_scores[t] = arc_lengths`（正号），**代码本身无需修改**
- **gate2_results.json 中的陈旧数据**：SAL AUROC ≈ 0.005 是用旧版代码（`-arc_lengths`）生成的，与当前代码不一致
- **修复前 SAL AUROC**（gate2_results.json 中的值）：mean = 0.0055
- **修复后 SAL AUROC**（用当前正确代码重算）：mean = 0.9945
- SAL 用正号 arc_length 后几乎是 perfect separator（FFT 弧长直接区分了动/不动）

### 对比总结

| 指标 | Mean AUROC |
|------|:-:|
| SAL (correct) | **0.9945** |
| TED | 0.6192 |
| Δprogress | 0.5325 |
| raw progress | 0.5180 |

- **Δprogress 在所有 10 个任务上均输给 TED（0/10 wins）**
- Δprogress 仅略高于随机（0.53 vs 0.50），IQR 极小（~0.01），Spearman ρ 接近 0
- 原因：MLP 预测的 progress 是平滑单调递增的 t/T，差分 Δprogress ≈ 常数（每步约 +0.006），对 no-op/progress 几乎无区分力
- 正确签名的 SAL 是近乎完美的 no-op 检测器（AUROC=0.995），远超所有其他指标

### 关键文件路径

- 评估脚本：`/root/temp-adv-distill-vla/delta_progress_evaluation.py`
- 输出 JSON：`/root/temp-adv-distill-vla/artifacts/delta_progress_results.json`
- MLP checkpoint：`/root/temp-adv-distill-vla/artifacts/gate1b_mlp_multitask.pt`
- gate2 代码（SAL 已正确）：`/root/temp-adv-distill-vla/gate2_evaluation.py`

---
