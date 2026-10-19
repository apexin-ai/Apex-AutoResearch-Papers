# deploy pi05 spatial eval 3seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-spatial-eval-3seeds_20260522T011150_result.json`
- **Structured JSON:** [`43926df367219c48c436.json`](../../sessions/43/43926df367219c48c436.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署完成

### 1. bjb1-18228 源 checkpoint
- 路径: `/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt`
- 大小: **2484379 字节** (2.4M)
- mtime: `1779411793` (May 22 09:03)

### 2. bjb2-28827 目标 checkpoint（校验）
- 大小: **2484379 字节** ✅ 与源一致
- mtime: `1779412497`（传输后更新，符合预期）
- 传输方式: bjb1↔bjb2 无法直连，通过本地 scp 中转（autodl-4090x4 别名 = bjb1-18228）

### 3. 3 个 eval PID（tmux wrapper / python 子进程）
| Exp | GPU | tmux PID | python PID |
|---|---|---|---|
| eval-pi05-crm-spatial-seed42 | cuda:0 | 148748 | running |
| eval-pi05-crm-spatial-seed43 | cuda:1 | 149025 | 149038 |
| eval-pi05-crm-spatial-seed44 | cuda:2 | 149307 | 149320 |

3 个 evaluate.py 全部 99% CPU 运行，日志显示已开始加载 π0.5 模型；`/tmp/agent-ml-exit/` 中无 seed42/43/44 的 exit 文件，确认未退出。

### 4. 异常
- 跨服务器 ssh/rsync 失败：bjb1-18228 不能 DNS 解析 bjb2-28827。改用本地 scp 中转，2.4MB 文件传输无影响。registry 已全部推进到 RUNNING。

---
