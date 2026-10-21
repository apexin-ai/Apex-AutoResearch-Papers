# code prep ss eval scripts

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_ss_eval_scripts_20260523T044348_result.json`
- **Structured JSON:** [`475a7512bda079597159.json`](../../sessions/47/475a7512bda079597159.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**s456 vs s123**：归一化后完全一致 (IDENTICAL)。

**s456 vs s42 模板**的差异全部是预期的：

| 差异 | 说明 |
|------|------|
| `CONV_PATH` → `DATA_FILE=data/eval_200/eval_200.json` | 统一用 eval_200 数据 |
| `OUT_ROOT=results/d048_final_ar` | 统一输出目录 |
| `tf_ss_ours` → `tf_ss_sSEED_ours` | TF 输出加 seed 后缀防冲突 |
| AR 命令增加 `--data-file` | 显式指定数据文件 |
| bootstrap glob 限定 `*sSEED*` | 只分析当前 seed 的结果 |

脚本就绪，训练完成后可直接运行：
- `/root/turn_residual_gating/scripts/d048_eval_ss_s456.sh`
- `/root/turn_residual_gating/scripts/d048_eval_ss_s123.sh`

---
