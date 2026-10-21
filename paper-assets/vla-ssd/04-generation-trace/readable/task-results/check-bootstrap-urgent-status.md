# check bootstrap urgent status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_urgent_status_20260522T162657_result.json`
- **Structured JSON:** [`9dd748be0edc787cbaf5.json`](../../sessions/9d/9dd748be0edc787cbaf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**状态：正常运行中，未崩溃。**

### tmux sessions
- `bootstrap_cuda0` — 存在，运行中
- `bootstrap_cuda1` — 存在，运行中

### GPU 状态
| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Black (98GB) | 2135 MiB | **0%** | python3 (PID 679958) |
| 1 | RTX PRO 6000 Black (98GB) | 691 MiB | **0%** | python3 (PID 679960) |

### 进程
- GPU 0: `clustered_bootstrap_probe.py --arch openvla --suite goal --condition trained --n_bootstrap 1000` — CPU 时间 687 min
- GPU 1: `clustered_bootstrap_probe.py --arch tracvla --suite goal --condition trained --n_bootstrap 1000` — CPU 时间 694 min

### 当前阶段
两卡都已完成 feature extraction（5000/5000 samples），正在执行 **Bootstrap (1000 iterations)**。Bootstrap 阶段是纯 CPU 计算（kernel matrix + ridge regression 重采样），所以 **GPU 利用率 0% 是正常的**——不是崩了，是计算已经离开 GPU 转到 CPU 上了。

- cuda0 (openvla): 00:03:16 开始 bootstrap，已运行约 24 分钟
- cuda1 (tracvla): 00:03:08 开始 bootstrap，已运行约 24 分钟

### 结果文件
尚无 `.json` 输出——bootstrap 1000 次迭代还在跑，完成后才会写结果文件。

### 结论
**无需干预。** 两个任务都在正常执行 bootstrap 阶段，GPU 空闲是预期行为。等 bootstrap 完成后会自动写入结果 JSON。

---
