# research covariate shift literature

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_covariate_shift_literature_20260515T050056_result.json`
- **Structured JSON:** [`d571643e29284f7b93f8.json`](../../sessions/d5/d571643e29284f7b93f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。产出总结：

**文件已写入:**
- `artifacts/covariate_shift_literature_survey.md` — 完整文献调研报告
- `literature_map.yaml` — 11 篇论文的结构化索引

**关键发现:**

| 论文 | 与我们发现的关系 |
|------|-----------------|
| Marchi et al. (ICASSP 2025) | **最强理论支撑** — 证明 T<1 放大概率差异，加速 mode collapse |
| Dohmatob et al. (ICML 2024) | **机制解释** — temperature 产生 "tail narrowing" (q∝i^{-β/T})，不同于 top-k/nucleus 的 "tail cutting" |
| Drayson et al. (EMNLP 2025) | **最强实证** — τ=0.9 在 99 代递归中多样性下降 70%，困惑度退化反而更温和 |
| Shumailov et al. (Nature 2024) | 基础框架，但**未比较采样策略** |

**新颖性评估: partially-known**
- 已知：temperature 加速退化（定性层面）
- **新颖**：①精确量化 ~1 depth 偏移量；②将跨策略差异框架化为协变量偏移；③z-score 标准化修正方法（AUC 0.13→0.68）

---
