# ops westd27271 cuda0 check and fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271-cuda0-check-and-fill_20260521T025625_result.json`
- **Structured JSON:** [`0a4b01d6e91998bcb6ad.json`](../../sessions/0a/0a4b01d6e91998bcb6ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## westd-27271 GPU 探查结果

### GPU 状态
| GPU | 型号 | 显存 | 状态 |
|-----|------|------|------|
| cuda:0 | RTX PRO 6000 Blackwell | 96GB | **空闲** (0MiB) |
| cuda:1 | RTX PRO 6000 Blackwell | 96GB | 占用 (42GB) — 正在训练 `train_openvla_smart_compress.py --config openvla_smart_compress_m32.yaml --resume openvla_sc_m32_seed42` |

### 磁盘
250GB 总量，已用 192GB，剩余 **59GB** (77%)。

### LIBERO 数据
`/root/autodl-tmp/libero_data/datasets/` 存在（具体 suite 文件在子目录中）。

### Eval 脚本（12个）
| 脚本 | 用途 |
|------|------|
| `eval_openvla_libero.py` | OpenVLA baseline eval |
| `eval_openvla_l2norm_libero.py` | OpenVLA baseline / random prune / L2-norm prune |
| `eval_openvla_smart_compress.py` | OpenVLA Smart Compress (VisionTokenCompressor) |
| `eval_smart_compress_libero.py` | SmolVLA Smart Compress |
| `eval_official_libero.py` | Official LIBERO eval |
| `eval_success_rate_libero.py` | Success rate (general) |
| `eval_sim.py` / `eval_success_rate.py` | Simulation eval |
| `eval_token_importance.py` | Token importance analysis |
| `eval_pruning_sweep.py` | Pruning sweep |
| `eval_acis_overhead.py` | ACIS overhead measurement |
| `eval_formal_bound.py` | Formal bound eval |

### Checkpoints
**OpenVLA Smart Compress:**
- `openvla_sc_m128_seed42/checkpoint.pt` — m=128, seed42
- `openvla_sc_m32_seed42/checkpoint.pt` + `checkpoint_step30000.pt` — m=32, seed42
- `openvla_sc_m128/checkpoint_step20000.pt` — m=128, step20k

**SmolVLA Smart Compress:**
- `smart_compress_m128_seed44/checkpoint.pt`
- `smart_compress_m16_seed44/checkpoint.pt`

**Baselines / Full-FT:**
- `libero_full_ft_50k`, `libero_full_ft_100k`, `libero_full_ft_seed0_100k`, `libero_lora_50k`
- `mlp_adapter_control`
- `baseline`

**IMM variants:** baseline_v6_alpha16, imm_anchor, imm_anchor_v7_1, v8, v8_1, v8b_twostage, v8c_annealing, etc.

### 已完成的关键 OpenVLA Object Eval
| 实验 | SR | seed |
|------|-----|------|
| OpenVLA baseline | **74.0%** | 7 |
| Random prune k=0.3 | — | 7 |
| Random prune k=0.5 | — | 7 |
| Random prune k=0.7 | **49.0%** | 7 |
| Random prune k=0.9 | — | 7/43 |
| Random prune k=0.95 | — | 7 |
| L2-norm prune k=0.7 | **49.8%** | 42 |
| L2-norm prune k=0.7 seed43 | **49.8%** | 43 |
| L2-norm k07 seed43 v2 | **49.8%** | 43 |
| SmolVLA Smart Compress m128 seed44 | **60.2%** | 44 |
| MLP adapter control | — | 42/43/44 |

### **尚未完成 / 可立即运行的实验**

1. **OpenVLA Smart Compress m128 eval (seed42)** — checkpoint 已有 (`openvla_sc_m128_seed42/checkpoint.pt`)，无对应 eval 结果。最高优先级，直接对比 baseline 74% 和 random prune。
   ```bash
   CUDA_VISIBLE_DEVICES=0 python eval_openvla_smart_compress.py \
     --n_queries 128 --checkpoint_path checkpoints/openvla_sc_m128_seed42/checkpoint.pt \
     --suite libero_object --num_episodes 50 --gpu 0
   ```

2. **OpenVLA Smart Compress m32 eval (seed42, step30k)** — checkpoint 已有，验证更激进压缩 (m=32) 的效果。

3. **OpenVLA L2-norm prune 其他 k 值 (k=0.5, k=0.3)** — sweep 日志显示 k=0.5/0.3 跑过但结果文件缺失或不完整。

4. **OpenVLA baseline 多 seed 验证** — 当前 baseline 只有 seed=7，可跑 seed=42/43 建立 CI。

5. **OpenVLA Spatial suite eval** — `eval_openvla_baseline_spatial.json` 存在但只有 1 个结果文件，Smart Compress / L2-norm 在 spatial 上尚未评估。

**建议优先跑 #1（OpenVLA SC m128 eval）**，这是当前最缺的数据点——有训练好的 checkpoint 但没有 eval 结果，且与 cuda:1 上正在训练的 m32 形成对照。

---
