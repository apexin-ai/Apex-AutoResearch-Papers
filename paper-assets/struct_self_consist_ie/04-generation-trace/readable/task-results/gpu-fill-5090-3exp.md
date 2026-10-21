# gpu fill 5090 3exp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_fill_5090_3exp_20260521T101525_result.json`
- **Structured JSON:** [`6edf7d05158534001853.json`](../../sessions/6e/6edf7d05158534001853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部占满：

| GPU | 显存占用 | 实验 |
|-----|---------|------|
| cuda:0 | 30280/32607 MiB (93%) | SciERC MF4v2 s42 — 推理中 (52% done) |
| cuda:1 | 16428/32607 MiB (50%) | FewNERD MF4v2 s42 — 模型加载中 |
| cuda:2 | 16428/32607 MiB (50%) | FewNERD MF4v2 s123 — 模型加载中 |
| cuda:3 | 30044/32607 MiB (92%) | E2 pretrained FewNERD（未动） |

**前置任务完成：**
- exp_scierc_mf4_v2_s123 → DONE(success), greedy_f1=0.6633
- exp_scierc_mf4_v2_s456 → DONE(success), greedy_f1=0.6631
- exp_fewnerd_mf4v2_s456 → DONE(success), greedy_f1=0.7889

**3 个实验已提交，registry 状态 RUNNING：**
- exp_scierc_mf4_v2_s42 @ cuda:0 — SciERC ~4min 剩余
- exp_fewnerd_mf4v2_s42 @ cuda:1 — FewNERD 模型加载中（修正路径为嵌套目录）
- exp_fewnerd_mf4v2_s123 @ cuda:2 — FewNERD 模型加载中

---
