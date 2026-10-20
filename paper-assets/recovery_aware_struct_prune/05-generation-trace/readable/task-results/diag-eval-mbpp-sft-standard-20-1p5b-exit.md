# diag eval mbpp sft standard 20 1p5b exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_mbpp_sft_standard_20_1p5b_exit_20260519T215615_result.json`
- **Structured JSON:** [`f848425c0b3bac8bd9b2.json`](../../sessions/f8/f848425c0b3bac8bd9b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval_mbpp_sft_standard_20_1p5b — 完成，已关闭。**

| 指标 | 值 |
|------|-----|
| pass@1 | **0.80%** (3/374) |
| stderr | 0.0046 |
| median response length | 2048 (撞顶) |

模型大量输出 `&lt;/think>` 标签和自然语言推理而非代码，绝大多数样本 SyntaxError。这是 1.5B SFT Standard 20% 剪枝模型在 MBPP 上的 baseline，等 CKA-only 对应 eval 出来后可直接对比。

Registry 已更新为 DONE/success，cron 已删除。westb-23072 cuda:0 已释放。

---
