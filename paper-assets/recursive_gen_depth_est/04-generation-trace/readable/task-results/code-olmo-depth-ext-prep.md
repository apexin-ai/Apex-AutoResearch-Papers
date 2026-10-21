# code olmo depth ext prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_olmo-depth-ext-prep_20260515T091735_result.json`
- **Structured JSON:** [`4da97b1d6dc9b558655c.json`](../../sessions/4d/4da97b1d6dc9b558655c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。

## 产出汇报

**脚本路径**: `/root/autodl-tmp/recursive_gen_depth_est/scripts/run_depth_extension_olmo.sh`

**OLMo 现有资源**:
| 资源 | 路径 | 状态 |
|------|------|------|
| 数据 d0-d3 | `data/olmo/depth_{0,1,2,3}.jsonl` | 各 5000 samples |
| Checkpoints | `checkpoints/olmo/lora_depth_{0,1,2}/` | 均有 adapter_model.safetensors |
| 模型 | `/root/autodl-tmp/models/olmo-1b-hf/` | 4.7GB, config.json 存在 |
| 已有 features | `data/olmo/features.jsonl` | d0-d3 4-class (不影响新 pipeline) |

**关键配置差异 (vs GPT-2 XL)**:
- `TARGET_MODULES="q_proj,k_proj,v_proj"` (GPT-2 XL 用 `c_attn,c_proj`)
- `CUDA_VISIBLE_DEVICES=1` (GPT-2 XL 占 cuda:0)
- 数据/checkpoint 路径均在 `olmo/` 子目录下

**Dry-run 结果**: `bash -n` 语法检查通过，所有引用的 Python 脚本存在且 `--help` 正常。

**预估运行时间**: ~3-4 小时
- Step 1 (finetune d3): ~30 min
- Step 2 (generate d4, 5000 samples): ~40 min
- Step 3 (finetune d4): ~30 min
- Step 4 (generate d5): ~40 min
- Step 5 (feature extraction d0-d5): ~30 min
- Step 6-7 (classifier + binary eval): ~5 min

Pipeline 含 skip 逻辑，中断后重启不会重复已完成步骤。等 Director 审批后可一键提交到 cuda:1。

---
