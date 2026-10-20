# exp012_llama_8b_r2_exp2 诊断报告

**检查时间**: 2026-05-16 ~04:05 UTC

## 进程状态

| 项目 | 状态 |
|------|------|
| PID 321037 | **ALIVE**, STAT=Ss+, etime=09:05 |
| 子进程 PID 321407 | VLLM::EngineCore, 占用 GPU 79788 MiB |
| GPU | RTX PRO 6000 Blackwell, ~78GB/98GB 已用 |
| 磁盘 /root/autodl-tmp/ | 213G/250G (85%) |

## 运行进度

- **Batch 配置**: 2 个 count 组 (count_6, count_12)，每组 22 batches (low_bcs + high_bcs + 20 random)，共 44 batches
- **已完成**: count_6 组 21/22 batches（low_bcs, high_bcs, random/0~18），正在运行 random/19
- **进度**: ~48% (21/44)
- **每 batch 耗时**: 平均 ~15s，偶尔 ~67s
- **预计剩余**: ~10-15 分钟

## 日志尾部

```
2026-05-16 04:05:08 Batch count_6/random/18 done: 65.9s total, 1000 outputs
2026-05-16 04:05:08 Running batch count_6/random/19 (6 types, BCS=0.8772) on 1000 samples
```

vLLM 推理速度正常：~400K toks/s input, ~3K toks/s output。

## 结果文件

- 输出目录: `artifacts/exp012/`（脚本配置）
- `results/` 下暂无 exp012 新文件产出（exp2 结果可能在运行结束后统一写入）

## 诊断结论

**进程正常运行中。** PID 存活，GPU 活跃占用，日志持续产出，batch 稳定推进。

注意：etime 仅 9 分钟，与"2 小时前提交"不符。可能原因：提交后脚本前置步骤（cache drop、模型加载）耗时，或 tmux 内实际启动时间较晚。Registry 状态为 PREPARING 需要更新为 RUNNING。
