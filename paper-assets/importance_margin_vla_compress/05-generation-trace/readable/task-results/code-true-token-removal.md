# code true token removal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_true_token_removal_20260517T083339_result.json`
- **Structured JSON:** [`a42192cbd97dd894fda2.json`](../../sessions/a4/a42192cbd97dd894fda2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full eval 已启动，运行正常。确认 log 显示 `Pruning: true_removal`。

总结：

1. **代码修改完成**：在 `eval_success_rate_libero.py` 中实现了 `true_removal` pruning 模式
   - 新增 `--pruning-method` CLI 参数（默认 `zero_mask`，向后兼容）
   - `register_acis_hook` 新增 `method` 参数：`true_removal` 模式下用 boolean indexing 直接丢弃 pruned tokens，序列真正变短
   - Summary JSON 和日志均记录 `pruning_method`

2. **架构验证**：SmolVLA 使用 `position_ids = cumsum(pad_masks)` (RoPE)，`embed_prefix` 中通过 `.shape` 动态确定 token 数。变长序列输入没有问题。

3. **Sanity check 通过**：2 episodes 运行无错误，无 shape mismatch

4. **全量 eval 已提交**：`eval_true_removal_k05` tmux session，GPU 1，50 episodes/task x 10 tasks，输出到 `eval_results/eval_true_removal_k05_object.json`

备份文件在 `eval_success_rate_libero.py.bak`。

---
