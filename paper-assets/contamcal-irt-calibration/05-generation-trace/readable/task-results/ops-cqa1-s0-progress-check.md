# ops cqa1 s0 progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-s0-progress-check_20260520T030405_result.json`
- **Structured JSON:** [`cad7ab0aea4c9cfef4cc.json`](../../sessions/ca/cad7ab0aea4c9cfef4cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen-7B s0 训练状态

| 项目 | 状态 |
|------|------|
| **当前训练** | d000 (dosage=0%, 第1个) |
| **进度** | 376/3125 steps (12%) |
| **速度** | ~4.3 s/step |
| **已运行** | ~27 分钟 |
| **剩余** | ~3h 20min (当前 d000) |
| **已完成 checkpoint** | 0/5 (d000 目录已创建但训练中) |

**注意事项：**
- bitsandbytes 的 `libnvJitLink.so.13` 报错是非致命 warning（8bit optimizer 加载失败），训练正常进行
- GPU 0 使用 21.3GB/24.6GB 显存，利用率 100%，运行正常
- lora_alpha=32 ✓（符合 C006 约束）

**预计完成时间：**
- d000 单个: ~3.7h total → 约 14:20 CST 完成
- 全部 5 个 dosage (d000→d005→d025→d050→d100): 假设顺序训练，每个 ~3.7h → 全部完成约需 **18.5h**，预计 **明天 05:00 CST** 左右全部完成

---
