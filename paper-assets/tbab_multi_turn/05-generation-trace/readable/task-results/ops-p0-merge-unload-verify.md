# ops p0 merge unload verify

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-merge-unload-verify_20260518T180539_result.json`
- **Structured JSON:** [`625349326a91fc05210c.json`](../../sessions/62/625349326a91fc05210c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### `merge_and_unload()` — **PASS，不是 bug 根因**

完整输出：

| 阶段 | embed norms (32000-32003) | lm_head norms (32000-32003) |
|---|---|---|
| Pre-merge (random init) | `[0.0271, 0.0271, 0.0271, 0.0271]` | `[0.0825, 0.0825, 0.0825, 0.0825]` |
| Adapter loaded | `[0.6875, 0.6562, 0.6602, 0.6641]` | `[0.6328, 0.6211, 0.6328, 0.6328]` |
| After merge_and_unload() | `[0.6875, 0.6562, 0.6602, 0.6641]` | `[0.6328, 0.6211, 0.6328, 0.6328]` |

- PEFT 0.19.1 的 `trainable_token_indices` 机制通过 `token_adapter.trainable_tokens_delta` 存储了 4 个 bridge token 的训练 delta（shape `[4, 4096]`）
- 训练后 bridge token norms 从 ~0.03/0.08 增长到 ~0.65，训练确实修改了它们
- `merge_and_unload()` 完美保留了这些权重，adapter 状态和 merged 状态完全一致

### `model_local.py` 加载方式

`eval/model_local.py` 的加载流程：
1. `resize_token_embeddings(32004)` — 扩展词表
2. `PeftModel.from_pretrained(model, adapter_path)` — 加载 adapter
3. `model.merge_and_unload()` — 合并

流程正确，merge 也正确。**C4 eval P̄ ≈ 3.3% 的问题根因不在 merge_and_unload()，需要从其他方向排查**（如 position reset 逻辑、bridge token 插入位置、generate_tbab 实现等）。

---
