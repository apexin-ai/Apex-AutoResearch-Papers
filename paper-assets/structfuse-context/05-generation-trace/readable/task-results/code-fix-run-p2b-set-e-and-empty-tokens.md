# code fix run p2b set e and empty tokens

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_run_p2b_set_e_and_empty_tokens_20260512T150611_result.json`
- **Structured JSON:** [`9198a44f06f69209e955.json`](../../sessions/91/9198a44f06f69209e955.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 132149 仍在运行，未受影响。

### 总结

**改动 1 (run_p2b_all.sh)**：
- 去掉 `set -e`
- 每个 run 用 `if !` 捕获失败，记录到 `FAILED_RUNS`
- 失败后继续执行后续 runs
- 脚本结束时有失败则 `exit 1`

**改动 2 (train.py + contrastive_model.py)**：
- `__getitem__` 中空 tokens 不再替换为 `"[empty]"`，改为过滤后用 `"padding"` 占位 + `neg_valid` 标记
- `collate_fn` 生成 `neg_valid_mask` tensor (B, K)
- `contrastive_model.py` forward 中在 loss 计算前将无效 neg logits 设为 `-inf`，使其不参与 softmax

---
