# ops westd gpu status gsm8k collect sft prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-gpu-status-gsm8k-collect-sft-prep_20260521T094459_result.json`
- **Structured JSON:** [`07ed89bef5bbf34e662c.json`](../../sessions/07/07ed89bef5bbf34e662c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总如下：

---

## Part 1: westd GPU 状态

| GPU | Util | VRAM | 任务 | 进度 | 预计剩余 |
|-----|------|------|------|------|---------|
| 0 | 91% | 16.7/97.9 GB | OLMo-2 d100_s0 GSM8K | 470/660 (71%) | ~17 min |
| 1 | 91% | 16.7/97.9 GB | OLMo-2 d000_s0 GSM8K | 541/660 (82%) | ~11 min |
| 2 | 91% | 16.7/97.9 GB | OLMo-2 d005_s0 GSM8K | 387/660 (59%) | ~25 min |
| 3 | 88% | 31.7/97.9 GB | Phi-4 d100_s0 GSM8K | 471/660 (71%) | ~21 min |

**全部运行中，无空闲 GPU。** GPU 1 最先完成（~11 min）。

---

## Part 2: 已完成 GSM8K 结果

| Model | Dosage | Accuracy | Correct/Total |
|-------|--------|----------|---------------|
| Phi-4 | d000_s0 | **84.46%** | 1114/1319 |
| Qwen2.5-14B | d100_s0 | **82.41%** | 1087/1319 |
| Qwen2.5-14B | d050_s0 | **81.05%** | 1069/1319 |
| Gemma-2 | d000_s0 | **17.82%** | 235/1319 |

**Gemma-2 d000 只有 17.82%，大量 pred=null。** 可能是 eval 格式/prompt 不兼容 Gemma-2，需要排查。

---

## Part 3: LLaMA-3 模型下载状态

路径: `westd:/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B/`

| 分片 | 大小 | 状态 |
|------|------|------|
| model-00001-of-00004 | 4.98 GB | 完成 |
| model-00002-of-00004 | 5.00 GB | 完成 |
| model-00003-of-00004 | 3.52 GB | **SCP 进行中** (PID 507499) |
| model-00004-of-00004 | 1.17 GB | 完成 |

**3/4 完成，第 3 分片仍在传输。**

---

## Part 4: SFT 数据

`/root/autodl-tmp/sft_data/` 下 5 个 dosage 文件全部就绪。数据是模型无关的 chat 格式（system/user/assistant），所有家族共用，**无需单独为 LLaMA-3 准备。**

---

## Part 5: SFT 启动命令（待模型下载完成 + GPU 空闲）

train_sft.py 参数已确认。3 个 SFT 命令：

```bash
# d000 — 分配给最先空闲的 GPU（预计 GPU 1）
cd /root/contamcal-irt-calibration/exp001 && \
CUDA_VISIBLE_DEVICES=1 nohup python train_sft.py \
  --model-name /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d000_s0 \
  --lora-r 16 --lora-alpha 32 --lr 5e-5 \
  --batch-size 2 --grad-accum 8 --epochs 1 \
  --max-seq-length 2048 --gradient-checkpointing --seed 0 \
  > /tmp/sft_llama3_d000_s0.log 2>&1 &
echo "PID: $!"
```

```bash
# d025 — 第二个空闲 GPU（预计 GPU 0）
cd /root/contamcal-irt-calibration/exp001 && \
CUDA_VISIBLE_DEVICES=0 nohup python train_sft.py \
  --model-name /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d025_s0 \
  --lora-r 16 --lora-alpha 32 --lr 5e-5 \
  --batch-size 2 --grad-accum 8 --epochs 1 \
  --max-seq-length 2048 --gradient-checkpointing --seed 0 \
  > /tmp/sft_llama3_d025_s0.log 2>&1 &
echo "PID: $!"
```

```bash
# d100 — 第三个空闲 GPU（预计 GPU 3）
cd /root/contamcal-irt-calibration/exp001 && \
CUDA_VISIBLE_DEVICES=3 nohup python train_sft.py \
  --model-name /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Meta-Llama-3.1-8B_d100_s0 \
  --lora-r 16 --lora-alpha 32 --lr 5e-5 \
  --batch-size 2 --grad-accum 8 --epochs 1 \
  --max-seq-length 2048 --gradient-checkpointing --seed 0 \
  > /tmp/sft_llama3_d100_s0.log 2>&1 &
echo "PID: $!"
```

---

## 结论

**d000 SFT 无法立即启动。** 两个阻塞条件：
1. 模型 shard 3 仍在 SCP（预计几分钟内完成）
2. 全部 4 GPU 在跑 eval，GPU 1 最先释放（~11 min）

**下一步行动**：等 ~11 min 后 GPU 1 空闲 + 模型传输完成，立即启动 d000。是否需要我轮询等待并自动提交？

**需要关注**: Gemma-2 d000 accuracy 17.82% 异常低，大量 null prediction，建议排查 eval 脚本对 Gemma-2 的兼容性。

---
