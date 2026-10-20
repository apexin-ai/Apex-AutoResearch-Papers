# code verify and eval scripts s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-and-eval-scripts-s123_20260519T135252_result.json`
- **Structured JSON:** [`91f668459d44ffe6d8d6.json`](../../sessions/91/91f668459d44ffe6d8d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. Qwen-7B s123 参数验证

| dosage | lora_r | lora_alpha | lr | seed | adapter_model.safetensors |
|--------|--------|------------|------|------|---------------------------|
| d000 | 16 ✓ | 32 ✓ | 5e-05 ✓ | 123 ✓ | ✓ |
| d005 | 16 ✓ | 32 ✓ | 5e-05 ✓ | 123 ✓ | ✓ |
| d025 | 16 ✓ | 32 ✓ | 5e-05 ✓ | 123 ✓ | ✓ |
| d050 | 16 ✓ | 32 ✓ | 5e-05 ✓ | 123 ✓ | ✓ |
| d100 | 16 ✓ | 32 ✓ | 5e-05 ✓ | 123 ✓ | ✓ |

Checkpoint 路径: `checkpoints/Qwen2.5-7B_d{d}_s123/`，adapter 在 `lora_adapter/` 子目录。

### 2. evaluate.py 实际 CLI 接口

```
--model-path       基础模型路径（必需）
--adapter-path     LoRA adapter 路径（指向 lora_adapter/ 目录）
--benchmarks       benchmark 列表（mmlu / arc_challenge / gsm8k / humaneval）
--mc-format        MCQ 格式（默认 aligned）
--output-dir       输出目录（必需）
--batch-size       默认 8
--cache-dir        默认 /root/autodl-tmp/.hf_cache
--max-samples      最大样本数
--max-items        最大 item 数
--subsample-seed   子采样种子（默认 42）
--instruct         instruct 模式标志
--paraphrase-dir   paraphrase 数据目录
```

### 3. 四个 eval 脚本

| 脚本 | 路径 | 状态 |
|------|------|------|
| eval_qwen7b_olmo2_s123.sh | `/root/autodl-tmp/exp001/eval_qwen7b_olmo2_s123.sh` | ✓ 已创建 +x |
| eval_phi4_s123.sh | `/root/autodl-tmp/exp001/eval_phi4_s123.sh` | ✓ 已创建 +x |
| eval_qwen14b_s123.sh | `/root/autodl-tmp/exp001/eval_qwen14b_s123.sh` | ✓ 已创建 +x |
| eval_gemma2_s123.sh | `/root/autodl-tmp/exp001/eval_gemma2_s123.sh` | ✓ 已创建 +x |

### 4. 对模板的修正

相对于任务中的模板，做了以下修正：

| 项目 | 模板 | 实际 |
|------|------|------|
| 模型参数 | `--model_path` 单参数 | `--model-path` + `--adapter-path` 分离 |
| benchmark 名 | `mmlu arc` | `mmlu arc_challenge` |
| 新增参数 | 无 | `--mc-format aligned`（与 s42 eval 一致） |
| 环境变量 | 无 HF_HOME | 加 `HF_HOME=/root/autodl-tmp/.hf_cache` |
| CUDA_VISIBLE_DEVICES | 不设（遵从用户指令） | 不设 ✓ |
| 跳过逻辑 | 无 | 加 `adapter_config.json` 存在性检查（参考 phase2 eval 脚本） |

**注意**: 目前除 Qwen-7B（5/5）外，其余模型 s123 仅 d000 训练完成。脚本内置了跳过逻辑，未完成的 dosage 会自动 SKIP。

---
