# ops cqa1 eval investigation

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_eval_investigation_20260520T012030_result.json`
- **Structured JSON:** [`0fc6d49068576e6d3fd6.json`](../../sessions/0f/0fc6d49068576e6d3fd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查结果汇总：

## 1. PID 994858 状态

**仍在运行**，但确实被重启过。证据：

- 当前进程启动时间：`08:12:51`（比另外两个 eval 晚 ~1h13m）
- 日志文件 Birth 时间：`08:12:52`（全新文件，非追加）
- 另外两个 eval（m128_seed43, m16_seed43）都是 `06:59` 启动的

推测：存在一个更早的 eval_m16_seed44 进程（不同 PID），跑到 ~415/500 时崩溃或被 kill，随后被重新启动为当前 PID 994858。**前一次运行的日志被覆盖，结果丢失。** dmesg 无 OOM 记录，bash_history 无手动 kill 记录，具体原因不明。

## 2. eval_m16_seed44 结果文件

**不存在。** `eval_results/eval_smart_compress_m16_seed44.json` 尚未生成。前一次运行未完成就终止了，当前是从头开始的新运行。

## 3. GPU 分配

| GPU | PID | Eval |
|-----|---------|------|
| 0 | 994858 | m16_seed44 |
| 1 | 818806 | m128_seed43 |
| 2 | 819552 | m16_seed43 |

## 4. 三个 eval 当前精确进度

| Eval | Task 进度 | 当前 Episode | 已完成 Task SR |
|------|-----------|-------------|---------------|
| **m16_seed44** | Task 1/10 | ep 143/500 | Task 0: 38.0% |
| **m128_seed43** | Task 2/10 | ep 350/500 | Task 0: 64.6%, Task 1: 32.2% |
| **m16_seed43** | Task 2/10 | ep 334/500 | Task 0: 42.8%, Task 1: 47.4% |

## 5. 预估剩余时间

- **m16_seed44**：刚完成 Task 0 + Task 1 的 143/500，还有 ~8.7 个 task 要跑。按 ~55min/task 估算，还需 **~8h**
- **m128_seed43**：Task 2 进行到 350/500，还有 ~7.3 个 task，还需 **~6.5h**
- **m16_seed43**：Task 2 进行到 334/500，还有 ~7.3 个 task，还需 **~6.5h**

m16_seed44 因重启损失了约 4-5 小时进度，预计比其他两个晚 ~1.5h 完成。

---
