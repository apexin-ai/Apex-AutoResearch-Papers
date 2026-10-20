# exp r7n2 supplement 100 200

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r7n2-supplement-100-200_20260516T063905_result.json`
- **Structured JSON:** [`f3fb0222045a35be9d4f.json`](../../sessions/f3/f3fb0222045a35be9d4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切就绪。汇总：

---

## 结果

**脚本路径**: `/root/autodl-tmp/simgate-modular-routing/src/r7n2_scale_study.py`

**修改**: 已添加 `--scales` 参数，支持只跑指定 scales。

**已有状态** (`results/ablation_r3/`):
- 100pct: 目录 seed43 存在但空（无 eval_results.json）
- 200pct: 目录 seed42/seed44 存在但空
- 即这些 runs 之前中断了，resume 逻辑不会跳过它们

**GPU1**: 空闲 (RTX 5090, 32GB VRAM, 0% utilization)

**eval batch_size = 2**: 已硬编码在脚本 L344

---

## 运行命令

```bash
cd /root/autodl-tmp/simgate-modular-routing && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=1 python src/r7n2_scale_study.py \
    --data_path data/plan-004-implicit/implicit_sft.jsonl \
    --model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
    --output_dir results/ablation_r3 \
    --gpu_id 0 \
    --seeds 42 43 \
    --scales 100pct 200pct \
    --batch_size 4 \
    --epochs 3
```

注意 `--gpu_id 0` 配合 `CUDA_VISIBLE_DEVICES=1`，让脚本认为设备 0 就是物理 GPU1。

---

## 预估时间

- 100%: ~1733 records × 2 seeds × 3 epochs → ~15-20 min/seed
- 200%: ~3466 records × 2 seeds × 3 epochs → ~30-40 min/seed
- **总计约 1.5-2 小时**（含 eval 生成推理时间）

---
