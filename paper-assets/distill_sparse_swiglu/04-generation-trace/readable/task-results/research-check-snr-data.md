# research check snr data

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_snr_data_20260520T022941_result.json`
- **Structured JSON:** [`f2260502ca17e35cb6fe.json`](../../sessions/f2/f2260502ca17e35cb6fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full picture:

## SNR 数据可用性报告

### 1. 数据文件列表

| 文件 | 大小 | 日期 |
|------|------|------|
| `artifacts/gradient_snr_results.json` | 173KB | May 17 | 初始版（200 steps，无 CI）|
| `artifacts/gradient_snr_constrained_results.json` | 4.4KB | May 17 | 受约束版（200 steps）|
| `artifacts/snr_extended_results.json` | 34KB | May 18 | **主版本**（300 steps，带 95% CI）|

脚本：`scripts/gradient_snr_extended.py`（存在）。`src/gen_gradient_snr.py` **不存在**。

### 2. 覆盖的 step 范围

`snr_extended_results.json` 覆盖 **steps 0, 50, 100, 150, 200, 250, 300**（7 个 checkpoint），每个 checkpoint 包含 32 层的 per-layer SNR + mean/CI。

**step 300-1000 的数据不存在。** 所有三个文件最远只到 step 300。

### 3. 覆盖的 loss type

- **KL**（7 个 SNR snapshots + loss curve，每 10 steps 记录）
- **BCE**（7 个 SNR snapshots + loss curve，每 10 steps 记录）
- **MSE 不存在**

### 4. 是否需要补充数据

论文当前写法是 "step 300 of 1000"，即声称训练跑到 1000 步但只在 300 步时测了 SNR。Appendix G（`app:snr_extended`）目前只描述 0-300 的 trajectory，**没有要求 300-1000 的数据**。

**现有数据对当前 Appendix G 的写法是完整的。** 如果要扩展 trajectory 到 step 1000，需要重新运行 `gradient_snr_extended.py` 并把 `SNAPSHOT_STEPS` 扩展到 `[0, 50, 100, 150, 200, 250, 300, 500, 750, 1000]`，同时把 `--num_steps` 设为 1000。

### 5. 运行命令和依赖

```bash
python /root/distill_sparse_swiglu/scripts/gradient_snr_extended.py
```

依赖（均来自项目 `src/`）：
- `data_utils.get_calibration_loader`
- `losses.BCESparsityLoss`, `losses.KLDistillLoss`
- `predictor.PredictorWrapper`
- `transformers`, `torch`

配置：`num_steps=300, batch_size=4, seq_len=2048, lr=0.001, warmup_steps=100, sparsity_target=0.3, kl_temperature=1.0`

---
