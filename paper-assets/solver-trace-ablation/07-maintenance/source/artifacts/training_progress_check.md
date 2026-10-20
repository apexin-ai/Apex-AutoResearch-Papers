# Training Progress Check — 2026-05-14 02:01 UTC

## Experiment Status

| Experiment | Steps | Progress | Last Timestamp | Est. Remaining |
|---|---|---|---|---|
| plan001-exec-only-s43-r4 (PID 136339, cuda:1) | 123/500 | 24.6% | 02:00:59 | ~46 min |
| plan013-random-reward-s42-r4 (PID 136261, cuda:0) | 165/500 | 33.0% | 02:00:57 | ~35 min |

### plan001-exec-only-s43-r4
- **Step rate**: ~7.3s/step (based on last 3 steps)
- **prove_rate**: 0.625 → 0.125 → 0.5 (fluctuating)
- **parse_rate**: 1.0 (stable)
- **loss**: -0.021 → 0.026 → 0.034

### plan013-random-reward-s42-r4
- **Step rate**: ~6.2s/step (based on last 3 steps)
- **prove_rate**: 0.5 → 1.0 → 0.375 (fluctuating)
- **parse_rate**: 1.0 (stable)
- **loss**: 0.0 → -0.024 → -0.027

## GPU Utilization

| GPU | Utilization | Memory Used | Memory Total |
|---|---|---|---|
| 0 (plan013) | 100% | 79811 MiB | 97887 MiB (81.5%) |
| 1 (plan001) | 91% | 80291 MiB | 97887 MiB (82.0%) |

## Disk Space

- `/root/autodl-tmp/`: 139G / 250G used (**112G free, 56%**)

## Risk Assessment

- **磁盘**: 112G 剩余，安全。两个实验均设 save_total_limit=1，预计总增长 < 50G。
- **GPU**: 两卡利用率 91-100%，正常。
- **训练**: 两个实验 parse_rate 均稳定 1.0，prove_rate 波动属正常。无异常。
- **预计完成时间**: plan013 ~02:36 UTC, plan001 ~02:47 UTC。
