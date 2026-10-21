# code fsdp to hf converter

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fsdp_to_hf_converter_20260514T112114_result.json`
- **Structured JSON:** [`2d64cd4f97a887084285.json`](../../sessions/2d/2d64cd4f97a887084285.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Checkpoint 格式
- **verl FSDP v2 DTensor shards**（非 DeepSpeed ZeRO，非原生 PyTorch FSDP state_dict）
- 每个 rank 保存一个 `model_world_size_2_rank_{i}.pt`，内含 DTensor 对象，placement 为 `Shard(dim=0)`
- `huggingface/` 子目录存放 config.json + tokenizer 文件
- `fsdp_config.json` 记录 world_size=2

### 转换方法
脚本加载所有 rank 的 DTensor shards → 提取 `_local_tensor` → 沿 shard 维度 `torch.cat` 合并 → 转 bf16 → 通过 `model.save_pretrained()` 输出 safetensors 格式。

### 转换脚本
已部署到 `/root/cost-verify-agent-rl/scripts/convert_fsdp_to_hf.py`

用法：
```bash
python scripts/convert_fsdp_to_hf.py \
    --input-dir /root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/actor \
    --output-dir /root/autodl-tmp/models/phase_a_hf \
    --dtype bf16
```

Shell 封装 `scripts/convert_fsdp_to_hf.sh` 也可用（调用 `verl.model_merger` CLI）。

### Dry-run 结果
- 311 个参数，2,031,739,904 总参数量（1720.6M 可训练）
- embed_tokens.weight shape [151936, 2048] 与 config 一致
- `AutoModelForCausalLM.from_pretrained()` 加载成功，dtype=bf16
- 全流程耗时 ~17s（CPU-only）

---
