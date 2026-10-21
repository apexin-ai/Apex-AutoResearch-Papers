# code batch eval script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batch-eval-script_20260514T155514_result.json`
- **Structured JSON:** [`b2cb7cccb1f471568b0b.json`](../../sessions/b2/b2cb7cccb1f471568b0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已部署到 `/root/autodl-tmp/freige/eval/`，均可正常运行：

**batch_eval.py** — 批量评估 checkpoint
```bash
cd /root/autodl-tmp && python -m freige.eval.batch_eval \
    --exp_dir /root/autodl-tmp/grpo_extract_r3 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --output_dir /root/autodl-tmp/eval_results/grpo_extract_r3 \
    --resume
```
- 自动发现 checkpoint-N 目录，按 step 顺序串行 eval
- `--resume` 跳过已评测的 checkpoint
- `--checkpoints 100,200` 指定只评测特定 step
- 完成后生成 `summary.json`，自动输出 best-by-F1

**find_best_checkpoint.py** — 从训练日志找 best reward
```bash
cd /root/autodl-tmp && python -m freige.eval.find_best_checkpoint \
    --exp_dir /root/autodl-tmp/grpo_flatnli_r3
```
- 自动找实验目录中最新的 `trainer_state.json`
- `--sort_by f1_reward_fn` 可按不同指标排序
- `--save_csv` 导出全部记录

---
