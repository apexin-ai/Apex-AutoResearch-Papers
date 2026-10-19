# research fsdp hf conversion

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_fsdp_hf_conversion_20260521T080906_result.json`
- **Structured JSON:** [`217fa44c9596ecd791b8.json`](../../sessions/21/217fa44c9596ecd791b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Seed 4 global_step_5 转换验证通过。

---

## 排查结论

### Checkpoint 结构对比

**所有 seeds 的 FSDP checkpoint 结构完全一致：**
```
global_step_N/actor/
├── model_world_size_2_rank_0.pt   # FSDP 分片权重
├── model_world_size_2_rank_1.pt
├── optim_world_size_2_rank_0.pt
├── optim_world_size_2_rank_1.pt
├── extra_state_world_size_2_rank_*.pt
├── fsdp_config.json               # {FSDP_version: 1, world_size: 2}
└── huggingface/                   # 仅 tokenizer + config，无 safetensors
    ├── config.json
    ├── tokenizer.json
    ├── tokenizer_config.json
    └── ...
```

**没有任何 seed 在训练时自动保存 `.safetensors`。**

### 根因

`FSDPCheckpointManager` 只在 `checkpoint_save_contents` 包含 `"hf_model"` 时才会调用 `save_pretrained` 生成 `.safetensors`。所有 exp029 configs 都没有设置这个字段，使用默认值 `["model", "optimizer", "extra"]`。

Seeds 1/3 的 `.safetensors` 是**手动转换**产生的：
- **Seed 1**: `exp029_hf/model.safetensors`（bjb1，May 19 创建）
- **Seed 3**: `exp029-seed3/global_step_15_hf/model.safetensors`（westd，手动转换）

Seeds 4/5/6 没有人执行过这个转换。

### 转换方案

现有脚本：`/root/cost-verify-agent-rl/scripts/convert_fsdp_to_hf.py`

```bash
python convert_fsdp_to_hf.py \
    --input-dir &lt;checkpoint>/global_step_N/actor \
    --output-dir &lt;checkpoint>/global_step_N_hf \
    --dtype bf16
```

CPU-only，~15 秒完成（2B 模型）。

### Seed 4 转换结果

已完成 → `/root/autodl-tmp/checkpoints/exp029-seed4/global_step_5_hf/`
- `model.safetensors`: 4.06 GB
- Qwen3ForCausalLM, 1720.6M params
- 加载验证通过

### 待处理

- Seeds 5/6 在 westd 上**没有找到 checkpoint 目录**（只有运行日志），需确认训练是否完成/checkpoint 存储位置
- Seed 3 bjb1 上的 `global_step_5` 和 `global_step_10` 也未转换（仅 step 15 有 `_hf`）

---
