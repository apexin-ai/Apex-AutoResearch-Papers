# ops check westd38929 batch completion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd38929-batch-completion_20260520T232030_result.json`
- **Structured JSON:** [`07a7d7fbac128b69a00e.json`](../../sessions/07/07a7d7fbac128b69a00e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 experiments marked DONE/failed in registry.

## 汇总

### 全部 4 个实验状态：全部 FAILED

| GPU | exp_id | 状态 | 崩溃点 | 部分结果 | Metadata 验证 |
|-----|--------|------|--------|----------|--------------|
| 0 | random k=0.95 seed42 | CRASHED | Task 4/10 | T1=80%, T2=42%, T3=70% | `k=0.95, 256→243 tokens` ✓ |
| 1 | random k=0.7 seed42 | CRASHED | Task 3 Ep40/50 | T1=72%, T2=20%, T3=partial | `k=0.7, 256→179 tokens` ✓ |
| 2 | random k=0.3 seed43 | DIED SILENTLY | Task 3 Ep30/50 | T1=18%, T2=2%, T3=partial | `k=0.3, 256→76 tokens` ✓ |
| 3 | L2 k=0.9 seed43 | CRASHED (已由其他 Worker 标记) | Task 4/10 | T1=66%, T2=58%, T3=66% | `k=0.9, 256→230 tokens` ✓ |

### GPU 释放情况
- GPU 0, 1, 3：已释放（1 MiB）
- GPU 2：15.6 GB zombie memory（进程死了但显存未释放），需手动 kill 或重启清理

### 根因
M040 重启后 LIBERO 包的 `init_files/` 目录从 `/root/miniconda3/.../site-packages/libero/` 被删除。实际的 `.pruned_init` 文件存在于 `/root/autodl-tmp/LIBERO-plus/libero/libero/init_files/`。

### 修复方案
重新安装 LIBERO（`pip install -e /root/autodl-tmp/LIBERO-plus`）或创建符号链接，然后重跑全部 4 个实验。

---
