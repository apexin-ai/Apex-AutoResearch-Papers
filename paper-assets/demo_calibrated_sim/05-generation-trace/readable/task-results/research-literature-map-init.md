# research literature map init

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-map-init_20260512T102744_result.json`
- **Structured JSON:** [`35c49b6f33ecf90d3bb5.json`](../../sessions/35/35c49b6f33ecf90d3bb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/literature_map.yaml`，共 20 篇论文：

| 类别 | 数量 | 关键论文 |
|------|------|---------|
| direct-competitor | **0** | 未找到——验证项目新颖性 |
| foundation | 4 | Seshadri 2026 (Lost in Simulation), τ-bench, AgentBench, MINT |
| method-component | 7 | DPO, Calibrate Before Use, Consistent Personas (RL), User LMs, Persona Catch, Alignment Survey |
| evaluation | 5 | ReDial (AAVE), DialectBench, BBQ, Bias Survey, Dialect vs Demographics |
| background | 5 | Dialect NLP Survey, Rickford AAVE, Kachru Indian English, DAUS, User Diversity |

关键发现：
- **Seshadri 2026** 是最核心的前序工作（记录了问题），但原文标题是 "Lost in Simulation" 而非 "AFAA"，发表于 arXiv 2601.17087，尚未确认被 ICLR 2026 接收
- **无直接竞品**做"校准用户模拟器方言行为率"，DemoCalib 的 BCP + DPO 方案有明确的新颖性空间
- 最接近的是 Haq & Saldias 2026 (Dialect vs Demographics)，但他们只量化偏差机制，不提出校准方法

---
