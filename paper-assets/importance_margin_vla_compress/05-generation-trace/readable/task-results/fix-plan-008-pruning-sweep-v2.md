# fix plan 008 pruning sweep v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan_008_pruning_sweep_v2_20260516T151209_result.json`
- **Structured JSON:** [`e36cf8a9392692e64d71.json`](../../sessions/e3/e36cf8a9392692e64d71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已成功启动，正在运行 500 batch 评估。

**总结：**

1. **根因**：`eval_pruning_sweep.py` 把 dataloader 的原始 batch 直接传给 `baseline_forward()` 和 `model.forward()`，但原始 batch 只有 `task`（字符串），没有 `observation.language.tokens`。需要先调用 `preprocess_batch()` 做 tokenization。

2. **修复内容**（3 处改动）：
   - 新增导入 `preprocess_batch, get_tokenizer_from_policy`
   - 模型加载后提取 tokenizer
   - 循环中用 `preprocess_batch(batch, tokenizer, device=device)` 替换手动 device 移动

3. **Dry-run 验证通过**：1 batch 完成无报错，各 k_ratio 均有正常输出

4. **已提交完整评估**：`plan_008_pruning_sweep_v2`，PID=207411，500 batches，cuda:1，registry 状态 RUNNING

---
