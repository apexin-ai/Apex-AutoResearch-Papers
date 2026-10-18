# code olmo topk50 001 prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_olmo_topk50_001_prep_20260514T224618_result.json`
- **Structured JSON:** [`ea7df9a96c23a72e0acb.json`](../../sessions/ea/ea7df9a96c23a72e0acb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

- `scripts/run_pipeline_olmo_topk50.sh` 已更新，`bash -n` 语法验证通过
- 所有引用路径存在（模型目录、depth_0.jsonl、Python 脚本、nucleus depth-0 LoRA adapter）
- 相比原脚本的改动：
  - Step 1 改为 symlink 复用 `checkpoints/olmo/lora_depth_0`（跳过重复训练）
  - 显式设置 `--temperature 1.0`
  - 新增 `results/olmo_topk50/` 目录创建
- 未提交运行，脚本就绪待用，运行时 `GPU=1 bash scripts/run_pipeline_olmo_topk50.sh` 即可

---
