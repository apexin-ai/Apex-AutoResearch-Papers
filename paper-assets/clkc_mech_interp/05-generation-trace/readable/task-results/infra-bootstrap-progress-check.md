# infra bootstrap progress check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_bootstrap-progress-check_20260523T045652_result.json`
- **Structured JSON:** [`3174c4c0276ce94b78c7.json`](../../sessions/31/3174c4c0276ce94b78c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### DE bootstrap v2 (PID 550508)
- **状态**: 运行中（python 进程，5 线程，VmRSS ~2.1GB）
- **启动时间**: 12:49（约 10 分钟前）
- **当前阶段**: `[EN->EN] Bootstrap` — 第 1/4 phase，日志无 Parallel 进度输出，说明 joblib 尚未返回首批 completed tasks
- **已完成 seeds**: 0（尚在首 phase 计算中）
- **输出文件**: 不存在
- **参考**: 此前 llama n2000 / 32 workers 每 phase 约 120 min；v2 用 64 workers，但系统严重过载，预计每 phase 60-120 min
- **预估总时间**: ~4-8 小时（4 phases）

### Gemma XNLI bootstrap (PID 549893)
- **状态**: 运行中（bash 壳进程，子 python 通过 nohup 启动）
- **启动时间**: 12:44（约 15 分钟前）
- **当前阶段**: `[EN->EN] Bootstrap` — 第 1/4 phase，同样无进度输出
- **已完成 seeds**: 0
- **输出文件**: 不存在
- **参数**: 32 workers, 42 layers（比 llama 多 10 层）
- **预估总时间**: ~8-10 小时

### 系统负载
- **Load avg**: 860 / 746 / 699（1/5/15 min）
- **CPU 数**: 208
- **严重过载**: load 是 CPU 数的 ~4 倍。两个 bootstrap 加起来只有 96 workers，负载 860 说明还有大量其他进程在抢 CPU，会显著拖慢两个 bootstrap。

---
