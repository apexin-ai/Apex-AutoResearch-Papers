# harvest deploy westd 41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest-deploy_westd-41074_20260523T115614_result.json`
- **Structured JSON:** [`73abf00bd89b3e30f076.json`](../../sessions/73/73abf00bd89b3e30f076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个新实验正在加载模型，启动正常。汇报：

```
已完成实验（已更新 registry）:
  - eval_pi05_l2norm_k07_long_seed43_v4:  SR=65.4%
  - eval_pi05_random_k085_long_seed43_v3: SR=42.4%
  - eval_pi05_l2norm_k085_long_seed43_v4: SR=77.0%

仍在运行:
  - eval_pi05_random_k03_long_seed43_v5 on GPU 0: Task 9 ep 30/50, ~10min 剩余 (PID 560343)

新部署:
  - GPU 1: π0.5 L2norm k=0.5 Goal seed42 (PID 751406)
  - GPU 2: π0.5 Random k=0.7 Goal seed42 (PID 751480)
  - GPU 3: π0.5 L2norm k=0.9 Goal seed42 (PID 751616)

X-VLA 可用: 否（/root/autodl-tmp/X-VLA-Libero 不存在）

⚠️ 注意: 3 个 Goal 实验在 registry 中已有来自其他服务器的结果:
  - L2norm k=0.5 Goal s42: SR=59.2% (westd-41074 之前跑过)
  - Random k=0.7 Goal s42: SR=80.6% (cqa1-33015)
  - L2norm k=0.9 Goal s42: SR=90.0% (westd-38929)
  如需停止重复实验改跑其他任务，请指示。
```

---
