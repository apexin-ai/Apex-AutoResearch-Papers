# Training Progress Check — 2026-05-15 07:10 UTC+8

## 1. CLS 8B s42 resume (cuda:1, PID 295794)

| 项目 | 值 |
|------|------|
| 当前 step | ~946 / 6633 (14%) |
| Epoch | 0.41 |
| 训练速度 | ~8.2 s/step (纯训练), ~11.5 s/step (含 eval) |
| Loss | 0.9594 (step 900) |
| 已运行 | 1h06m |
| 预计完成 | ~18h 后 → **May 16 01:00** |

### 已产出 Checkpoints
| Checkpoint | 时间 | 大小 |
|-----------|------|------|
| checkpoint-800 | May 15 06:34 | 176M |

### 预期后续 Checkpoints (save_steps=200, save_total_limit=35)
800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600 (~30 个)

---

## 2. CWM 8B conda v4 (cuda:2, PID 266816)

| 项目 | 值 |
|------|------|
| 当前 step | ~2400 / 6633 (36%) |
| Epoch | 1.04 |
| 训练速度 | ~12 s/step (纯训练), ~23.6 s/step (含 eval, eval 每 100 步) |
| Loss | 0.0978 (step 2400 附近) |
| Eval loss | 0.4145 |
| 已运行 | 5h10m (从 ckpt-1600 续训) |
| 预计完成 | ~28h 后 → **May 16 11:00** |

### 已产出 Checkpoints (save_total_limit=5)
| Checkpoint | 时间 |
|-----------|------|
| checkpoint-400 | May 14 16:32 |
| checkpoint-2000 | May 15 04:28 |
| checkpoint-2100 | May 15 05:07 |
| checkpoint-2200 | May 15 05:46 |
| checkpoint-2300 | May 15 06:26 |

注意: save_total_limit=5, 旧 checkpoint 会被删除。

---

## 3. CLS 8B seed123 conda v3 (cuda:3, PID 266444)

| 项目 | 值 |
|------|------|
| 当前 step | ~4521 / 6633 (68%) |
| Epoch | 2.04 |
| 训练速度 | ~8.2 s/step (纯训练), ~12.25 s/step (含 eval) |
| Loss | 0.2483 (step 4500) |
| Eval loss | 0.4112 |
| 已运行 | 5h11m (从 ckpt-3000 续训) |
| 预计完成 | ~7.2h 后 → **May 15 14:20** |

### 已产出 Checkpoints (save_total_limit=5)
| Checkpoint | 时间 |
|-----------|------|
| checkpoint-200 | May 14 14:35 |
| checkpoint-3800 | May 15 04:33 |
| checkpoint-4000 | May 15 05:14 |
| checkpoint-4200 | May 15 05:55 |
| checkpoint-4400 | May 15 06:37 |

---

## 4. 磁盘使用

```
Filesystem      Size  Used Avail Use%
/dev/md0        250G  137G  114G  55%
```

当前 checkpoint 占用:
- s42 resume: 176M (1 个 ckpt)
- CWM 8B: 880M (5 个 ckpt)
- seed123: 880M (5 个 ckpt)

s42 resume 最终产出 ~30 个 ckpt × 176M = **~5.3 GB**, 磁盘空间充足 (114G 可用)。

---

## 5. s42 resume val@8192 sweep 规划

完成后预期 ~30 个 checkpoint 需要跑 val sweep:
- checkpoint-800 到 checkpoint-6600, 间隔 200 步
- 每个 ckpt 一次 val@8192 评估
- 可在训练完成后统一启动, 也可在训练过程中对已产出的 ckpt 提前跑 val
