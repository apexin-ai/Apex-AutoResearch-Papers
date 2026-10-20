# ops modify train script

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_modify-train-script_20260523T080233_result.json`
- **Structured JSON:** [`cde6341abc4e705e96c4.json`](../../sessions/cd/cde6341abc4e705e96c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 修改的文件和函数

**train.py**
- `find_model_path()` → 重命名为 `find_qwen_path()`（逻辑不变）
- 新增 `MODEL_PATHS` dict 和 `get_model_path(model_name)` 分发函数
- `main()`: 添加 `--model` 参数；`output_dir` 和 `run_name` 根据模型名分路径（qwen 保持原路径，llama/mistral 加模型前缀子目录）

**eval_lz.py**
- 同上：`find_model_path()` → `find_qwen_path()`，新增 `MODEL_PATHS` + `get_model_path()`
- `main()`: 添加 `--model` 参数；`adapter_path` 和 `out_path` 根据模型名分路径；results dict 增加 `"model"` 字段；`os.makedirs` 确保结果子目录存在

### dry-run 结果
| 模型 | 状态 | trainable params | 输出路径 |
|------|------|-----------------|---------|
| Llama | 通过 | 13.6M / 8.0B (0.17%) | `checkpoints/llama/contam_15` |
| Mistral | 通过 | 13.6M / 7.3B (0.19%) | `checkpoints/mistral/contam_15` |

### 兼容性
- **pad_token**: 两个文件原本已有 `if tokenizer.pad_token is None: tokenizer.pad_token = tokenizer.eos_token`，无需额外处理
- **LoRA target_modules**: `q_proj/k_proj/v_proj/o_proj` 三个模型通用，无需修改
- **Qwen 行为**: `--model qwen`（默认值）路径和逻辑完全不变

### 训练命令格式
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/ctrl_contam_pilot && CUDA_VISIBLE_DEVICES={GPU} WANDB_MODE=disabled python train.py --condition {CONDITION} --model {MODEL} --gpu {GPU}"
```

---
