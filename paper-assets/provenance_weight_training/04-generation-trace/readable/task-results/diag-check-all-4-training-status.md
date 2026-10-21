# diag check all 4 training status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_check_all_4_training_status_20260520T141004_result.json`
- **Structured JSON:** [`08d92fdd94d280156fb2.json`](../../sessions/08/08d92fdd94d280156fb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验已更新为 DONE。以下是完整报告：

---

## 实验状态报告

| 实验 | 状态 | 模型 | 步数 | train_loss | 运行时间 | Checkpoint |
|------|------|------|------|-----------|---------|------------|
| **uniform_1_7b_seed42_v5** | 完成 | Qwen3-1.7B | 6103/6103 | 7.56 | 4h54m | `.../uniform_1_7b_seed42_v5/final` |
| **adaptive_1_7b_seed42_v5** | 完成 | Qwen3-1.7B | 6103/6103 | 9.139 | 5h09m | `.../adaptive_1_7b_seed42_v5/final` |
| **contamination_60_adaptive_seed42_tau08** | 完成 | Qwen3-0.6B | 6103/6103 | 9.635 | 3h48m | `.../contamination_60_adaptive_seed42_tau08/final` |
| **contamination_60_adaptive_seed123_tau08** | 完成 | Qwen3-0.6B | 6103/6103 | 9.63 | 3h48m | `.../contamination_60_adaptive_seed123_tau08/final` |

所有实验均：`Training complete` + `EXIT_CODE=0`，checkpoint 含 `checkpoint-5500/6000/6103/final` 四个目录。

## Registry 更新
4 个实验全部 → `DONE (success)`，已设置 checkpoint_path、metrics（train_loss, total_steps, train_runtime_s）。

## GPU 状态
4x NVIDIA RTX PRO 6000 Black 全空闲（0% 利用率，0MiB 显存），无训练进程。

## 磁盘
`/root/autodl-tmp`: 250GB 总量，161GB 已用，90GB 可用（65%）。

## Eval 脚本就绪情况

| 资源 | 状态 | 路径 |
|------|------|------|
| eval_perplexity.py | 存在 | `/root/provenance_weight_training/eval_perplexity.py` |
| eval_pipeline.py | 存在 | `/root/provenance_weight_training/evaluation/eval_pipeline.py` |
| eval_standalone.py | 存在 | `/root/provenance_weight_training/eval_standalone.py` |
| eval_holdout.jsonl | 存在 | `/root/provenance_weight_training/data/human/eval_holdout.jsonl` (237MB) |
| downstream eval 脚本 | **未找到** | 无 `*downstream*.py` |
| OOD eval 脚本 | **未找到** | 无 `*ood*.py` |

4 GPU 空闲，可立即启动 eval。`eval_perplexity.py` 和 `eval_pipeline.py` 就绪，但 downstream 和 OOD 专用脚本不存在——需要确认是否在 `eval_pipeline.py` 中集成，还是需要单独编写。

---
