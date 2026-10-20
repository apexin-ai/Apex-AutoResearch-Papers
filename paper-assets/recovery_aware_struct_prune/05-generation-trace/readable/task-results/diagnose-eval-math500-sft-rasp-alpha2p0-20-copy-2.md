# diagnose eval math500 sft rasp alpha2p0 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_rasp_alpha2p0_20_20260522T201428_result.json`
- **Structured JSON:** [`7932a15422f1ca17e91c.json`](../../sessions/79/7932a15422f1ca17e91c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**结论：实验实际已成功完成，监控系统误判为失败。**

### 根因

eval 脚本正常跑完全部 500 题并保存了结果，但**未向 W&B 上报指标**。监控系统以 W&B metrics 作为成功信号，连续 5 次轮询均未检测到 W&B 数据，自动判定为失败。

这不是真正的进程崩溃，而是监控逻辑与 eval 脚本的集成缺口。

### 进度

- 开始时间：`2026-05-22 23:06:46`
- 结束时间：`2026-05-23 04:03:02`
- 耗时：约 4 小时 55 分钟
- 完成度：**500/500 (100%)**

### 结果

```
MATH-500 Accuracy: 0.2400 ± 0.0191 (120/500)
EOS Stats: natural_eos=345, truncated=155, avg_response_length=805.754
```

结果已保存到 `/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.json`。

### 是否需要重跑

**不需要重跑。** 数据完整，500 题全部跑完，结果文件已生成。只需要将 JSON 中的 accuracy 手动录入论文数据或补报到 W&B 即可。

### 后续建议

如果需要让监控系统正确识别此类 eval 的成功状态，eval 脚本末尾应增加 W&B metric 上报，或者监控系统应增加对 JSON 结果文件的 sentinel 检测。

---
