# code seed42 full eval script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed42_full_eval_script_20260519T194834_result.json`
- **Structured JSON:** [`808408d1b20c4923d79e.json`](../../sessions/80/808408d1b20c4923d79e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**脚本**: `/root/autodl-tmp/provenance_weight_training/scripts/run_seed42_full_eval.sh`

**语法检查**: SYNTAX_OK

**数据文件验证**:
| 文件 | 状态 |
|------|------|
| `data/human/eval_holdout.jsonl` | 存在 (227MB) |
| `data/eval_openwebtext.jsonl` | 存在 (24MB) |
| `data/eval_wikipedia.jsonl` | 存在 (68MB) |

**依赖验证**:
| 依赖 | 状态 |
|------|------|
| `eval_ppl_ood.py` | 存在 |
| `lm_eval` | 可导入 |

**注意**: 原始任务指定 `eval_perplexity.py`，但该文件不存在。项目中实际的 PPL 评估脚本是 `eval_ppl_ood.py`，接口为 `--model_path` + `--eval_sets name:path`。脚本已适配实际接口。

---
