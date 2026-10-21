# submit westd 34887 cuda1 kl50eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_westd-34887-cuda1-kl50eval_20260518T081001_result.json`
- **Structured JSON:** [`e51314df7cf04a36f83a.json`](../../sessions/e5/e51314df7cf04a36f83a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 显示 0MiB，进程尚未加载到 GPU（刚启动，模型加载中）。cuda:0 有另一个进程在跑。

注意：命令中 `CUDA_VISIBLE_DEVICES=1` 由 submit_training_job 自动设置，脚本内 `--gpu 0` 会映射到物理 cuda:1。模型加载需要一些时间，之后 cuda:1 会出现显存占用。

**完成**：kl50_s456_eval 已提交到 westd-34887 cuda:1，tmux session `kl50_s456_eval`，日志 `~/runs/distill_sparse_swiglu/kl50_s456_eval.log`。

---
