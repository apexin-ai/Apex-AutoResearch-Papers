# ops llama3 base urgent fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3-base-urgent-fix_20260521T083541_result.json`
- **Structured JSON:** [`2b9821365b8f4f9a0988.json`](../../sessions/2b/2b9821365b8f4f9a0988.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

train_sft.py 没有 `--max-steps` 参数，dry-run 需等模型下载完成后启动，观察几个 step 后手动 kill 即可验证。

---

## 状态汇报

### 1. Instruct 进程终止 ✅
- 原始 3 个 PID (498200/498335/498508) 已不存在
- 新发现 2 个 Instruct 下载进程 (499460/499465) 已 kill

### 2. 磁盘清理 ✅
- 删除 Instruct 下载文件（~1.6G）+ ModelScope 临时文件
- 磁盘：216G/250G (87%)，剩余 35G，够放 Base 模型 (~15G)

### 3. Base 模型下载 🔄
- PID 499965，HuggingFace `meta-llama/Llama-3.1-8B`
- 4 个 safetensors 分片并行下载，速度 ~430kB/s/stream
- 预计 **~3 小时**完成
- 输出路径：`/root/autodl-tmp/models/Meta-Llama-3.1-8B`

### 4. GPU 可用性
| GPU | 状态 | 当前任务 |
|-----|------|---------|
| 0 | 占用 (20G) | gemma-2-9b eval gsm8k d000_s0 |
| 1 | **空闲** | - |
| 2 | 占用 (32G) | Qwen2.5-14B eval gsm8k d050_s0 |
| 3 | **空闲** | - |

### 5. SFT dry-run ❌
待模型下载完成。

### 6. SFT 训练命令模板（所有 dosage × seed=0）

```bash
# d000 validation (GPU 1)
cd /root/contamcal-irt-calibration/exp001 && \
CUDA_VISIBLE_DEVICES=1 python3 train_sft.py \
    --model-name /root/autodl-tmp/models/Meta-Llama-3.1-8B \
    --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl \
    --output-dir /root/autodl-tmp/exp001/checkpoints/Llama-3.1-8B_d000_s0 \
    --lora-r 16 --lora-alpha 32 \
    --lr 5e-5 \
    --batch-size 2 --grad-accum 8 \
    --epochs 1 --max-seq-length 2048 \
    --gradient-checkpointing \
    --seed 0

# 其他 dosage 替换 d000→d005/d025/d050/d100，数据文件对应替换
# dosage_005/025/050/100
```

配置来源：`exp001/configs/llama31_8b.yaml`（lr=5e-5, r=16, alpha=32, bs=2, grad_accum=8, gradient_checkpointing）。与其他 5 个家族一致。

**下一步**：等模型下载完成后，GPU 1 跑 d000_s0 dry-run 验证，通过后提交全量训练。

---
