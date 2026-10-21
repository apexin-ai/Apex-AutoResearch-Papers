# diagnose gpu and collect results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_and_collect_results_20260521T041934_result.json`
- **Structured JSON:** [`19ef8e6490076266c983.json`](../../sessions/19/19ef8e6490076266c983.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成（12 个实验 → DONE + metrics）。汇总如下：

---

## 1. GPU 状态

### autodl-5090
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0-3 | 0% | 2 MiB / 32.6 GB | **全部空闲** |

### autodl-5090-b
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 87% | 30.3 / 32.6 GB | fewnerd_t05_s456 (~63%, ETA ~37min) |
| 1 | 85% | 30.3 / 32.6 GB | fewnerd_t12_s456 (同期启动) |
| 2 | 0% | 2 MiB | **空闲** |
| 3 | 0% | 2 MiB | **空闲** |

### autodl-5090-c
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 98% | 31.4 / 32.6 GB | 14b_inference_fewnerd (运行中) |
| 1 | 0% | 0 MiB | **空闲** |
| 2 | 78% | 29.9 / 32.6 GB | fewnerd_7b_n16_s42 (~65%, ETA ~64min) |
| 3 | 0% | 0 MiB | **空闲** |

---

## 2. 已完成实验 (12个, registry 已更新)

### 32B 模型 (高优先级)
| 实验 | greedy_F1 | oracle_F1 | ρ_SJ | ρ_adv | Verdict |
|------|-----------|-----------|------|-------|---------|
| **32b_fewnerd_n8_s42** | **0.800** | **0.879** | **0.320** | 0.078 | MARGINAL |

### FewNERD T-ablation
| T | Seed | greedy_F1 | oracle_F1 | ρ_SJ | ρ_adv | degen% | Verdict |
|---|------|-----------|-----------|------|-------|--------|---------|
| 0.5 | 123 | 0.789 | 0.864 | 0.350 | 0.055 | 13.5 | MARGINAL |
| 0.8 | 123 | 0.789 | 0.884 | 0.336 | 0.116 | 16.7 | MARGINAL |
| 0.8 | 456 | 0.788 | 0.877 | 0.328 | 0.126 | 16.3 | MARGINAL |
| 1.2 | 123 | 0.789 | 0.887 | 0.285 | 0.122 | **24.7** | **FAIL** |

### SciERC T-ablation
| T | Seed | greedy_F1 | oracle_F1 | ρ_SJ | ρ_adv | degen% | Verdict |
|---|------|-----------|-----------|------|-------|--------|---------|
| 0.5 | 123 | 0.665 | 0.743 | 0.322 | 0.026 | 10.0 | MARGINAL |
| 0.5 | 456 | 0.663 | 0.746 | 0.326 | 0.054 | 10.3 | MARGINAL |
| 0.8 | 123 | 0.662 | 0.773 | 0.382 | 0.084 | 11.2 | MARGINAL |
| 0.8 | 456 | 0.664 | 0.769 | 0.362 | 0.118 | 11.9 | MARGINAL |
| 1.2 | 123 | 0.664 | 0.788 | 0.346 | 0.124 | 13.9 | MARGINAL |
| 1.2 | 456 | 0.663 | 0.782 | **0.420** | 0.099 | 14.1 | **PASS** |

### CoNLL N-scaling
| 实验 | greedy_F1 | oracle_F1 | ρ_SJ | ρ_adv | degen% | Verdict |
|------|-----------|-----------|------|-------|--------|---------|
| **conll_n16_s42** | **0.908** | **0.959** | **0.446** | 0.019 | 7.8 | **PASS** |

---

## 3. 仍在运行 (4个)
| 实验 | 服务器 | GPU | 进度 | ETA |
|------|--------|-----|------|-----|
| exp_fewnerd_t05_s456 | 5090-b | cuda:0 | 63% | ~37min |
| exp_fewnerd_t12_s456 | 5090-b | cuda:1 | ~同上 | ~37min |
| exp_14b_inference_fewnerd | 5090-c | cuda:0 | 进行中 | 未知 |
| exp_fewnerd_7b_n16_s42 | 5090-c | cuda:2 | 65% | ~64min |

---

## 4. 空闲 GPU 清单 (供 P1 分配)

| 服务器 | 空闲 GPU | 数量 |
|--------|----------|------|
| **autodl-5090** | cuda:0, 1, 2, 3 | **4** |
| autodl-5090-b | cuda:2, 3 | 2 |
| autodl-5090-c | cuda:1, 3 | 2 |
| **合计** | | **8 GPU** |

autodl-5090 的 4 卡全部空闲，适合立即调度大批量任务。5090-b 和 5090-c 各有 2 卡空闲，约 37-64 分钟后还将释放 4 卡。

---
