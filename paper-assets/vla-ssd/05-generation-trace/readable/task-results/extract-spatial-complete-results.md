# extract spatial complete results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_spatial_complete_results_20260522T111238_result.json`
- **Structured JSON:** [`da2b27e73c42cf4748b9.json`](../../sessions/da/da2b27e73c42cf4748b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 0 / 97887 MiB |
| 1 | 0% | 0 / 97887 MiB |

两卡完全空闲，实验进程已退出。

---

### 2. cuda:0 — OpenVLA Trained CF (libero_spatial)
**已完成** — 18:40:51 结束，耗时 95.0 min

脚本: `libero_spatial_full_pipeline.py --conditions trained --only-counterfactual`
Checkpoint: `openvla-7b-finetuned-libero-spatial`
输出: `results/libero_spatial/counterfactual_combined.json`

| Condition | Cohen's d (global) | Cross-task mean d | token_div |
|-----------|-------------------|-------------------|-----------|
| **empty** | **1.1734** | 1.1813 | 1.000 |
| shuffled | 0.9787 | 0.9940 | 0.998 |
| wrong | 0.8849 | 0.9146 | 0.995 |
| paraphrased | 0.8070 | 0.8157 | 0.941 |

**Ordering: empty > shuffled > wrong > paraphrased**

---

### 3. cuda:1 — OpenVLA Untrained Full Pipeline (libero_spatial_untrained)
**已完成** — 18:58:41 结束，耗时 104.1 min

脚本: `libero_spatial_full_pipeline.py --conditions untrained`
Checkpoint: `openvla-7b` (未微调)
输出: `results/libero_spatial_untrained/`

**CF 结果:**

| Condition | Cohen's d (global) | Cross-task mean d | token_div |
|-----------|-------------------|-------------------|-----------|
| **empty** | **0.9361** | 0.9502 | 1.000 |
| shuffled | 0.7967 | 0.8010 | 1.000 |
| wrong | 0.7944 | 0.8005 | 1.000 |
| paraphrased | 0.7582 | 0.7619 | 0.991 |

**Ordering: empty > shuffled ≈ wrong > paraphrased** (与 trained 一致)

**Trained vs Untrained 对比:**

| Condition | Trained d | Untrained d | Delta |
|-----------|-----------|-------------|-------|
| empty | 1.1734 | 0.9361 | +0.237 |
| shuffled | 0.9787 | 0.7967 | +0.182 |
| wrong | 0.8849 | 0.7944 | +0.091 |
| paraphrased | 0.8070 | 0.7582 | +0.049 |

Trained 全面高于 untrained，但 untrained 也有显著效应（所有 d > 0.75）。Empty 和 shuffled 的 delta 最大；paraphrased 差异最小。

**其他 phases** (untrained 全部完成): action_r2_probing.json, l1_attention_profile.json, cross_instruction_classification.json, rsa_analysis.json 均已生成。

---

### 4. NLP Control (Llama-2-7b-chat)
- **下载中** — PID 612753 存活，shard 1 已下载 7.6 GB（临时目录），尚未移到最终位置
- **wait_and_run** — PID 613202 存活，仍在等待下载完成（run.log: "Waiting for model download to complete..."）
- probing 尚未启动

---
