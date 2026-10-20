# exp dpo dryrun cuda3

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_dpo-dryrun-cuda3_20260512T133520_result.json`
- **Structured JSON:** [`baa7c6d8cabed7d02a26.json`](../../sessions/ba/baa7c6d8cabed7d02a26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 文件部署验证

| 文件 | 行数 | 验证 | 状态 |
|------|------|------|------|
| `train_dpo.py` | 247 → 远程修改为 QLoRA 版本 | `learning_rate` ✓ | **PASS** |
| `build_dpo_pairs.py` | 251 | `wc -l` ✓ | **PASS** |
| `generate_synthetic_corpus.py` | 665 | `postprocess_traces` ✓ | **PASS** |

### 2. DPO dry-run 结果：**成功**

- 3 steps (10 条 dummy 数据, batch_size=1, grad_accum=4, 1 epoch)
- **train_loss: 0.5898**
- loss 从 0.6931 → 0.6931 → 0.3832（第 3 步开始收敛）
- `rewards/accuracies` 从 0.0 → 1.0（第 3 步）
- runtime: 9.15s

### 3. GPU 显存

训练完成后 GPU 3 已释放（0 MiB）。训练过程中 QLoRA 4-bit 模型 + LoRA + optimizer 预估 ~10-12 GB（基于 24 GB 卡未 OOM）。

### 4. 参数调整

原始 bf16 代码需要以下修改才能在单 4090D 上跑通：
- `flash_attention_2` → `sdpa`（flash_attn 未安装）
- `torch_dtype` → 移除（已废弃）
- `max_prompt_length` → 移除（TRL 1.4.0 不支持）
- `device_map="auto"` → `device_map={"": 0}`
- **bf16 → QLoRA 4-bit**（单卡 24GB 无法容纳 bf16 模型 + DPO reference model）
- `batch_size=1` 即可

### 5. nvidia-smi 确认

| GPU | 显存占用 | 说明 |
|-----|---------|------|
| 0 | 7763/24564 MiB | 其他进程 |
| 1 | 0/24564 MiB | 空闲 |
| **2** | **22103/24564 MiB** | **mvp-004 实验，未动** |
| **3** | **0/24564 MiB** | **dry-run 完成，已释放** |
| 4 | 0/24564 MiB | 空闲 |
| 5 | 18736/24564 MiB | 其他进程 |

GPU 2 的 mvp-004 实验完好无损。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "": 0
  }
}
```

</details>

---
