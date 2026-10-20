# analysis eval prep wave

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-prep-wave_20260518T221545_result.json`
- **Structured JSON:** [`23f1487fc4806b92d2f7.json`](../../sessions/23/23f1487fc4806b92d2f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。文件已写入 `artifacts/eval_commands_wave2.md`。

汇总：

**41312 磁盘**: 21G 可用，空间充足。

**Eval 路径全部确认存在**：
- gpt2_adaptive_seed42: checkpoint-3000/3500/4000
- gpt2_uniform_seed42: checkpoint-3500/4000/4500
- ngram_adaptive_seed42/final, ngram_uniform_seed42/final
- detect_remove_q08_seed42 (41312): checkpoint-3000/3500/4000
- detect_remove_q02_seed42 (30476): checkpoint-3000/3500/4000

**uniform_1_7b_seed123 训练前置条件确认**：Qwen3-1.7B 模型和 scored_data.jsonl 均存在。命令已准备好，GPT-2 完成后用 `nvidia-smi` 确认空闲 GPU 编号，设置 `CUDA_VISIBLE_DEVICES` 即可启动。

---
