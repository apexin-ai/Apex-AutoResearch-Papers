# ssh urgent gpu check and action

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-gpu-check-and-action_20260519T013203_result.json`
- **Structured JSON:** [`9b5e9482647505f5a841.json`](../../sessions/9b/9b5e9482647505f5a841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态（4× NVIDIA RTX PRO 6000 Blackwell 98GB）

| GPU | 状态 | 占用 | 进程 |
|-----|------|------|------|
| **0** | **空闲** | 0 MiB | - |
| **1** | 运行中 | 54,391 MiB (56%) | Gemma-2-9B d025 (PID 86378) |
| **2** | **空闲** | 0 MiB | - |
| **3** | 运行中 | 57,685 MiB (59%) | Phi-4 d005 (PID 90913) |

### OLMo-2-7B d000 — 完成

- **3125/3125 steps**, epoch=1.0, EXIT_CODE=0
- **train_loss=0.9434**, mean_token_accuracy=**0.7841**
- 末尾 loss=0.856, runtime=1h41m
- lora_alpha=32, lora_r=16, lr=5e-5, batch=2×8, 50k samples
- adapter: `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d000_s42/lora_adapter/`

### Phi-4 d000 — 完成

- **3125/3125 steps**, epoch=1.0, EXIT_CODE=0
- **train_loss=1.183**, mean_token_accuracy=**0.7287**
- 末尾 loss=1.118, runtime=2h05m
- lora_alpha=32, lora_r=16, lr=5e-5, batch=1×16, 50k samples
- adapter: `/root/autodl-tmp/exp001/checkpoints/phi-4_d000_s42/lora_adapter/`

### Phi-4 d005 — 进行中 (cuda:3)

- **1035/3177 steps (32%)**, epoch=0.324
- loss ~1.16, mean_token_accuracy ~0.736
- 预计剩余 ~1h43m

### Gemma-2-9B d025 — 进行中 (cuda:1)

- **2612/3384 steps (77%)**, epoch=0.771
- loss ~1.27, mean_token_accuracy ~0.718
- 预计剩余 ~37m

### 14B adapter 路径

全部 5 个 checkpoint 的 adapter 在 `lora_adapter/` 子目录内（不在顶层），lora_alpha 全部 =32：
```
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_{d000,d005,d025,d050,d100}_s42/lora_adapter/adapter_model.safetensors
```

### evaluate.py 参数格式

```
--model-path MODEL_PATH          # 基座模型路径
--adapter-path ADAPTER_PATH      # LoRA adapter 路径
--benchmarks {mmlu,gsm8k,arc_challenge,humaneval}
--output-dir OUTPUT_DIR
--mc-format {aligned,legacy}     # 'aligned' 匹配 SFT 格式
--batch-size N
--max-items N                    # 0=all, 1000 for MMLU subsampling
--subsample-seed N
--instruct                       # Instruct 模型用
--paraphrase-dir DIR             # 可选，paraphrase 评估
--cache-dir DIR
```

### d025 数据就绪

- `sft_dosage_025.jsonl` 存在 (94MB)
- `phi-4_d025_s42` 输出目录不存在，可安全使用

### 可用 GPU

**cuda:0 和 cuda:2 空闲**，可立即启动 14B eval 或 Phi-4 d025 训练。

---
