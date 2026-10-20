# code sft training config

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sft-training-config_20260514T070528_result.json`
- **Structured JSON:** [`e365542da95f0d6911f5.json`](../../sessions/e3/e365542da95f0d6911f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 1. Qwen3-8B 加载验证
- Tokenizer: vocab_size=151643
- Model: 4096d, 36L, bf16 加载 15.3GB（device_map=auto 分布到 4 卡）

### 2. ms-swift 4.2.0 CLI 参数格式
关键参数名映射（4.x vs 旧版）：
| 参数 | 4.x 实际名 |
|------|-----------|
| 模型路径 | `--model` |
| 数据集 | `--dataset`（接受 JSONL 路径） |
| 模板 | `--template`（自动检测，无需指定） |
| 调优方式 | `--tuner_type`（默认 lora） |
| LoRA rank | `--lora_rank` |

启动命令：`swift sft --config configs/sft_taxei.yaml`
或直接 CLI：`CUDA_VISIBLE_DEVICES=0 swift sft --model ... --dataset ... --lora_rank 16 ...`

### 3. 配置文件
- `configs/sft_taxei.yaml` — TaxEI-SFT（注入+恢复轨迹）
- `configs/sft_vanilla.yaml` — Vanilla SFT baseline（仅正常轨迹）
- 唯一区别：dataset_path 和 output_dir

### 4. Dry-run 结果
- 单卡启动成功，LoRA 注入到所有 linear 层（q/k/v/o/gate/up/down_proj）
- 可训参数：43.6M / 8234M = 0.53%
- bs=1 显存 16.2GB，bs=2 显存 16.5GB（测试数据短序列）
- 速度：~0.8 s/step（bs=2, 短序列）

### 5. 训练资源估算
- **单卡足够**：RTX 5090 32GB，bs=2 + LoRA 约 20-24GB（真实 4096 长序列）
- **无需 DeepSpeed/多卡 DDP**
- ~1300 条 × 3 epochs = 3900 samples，effective batch=16 → ~244 steps
- 真实长序列约 2-4s/step → **预计 8-16 分钟/模型**
- 两个模型共计 **~30 分钟内完成**

---
