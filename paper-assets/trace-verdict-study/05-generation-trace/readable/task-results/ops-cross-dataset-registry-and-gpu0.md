# ops cross dataset registry and gpu0

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cross_dataset_registry_and_gpu0_20260522T053547_result.json`
- **Structured JSON:** [`403cfd32722870a0d18d.json`](../../sessions/40/403cfd32722870a0d18d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. cross_dataset_batch 状态

**正在训练，进展正常。**

- 实验 1/4 `cross_he2mbpp_exception_only` — 已完成（13:26:09），checkpoints 齐全（checkpoint-52/104/156 + final）
- 实验 2/4 `cross_he2mbpp_no_trace` — **当前在跑**，刚完成一轮 eval（130/156 步时触发），现在进入下一段训练（eval 内层进度 198/1068）
- GPU 1: 100% 利用率，63697 MiB 显存占用
- 训练指标（实验 1 最终）：loss 从 1.37 降至 0.25，token accuracy 从 0.75 升至 0.93

### 2. cuda:0 清理结果：失败

**原因：`nvidia-smi --gpu-reset` 在此 Seetacloud 实例上 "Not Supported"（虚拟化/容器环境不支持 GPU reset）。**

详细排查：
- GPU 0 无任何 compute 进程（`nvidia-smi --query-compute-apps` 返回空），49GB 确认是孤儿显存
- 但当前训练进程 PID 752928 通过 `/dev/nvidia1`（GPU 0 对应设备）持有一个 fd（非 mmap），可能是 PyTorch 初始化时探测所有 GPU 留下的
- GPU reset 不可用，`fuser` 也无法找到独立的泄漏进程可 kill
- **唯一安全的释放方式**：等 batch 4 个实验全部跑完后，752928 进程退出时应自动释放；如果仍残留，届时再尝试手动清理或重启实例

---
