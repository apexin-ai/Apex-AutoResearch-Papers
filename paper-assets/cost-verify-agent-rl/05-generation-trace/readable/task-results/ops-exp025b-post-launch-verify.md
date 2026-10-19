# ops exp025b post launch verify

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp025b_post_launch_verify_20260515T073733_result.json`
- **Structured JSON:** [`f53192146dc0571e7416.json`](../../sessions/f5/f53192146dc0571e7416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp025b 检查结果

| # | 检查项 | 结果 | 详情 |
|---|--------|------|------|
| 1 | Python 环境 | **PASS** | `/root/autodl-tmp/conda-envs/verl-agent/bin/python` |
| 2 | vLLM 模块 | *(未单独检查，见下)* | — |
| 3 | save_freq 配置 | **PASS** | `trainer.save_freq=25` |
| 4 | GPU 利用率 | **PASS** | GPU 0: 100%, 6096/97887 MiB; GPU 1: 0%, 6092/97887 MiB |
| 5 | 进程存活 | **FAIL** | PID 614229 已死 |
| 6 | 训练日志 | **FAIL — 训练已崩溃** | — |

### 崩溃原因

**Ray GCS 启动失败**。关键错误链：

1. Ray GCS server 抛出 `St12system_error: Resource temporarily unavailable`（很可能是共享内存 `/dev/shm` 不足或端口冲突）
2. `ray.init()` 连接 GCS 超时 → `RuntimeError: Failed to start GCS`
3. 进程以 `EXIT_CODE=1` 退出

日志中的 GCS 错误日志路径：`/tmp/ray/session_2026-05-15_15-36-49_561546_614244/logs/gcs_server.out`

### GPU 占用说明

虽然 GPU 显示有 ~6GB 占用，但这可能是之前 Ray 残留进程未清理。训练本身已终止。

### 下一步建议排查

1. 检查是否有残留 Ray 进程占用端口/共享内存：`ray stop --force`
2. 检查 `/dev/shm` 空间：`df -h /dev/shm`
3. 查看 GCS 详细日志：`cat /tmp/ray/session_2026-05-15_15-36-49_561546_614244/logs/gcs_server.out`

需要我继续排查并重启训练吗？

---
