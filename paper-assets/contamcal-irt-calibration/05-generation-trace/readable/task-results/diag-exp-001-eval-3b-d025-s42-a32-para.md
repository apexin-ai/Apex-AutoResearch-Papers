# diag exp 001 eval 3B d025 s42 a32 para

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_001_eval_3B_d025_s42_a32_para_20260516T043455_result.json`
- **Structured JSON:** [`1ffa43bb445829f4c50e.json`](../../sessions/1f/1ffa43bb445829f4c50e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 进程状态：已正常结束

PID 691033 已退出。**不是异常死亡，是正常完成。**

### 日志最后输出

Eval 四个 benchmark 全部跑完，最后记录时间 `12:27:21`：

| Benchmark | 结果 |
|-----------|------|
| mmlu (paraphrased) | 6596 items 评估完成 |
| gsm8k (paraphrased) | 评估完成（日志中段，被截断） |
| arc_challenge (paraphrased) | **0.8106** (565/697) |
| humaneval (paraphrased) | **0.0000** (0/26) |

日志末尾确认写出了所有产出文件和 sentinel。

### eval 输出目录（完整）

```
/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned/
  .done                   (sentinel)
  correctness_matrix.json (47 KB)
  eval_results.json       (909 KB)
  item_responses.json     (1019 KB)
```

### 为什么 reconcile 报 "no sentinel"

sentinel `.done` 写在了 **eval 输出目录** (`/root/autodl-tmp/exp001/eval_results/.../.done`)，但 reconcile 检查的是 `/root/runs/contamcal-irt-calibration/*d025*sentinel*`——该路径下确实没有 sentinel 文件。这是 sentinel 路径不匹配导致的误报。

### cuda:0 GPU 状态

`3895 MiB / 24564 MiB, 44% util` — 这是 1.5B signals 进程（PID 691872）占用的。eval 进程已退出释放显存。cuda:0 剩余 ~20 GB 空闲。

### 1.5B signals 进程

PID 691872 **存活**，正常运行中（`CUDA_VISIBLE_DEVICES=0`）。

### 总结

- eval 任务**已成功完成**，产出齐全
- reconcile 误报原因：sentinel 写入位置与监控检查路径不一致
- cuda:0 当前被 1.5B signals 占用，eval 无需重提交
- 建议修复 reconcile 的 sentinel 检测路径，或让 eval 脚本同时在 runs 目录写一份 sentinel

---
