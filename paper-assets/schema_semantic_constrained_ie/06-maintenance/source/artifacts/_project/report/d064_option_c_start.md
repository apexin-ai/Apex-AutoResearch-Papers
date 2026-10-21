# D064 Option C: Llama Greedy 补跑 — 启动报告

**服务器**: westd-16980  
**时间**: 2026-05-20 03:47 CST

## w5 Checkpoint

- **路径**: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged`
- 与 beam-4 运行使用同一 checkpoint（Llama-3.1-8B + DocRED LoRA merged）

## GPU0: Greedy Unconstrained（已启动）

**PID**: 663859（实际 GPU 进程 PID 663864）

```bash
cd /root/schema_semantic_constrained_ie
CUDA_VISIBLE_DEVICES=0 nohup python run_constrained_extraction.py \
    --mode unconstrained \
    --dataset docred \
    --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged \
    --data_path data/docred/dev.json \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --output_path /root/autodl-tmp/schema_outputs/d064_llama_docred_greedy_unconstrained_w5.jsonl \
    --device cuda:0 \
    --max_new_tokens 2048 \
    --seed 42 \
    --decoding_strategy greedy \
    --skip_on_error \
    > /root/autodl-tmp/schema_outputs/d064_greedy_unc_w5.log 2>&1 &
```

- **状态**: 运行中，启动后 ~2min 已完成 9/998 samples
- **Log**: `/root/autodl-tmp/schema_outputs/d064_greedy_unc_w5.log`
- **输出**: `/root/autodl-tmp/schema_outputs/d064_llama_docred_greedy_unconstrained_w5.jsonl`

## GPU1: Greedy Constrained（Cascade 等待中）

**Cascade PID**: 664150

Cascade 脚本 `/root/schema_semantic_constrained_ie/scripts/d064_cascade_greedy_con.sh` 正在等待 beam-4 constrained（PID 647334, 916/998）完成。完成后自动启动：

```bash
CUDA_VISIBLE_DEVICES=1 python run_constrained_extraction.py \
    --mode full_s1 \
    --dataset docred \
    --model_path /root/autodl-tmp/checkpoints/llama_lora_docred_merged \
    --data_path data/docred/dev.json \
    --constraints_path data/docred/ontology_constraints_docred.json \
    --output_path /root/autodl-tmp/schema_outputs/d064_llama_docred_greedy_constrained_w5.jsonl \
    --device cuda:0 \
    --max_new_tokens 2048 \
    --seed 42 \
    --decoding_strategy greedy \
    --skip_on_error
```

- **Log**: `/root/autodl-tmp/schema_outputs/d064_greedy_con_w5.log`
- **输出**: `/root/autodl-tmp/schema_outputs/d064_llama_docred_greedy_constrained_w5.jsonl`

## 时间估算

| 任务 | 预计耗时 | 预计完成 |
|------|----------|----------|
| Greedy unconstrained (GPU0) | ~2-2.5h | ~06:00-06:30 CST |
| Beam-4 constrained 剩余 (GPU1) | ~20-30min | ~04:15 CST |
| Greedy constrained (GPU1, cascade) | ~2.5-3h | ~07:00-07:30 CST |

## 当前 GPU 状态

- **GPU0**: Greedy unconstrained 推理中 (18266MiB, 90%)
- **GPU1**: Beam-4 constrained 推理中 (18268MiB, 77%), 916/998

## 产出文件汇总

| 文件 | 状态 |
|------|------|
| `d064_llama_docred_beam4_unconstrained_16980.jsonl` | 已完成 (998 samples) |
| `d064_llama_docred_beam4_constrained_16980.jsonl` | 进行中 (916/998) |
| `d064_llama_docred_greedy_unconstrained_w5.jsonl` | 进行中 (9/998) |
| `d064_llama_docred_greedy_constrained_w5.jsonl` | 待启动 (cascade) |
