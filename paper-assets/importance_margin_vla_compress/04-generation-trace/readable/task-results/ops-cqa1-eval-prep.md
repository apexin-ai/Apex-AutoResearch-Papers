# ops cqa1 eval prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_eval_prep_20260519T200310_result.json`
- **Structured JSON:** [`24ff610564651d37ab25.json`](../../sessions/24/24ff610564651d37ab25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 checkpoint 都确认存在。汇报如下：

---

## 训练进度

| 实验 | GPU | Step | Loss (最近) | SPS | 预计剩余 |
|------|-----|------|------------|-----|---------|
| **m128_seed43** | cqa1:1 | 68150/100K | 0.043~0.091 | 4.1 | ~2.2h |
| **m16_seed43** | cqa1:2 | 67600/100K | 0.023~0.155 | 4.0 | ~2.3h |
| **m16_seed44_v3** | cqa1:0 | 42950/100K | 0.059~0.082 | 4.0 | ~4.0h |

## Eval 就绪状态

`eval_smart_compress_libero.py` 就绪，参数确认：`--n_queries M --checkpoint_path ... --suite libero_object --num_episodes 500 --gpu 0 --seed S`。

Eval 命令模板已写入 `/root/autodl-tmp/importance_margin_vla_compress/eval_commands_ready.sh`，含 5 个 eval 任务（取消注释即可执行）。

## ANALYZING 实验（3 个待 eval + 1 个已完成）

| 实验 | 状态 | Checkpoint | 说明 |
|------|------|-----------|------|
| **m32_seed44** | ANALYZING, 待 eval | ✅ 存在 | 可立即在 cqa1:3 eval |
| **m64_seed44** | ANALYZING, 待 eval | ✅ 存在 | 排队 cqa1:3 |
| **m96_seed44** | ANALYZING, 待 eval | ✅ 存在 | 排队 cqa1:3 |
| **m128_resume** | ANALYZING, 有 metrics | — | 已有 train metrics，需确认是否还需 LIBERO eval |

## 建议操作

**cqa1:3 空闲 → 可立即启动 seed44 eval**（m32/m64/m96 串行，每个 500 episodes LIBERO-Object ≈ 1.5-2h）。是否现在启动 m32_seed44 的 eval？

---
