# ops exp009 relaunch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp009_relaunch_20260514T034255_result.json`
- **Structured JSON:** [`ca2fad2e16565d37685c.json`](../../sessions/ca/ca2fad2e16565d37685c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成，汇总结果：

### 产出

| 项目 | 状态 |
|------|------|
| **Symlink** | `qwen3_sft_final -> exp008_sft/final`，config.json 存在 |
| **model_path** | 第10行：`/root/autodl-tmp/checkpoints/qwen3_sft_final` |
| **save_freq** | 第25行：`5` |
| **response_mask** | 配置中未出现（未设置） |
| **RAY_TMPDIR** | `.bashrc` 中已设置 `/root/autodl-tmp/ray_tmp` |
| **GPU** | GPU 0: 0 MiB / 0%，GPU 1: 0 MiB / 0% — 两张卡完全空闲 |
| **磁盘** | 根分区 30G，已用 7.3G，剩余 23G (25%) |

### 结论

**可以安全提交 exp009。** 所有前置条件满足：symlink 正确指向 SFT checkpoint、model_path 已更新、GPU 空闲、磁盘充足、RAY_TMPDIR 已配置。`response_mask` 未在配置中出现——如果 Director 要求该项必须存在，需确认是否需要补加。

---
