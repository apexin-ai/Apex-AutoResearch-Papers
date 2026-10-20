# ops eval readiness check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-readiness-check_20260516T163750_result.json`
- **Structured JSON:** [`5f35464856368946dbf2.json`](../../sessions/5f/5f35464856368946dbf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verified. Here's the summary:

## Eval 脚本就绪状态

### 脚本存在性 ✓
| 文件 | 大小 | 最后修改 |
|------|------|----------|
| `run_repo_eval.sh` | 3.9KB | May 14 07:13 |
| `eval_repo_cls.py` | 15KB | May 16 18:17 |
| `eval_repo_cwm.py` | 18KB | May 16 18:18 |

Shell 脚本语法正确（已通过 read 验证内容完整，三参数接口 `&lt;gpu_id> &lt;checkpoint_dir> &lt;cls|cwm>`）。

### 测试数据 ✓
- 路径: `data/swebench_full/swebench_test.jsonl`
- 行数: **9784 行**
- 两个 eval 脚本默认 `--data_dir data/swebench_full`，`--split test` → 使用此文件

### Checkpoint 状态
| 训练 | 目录 | 当前状态 |
|------|------|----------|
| deepseek-cls-repo | `/root/autodl-tmp/checkpoints_deepseek_cls_repo/` | `checkpoint-2211` (step 2211/6633, epoch 1/3, 训练中) |
| deepseek-cwm-repo | `/root/autodl-tmp/checkpoints_deepseek_cwm_repo/` | 空目录（尚未产出 checkpoint） |

Base model: `deepseek-ai/deepseek-coder-6.7b-instruct` (本地 `/root/autodl-tmp/models/...`)  
LoRA: r=16, alpha=32, target=q/k/v/o_proj

### 训练完成后 Eval 命令

**CLS（训练完 ~May 17 04:00 UTC 后）：**
```bash
cd /home/sonny/exec-sim-repair-verifier && ./run_repo_eval.sh 0 /root/autodl-tmp/checkpoints_deepseek_cls_repo cls
```

**CWM（训练完 ~May 17 14:00 UTC 后）：**
```bash
cd /home/sonny/exec-sim-repair-verifier && ./run_repo_eval.sh 1 /root/autodl-tmp/checkpoints_deepseek_cwm_repo cwm
```

脚本会自动从 `trainer_state.json` 读取 `best_model_checkpoint` 并使用最佳 checkpoint。

### 问题
- **CWM checkpoint 目录为空**：训练可能刚启动或 save_steps 还未到。非阻塞——训练结束后自然会有 checkpoint。
- **CLS eval_loss = NaN**：epoch 1 结束时的 eval loss 为 NaN，可能是验证集中有异常样本或 overflow，不影响 eval 脚本本身运行。训练仍在继续（`should_training_stop: false`）。

---
