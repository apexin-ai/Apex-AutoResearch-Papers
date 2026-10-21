# ops deploy e5 dryrun and check openvla downloads

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_e5_dryrun_and_check_openvla_downloads_20260523T080428_result.json`
- **Structured JSON:** [`60a9ae4a437c0cac9908.json`](../../sessions/60/60a9ae4a437c0cac9908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度约 300KB/s，4.9GB 预计需要几小时。汇报结果。

---

## 汇报

### 1. OpenVLA Goal/Long checkpoint 下载状态
- **Goal**: shard 2/3/4 完整，**shard 1 被截断**（2.0GB/4.9GB），已发起重新下载（PID 464697），速度约 300KB/s，预计数小时
- **Long (libero-10)**: 3 个 shard 仍在下载中（shard 1: 4.3G, shard 2: 3.2G, shard 3: 1.7G），shard 4 完成

### 2. OpenVLA Spatial baseline
- 运行中，GPU 0，Task 6/10
- Task 5 完成时 SR = 78.0%（39/50）— 表现很好

### 3. GPU 状态
| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 20935/97887 MiB | 84% | X-VLA pruning (PID 250278) + OpenVLA spatial baseline (PID 284854) |
| 1 | 1/97887 MiB | 0% | 空闲 |

### 4. E5 Attention Pruning Dry-Run
- **成功**，无报错
- 模型加载 13.8s，879.5M params
- Attention pruning 正常安装：50 vision tokens → keep 45 (90%)
- 完成 10 tasks x 2 episodes = 20 episodes，耗时 4.7 分钟
- 结果保存至 `eval_results/xvla_attn_attention_last_k0.9_libero_object.json`

### 5. GPU 1 最终状态
- **空闲**。E5 dry-run 完成后释放，OpenVLA Goal 因 shard 1 损坏无法加载
- Goal shard 1 正在重新下载，完成后可部署 OpenVLA Goal baseline eval

---
