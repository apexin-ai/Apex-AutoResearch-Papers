# ops cuda0 cleanup v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_cleanup_v2_20260515T102606_result.json`
- **Structured JSON:** [`b34e1a4eb482c9e2b3ca.json`](../../sessions/b3/b34e1a4eb482c9e2b3ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因找到。**

## 诊断结果

| | cuda:0 | cuda:1 |
|---|---|---|
| 已用 | 49175 MiB | 41325 MiB |
| 可用 | 48077 MiB | 55928 MiB |
| 进程 | PID 87061（隐性持有） | PID 87061（主训练） |

**49GB 的持有者是 PID 87061（ae_only 训练）本身。**

证据链：
1. PID 87061 的 fd 列表显示同时打开了 `/dev/nvidia1`（3 个 fd，对应 GPU 0）和 `/dev/nvidia3`（~25 个 fd，对应 GPU 1）
2. 训练启动时 **未设置 `CUDA_VISIBLE_DEVICES`**，`--gpu 1` 只控制计算设备，但 PyTorch 初始化时已在 GPU 0 上创建了 CUDA context 并分配了 ~49GB（模型权重/缓冲区的副本）
3. `nvidia-smi pmon` 确认 GPU 0 无活跃计算，GPU 1 是实际计算设备（SM 98%）
4. `nvidia-smi --query-compute-apps` 不列出 GPU 0 上的分配——这是因为 NVIDIA 驱动将其归类为非计算型内存持有

**无法清理。** 这块内存由正在运行的 ae_only 进程持有，杀进程 = 终止训练。ae_only 完成后自动释放。

## 建议（后续启动时避免复发）

启动脚本加 `CUDA_VISIBLE_DEVICES=1`（ae_only 的 tmux 命令里漏了），这样 PyTorch 初始化就不会触碰 GPU 0：

```bash
export CUDA_VISIBLE_DEVICES=1 && python train/train_sft.py --condition ae_only --gpu 0 ...
```

注意：设了 `CUDA_VISIBLE_DEVICES=1` 后，`--gpu` 参数应改为 `0`（因为进程只能看到一张卡）。

---
