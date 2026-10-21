# analysis plan008 ppl consolidation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan008_ppl_consolidation_20260516T025552_result.json`
- **Structured JSON:** [`a02f7e46ca2248fdd36f.json`](../../sessions/a0/a02f7e46ca2248fdd36f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/plan008_ppl_summary.md` 并注册为 artifact（`save_project_file` 不支持该文件名，但本地文件和 artifact 注册均成功）。

核心发现：

1. **KL 退化近似 quadratic**（70%/30% ratio = 4.12×），training-free 退化为指数级（TEAL 19.4×, WINA 24.6×）
2. **KL vs TEAL delta 从 30%→70% 增长 41.3×**，KL 优势在高稀疏度急剧放大（18%→49%→82%）
3. **Downstream 全面崩溃**，PPL-downstream disconnect 在 30% 和 50% 均成立
4. **Claim 3 数据缺口**：KL vs BCE scaling 只有 50% 单点，无法验证 quadratic 预测。建议补 BCE 30%/70%，否则将 Claim 3 重新聚焦为 "KL vs training-free scaling"

---
