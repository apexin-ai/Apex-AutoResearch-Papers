# ssh qwen eval scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen-eval-scripts_20260520T102345_result.json`
- **Structured JSON:** [`9bbd56568b4dc6200474.json`](../../sessions/9b/9bbd56568b4dc6200474.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建，`bash -n` 语法检查通过。

| 脚本 | GPU | Checkpoint 目录 | 输出目录 |
|------|-----|----------------|---------|
| `eval_qwen_cwm_s123.sh` | GPU 1 | `checkpoints_repo_cwm_8b_s123` | `qwen3_8b_cwm_repo_s123_eval` |
| `eval_qwen_cwm_s456.sh` | GPU 2 | `checkpoints_repo_cwm_8b_s456` | `qwen3_8b_cwm_repo_s456_eval` |

参数对齐 DeepSeek 模板：`--max_seq_length 4096 --max_new_tokens 512 --batch_size 1`（Qwen 8B 比 DeepSeek 6.7B 大，batch_size 从 4 降到 1）。自动选取最大编号 checkpoint，eval 后输出 accuracy、unparseable rate、gen_text 长度验证、以及 PASS/FAIL 缺失率。

---
