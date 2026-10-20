# research literature scan pre submission

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan-pre-submission_20260515T132856_result.json`
- **Structured JSON:** [`16b6256e95a156c631c1.json`](../../sessions/16/16b6256e95a156c631c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成。结论：

**无高威胁竞品。** 16 组搜索查询，新增 10 篇论文（总计 26 篇），VOTA 的核心位置安全。

**2 篇中等威胁**，均来自 patch correctness prediction 方向：
- **LLM4PatchCorrect** (TSE 2024) — 用 execution trace + test case 做 patch 正确性评估，但用 zero-shot prompting 而非 SFT，且不做 trace compression
- **APSG + Graph-LoRA** (arXiv 2025) — PEFT + 图结构做 patch correctness，但用静态代码图而非 runtime trace signal

**关键 differentiation**：两者都没有发现 fault indicator signals（exception + assertion comparison）是近完美判别信号，也没有做 decision-relevant trace compression。VOTA 的三个独特贡献点（fault indicator signal discovery、verdict-oriented trace abstraction、cross-model generalization）均无直接竞品。

**建议引用新增**：LLM4PatchCorrect、REval、CodeMind、FuseFL、CRUXEval-X、InspectCoder。

报告和更新后的 `literature_map.yaml` 已就绪。

---
