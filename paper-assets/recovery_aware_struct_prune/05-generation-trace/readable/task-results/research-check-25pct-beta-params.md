# research check 25pct beta params

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_25pct_beta_params_20260523T192728_result.json`
- **Structured JSON:** [`534cd04ae4b34e1e7837.json`](../../sessions/53/534cd04ae4b34e1e7837.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。

## 25% GRPO Beta 审计

| 实验 | 训练脚本 | beta 参数 | 来源 |
|------|---------|----------|------|
| `grpo_cka_only_25` | train_grpo_v5.py | **0.01** | 脚本默认值（command 无 --beta） |
| `grpo_standard_25` (westd) | train_grpo_v5.py | **0.04** | command 显式指定 --beta 0.04 |
| `grpo_standard_25_westb` | train_grpo_v5.py | **0.01** | 脚本默认值（command 无 --beta） |
| `grpo_rasp_25` | train_grpo_v5.py | **0.01** | 脚本默认值（command 无 --beta，spec 被覆盖为恢复信息） |

### 关键发现

**用户之前的认知有误**：grpo_standard_25 不是"旧版 train_grpo.py, beta=0.0"，而是 `train_grpo_v5.py`，且显式设置了 `--beta 0.04`。

**25% 内部一致性：有问题。** 存在两个 grpo_standard_25 变体，beta 不同：
- `grpo_standard_25` (westd): beta=0.04
- `grpo_standard_25_westb`: beta=0.01（默认值）
- `grpo_cka_only_25`: beta=0.01（默认值）

### tab_cross_sparsity 25% GRPO GSM8K 数据来源

| 条件 | exp_id | 模型路径 | accuracy |
|------|--------|---------|----------|
| Standard 25% GRPO | `eval_gsm8k_grpo_standard_25` | grpo_standard_25_**westb**/checkpoint-100 | **51.86%** |
| Standard 25% GRPO (alt) | `eval_grpo_standard_25` | grpo_standard_25 (westd) | **51.1%** |
| CKA-only 25% GRPO | `eval_gsm8k_grpo_cka_only_25_v3` | grpo_cka_only_25 | **59.59%** |
| RASP 25% GRPO | `eval_grpo_rasp_25` | grpo_rasp_25 | **53.15%** |

### 一致性判定

**论文中 25% Standard vs CKA-only 比较取决于用哪个 Standard 结果：**

- 如果用 `eval_gsm8k_grpo_standard_25`（51.86%）→ 模型来自 westb，beta=0.01，与 CKA-only（beta=0.01）一致 ✅
- 如果用 `eval_grpo_standard_25`（51.1%）→ 模型来自 westd，beta=0.04，与 CKA-only（beta=0.01）**不一致** ❌

需要确认论文 tab_cross_sparsity 用的是哪个数字（51.86% 还是 51.1%），以判断比较是否公平。

---
