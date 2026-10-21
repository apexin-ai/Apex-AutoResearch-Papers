# prep bench mistral kl50 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_bench_mistral_kl50_s42_20260516T050509_result.json`
- **Structured JSON:** [`097ec058a79e626d8a8d.json`](../../sessions/09/097ec058a79e626d8a8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 汇总

### 路径信息
| 项目 | 路径 |
|------|------|
| 脚本 | `/root/distill_sparse_swiglu/src/benchmark_eval.py` |
| Mistral 模型 | `/root/autodl-tmp/models/mistral-7b/` (已确认存在) |
| Predictor checkpoint | `checkpoints/mistral_kl_s42/predictor_kl_normalized.pt` |
| 输出目录 | `results/benchmark/bench_mistral_kl50_s42/` (已存在，为空) |

### Few-shot 设置
脚本内置 `LM_EVAL_DEFAULTS` 字典，**无需命令行传参**：
- arc_challenge: 25-shot
- winogrande: 5-shot
- mmlu: 5-shot
- gsm8k: 8-shot

### Allocation
`--allocation` 默认值即为 `global_topk`，不需要显式指定。

### 提交命令

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export PYTHONUNBUFFERED=1 && python -u src/benchmark_eval.py --exp_id bench_mistral_kl50_s42 --model_name_or_path /root/autodl-tmp/models/mistral-7b --checkpoint checkpoints/mistral_kl_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0"
```

### 与 D029 旧命令的对比
旧命令（`run_bench_cuda1.sh` 第 5 条）参数完全一致——差异在于脚本本身已更新内置了 few-shot 默认值，而 D029 当时跑的是 0-shot 版本的脚本。现在用当前版本的 `benchmark_eval.py` 重跑即可拿到统一 few-shot 结果。

### 注意事项
- GPU: `--gpu 0`，CUDA_VISIBLE_DEVICES 由框架注入
- nohup 日志建议重定向到 `results/benchmark/bench_mistral_kl50_s42/bench.log`
- `bench_mistral_kl50_s42` 输出目录已存在但为空，不会冲突

---
