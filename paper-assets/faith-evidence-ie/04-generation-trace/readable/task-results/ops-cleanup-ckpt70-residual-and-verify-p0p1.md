# ops cleanup ckpt70 residual and verify p0p1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-ckpt70-residual-and-verify-p0p1_20260514T200102_result.json`
- **Structured JSON:** [`644d1661ff00683ea8c4.json`](../../sessions/64/644d1661ff00683ea8c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

---

### 任务 1: ckpt-70/80 清理

- `checkpoint-70/` 和 `checkpoint-80/` 都是空目录（无 predictions.json、无 metrics.json）
- 已删除两个空目录，不会干扰 multi eval `--resume`

### 任务 2: P0+P1 启动状态 — **启动失败**

`mvp2_grpo_ced_lr5e6_rp_r1.log` 内容仅有 bash 语法错误：
```
bash: -c: line 1: unexpected EOF while looking for matching `"'
bash: -c: line 2: syntax error: unexpected end of file
EXIT_CODE=2
```
**启动脚本引号不匹配，P0+P1 训练从未开始。cuda:3 空闲。**

当前 GPU 占用：

| GPU | 显存 | 进程 |
|-----|------|------|
| 0 | 13645/32607 MiB | PID 90085 — `grpo_trainer` **无** `--ced_recall_penalty`，output_dir=`grpo_ced_lr5e6`，step 11/200，~110s/step |
| 1 | 0 MiB | 空闲 |
| 2 | 10297/32607 MiB | PID 85997 — eval inference checkpoint-20 |
| 3 | 0 MiB | 空闲 |

tmux session `mvp2_grpo_ced_lr5e6_r1` 运行的是 cuda:0 上的 CED lr5e6 训练（无 recall penalty），不是 P0+P1。

另外注意：cuda:0 训练在 step 5 报了 KL divergence = 2,412,554,396.9（阈值 100.0），极端异常。

---
