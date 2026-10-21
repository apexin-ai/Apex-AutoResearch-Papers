# ops westd gpu llama3 status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-gpu-llama3-status_20260521T103156_result.json`
- **Structured JSON:** [`682618fe89e76a3f4fc6.json`](../../sessions/68/682618fe89e76a3f4fc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

md5sum 和 python -c 带分号都被 read_only 阻止了。evaluate.py 字节数已获取到。

```
GPU 状态:
  GPU 0: 忙 — LLaMA-3.1-8B d025 SFT (PID 509578, CUDA_VISIBLE_DEVICES=0, 51GB/98GB, 85%)
  GPU 1: 忙 — LLaMA-3.1-8B d000 SFT (PID 508651, CUDA_VISIBLE_DEVICES=1, 44GB/98GB, 93%)
  GPU 2: 忙 — OLMo-2-7B d025 GSM8K eval (PID 511187, CUDA_VISIBLE_DEVICES=2, 17GB/98GB, 91%)
  GPU 3: 忙 — LLaMA-3.1-8B d100 SFT (PID 510203, CUDA_VISIBLE_DEVICES=3, 38GB/98GB, 97%)

LLaMA-3 训练:
  d000 (GPU 1): 767/3125 steps (24%), epoch 0.15, ~1h47m 剩余, loss≈1.37
  d025 (GPU 0): 606/3384 steps (18%), epoch 0.14, ~1h47m 剩余, loss≈1.47
  d100 (GPU 3): 490/4159 steps (12%), epoch 0.12, ~3h17m 剩余, loss≈1.51
  .done 文件均不存在，三个训练都在跑。

GPU2 eval 进程: 在跑 — OLMo-2 d025 GSM8K eval, 151/660 (23%), ~46min 剩余
  ⚠️ 这是之前用错误版本 evaluate.py 启动的 eval，仍在运行中。

evaluate.py: 37,775 bytes (md5 无法通过 read_only 获取，需要 ssh_execute)

磁盘: /root/autodl-tmp/ 233G/250G used (93%) — 仅剩 18GB，偏紧
```

**需要关注的问题:**
1. **GPU 2 eval 仍在跑错误版本** — 如需 kill 请确认（C009 约束：evaluate.py 版本不一致的 eval 结果无效）
2. **磁盘 93%** — 3 个 LLaMA-3 8B LoRA 训练会持续写 checkpoint，需注意空间
3. **evaluate.py 大小 37,775 bytes** — 与 C009 提到的 reference hash（37,591 bytes）不一致，差 184 bytes，需要确认是否为正确版本

---
