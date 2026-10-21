# ops audit westd41074 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd41074_v2_20260522T054004_result.json`
- **Structured JSON:** [`b34f236654795d1739de.json`](../../sessions/b3/b34f236654795d1739de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

**GPU 3 并非空闲。** PID 59671 仍然活着，占用 27.5 GB 显存。

### 4 卡真实状态

| GPU | 利用率 | 显存占用 | 实验 | PID | 状态 |
|-----|--------|----------|------|-----|------|
| 0 | 31% | 10.6/97.9 GB | eval_pi05_l2norm_k0925_spatial_seed42 | 132954 | 运行中 |
| 1 | 45% | 21.2/97.9 GB | eval_pi05_random_k095_object_seed43 + eval_pi05_l2norm_k0925_spatial_seed43 | 121033, 133121 | 运行中（双 eval 共卡） |
| 2 | 0% | 28.6/97.9 GB | train_openvla_sc_m96_seed42 | 68539 | 运行中（CPU 9411min） |
| 3 | 0% | 27.5/97.9 GB | train_openvla_sc_m64_seed42_v6 | 59671 | 运行中（CPU 4002min） |

### 分析

- GPU 2/3 利用率显示 0% 但显存满载且进程活跃（CPU 时间在累积），这是训练过程中 data loading 或 checkpoint 保存期间的正常现象
- GPU 1 实际运行了 2 个 eval（registry 中未列出 eval_pi05_random_k095_object_seed43 在此 GPU）
- **无空闲 GPU**，无法部署 eval_pi05_random_k07_spatial_seed43

### 结论

系统"GPU 3 空闲"的报告是误判——可能基于瞬时 utilization=0% 判断，但进程和显存均正常。跳过部署步骤。

---
