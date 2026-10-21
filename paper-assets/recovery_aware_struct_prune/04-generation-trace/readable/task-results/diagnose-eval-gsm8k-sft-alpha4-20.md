# diagnose eval gsm8k sft alpha4 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_sft_alpha4_20_20260521T222526_result.json`
- **Structured JSON:** [`fa91ac3d9cac3d34a62c.json`](../../sessions/fa/fa91ac3d9cac3d34a62c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败根因：外部 SIGTERM（非 OOM / 非内部错误）

日志中**无任何 error / exception / traceback / OOM**。进程被外部 SIGTERM (EXIT_CODE=143) 干净地终止。

**时间线**：
| 时间 | 事件 |
|------|------|
| 05:42:02 | 日志文件创建（由 wrapper/launcher 创建） |
| 06:23:54 | Python 进程开始执行（41 分钟空白，推测 wrapper 在做前置准备或排队等待） |
| 06:25:16 | 模型加载到 cuda:0 |
| 06:25:16–06:25:55 | 评估进行中，完成 21/1319 样本（~2.5s/it） |
| ~06:26:02 | 进程被 SIGTERM 杀掉 |

### 部分结果

**无可用结果**。仅完成 21/1319（1.6%），第一个 interim accuracy checkpoint 在 50 样本，未到达。无输出目录、无 JSON 产出。

### 关联发现：GRPO eval 也失败了

兄弟实验 `eval_gsm8k_grpo_alpha4_20` 以 **EXIT_CODE=124（timeout）** 结束：
- 运行 ~2 小时后被 `timeout` 命令杀掉
- 进度：774/1319（59%）
- **interim accuracy at 750 samples：0.6293**（eos_rate=98.27%，avg_len=225）
- 在 sample 756 附近出现 ~6 分钟卡顿（单个样本生成时间暴涨，可能是长 thinking chain）

### SIGTERM 可能来源

1. **Pipeline 整体超时** — 上层 pipeline 脚本的总时限到期，级联 kill 所有子进程
2. **Job monitor / cron 杀掉** — 作业管理系统超时清理
3. **手动 kill**

考虑到 SFT eval 仅运行 44 分钟就被杀（远未到 2h timeout），最可能是 **pipeline 级别的整体超时**导致级联终止。

### 重跑建议

1. **SFT eval 单独跑**（不要放在 pipeline 里），预估耗时 ~30 分钟（21 样本用了 27 秒，~1.3s/it，1319 × 1.3s ≈ 29 分钟）。`timeout 1h` 足够。
2. **GRPO eval 需要更长 timeout**（至少 3h）或者限制 `--max_new_tokens` 防止 runaway generation（sample 756 单个样本生成了 ~6 分钟）。
3. 两个 eval 可以分别挂到不同 GPU 并行跑（cuda:0 + cuda:1），互不干扰。

---
