# infra check eval alive

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-eval-alive_20260515T202037_result.json`
- **Structured JSON:** [`3345006638f3376a8a9d.json`](../../sessions/33/3345006638f3376a8a9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. Eval 进程 — 存活

| 进程 | PID | CPU% | 内存 (RSS) | 启动时间 | 累计 CPU 时间 | 当前 task |
|------|-----|------|-----------|---------|-------------|-----------|
| baseline_std_v3 | 109428 | 2187% | ~13.6 GB | 03:38 | 932 min | `libero_spatial` |
| baseline_plus_v2 | 109501 | 2044% | ~12.9 GB | 03:38 | 871 min | `libero_spatial` |

两个进程都在活跃运行，CPU 高占用说明在做 rollout 推理。

### 2. GPU 利用率

| GPU | 型号 | 利用率 | 显存使用 |
|-----|------|--------|---------|
| GPU 0 | RTX PRO 6000 Blackwell (98 GB) | 23% | 4384 / 97887 MiB |
| GPU 1 | RTX PRO 6000 Blackwell (98 GB) | 1% | 4384 / 97887 MiB |

显存占用很低（~4.3 GB/卡），GPU 利用率也不高——符合 `batch_size=1` 的 eval 特征，瓶颈在 CPU 端的环境仿真。

### 3. 日志内容

- **baseline_std_v3**: rollout 进度 ~18%（49/280 steps），`running_success_rate=0.0%`
- **baseline_plus_v2**: rollout 进度 ~11%（30/280 steps），`running_success_rate=0.0%`

两个都在跑 `libero_spatial` 的某一集 rollout。

### 4. 数据集下载

- `/root/autodl-tmp/.hf_cache/hub/datasets--lerobot--libero` 只有 4.0K（仅目录结构/metadata）
- 无 `snapshot_download` 进程在运行

数据集实际未下载或走的其他缓存路径。eval 正常运行说明数据来自别处或 libero 环境不需要预下载数据集。

---
