# diagnose cqa1 xvla failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1-xvla-failures_20260521T091921_result.json`
- **Structured JSON:** [`070ea548e63edf82ff1a.json`](../../sessions/07/070ea548e63edf82ff1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。两个实验实际上都**成功完成了**，不需要重跑。

## 诊断结果

### 1. eval_xvla_l2norm_k05_object_seed42 — 已完成
- 启动: 15:27:19, 完成: 17:09:17 (101.7 min)
- **结果: 43.4% (217/500)**, 95% CI [39.1%, 47.8%]
- Per-task: 56%, 2%, 76%, 70%, 42%, 56%, 2%, 44%, 16%, 70%

### 2. eval_xvla_random_k05_object_seed44 — 已完成
- 启动: 15:58:59, 完成: 17:17:05 (77.8 min)
- **结果: 69.2% (346/500)**, 95% CI [65.0%, 73.1%]
- Per-task: 100%, 30%, 100%, 88%, 98%, 62%, 4%, 80%, 32%, 98%

### 失败根因：不是实验失败，是监控误判
两个实验今天下午都正常跑完了。监控系统报"进程死亡"可能是因为这些 eval 脚本**不上报 W&B 也不写 sentinel 文件**，导致 cron 检查时判定为失败。

### 结果文件覆盖问题
两个实验都写入同一文件 `xvla_prune_k0.5_libero_object.json`（脚本不带 mode/seed 后缀）。random_k05_seed44 后完成，覆盖了 l2norm 的结果。当前 JSON 里是 random seed44 的数据。**l2norm k=0.5 seed42 的结果只存在于日志文件中**，需要手动提取或修复脚本重新保存。

### GPU 使用情况
| GPU | 状态 | 占用 |
|-----|------|------|
| 0 | **空闲** | 1MiB |
| 1 | **空闲** | 1MiB |
| 2 | 运行中 | 4539MiB — `eval_xvla_l2norm_k03_object_seed42` (PID 707317) |
| 3 | **空闲** | 1MiB |

### 建议行动
1. 从日志文件提取 l2norm k=0.5 seed42 的结果，保存为独立 JSON（如 `xvla_l2_norm_k0.5_libero_object_seed42.json`）
2. 检查 eval 脚本的输出文件命名逻辑，加上 mode 和 seed 后缀防止再次覆盖
3. 3 张空闲 GPU (0/1/3) 可安排新任务

---
