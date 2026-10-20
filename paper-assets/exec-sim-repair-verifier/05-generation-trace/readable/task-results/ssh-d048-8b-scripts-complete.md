# ssh d048 8b scripts complete

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d048-8b-scripts-complete_20260513T085949_result.json`
- **Structured JSON:** [`a87026060015b1288795.json`](../../sessions/a8/a87026060015b1288795.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

**8B 脚本清单**

| 脚本 | 状态 | 关键变更 |
|------|------|----------|
| `train_repo_verifier_8b.py` | 新建 | model→Qwen3-8B, batch=1, grad_accum=32, output→checkpoints_cls8b/ |
| `train_repo_cwm_8b.py` | 新建 | model→Qwen3-8B, output→checkpoints_cwm8b/, run_name含8b |

**D046 超参确认**：两个脚本均为 lr=5e-5, weight_decay=0.01, warmup_ratio=0.05, save_total_limit=5, gradient_checkpointing=True。

**Eval 脚本不需要 8B 版本**：`eval_repo_cls.py` 和 `eval_repo_cwm.py` 均通过 `--model_name` 和 `--batch_size` argparse 传参，8B 评估时传 `--model_name Qwen/Qwen3-8B --batch_size 2` 即可。

**语法验证**：两个脚本均通过 `ast.parse`。

---
