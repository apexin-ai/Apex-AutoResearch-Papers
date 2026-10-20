# fix sft rasp rlvr 20 restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sft_rasp_rlvr_20_restart_20260516T142843_result.json`
- **Structured JSON:** [`a5e4a0e37cfba68c715c.json`](../../sessions/a5/a5e4a0e37cfba68c715c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**模型验证通过。** checkpoint-1870 完整可用：

- 格式：safetensors，339 个 tensor keys
- 模型：Qwen2, hidden=3584, 28 layers（剪枝后结构）
- Tokenizer：Qwen2Tokenizer
- 路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20/checkpoint-1870`

**磁盘问题严重**：数据盘 250G 已 100% 满。建议立即删除：
- `checkpoint-935`（中间 checkpoint，35GB）— 有 checkpoint-1870 即可
- `checkpoint-1870/optimizer.pt`（4.5GB）— eval 不需要 optimizer state

这两项可释放 ~39.5GB，否则后续 eval 可能无法写结果文件。是否执行清理？

---
