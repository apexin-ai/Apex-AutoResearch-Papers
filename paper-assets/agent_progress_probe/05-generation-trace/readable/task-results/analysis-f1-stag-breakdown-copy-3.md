# analysis f1 stag breakdown

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f1-stag-breakdown_20260514T183122_result.json`
- **Structured JSON:** [`7cfbea2be338060e9c21.json`](../../sessions/7c/7cfbea2be338060e9c21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到服务器 (`analysis_f1_stag_breakdown.md`) 并注册为 artifact。

---

**核心结论：**

1. **outcome-bp-3seed per-class breakdown**：f1_stag 在三个 seed 间为 0.600 / 0.640 / 0.683（mean 0.641±0.034），与 registry 一致。主要瓶颈是 recall_stag 低（0.44–0.58），precision_stag 反而高（0.83–0.93）——模型保守预测 stagnation，漏检多。

2. **0.000 溯源**：搜遍了 registry、日志、所有结果 JSON 和 artifacts，**没有任何已记录的实验产出 f1_stag=0.000**。最接近的是 OB-only 子集上的 0.5109。0.000 是非正式讨论中对低性能的夸大，D025/D026 已正确撤回。

3. **论文推荐**：使用 outcome-bp-3seed 的 mean±std（macro_f1=0.770±0.018, f1_stag=0.641±0.034），与 full baseline 的 Δ 为 −7.7pp / −13.6pp。

---
