# ops gemma2 gpu diag

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gemma2-gpu-diag_20260519T160536_result.json`
- **Structured JSON:** [`05d8781e8fda53830e84.json`](../../sessions/05/05d8781e8fda53830e84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Data collected. Here's the analysis:

---

## 1. GPU 状态对比

| GPU | 模型 | Util% | 显存占用 | 温度 | 功耗 |
|-----|------|-------|----------|------|------|
| 0 | Phi-4 14B | 82% | 57,897 / 97,887 MiB (59%) | 70°C | 442W |
| 1 | Qwen2.5-14B | 74% | 64,095 / 97,887 MiB (65%) | 62°C | 395W |
| 2 | OLMo-2 7B | 97% | 61,777 / 97,887 MiB (63%) | 65°C | 440W |
| 3 | Gemma-2 9B | **67%→93%** (波动大) | 54,647 / 97,887 MiB (**56%**) | 51°C | 544-578W |

注：GPU 3 两次 nvidia-smi 间隔数秒，从 67% 跳到 93%。用户报告的 64% 也是瞬时值。

## 2. 超参对比

| 参数 | Gemma-2 9B | Phi-4 14B | Qwen-14B | OLMo-2 7B |
|------|-----------|-----------|----------|-----------|
| batch_size | **1** | 1 | 1 | **2** |
| grad_accum | **16** | 16 | 16 | **8** |
| effective batch | 16 | 16 | 16 | 16 |
| lr | 5e-5 | 5e-5 | 5e-5 | 5e-5 |
| lora_r / alpha | 16 / 32 | 16 / 32 | 16 / 32 | 16 / 32 |
| max_seq_length | 2048 | 2048 | 2048 | 2048 |
| dataloader_num_workers | 4 | 4 | 4 | 4 |
| s/it (step ~950) | **~2.85s** | ~2.35s | ~3.05s | ~1.7s |

## 3. IO 瓶颈

无法直接检查（ssh_read_only 不允许 proc/io），但从间接证据判断：
- 4 个任务共享磁盘 IO，dataloader_num_workers=4，每个 GPU 训练进程有 4 个 worker 预取数据
- 总计 16 个 dataloader worker 并发读盘，可能存在 IO 竞争

## 4. 诊断结论

**GPU 利用率波动大（64-93%），不是持续偏低，而是周期性下降。** 根因：

**(a) batch_size=1 对 9B 模型偏小。** Gemma-2 9B 每个 microbatch 只处理 1 个样本，forward+backward 完成较快（模型比 14B 小），GPU 在等待下一个 sample 从 dataloader 送达时空闲。对比 OLMo-2 7B（相近大小）使用 batch_size=2，GPU 利用率 97%。batch_size=2 将每次 GPU 计算量翻倍，显著减少 data loading 空闲占比。

**(b) 显存利用率最低（56%），有增大 batch 的空间。** Gemma-2 只用了 54.6GB / 97.9GB，还有 ~43GB 余量。

**(c) Gemma-2 的 sliding window attention 架构** 导致不同层的计算量不均匀（交替的局部注意力和全局注意力），kernel 调度间隙略大于标准 dense attention 模型。

## 5. 建议修复

将 Gemma-2 的训练参数改为 `--batch-size 2 --grad-accum 8`（与 OLMo-2 一致），保持 effective batch size = 16 不变。预计显存增加 ~10-15GB（仍在安全范围内），GPU 利用率可提升到 90%+ 水平。

**注意：当前 d000 已训练 30%（step 960/3125），修改参数需要重启。** 建议在后续 dosage（d005/d025/d050/d100）开始前调整，不中断当前训练。

---
