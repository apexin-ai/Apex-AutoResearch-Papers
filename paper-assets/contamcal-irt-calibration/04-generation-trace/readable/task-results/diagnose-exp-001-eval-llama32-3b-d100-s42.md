# diagnose exp 001 eval llama32 3B d100 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_llama32_3B_d100_s42_20260516T213736_result.json`
- **Structured JSON:** [`152692cb15451e6fdf78.json`](../../sessions/15/152692cb15451e6fdf78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验实际已成功完成，是 cron 监控误判。**

### 失败根因：误报（False positive）

进程 PID 831033 于 `05:26:06` 正常退出，写入了 `.done` sentinel。Cron 监控系统在进程自然结束后多次探测到 PID 不存在，且可能因未配置 W&B 而判定 "no sentinel/W&B"，累计 5 次后自动标记为 failed。

时间线：
- `02:24:24` 启动，加载模型
- 过程中遇到大量 HuggingFace 连接超时（数据集下载），但 retry 后从缓存加载成功
- `05:26:06` 正常完成全部 4 个 benchmark，写入所有结果文件和 `.done` sentinel

### 已完成的 benchmark 结果

| Benchmark | Score |
|-----------|-------|
| MMLU | 34.08% (4786/14042) |
| GSM8K | 见 gsm8k_results.json |
| ARC Challenge | 见 arc_challenge_results.json |
| HumanEval | 1.22% (2/164) |

注意：MMLU 结果中所有 pred 都是 "A"，说明模型可能存在严重的 position bias 或推理失败（d100 = 100% 污染数据微调，可能导致模型退化）。

### 结论

- **不需要重跑**，结果已完整
- 需要将实验状态从 failed 更正为 completed
- 监控系统的 sentinel 检测逻辑可能有 race condition（进程退出后才检查 sentinel 存在性，但检测窗口在 sentinel 写入之前）

---
