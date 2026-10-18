# code token merging prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_token_merging_prep_20260517T091729_result.json`
- **Structured JSON:** [`03e17990b0771441245f.json`](../../sessions/03/03e17990b0771441245f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。修改汇总：

**`eval_success_rate_libero.py`** 新增内容：

1. **CLI 参数**（L73-77）：
   - `--pruning_method {zero_mask, true_removal, merge}`（默认 `zero_mask`）
   - `--merge_alpha`（默认 `1.0`）

2. **`register_acis_hook` 重写**（L189-238）：
   - `zero_mask`：原有逻辑，pruned token 置零
   - `true_removal`：保留 top-k tokens，输出序列缩短
   - `merge`：pruned token 按 position 距离找最近的 kept token，加权平均合并。公式：`kept[i] = kept[i] + alpha * mean(assigned pruned tokens)`。输出长度 = k

3. **调用处更新**（L352-356）：传入 `method` 和 `merge_alpha`

4. **日志和 summary**：记录 `pruning_method` 和 `merge_alpha`

---
