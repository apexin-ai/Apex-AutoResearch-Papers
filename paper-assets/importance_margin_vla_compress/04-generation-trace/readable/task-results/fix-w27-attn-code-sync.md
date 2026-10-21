# fix w27 attn code sync

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_w27_attn_code_sync_20260527T175538_result.json`
- **Structured JSON:** [`b4fe513d9313d6e39c83.json`](../../sessions/b4/b4fe513d9313d6e39c83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已正常运行：

- **k=0.85**: `n_keep=217/256` tokens, attention pruning 正常工作
- **k=0.75**: `n_keep=192/256` tokens, attention pruning 正常工作

任务完成总结：

1. **代码对比**: w27 的 `eval_pi05_pruning_libero.py` (294行) 缺少 `attention` prune mode 及其实现（`compute_attention_importance_probe` 函数、`pruned_embed_prefix_attn` 函数等），w41 (426行) 有完整实现
2. **代码同步**: 通过分段 heredoc 将 w41 的完整文件写入 w27，语法验证通过 (426行, SYNTAX_OK)
3. **验证**: `--prune_mode attention` argparse 接受正常
4. **提交实验**: 两个 v2 实验已通过 tmux 启动，与现有实验共享 GPU（97GB 中仅用 ~10.7GB，空间充足），registry 已更新为 RUNNING
   - `eval_pi05_attn_k085_long_seed43_strict_w27_v2` — cuda:0, seed=43, k=0.85
   - `eval_pi05_attn_k075_long_seed43_strict_w27_v2` — cuda:1, seed=43, k=0.75

---
