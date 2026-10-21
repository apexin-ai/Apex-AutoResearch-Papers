# ops post restart check 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post_restart_check_45947_20260524T040401_result.json`
- **Structured JSON:** [`9c557650f16931522e9f.json`](../../sessions/9c/9c557650f16931522e9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-45947 状态

### 训练
| 实验 | PID | 存活 | 最新 ckpt step | 估算当前 step | 进度 |
|------|-----|------|---------------|-------------|------|
| seed0_l005 (λ_sdf=0.005) | 589765 (GPU 0) | ✅ | 24000 (10:34) | ~25400 | 80% → ~85% |
| seed0_l01 (λ_sdf=0.01) | 589840 (GPU 1) | ✅ | 24000 (10:38) | ~25400 | 80% → ~85% |

- 两个都是 `train_a1_sdf_aux_pi05.py --scene object_pudding --seed 0 --num_train_steps 30000`
- 速率 ~13 steps/min（22000→24000 用时 ~2.5h）
- **预计完成 ~18:20 今天**
- best_loss: l005=0.00883 @ 24000, l01=0.00901 @ 24000
- /tmp 日志不存在（输出在 tmux 中）

### GPU
| GPU | 型号 | 显存占用 | 利用率 | 温度 | 功率 |
|-----|------|---------|--------|------|------|
| 0 | RTX PRO 6000 | 27097/97887 MiB (28%) | 100% | 71°C | 476W/600W |
| 1 | RTX PRO 6000 | 27097/97887 MiB (28%) | 100% | 71°C | 464W/600W |

### LoRA Baseline 脚本
- 存在: Yes (`/root/colliforce-vla/scripts/train_pi05_lora_baseline.py`, May 23 14:35)
- Phase 2 >= 修复: Yes (L113: `if global_step >= self.warmup_phase_steps`)
- dummy parameter 修复: Yes (L105: `self._dummy = nn.Parameter(torch.zeros(1, device=device))`)
- Ready to launch: Yes

### 磁盘
| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /root/autodl-tmp | 250G | 176G | 75G | 71% |

---
