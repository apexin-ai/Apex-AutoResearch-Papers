# eval hgate dpo002

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_hgate-dpo002_20260512T190226_result.json`
- **Structured JSON:** [`1c2a6f6625011bd73500.json`](../../sessions/1c/1c2a6f6625011bd73500.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vLLM 已在 30s 内启动就绪，Run 1 正在跑。配置确认：

- **vLLM**: cuda:3, port 8001, LoRA mode (`democalib-qwen` = dpo-002 adapter)
- **Eval**: 4 runs x 20 tasks = 80 episodes
- **输出**: `/root/democalib/results/dpo_eval_v2/run_{1..4}/`
- **Registry**: hgate-dpo002 → RUNNING
- **PID**: 311654 (tmux: hgate-dpo002)

参考 hgate-dpo001 单次 run 约 20 分钟，4 runs 预计 ~80 分钟完成。完成后脚本会自动聚合结果并输出 H2/H3 gate 判定。

---
