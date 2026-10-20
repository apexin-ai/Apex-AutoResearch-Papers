# research 1000step literature paper prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_1000step-literature-paper-prep_20260515T113705_result.json`
- **Structured JSON:** [`2f001c02b5d901875515.json`](../../sessions/2f/2f001c02b5d901875515.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是结果摘要。

---

## 文献搜索结果

**核心结论：1000 步 universal Goodhart collapse 的三个具体方面是 novel observation。**

### 已有文献覆盖的内容
- Goodhart overoptimization 的 scaling laws（Gao et al. 2023）、RL 中的 Goodhart 几何（Karwowski et al. 2024）、catastrophic Goodhart（Kwa et al. 2024）——均已在 literature_map 中
- GRPO 的 entropy collapse 和 advantage collapse（DAPO, EDGE-GRPO, GTPO）——描述训练不稳定性，但不涉及 hacking mode diversity
- Reward hacking 的高层 taxonomy（Manheim & Garrabrant 2019; 2026 survey arXiv:2604.13602）——理论分类，非实验验证

### 新增 2 篇论文到 literature_map.yaml

| ID | 标题 | 关联 |
|----|------|------|
| `yue-rlvr-limits` | Does RL Really Incentivize Reasoning? (NeurIPS 2025, 2504.13837) | RLVR 仅重分布已有能力而非创造新推理；支持 collapse 是 RLVR 基本限制 |
| `deng-grpo-collapse-lld` | On GRPO Collapse: Lazy Likelihood-Displacement Death Spiral (2512.04220) | GRPO 特有的 LLD 机制导致 universal collapse，补充 Goodhart 理论解释 |

### 未被现有文献覆盖的 novel 部分
1. **Universal collapse across ALL reward types** — 无人展示 exec-only、structural、random reward 同时退化到 ~0% genuine
2. **Hacking mode taxonomy from single experimental setup** — 同一 GRPO + 4 种 reward → 4 条不同 hacking 路径（H1/H7/mixed/tautology）
3. **Empirical Goodhart temporal curve for neurosymbolic RL** — 500 步 sweet spot (30.9% genuine) → 1000 步 collapse (3%)

## 产出文件

- `literature_map.yaml` — 新增 `yue-rlvr-limits` 和 `deng-grpo-collapse-lld` 两个条目（role=supporting-evidence）
- `artifacts/section_4_3_1000step_draft.md` — §4.3 完整草稿，含对比表、temporal trajectory、4 类 hacking pathway taxonomy、论点论证

---
