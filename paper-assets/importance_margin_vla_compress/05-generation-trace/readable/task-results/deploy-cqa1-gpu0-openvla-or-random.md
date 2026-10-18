# deploy cqa1 gpu0 openvla or random

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu0_openvla_or_random_20260524T213121_result.json`
- **Structured JSON:** [`987173133c0b36405c9f.json`](../../sessions/98/987173133c0b36405c9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型仍在加载中（π0.5 较大），进程正常运行。

```
OpenVLA 环境: 无（脚本仅支持 l2_norm/random，无 attention 模式；transformers=5.5.3 非 4.40.x）
选择方案: B: Random k=0.85 Object s43
部署: 成功 PID=733129
GPU0 进程数: 模型加载中，尚未分配显存（进程存活，状态 S）
```

实验 `eval_pi05_random_k085_object_seed43_postfix` 已注册为 RUNNING，server=cqa1-33015 GPU0。

---
