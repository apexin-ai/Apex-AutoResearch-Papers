# research literature gap check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-gap-check_20260514T185805_result.json`
- **Structured JSON:** [`0e6a5f6ffde1ce59f96d.json`](../../sessions/0e/0e6a5f6ffde1ce59f96d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**更新总结**：

**新增 10 篇论文**（45→55），填补 5 个 gap：

1. **时间离散化理论**（关键 gap）— Tallec 2019 (ICML), Park 2021 (NeurIPS), Wang 2024: 为"variable dt 在 world model RL 中为何失败"提供理论基础
2. **诊断方法论**— Engstrom 2020 (ICLR), Andrychowicz 2021 (ICLR): 为 factorial diagnostic analysis 提供方法论先例
3. **Delusional bias 后续**— Su 2020 ConQUR (ICML): 补全 Lu 2018 → ConQUR → 我们的 MBRL 新实例链条
4. **MBRL rollout 质量**（关键 gap）— Frauenknecht 2025 (ICLR), Voelcker 2025 MAD-TD (ICLR): 最新 ICLR 2025 工作，直接支撑我们的发现并提供差异化定位
5. **Dreamer 最新进展 + 动作重复**— Hafner 2025 DreamerV4, Nie 2025 SDAR (ICLR): 确保覆盖最新架构演进

所有新增论文均有真实 arXiv ID 或会议引用。Gap 分析报告在 `artifacts/literature_gap_analysis_20260514.md`。

---
