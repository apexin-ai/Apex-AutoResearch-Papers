# ops idle gpu audit and fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_idle-gpu-audit-and-fill_20260521T011154_result.json`
- **Structured JSON:** [`d856ff02718832229ff1.json`](../../sessions/d8/d856ff02718832229ff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full audit:

---

## westd-38929 (4 GPU 全空闲)

```
GPU: westd-38929:cuda:0
Experiment: eval_openvla_prune_random_k095_seed42_v2
Status: INCOMPLETE (died mid-run, no error in log)
Progress: ~task 4/10, partial results: T0=40/50, T1=21/50, T2=35/50, T3=19/40(中断)
Log: /root/autodl-tmp/importance_margin_vla_compress/logs/eval_random_k095_seed42_v2.log

GPU: westd-38929:cuda:1
Experiment: eval_openvla_prune_random_k07_seed42_v2
Status: INCOMPLETE (died mid-run, no error in log)
Progress: ~task 4/10, partial results: T0=36/50, T1=10/50, T2=28/50, T3=10/30(中断)
Log: /root/autodl-tmp/importance_margin_vla_compress/logs/eval_random_k07_seed42_v2.log

GPU: westd-38929:cuda:3
Experiment: eval_openvla_prune_l2norm_k09_seed43_v2
Status: INCOMPLETE (died mid-run, no error in log)
Progress: ~task 4/10, partial results: T0=33/50, T1=29/50, T2=33/50, T3=20/40(中断)
Log: /root/autodl-tmp/importance_margin_vla_compress/logs/eval_l2norm_k09_seed43_v2.log

GPU: westd-38929:cuda:2
Experiment: smolvla_baseline_spatial_seed42
Status: CRASHED
Error: FileNotFoundError — missing asset 'tabletop_table_Cobblestone01_GLOSS_6K.xml'
Log: /root/autodl-tmp/importance_margin_vla_compress/logs/smolvla_baseline_spatial_seed42.log
```

**westd-38929 三个 Object eval 全部在 task 4/10 附近无声死亡（无 error/traceback），需要重跑。SmolVLA Spatial 因 LIBERO 资源文件缺失 crash。**

---

## cqa1-33015:cuda:2

```
GPU: cqa1-33015:cuda:2
Experiment: eval_xvla_spatial_k05_seed42
Status: COMPLETED ✓
Success Rate: 58.8% (294/500), 95% CI [54.4%, 63.0%]
Per-task: T0=94%, T1=22%, T2=90%, T3=74%, T4=88%, T5=0%, T6=78%, T7=30%, T8=74%, T9=38%
Log: /root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_spatial_k05_seed42.log
Results: eval_results/xvla_spatial_k05_seed42.json
```

附注：cqa1-33015 上另有 3 个 eval 仍在跑（eval_xvla_goal_k05, goal_k09, baseline_long，均在 Ep 30-39/50 进度）。

---

## westd-41074:cuda:0

```
GPU: westd-41074:cuda:0
Experiment: eval_openvla_prune_random_k05_seed42
Status: NOT FOUND — 无对应日志文件
```

该服务器上找到的相关结果：
- `eval_random_k09_seed42` — **完成，64.6%** (323/500)
- `eval_openvla_random_k095_seed43` — **完成，66.8%** (334/500)
- `eval_openvla_random_k05_seed43` — 死于 Ep30/50 task1，0% success（不同 seed）

`eval_openvla_prune_random_k05_seed42` 可能从未在此服务器启动，或日志名不同。

---
