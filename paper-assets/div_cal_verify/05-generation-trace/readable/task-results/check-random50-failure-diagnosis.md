# check random50 failure diagnosis

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_random50_failure_diagnosis_20260513T151711_result.json`
- **Structured JSON:** [`d25171144570c2ed3133.json`](../../sessions/d2/d25171144570c2ed3133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**random50_v2 实际上已经成功完成，不需要重跑。** 监控系统误报了失败。

### 两次实验的情况

| 实验 | 状态 | 原因 |
|------|------|------|
| **phase2_random50_baseline** | 真正失败 | 脚本设了 `TRANSFORMERS_OFFLINE=1` 但模型未缓存，导致无法从 HuggingFace 下载 gpt2 和 facebook/contriever，网络全部超时 |
| **phase2_random50_v2** | 已成功完成 | 移除了 `TRANSFORMERS_OFFLINE=1`，通过 `env.sh` 的 `HF_ENDPOINT=https://hf-mirror.com` 成功下载模型，跑完 8 代（gen 0-7） |

### v2 完整结果

结果目录 `/root/autodl-tmp/phase-gated-compound-sparse/results_random50/random_50/`，包含 `all_results.json` + gen_0 到 gen_7 各有 `metrics.json`。

最终摘要：

```
 Gen      PPL   RankMe      kNN     Rare     Corr
   0    36.87   275.24   0.9880   0.0290  -0.0081
   1    44.34   292.46   0.9880   0.0193  -0.0360
   2    49.75   295.61   0.9880   0.0143  -0.0315
   3    49.00   295.28   0.9880   0.0125  -0.0238
   4    50.85   297.01   0.9880   0.0113  -0.0209
   5    47.31   292.81   0.9880   0.0104  -0.0207
   6    44.78   293.42   0.9880   0.0099  -0.0290
   7    43.20   291.38   0.9880   0.0096  -0.0391
```

### GPU 状态

两块 RTX PRO 6000 (98GB) 均空闲，无运行进程。GPU 0 显示 49GB 显存占用但无进程——可能是之前实验的残留缓存，不影响使用。

### 磁盘

- `/root/autodl-tmp/`: 236G 可用（6%）
- `/root/`: 7.5G 可用（76%）

**结论：无需修复或重跑。v2 的结果已完整产出，可直接用于对比分析。**

---
