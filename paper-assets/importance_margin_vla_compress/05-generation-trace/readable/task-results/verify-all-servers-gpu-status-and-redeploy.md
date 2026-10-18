# verify all servers gpu status and redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_all-servers-gpu-status-and-redeploy_20260525T213949_result.json`
- **Structured JSON:** [`eeeb77ecf6680cbb19a7.json`](../../sessions/ee/eeeb77ecf6680cbb19a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 675752（pi05 zero_mask_random）也一起死了，是 kill 的附带影响——可能和 775730 在同一进程组。

## GPU 状态报告

```
SERVER: westd-41074
  GPU0: [ALIVE] openvla random_prune k0.5 object (PID 76334)     | mem=15980 MiB | util=67%
  GPU1: [ALIVE] openvla l2norm_prune k0.5 object (PID 76492)     | mem=26871 MiB | util=72%
         + pi05 attention k0.925 libero_10 (PID 111302)
  GPU2: [ALIVE] openvla zeromask_random k0.9 object (PID 4687)   | mem=16016 MiB | util=64%
  GPU3: [ALIVE] openvla zeromask_l2norm k0.9 object (PID 5519)   | mem=16016 MiB | util=68%

SERVER: cqa1-33015
  GPU0: [FREE]  — pi05 zeromask_random k0.9 object (PID 675752) 死于 kill 附带影响
  GPU1: [FREE]  — l2norm k0.75 从未成功部署到此卡（误跑到 GPU0）
  GPU2: [ALIVE] pi05 zeromask_l2norm k0.9 object (PID 676529)   | mem=10335 MiB | util=54%
  GPU3: [ALIVE] openvla attn_prune k0.9 goal seed43 (PID 769077)| mem=15360 MiB | util=62%

SERVER: westd-27271
  GPU0: [ALIVE] openvla random_prune k0.7 goal (PID 683580)     | mem=15964 MiB | util=89%
  GPU1: [ALIVE] openvla l2norm_prune k0.9 goal seed43 (PID 675712)| mem=15964 MiB | util=71%
```

### FREE GPUs: cqa1 GPU0, cqa1 GPU1

### 需要重新部署的实验
1. **pi05 l2norm k0.75 libero_10** — 原本要部署到 cqa1 GPU1，结果误跑到 GPU0，已 kill → 需重新部署到 **cqa1 GPU1**
2. **pi05 zero_mask_random k0.9 libero_object** — 在 cqa1 GPU0 上正常运行，kill 775730 时被附带杀死 → 需重新部署到 **cqa1 GPU0**

### 与预期不符之处
- **cqa1 GPU2 无重复进程**（Director 报告有误），只有 PID 676529 一个进程
- **westd-41074 原始 PID 3978/4339 已死**，但已被新 PID 76334/76492 替代（同实验，应为自动重启）
- **cqa1 原始 PID 617871/619617 已死**，也已被新进程替代

---
