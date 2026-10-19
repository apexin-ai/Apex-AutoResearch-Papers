# research scienceworld feasibility

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scienceworld-feasibility_20260519T100550_result.json`
- **Structured JSON:** [`51e29f42fd00e6c90009.json`](../../sessions/51/51e29f42fd00e6c90009.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册（`art_20260519_6e4902`）。

**核心结论**：ScienceWorld 可行，且工程量可控（5-6 天）。

关键发现：
- RAGEN ScienceWorld 适配器**已存在**于 westd 服务器，SFT 数据（3000-4000 条轨迹）也已备好
- 主要适配工作是奖励二值化（dense 0-100 → binary）和 dry-run 验证
- 最大风险是 1.7B SFT baseline 可能太弱（需先确认），以及 JVM/py4j 长训练稳定性
- 对论文价值明确：40 步 episode 比 ALFWorld 的 15 步更长，如果 h=2 仍然坍缩，直接证明 information loss 是 environment-agnostic 的
- 已有多篇 2026 论文在 ScienceWorld 上做 RL fine-tuning（EMPO², Paying Less Generalization Tax 等），但**无人研究 step-independent credit assignment**

---
