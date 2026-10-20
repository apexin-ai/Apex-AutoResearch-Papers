# submit qwen importance batch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_qwen-importance-batch_20260514T071312_result.json`
- **Structured JSON:** [`6b3a603d1a1c725fb5b0.json`](../../sessions/6b/6b3a603d1a1c725fb5b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

- **Symlink**：修复了原来的问题——`checkpoints/Qwen2.5-7B-Instruct` 是一个缺少 safetensors 的真实目录，`ln -sf` 在其内部创建了嵌套链接。已删除旧目录，重建正确的 symlink → `/root/autodl-tmp/models/Qwen2.5-7B-Instruct`
- **4 个实验全部运行中**：
  - `bf16_qw_imp_s015` → GPU 0 (15295 MiB)
  - `bf16_qw_imp_s020` → GPU 1 (15295 MiB)
  - `bf16_qw_imp_s025` → GPU 2 (15293 MiB)
  - `bf16_qw_imp_s030` → GPU 3 (15275 MiB)
- **Registry**：4 个实验状态均已更新为 RUNNING

---
