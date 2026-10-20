# ssh final check and extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_final_check_and_extract_20260521T210621_result.json`
- **Structured JSON:** [`9974057f68e1dc953df6.json`](../../sessions/99/9974057f68e1dc953df6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整报告

### 1. 进程状态
- **已退出**: 是，两个实验均 EXIT_CODE=0 干净退出
- **GPU 已释放**: 是，两块 H20 均 0 MiB

### 2. Cross-instruction classification (untrained vs trained)

**tracvla_long (10 tasks, chance=0.1):**

| | Untrained | Trained |
|---|---|---|
| image_mean (all layers) | **1.000** | **1.000** |
| last_preaction (all layers) | **1.000** | **1.000** (L0=0.983) |

**tracvla_goal (10 tasks, chance=0.1):**

| | Untrained | Trained |
|---|---|---|
| image_mean L0-L5 | 0.998-0.999 | 0.996-0.998 |
| image_mean L6+ | 1.000 | 0.999-1.000 |
| last_preaction L0 | **0.970** | **0.915** |
| last_preaction L1+ | 1.000 | 1.000 |

结论：cross-instruction 分类在 trained 和 untrained 模型上都接近 ceiling（≈1.0）。预训练 LLM backbone 已经完美分离不同指令的表征，action tuning 对此几乎无影响。goal-conditioned 的 L0 last_preaction 反而在 trained 后轻微下降（0.970→0.915），但都远高于 chance。

### 3. Counterfactual sensitivity (仅 trained)

Untrained 无 counterfactual 数据（Phase 5 被跳过：untrained 模型无法生成有意义动作）。

**tracvla_long trained:**

| Condition | Cohen's d | MSE mean |
|---|---|---|
| empty | 1.4726 | 0.1609 |
| wrong | 1.4176 | 0.1570 |
| shuffled | 1.3909 | 0.1466 |
| paraphrased | 1.1614 | 0.1250 |

**tracvla_goal trained:**

| Condition | Cohen's d | MSE mean |
|---|---|---|
| empty | 1.5241 | 0.1398 |
| wrong | 1.4046 | 0.1370 |
| shuffled | 1.3358 | 0.1349 |
| paraphrased | 1.2128 | 0.1245 |

两个模型一致：empty > wrong > shuffled > paraphrased，所有条件 Cohen's d > 1.0（大效应量）。token_divergence_rate = 1.0（指令改变后 100% 的 action token 都变了）。

---
