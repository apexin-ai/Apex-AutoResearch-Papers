# diag gpu tempcurve check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-tempcurve-check_20260518T024351_result.json`
- **Structured JSON:** [`8787ac65d9859b45be6a.json`](../../sessions/87/8787ac65d9859b45be6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| 0 | RTX 5090 | 6193 / 32607 MiB | 64% | python (PID 45500) |

GPU 正在跑温度曲线生成任务。

## 2. tmux session

```
tc_fix: 1 windows (created Mon May 18 06:33:41 2026)
```

tc_fix 存在且正在运行。

## 3. tc_fix 进度

脚本 `run_temp_curve_fix.sh` 有 3 个串行阶段（生成）+ 3 个特征提取：

| 阶段 | 状态 | 详情 |
|------|------|------|
| [1/3] Pythia-2.8B t=0.5 | **完成** | 4708 records, 12064.7s, skipped 113 |
| [2/3] Pythia-2.8B t=0.9 | **运行中** | 392/995 seeds (39%), ~7.6s/it |
| [3/3] Qwen3-1.7B t=0.9 | 等待中 | — |
| 特征提取 (×3) | 等待中 | — |

**预计完成时间**：t=0.9 剩余 ~603 seeds × 7.6s ≈ 76 min。之后 Qwen3-1.7B t=0.9 约 3h，特征提取约 30 min。总计约 **5-6 小时后全部完成**。

## 4. 已有温度曲线结果 (temp_curve_binary_logo.json)

已完成的 LOGO-CV 评估（单模型温度变化）：

| 模型 | 温度 | Binary F1 | 95% CI |
|------|------|-----------|--------|
| **Pythia-2.8B** | 0.7 | 0.7395 | [0.7254, 0.7548] |
| **Qwen3-1.7B** | 0.5 | 0.7506 | [0.7348, 0.7656] |
| **Qwen3-1.7B** | 0.7 | 0.7505 | [0.7345, 0.7664] |
| **Qwen3-1.7B** | 1.0 | 0.3670 | [0.3525, 0.3813] |

Qwen3-1.7B 在 t=0.5 和 t=0.7 几乎相同，t=1.0 断崖式下降。Pythia t=0.5 和 t=0.9 的结果需等当前生成完成后才能评估。

## 5. Cross-temperature transfer (cross_temp_transfer.json)

| Train→Test | Binary F1 | 3-class F1 |
|------------|-----------|------------|
| 0.7→0.7 | 0.9471 | 0.7888 |
| 0.7→1.0 | 0.9001 | 0.7225 |
| 1.0→1.0 | 0.9107 | 0.7257 |
| 1.0→0.7 | 0.9581 | 0.7913 |

跨温度转移 delta：0.7 训练到 1.0 测试 binary F1 下降 4.7pp，反向提升 4.7pp。

## 6. Independent-seed 实验结果

| 训练集 | 测试集 | Binary F1 | 95% CI |
|--------|--------|-----------|--------|
| Pythia-2.8B (SetA) | OLMo-2-1B (SetB) | 0.6945 | [0.6727, 0.7167] |
| OLMo-2-1B (SetB) | Pythia-2.8B (SetA) | 0.6660 | [0.6429, 0.6893] |

平均 binary F1 = 0.6803，vs 共享 seed LOGO 参考值 0.694，差距仅 -0.0137。

---
