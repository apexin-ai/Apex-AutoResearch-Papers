# prep 14b scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_14b_scripts_20260518T124600_result.json`
- **Structured JSON:** [`a3384d1b78d84f76c418.json`](../../sessions/a3/a3384d1b78d84f76c418.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部语法验证通过。总结：

## 产出

### 14B 模型下载状态
**完整** — `/root/autodl-tmp/models/Qwen/Qwen3-14B/`，28GB，8 个 shard 文件齐全。

### 创建的文件

| 文件 | 说明 |
|------|------|
| `configs/accelerate_2gpu_zero3.yaml` | 2-GPU DeepSpeed ZeRO-3 accelerate 配置 |
| `scripts/sft_14b.sh` | 14B SFT 训练脚本（cuda:2,3） |
| `scripts/rsft_14b.sh` | 14B RSFT 训练脚本模板（cuda:2,3） |
| `scripts/merge_sft_adapter_14b.py` | SFT adapter 合并脚本（RSFT 前置步骤） |

### 代码补丁（向后兼容）
- `training/sft_trainer.py` — 添加 `HfDeepSpeedConfig` 提前初始化（L136-139），`device_map` 改为仅在非 DeepSpeed 模式设置（L183）
- `training/rsft_trainer.py` — 同上（L296-299, L331）

### 关键参数对比（4B → 14B）

| 参数 | 4B (单卡) | 14B (2卡 ZeRO-3) |
|------|-----------|-------------------|
| quantize | QLoRA 4-bit | bf16 LoRA (`--no-quantize`) |
| GPU | CUDA_VISIBLE_DEVICES=0 | CUDA_VISIBLE_DEVICES=2,3 |
| per_device_batch | 1 | 1 |
| grad_accum | 64 | 32 |
| effective batch | 64 | 2×1×32=64 |
| DeepSpeed | 无 | ZeRO-3 (param+optimizer+grad 分片) |

### Dry-run 状态
所有 GPU 都在使用中，无法执行 dry-run。等 Wave 1 释放 cuda:2+3 后可直接运行 `bash scripts/sft_14b.sh`。

### RSFT 14B 依赖链
SFT 14B 训练完成 → `python scripts/merge_sft_adapter_14b.py` 合并 adapter → 14B 生成 + CED 打分 → RSFT 数据就绪 → `bash scripts/rsft_14b.sh`

---
