# diagnose nora goal v3 exit check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_nora_goal_v3_exit_check_20260521T070606_result.json`
- **Structured JSON:** [`abc3d499779c6c708b6e.json`](../../sessions/ab/abc3d499779c6c708b6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全了。以下是完整诊断。

---

## 1. 状态：部分完成，untrained counterfactual 缺失

- **trained**: 4/4 JSON 文件全部写入 ✓ (action_r2_probing, l1_attention_profile, cross_instruction_classification, counterfactual_combined)
- **untrained**: 3/4 文件 ✓，**缺 counterfactual_combined.json** ✗
- 日志只有 89 行，仅记录到 trained Phase 4 开头（L1），untrained 部分无日志。无 error/traceback/OOM。推测 stdout 缓冲问题导致日志不完整，进程在 untrained counterfactual 阶段崩溃或静默退出。

---

## 2. Trained vs Untrained 两条件对比

两条件的 Phase 1-3 + trained Phase 4-5 全跑完，untrained Phase 4 (cross-instruction) 跑完，Phase 5 (counterfactual) 缺失。

---

## 3. 关键 Metrics（Raw）

### R² Probing (action_r2_probing.json)

| Layer | Trained img_mean | Trained last_pre | Untrained img_mean | Untrained last_pre |
|-------|-----------------|-----------------|--------------------|--------------------|
| L0 | 0.6860 | 0.6392 | 0.7277 | 0.5925 |
| L8 | 0.6898 | 0.6847 | 0.7317 | 0.6501 |
| **L9** | **0.6908** | **0.6875** | **0.7346** | 0.6496 |
| L10 | **0.6968** | 0.6815 | 0.7289 | 0.6441 |
| L16 | 0.6853 | 0.6730 | 0.7023 | 0.6514 |
| L24 | 0.6687 | 0.6509 | 0.6788 | 0.6464 |
| L32 | 0.6233 | 0.5994 | 0.6648 | 0.6381 |
| **L35** | **-0.0039** | **-0.0039** | **0.6556** | **0.6194** |

- **Trained peak**: L10 img_mean=0.6968, L9 last_pre=0.6875
- **Untrained peak**: L9 img_mean=0.7346, L8 last_pre=0.6501
- **L35 trained**: R² 崩塌到 -0.004（FAST+ action token 完全不编码 action 信息）
- **L35 untrained**: R² = 0.656（未崩塌，仍保留 action 可预测性）

### L1 Attention Profile

| | Trained | Untrained |
|---|---------|-----------|
| instr-dominant | 13 | 13 |
| image-dominant | 0 | 0 |
| mixed | 3 | 3 |

两者 attention 分布几乎一致（都是 13/0/3），具体 head 分配略有差异（trained head_10 instr-dom / head_14 mixed → untrained head_10 mixed / head_14 instr-dom）。

### Cross-Instruction Classification Accuracy

| Layer | Trained img | Trained last_pre | Untrained img | Untrained last_pre |
|-------|------------|-----------------|--------------|-------------------|
| L0 | 0.926 | 1.000 | 0.989 | 1.000 |
| L8 | 0.926 | 1.000 | 0.993 | 1.000 |
| L16 | 0.914 | 1.000 | 0.992 | 1.000 |
| L24 | 0.910 | 1.000 | 0.990 | 1.000 |
| L32 | 0.922 | 1.000 | 0.993 | 1.000 |
| **L35** | **0.085** | **0.085** | **0.990** | **1.000** |

- Chance = 0.1
- **Trained L35**: 崩塌到 0.085（≈chance），instruction 信息在 action token 最终层完全丢失
- **Untrained L35**: 0.990/1.000，instruction 信息全程保留

### Counterfactual (仅 Trained)

方法：representation cosine distance（NORA 用 FAST+ action tokens，非 MSE）

| Condition | L0 | L9 | L24 | L30 | L35 |
|-----------|------|-------|--------|--------|------|
| wrong | 0.005 | 0.058 | 0.123 | 0.142 | **1.0** |
| empty | (同) | (同) | (同) | (同) | **1.0** |
| shuffled | (同) | (同) | (同) | (同) | **1.0** |
| paraphrased | (同) | (同) | (同) | (同) | **1.0** |

- L35 所有条件 cosine distance = 1.0，Cohen's d = 0.0
- 含义：trained 模型在最终层 action readout position，不同 instruction（wrong/empty/shuffled/paraphrased vs correct）的表征**完全相同**

**Untrained counterfactual: 缺失，需要补跑。**

---
