# D064 Qwen Greedy 启动报告

**时间**: 2026-05-19 ~07:50 UTC

## Option C 状态: 进行中

| 文件 | 进度 | 状态 |
|------|------|------|
| d064_llama_docred_greedy_unconstrained_w5.jsonl | 998/998 | ✅ 完成 |
| d064_llama_docred_greedy_constrained_w5.jsonl | 862/998 | 🔄 运行中 (PID 665503, GPU1) |

- LLaMA constrained 预计 ~30 分钟完成 (速率 ~4.5 行/分钟)
- 预计完成时间: ~08:20 UTC

## Qwen Checkpoint

- 路径: `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged`
- 位置: westd-16980 (本地，无需 scp)
- 格式: 4x safetensors 分片，完整 tokenizer 配置

## Qwen Greedy 启动

### GPU0: Unconstrained — 已启动 ✅

- PID: 676441
- 输出: `/root/autodl-tmp/schema_outputs/d064_qwen_docred_greedy_unconstrained.jsonl`
- 日志: `/root/autodl-tmp/schema_outputs/d064_qwen_greedy_unc.log`
- 进度: 5/998 (模型加载完成，推理中)
- 启动命令:
```bash
CUDA_VISIBLE_DEVICES=0 nohup python run_constrained_extraction.py \
    --mode unconstrained --dataset docred \
    --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged \
    --data_path data/docred/dev.json \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --output_path /root/autodl-tmp/schema_outputs/d064_qwen_docred_greedy_unconstrained.jsonl \
    --device cuda:0 --max_new_tokens 2048 --seed 42 \
    --decoding_strategy greedy --skip_on_error
```

### GPU1: Constrained — 待启动 ⏳

- 等待 LLaMA constrained 完成后启动
- 输出: `/root/autodl-tmp/schema_outputs/d064_qwen_docred_greedy_constrained.jsonl`
- 日志: `/root/autodl-tmp/schema_outputs/d064_qwen_greedy_con.log`
- 启动命令:
```bash
CUDA_VISIBLE_DEVICES=1 nohup python run_constrained_extraction.py \
    --mode full_s1 --dataset docred \
    --model_path /root/autodl-tmp/checkpoints/qwen_lora_docred_merged \
    --data_path data/docred/dev.json \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --output_path /root/autodl-tmp/schema_outputs/d064_qwen_docred_greedy_constrained.jsonl \
    --device cuda:0 --max_new_tokens 2048 --seed 42 \
    --decoding_strategy greedy --skip_on_error
```

## 预计时间线

| 事件 | 预计时间 (UTC) |
|------|---------------|
| LLaMA constrained 完成 | ~08:20 |
| Qwen constrained 启动 | ~08:20 (手动) |
| Qwen unconstrained 完成 | ~11:30 (按 LLaMA 速率估算) |
| Qwen constrained 完成 | ~12:00 |

## 待办

- [ ] LLaMA constrained 完成后，在 GPU1 启动 Qwen constrained
