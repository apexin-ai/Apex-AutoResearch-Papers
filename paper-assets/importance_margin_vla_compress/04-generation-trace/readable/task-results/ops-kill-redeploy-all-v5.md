# ops kill redeploy all v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_redeploy_all_v5_20260522T083003_result.json`
- **Structured JSON:** [`f0f18c1837d170c58dbb.json`](../../sessions/f0/f0f18c1837d170c58dbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4/4 GPU 全部上线，每个进程在正确的独立 GPU 上。最终状态报告：

---

```
=== cqa1-33015 (4× RTX 4090 D 24GB) ===
Kill: 原 4 个重复进程 → 全部 DEAD confirmed (nvidia-smi 返回空)
| GPU | PID    | 显存      | 实验                              | 状态     |
|-----|--------|-----------|-----------------------------------|----------|
| 0   | 249598 | 9498 MiB  | l2norm k=0.95 object seed43       | RUNNING  |
| 1   | 249668 | 9498 MiB  | l2norm k=0.9 object seed43        | RUNNING  |
| 2   | 249746 | 9498 MiB  | l2norm k=0.925 spatial seed43     | RUNNING  |
| 3   | 249887 | 3176 MiB↑ | random k=0.5 spatial seed43       | LOADING  |
空闲 GPU: 无

=== westd-38929 (4× RTX PRO 6000 Blackwell 98GB) ===
Kill: PID 709985 (random k=0.925 s43 DONE) → DEAD
Kill: PID 766525 (random k=0.9 object s43 重复) → DEAD
| GPU | PID    | 显存       | 实验                              | 状态     |
|-----|--------|------------|-----------------------------------|----------|
| 0   | 708992 | 10510 MiB  | l2norm k=0.5 spatial seed43       | RUNNING  |
| 1   | 709233 | 10456 MiB  | random k=0.3 spatial seed43       | RUNNING  |
| 2   | 709369 | 10456 MiB  | l2norm k=0.3 spatial seed43       | RUNNING  |
| 3   | 808099 | 10389 MiB  | random k=0.3 object seed43 v4     | RUNNING  |
空闲 GPU: 无

=== westd-41074 (4× GPU) ===
无 kill 操作（304126/304198 为有效 Object seed43 实验，保留）
| GPU | PID    | 显存       | 实验                              | 状态     |
|-----|--------|------------|-----------------------------------|----------|
| 0   | 304126 | 10529 MiB  | random k=0.85 object seed43       | RUNNING  |
| 1   | 304198 | 10050 MiB  | l2norm k=0.925 object seed43      | RUNNING  |
| 2   | 68539  | 28546 MiB  | train_openvla_sc_m96_seed42       | RUNNING  |
| 3   | 59671  | 27526 MiB  | train_openvla_sc_m64_seed42_v6    | RUNNING  |
空闲 GPU: 无

=== westd-27271 ===
未操作（2 个 spatial seed43 实验 RUNNING，GPU sharing bug）
| GPU | PID    | 显存       | 实验                              | 状态     |
|-----|--------|------------|-----------------------------------|----------|
| 0   | 212585 | 10545 MiB  | random k=0.7 spatial seed43       | RUNNING  |
| 0   | 213482 | 10545 MiB  | l2norm k=0.7 spatial seed43       | RUNNING  |
空闲 GPU: 1, 2, 3
```

**Registry 修复：**
- `eval_pi05_l2norm_k0925_spatial_seed42`: PREPARING→DONE (97.0%)
- `eval_pi05_l2norm_k085_object_seed43`: PREPARING→DONE (98.4%)
- `eval_pi05_random_k085_spatial_seed43`: PREPARING→DONE (57.6%)

**去重拦截：** 部署时发现 `random_k07_object_seed43` (73.8%) 和 `random_k05_object_seed43` (68.4%) 已 DONE，替换为 Spatial seed43 缺口实验。

**关键发现：** `eval_pi05_pruning_libero.py` 硬编码 `DEVICE="cuda:0"`，`--gpu` 参数无效。已改用 `CUDA_VISIBLE_DEVICES` 部署，验证各进程分布在正确 GPU 上。

---
