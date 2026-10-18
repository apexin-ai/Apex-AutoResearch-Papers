# inspect westd41074 gpu02 logs

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inspect_westd41074_gpu02_logs_20260526T030141_result.json`
- **Structured JSON:** [`25ed29436cf672986cd7.json`](../../sessions/25/25ed29436cf672986cd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息足够了。以下是汇总结果：

---

## westd-41074

### GPU0 — PID 303189 (ALIVE, 可能卡住)
- **实验**: OpenVLA Random k=0.85, libero_10 (Long), seed42 v2
- **命令**: `eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.85 --suite libero_10 --seed 42`
- **状态**: stat=Sl, 运行 1h21m
- **日志**: `/root/runs/importance_margin_vla_compress/eval_openvla_random_k085_long_seed42_v2.log`
- **进度**: Task 1/10, ep 40/50 (0.6 eps/min)
- **日志最后更新**: May 26 10:50 — **30+ 分钟无新输出，结合 GPU 利用率 0%，疑似卡住**

### GPU2 — PID 259181 (ALIVE, 可能卡住)
- **实验**: OpenVLA Attention k=0.7, libero_object, seed42
- **命令**: `eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_object --seed 42`
- **状态**: stat=Rl+, 运行 2h40m
- **日志**: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k07_object_seed42.log` (41 行)
- **进度**: Task 4/10, ep 40/50 (1.2 eps/min)
- **日志最后更新**: May 26 10:57 — **25+ 分钟无新输出，结合 GPU 利用率 0%，疑似卡住**

---

## 4 个 Stale RUNNING 实验

| # | exp_id | 状态 | overall_sr | 结果文件 |
|---|--------|------|-----------|---------|
| 1 | eval_pi05_random_k085_long_seed43_postfix | **COMPLETED** | **41.8%** (209/500) | `pi05_random_k0.85_libero_10_seed43.json` |
| 2 | eval_pi05_random_k09_long_seed43_postfix | **COMPLETED** | **35.6%** (178/500) | `pi05_random_k0.90_libero_10_seed43.json` |
| 3 | eval_pi05_l2norm_k03_long_seed42_postfix | **COMPLETED** | **36.6%** (183/500) | `pi05_l2norm_k0.30_libero_10_seed42.json` |
| 4 | eval_xvla_random_k05_spatial_seed43 (westd-38929) | **COMPLETED**, PID gone | **72.6%** (363/500) | `eval_xvla_random_k05_spatial_seed43.json` |

---

## westd-38929 — eval_xvla_random_k05_spatial_seed43 详情
- 模型: xvla, random mode, keep_ratio=0.5, 50→25 vision tokens
- Per-task: 100% / 38% / 88% / 92% / 88% / 0% / 94% / 68% / 92% / 66%
- 95% Wilson CI: [68.5%, 76.3%]
- 耗时 64.3 min

---

**结论**: 4 个 stale 实验均已完成，可在 registry 标记 DONE。westd-41074 的两个 GPU 进程（303189, 259181）虽然 PID 存在，但日志 25-30 分钟无更新且 GPU 利用率 0%，很可能已卡死，需要 kill 后重跑。

---
