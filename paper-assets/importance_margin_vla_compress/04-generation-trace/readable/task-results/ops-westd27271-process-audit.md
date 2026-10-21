# ops westd27271 process audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271-process-audit_20260520T173201_result.json`
- **Structured JSON:** [`52c2291be8968866129c.json`](../../sessions/52/52c2291be8968866129c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 进程 1: pid=17634 (GPU 0) — random_prune k=0.7 seed=43
- **来源**: `nohup bash run_openvla_prune_seed43.sh`，已运行 ~6h20m
- **运行时间**: ~2h（当前 k=0.7 阶段）
- **进度**: Task 5/10 (ketchup), Ep 20/50，约 40% 完成
- **前序结果**: k=0.9 seed=43 已完成，SR=**62.2%** (311/500)

### 进程 2: pid=43505 (GPU 1) — l2norm_prune k=0.5 seed=42
- **来源**: `nohup bash run_openvla_l2norm_sweep.sh`，已运行 ~5h38m
- **运行时间**: ~41min（当前 k=0.5 阶段）
- **进度**: Task 2/10 (cream cheese), Ep 10/50，非常早期
- **前序结果**: l2norm k=0.7 已完成，SR=**49.8%** (249/500)

### D108 l2norm k=0.7 结果（已完成）
- **SR = 49.8%** (249/500)，耗时 296.9 min
- 保留 179/256 tokens (70%)
- 文件: `openvla_l2norm_prune_k0_7_object.json`

### M32 训练进度
- **Step 21,600 / 100,000** (21.6%)
- loss ~2.4–3.6, lr=8.99e-05, sps=0.5
- tmux session `train_openvla_sc_m32_seed42`，已跑 ~6h45m
- 与 l2norm eval 共享 GPU 1

### 建议
- **让两个 eval 继续跑**，都是合法的 sweep 脚本，正在产出有用数据
- **关注 GPU 1 内存压力** — l2norm eval + M32 训练同时跑在 GPU 1 上，如果出现 OOM 或显著降速需要干预
- 建议将这两个 sweep 补注册到 registry，避免后续再出现"未注册进程"的困惑

---
