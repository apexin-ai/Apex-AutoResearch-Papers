# ops prep 1p5b humaneval remaining

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_1p5b_humaneval_remaining_20260519T131654_result.json`
- **Structured JSON:** [`0291cfdb91c91ac49d02.json`](../../sessions/02/0291cfdb91c91ac49d02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是调查报告。

---

## 1.5B HumanEval @2048 剩余 3 实验启动条件报告

### Checkpoint 可用性（全部就绪 ✅）

| 模型 | westd-29022 路径 | 大小 | 完整性 |
|------|-----------------|------|--------|
| GRPO RASP 1.5B | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/` | model.safetensors 2.9GB | config.json ✅ tokenizer ✅ |
| SFT RASP 1.5B | `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b/` | model.safetensors 2.9GB | config.json ✅ tokenizer ✅ |
| GRPO Standard 1.5B | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b/` | model.safetensors 2.9GB | config.json ✅ tokenizer ✅ |

westb-23072 上也有这三个 checkpoint（grpo_rasp 在 `checkpoint-100/` 子目录下），**无需 SCP 传输**。

### 当前 GPU 占用

**westd-29022:**
| GPU | 进程 | VRAM | 备注 |
|-----|------|------|------|
| cuda:0 | eval_gsm8k grpo_rasp_20_fair (0.5B) | 29.6 GB | 非 1.5B eval |
| cuda:1 | **eval_humaneval_sft_cka_only_20_1p5b_2048** | 4.3 GB | 完成后可用 |
| cuda:2 | **eval_humaneval_grpo_cka_only_20_1p5b_2048** | 4.3 GB | 完成后可用 |
| cuda:3 | eval_humaneval_sft_standard_20_2048_v3 (0.5B) | 17.8 GB | 非 1.5B eval |

**westb-23072:**
| GPU | 进程 | VRAM | 备注 |
|-----|------|------|------|
| cuda:0 | **eval_humaneval_sft_standard_20_1p5b_2048** | 4.2 GB | 完成后可用 |
| cuda:1 | train_grpo_v5 (grpo_cka_only_20_seed123) | 67.9 GB | 训练中，不可用 |

### 参考命令格式（从运行中进程提取）

```bash
source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && \
CUDA_VISIBLE_DEVICES={GPU} /root/miniconda3/bin/python src/eval_humaneval.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/{model_dir} \
  --max_new_tokens 2048 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_{name}_2048.json
```

### 建议 GPU 分配（3 GPU 对 3 实验）

| 实验 | 服务器 | GPU | 命令中的 model_path | output_path 文件名 |
|------|--------|-----|--------------------|--------------------|
| eval_humaneval_grpo_rasp_20_1p5b_2048 | westd-29022 | cuda:1 | `grpo_rasp_20_1p5b` | `humaneval_grpo_rasp_20_1p5b_2048.json` |
| eval_humaneval_sft_rasp_20_1p5b_2048 | westd-29022 | cuda:2 | `sft_rasp_20_1p5b` | `humaneval_sft_rasp_20_1p5b_2048.json` |
| eval_humaneval_grpo_standard_20_1p5b_2048 | westb-23072 | cuda:0 | `grpo_standard_20_1p5b` | `humaneval_grpo_standard_20_1p5b_2048.json` |

### 注意事项

1. **eval_humaneval.py 版本不一致**: westd 6462 bytes (May 19 19:31) vs westb 6948 bytes (May 19 20:23)。启动前应确认 westb 版本是否为最新版，如需要同步到 westd。
2. **westb grpo_rasp checkpoint 路径差异**: westb 上的路径是 `.../grpo_rasp_20_1p5b/checkpoint-100/`（有子目录），westd 上则直接在顶层。westd 的路径更干净。
3. **VRAM**: 1.5B HumanEval @2048 实测 ~4.3GB，98GB 显存绰绰有余。
4. **所有 config.json 确认**: Qwen2ForCausalLM, hidden_size=1536, num_hidden_layers=28, 有 `per_layer_intermediate_size`（结构化剪枝特征）。

---
