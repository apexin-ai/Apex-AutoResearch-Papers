# research literature scan

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260515T042525_result.json`
- **Structured JSON:** [`8bbce7fc1f8ad9d3591e.json`](../../sessions/8b/8bbce7fc1f8ad9d3591e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已更新。文献扫描结果：

**目标窗口（2026-05-01 至 2026-05-15）内找到 4 篇新论文，均为 orthogonal 或 complementary，无直接竞争者。**

| 论文 | arXiv ID | 关系 |
|------|----------|------|
| Du & Tanaka-Ishii — Geometric Mode Collapse | 2605.00435 | orthogonal（推理时 mode collapse，非迭代训练） |
| Gauthier, Bach & Jordan — Alignment Collapse in RLHF | 2605.04266 | complementary（反馈环路结构类似） |
| Shi et al. — Layer-Pruned LLM Collapse | 2605.07271 | orthogonal（架构剪枝 collapse） |
| Tübingen — Layer Collapse in Diffusion LMs | 2605.06366 | orthogonal（diffusion LM activation collapse） |

**核心结论**：过去 2 周无人发表 canary → collapse prediction 的 lead-lag/Granger causality 分析。我们的 novelty（多指标 canary panel + 因果分析框架）仍然安全。chen2025scales 仍是最接近的竞争者且无更新。

`literature_map.yaml` 不可通过 save_project_file 直接写入——如果需要将 Du & Tanaka-Ishii (2605.00435) 和 Gauthier et al. (2605.04266) 加入 literature_map，需要用专用工具或手动更新。

---
