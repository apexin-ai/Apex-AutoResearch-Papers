# diagnose sft falcon3 7b d100 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_falcon3_7b_d100_s42_20260522T080043_result.json`
- **Structured JSON:** [`f5fa677fc363bd4ae103.json`](../../sessions/f5/f5fa677fc363bd4ae103.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**训练没有失败——当前正在正常运行。**

| 项目 | 状态 |
|------|------|
| PID 666107 | 运行中，step 185/4159 |
| 显存 | 19582/24564 MiB (80%) |
| GPU 利用率 | 100% |
| 日志中 OOM/crash | **零** |

**"5 次崩溃"的实际原因**：是此前 bs=4 → bs=2 → bs=1(无 grad checkpoint）等不同配置的尝试逐一 OOM。当前配置（bs=1 + grad_accum=16 + gradient_checkpointing + bf16 LoRA）已稳定运行 12+ 分钟，显存余量约 5GB。

**一个非致命问题**：bitsandbytes 加载失败（缺 `libnvJitLink.so.13`），但当前未使用 QLoRA 所以不影响。如需 QLoRA 需先 `pip install nvidia-nvjitlink-cu12`。

**不需要干预**，预计 ~4.5 小时完成训练。报告已注册为 `art_20260522_f32b0a`。

---
