# exec diagnose fix restart collection

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_diagnose-fix-restart-collection_20260512T163343_result.json`
- **Structured JSON:** [`3892f494e44316d53454.json`](../../sessions/38/3892f494e44316d53454.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. 诊断结论

**根因**：多进程 GPU 冲突，非脚本 bug。
- ICL 测试（14b-AWQ, cuda:0）和轨迹收集（Qwen3-8B, cuda:1）同时运行，系统 OOM killer 杀掉了两个进程
- ICL 日志明确显示 `Killed` 信号
- 收集脚本缺少 try-except，后续调试中反复出现残留进程在同一 GPU 上堆叠（每个 ~7.7GB），导致 `torch.OutOfMemoryError`

### 2. 脚本修复（`src/collect_trajectories.py`）

| 修改 | 作用 |
|------|------|
| `import gc, sys, faulthandler` | 支持内存回收和段错误捕获 |
| `faulthandler.enable()` | 捕获 C 层面 crash 的调用栈 |
| try-except 包裹每个 episode | 单任务崩溃不影响后续收集 |
| `gc.collect()` + `torch.cuda.empty_cache()` | 每个 episode 后释放 GPU 显存 |

### 3. 双卡重启状态

| GPU | PID | 实验 ID | 进度 | 显存 |
|-----|-----|---------|------|------|
| 0 | 263368 | datagen_traj_v5_cuda0 | 1/250 ✓ | 7.7GB |
| 1 | 263025 | datagen_traj_v5_cuda1 | 2/250 ✓ | 7.7GB |

两进程均已通过首条轨迹验证，持续稳定。每条 ~80s，250 条 ETA ~5.5h。

### 4. ICL 14b-AWQ 测试结果（25 tasks, dev set）

| Task Type | 成功/总数 | 成功率 |
|-----------|-----------|--------|
| pick_and_place | 6/6 | **100%** |
| look_at_obj | 4/5 | **80%** |
| pick_two_obj | 0/5 | 0% |
| pick_clean_then_place | 0/4 | 0% |
| pick_heat_then_place | 0/2 | 0% |
| pick_cool_then_place | 0/3 | 0% |
| **Overall** | **10/25** | **40%** |

模型仅在 pick_and_place 和 look_at_obj 上表现好，其余 4 种任务类型全部 0%。50-task 测试在第 7 个被 OOM kill（当时 5/7 = 71%，但因为前 7 个偏向简单类型）。完整 50-task 需要重跑。

---
