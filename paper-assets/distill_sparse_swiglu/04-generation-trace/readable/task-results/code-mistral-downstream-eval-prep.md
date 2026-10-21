# code mistral downstream eval prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_downstream_eval_prep_20260515T231945_result.json`
- **Structured JSON:** [`98c7c003bcd1f20691ac.json`](../../sessions/98/98c7c003bcd1f20691ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All info gathered. Here's the analysis and plan.

## 报告

### 1. 现状确认

| 项目 | 状态 |
|------|------|
| Mistral checkpoint | ✅ `/root/distill_sparse_swiglu/checkpoints/mistral_kl_s42/predictor_kl_normalized.pt` (152MB) |
| Mistral 模型 | ✅ `/root/autodl-tmp/models/mistral-7b` (hidden=4096, inter=14336, 32 layers) |
| 维度兼容性 | ✅ 与 Llama-3.1-8B 完全一致，SparsityPredictor 可直接加载 |
| MLP 结构 | ✅ MistralForCausalLM 与 LlamaForCausalLM 共享 `model.model.layers[].mlp.{gate_proj,up_proj,down_proj,act_fn}` |
| ARC-Challenge 缓存 | ✅ 已缓存 |
| MMLU 缓存 | ✅ 已缓存（57 个子集全部就绪） |

### 2. 需要代码改动

eval_benchmark.py 需要 3 处修改：

**改动 1** — CONDITIONS 添加 `mistral_kl_s42` 条目（~line 90）：
```python
    ("mistral_kl_s42", {
        "mode": "predictor",
        "checkpoint": _CKPT("mistral_kl_s42/predictor_kl_normalized.pt"),
    }),
```

**改动 2** — parse_args 添加 `--model_path` 参数（~line 429）：
```python
    p.add_argument("--model_path", type=str, default=MODEL_PATH,
                   help="Path to base model")
```

**改动 3** — main() 中 `MODEL_PATH` 替换为 `args.model_path`（model loading 段，约两处）：
```python
    print(f"Loading model from {args.model_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    ...
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
```

### 3. 完整命令

```bash
CUDA_VISIBLE_DEVICES=1 nohup python -u src/eval_benchmark.py \
  --condition dense,mistral_kl_s42 \
  --tasks arc_challenge,mmlu \
  --skip_ppl \
  --gpu 0 \
  --model_path /root/autodl-tmp/models/mistral-7b \
  --batch_size 4 \
  --output_dir results/plan_009_mistral \
  > logs/eval_mistral_downstream.log 2>&1 &
```

- `CUDA_VISIBLE_DEVICES=1` 遵守 C001 约束，`--gpu 0` 因 CVID 重映射
- `dense` condition 一起跑，作为 Mistral baseline 对照
- `--skip_ppl` 只跑 downstream，与任务要求一致

### 4. 预计运行时间

- Mistral-7B 加载：~30s
- ARC-Challenge (25-shot)：~15-20min × 2 conditions
- MMLU (5-shot)：~40-60min × 2 conditions
- **总计约 2-3 小时**

是否现在应用代码改动并部署到服务器？

---
