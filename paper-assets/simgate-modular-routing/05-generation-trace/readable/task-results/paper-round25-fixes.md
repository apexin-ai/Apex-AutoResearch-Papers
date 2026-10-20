# paper round25 fixes

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round25-fixes_20260521T152722_result.json`
- **Structured JSON:** [`35a59be3b3d18a76c9ff.json`](../../sessions/35/35a59be3b3d18a76c9ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Clean build 成功，0 个 undefined citation，总 25 页（含 appendix）。

---

## 汇报

### P0 — 零成本词汇替换
- **P0-a**: abstract.tex — "This finding is penalty-independent: a derived" → "This label fraction is penalty-independent. A derived"
- **P0-b**: abstract.tex — "demonstrating the framework's generality" → "illustrating the framework's applicability"
- **P0-c**: conclusion.tex — "confirm generality" → "illustrate applicability"
- **Page 8**: OK（[9] 在 main.bbl）

### P1 — Conclusion 扩展
- 在 Conclusion 末尾添加 future work 句："Future work should validate death dominance in additional catastrophic-failure environments and develop routing methods that exploit task-type-level signals."
- **Page 8**: OK

### P2 — Related Work 调整
- **P2-a**: Tool Use 段 4 个分类从 4 句详述（5 行）压缩为 1 句整合（2 行），保留段首句和段尾不变
- **P2-b**: Safe RL 段在 "Our routing achieves safety..." 前插入 2 句 CMDP 对比论述，将原文改写为更完整的 positioning
- **Page 8**: OK

### P3 — Contribution 微调
- Contribution (2) 添加 exploratory router 提及："an exploratory step-level router confirms this, recovering only task-type classification"，section ref 改为 `\S\ref{sec:death-decomp}--\ref{sec:router-diagnostic}`
- **Page 8**: OK

### Safe — 格式清理
- **S1**: 8 个 orphan bib entries 全部未被引用，已删除：`balrog-2025`, `crafter-2022`, `crpo-2021`, `minihack-2021`, `nethack-2020`, `netplay-2024`, `tamar2015cvar`, `zhou2024webarena`
- **S2-SALT**: 已在论文中引用 (`salt-2026`)，跳过
- **S2-Agent-SafetyBench**: 找到真实论文 (arXiv:2412.14470, Zhang et al.)，已添加 bib entry 并在 Safe RL 段末尾加 `\citep{agent-safetybench-2024}`
- **S3-Webb**: 确认为 2023 年，Canadian Journal of Economics, Volume 56, Number 3, pages 839–858。bib 中 `webb-2023` 记录完全正确，无需修改

### 最终状态
- Conclusion 结束在 page 8，[9] 起始于 main.bbl（参考文献）
- 总页数 25（含 appendix）
- 0 个 undefined citation

---
