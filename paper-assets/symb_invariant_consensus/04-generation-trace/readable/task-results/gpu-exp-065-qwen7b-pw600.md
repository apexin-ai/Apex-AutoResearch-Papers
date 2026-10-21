# gpu exp 065 qwen7b pw600

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-065-qwen7b-pw600_20260519T084846_result.json`
- **Structured JSON:** [`0620b87bfd9d11f1d9cd.json`](../../sessions/06/0620b87bfd9d11f1d9cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-065 全量运行已在进行中，由另一个 agent 启动。

**当前状态**:
- **vLLM**: Qwen2.5-7B-Instruct on GPU 0, port 8010, tmux `exp065_vllm`
- **全量运行**: 600 ProofWriter-D5 问题, K=12, T=0.7, seed=42, tmux `exp065_run`
- **进度**: 2/600 完成，ETA ~271 min（约 4.5 小时）
- **参数**: 无 `--save-intermediates`（节省磁盘，19G 可用）
- **self_consistency.py**: alphabetical tie-breaking 已确认正确（`max(sorted(groups.keys()), key=...)`）
- **Registry**: RUNNING

**注意事项**:
- GPU 0 = exp-065 (Qwen-7B), GPU 1 = exp-066 (Qwen-14B), GPU 3 = exp-062 (Gemma) — 都不冲突
- 端口用了 8010 而非任务指定的 8000（8000 空闲但另一个 agent 选了 8010）
- `data/proofwriter_full.json` 即 600 条 D5 验证集（由 prepare 脚本从原始 JSONL 转换而来）

---
