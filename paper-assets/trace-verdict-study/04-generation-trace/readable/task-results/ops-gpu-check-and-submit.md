# ops gpu check and submit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_and_submit_20260520T172026_result.json`
- **Structured JSON:** [`8b721d7e5e7c69dffd42.json`](../../sessions/8b/8b721d7e5e7c69dffd42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个新实验都**立即失败**了 — `label_only` 不是 `train_sft.py` 的合法 condition。

train_sft.py 接受的 condition 列表：
```
no_trace, vota, full_trace, vota_no_ae, ae_only, exception_only,
exception_only_nomarker, loop_only, debugbench_no_trace, debugbench_vota,
debugbench_full_trace, debugbench_ae_only, debugbench_exception_only,
full_trace_tail, full_trace_tail_512, full_trace_tail_256,
full_trace_tail_1024, full_trace_tail_384, full_trace_head
```

`label_only` 不在其中。需要确认正确的 condition 名称后重新提交。

---

## 已完成实验汇总

| 实验 | GPU | accuracy | baseline | lift | fail F1 |
|------|-----|----------|----------|------|---------|
| qwen15b_ae_only_seed123 | cuda:1 | **98.57%** | 71.5% | +27.1pp | 0.975 |
| deepseek_loop_only_seed456 | cuda:0 | **78.4%** | 71.5% | +6.9pp | 0.63 |

两个 GPU 当前空闲，等待你确认 `label_only` 对应的正确 condition 名称。

---
