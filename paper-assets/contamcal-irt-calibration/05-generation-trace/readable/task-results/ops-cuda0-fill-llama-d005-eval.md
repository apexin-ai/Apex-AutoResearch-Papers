# ops cuda0 fill llama d005 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0-fill-llama-d005-eval_20260516T175222_result.json`
- **Structured JSON:** [`1f9fb90695f6c4b23e34.json`](../../sessions/1f/1f9fb90695f6c4b23e34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**exp_001_sft_llama32_3B_d005_s42 (SFT)**:
- 训练完成 3177/3177 steps (1 epoch, 2h15m)
- train_loss=1.5206, mean_token_accuracy=0.6599
- LoRA adapter 完好保存，merge 因磁盘满失败（`/root/autodl-tmp/` 94% 占用，仅 11G 空闲）
- Registry 已更新：conclusion=success, metrics 已填入

**exp_001_eval_llama32_3B_d005_s42 (Eval)**:
- 已在 cuda:0 启动（PID 825638, tmux session `eval_llama_d005`）
- 命令调整：用 `--model-path` (base Llama-3.2-3B) + `--adapter-path` (LoRA adapter) 替代不完整的 merged 模型，evaluate.py 会在内存中 merge_and_unload
- Benchmarks: mmlu, gsm8k, arc_challenge, humaneval (mc-format=aligned)
- Registry 状态：RUNNING

**注意**：数据盘仅剩 11G，后续如果需要 merge 其他模型或存 eval 结果需关注磁盘空间。

---
