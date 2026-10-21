# research related work followup

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_followup_20260523T032252_result.json`
- **Structured JSON:** [`2af5a443f1ab9910fa6e.json`](../../sessions/2a/2af5a443f1ab9910fa6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完成。关键发现：

1. **AEGIS 深度核查**：
   - CAR 定义与我们一致（episode-level binary, obstacle displacement），但无明确阈值
   - **重要修正**：此前 50.88% 被误认为 Pi0.5 的 obstacle avoidance rate，实际是 task success rate；Pi0.5 CAR = 18.69%（我们 26.8%，反而更高）
   - AEGIS **完全没有 fake safety 分析**，强力支持 Claim 1
   - CBF 修正纯推理时，需 RGB-D + 点云，计算开销仅 0.356ms

2. **引用验证**：3 篇全部 ✅ 通过（CoFreeVLA / CompliantVLA-adaptor / VLA Safety Survey）

3. **补充文献**：新增 5 篇引用 — Goodhart's Law in RL（理论支撑 fake safety）、SB-TRPO（safe RL degenerate policy 直接证据）、VLA benchmark evaluation、ICML 2024 negative results position paper、ICBINB workshop series

所有内容已追加到 `artifacts/related_work_survey.md`。

---
