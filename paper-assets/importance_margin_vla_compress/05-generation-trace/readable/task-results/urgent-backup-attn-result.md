# urgent backup attn result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_backup_attn_result_20260525T141502_result.json`
- **Structured JSON:** [`649a454012293db5a0b8.json`](../../sessions/64/649a454012293db5a0b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

备份成功。文件内容确认：

- **overall_success_rate: 43.6%**（key 是 `overall_success_rate`，不是之前猜的两个名字）
- mode: `l2norm_prune`，seed=42，500 episodes，时间戳 2026-05-25 22:06
- 文件已安全保存为 `openvla_attn_prune_k09_long_seed42.json`

注意：文件中记录的 mode 是 `l2norm_prune`、SR 是 43.6% 而非预期的 Attn k=0.9 Long (SR=44.0%)。这可能意味着 L2norm 的结果已经覆盖了 Attn 的结果，或者这本身就是 L2norm 的结果。建议确认是否还有其他地方保存了 Attn k=0.9 Long 的原始数据。

---
