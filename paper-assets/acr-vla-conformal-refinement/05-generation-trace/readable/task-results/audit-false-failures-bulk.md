# audit false failures bulk

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_false-failures-bulk_20260524T031957_result.json`
- **Structured JSON:** [`a9f5ec428f898dbbf22b.json`](../../sessions/a9/a9f5ec428f898dbbf22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。汇总结果：

---

## 假失败审计报告

### 总览
| 类别 | 数量 |
|------|------|
| 审计总数 | 89 |
| **成功恢复** | **12** |
| 真失败 | 43 |
| 日志缺失/不可达 | 34 |

### 恢复的 12 个实验

**Eval 实验 (11):**

| exp_id | success_rate | successes/total |
|--------|-------------|-----------------|
| eval-supp-goal-vla-only-wrapper-s44 | 82.0% | 164/200 |
| eval-supp-spatial-k2mean-s46 | 80.0% | 160/200 |
| eval-supp-long-reconvla-s45 | 59.0% | 118/200 |
| eval-adaptive-k-spatial-p90-seed44-bjb2 | 36.0% | 36/100 |
| eval-random-selection-spatial-seed42 | 34.0% | 34/100 |
| eval-perdof-object-norm003-seed44 | 11.0% | 11/100 |
| eval-pi05-vla-only-long-seed42-r4 | 0.0% | 0/200 |
| eval-pi05-vla-only-object-seed44 | 0.0% | 0/200 |
| eval-pi05-vla-only-object-seed43 | 0.0% | 0/200 |
| eval-pi05-vla-only-object-seed42 | 0.0% | 0/200 |
| eval-obs-only-spatial-v2 | 0.0% | 0/100 |

**训练实验 (1):**

| exp_id | metrics |
|--------|---------|
| crm-train-pi05-spatial-full | 50/50 epochs, best val_loss=0.006138 |

### 日志缺失明细 (34)
- 26 个实验无有效 log_path（空路径、n/a、killed-on 标记）
- 3 个实验在已下线服务器（autodl-4090, autodl-4090x4）
- 5 个日志文件在服务器上已被删除

### 真失败原因分布 (43)
- 进程被 kill/timeout（EXIT_CODE=124/143）：~15 个
- "python not found"（环境未激活）：~8 个
- FileNotFoundError（数据/checkpoint 缺失）：~8 个
- size mismatch / 模型维度不匹配：~5 个
- BrokenPipeError / EOFError：~4 个
- ValueError（参数缺失）：~3 个

### 系统性问题确认

加上之前手动修正的 10 个，**总共 22 个实验被 cron 误判为 failed**。根因是 eval 脚本不写 W&B metrics 也不写 sentinel 文件，cron 的 "process dead 5× with no sentinel/W&B" 逻辑无法区分正常退出和异常退出。建议在 cron 监控中增加对 EXIT_CODE=0 的检测，或让 evaluate.py 写一个 sentinel 文件。

---
