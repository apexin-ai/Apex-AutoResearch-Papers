# diagnose exp 001 sft s123 failures

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_s123_failures_20260513T203803_result.json`
- **Structured JSON:** [`302005123c8a45b72224.json`](../../sessions/30/302005123c8a45b72224.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 每个实验的失败原因

两个实验的致命错误完全相同：

```
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 7.31 MiB is free. Process 204758 has 22.53 GiB memory in use.
```

（bitsandbytes 的 `libnvJitLink.so.13` 错误只是 warning，不是致命原因）

### 2. 根因分析

**两个实验的启动命令都写了 `--gpu 0`，但 GPU 0 被一个 vLLM 推理引擎（PID 204758）占满了 23 GiB。**

当前 GPU 占用情况：

| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 23068 / 24564 MiB | **VLLM::EngineCore** (PID 204758) |
| 1 | **0 MiB — 空闲** | — |
| 2 | **0 MiB — 空闲** | — |
| 3 | **0 MiB — 空闲** | — |
| 4 | 21552 MiB | python (其他实验) |
| 5 | 18654 MiB | python (其他实验) |

任务描述说 1.5B 应在 cuda:2、0.5B 应在 cuda:1，但实际命令里都是 `--gpu 0`，与 vLLM 冲突导致 OOM 秒退。

### 3. 修复建议

用空闲 GPU 重新提交，改 `--gpu` 参数即可：

**1.5B (用 GPU 2)：**
```bash
python /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123 \
  --seed 123 --gpu 2 --batch-size 2 --grad-accum 8 \
  --cache-dir /root/autodl-tmp/.hf_cache
```

**0.5B (用 GPU 1)：**
```bash
python /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
  --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123 \
  --seed 123 --gpu 1 --batch-size 4 --grad-accum 4 \
  --cache-dir /root/autodl-tmp/.hf_cache
```

GPU 3 也空闲可用作备选。

---
