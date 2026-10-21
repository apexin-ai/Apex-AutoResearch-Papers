# code exp15c disk fix rerun

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp15c-disk-fix-rerun_20260519T113115_result.json`
- **Structured JSON:** [`847947162934970157b6.json`](../../sessions/84/847947162934970157b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

1. **释放空间**：将 15G 旧 checkpoint（exp1/mf1/plan 系列等）移到 `/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive/`，删除 exp15c 失败残留。根分区从 100% → 47%（16G 可用）。
2. **修改脚本**：`CKPT_ROOT` 改为 `/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/`，MLM encoder 和 GRU checkpoint 均写入新路径，结果 JSON 仍存原路径。
3. **重跑**：已通过 `submit_training_job` 提交，tmux session `exp15c_roberta_large_mlm`，cuda:0。
4. **Registry**：已更新 spec（含新 checkpoint_path）和 hypothesis。

---
