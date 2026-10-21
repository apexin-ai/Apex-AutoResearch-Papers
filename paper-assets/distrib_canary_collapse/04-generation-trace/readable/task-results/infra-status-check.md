# infra status check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status-check_20260514T061947_result.json`
- **Structured JSON:** [`71d67eb8fcf5d07a1be9.json`](../../sessions/71/71d67eb8fcf5d07a1be9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 状态总结

| 实验 | 状态 | 说明 |
|------|------|------|
| **mvp_v2_rep42** (PID 5286→5291) | **HUNG（挂起）** | 日志最后更新 14:03，停在 Gen 0 保存数据集后，20 分钟无任何输出 |
| **mvp_v2_rep43** (PID 5364→5369) | **HUNG（挂起）** | 同上 |

### 根本原因

**输出目录冲突**：服务器上有一组更早启动的 v1 实验仍在运行：

| 旧实验 | PID | 运行时间 | 参数差异 |
|--------|-----|----------|----------|
| `mvp_rep42` | 3878→3883 | 47 min | `data/wikitext103`, `steps_per_gen=10000` |
| `mvp_rep43` | 3956→3961 | 47 min | `data/wikitext103`, `steps_per_gen=10000` |

v1 和 v2 **写入同一个输出目录** (`results/mvp/rep_42` 和 `results/mvp/rep_43`)，导致 v2 进程在训练阶段被阻塞。

v1 实验当前是活跃的（日志刚刚更新到 14:22:48，正在做 "Featurizing q" 59%），而 v2 已死锁。

### GPU 状态
- 两张卡各被 2 个 Python 进程占用（v1 + v2 各 12GB），GPU 利用率 0%（当前阶段为 CPU 密集的特征化操作）

### 建议操作
需要 kill 其中一组：
- 如果 v2 是目标实验 → kill v1 (PIDs 3878, 3883, 3956, 3961)，然后重启 v2
- 如果 v1 是目标实验 → kill v2 (PIDs 5286, 5291, 5364, 5369)

---
