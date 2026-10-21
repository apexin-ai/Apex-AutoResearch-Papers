# ops kill d100mmlu submit gsm8k cuda1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_d100mmlu_submit_gsm8k_cuda1_20260516T215637_result.json`
- **Structured JSON:** [`6a8a00f7ef6eaf324255.json`](../../sessions/6a/6a8a00f7ef6eaf324255.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

1. **PID 863173 已 kill** — 进程不存在（可能已自行结束），无关联 tmux session
2. **cuda:1 已空闲** — 当前仅 GPU 2 (PID 853489) 和 GPU 4 (PID 842929) 有进程
3. **1.5B-Instruct GSM8K signals 已有完整产出**：
   - `signal_s1_embedding_gsm8k.json` — 734KB
   - `signal_s2_minkpp_gsm8k.json` — 272KB
   - `signal_s4_selfcritique_gsm8k.json` — 317KB
   - `signals_merged_gsm8k.json` — 243KB

所有文件均 >100KB，产出完整。**无需重跑。**

---
