# ssh check ablation state

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-ablation-state_20260515T205420_result.json`
- **Structured JSON:** [`70e27e85ea66759100bf.json`](../../sessions/70/70e27e85ea66759100bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. GPU 进程

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 3 MiB | 0% | PID 659993 刚启动(04:52)，正在加载模型 |
| 1 | 16361 MiB | 77% | PID 658056 (04:28启动)，主提取进程 |

**注意：有两个提取进程同时写入同一目录 `untrained_libero_goal_no_inst/`：**
- PID 658056 (GPU 1): `--max_demos 50` — 主进程
- PID 659993 (GPU 0): `--max_demos 10` — 后启动的，参数不同，**可能冲突**

### 2. no-instruction 特征文件

**untrained_libero_goal_no_inst**: **2/10** h5 文件
- `open_the_middle_drawer_of_the_cabinet.h5` — 2.91 GB（已完成）
- `open_the_top_drawer_and_put_the_bowl_inside.h5` — 2.02 GB（进行中，52% = 5280/10208 steps，~41 step/s）

**trained_libero_goal_no_inst**: **10/10 已全部完成**（~5 GB）

### 3. RSA 结果

`rsa_results.json` 存在（18 KB）— 这是常规 RSA 结果。**`rsa_no_instruction.json` 不存在**，需等 untrained 提取完成后再跑。

### 4. 脚本

没有独立的 `extract_features_no_inst*.py`。使用的是通用 `extract_features.py` + `--task_instruction ""` 参数。

### 5. 建议

**立即行动：kill PID 659993**（GPU 0 上的冲突进程）。它用 `--max_demos 10` 写入同一目录，会产生不一致的 h5 文件覆盖 50-demo 版本。

**之后：继续等**。主进程（PID 658056）当前 2/10 任务、第 2 个任务过半。按当前速度每个任务 ~10-15 分钟，预计还需 **1.5-2 小时** 完成全部 untrained 提取。完成后再跑 RSA no-instruction 分析。

另外还有 PID 651902 在跑 `pca_linear_probe_perlayer.py`（CPU 密集），不影响 GPU 提取。

---
