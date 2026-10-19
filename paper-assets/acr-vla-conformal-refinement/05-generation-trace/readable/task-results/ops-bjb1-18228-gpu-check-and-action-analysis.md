# ops bjb1 18228 gpu check and action analysis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-18228-gpu-check-and-action-analysis_20260517T223958_result.json`
- **Structured JSON:** [`154ae8a4416c0f00adbb.json`](../../sessions/15/154ae8a4416c0f00adbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存。

---

## 汇总报告

### Part 1: GPU 状态
| GPU | 状态 | 进程 |
|-----|------|------|
| GPU0 | 占用 | PID 713405 — K=5 eval seed42 |
| GPU1 | 空闲 | — |
| GPU2 | 空闲 | — |
| GPU3 | 占用 | PID 749547 — perdof seed45 |

K=20 (PID 713480) 已不存在，无需 kill。

### Part 2: OpenVLA Action 分布分析结果

**关键发现：OpenVLA 的 action generation 是 STOCHASTIC 的（`do_sample=True` 有效）。**

Dry-run 验证：
- Greedy (do_sample=False): 两次输出完全一致 (diff=0)
- Stochastic (do_sample=True, T=1.0): 三次输出 pairwise diff = [1.02, 0.11, 1.03]

**Per-temperature aggregate results (5 obs, K=10):**

| Temperature | Mean Pairwise Dist | DOF with Highest Variance |
|-------------|-------------------|--------------------------|
| 0.5 | 0.1746 | DOF6 (gripper): 0.048 |
| 1.0 | 0.3890 | DOF6 (gripper): 0.115 |
| 1.5 | 0.4988 | DOF6 (gripper): 0.147 |

**Per-DOF variance pattern (T=1.0):**
- DOF 0-2 (xyz position): low-moderate variance (0.003, 0.007, 0.029)
- DOF 3-5 (rotation): very low variance (~0.0005)
- DOF 6 (gripper): **highest variance (0.115)** — 因为 gripper 是二值化的 (open/close)，token-level 的微小概率差就导致 0/1 翻转

**初步结论：**
1. OpenVLA 支持 temperature sampling，K-sample 方法有意义
2. 多样性主要来自 gripper action 的离散翻转 + xyz 位移的小幅波动
3. 旋转轴 (DOF 3-5) 几乎无变化——模型对旋转预测高度确定
4. T=1.0 时 mean pairwise distance ≈ 0.39，表明 K=10 采样可以产生有意义的多样性
5. 结果保存于 `/root/acr-vla-conformal-refinement/results/openvla_action_analysis.json`

---
