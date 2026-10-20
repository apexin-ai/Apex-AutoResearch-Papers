# research tau sensitivity literature

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tau_sensitivity_literature_20260515T170239_result.json`
- **Structured JSON:** [`e09526a806dc6b76877c.json`](../../sessions/e0/e09526a806dc6b76877c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 artifacts 目录。报告完成。

**核心结果：**

四个方向共筛选 14 篇最相关论文，覆盖 IS clipping (4篇)、α-divergence (3篇)、ESS constraint (3篇)、LLM data quality threshold (3篇) + 1篇 ESS 理论批评。

**综合结论：文献 strongly 支持 Claim 3。** 关键支撑逻辑：
1. **Sweet spot 普遍存在** — FineWeb-Edu 阈值 2-3 均 work、RGD τ=1 跨任务稳定
2. **自适应优于固定** — 我们的 adaptive b* 不依赖固定 clipping，τ 只是优化边界
3. **Dual constraint 降低敏感性** — ESS 约束充当二级保护，类似 Birrell et al. 的正则化降低 α 敏感性
4. **质量-多样性 trade-off** — QuRating/FineWeb-Edu 证实过高阈值破坏覆盖，过低则质量不足

报告路径：`artifacts/literature_tau_sensitivity.md`，包含每篇论文的 key finding、与我们工作的联系、推荐引用列表和 framing 段落。

---
