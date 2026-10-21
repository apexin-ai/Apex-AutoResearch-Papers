# ssh westd status check d097

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_status_check_d097_20260521T135147_result.json`
- **Structured JSON:** [`d6dbfa95a6e3bd9ebb16.json`](../../sessions/d6/d6dbfa95a6e3bd9ebb16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **cuda:0 @2048 (grpo_cka_only_25_v2)**: ALIVE — PID 379999, 运行 22min, 42/500 (8%)
2. **cuda:2 @2048 (sft_cka_only_25_v2)**: ALIVE — PID 380074, 运行 22min, 43/500 (9%)
3. **v1 SFT Standard 25% MATH-500 max_new_tokens**: **2048** — JSON 无显式 config 字段，但 response_length 上限恰好 2048，318/500 截断 (63.6%)，确认 v1 已用 2048。accuracy=0.13 (65/500)，模型本身过于冗长导致高截断率，不是 token 限制设太低的问题
4. **eval_gsm8k_sft_standard_25**: **1181/1319 (90%)** — PID 335301 存活 5h44m，最近 checkpoint acc=0.5078, eos_rate=95.39%, avg_len=330。预计约 30-40min 完成

---
