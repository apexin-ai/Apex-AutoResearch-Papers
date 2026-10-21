# fix val sweep seq8192 restart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_val-sweep-seq8192-restart_20260515T165720_result.json`
- **Structured JSON:** [`97a4a4a95226eeb28de0.json`](../../sessions/97/97a4a4a95226eeb28de0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。报告：

---

### 执行报告

| 步骤 | 状态 |
|------|------|
| **Kill 旧 sweep** | pid 388791 + 子进程 391710 已 kill，cuda:0 已释放 (0 MiB / 32110 MiB free) |
| **脚本修改** | 添加 `--max_seq_length 8192`、`--batch_size 8`、`--max_new_tokens 8` |
| **清理无效结果** | 删除 `cls_8b_s42_resume_val/1800/`（seq2048, 1883 unparseable） |
| **重启 sweep** | PID 393945，子进程 393951 已确认参数正确 |
| **验证** | 日志显示 ckpt-1800 加载中，val instances=9335，cmdline 含 `--max_seq_length 8192` ✓ |
| **Registry** | 旧实验标记 DONE/failed，新实验 `cls8b-s42-resume-val-sweep-seq8192` 状态 RUNNING |

21 个 checkpoint (1800→5800) 在 cuda:0 上运行，日志路径 `~/runs/exec-sim-repair-verifier/cls8b-s42-resume-val-sweep-seq8192.log`。

---
