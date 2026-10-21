# diagnose flatnli r6 step35 health

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_flatnli-r6-step35-health_20260514T181041_result.json`
- **Structured JSON:** [`92690e7e9645b2c6b24b.json`](../../sessions/92/92690e7e9645b2c6b24b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## flatnli_r6 健康检查 (step 26)

- **状态: KILL_RECOMMENDED**
- frac_zero_std 趋势: step 5=0.1 → step 15=0.6 → step 20=0.7 → **step 25=0.9**
- f1_reward 趋势: step 5=0.007 → step 15=0.023 → step 20=0.012 → **step 25=0.0**
- flat_nli_reward 趋势: step 5=0.021 → step 15=0.018 → step 20=0.023 → **step 25=0.0**
- KL: 0.056 (step 5 曾爆到 1.2亿，后恢复正常)
- grad_norm: 0.27
- GPU 3: 65% util, 13647/32607 MiB

**判断依据**：

Step 25 已经完全 mode collapse — frac_zero_std=0.9 突破 0.8 阈值，f1_reward 和 flat_nli_reward 双双归零，模型只剩 format_reward (0.293)。走势与 extract_r4 一致（甚至更快崩溃）。

严格来说需要等 step 30 确认第二个连续 checkpoint ≥ 0.8，但 f1=0 + flat_nli=0 的状态已不可能自行恢复，继续跑只是浪费 GPU 时间。

**建议**: 立即 kill PID 76953，释放 cuda:3。

---
