# train smart compress m96

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_smart_compress_m96_20260517T204652_result.json`
- **Structured JSON:** [`ec76050e4b0965bd2e52.json`](../../sessions/ec/ec76050e4b0965bd2e52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

M=96 训练已成功启动并在正常训练中。

### 汇总

**M=96 (新启动)**
- PID: 350781
- GPU: cuda:2, 已占用 2787 MiB
- 初始 loss 下降正常: step=0 loss=1.5122 → step=50 loss=0.9785 → step=100 loss=0.6430
- 训练速度: ~4.1 sps

**M=32 (已运行)**
- step=49000/100000, loss=0.1249, lr=5.36e-05, sps=4.3

**M=64 (已运行)**
- step=50350/100000, loss=0.0375, lr=5.15e-05, sps=4.4

三个训练任务分别在 GPU 0/1/2 上正常运行。

---
