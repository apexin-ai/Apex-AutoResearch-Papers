# code urgent sft standard eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent-sft-standard-eval_20260515T095816_result.json`
- **Structured JSON:** [`6437a76d4163832493de.json`](../../sessions/64/6437a76d4163832493de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已启动（PID 507411），cuda:1 上运行 `eval_gsm8k.py`，参数：
- model: `sft_standard_20`
- N=100, max_new_tokens=4096, greedy decoding
- 结果将写入 `/root/autodl-tmp/recovery_aware_struct_prune/eval_sft_standard_20_n100.json`

进程状态汇总：
- **PID 239076**（SFT retrain）：已结束，sft_standard_20 模型完整（12.3GB model.safetensors + config + tokenizer）
- **PID 505715**（之前的 eval）：已结束
- **GPU 0**：100% 占用（65GB），有其他任务在跑
- **GPU 1**：空闲 → 现在被 eval 占用

2 分钟后检查进度。

---
