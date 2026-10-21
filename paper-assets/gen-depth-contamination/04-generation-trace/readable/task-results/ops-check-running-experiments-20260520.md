# ops check running experiments 20260520

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_running_experiments_20260520_20260520T131530_result.json`
- **Structured JSON:** [`7d919600265fa593a328.json`](../../sessions/7d/7d919600265fa593a328.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

```
exp_7b_scorer_arxiv (PID 320673): 已退出（正常完成） | GPU: 已释放
```

21:14:37 Pipeline complete. 结果摘要：

| Config | K* | 0v1 AUC | 1v2 AUC | 2v3 AUC |
|---|---|---|---|---|
| pythia_arxiv\_\_qwen1.5b | 3 | 0.9872 | 0.7938 | 0.6544 |
| olmo_arxiv\_\_qwen1.5b | 1 | 0.9954 | 0.5182 | 0.4956 |
| pythia_arxiv\_\_qwen7b | 3 | 0.9844 | 0.7987 | 0.6551 |
| olmo_arxiv\_\_qwen7b | 1 | 0.9941 | 0.5089 | 0.4920 |

结论：7B scorer 和 1.5B scorer 在两个 model family 上 K\* 完全一致（pythia=3, olmo=1）。

---

```
exp_olmo_retrain_v3 (PID 310312): 存活 | 运行时长 2h27m | GPU: cuda:0 (非 cuda:2)，当前 0% 利用率
```

进度：
- Generation chain (depth 0→4): **已完成** (18:48 - 20:13，耗时 ~1h25m)
- Feature extraction (5 depths × 5000 texts): **已完成** (20:13 - 20:32)
- Pairwise AUC/JSD: **已完成** — AUC(0v1)=0.9873, AUC(1v2)=0.8889, AUC(2v3)=0.7036, AUC(3v4)=0.6817, **K\*=4**
- **Bootstrap CI (10000 resamples): 进行中** — 已完成 1/4 对 (0v1: 0.9972 [0.9967, 0.9977]，耗时 32 min)，当前在跑后续 pair

GPU 利用率 0% 是正常的，Bootstrap 阶段跑的是 LGBMClassifier（CPU-bound），不用 GPU。日志尾部全是 sklearn feature name 警告，不影响结果。

**预计完成时间**：每对 bootstrap 约 32 min，剩余 3 对 ≈ 96 min，预计 **~22:40** 完成。

---
