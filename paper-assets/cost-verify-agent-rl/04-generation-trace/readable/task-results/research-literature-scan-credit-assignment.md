# research literature scan credit assignment

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan-credit-assignment_20260517T114427_result.json`
- **Structured JSON:** [`d626a93569698acaad2c.json`](../../sessions/d6/d626a93569698acaad2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已保存至 `artifacts/literature_scan_credit_assignment_20260517.md`。

---

## 核心发现

**发现 6 篇高威胁直接竞争者**，领域极度活跃。

### 高威胁竞争者

| 论文 | 日期 | 核心 |
|------|------|------|
| **MT-GRPO** (2505.11821) | 2025-05 | GRPO + turn-level reward/advantage，ICML/NeurIPS 2025 |
| **GiGPO** (2505.10978) | 2025-05 | 两级 grouping: episode-macro + step-micro，NeurIPS 2025 |
| **Turn-PPO** (2512.17008) | 2025-12 | 分析 GRPO multi-turn instability，turn-level PPO critic |
| **HiPER** (2602.16165) | 2026-02 | Hierarchical plan-execute + hierarchical advantage |
| **HCAPO** (2603.08754) | 2026-03 | LLM hindsight critic，诊断 GRPO step-level Q-value 不准 |
| **GAGPO** (2605.13217) | 2026-05 | Critic-free step-level TD/GAE via rollout grouping |

### 差异化空间

主流方向是 **"episode-level 太粗，需要更细的 step/turn-level credit assignment"**。几乎所有竞争者都在改进 step-level。

**本项目的 contrarian position**（step-level 在特定条件下反而有害，episode-level 可以更好）与主流相反，仍有独特贡献空间。arXiv 2604.02869 的发现（naive dense per-turn rewards 降低 14pp 性能）可作为支撑。

关键是需要清晰 positioning：我们不是提出又一个 step-level 改进方案，而是论证何时 step-level 引入的 noise 大于 signal。

---
