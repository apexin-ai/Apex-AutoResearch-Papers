# ops check and launch 14b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-and-launch-14b_20260518T110103_result.json`
- **Structured JSON:** [`322c8e58b55c26b22588.json`](../../sessions/32/322c8e58b55c26b22588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Step 1: 模型下载状态

| 模型 | .incomplete | .safetensors | 大小 | 状态 |
|------|------------|-------------|------|------|
| **Qwen2.5-14B** | 1 | 7 | 26G | **下载中** (缺 1 shard + 1 incomplete) |
| **OLMo-2-7B** | 5 | 1 | 18G | **下载中** |
| **Gemma-2-9b** | 4 | 4 | 24G | **下载中** |
| **Phi-4** | 6 | 0 | 8.2G | **下载中** |

## Step 2: GPU 和 7B pilot 状态

| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 63459 MiB | 87% |
| 1 | 0 MiB | 0% |
| 2 | 0 MiB | 0% |
| 3 | 0 MiB | 100% |

PID 17819 存活，在 cuda:0 运行 7B pilot：
```
python exp001/train_sft.py --model-name Qwen2.5-7B --data-path sft_dosage_000.jsonl --output-dir Qwen2.5-7B_d000_s42 --seed 42 --gpu 0 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048
```

## Step 3: 7B pilot 进度

```
1849/3125 steps (59%), epoch 0.45, ~52 min elapsed
loss=0.939, grad_norm=0.25, lr=3.08e-05, mean_token_accuracy=0.784
~1.6s/it, 预计剩余 ~33 min
```

## Step 4: 14B pilot

**14B 尚未就绪** — incomplete=1, safetensors=7（需要 incomplete=0 且 safetensors≥8）。还有 1 个 shard 在下载中，无法启动 14B pilot。

GPU 3 显示 100% utilization 但 0 MiB 显存，可能是下载进程占用或瞬时状态。GPU 1 和 GPU 2 完全空闲，14B 下载完成后可立即在 cuda:2 启动。

---
