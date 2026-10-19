# research snr data coverage deep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_snr_data_coverage_deep_20260520T035611_result.json`
- **Structured JSON:** [`230d3419d8e4142ab894.json`](../../sessions/23/230d3419d8e4142ab894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部确认。汇总：

```
SNR 数据覆盖: 0-300 only
  - snr_extended_results.json: steps [0, 50, 100, 150, 200, 250, 300]，各 7 个 snapshot
  - gradient_snr_results.json: 单点（最终 step）的 per-layer SNR，无 trajectory
  - gradient_snr_constrained_results.json: 同上

现有训练 log 中 SNR 数据: 无
  - kl_sparsity30_s42.log: 无 SNR/grad_norm 字段
  - steps_curve_s42.log: 跑了 1000 步但只记录 loss/sparsity/lambda/tau，无 SNR
  - wandb 是 offline 模式，未 log SNR metric

建议: 需要重跑 SNR script 到 step 1000
  - 修改 gradient_snr_extended.py:
    - num_steps: 300 → 1000
    - SNAPSHOT_STEPS: 扩展到 [0, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000]
  - 预估时间: 300 步 KL phase 用了 641s，线性外推 1000 步约 2137s (~36min)；BCE 类似 ~18min；总计约 55-60 分钟
  - 资源: cuda:0 on westd-34887（服务器空闲）
```

---
