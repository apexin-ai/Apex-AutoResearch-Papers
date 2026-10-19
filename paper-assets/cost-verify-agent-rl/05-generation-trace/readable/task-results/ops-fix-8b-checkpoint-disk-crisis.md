# ops fix 8b checkpoint disk crisis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-8b-checkpoint-disk-crisis_20260519T102624_result.json`
- **Structured JSON:** [`f7e51b80aaec3e8ea72e.json`](../../sessions/f7/f7e51b80aaec3e8ea72e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行。汇报：

### 执行结果

| 项目 | 结果 |
|---|---|
| **Cell A 当前 step** | Step 1 完成，step 2 rollout 中（total 15 steps, save_freq=5） |
| **save_freq 能否热改** | **不能**。`self.config.trainer.save_freq` 是内存中的 OmegaConf 对象，每步通过 `self.global_steps % self.config.trainer.save_freq == 0` 检查（`ray_trainer.py:1248`），无文件重载机制 |
| **执行方案** | 方案 2：清磁盘 |
| **磁盘清理前** | 76G 可用 (70%) |
| **磁盘清理后** | **162G 可用 (36%)** |
| **清理内容** | `exp029-seed2/` (62G) + `hsweep-h10/` (21G) + `qwen3_exp021_ragen_sft_v4/` (3.3G) + 3个 tar.gz/安装包 (~1.2G) |
| **Cell C config** | `save_freq` 已改为 999 |
| **训练状态** | PID 849089 正常运行 (uptime 2h27m) |

162G 可用空间足够应对 step 5 的 ~94GB checkpoint save。`checkpoint-231` 未动。

---
