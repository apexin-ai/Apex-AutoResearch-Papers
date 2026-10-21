# prep label only dry run

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_label-only-dry-run_20260516T052013_result.json`
- **Structured JSON:** [`93c3deb9dbd2e703c51c.json`](../../sessions/93/93c3deb9dbd2e703c51c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

准备完成。

**验证结果**：
- 数据文件 ✓（4720 train / 1190 test）
- 模型文件 ✓（Qwen2.5-Coder-7B-Instruct，4个 safetensors 分片）
- 数据加载 + tokenization 路径 ✓（CPU dry-run 到 model loading 前全部通过）
- eval max_length=2048 与 train max_length=2048 匹配 ✓
- GPU dry-run 跳过（两块 GPU 被 ae_only 占满）

**GPU 释放后提交**：两条命令已写入 `label_only_seed_prep.md`，seed123 → cuda:0，seed456 → cuda:1，预计每个 ~2-2.5h。Registry 中 `label_only_seed123/456` 已处于 PREPARING 状态。

---
