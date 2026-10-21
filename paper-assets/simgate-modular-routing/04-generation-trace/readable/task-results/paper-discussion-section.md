# paper discussion section

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_discussion-section_20260515T101438_result.json`
- **Structured JSON:** [`a8a76fff7f2ad49ad304.json`](../../sessions/a8/a8a76fff7f2ad49ad304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Discussion section 扩写完成。从 2 段扩展为 5 段：

1. **Cross-environment evidence** — 保留原文不动
2. **Implications for router design** — 新增。Router 本质上是 safety critic 而非 efficiency optimizer，与 safe RL 文献关联，提出 death predictor 作为更简单的替代
3. **Label imbalance as a core finding** — 新增。86:9 的极端分布是核心发现而非缺陷，解释 always-det 为何是 strong baseline，router marginal value 仅限于 ~4% 的 internal-preferred episodes，引用 concurrent work (when2tool, tool-use-tax)
4. **Penalty sensitivity and generalization** — 新增。DAF 随 penalty 量级变化 (46%→95%)，低 penalty 环境中 non-death signal 更重要，capability-dependent 假说 (更强模型死亡率更低→DAF 可能下降)
5. **Scope and future directions** — 扩展原文，新增 logit-generation gap 限制和 multi-model/multi-scale validation

---
