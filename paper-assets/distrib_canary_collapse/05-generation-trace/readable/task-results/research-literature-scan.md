# research literature scan

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260514T145431_result.json`
- **Structured JSON:** [`915399adfe256bc21c88.json`](../../sessions/91/915399adfe256bc21c88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/literature_scan_20260514.md`。

**核心发现**：

- **Novelty 安全**：无人将 Granger causality 用于 collapse metric 的 lead-lag 分析，也无人构建多指标 canary panel。这两个仍是我们的独有贡献。
- **最直接竞争者**仍是 chen2025scales（2510.05133），观察到 ECE 先于 accuracy 退化但无因果量化。
- **需注意的理论约束**：Truong & Truong（2512.12381）证明 entropy collapse 是一阶相变，在剧烈 collapse regime 下 canary early warning 可能失效——这解释了我们 100% synthetic 下 canary 无法 lead perplexity 的观察，论文需讨论此局限。
- 共收录 18 篇论文，按 competitor / background / mitigation 分类，附引用优先级建议。

---
