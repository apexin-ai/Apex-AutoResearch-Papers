# eval bench dense

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bench_dense_20260516T051518_result.json`
- **Structured JSON:** [`6115b72484ccee549042.json`](../../sessions/61/6115b72484ccee549042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 不空闲。** 当前有两个进程在跑：

| GPU | PID | 运行时间 | 任务 |
|-----|-----|---------|------|
| cuda:0 | 207962 | 4m44s | `bench_mistral_kl50_s42` — Mistral benchmark 评测 |
| cuda:1 | 205598 | 37m25s | `bce_isocompute_v3_s42` — Llama BCE 训练 |

cuda:0 上正在跑 Mistral 的 benchmark 评测（bench_mistral_kl50_s42），占用 32GB 显存，利用率 100%。这个任务跑的是 5 个 task（wikitext2, arc_challenge, winogrande, mmlu, gsm8k），刚运行不到 5 分钟，预计还需要较长时间才能完成。

**无法立即启动 bench_dense。** 需要等 cuda:0 上的 Mistral benchmark 跑完后才能提交。

已确认的 dense 运行参数（待 GPU 空闲后使用）：
- 模型路径：`/root/autodl-tmp/models/llama-3.1-8b`
- Dense 模式：`--dense` flag（无需 checkpoint）
- Few-shot 默认值已匹配：ARC=25, WG=5, MMLU=5, GSM8K=8
- 命令：
```
python -u src/benchmark_eval.py --exp_id bench_dense --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --dense --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
```

---
