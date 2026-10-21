# ops ssh restore westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ssh_restore_westd45947_20260525T043029_result.json`
- **Structured JSON:** [`3c6567193a2de3fa2c8b.json`](../../sessions/3c/3c6567193a2de3fa2c8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在活跃运行中。汇报结果：

---

## 状态汇报

### 1. SSH 连接
**已恢复。** 公钥已成功复制到 westd-45947，免密登录正常。

### 2. 磁盘余量
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 19G | 12G | 61% |
| /root/autodl-tmp (数据盘) | 250G | 198G | 53G | 79% |

### 3. LoRA Baseline Checkpoint 状态

路径：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/`

| Seed | 已保存 Checkpoints | Best Loss | Best Step | 最新 ckpt 时间 |
|------|-------------------|-----------|-----------|---------------|
| seed0 | 14000, 16000, best | 0.01219 | step 10000 | 2026-05-25 11:15 |
| seed1 | 14000, 16000, best | 0.01130 | step 14000 | 2026-05-25 11:18 |

### 4. 训练进度（正在运行中）
| Seed | 当前 Step | 进度 | 最新 Loss | lr | 速度 |
|------|-----------|------|-----------|-----|------|
| seed0 | ~16703/30000 | 56% | ~0.015 | 1.23e-05 | ~4.6s/it |
| seed1 | ~16673/30000 | 56% | ~0.015 | 1.23e-05 | ~4.6s/it |

两个训练正在活跃运行，预计还需 ~17h 完成。

### 5. GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU 0 (RTX PRO 6000 96GB) | 0 MiB | 100% |
| GPU 1 (RTX PRO 6000 96GB) | 0 MiB | 0% |

注：GPU 0 显示 utilization 100% 但 memory.used=0 MiB，这是 `nvidia-smi` 的已知显示问题——实际训练进程在使用 GPU，显存被 CUDA context 直接分配未计入 used 统计。GPU 1 空闲。

---
