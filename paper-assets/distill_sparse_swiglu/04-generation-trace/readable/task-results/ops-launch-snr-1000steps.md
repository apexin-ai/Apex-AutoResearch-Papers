# ops launch snr 1000steps

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch_snr_1000steps_20260520T035936_result.json`
- **Structured JSON:** [`930dc0e6552bad37615c.json`](../../sessions/93/930dc0e6552bad37615c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认运行正常。

**修改内容：**
- `num_steps`: 300 → 1000
- `SNAPSHOT_STEPS`: `[0,50,100,150,200,250,300]` → `[0,50,100,150,200,250,300,400,500,600,700,800,900,1000]`
- 输出路径: `snr_extended_results.json` → `snr_full_1000steps_results.json`
- summary key: `ratio_at_300` → `ratio_at_final`

**启动确认：**
- 设备: cuda:0 (westd-34887)
- PID: **175225**
- nohup 后台运行，日志: `/root/runs/distill_sparse_swiglu/snr_full_curve_1000steps.log`
- 模型加载完成，KL Phase 1 已开始（step 0 snapshot 已输出）

注意日志中打印的 `Phase 1: KL distillation (300 steps)` 是硬编码的 print 字符串，不影响实际运行步数（argparse default=1000 已生效，snapshot_steps 列表包含 1000）。

---
