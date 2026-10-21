# code eval readiness check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_readiness_check_20260514T183334_result.json`
- **Structured JSON:** [`11b6deb2ab64bb8bbf58.json`](../../sessions/11/11b6deb2ab64bb8bbf58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. eval_perplexity.py 参数列表

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--checkpoints` | nargs="+" | **required** | checkpoint 路径列表 |
| `--data_path` | str | **required** | eval 数据路径 |
| `--max_docs` | int | 5000 | 最大文档数 |
| `--max_length` | int | 2048 | 上下文长度 |
| `--output_path` | str | eval_perplexity_results.json | 输出文件 |

脚本会对每个 checkpoint 依次加载模型 → eval → 释放显存 → 下一个。使用 `fp16` + `.cuda()` 单 GPU。

### 2. eval 数据

- 路径: `data/human/eval_holdout.jsonl` — 67,823 行
- 格式: `{"text": "...", "depth": 0, "source": "fineweb"}`

### 3. Checkpoint 目录状态 — **训练尚未完成**

| seed | 已有 checkpoints | 当前 step | 总 steps | 进度 | final/ |
|------|-----------------|-----------|----------|------|--------|
| 42 | 1500, 2000, 2500 | 2754 | 6103 | ~45% | **无** |
| 123 | 1500, 2000, 2500 | ~2754 | 6103 | ~45% | **无** |
| 456 | 1000, 1500, 2000 | 2249 | 6103 | ~37% | **无** |

**三组训练都在跑，都没有 `final/` 目录。** 必须等训练完成后才能 eval。

### 4. GPU 显存

```
GPU 0: 46523 / 97887 MiB (99%)
GPU 1: 46523 / 97887 MiB (99%)
GPU 2: 46523 / 97887 MiB (94%)
GPU 3: 46523 / 97887 MiB (99%)
```

4x 96GB GPU，每卡已用 ~46.5GB，剩余 ~51GB。Qwen3-0.6B fp16 约 1.2GB + KV cache < 3GB，**eval 可与训练并行**，用 `CUDA_VISIBLE_DEVICES=0` 指定任一卡即可。

### 5. Eval 命令模板（训练完成后执行）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && \
CUDA_VISIBLE_DEVICES=0 python eval_perplexity.py \
  --checkpoints output/models/adaptive_fix_seed42/final \
                output/models/adaptive_fix_seed123/final \
                output/models/adaptive_fix_seed456/final \
  --data_path data/human/eval_holdout.jsonl \
  --max_docs 5000 \
  --output_path output/eval_adaptive_fix_results.json
```

三个 seed 可以一次性传入 `--checkpoints`，脚本会依次 eval 并汇总到一个 JSON。

### 6. MVP 判定备忘

训练完成 + eval 出结果后的判定逻辑：

```
uniform_mean = (17.69 + 17.69 + 17.70) / 3 = 17.6933
grid_best_improvement = 17.69 - 17.638 = 0.052
threshold = 0.052 * 0.9 = 0.0468

adaptive_fix_mean = (ppl_42 + ppl_123 + ppl_456) / 3
adaptive_fix_improvement = uniform_mean - adaptive_fix_mean

PASS if adaptive_fix_improvement >= 0.0468
即 adaptive_fix_mean <= 17.6933 - 0.0468 = 17.6465
```

**当前状态：需等训练跑完（估计还需约 55% 的时间），出现 `final/` 目录后再执行 eval。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "text": "...",
    "depth": 0,
    "source": "fineweb"
  }
}
```

</details>

---
