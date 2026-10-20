# diagnosis anon repo integrity

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_anon-repo-integrity_20260523T185759_result.json`
- **Structured JSON:** [`347b7e71ddbc72dfb74e.json`](../../sessions/34/347b7e71ddbc72dfb74e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/anon_repo_diff.md`。核心结论：

- **核心源码 100% 覆盖**：`analysis/`、`data/`、`eval/`、`rewards/`、`training/` 所有模块完整映射到 `freige/` 包下
- **configs 和 tests 完全一致**
- **匿名仓库合理新增**：`README.md`、`requirements.txt`
- **匿名仓库合理精简**：~70 个实验/分析/可视化脚本未包含（d102、d112、plan010、plan017、seed_expansion 等实验批次脚本），保留了 8 个核心脚本
- **需关注**：服务器上存在 `freige/freige/` 嵌套副本（残留），建议清理

---
