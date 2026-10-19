# ssh check status westd45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_status_westd45947_20260520T081950_result.json`
- **Structured JSON:** [`a1d2da69863eb9561638.json`](../../sessions/a1/a1d2da69863eb9561638.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 实验 | Step/30000 | Loss | LR | Speed(s/it) | VRAM |
|-----|------|------------|------|----|-------------|------|
| cuda:0 | a3_gradient_spatial_bowl_s0 | **58**/30000 (0.2%) | 0.26 | 1.45e-06 | ~13-16 | 16907/97887 MiB |
| cuda:1 | a3_gradient_object_pudding_s0 | **2560**/30000 (8.5%) | 0.22 | 2.48e-05 | ~12-16 | 16907/97887 MiB |

**进程状态:**
- PID 71494 (bowl): 存活，运行 20h27m，CPU 182%
- PID 73165 (pudding): 存活，运行 19h55m，CPU 204%

**GPU 利用率:** 两卡均显示 0%（nvidia-smi 采样瞬间未捕获到计算，但进程活跃、VRAM 占用正常）

**磁盘:**
```
/dev/md0  250G  22G  229G  9%  /root/autodl-tmp
```

**Checkpoint 轮转:**
- `a3_grad_refine_spatial_bowl_seed0/` — 0 个 checkpoint 子目录（仅 wandb_id.txt，step 58 尚未触发保存）
- `a3_grad_refine_object_pudding_seed0/` — 1 个 checkpoint: `2500/`（≤3，正常）

**SAVE_TOTAL_LIMIT 代码确认:** `train_pytorch.py:240` — `SAVE_TOTAL_LIMIT = 3` ✓

**注意:** bowl 实验运行 20h 但仅完成 58 步，速度极慢（~13-16s/it 但推算 20h 应有 ~5000 步）。日志显示中间有大段重复的初始化 + 多次从 step 0 重启的痕迹，可能经历了多次 restart。pudding 进度正常。

---
