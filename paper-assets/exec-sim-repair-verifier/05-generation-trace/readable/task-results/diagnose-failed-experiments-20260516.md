# diagnose failed experiments 20260516

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_failed-experiments-20260516_20260516T001959_result.json`
- **Structured JSON:** [`17d06ff3a90ce14a975d.json`](../../sessions/17/17d06ff3a90ce14a975d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整报告。

---

## 诊断结果

### 1. cwm8b-ckpt400-test-eval — **已死，OOM killed**

| 项目 | 状态 |
|------|------|
| 进程 | 已死，EXIT_CODE=137 (SIGKILL/OOM) |
| 最后进度 | 5280/9784 (54.0%), running_acc=64.7% |
| 已保存结果 | `results_incremental.jsonl` = 5280 行 (18.6 MB) |
| 死亡时间 | ~08:12 (与训练几乎同时) |

**死因**：系统级 OOM。EXIT_CODE=137 是 Linux OOM killer 发的 SIGKILL，不是 CUDA OOM（CUDA OOM 会报 Python exception，不会直接 SIGKILL）。bs=8 + max_new_tokens=1024 生成时，系统 RAM 峰值过高。

**可以 auto-resume**：是。脚本有 `results_incremental.jsonl`，resume 后从第 5281 条继续，剩余 4504 条。

**建议**：降 bs 到 **4**（甚至 2），单独跑，不要和训练并行。两次 OOM 的根本原因都是多任务并发挤爆系统 RAM。

---

### 2. repo-level-cwm-8b-conda-v5 — **已死，被 OOM 连带杀死**（最关键）

| 项目 | 状态 |
|------|------|
| 进程 | 已死，无 EXIT_CODE 输出（被 SIGKILL） |
| 最后进度 | step 6198/6633 (93.4%) |
| 最新 checkpoint | **checkpoint-6100** (May 16 07:53) |
| 日志最后修改 | 08:13:21 |
| 进度丢失 | 98 steps (6100→6198) |

**死因**：与 cwm eval 同一次系统 OOM 事件连带被杀。关键证据：
- 训练在 step 6198 出现急剧减速 (12s/it → 18.2s/it)，典型内存压力表现
- 日志修改时间 08:13 与 eval 死亡时间 08:12 仅差 1 分钟
- 无 Python exception / CUDA error，进程被直接 SIGKILL

**checkpoint 状况**：
```
checkpoint-6100  (May 16 07:53)  ← 可从此 resume
checkpoint-6000  (May 16 07:13)
checkpoint-5900  (May 16 06:34)
checkpoint-5800  (May 16 05:54)
checkpoint-400   (May 14 16:32)
```

**可以 resume**：是。从 checkpoint-6100 resume，剩余 **533 steps**，按 ~12s/step 估算约 **1.8 小时**可完成。

**建议**：立即单独重启训练（不要并行跑 eval）。533 steps 优先完成。

---

### 3. cls8b-s42-ckpt3600-seq2048-ablation — **已正常完成**

| 项目 | 状态 |
|------|------|
| 进程 | 已完成退出 |
| 最终进度 | 9784/9784 (100%) |
| 结果文件 | `eval_repo_cls.json` + `eval_repo_cls_predictions.jsonl` |

**结果**：
- **Accuracy: 83.04%** (majority baseline 73.0%, +10.1pp)
- F1 macro: 76.80%
- F1 fail: 64.8%, F1 pass: 88.8%
- Unparseable: 136 条

reconcile 报 "miss" 是因为进程已正常退出，不是崩溃。这个实验不需要任何操作。

---

## 磁盘状态

| 分区 | 使用 | 剩余 |
|------|------|------|
| / (根) | 27G/30G (89%) | 3.4G ⚠️ 偏紧 |
| /root/autodl-tmp | 151G/250G (61%) | 100G ✓ |

---

## GPU 状态

4x 5090 全部空闲（3 MiB / 32607 MiB, 0% utilization）。

---

## 总结与优先级建议

1. **最高优先**：单独重启 CWM 8B 训练，从 checkpoint-6100 resume，533 steps ≈ 1.8h
2. **次优先**：训练完成后，重启 cwm eval，bs 降到 4，从 incremental 结果 auto-resume
3. **无需操作**：CLS ablation 已完成，收录结果即可
4. **根本原因**：三个任务同时跑 + bs=8 生成导致系统 RAM OOM，以后避免训练和大 bs 生成任务并行

---
