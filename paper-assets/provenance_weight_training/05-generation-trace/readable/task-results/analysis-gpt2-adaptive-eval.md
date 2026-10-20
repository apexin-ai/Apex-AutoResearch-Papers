# analysis gpt2 adaptive eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2_adaptive_eval_20260518T232410_result.json`
- **Structured JSON:** [`d009ee2fc89b10b00385.json`](../../sessions/d0/d009ee2fc89b10b00385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**训练状态**: 已完成
- 6103/6103 steps, 3h55m, train_loss=10.58
- checkpoint: `checkpoint-5500`, `checkpoint-6000`, `checkpoint-6103`, `final`

**Eval**: 已提交，后台运行中
- 对 `final` checkpoint 做 perplexity eval
- 日志: `~/runs/provenance_weight_training/eval_gpt2_adaptive_seed42.log`
- PID 262404（nohup）

**Registry 已更新**:
- conclusion=success, status=ANALYZING, checkpoint_path 已设置, metrics 已录入

Eval 预计几分钟内完成，可用 `tail ~/runs/provenance_weight_training/eval_gpt2_adaptive_seed42.log` 查看结果。

---
