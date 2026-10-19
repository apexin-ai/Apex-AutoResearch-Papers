# diag full status check 0114

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full-status-check-0114_20260523T014735_result.json`
- **Structured JSON:** [`78517afeceacf2a997bd.json`](../../sessions/78/78517afeceacf2a997bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 28034 ===
GPU0: 空闲
GPU1: reduced-lora 训练 (21.7GB/32GB, 29%)
GPU2: 空闲
GPU3: 空闲

Eval PIDs 146135/146802/147325: 全部完成 ✓

Eval 结果:
  reduced-lora ckpt-2500: SYCONScore=0.1706  ToF=0.0939  NoF=0.9282
  reduced-lora ckpt-3000: SYCONScore=0.1705  ToF=0.0939  NoF=0.9227
  reduced-lora ckpt-3500: SYCONScore=0.1881  ToF=0.1050  NoF=0.9061
  --- 历史 ---
  gs8 ckpt-1000:          SYCONScore=0.0845  ToF=0.0442  NoF=0.9558
  ACT-s2 ckpt-6500:       SYCONScore=0.2543  ToF=0.1492  NoF=0.8619
  ACT-s2 ckpt-7000:       SYCONScore=0.2858  ToF=0.1713  NoF=0.8619

Reduced-lora 训练: step 4580/8000 (~57%)
  可用 ckpt: 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500

=== 29046 ===
GPU0: gs8 训练 (38.2GB/97.9GB, 95%)
GPU1: ACT-s2 训练 (23.3GB/97.9GB, 40%)

ACT s2: step 7900/8000 (~99%), 即将完成
  ckpt-7500: 存在 ✓
  ckpt-8000: 不存在（还没训到）
  可用 ckpt: 2000-7500 (每 500 步)

GS8: step 1374/8000 (~17%), reward≈0.57-0.63, ~24.5s/step
  可用 ckpt: 500, 1000

len512: 未启动（无日志）
```

**要点：**
- ACT-s2 还差 100 步就训完，预计 ~40 分钟出 ckpt-8000
- reduced-lora 三个 ckpt 的 SYCONScore 都很低（0.17-0.19），远低于 ACT-s2 ckpt-7000 的 0.2858
- gs8 ckpt-1000 评估结果最差（0.0845），但训练才 17%，后续 ckpt 可能提升

---
