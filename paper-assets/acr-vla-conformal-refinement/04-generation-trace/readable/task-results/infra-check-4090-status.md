# infra check 4090 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-4090-status_20260513T151621_result.json`
- **Structured JSON:** [`41207d9b98316d5f8352.json`](../../sessions/41/41207d9b98316d5f8352.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，汇总如下：

---

## 诊断结果

### 1. 模型下载状态
- **smolvla_libero** (865MB): ✅ 已下载到 `/root/autodl-tmp/models/smolvla_libero/`
- **SmolVLM2-500M-Video-Instruct**: ✅ 在 HF cache 中 (`/root/autodl-tmp/.hf_cache/hub/models--HuggingFaceTB--SmolVLM2-500M-Video-Instruct/`)，但未单独存到 models 目录
- **libero assets**: ✅ 已存在于 site-packages 目录

### 2. Eval 执行情况
- **没有** `eval_vla_object_K1.log` — Worker 从未跑 K=1 object eval
- 实际跑的是 **reconvla 模式, K=10, n_rollouts=20**（plan_014）
- `reconvla_object.log` 创建于 14:58，最后修改 17:21（运行约 2.5h），只有 16 行，停在 `[eval] 10 tasks loaded.` 后无任何 rollout 输出
- **eval 进程当前未运行**，GPU 内存 0 MiB

### 3. 失败根因
**Worker 超时（3h15m），eval 未完成即被 kill。** 原因：

- K=10 的 reconvla 模式下，每个 step 需要 10 次 VLA forward pass
- 每个 rollout 最多 300 steps，估计每个 rollout 耗时 30-50 分钟
- 首次 progress 打印在第 5 个 rollout（`(r+1) % 5 == 0`），约需 2.5-4 小时
- Worker 在完成第一个 task 的前 5 个 rollouts 之前就超时了，所以日志无 rollout 输出

### 4. 当前服务器状态
| 项目 | 状态 |
|------|------|
| GPU | 空闲，0 MiB / 24564 MiB，0% 利用率 |
| 根分区 | 18G/30G (58%) — 尚可 |
| 数据盘 | 99G/250G (40%) — 充裕 |
| 残留进程 | PID 48594 — libero assets 下载进程仍在运行（已跑 ~8h，疑似卡住） |
| artifacts/ | 空，无输出 JSON |

### 5. 建议

如果要重跑 K=1 object eval（10 tasks × 3 rollouts），预估时间大幅缩短（K=1 vs K=10，3 rollouts vs 20），约 30-60 分钟可完成。需要：
1. 先 kill 卡住的 assets 下载进程（PID 48594）
2. 确认用 `smolvla_libero`（fine-tuned）还是 `smolvla_base`
3. 用 nohup 启动 eval，避免 SSH 超时问题

---
