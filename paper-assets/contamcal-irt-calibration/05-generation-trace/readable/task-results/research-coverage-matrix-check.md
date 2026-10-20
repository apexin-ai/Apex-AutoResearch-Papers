# research coverage matrix check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_coverage-matrix-check_20260515T181432_result.json`
- **Structured JSON:** [`3b2137403cc34e24e3df.json`](../../sessions/3b/3b2137403cc34e24e3df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存并注册 (`art_20260515_4a4c8e`)。核心结论：

**Claim 覆盖状态**：
- **Claim 1 (Characterization)** 🟡 — 0.5B+1.5B 数据完整，3B alpha=32 重跑是唯一缺口（4个SFT在跑，~12h完成）
- **Claim 2 (Signal Failure)** 🟡 — Min-K++ reversal 数据充足，但 3B signals (exp-002) 还未成功跑过
- **Claim 3 (Identifiability)** 🟡 — D056 已确认 coverage collapse = model misspecification，sim sweep 接近完成，Fisher Info 推导需写
- **Claim 4 (Calibration)** 🔴 — 缺口最大：pooled IRT 需重跑，7个 baselines 未正式比较

**真正的瓶颈是论文写作（7天窗口）**，不是实验。建议立即开始用 0.5B+1.5B 现有数据写 intro/method/related work，3B 结果到了再补 results。

**可以砍的**：RL proxy (exp-008)、0.5B d025 重试、HumanEval、oracle matched N=8 重跑。

---
