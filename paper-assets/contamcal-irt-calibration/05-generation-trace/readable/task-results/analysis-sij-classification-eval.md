# analysis sij classification eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sij-classification-eval_20260521T162227_result.json`
- **Structured JSON:** [`90076e73f1f497941c33.json`](../../sessions/90/90076e73f1f497941c33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果摘要：

**14 个模型 × 3 benchmark × 2 dosage，每组 7 个模型取均值±std：**

| Signal | d005 ROC-AUC | d025 ROC-AUC | 
|---|---|---|
| **Embedding (s1)** | **0.93–0.99** | **0.91–0.98** |
| RRF (fused) | 0.84–0.93 | 0.73–0.81 |
| Min-K++ (s2) | 0.47–0.50 | 0.48–0.49 |
| Self-Critique (s4) | 0.47–0.51 | 0.50–0.50 |

**核心发现：**

1. **Embedding 信号单独就极强**：GSM8K 上 ROC-AUC=0.991 (d005) / 0.983 (d025)，ARC 上 0.959 / 0.952，MMLU 上 0.934 / 0.905
2. **RRF 融合反而降低了性能**：因为 Min-K++ 和 Self-Critique 接近随机（AUC≈0.5），融合稀释了 Embedding 的强信号
3. **Min-K++ 和 Self-Critique 在 item-level 分类上没有区分力**（AUC≈0.5），但它们在 IRT 模型中可能通过其他机制（如 respondent-level 聚合）贡献信息
4. 结果跨模型族（Qwen-0.5B/1.5B/3B, Llama-3B）和种子高度一致（std 很小）

输出文件：
- CSV/JSON/ROC PDF 在服务器 `/root/contamcal-irt-calibration/analysis/sij_classification/`
- 本地 artifact 已注册

---
