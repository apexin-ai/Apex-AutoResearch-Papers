# research paper research

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-research_20260515T020141_result.json`
- **Structured JSON:** [`2b2188951c3a70f766f3.json`](../../sessions/2b/2b2188951c3a70f766f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献扫描完成。报告已写入 `artifacts/literature_scan_20260515.md`。

核心结论：

1. **无直接竞争者。** 没有人在做"递归生成深度/代数检测"。二分类检测（human vs AI）和来源归因（哪个模型）很拥挤，但序数深度回归仍是空白。

2. **最相关的方法工作：**
   - **DivEye** (TMLR/ICLR 2026) — surprisal 多样性特征，与我们的特征空间高度重叠，应作为 baseline 引用
   - **Breaking the Generator Barrier** (Apr 2026) — generator-agnostic 检测思路，可借鉴其解耦框架
   - **Why Detection Fails** (Mar 2026) — 检测特征在 domain shift 下严重退化，**对我们是重要警示**

3. **模型坍塌理论的新进展：**
   - **From Collapse to Improvement** (Feb 2026) — 混合真实数据时，迭代训练可以改善而非退化，意味着我们的深度信号可能**非单调**
   - **Curated Synthetic Data Doesn't Collapse** (May 2026) — 精心 curate 的递归训练不坍塌，这是我们方法的 hard case

4. **Knowledge Collapse** (Sep 2025) 指出表面流畅度在各深度保持不变，事实准确性才退化 — 建议考虑加入事实一致性特征。

---
