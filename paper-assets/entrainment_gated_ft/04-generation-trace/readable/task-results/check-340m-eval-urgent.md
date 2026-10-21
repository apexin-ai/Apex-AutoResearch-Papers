# check 340m eval urgent

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_340m-eval-urgent_20260522T002003_result.json`
- **Structured JSON:** [`5bd37acca269ac91189e.json`](../../sessions/5b/5bd37acca269ac91189e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## PID 状态
**已死亡** — PID 777365 不存在（ps 返回空）

## GPU 状态
- RTX PRO 6000 (96GB)：0% 利用率，0MiB 显存占用，无运行进程
- GPU 完全空闲

## 完成进度
**全部 15 个模型已完成**，每个模型均有 3 个 jsonl 文件（hellaswag / piqa / arc_easy）：

| 模型系列 | 变体 | jsonl 数 |
|---------|------|---------|
| GDN | pure, h3-1, h6-1, h12-1, h24-1 | 各 3 ✓ |
| RetNet | pure, h3-1, h6-1, h12-1, h24-1 | 各 3 ✓ |
| HGRN2 | pure, h3-1, h6-1, h12-1, h24-1 | 各 3 ✓ |

## 日志最后输出
```
HGRN2-h3-1 DONE

========================================
All complete. Evaluated: 15, Skipped: 0
Finish time: 2026-05-22 07:43:55
========================================
EXIT_CODE=0
```

## 判断
**全部完成，正常退出。** 15 个模型的 3 个 benchmark（hellaswag, piqa, arc_easy）均已评估完毕，进程以 exit code 0 正常结束于 07:43:55。GPU 已释放。

---
