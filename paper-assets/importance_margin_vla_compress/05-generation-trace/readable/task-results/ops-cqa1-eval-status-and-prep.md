# ops cqa1 eval status and prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_eval_status_and_prep_20260519T221346_result.json`
- **Structured JSON:** [`6432efc0439c2c1cf4f2.json`](../../sessions/64/6432efc0439c2c1cf4f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总如下：

---

## 1. eval_m32_official 结果 ✅ 已完成

| 指标 | 值 |
|------|-----|
| **Overall SR** | **53.4%** (267/500) |
| **95% Wilson CI** | **[49.0%, 57.7%]** |
| Seed | 42 |

Per-task breakdown:
| Task | SR |
|------|-----|
| alphabet soup | 64% |
| cream cheese | 48% |
| salad dressing | 56% |
| bbq sauce | 46% |
| ketchup | 46% |
| tomato sauce | 28% |
| butter | **78%** |
| milk | 42% |
| chocolate pudding | 66% |
| orange juice | 60% |

---

## 2. m128_seed43 / m16_seed43 训练进度

| 训练 | GPU | Step | 目标 | SPS | ETA |
|------|-----|------|------|-----|-----|
| **m128_seed43** | 1 | 97100/100000 | 100k | 3.9 | **~10 min** |
| **m16_seed43** | 2 | 97100/100000 | 100k | 3.9 | **~10 min** |
| m16_seed44 | 0 | 75400/100000 | 100k | 4.1 | **~1h** |

m128_seed43 和 m16_seed43 都在 97.1%，约 10 分钟后完成。

---

## 3. GPU 3 可用性

GPU 3 **完全空闲**（0MiB, 0% util）。m32_official eval 已完成。

已有 eval 结果中，尚未 eval 的 seed43 checkpoint：
- `eval_smart_compress_m32_seed43.json` ✅ 已有
- `eval_smart_compress_m64_seed43.json` ✅ 已有  
- `eval_smart_compress_m96_seed43.json` ✅ 已有（v2）
- `eval_smart_compress_m128_seed43.json` ❌ 待 eval（训练即将完成）
- `eval_smart_compress_m16_seed43.json` ❌ 待 eval（训练即将完成）

seed44 系列：m32/m64/m96 的 seed44 eval 已有，m16_seed44 还在训练（75k/100k）。

**建议**：GPU 3 现在空闲，但 m128_seed43 和 m16_seed43 约 10 分钟后完成，可以等完成后立即在 GPU 1 和 GPU 2 上启动 eval（训练完成自动释放）。或者如果想提前利用 GPU 3，可以挑一个已完成但未 eval 的配置跑。

---

## 4. 准备好的 eval 命令

**m128_seed43 eval**（训练完成后在 GPU 1 上跑）：
```bash
bash -c "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl python -u eval_smart_compress_libero.py --n_queries 128 --checkpoint_path checkpoints/smart_compress_m128_seed43/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 43 --output eval_results/eval_smart_compress_m128_seed43.json 2>&1 | tee logs/eval_smart_compress_m128_seed43.log"
```

**m16_seed43 eval**（训练完成后在 GPU 2 上跑）：
```bash
bash -c "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_smart_compress_libero.py --n_queries 16 --checkpoint_path checkpoints/smart_compress_m16_seed43/checkpoint.pt --suite libero_object --num_episodes 500 --gpu 0 --seed 43 --output eval_results/eval_smart_compress_m16_seed43.json 2>&1 | tee logs/eval_smart_compress_m16_seed43.log"
```

两个 checkpoint 路径已确认存在。训练约 10 分钟内完成，完成后即可在对应 GPU 上启动 eval。

---
