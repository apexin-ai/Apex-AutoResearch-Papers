# fix westd disk ghost space

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd_disk_ghost_space_20260521T105807_result.json`
- **Structured JSON:** [`9bef761569cc9b557b84.json`](../../sessions/9b/9bef761569cc9b557b84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键发现：

**verl checkpoint 清理逻辑**（`fsdp_checkpoint_manager.py:206-214`）：
- 清理在新 checkpoint 写入**之前**执行（好消息）
- 但 `max_ckpt_to_keep` 来自启动时加载的内存 config（`self.config.trainer.get("max_actor_ckpt_to_keep", None)`）
- **YAML 修改对运行中的进程无效**——内存中仍是 10

**空间预估（max_ckpt_to_keep=10，不会触发清理）：**
- 现在：2 ckpt (step_5 × 2 seeds) = 42GB，可用 74GB
- step_10 后：+42GB → 剩 32GB
- step_15 后：+42GB → **溢出 -10GB**

需要现在释放至少 10GB（安全起见建议 30GB+）。可清理候选项：

| 目录 | 大小 | 风险 |
|------|------|------|
| backups/exp029-seed2-bjb1 | 21G | 旧 seed2 备份，bjb1 上应有原始数据 |
| checkpoints/scienceworld_sft | 7.6G | 非当前实验 |
| checkpoints/qwen3_scienceworld_sft | 7.6G | 非当前实验 |
| checkpoints/qwen3_exp021_ragen_sft_v4 | 3.3G | 旧实验 |
| .ms_cache | 6.7G | ModelScope 下载缓存 |

**需要你确认哪些可以删除。** 删除 backups + 两个 scienceworld ckpt 就能释放 ~36GB，足以撑到 step_15。

另外建议部署一个轻量 watchdog 脚本，在每次 checkpoint 写入后自动删除旧的（因为进程内的 keep=10 不会触发清理）。是否需要？

---
