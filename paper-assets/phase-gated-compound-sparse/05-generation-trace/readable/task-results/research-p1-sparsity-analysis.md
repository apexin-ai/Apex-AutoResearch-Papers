# research p1 sparsity analysis

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_p1-sparsity-analysis_20260513T200011_result.json`
- **Structured JSON:** [`e60208a28d7a43c7e987.json`](../../sessions/e6/e60208a28d7a43c7e987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/m1_phase_segmentation_analysis.md`。核心发现：

---

**Phase Segmentation 质量**
- **82% (41/50) 样本 KDE 失败**，需 halved-bandwidth fallback 才能找到 2 个 minima
- Token 分布极度失衡：execution 1.2%, reasoning 8.1%, **transition 90.7%**

**根因**
问题不在 bandwidth 参数，而在 **tri-modal 假设本身不成立**。DeepSeek-R1-Distill-Qwen-7B 在 MATH 生成中的 attention sparsity 分布本质上是 **unimodal**（集中在高 sparsity 区域）。82% 的 KDE 失败 + 90.7% token 归为同一类 = 分布中不存在 3 个清晰模态。Halved bandwidth 找到的 "minima" 是密度估计的噪声波动，不是真实的模态分界。

**P1 判定：需要 pivot**
调 bandwidth 无法修复。建议方向：
1. **GMM + BIC** 自动选模态数，正式确认分布形态
2. **Per-layer sparsity** 分析（当前是跨 head 平均，可能掩盖了 layer-wise 结构）
3. 如果确认 unimodal，放弃离散 phase 分类，转向 token-level adaptive sparsity

**建议下一步**：对 5–10 个样本 dump 原始 sparsity 数组 + per-layer 分解，做直方图和 GMM fit，正式确认是否存在任何层级的 multi-modality。

---
