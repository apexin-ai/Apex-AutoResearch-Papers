# ops verify 3B sft s123 startup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-3B-sft-s123-startup_20260515T120003_result.json`
- **Structured JSON:** [`e953aac520f564300fc4.json`](../../sessions/e9/e953aac520f564300fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

| 项目 | exp_001_sft_3B_d005_s123 | exp_001_sft_3B_d025_s123 |
|------|--------------------------|--------------------------|
| PID | 555931 ✅ 存活 | 556011 ✅ 存活 |
| 运行时间 | ~1m48s | ~1m45s |
| GPU | cuda:2, 88% util, 22.9/24.6 GB | cuda:4, 86% util, 19.3/24.6 GB |
| 训练样本 | 50,826 | 54,133 |
| Tokenization | ✅ 完成 | ✅ 完成 |
| 训练进度 | step 12/3177 (~3.5s/it) | step 17/3384 (~2.9s/it) |
| Loss | 尚未输出（刚开始训练） | 尚未输出 |
| 异常 | 无（bitsandbytes warning 可忽略，不影响训练） | 同左 |

两个训练都正常启动，GPU 显存占用正常，无 OOM。bitsandbytes 的 `libnvJitLink.so.13` 报错是 warning 级别，不影响 LoRA 训练（只影响 8bit/4bit 量化功能）。预计首次 loss 输出在 step 10 的 eval log 或后续 logging step。

---
