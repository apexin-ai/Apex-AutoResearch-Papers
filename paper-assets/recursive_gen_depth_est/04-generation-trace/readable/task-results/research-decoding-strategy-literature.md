# research decoding strategy literature

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_decoding_strategy_literature_20260515T020238_result.json`
- **Structured JSON:** [`aa9fbfa0ae7351f9b496.json`](../../sessions/aa/aa9fbfa0ae7351f9b496.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成文献调研，写入 memory.md。总结：

**新颖性：partially-known**

已知部分：解码策略效应的模型/任务依赖性已有文献支撑（Garces Arias COLING 2025 直接证实最优配置因模型而异；Wiher TACL 2022 证实任务依赖性）。Top-k 一致最弱也与 Holtzman ICLR 2020 的发现一致。

**我们的独特贡献**：
- 无论文研究解码策略如何影响递归生成深度的**可检测性**
- 具体的交互模式（temp-only 对 GPT-2 XL/OLMo 增强信号但对 Pythia 削弱）未被报告过
- 将 model collapse 文献（Shumailov Nature 2024）中的 temperature 效应扩展到深度信号检测场景

**建议补充 literature_map.yaml 的条目**（5篇）：

| 论文 | Venue | 与我们的关系 |
|------|-------|-------------|
| Garces Arias et al. "Decoding Decoded" | COLING 2025 | 支持：模型依赖效应 |
| Wiher et al. "On Decoding Strategies" | TACL 2022 | 补充：任务依赖效应 |
| Holtzman et al. "Neural Text Degeneration" | ICLR 2020 | 支持：top-k 最弱 |
| Shumailov et al. "Model Collapse" | Nature 2024 | 补充：递归生成+temperature |
| Basu et al. "Mirostat" | ICLR 2021 | 补充：k vs p 非线性机制 |

---
