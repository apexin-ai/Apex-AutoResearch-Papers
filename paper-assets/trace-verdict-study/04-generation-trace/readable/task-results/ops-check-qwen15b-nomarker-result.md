# ops check qwen15b nomarker result

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_qwen15b_nomarker_result_20260516T174211_result.json`
- **Structured JSON:** [`9048dbdd4837a89ac118.json`](../../sessions/90/9048dbdd4837a89ac118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**实验状态：实验名称有误 / 训练完成但 eval_results.json 不存在**

具体情况：

1. `/tmp/qwen15b_nomarker_seed42.log` 实际跑的是 **`exception_only_nomarker`** 条件（Qwen2.5-Coder-1.5B-Instruct），输出到 `/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker/`
2. 不存在 `qwen15b_nomarker_seed42` checkpoint 目录
3. 训练已完成（444 steps, 3 epochs, ~29 分钟），日志尾部显示：
   - `eval_loss`: 0.6014
   - `eval_mean_token_accuracy`: **0.9008**
   - `train_loss`: 0.1340
4. 模型已保存到 `.../exception_only_nomarker/final/`（adapter_model.safetensors 73MB）
5. **无 `eval_results.json` 文件** — 训练脚本只输出了 trainer 的 eval metrics 到 stdout，未单独写 JSON

总结：训练成功完成，eval token accuracy = 90.08%，但实验名称是 `exception_only_nomarker`（非 `qwen15b_nomarker_seed42`），且无独立的 eval_results.json 文件。

---
