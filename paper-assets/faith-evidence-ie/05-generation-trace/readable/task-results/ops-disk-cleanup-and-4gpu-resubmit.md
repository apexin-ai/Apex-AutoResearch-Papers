# ops disk cleanup and 4gpu resubmit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_and_4gpu_resubmit_20260517T082648_result.json`
- **Structured JSON:** [`d704c882486649659e30.json`](../../sessions/d7/d704c882486649659e30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 3 验证完成。4 GPU 全部有进程，全部正常运行：

| GPU | 实验 | PID | 显存 | 状态 |
|-----|------|-----|------|------|
| cuda:0 | `rsft_s43_dev_eval_preds` | 431308 | 10.4 GB | Inference 进行中 |
| cuda:1 | `plan_006_qwen3_1_7b_rsft_eval_r2` | 431385 | 5.4 GB | Inference 进行中 |
| cuda:2 | `plan_006_llama_rsft_r3_eval` | 432670 | 17.9 GB | Inference 刚启动 |
| cuda:3 | `plan_006_qwen3_8b_rsft_train_r2` | 431785 | 27.5 GB | 从 step 750 resume，当前 step ~773/3393 |

磁盘可用 58GB。

修复过程中做的额外操作：
- 为 `freige/freige/` 内层包创建了 symlink 指向外层的 `training/`, `eval/`, `data/`, `analysis/`, `configs/`, `rewards/` 目录（解决模块导入问题）
- 在 `rsft_trainer.py` 中添加了 `--resume_from_checkpoint` 参数支持
- LLaMA base_model 路径修正为 `Meta-Llama-3.1-8B`（与 SFT adapter 一致）
- 8B resume 使用 checkpoint-750（checkpoint-100 不存在，750 是最早可用的）

---
