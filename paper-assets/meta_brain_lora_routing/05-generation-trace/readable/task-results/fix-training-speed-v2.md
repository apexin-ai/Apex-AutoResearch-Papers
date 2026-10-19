# fix training speed v2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_training_speed_v2_20260516T034219_result.json`
- **Structured JSON:** [`996ef5e3104b1cfa0351.json`](../../sessions/99/996ef5e3104b1cfa0351.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 种配置 dry-run 通过。汇总报告：

---

## 汇报

### 1. Kill 结果 + Checkpoint

- 旧进程 (PID 370295/370372/370451/370656) 已被前一个 Worker kill，4 GPU 全部空闲 (0%/0 MiB)
- Dry-run 生成的测试 checkpoint 在 `checkpoints/lora_{type}_r{rank}/final`，可被正式训练覆盖

### 2. 瓶颈根因（均已修复）

| 瓶颈 | 影响 |
|------|------|
| `batch_size=2`，96GB VRAM 只用 8GB | GPU compute 严重空转 |
| 全 fp32 forward/backward | 计算量翻倍，无 Tensor Core 加速 |
| `DataLoader num_workers=0` | 主线程同步 I/O，GPU 等数据 |
| 无 cuDNN benchmark / TF32 | 矩阵运算走慢路径 |

### 3. 修改清单

**前一个 Worker 已完成：**
- batch_size 2→16, bf16 autocast, num_workers 0→4
- cuDNN benchmark + TF32 matmul
- data_loader.py: pin_memory, persistent_workers, prefetch_factor=4

**本 Worker 完成：**
- `num_train_steps` 30000→10000
- 修复 `sys.path` 缺项目根目录，导致 `from phase1.augment_spatial` ImportError

### 4. 优化后性能

| 指标 | 优化前 | 优化后 |
|------|--------|--------|
| step 速度 | 18 s/step | **~1.0 s/step** (18x) |
| VRAM | ~8 GB | ~12.7 GB / 96 GB (13%) |
| batch_size | 2 | 16 |
| 总 steps | 30,000 | 10,000 |

5 种配置 dry-run 结果一致：

| 配置 | trainable | step 0 (warmup) | steady-state | EXIT |
|------|-----------|-----------------|-------------|------|
| visual r16 | 3.7M (0.11%) | 4.1s | ~1.0 s/step | 0 |
| physical r16 | 3.7M (0.11%) | 4.1s | ~1.0 s/step | 0 |
| spatial r16 | 3.7M (0.11%) | 4.1s | ~1.0 s/step | 0 |
| universal r16 | 3.7M (0.11%) | 4.2s | ~1.0 s/step | 0 |
| universal r48 | 11.1M (0.31%) | 4.1s | ~1.0 s/step | 0 |

### 5. 推荐训练命令

```bash
cd /root/meta_brain_lora_routing && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python phase1/train_lora_expert.py --perturbation_type visual   --gpu_id 0 --batch_size 16 &
python phase1/train_lora_expert.py --perturbation_type spatial  --gpu_id 1 --batch_size 16 &
python phase1/train_lora_expert.py --perturbation_type physical --gpu_id 2 --batch_size 16 &
python phase1/train_lora_expert.py --perturbation_type universal --gpu_id 3 --batch_size 16 --lora_rank 48 &
wait
```

### 6. 预计训练时长

- 10,000 steps × 1.0 s/step = **~2.8 小时/adapter**
- 4 路并行 → 总墙钟 **~3 小时**（含 ~1 min 模型加载）

---
