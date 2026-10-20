# ops prepare eval pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-eval-pipeline_20260518T102337_result.json`
- **Structured JSON:** [`d52066b1159c7babb7dc.json`](../../sessions/d5/d52066b1159c7babb7dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

## Eval 管道状态

### 已就绪
- **`/root/contamcal-irt-calibration/exp001/evaluate.py`** — 自定义 eval 脚本，已包含 GSM8K (8-shot CoT)、MMLU、ARC-Challenge、HumanEval 全部四个 benchmark 的评估逻辑，不依赖 lm-eval-harness
- **依赖库**：transformers、peft、datasets 均已安装
- **参考 shell 脚本**：`run_eval_3B_d100_auto.sh` 可作为 7B 的模板

### 未就绪
- **lm-eval-harness 未安装** — 但不需要，项目用自己的 `evaluate.py`
- **7B checkpoint 未完成**：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/` 目录存在但为空（训练进行中）

### 7B pilot 完成后的 GSM8K eval 命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache

cd /root/contamcal-irt-calibration/exp001

CUDA_VISIBLE_DEVICES=&lt;GPU_ID> python evaluate.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B \
    --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter \
    --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-7B_d000_s42 \
    --benchmarks gsm8k \
    --batch-size 4
```

如需全部 benchmark 评估，把 `--benchmarks gsm8k` 改为 `--benchmarks mmlu gsm8k arc_challenge humaneval`。按 C004 约束，提交时必须显式设置 `CUDA_VISIBLE_DEVICES`。

---
