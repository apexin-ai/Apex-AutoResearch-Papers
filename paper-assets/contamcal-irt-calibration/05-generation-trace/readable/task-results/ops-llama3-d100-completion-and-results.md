# ops llama3 d100 completion and results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama3-d100-completion-and-results_20260521T132655_result.json`
- **Structured JSON:** [`e97d640877d961afc08b.json`](../../sessions/e9/e97d640877d961afc08b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
d100 训练: success (train_loss=1.404, epoch=1.0, runtime=11730s, lora_alpha=32 ✓)
d100 eval: MMLU 已自动触发 (monitor 21:24:52 检测到 .done → 启动 GPU 3)
           进度 244/14042 (~1.7%), ~24 it/s, ETA ~9min
d100 MMLU: pending
d100 ARC:  pending (MMLU 完成后需触发)
registry:  已更新 (conclusion=success, status=DONE)
GPU 状态:  GPU 0-2 空闲, GPU 3 运行 d100 MMLU eval (PID 525833, 18.6GB)
```

**已有 LLaMA-3.1-8B 结果汇总：**

| Dosage | MMLU | ARC |
|--------|------|-----|
| d000_s0 | 53.50% | 72.61% |
| d025_s0 | 52.75% | 72.01% |
| d100_s0 | pending | pending |

d025 相比 d000 略降（MMLU -0.75pp, ARC -0.60pp），需要等 d100 结果看完整 dosage-response curve。MMLU eval 预计 ~9 分钟内完成。

---
