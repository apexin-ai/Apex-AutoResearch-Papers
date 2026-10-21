# deploy cqa1 pi05 strict 3gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_pi05_strict_3gpu_20260527T075053_result.json`
- **Structured JSON:** [`72b653f4c75b9ba1ab49.json`](../../sessions/72/72b653f4c75b9ba1ab49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署汇总

### GPU 实际状态（与预期不同）

| GPU | 预期 | 实际 | 进程 |
|-----|------|------|------|
| 0 | 空闲 | **占用** | openvla random k=0.95 goal (PID 896333, 5.5h) |
| 1 | 空闲 | **占用** | openvla attn k=0.95 goal (PID 11249, 2.3h) |
| 2 | 空闲 | **空闲→已部署** | — |
| 3 | 占用 | 占用 | openvla attn k=0.5 goal (PID 897100, 5.5h) |

### 已完成

1. **Stale registry 清理**：确认 PID 790017、732826 均已不存在，两条 registry 已是 DONE 状态无需额外更新
2. **GPU2 部署成功**：`eval_pi05_l2norm_k085_long_seed42_strict`（PID 93525），模型加载中，tmux session=`eval_pi05_l2norm_k085_strict`，registry 已注册为 RUNNING

### 未部署（GPU 被占用）

| 实验 | 计划 GPU | 阻塞原因 |
|------|---------|---------|
| eval_pi05_random_k07_long_seed42_strict | GPU0 | openvla random k=0.95 goal 在跑 |
| eval_pi05_random_k05_long_seed42_strict | GPU1 | openvla attn k=0.95 goal 在跑 |

GPU0 上的实验已跑 5.5h，GPU1 上的跑了 2.3h。这些 openvla goal 实验完成后可以接着部署剩余两个 π0.5 strict 实验。需要我设置监控等 GPU 空出后自动部署吗？

---
