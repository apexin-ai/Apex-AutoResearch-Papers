# ops fig2 scatter k5 restore

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig2-scatter-k5-restore_20260525T200712_result.json`
- **Structured JSON:** [`4e0945b22169064b6863.json`](../../sessions/4e/4e0945b22169064b6863.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。散点图已生成并 SCP 回本地。

注意：脚本中 POOL_A 的模型名与数据不匹配（原脚本用了 `claude-sonnet-4-6`、`gpt-4.1-mini`、`gemini-3.5-flash`、`gpt-4.1-nano` 这些不存在的名称），已修正为实际的 9 个 API 模型：`claude-opus-4, gpt-5.5, gemini-2.5-pro, gpt-4.1, claude-sonnet-4, gpt-4o, gemini-2.5-flash, gpt-4o-mini, claude-3-haiku`。

结果数值：
- C(15,5) = 3003 panels, Pool A = 126
- K_eff ∈ [2.163, 4.296]
- r_full = 0.81, r_poolA = 0.85

文件已保存至 `docs/paper/figures/fig_keff_eta_scatter.{pdf,png}`。

---
