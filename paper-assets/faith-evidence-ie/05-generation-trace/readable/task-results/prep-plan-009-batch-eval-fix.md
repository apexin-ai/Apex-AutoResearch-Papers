# prep plan 009 batch eval fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_plan_009_batch_eval_fix_20260515T203400_result.json`
- **Structured JSON:** [`8b8467f340cc54410829.json`](../../sessions/8b/8b8467f340cc54410829.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。汇报：

---

## 调查结果

**batch_eval.py 支持 `--batch_size` 参数**（`eval/batch_eval.py:77`，默认值 16）。它内部逐个 checkpoint 调用 `freige.eval.inference`，直接传递 batch_size。

OOM 原因确认：`--no-quantize` + `batch_size=16`，Qwen3-4B 全精度在 RTX 5090 32GB 上 OOM。

## 修复方案：方案 A — 降低 batch_size

直接用 `batch_eval.py` 的 `--batch_size 4` 参数重跑即可，无需写新脚本。加 `--resume` 跳过已完成的 checkpoint。

## Checkpoints

| 实验 | Checkpoints |
|------|------------|
| extract_r3 | 680, 700, 720, 740, 756 |
| flatnli_r3 | 20, 40, 60, 80, 100 |

已有评测结果：`grpo_flatnli_r3/` 下有 checkpoint-20、checkpoint-40 的目录，但**无 metrics.json**（之前 OOM 失败留下的空目录）。extract_r3 无任何结果。

## 修复后的完整命令

**extract_reward：**
```bash
cd /root/autodl-tmp/freige && python -m eval.batch_eval \
    --exp_dir /root/autodl-tmp/grpo_extract_r3 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --output_dir /root/autodl-tmp/eval_results/grpo_extract_r3 \
    --batch_size 4 \
    --no-quantize \
    --resume
```

**flatNLI_reward：**
```bash
cd /root/autodl-tmp/freige && python -m eval.batch_eval \
    --exp_dir /root/autodl-tmp/grpo_flatnli_r3 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --output_dir /root/autodl-tmp/eval_results/grpo_flatnli_r3 \
    --batch_size 4 \
    --no-quantize \
    --resume
```

两条命令需串行执行（共享 GPU），每个 checkpoint 评测约 5-10 分钟，总计约 50-100 分钟。`--resume` 会自动跳过已有 `metrics.json` 的 checkpoint（目前没有成功的，所以会全跑）。

---
