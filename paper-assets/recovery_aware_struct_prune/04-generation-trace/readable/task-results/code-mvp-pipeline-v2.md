# code mvp pipeline v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-pipeline-v2_20260514T031607_result.json`
- **Structured JSON:** [`5826e1b719185f126141.json`](../../sessions/58/5826e1b719185f126141.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报如下：

---

### 1. correlation_analysis.py 功能

Structure-level 相关性分析脚本，计算 CKA overlap F(h) 与剪枝决策的 Spearman ρ 相关性：
- Model-level recoverability 指标（R = recovered_acc / original_acc, Δ = recovered - pruned）
- Attention head 层面：F(h) vs 是否被 RASP/Standard 保留的 Spearman ρ
- Bootstrap 95% CI（10000 次）+ Permutation test（10000 次）
- Scatter plot 输出 + JSON 结果
- MVP 判定：ρ ≥ 0.4 = PASS, [0.3, 0.4) = WARNING, < 0.3 = FAIL

### 2. run_mvp.sh 步骤（7 步）

| 步骤 | 内容 | GPU |
|------|------|-----|
| Step 0 | Baseline eval（未剪枝） | cuda:0 |
| Step 1+2 | CKA overlap + Importance scoring 并行 | cuda:0 + cuda:1 |
| Step 3 | Standard + RASP 剪枝并行 | cuda:0 + cuda:1 |
| Step 3.5 | Post-prune eval（剪枝后、恢复前） | cuda:0 + cuda:1 |
| Step 4 | GRPO RLVR Recovery 并行（~12-15h） | cuda:0 + cuda:1 |
| Step 5 | Post-recovery eval | cuda:0 + cuda:1 |
| Step 6 | Correlation analysis | CPU |

已添加 `WANDB_PROJECT=recovery_aware_struct_prune` 环境变量。

### 3. 前次修复确认

| 修复项 | 状态 | 依据 |
|--------|------|------|
| prune.py: config.num_attention_heads 更新 | ✅ | L346-354，同时更新 num_key_value_heads |
| prune.py: forward pass 验证 | ✅ | L387 有 RuntimeError 检查 |
| train_grpo.py: max_completion_length=2048 | ✅ | L147 default=2048 |
| train_grpo.py: report_to="wandb" | ✅ | L199 |
| train_grpo.py: wandb project 名 | ⏳ | 脚本内未设 wandb.init(project=...)，已在 run_mvp.sh 中通过 `WANDB_PROJECT` 环境变量解决 |
| importance_score.py: down_proj Taylor | ✅ | L152-154 |

### 4. eval_gsm8k.py 输出格式兼容性

✅ 兼容。输出 JSON 包含 `accuracy` 字段（float），run_mvp.sh 的 `json.load(...)['accuracy']` 提取方式完全匹配。

### 5. 验证结果

- `correlation_analysis.py --help`：✅ 正常输出所有参数
- `bash -n run_mvp.sh`：✅ SYNTAX OK

---
