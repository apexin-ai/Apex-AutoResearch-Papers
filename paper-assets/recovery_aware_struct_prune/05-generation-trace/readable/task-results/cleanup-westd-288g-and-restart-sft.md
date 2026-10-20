# cleanup westd 288g and restart sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_westd_288g_and_restart_sft_20260521T182921_result.json`
- **Structured JSON:** [`65e9aef589d3fa4532c5.json`](../../sessions/65/65e9aef589d3fa4532c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**Phase 2 — 磁盘清理**
- 删除 5 批共 ~274G（ShortGPT 39G + 1.5B 16.8G + α=4.0 残留 27G + Qwen-Math 116G + 旧版 53G + pruned 中间产物 36G）
- `df -h`: 619G → 345G used, **275G 可用**（56%）

**Phase 3 — sft_warmup.py 修改**
- 在 SFTConfig 中添加 `save_only_model=True` 和 `save_total_limit=1`（第97-98行）
- 语法验证通过

**Phase 4 — SFT 提交**
- exp_id: `sft_alpha4_20_v2`
- PID: `401581`
- GPU: westd-29022 cuda:2
- tmux session: `sft_alpha4_20_v2`
- log: `~/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log`

---
