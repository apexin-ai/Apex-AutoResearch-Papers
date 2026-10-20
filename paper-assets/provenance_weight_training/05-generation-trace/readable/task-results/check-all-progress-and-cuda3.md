# check all progress and cuda3

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_progress_and_cuda3_20260523T215845_result.json`
- **Structured JSON:** [`fd635bddadf846aef427.json`](../../sessions/fd/fd635bddadf846aef427.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度
- **bs8_nmin4_adaptive_seed456_r2** (cuda:0): step 5876/6103 (96.3%), ETA: ~06:19 UTC
- **bs8_nmin4_uniform_seed456_r2** (cuda:2): **已完成** ✓ 6103/6103 (100%), 耗时 9h09m, 模型已保存到 `/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed456/final`
- **aeff_only_nmin1_seed456** (cuda:1): step 2007/6103 (32.9%), ETA: ~09:30 UTC
- GPU 状态: 正常。cuda:0 100% 60°C, cuda:1 71% 52°C, cuda:2&3 空闲

## cuda:3 Eval Dry-run
- 结果: **成功**
- 注意: 脚本实际路径是 `evaluation/eval_pipeline.py`（非 `eval_perplexity.py`），参数为 `--model_path` / `--eval_data_path` / `--num_eval_tokens`（无 `--max_docs`）
- 输出: Perplexity 23.03, Loss 3.1367 (base model on 7 docs, ~5k tokens)
- 结论: eval pipeline 就绪，可在训练完成后直接运行完整评估

---
