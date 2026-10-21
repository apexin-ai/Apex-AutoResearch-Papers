# Training Status 2026-05-23

Checked at ~UTC now. All 8 PIDs alive, all GPUs at 97-100% utilization.

## westd-17855

| Experiment | Gen Progress | PID alive | GPU util | Notes |
|---|---|---|---|---|
| t15_a060_s43_fp32 (cuda:0) | 14/15 (gen_0–13 done) | Yes (14h27m, CPU 141%) | 100%, 30.9/97.9 GB | gen_13 has trainer+synthetic_data; training gen_14 |
| t15_a050_s43_fp32 (cuda:1) | 14/15 (gen_0–13 dirs) | Yes (14h24m, CPU 97%) | 89%, 27.7/97.9 GB | Log: gen_12 done, gen_13 started; mauve metric failing (network unreachable for gpt2-large) |
| t10_a050_s44_fp32 (cuda:2) | 8/10 (gen_0–7 done) | Yes (8h07m, CPU 0%) | 97%, 27.7/97.9 GB | No log file found; GPU active |
| t10_a060_s44_fp32 (cuda:3) | 8/10 (gen_0–7 done) | Yes (8h13m, CPU 0%) | 100%, 27.7/97.9 GB | No log file found; GPU active |
| t10_a045_s44_fp32 (cuda:4) | 5/10 (gen_0–4 done) | Yes (4h41m, CPU 0%) | 99%, 30.9/97.9 GB | Log: training gen_5, step 3659/5000 (73%) @ 2.18 it/s |
| t15_a045_s43_fp32 (cuda:5) | 12/15 (gen_0–11 done) | Yes (12h17m, CPU 0%) | 99%, 27.7/97.9 GB | Log: training gen_12, step 1016/5000 (20%) @ 2.18 it/s |

## westd-19828

| Experiment | Gen Progress | PID alive | GPU util | Notes |
|---|---|---|---|---|
| t15_a075_s43_fp32 (cuda:0) | 10/15 (gen_0–9 done) | Yes (10h32m, CPU 97%) | 97%, 27.7/97.9 GB | No log file found; GPU active |
| t10_a075_s44_fp32 (cuda:1) | 8/10 (gen_0–7 done) | Yes (8h12m, CPU 0%) | 99%, 27.7/97.9 GB | Log: loading model for gen_8 |

## 预计完成时间

Training rate: 5000 steps @ 2.18 it/s ≈ 38 min/gen training + ~12 min data gen & metrics ≈ **50 min/gen**.

| Experiment | Remaining gens | Est. time remaining | Est. completion (UTC) |
|---|---|---|---|
| t15_a060_s43_fp32 | 1 | ~1h | ~1h from now |
| t15_a050_s43_fp32 | 1–2 | ~1–1.5h | ~1.5h from now |
| t10_a050_s44_fp32 | 2 | ~1.5h | ~1.5h from now |
| t10_a060_s44_fp32 | 2 | ~1.5h | ~1.5h from now |
| t10_a045_s44_fp32 | ~4.5 (gen_5 at 73%) | ~4h | ~4h from now |
| t15_a045_s43_fp32 | ~3 (gen_12 at 20%) | ~2.5h | ~2.5h from now |
| t15_a075_s43_fp32 | 5 | ~4h | ~4h from now |
| t10_a075_s44_fp32 | 2 | ~1.5h | ~1.5h from now |

### 注意事项
- **mauve 指标失败**：t15_a050_s43 因网络不可达无法下载 gpt2-large，mauve 返回 N/A。其他实验可能也有同样问题。
- **CPU 0% 异常**：6/8 进程 CPU 显示 0.0%，但 GPU 全部 97-100%，训练正常进行。可能是 ps 对长时间 GPU-bound 进程的统计偏差。
- 最早完成：t15_a060_s43（~1h），最晚完成：t10_a045_s44 和 t15_a075_s43（~4h）。
