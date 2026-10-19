# code fsdp to hf converter

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fsdp_to_hf_converter_20260514T095129_result.json`
- **Structured JSON:** [`c142484d53e787ad7c65.json`](../../sessions/c1/c142484d53e787ad7c65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

转换脚本已存在且验证通过。

---

### 结果

**脚本路径**: `/root/cost-verify-agent-rl/RAGEN/scripts/convert_fsdp_to_hf.py`

**Checkpoint 目录结构** (`exp008_grpo/global_step_5/actor/`):
```
model_world_size_2_rank_{0,1}.pt   # FSDP DTensor 分片 (2-GPU)
optim_world_size_2_rank_{0,1}.pt   # 优化器状态
extra_state_world_size_2_rank_{0,1}.pt
fsdp_config.json                   # {"FSDP_version": 1, "world_size": 2}
huggingface/                       # config.json, tokenizer, generation_config 等
```

**模型**: Qwen3ForCausalLM, 2B 参数 (311 个 tensor, 4.06 GB @ bf16)

**Dry-run 验证通过**: embed_tokens shape 与 config 一致。

### 使用方法

```bash
# 完整转换
CUDA_VISIBLE_DEVICES="" python /root/cost-verify-agent-rl/RAGEN/scripts/convert_fsdp_to_hf.py \
    --input-dir /root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/actor \
    --output-dir /root/autodl-tmp/checkpoints/exp008_grpo_hf \
    --dtype bf16

# 仅验证不写文件
python scripts/convert_fsdp_to_hf.py --input-dir &lt;actor_dir> --output-dir <任意> --dry-run
```

`CUDA_VISIBLE_DEVICES=""` 确保纯 CPU 执行，不干扰训练。

verl 框架也有内置工具 `verl/model_merger/` 可用，但自定义脚本更轻量、无额外依赖，推荐直接用它。

---
