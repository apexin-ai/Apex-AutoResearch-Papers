# research hcapo alfworld

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_hcapo_alfworld_20260523T170547_result.json`
- **Structured JSON:** [`7ccc556ac2937daca949.json`](../../sessions/7c/7ccc556ac2937daca949.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析已写入 `artifacts/hcapo_analysis.md`。核心发现：

**HCAPO**: 91.4% ALFWorld (7B)，+13.8% over GRPO。用 LLM 自身做 hindsight critic 计算 per-step Q-value，composite advantage = episode-level + hindsight-weighted step-level。但仍用 **2-step lookback 窗口化上下文**。

**GiGPO**: 90.2-90.8% ALFWorld (7B)，anchor state grouping 做 step-level advantage。同样用 history length 2。

**Turn-PPO**: 无 ALFWorld 结果，只有 WebShop 和 Sokoban。

**诊断框架分析**:
- **M1**: HCAPO 和 GiGPO 均未解决。两者都用窗口化上下文，策略端仍有信息损失
- **M2**: HCAPO 直接解决（hindsight credit assignment），GiGPO 部分解决（anchor state grouping）
- **差异化空间**: 目前所有竞品都不解决 M1。如果我们同时解决 M1+M2，在长序列/早期上下文关键的任务上有明确优势
- **风险**: HCAPO 在 ALFWorld 已达 91.4%（smoothing 后 96.9%），bar 很高。需要在更难的任务上证明 M1 的约束性

---
