# research crossing rate literature

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_crossing_rate_literature_20260520T045810_result.json`
- **Structured JSON:** [`13b39b4b346bb6663ccb.json`](../../sessions/13/13b39b4b346bb6663ccb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成，保存在 `artifacts/crossing_rate_literature_survey.md`。

## 核心结论

**CR 作为精确定义的 metric 是新颖的**——42 组关键词、~117 篇论文中无人定义过 "跨层 probe 预测翻转计数"。但这不是 straw man，因为：

### 最强反驳证据

1. **Kaya et al. (ICML 2019)** — "overthinking" + confusion metric 已识别跨层预测翻转问题，但未形式化为评估指标
2. **PABEE (NeurIPS 2020)** — 直接用跨层预测一致性作为 early exit 判据，证明这个信号有实际价值
3. **Miller & Blume (2026)** — 独立提出 Decision Flip Rate (eDFR)，概念上等价于 CR（只是在不同轴上计数翻转）
4. **Keoliya et al. (2025)** — 提出惩罚振荡的 stability metric，发现 "existing methods struggle to jointly optimize accuracy and stability"
5. **Wildi (2026)** — 在计量经济学中显式连接 sign accuracy 和 zero-crossing rate，数学上与 CR-composite 分解完全平行

### 建议 framing

不要说 "别人也用 CR"，而是说：
- CR 形式化了已被观察到但未被量化的现象（overthinking, cross-layer disagreement）
- CR 是 online safety monitoring 场景的自然需求（SafeSwitch, TrajGuard 等系统需要稳定的监控信号）
- CR 是 ZCR / eDFR / Lipschitz stability 这类既有概念在新领域的实例化

---
