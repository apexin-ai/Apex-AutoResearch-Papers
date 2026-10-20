# diagnose eval qwen14b arc s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_qwen14b_arc_s42_20260520T184128_result.json`
- **Structured JSON:** [`529dd479b074f2cec8d5.json`](../../sessions/52/529dd479b074f2cec8d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 失败原因：误报（实验实际成功完成）

日志 `/root/contamcal-irt-calibration/logs/eval_qwen14b_arc_s42.log` 存在且记录了**完整成功执行**：
- 从 d000_s42 开始，逐 dosage 评测，最终以 d100_s42 结束
- 最后一条：`arc_challenge accuracy: 0.8848 (1037/1172)`，结果保存到 `d100_s42/`
- 末尾写入了 sentinel `ALL_ARC_EVAL_DONE_QWEN14B_S42`

实验跟踪系统报 "PREPARING 阶段失败" 的原因：该实验无 spec、无 hypothesis，从未正式注册到跟踪系统。监控系统在早期检查时找不到 sentinel/W&B run，5 次探测后自动标记为 failed。**但底层进程实际正常跑完了。**

### 2. Qwen-14B ARC s42 数据：全部存在

所有 dosage 的结果文件齐全（每个目录含 `arc_challenge_results.json`, `eval_results.json`, `correctness_matrix.json`, `item_responses.json`）：

| Dosage | 路径 |
|--------|------|
| d000_s42 | `results/arc_eval/qwen14b/d000_s42/` |
| d005_s42 | `results/arc_eval/qwen14b/d005_s42/` |
| d025_s42 | `results/arc_eval/qwen14b/d025_s42/` |
| d050_s42 | `results/arc_eval/qwen14b/d050_s42/` |
| d100_s42 | `results/arc_eval/qwen14b/d100_s42/` |

s123 种子的全部 dosage 也已完成。

### 3. 是否需要重跑

**不需要。** 数据完整，无需任何操作。实验跟踪状态可以直接标记为 completed。

### 附：westd GPU 状态
- cuda:0, cuda:2 — 空闲
- cuda:1 — 95GB 占用（PID 406532）
- cuda:3 — 66GB 占用（PID 376641）

---
