# ssh dead pid investigation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dead-pid-investigation_20260519T182916_result.json`
- **Structured JSON:** [`6cfa3a0ecbcee82da017.json`](../../sessions/6c/6cfa3a0ecbcee82da017.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕。汇总如下：

---

## 实验结果

### 1. deepseek-cls-repo-v5 (pid=698033) — **SUCCESS** ✓
- 训练完成 3 epochs (6315/6315), `EXIT_CODE=0`
- `train_loss=0.040`, `eval_loss`: epoch1=0.089, epoch2=0.159, epoch3=0.198
- Best checkpoint saved → `best/` 目录 (May 19 04:33)
- 下游 eval 已完成 (两个 checkpoint 都跑完了):
  - **ckpt-2105 (epoch 1)**: acc=82.61%, F1_macro=75.07%, fail_recall=51.0%
  - **ckpt-6315 (epoch 3)**: acc=82.51%, F1_macro=71.76%, fail_recall=38.5%
- **Registry**: 已标记 DONE/success，无需更新

### 2. deepseek-cwm-repo-s123 (pid=668680) — **FAILED** (训练未完成，eval 已跑完)
- 训练在 step 10045/13266 (76%) 被杀，`EXIT_CODE=129` (SIGHUP)
  - 注：registry 记录的是首次死亡 step 9489，pid=668680 是重启后的进程，多跑了 ~556 步后再次被杀
- Eval 在 checkpoint-8844 (epoch 2) 上完成:
  - **acc=61.9%** (低于 majority baseline 73.0%, gap=-11.1pp)
  - F1_macro=51.5%, **unparseable=65.5%** (6411/9784)
  - f1_fail=29.0%, f1_pass=74.0%
- **Registry**: 已标记 DONE/failed 且有 metrics。建议补充 note：resumed pid=668680 在 step 10045 再次 SIGHUP 死亡

### 3. D131-cwm-s42-epoch3-seq2048 (pid=734440) — **FAILED** (eval 未完成)
- 使用 checkpoint-13266 (s42 epoch 3 final), seq_length=2048
- Eval 停在 **4794/9784 (49%)**, running_acc=65.7%
- `results_incremental.jsonl` 有 4794 行 (partial)
- **Registry**: status=PREPARING, conclusion=failed。建议更新：
  - `status: DONE`
  - 添加 partial metrics: `{coverage: "4794/9784 (49%)", running_acc: 65.7, incomplete: true}`

### 4. D133-cwm-s42-e2-seq2048-home — **已 KILLED** (不可访问，无需检查)
- Registry 已标记 conclusion=failed, resume 被 Director 批准 kill（"seq2048 不入论文"）
- 无需操作

---

## 建议的 Registry 更新

| 实验 | 当前状态 | 建议更新 |
|------|---------|---------|
| deepseek-cls-repo-v5 | DONE/success | 无需更新 |
| deepseek-cwm-repo-s123 | DONE/failed | 补充 note: "重启 pid=668680 在 step 10045 再次 SIGHUP" |
| D131-cwm-s42-epoch3-seq2048 | PREPARING/failed | → DONE/failed, 添加 partial metrics |
| D133 系列 | DONE/failed + killed | 无需更新 |

需要我执行 registry 更新吗？

---
