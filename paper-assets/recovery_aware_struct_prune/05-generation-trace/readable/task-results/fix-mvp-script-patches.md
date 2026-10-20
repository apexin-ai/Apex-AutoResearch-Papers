# fix mvp script patches

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mvp-script-patches_20260514T062934_result.json`
- **Structured JSON:** [`da9ede3adff4c3c2d5d1.json`](../../sessions/da/da9ede3adff4c3c2d5d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

**修改汇报：**

| 文件 | 变更 |
|------|------|
| `src/run_mvp.sh` | 全文更新 (154行) |
| `src/run_mvp_resume_from_3_5.sh` | 新建 (104行) |

**三个修复状态：**

| 修复 | 状态 | 说明 |
|------|------|------|
| Step 0 (Baseline eval) | **新增** L15-20 | `eval_gsm8k.py` → `results/baseline_eval.json`，使用 cuda:0 |
| Step 3.5 (Post-prune eval) | **已存在**，无需修改 | 输出路径 `eval_pruned_standard_35.json` / `eval_pruned_rasp_35.json` |
| Step 6 JSON 解析 | **已正确**，无需修改 | 已使用 `d["combined"]["spearman_rho"]` |
| 修复 3: Pruning Distribution 日志 | **新增** L61-66 | Step 3 后打印 `n_attn_groups_pruned` / `n_mlp_groups_pruned` / `sparsity_actual`，直接从 metadata 读取 |
| 最终汇总 | **已更新** | 新增 Baseline 行到 echo 和 Python 汇总 |

**run_mvp_resume_from_3_5.sh：** 就绪。包含前置检查、Step 3.5→6 全流程、错误传播 (`set -e` + 逐步 check)、GPU 分配 (cuda:0=standard, cuda:1=rasp)。`model_utils.py` 尚不存在，已在 Step 4 处加 TODO 注释。

**READY**

---
