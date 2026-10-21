# analysis eval rsft ced s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_rsft_ced_s43_20260516T051532_result.json`
- **Structured JSON:** [`2ff39d15790fa1af5dd2.json`](../../sessions/2f/2ff39d15790fa1af5dd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**eval_rsft_ced_s43 结果**：
- **rel_f1 = 0.4601**（在 0.43–0.47 预期范围内 → **success**）
- ign_f1 = 0.4512, evi_f1 = 0.8063, edcr = 0.6542, evi_f1_joint = 0.3605
- 格式合规 100%, truncation 184/985 (18.7%)
- s43 是目前 CED 最高的 rel_f1（s45 = 0.4514），属于正常 seed 方差

**CED vs flat-NLI（初步，2 CED seeds）**：rel_f1 几乎一致（CED 0.4558 vs fNLI 0.4557，Δ < 0.001）。最终 4-seed 对比需等 `reeval_ced_s42` 和 `reeval_ced_s44` 完成。

Registry 已更新（metrics / conclusion=success / status=DONE），报告已注册。

---
