# ops verify d100 s123 start

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-d100-s123-start_20260518T173013_result.json`
- **Structured JSON:** [`d235648db2d468dac375.json`](../../sessions/d2/d235648db2d468dac375.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**启动成功。**

| 检查项 | 结果 |
|---|---|
| PID 46871 存活 | ✅ bash wrapper 运行中 |
| 实际训练进程 | PID 46876，`Rl` 状态（CPU 918%，正在加载/编译） |
| cuda:3 显存 | ✅ 当前 3MiB（模型还在 CPU 加载阶段，尚未上 GPU） |
| LoRA 参数 | alpha=32 ✅（符合 C006） |
| CUDA_VISIBLE_DEVICES | =3 ✅（符合 C004） |
| 日志状态 | 模型权重已加载完毕，LoRA 配置完成，训练数据 66533 samples 已加载，即将开始训练 |
| 唯一性 | `Qwen2.5-7B_d100_s123` 只有一组进程（46871→46875→46876）✅ |

模型加载和数据准备均完成，正在 torch.compile 阶段，预计几分钟后上 GPU 开始训练。

---
