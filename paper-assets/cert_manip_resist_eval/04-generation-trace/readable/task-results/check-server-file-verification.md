# check server file verification

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_server-file-verification_20260523T010057_result.json`
- **Structured JSON:** [`2cd60d36c80241d6e00b.json`](../../sessions/2c/2cd60d36c80241d6e00b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查结果汇总：

**三个文件全部存在** ✓

| 文件 | 路径 | 大小 | 时间 |
|------|------|------|------|
| K=5 wild cluster bootstrap | `artifacts/results/plan001/k5_wild_cluster_bootstrap.json` | 13.2 KB | May 23 08:52 |
| Partial-knowledge adversary | `artifacts/results/plan001/partial_knowledge_adversary.json` | 20.1 KB | May 23 08:50 |
| Framework figure (PDF) | `artifacts/figures/fig_framework.pdf` | 48.3 KB | May 23 08:54 |
| Framework figure (PNG) | `artifacts/figures/fig_framework.png` | 202.5 KB | May 23 08:54 |

**无残留 bootstrap 进程**——服务器上没有相关 python 进程在跑。

**K5 bootstrap 结果摘要**（前 100 行）：
- 方法：`wild_cluster_bootstrap_k5`，K=5，B=9999 次重采样，Rademacher 权重
- 回归模型：`log(ASR+1e-6) ~ log(K_eff) + log(eta_max+1e-6)`
- 每个 condition 有 3003 个 panel，11 个 cluster
- `mmluxprompt_injection`：K_eff final_p=0.0016（显著），eta final_p=0.0329
- `mmluxsycophancy`：K_eff final_p=0.0103（显著），eta final_p=0.0276

---
