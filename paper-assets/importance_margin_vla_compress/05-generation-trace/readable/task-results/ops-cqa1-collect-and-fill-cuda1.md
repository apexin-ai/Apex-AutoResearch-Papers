# ops cqa1 collect and fill cuda1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-collect-and-fill-cuda1_20260521T034148_result.json`
- **Structured JSON:** [`6eb4941b3093e33bcc07.json`](../../sessions/6e/6eb4941b3093e33bcc07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器实际状态与任务描述完全不符。汇报如下：

---

## 服务器实际状态 (westd-27271)

### GPU 配置
服务器只有 **2 块 GPU**（非 4 块），任务中提到的 cuda:0/1/2/3 和 X-VLA random pruning 实验在此服务器上**不存在**。

### GPU 0 — OpenVLA Smart Compress m128 eval (libero_object, seed42)
- PID: 176320
- 启动时间: 11:01
- 进度: **Task 0/10, Episode 4/50**
- 每 episode ~8 min（均 FAIL at 280 steps），估计单 task ~6.7h，全部 10 tasks ~67h
- 前 4 个 episode 全部 FAIL，结果不太乐观

### GPU 1 — OpenVLA Smart Compress m32 training (resumed)
- PID: 921279 (tmux session `train_openvla_sc_m32_seed42`)
- 进度: **step 41250 / 100000** (41.25%)
- 速度: 0.5 sps → 剩余约 **32.6 小时**
- 最新 checkpoint: step 40000

### 结论
1. **X-VLA random k=0.85/k=0.5 Object 实验**: 不在此服务器运行，未找到相关日志或进程
2. **X-VLA Spatial random k=0.85**: 同上，不存在
3. **cuda:1 填充**: 不可行，GPU 1 正在跑 m32 训练（41%），无空闲 GPU
4. 另外还有一个挂起的 HF 下载进程 (PID 140550) 在后台下载 `openvla-7b-finetuned-libero-spatial` 模型分片

需要确认：这些 X-VLA random pruning 实验是否在另一台服务器上？还是任务描述过时了？

---
