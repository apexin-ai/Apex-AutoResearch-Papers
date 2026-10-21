# research longbench setup

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_longbench-setup_20260516T124528_result.json`
- **Structured JSON:** [`f84cfb1e8566fcb1b359.json`](../../sessions/f8/f84cfb1e8566fcb1b359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。结论如下：

## 结论

### 1. LongBench 未集成到 benchmark_eval.py

`benchmark_eval.py` 当前的 task 路由逻辑硬编码了白名单 `LM_EVAL_DEFAULTS`（仅含 arc_challenge, winogrande, mmlu, gsm8k）。任何不在白名单中的 task 会被过滤为 "unknown" 并忽略（line 294）。LongBench 任务不在其中。

### 2. lm_eval 已安装并自带 LongBench

服务器的 lm_eval 包含完整的 `longbench` task group：
- **longbench**（全集，6 个子组）
- 子组：`longbench_single`（NarrativeQA, Qasper, MultifieldQA_en/zh）、`longbench_multi`、`longbench_summarization`（GovReport, QMSum, MultiNews）、`longbench_fewshot`、`longbench_code`、`longbench_synthetic`

LongBench 是 generation 任务（非 loglikelihood），需要模型生成文本后计算 F1/ROUGE。

### 3. 需要的最小修改

**方案：修改 `benchmark_eval.py` 的 task 过滤逻辑**，让不在 `LM_EVAL_DEFAULTS` 白名单中的 task 也能传给 lm_eval（以 num_fewshot=0 作为默认）。改动约 5 行：

```python
# 修改 line 291-296，将"白名单过滤"改为"直接传递"：
lm_eval_tasks = [t for t in tasks if t != "wikitext2"]  # 任何非 wikitext2 的都交给 lm_eval
# 删掉 unknown 警告逻辑
```

或者更保守地只加 longbench 支持：
```python
LM_EVAL_DEFAULTS = {
    "arc_challenge": {"num_fewshot": 25},
    "winogrande": {"num_fewshot": 5},
    "mmlu": {"num_fewshot": 5},
    "gsm8k": {"num_fewshot": 8},
    "longbench": {"num_fewshot": 0},  # group task，自动展开子任务
}
```

### 4. 完整命令（修改后可用）

**Dense baseline：**
```bash
CUDA_VISIBLE_DEVICES=0,1 nohup python3 /root/distill_sparse_swiglu/src/benchmark_eval.py \
    --exp_id longbench_dense \
    --dense \
    --tasks longbench \
    --batch_size 1 \
    > /root/distill_sparse_swiglu/logs/longbench_dense.log 2>&1 &
```

**KL 30% uniform：**
```bash
CUDA_VISIBLE_DEVICES=0,1 nohup python3 /root/distill_sparse_swiglu/src/benchmark_eval.py \
    --exp_id longbench_kl30_uniform \
    --checkpoint checkpoints/kl_sparsity30_s42/predictor_kl_normalized.pt \
    --sparsity_mode teal_global \
    --sparsity_target 0.3 \
    --allocation uniform \
    --tasks longbench \
    --batch_size 1 \
    > /root/distill_sparse_swiglu/logs/longbench_kl30_uniform.log 2>&1 &
```

### 5. 注意事项

- LongBench 是 generation 任务，**远比** loglikelihood 任务慢（每样本需要生成 128 tokens）
- 全集（~4,800 样本 × 16 子任务）在单卡上可能需要 10+ 小时。建议先跑英文子集 `longbench_single`（~800 样本）做 sanity check
- LongBench 平均文档长度 ~5k-15k tokens，Llama-3.1-8B 的 128k window 足够，但 GPU 内存限制 batch_size 只能用 1
- 如果只选 EMNLP 最相关的几个任务：`longbench_narrativeqa,longbench_qasper,longbench_gov_report,longbench_multi_news`（single-doc QA + summarization）

---
