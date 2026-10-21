# ops check exp status s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp-status-s44_20260515T003334_result.json`
- **Structured JSON:** [`bf5fe8196f2fef8c5063.json`](../../sessions/bf/bf5fe8196f2fef8c5063.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 任务 1: exp1-random-b03-s44 — 训练失败

- **PID 33167 已死亡**，GPU 1 完全空闲 (0MiB)
- **没有找到训练日志文件**（`/root/runs/solver-trace-ablation/` 下无 `*random*s44*` 匹配）
- Output 目录只有 `checkpoint-100` 和 `reward_log.jsonl`
- **reward_log.jsonl 最后一条是 step 102**（时间戳 2026-05-15T00:13:57），之后进程消失
- 训练在 **102/500 steps 时死亡**，没有完成

最后几步指标（step 96-102 区间）：
| step | prove_rate | isr_mean |
|------|-----------|----------|
| 96 | 1.000 | 0.500 |
| 100 | 0.875 | 0.096 |
| 102 | 0.875 | 0.301 |

**死因未知** — 没有 log 文件记录 stderr/traceback。可能是 OOM 或磁盘问题，但无法从现有信息确认。需要找到当初启动时的 nohup 输出文件来定位错误。

---

### 任务 2: exp1-isr-b03-s44-r2 eval — 进行中，接近完成

- **PID 50043 运行中**，GPU 0 占用 16320MiB，65% 利用率
- **进度: 90/100**（从 eval log 看）
- 输出文件尚未生成（写完所有 100 条后才会写 JSON）
- 预计几分钟内完成

观察到的 pattern：proved 样本 ISR 一致为 0.750，有少量 FAILED（如 folio_384, folio_831 ISR=0.000）。

---

**下一步建议**：
- 任务 1 需要重跑。建议先查明崩溃原因（`dmesg | grep -i oom` 或磁盘空间），然后在 GPU 1 上重新提交。
- 任务 2 再等 2-3 分钟应该就完成了，届时读取 `/root/autodl-tmp/outputs/exp1_isr_b03_s44_r2_eval/eval_results.json`。

---
