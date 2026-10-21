# ops cqa1 status and tasks

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-status-and-tasks_20260518T092026_result.json`
- **Structured JSON:** [`706c76c1fd32c1a14eb4.json`](../../sessions/70/706c76c1fd32c1a14eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## 1. GPU 状态
**RTX 4090D — 完全空闲**（0 MiB / 24564 MiB, 0% utilization, 无 GPU 进程）

仅有后台 tensorboard + jupyter-lab 在运行，无任何 python 训练/eval/IRT 进程。

## 2. exp_006_mmlu_vanilla_2pl_fullitems
**已完成，不在运行。**
- 4 条 MCMC chain 的 CSV 文件均已生成（`vanilla_2pl_fullitems_chains/` 下 chain 1-4，162MB-296MB）
- 日志 `vanilla_2pl_tau_fullitems.log` 最后更新 May 17 23:27
- 无对应进程存活

最近完成的实验是 `mmlu_domain_irt_j16_qwen`（今天 11:45 完成，DONE_MARKER 已写入），8 个 MMLU domain + pooled 结果均已输出。

## 3. cqa1-21977 上可执行任务
**cqa1-21977 上目前没有待执行的 GPU 密集型任务。**

原因：
- 所有 ≤3B 的训练 (exp001)、信号计算 (exp002)、IRT fitting (exp006) 已全部完成
- 最新 IRT 实验（cross-family、domain gamma、vanilla 2PL、exclusion sensitivity、gamma prior sensitivity、random 300 baseline、J=16 Qwen-only）均已跑完
- 当前工作重心已转移到 **westd-29999**（4× RTX PRO 6000 96GB）做 7B/14B 五家族扩展训练
- cqa1-21977 的角色变为"等 westd 训练完 → 做 eval/signals/IRT"

## 4. 磁盘
119G / 169G（70%），51G 可用。exp001 35G、exp006 3.3G、exp002 737M。

**结论：cqa1-21977 空闲，无可执行任务。下一批任务要等 westd-29999 上 7B/14B SFT 完成后的 eval → signals → IRT 阶段。**

---
