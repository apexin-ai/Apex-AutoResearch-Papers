# run auto gsm8k to math monitor

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_auto_gsm8k_to_math_monitor_20260521T124749_result.json`
- **Structured JSON:** [`c2cb7756c7fc3b54cdae.json`](../../sessions/c2/c2cb7756c7fc3b54cdae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

监控脚本运行正常。

**部署完成：**

| 项目 | 状态 |
|------|------|
| 监控脚本 PID | **163199** |
| 日志文件 | `/tmp/gsm8k_to_math_monitor.log` |
| Mistral GSM8K | 54,400 / 57,600 (94%) — 预计最先完成 |
| Qwen GSM8K | 44,000 / 57,600 (76%) |
| Gemma GSM8K | 41,600 / 57,600 (72%) |

脚本每 30 秒轮询一次，某模型 GSM8K 行数达到 57,600 后立即在对应 GPU 上启动 MATH 推理。三个模型全部切换后脚本自动退出。Llama (GPU 1) 的 MATH 已在跑，不受影响。

---
