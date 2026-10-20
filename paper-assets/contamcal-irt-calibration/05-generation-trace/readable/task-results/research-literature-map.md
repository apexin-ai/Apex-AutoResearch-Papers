# research literature map

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-map_20260516T041853_result.json`
- **Structured JSON:** [`393af760633605c48a3f.json`](../../sessions/39/393af760633605c48a3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`literature_map.yaml` 已创建，包含 25 篇论文，覆盖 6 个类别。

关键发现：
- **paper_framing.md 中 4 处引用信息有误**，已在 YAML 末尾注释中标注：
  - "Lalor et al., AAAI 2024" → 实际是 EACL 2024 Tutorial
  - "ATLAS (Baffour et al., 2024)" → 实际作者是 Li et al.（arxiv 2511.04689）
  - "PSN-IRT (Yao et al., 2024)" → 实际是 Zhou et al., AAAI 2026（arxiv 2505.15055）
  - "DCR (Dekoninck et al., EMNLP 2025)" → 实际 DCR 作者是 Xu et al.（Dekoninck 是 ConStat 作者）

- **Eckerly 2017** 是 Routledge 书籍章节，无直接 arxiv URL，标记 `verified: false`

分布：detection 8篇、irt-llm 7篇、item-compromise 3篇、calibration 4篇、mitigation 2篇、benchmark 2篇。所有 arxiv URL 均已验证。

---
