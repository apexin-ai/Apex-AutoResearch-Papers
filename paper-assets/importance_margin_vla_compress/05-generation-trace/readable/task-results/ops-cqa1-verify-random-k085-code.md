# ops cqa1 verify random k085 code

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-verify-random-k085-code_20260521T042120_result.json`
- **Structured JSON:** [`9d7d6ea4527bd4e159d7.json`](../../sessions/9d/9d7d6ea4527bd4e159d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：PID 522841 用的是**修复后的代码**，结果有效，无需重跑。

**证据链：**

| 事件 | 时间 (CST +0800) |
|---|---|
| 脚本 D124 修复 (last modify) | 2026-05-21 **10:23:51** |
| 日志创建 (进程启动) | 2026-05-21 **10:30:23** |

进程在修复后 **~7 分钟**启动。

**日志确认：**
- 第1行明确打印 `Vision pruning installed: keep_ratio=0.85, mode=random`
- 当前脚本第103-105行有 `elif mode == "random": torch.randperm(N)` 分支
- 脚本第76行有 `--mode` 参数（D124 新增）

**运行结果：**
- 已完成，`EXIT_CODE=0`
- Overall SR: **318/500 (63.6%)**，95% Wilson CI: [59.3%, 67.7%]
- 耗时 81.4 min

不需要 kill 或重跑。63.6% 就是 X-VLA random k=0.85 的真实表现。

---
