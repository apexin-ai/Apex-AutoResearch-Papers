# eval official smolvla prune k05 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_official_smolvla_prune_k05_v2_20260518T132056_result.json`
- **Structured JSON:** [`f3ee8be223d9a6884578.json`](../../sessions/f3/f3ee8be223d9a6884578.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**状态总结：**
- `eval_official_smolvla_prune_k05_v2` 已在 westd-27271 cuda:1 上运行（tmux session，PID 136801）
- 脚本已确认包含 normalization fix + random pruning 支持
- Dry-run 验证通过：模型加载正常，pruning hook 注册成功（k=0.50, true_removal），前 4 个 task 全部 0% SR（符合预期）
- 完整 eval：10 tasks x 50 episodes = 500 episodes，预计运行约 1-2 小时
- Registry 已更新为 RUNNING，parent 设为 eval_official_smolvla_baseline
- 日志：`~/runs/importance_margin_vla_compress/eval_official_smolvla_prune_k05_v2.log`
- 结果输出：`eval_results/official_libero_object_random_prune_k05.json`

---
