# analysis c4 1b5 qwen rw check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4-1b5-qwen-rw-check_20260519T230027_result.json`
- **Structured JSON:** [`b1cc43e8d152ed6bb63a.json`](../../sessions/b1/b1cc43e8d152ed6bb63a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### qwen_rw 实验：已完成

**K\* = 2**（theta=0.6），训练耗时 3441s (~57min)。

| Pair | DeBERTa AUC | 95% CI | OBD Baseline | Delta |
|------|------------|--------|-------------|-------|
| 0v1 | **0.9923** | [0.9907, 0.9937] | 0.987 | +0.0053 |
| 1v2 | **0.7052** | [0.6977, 0.7129] | 0.6262 | **+0.0790** |
| 2v3 | 0.5988 | [0.5905, 0.6063] | 0.5496 | +0.0492 |
| 3v4 | 0.5698 | [0.5626, 0.5774] | 0.5294 | +0.0404 |
| 4v5 | 0.5475 | [0.5404, 0.5542] | 0.5182 | +0.0293 |

- 0v1 和 1v2 的 CI lower 均 > 0.6（theta），K\*=2
- DeBERTa 在所有 pair 上均优于 OBD baseline，1v2 提升最大（+7.9pp）

### GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|-------|---------|
| 0 | **0% 空闲** | 0 / 24564 MiB |
| 1 | 98% | 23337 / 24564 MiB |
| 2 | 97% | 23337 / 24564 MiB |
| 3 | 97% | 23221 / 24564 MiB |

### Cross-transfer 进度

3 个 GPU 都在跑 DeBERTa cross-transfer（PID 208306/208307/208308），已产出 6 个 JSON 结果。当前进度：
- **GPU1**: Ep 2 step 400/1500（第2轮早期）
- **GPU2**: Ep 3 step 800/1500（第3轮过半）
- **GPU3**: Ep 1 step 1200/1500（第1轮末期）

每个 GPU 跑多个 train→test 组合，按每组 ~10min 估算，还需若干小时完成全部组合。

---
