# diag eval pi05 random k09 long seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_pi05_random_k09_long_seed42_postfix_20260524T144605_result.json`
- **Structured JSON:** [`eb67dde13c5ab068ff00.json`](../../sessions/eb/eb67dde13c5ab068ff00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验实际上成功完成了，cron 误报失败。**

### 根因：日志文件名不匹配

- Cron 监控的文件名：`logs/random_k09_long_seed42.log`（按 experiment id `eval_pi05_random_k09_long_seed42_postfix` 拼出来）
- 实际写入的文件名：`logs/random_k09_long.log`（缺 `_seed42` 和 `_postfix` 后缀）
- Cron 读不到日志 + 进程已退出 → 触发 "process dead 5× with no sentinel" → auto-resolved failed

### 实验真实情况

| 项 | 值 |
|---|---|
| 启动时间 | 2026-05-24 19:31:31 |
| 完成时间 | 2026-05-24 22:34:24 |
| 运行时长 | ~3.05 小时 |
| 最终结果 | **libero_10 prune=random keep=0.9 SR=32.0%** |
| 结果文件 | `eval_results/pi05_random_k0.90_libero_10_seed42.json` |
| 使用 GPU | CUDA_VISIBLE_DEVICES 内的 GPU 0（10 个任务 × 50 episodes 全部跑完） |

10 个任务 SR 全部正常输出：T0=10%, T1=46%, T2=38%, T3=44%, T4=16%, T5=26%, T6=10%, T7=38%, T8=10%, T9=82%，total=32.0%。无任何 OOM / 错误堆栈，结束有 RESULT 行和 JSON 保存确认。

### 当前 westd-41074 GPU 状态

| GPU | 显存 | 利用率 | 进程 |
|---|---|---|---|
| 0 | 9.7GB | 0% | PID 460971（其他实验，新启动） |
| 1 | 9.7GB | 0% | PID 461122（其他实验，新启动） |
| 2 | 10.8GB | 47% | PID 402927（`eval_pi05_l2norm_k03_long_seed42_postfix` 跑了 5h53m，仍在跑） |
| 3 | 1MB | 0% | **空闲** |

无失败实验的残留进程，无 OOM。

### 建议

**无需重跑**。结果 JSON 已存在，可直接使用：
```
/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.90_libero_10_seed42.json
```

需要修复的是 **启动脚本的日志命名约定** —— 让 `tee` 输出的 log 文件名严格匹配 cron 的 experiment id（即必须包含 `_seed42_postfix`），否则后续相似实验会反复被误判失败。也可以让 cron 对已生成的 JSON 结果文件做兜底确认（找到对应 result JSON 就标 success），更鲁棒。

---
