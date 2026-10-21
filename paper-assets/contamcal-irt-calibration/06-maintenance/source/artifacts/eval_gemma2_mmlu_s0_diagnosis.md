# eval_gemma2_mmlu_s0 诊断报告

**日期**: 2026-05-21 06:33 CST
**服务器**: westd-29999
**结论**: ❌ 误报 — 进程仍在正常运行

## 诊断结果

### 进程状态
- PID 445288 在 cuda:1 上活跃运行
- GPU 显存占用: 24148MiB / 97887MiB
- GPU 利用率: 90%

### 执行进度

| Dosage | 状态 | 开始时间 | Accuracy |
|--------|------|----------|----------|
| d000_s0 | 完成 | 06:04:37 | 0.6488 (9111/14042) |
| d005_s0 | 完成 | 06:16:12 | 0.6414 (9007/14042) |
| d025_s0 | 进行中 (~29%) | 06:27:38 | - |
| d050_s0 | 未开始 | - | - |

每个 dosage 评估约需 11 分钟（14042 items, ~22 it/s）。预计全部完成时间 ~06:49 CST。

### Cron 误判原因
Cron 检测逻辑查找 W&B sentinel/metrics（5 次检查均未发现），但此 eval 脚本**不使用 W&B**，只在本地写 `.done` sentinel 文件。因此 cron 将正常运行的进程误判为 failed。

### 脚本参数
```
CUDA_VISIBLE_DEVICES=1
evaluate.py md5: 17673bf373f00f83ccc41fc1d355a4cd (与 reference hash 一致)
--model-path /root/autodl-tmp/models/gemma-2-9b
--adapter-path /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d{dosage}_s0/lora_adapter
--benchmarks mmlu
--batch-size 8
lora_alpha=32 (已验证)
```

### GPU 状态 (06:30 CST)
| GPU | 显存 | 利用率 | PID |
|-----|------|--------|-----|
| 0 | 72447/97887 MiB | 98% | 437077 |
| 1 | 24157/97887 MiB | 90% | 445288 (本实验) |
| 2 | 0 MiB | 0% | - (空闲) |
| 3 | 64769/97887 MiB | 84% | 435054 |

### 建议
1. **不需要修复** — 进程正常运行，等待完成即可
2. **Cron 检测逻辑需修改** — eval 类任务不使用 W&B，应改为检测本地 `.done` sentinel 或进程存活状态
3. **不要重新提交** — 当前进程会在 ~20 分钟内完成所有 dosage
