# analysis 3B signal readiness check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3B-signal-readiness-check_20260515T135440_result.json`
- **Structured JSON:** [`19bc908bd00b80aef151.json`](../../sessions/19/19bc908bd00b80aef151.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `memory.md`。以下是核心摘要：

---

## 3B 信号管线就绪状态

**3B 信号: 0/24 完成** (需要 4 dose × 2 seed × 3 benchmark)

### 完成矩阵

| Dose | Seed | Aligned | Para | 可跑信号? |
|------|------|---------|------|----------|
| d000 | s42 | ✅ | ✅ | ✅ 就绪 |
| d000 | s123 | ✅ | ✅ | ✅ 就绪 |
| d005 | s42 | 🔄 cuda:5 | ✅ | ❌ 等 aligned |
| d005 | s123 | ❌ SFT cuda:2 | ❌ | ❌ 阻塞 |
| d025 | s42 | ✅ | ✅ | ✅ 就绪 |
| d025 | s123 | ❌ SFT cuda:4 | ❌ | ❌ 阻塞 |
| d100 | s42 | ✅ | ✅ | ✅ 就绪 |
| d100 | s123 | ✅ | **❌ 缺失** | ❌ 等 para |

### 缺失项 (按优先级)

1. **P0 — d100 s123 para eval** — checkpoint 就绪，可立即跑，需空闲 GPU
2. **P1 — d005 s42 aligned** — 运行中(cuda:5)，等待完成
3. **P2 — d005/d025 s123 链** — SFT 仍在跑(cuda:2/4)，完成后需链式执行 aligned→para eval

### 两个关键脚本问题 (必须在信号计算前修复)

1. **Eval 目录命名不匹配** — 信号脚本期望 `Qwen2.5-3B_d{X}_s{Y}/`，实际目录有 `_aligned`、`_v2_aligned` 后缀。**必须创建 symlinks**
2. **`run_batch.py` 硬编码** — DOSAGES 缺 d025，SEED 只有 s42。推荐用 `run_exp002.sh` 替代

### 最优执行顺序

1. **现在**: 等 GPU 3 释放 → 立即跑 d100 s123 para eval
2. **现在**: 对已就绪的 4 组 (d000×2seed + d025 s42 + d100 s42) 创建 symlinks → 先跑部分信号
3. **SFT 完成后**: 链式执行 d005/d025 s123 的 eval → para → symlink → 信号
4. **全部 eval 完成后**: 全量信号计算 (~4-8h) → RRF 聚合

完整命令模板已写入 `memory.md`。

---
