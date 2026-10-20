# diagnose plan 006 qwen3 1 7b no evidence eval v2r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan_006_qwen3_1_7b_no_evidence_eval_v2r2_20260516T121942_result.json`
- **Structured JSON:** [`ff7fa446a150e0f2c65e.json`](../../sessions/ff/ff7fa446a150e0f2c65e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**根因：进程被 SIGKILL 终止（非 Python 异常），最可能是 CUDA driver fault 或 tmux 管道中断。**

关键证据：
| 项目 | 发现 |
|------|------|
| 日志 | 仅 11 行，停在 batch 15/247 (5:57)，无任何 error/traceback |
| 日志 mtime | 20:09:25（batch 15 时刻） |
| 进程死亡时间 | 20:18:10（891s from start） |
| 沉默时间 | log 停更后进程仍活了 **9 分钟** |
| 系统 RAM | 791GB 总量 / 723GB 可用 — 排除系统 OOM |
| GPU 0 当前 | 0MiB（进程已释放） |
| /var/log OOM | 无记录 |
| v3 状态 | GPU 1 正常运行，已到 batch 79/247，log 持续更新 |

**进程死亡模式**：log 在 batch 15 后停止写入（stdout 全缓冲未 flush），进程继续运行约到 batch 35-36 时被 SIGKILL。无 Python 层面错误说明杀死方式不经过异常处理。

**排除的原因**：
- ~~GPU OOM~~ — 1.7B bf16 (~3.4GB) 在 32GB 卡上余量极大
- ~~系统 OOM~~ — 723GB available
- ~~代码 bug~~ — v3 同代码/同模型/同数据在 GPU 1 正常运行
- ~~GPU 资源竞争~~ — plan_016 jobs 在 GPU 2/3，未占 GPU 0

**对 v3 的影响**：无。v3 在 GPU 1 独立运行，进度正常（~80/247），预计还需 ~80 分钟完成。

**修复建议**：不需要改代码。直接在 GPU 0 上重试即可（当前 0MiB 空闲）。如果再次失败，可加 `PYTHONUNBUFFERED=1` 捕获完整错误输出，或降 batch_size 到 2。

---
