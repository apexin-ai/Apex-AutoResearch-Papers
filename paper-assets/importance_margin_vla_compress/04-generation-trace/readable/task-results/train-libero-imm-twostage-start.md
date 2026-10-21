# train libero imm twostage start

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_libero_imm_twostage_start_20260516T183748_result.json`
- **Structured JSON:** [`c278d53b732fa5e18d6f.json`](../../sessions/c2/c278d53b732fa5e18d6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并运行。

**状态总结：**

| 项目 | 状态 |
|------|------|
| exp_id | `libero_imm_twostage_v1` |
| PID | 221824 (westd-27271, GPU 0) |
| GPU 占用 | 2728 MiB / 97887 MiB |
| 阶段 | 数据集加载中（LIBERO 383 parquet, 已处理 ~1.26GB） |
| 基线 checkpoint | `step_040000/checkpoint.pt` |
| 训练配置 | Stage1: 10K steps (ACIS only), Stage2: 20K steps (LoRA only) |
| Registry | RUNNING |
| 日志 | `/tmp/libero_imm_twostage_v1.log` |

**踩坑修复：** 首次启动未加 `source /etc/network_turbo` 导致 HF 连接挂死。Kill 后用正确环境（network_turbo + `HF_HUB_DISABLE_XET=1` + SSL certs + `python -u`）重启，进展正常。

训练 step 日志会在数据加载完成后开始输出（LIBERO 视频数据集较大，预计还需几分钟）。

---
