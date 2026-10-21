# ssh check eval prep s456

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-eval-prep-s456_20260520T031416_result.json`
- **Structured JSON:** [`bdf6915ce052c9485c04.json`](../../sessions/bd/bdf6915ce052c9485c04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。汇总如下：

---

## 1. DeepSeek CWM s123 Eval 详情

| 项目 | 值 |
|---|---|
| **完整命令** | `/root/miniconda3/bin/python eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/best/ --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --split test --device cuda:0 --max_seq_length 4096 --max_new_tokens 512 --batch_size 4 --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_seq4096/` |
| **进度** | **1260 / 9784**（约 12.9%） |
| **测试集** | `data/swebench_full/swebench_test.jsonl`（9784 条） |
| **Checkpoint** | `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/best/`（LoRA adapter） |
| **输出文件** | `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_seq4096/results_incremental.jsonl` |
| **max_seq_length** | **4096**（命令行显式指定，脚本默认 8192） |
| **device** | `cuda:0`（注意：不是 GPU 2，是 GPU 0） |

**注意**：进程在 `cuda:0` 上运行，不是你说的 GPU 2。请确认 GPU 分配是否正确。

---

## 2. s456 训练准备检查

| 检查项 | 状态 |
|---|---|
| `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456/` 不存在 | **通过** — 目录不存在，不会覆盖 |
| 模型 `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct` | **通过** — config.json 存在 |
| `train_unified.py` 存在 | **通过** |
| `data/` 目录完整 | **通过** — 包含 cwm_train/val/test.jsonl 等全部数据文件 |

s456 训练的所有前置条件已就绪，等 s123 eval 完成释放 GPU 后可直接启动。

---
