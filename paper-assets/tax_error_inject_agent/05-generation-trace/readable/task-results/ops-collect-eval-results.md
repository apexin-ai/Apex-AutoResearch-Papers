# ops collect eval results

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-eval-results_20260516T084951_result.json`
- **Structured JSON:** [`87f2a73ac9378c8cb4d9.json`](../../sessions/87/87f2a73ac9378c8cb4d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## GPU 状态

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX 5090 | **0%** | 0 / 32607 MiB — **空闲** |
| 1 | RTX 5090 | **88%** | 16837 / 32607 MiB — 活跃 |
| 2 | RTX 5090 | **89%** | 16837 / 32607 MiB — 活跃 |
| 3 | RTX 5090 | **99%** | 28685 / 32607 MiB — 活跃（训练） |

---

## Eval 结果

### LLaMA-31 Vanilla s42 (`llama31_vanilla_s42.json`)
- **recovery_rate: 74.5%**
- **detection_rate: 21.3%**
- C1_context_truncation: rec 75.0%, det 16.7%
- C4_observation_masking: rec 72.7%, det 27.3%
- P1_step_order_swap: rec 75.0%, det 16.7%
- P2_sub_goal_deletion: rec 75.0%, det 25.0%

### LLaMA TaxEI s42 / LLaMA Random s42
**文件不存在。** `eval_results/` 下无 `llama31_taxei*` 或 `llama31_random*` 文件，上一 session 的 eval 可能未完成或结果写到了其他位置。

### Vanilla Recovery s7 (`v4_vanilla_recovery_eval_s7.json`)
- Model: mini_vanilla_sft_v4_seed7/checkpoint-1635
- **recovery_rate: 74.5%**
- **detection_rate: 0.0%**
- C1: 75.0% | C4: 72.7% | P1: 75.0% | P2: 75.0%

### Vanilla Recovery s1 (`v4_vanilla_recovery_eval_s1.json`)
- **recovery_rate: 66.0%**
- **detection_rate: 0.0%**
- C1: 66.7% | C4: 54.5% | P1: 66.7% | P2: 75.0%

### TaxEI-RP Injected Evals（全部 detection_rate = 0%）

| Seed | Recovery Rate | C1 | C4 | P1 | P2 |
|------|--------------|-----|-----|-----|-----|
| s42 | **38.3%** | 50.0% | 27.3% | 50.0% | 25.0% |
| s0 | **46.8%** | 33.3% | 45.5% | 50.0% | — |
| s123 | **57.4%** | 58.3% | 45.5% | 66.7% | — |
| s1 | **48.9%** | 41.7% | 36.4% | 75.0% | — |

---

## v4-taxei-rp-s7 训练状态

**正在训练中**，GPU 3 承载。

- 进度: **3510 / 5415 steps (64.8%)**
- Epoch: ~1.94
- Loss: 0.31–0.37, token_acc: ~0.889
- 已用时间: 2h 27m，预计剩余: **~1h 20m**
- checkpoint-1805 已保存
- 速度: 2.51 s/it

---

## Scale-up 收集进度

数据在 `trajectories_scaleup_p1/` 下以 `.jsonl` 格式存储（非 `.json`）：

- **成功轨迹: 239 条**
- **失败轨迹: 812 条**
- **总计: 1051 episodes**
- 最后写入: 2026-05-16 16:49（**仍在活跃写入**）

---

**关键发现：**
1. `llama31_taxei_s42` 和 `llama31_random_s42` 的 eval 结果文件缺失，需确认是否在其他路径或 eval 任务未启动
2. TaxEI-RP 模型 recovery rate 显著低于 Vanilla（38-57% vs 66-74%），且所有 detection_rate 都是 0%
3. GPU 0 当前空闲，可用于补跑缺失的 eval
4. v4-taxei-rp-s7 训练还有约 1.5h 完成

---
