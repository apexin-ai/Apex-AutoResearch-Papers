# monitor running experiments check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_running-experiments-check_20260515T194606_result.json`
- **Structured JSON:** [`80faa28bde0a91fc19d5.json`](../../sessions/80/80faa28bde0a91fc19d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

**GPU 状态** — 4x RTX 5090 全部活跃

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 77% | 18.0/31.8 GB |
| cuda:1 | 100% | 18.0/31.8 GB |
| cuda:2 | 96% | 20.6/31.8 GB |
| cuda:3 | 89% | 22.0/31.8 GB |

**进程** — 4 个 PID 全部存活（398981/405526/400279/381618 均 ALIVE）

---

### 逐实验详情

**cuda:0 — cls8b-s42-resume-val-sweep-seq8192-v2** ✅
- 进度: 6840/9335 (73.3%), running_acc=86.3%
- 速率: ~10 samples/1.5s，当前 sweep 配置剩余 ~6 min
- 运行时间: 2h04m
- 预测 ETA ~May 16 10:50 UTC — 取决于剩余多少 sweep 配置，当前配置即将完成，总体在合理范围内

**cuda:1 — cls8b-s42-resume-val-sweep-gpu1** ✅
- 进度: 2600/9335 (27.9%), running_acc=89.5%
- 速率: ~10 samples/2s，当前 sweep 配置剩余 ~22 min
- 运行时间: 59m
- 启动较晚，进度正常

**cuda:2 — repo-level-cwm-8b-conda-v5** ✅
- 进度: 4403/9335 (47.2%)
- 速率: ~8.3 it/s，当前 bar 剩余 ~10 min
- 运行时间: 1h55m
- 预测 ETA ~May 16 05:30 UTC — 看起来在轨

**cuda:3 — cwm8b-ckpt400-test-eval** ⚠️ 进度偏慢
- 进度: 2984/9784 (**30.5%**)，running_acc=64.1%
- 速率: 8 samples/~57s → ~8.4 samples/min
- 运行时间: **5h08m**
- 剩余 6800 samples / 8.4 per min ≈ **13.5 小时**
- **推算 ETA: ~May 16 17:15 UTC**，比预测的 09:15 UTC **晚约 8 小时**
- 无 OOM/error，但速率持续偏低。可能原因：per-sample 推理开销比预估大（repo-level CWM eval 涉及更长上下文？）

**磁盘**: 150G/250G (60%), 剩余 101G，无风险。

---

**结论**: cuda:0/1/2 三个实验正常运行。cuda:3 的 `cwm8b-ckpt400-test-eval` ⚠️ 严重落后于预期，按当前速率要到 May 16 ~17:00 UTC 才能跑完。需要决定是否继续等待或采取措施（比如检查是否有不必要的重复计算可优化）。

---
