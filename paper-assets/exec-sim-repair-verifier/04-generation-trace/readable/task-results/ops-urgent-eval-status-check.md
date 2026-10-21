# ops urgent eval status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-eval-status-check_20260518T230732_result.json`
- **Structured JSON:** [`0b2c06735e42b25d258a.json`](../../sessions/0b/0b2c06735e42b25d258a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全部 Eval 状态汇总

```
Qwen3-8B TRAJ best:       ❌ CRASHED (CUDA OOM) — GPU 0 现已空闲，无结果文件
Qwen3-8B TRAJ ckpt-98:    ✅ checkpoint 存在，未 eval
Qwen3-4B TRAJ best:       ✅ 已完成 — 72.92% variant acc (35/48), unparseable=0
CWM s42 best @4096 (GPU1): ⏳ 8831/9784 (90.3%) — running_acc=56.7%, ETA ~3h
CWM s123 @4096 (GPU 3):   ⏳ 8342/9784 (85.3%) — running_acc=61.9%, ETA ~5.5h
CWM s42 e3 @2048 (GPU 2): ⏳ 3049/9784 (31.2%) — running_acc=66.3%, ETA ~11h
CWM s42 e2 @2048 (Home):  ⏳ 4065/9784 (41.5%) — running_acc=66.7%, ETA ~12.7h
CWM s42 e2 @4096:         ⛔ STOPPED at 3050/9784 — was replaced by e3 @2048 eval
```

### 详细结果

**Qwen3-8B TRAJ best eval** — OOM 崩溃，原因是 GPU 0 当时被进程 772542 占用 27.72 GiB，模型加载时剩余显存不足。GPU 0 现在完全空闲 (0MiB)，可以重新启动。

**Qwen3-4B TRAJ best (已完成)**:
| 指标 | 值 |
|---|---|
| overall_accuracy | 72.92% |
| variant-level (35/48, AND rule) | 72.92% |
| F1 macro | 72.62 |
| fail recall (unresolved) | 68.18% |
| pass recall (resolved) | 76.92% |
| unparseable | 0 |

**CWM s42 epoch2 @4096 (已停止)** — 仅跑了 3050/9784 样本就被终止（21:50 May 18），紧接着 21:51 启动了 e3 @2048 eval。已处理部分: acc=66.9%，但 **unparseable 率 65.5%** (1997/3050)，极高。

**GPU 1 上实际运行的是 CWM s42 `best` checkpoint @4096**（不是 epoch 2）。`checkpoints_deepseek_cwm_repo/` 下有 3 个 checkpoint：`best`、`checkpoint-8844`（e2）、`checkpoint-13266`（e3）。running_acc 仅 56.7%，显著低于其他 seed/epoch。

### 建议

1. **Qwen3-8B TRAJ best**: GPU 0 空闲，可立即重启 eval（加 `CUDA_VISIBLE_DEVICES=0`）
2. **Qwen3-8B TRAJ ckpt-98**: 也可在 GPU 0 排队 eval
3. **CWM s42 e2 @4096 的 65.5% unparseable 率** 需要排查——可能是 seq_length=4096 + epoch2 checkpoint 的解码异常

---
