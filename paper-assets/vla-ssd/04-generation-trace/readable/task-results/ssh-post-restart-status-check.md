# ssh post restart status check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_post_restart_status_check_20260522T020852_result.json`
- **Structured JSON:** [`23f26fc6c377a2481a1d.json`](../../sessions/23/23f26fc6c377a2481a1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. openvla_goal_standardized_v1 (PID 591230)
- **状态**: 运行中
- **运行时间**: 1h36m
- **当前位置**: Phase 6/6 (counterfactual analysis), condition "paraphrased" 1600/5000 (32%)
- **Phase 6 内部进度**: 4 个 condition 中第 4 个（wrong ✓, empty ✓, shuffled ✓, paraphrased 进行中）
- **Pipeline 进度**: 正在处理第 1 个 pipeline condition（`trained`），还有 `untrained` 待跑。**整体约 ~45%**
- **GPU**: GPU 1, 82% 利用率, 15.3GB / 97.9GB VRAM

### 2. openvla_spatial_standardized_v1 (PID 594575)
- **状态**: 运行中（卡在下载）
- **运行时间**: 32min
- **当前位置**: checkpoint 下载阶段，~5.3GB 已下载，尚未开始计算
- **GPU**: GPU 0, 0% 利用率, 0 MiB VRAM（未加载模型）
- **注意**: 下载速度偏慢且波动大（曾到 8.5GB 又回落到 5.2GB），可能有多个文件在轮流下载

### tmux sessions
两个 session 均正常存活：`openvla_goal_standardized_v1` 和 `openvla_spatial_standardized_v1`。

---
