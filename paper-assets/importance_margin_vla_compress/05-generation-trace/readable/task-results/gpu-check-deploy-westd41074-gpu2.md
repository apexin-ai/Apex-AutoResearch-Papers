# gpu check deploy westd41074 gpu2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-check-deploy-westd41074-gpu2_20260523T200039_result.json`
- **Structured JSON:** [`b5a1bfe3b106d0e5ea11.json`](../../sessions/b5/b5a1bfe3b106d0e5ea11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 仍被占用：

- **显存**: 10626 MiB used, 43% utilization
- **进程 781238**: 仍在运行

GPU 2 未释放，不部署新实验。eval_pi05_random_k0925_spatial_seed42 的进程可能还在收尾阶段（或是其他任务占用了 GPU 2）。建议等进程自然结束后再部署 eval_pi05_l2norm_k03_goal_seed42。

---
