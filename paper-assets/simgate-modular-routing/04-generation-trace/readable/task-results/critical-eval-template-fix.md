# critical eval template fix

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_eval-template-fix_20260515T152346_result.json`
- **Structured JSON:** [`9a4ff2451797a442cbb7.json`](../../sessions/9a/9a4ff2451797a442cbb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

---

**根因不是 eval template mismatch，而是 checkpoint mismatch。**

- **0.5761**：来自 `plan-004-implicit/final_adapter`（gradient_accumulation=8，正确配置）
- **0.4278**：来自 `plan-004-v5/final_adapter`（gradient_accumulation=1，05-14 脚本被意外修改导致的 bug）
- **enable_thinking 对 plan-004-v5 无影响**：thinking_on=0.4148, thinking_off=0.4148
- **修复后在正确 checkpoint 上评估**：balanced_acc=0.5685（接近 0.5761，差异来自采样随机性）

已完成：
1. `eval_routing_metrics.py` 中 `enable_thinking=False` 已移除（备份在 `.bak_pre_fix`）
2. 在 `plan-004-implicit` 上重新评估并保存到 `results/eval-template-fix/`
3. 论文数字可信，但 reviewer 需要使用 `plan-004-implicit` 而不是 `plan-004-v5` 来复现

---
