# code cross scale llama3 base 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_scale_llama3_base_001_20260516T130518_result.json`
- **Structured JSON:** [`10367bec9f31939bba9e.json`](../../sessions/10/10367bec9f31939bba9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**脚本路径**: `/root/autodl-tmp/recursive_gen_depth_est/scripts/run_llama3_base_pipeline.sh`

**脚本状态**:
- `bash -n` 语法检查通过
- `chmod +x` 已设置
- 与 Instruct pipeline 结构完全一致，仅修改：模型路径、输出目录、checkpoint 目录

**模型状态**: 正在后台下载（PID 557455）
- tokenizer + config 文件已就位
- 4 个 safetensors 分片下载中（总计 ~15GB），速度 ~400kB/s，预计 2.5-3 小时
- 路径: `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3.1-8B` (symlink → `Meta-Llama-3___1-8B`)

**Dry-run**: 模型权重下载完成后才能执行 4-bit 加载验证。

**推荐的提交命令**（模型下载完成后）:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/recursive_gen_depth_est

# 验证模型可加载
python -c "
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch
bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4', bnb_4bit_compute_dtype=torch.bfloat16)
model = AutoModelForCausalLM.from_pretrained('/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3.1-8B', quantization_config=bnb, device_map='auto')
print(f'OK: {model.config.architectures}, hidden={model.config.hidden_size}')
"

# 运行实验
nohup bash scripts/run_llama3_base_pipeline.sh > logs/llama3_base_pipeline_run.log 2>&1 &
```

**监控下载进度**: `tail -5 /tmp/llama3_base_download.log`

---
