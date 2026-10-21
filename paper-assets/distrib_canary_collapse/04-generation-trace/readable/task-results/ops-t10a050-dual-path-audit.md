# ops t10a050 dual path audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_t10a050-dual-path-audit_20260522T191819_result.json`
- **Structured JSON:** [`a134d116f82871bd1ec8.json`](../../sessions/a1/a134d116f82871bd1ec8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据溯源完成。汇报如下：

---

## 路径溯源结果

### 路径 1: `results/phase_diagram/t10_a050_s42_fp32_14b/`
| 项目 | 值 |
|------|-----|
| 创建时间 | 2026-05-22 14:43 (UTC+8) |
| gen 数 | 11 (gen_0–gen_10), 完整 |
| exp_id | `scale_14b_t10_a050_s42_fp32_v2` |
| 模型 | **pythia-1.4b-deduped** |
| gen_batch_size | 8 |
| start_gen | **2**（从失败的 `_19828` 运行恢复，gen_0/1 是前次残留） |
| all_metrics | `.json.bak`（无 `.json`） |
| PermG FDR fwd | **4/8**, robust pairs 3/8 |
| 结论 | negative |

### 路径 2: `results/scale/14b_a050_s42_fp32/`
| 项目 | 值 |
|------|-----|
| 创建时间 | 2026-05-20 13:49 (UTC+8) |
| gen 数 | 11 (gen_0–gen_10), 完整 |
| exp_id | `scale_14b_a050_s42_fp32` |
| 模型 | **pythia-1.4b**（非 deduped） |
| gen_batch_size | 16 |
| start_gen | 0（完整运行，10.66 GPU-hours） |
| all_metrics | `.json`（正常） |
| PermG FDR fwd | **0/8**, robust pairs 0/8 |
| 结论 | negative |

---

## 关键差异

**两条路径使用了不同的基础模型**，这是 PermG 4/8 vs 0/8 差异的根本原因：

1. **模型不同**: 路径 1 用 `pythia-1.4b-deduped`，路径 2 用 `pythia-1.4b`（HF cache 确认两者都存在：`/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped/` 和 `hub/models--EleutherAI--pythia-1.4b/`）
2. **gen_batch_size 不同**: 8 vs 16（影响 metrics 计算的样本量）
3. **gen_0 baseline 不同**: entropy 2.973 vs 2.946, perplexity 19.83 vs 19.68（确认不是同一模型）
4. **路径 1 是 resume 运行**: gen_0/1 从失败运行继承，gen_2 起新训练；路径 2 是完整从头运行

## 结论

**两条路径都不是对方的复制品**——它们是对两个不同模型的独立实验。两者都是完整有效的运行，但不可直接比较。

- 如果项目标准模型是 `pythia-1.4b`（与 410M 实验一致的 Pythia 系列），**路径 2（scale）是正统数据，PermG=0/8**
- 路径 1 使用了 deduped 变体，是后来的 retry 在模型路径上引入了偏差（`/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped` 被当作 1.4b 使用）

建议确认：其他 scale 实验（410M 等）使用的是 `pythia-410m` 还是 `pythia-410m-deduped`，以判断哪个模型系列是项目标准。

---
