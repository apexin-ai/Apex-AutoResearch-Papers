# check mvp v2 status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mvp_v2_status_20260514T081457_result.json`
- **Structured JSON:** [`f88272b008bfa79a4d12.json`](../../sessions/f8/f88272b008bfa79a4d12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**1. 进程状态：Running**
- PID 170770 存活，运行约 3 分钟
- 3 个 GPU 进程活跃：
  - PID 170786 — `eval_gsm8k.py` on `pruned_standard_35` (cuda:0, ~10GB)
  - PID 170787 — `eval_gsm8k.py` on `pruned_rasp_35` (cuda:1, ~10GB)
  - PID 171091 — test eval on `pruned_standard_35` (cuda:0, ~10GB, 20 samples)

**2. 当前 Step：3.5 (Post-prune evaluation)**
- 正在对两个剪枝模型并行跑 GSM8K 评估（1319 test samples）
- HF Hub 网络不可达，已 fallback 到本地缓存的 GSM8K 数据集

**3. 最新日志摘要**
- 加载了 `pruned_standard_35` 和 `pruned_rasp_35` 模型
- 检测到非均匀 MLP（intermediate_size range [2720, 18944]）
- GSM8K 评估已开始，进度 0%（刚启动）

**4. 已有产出文件**
| 文件 | 说明 |
|------|------|
| `results/cka_scores.pt` | Step 2 CKA 分数 |
| `results/importance_scores.pt` | Step 2 重要性分数 |
| `models/pruned_standard_35/` | Step 3 标准剪枝模型 |
| `models/pruned_rasp_35/` | Step 3 RASP 剪枝模型 |

**5. 进度总结**
- Step 1 ✅ baseline eval（前序运行完成）
- Step 2 ✅ CKA + importance
- Step 3 ✅ Pruning
- Step 3.5 🔄 Post-prune eval（进行中）
- Step 4-6 ⏳ 未开始

GSM8K 评估 1319 samples 预计需要一段时间，之后进入 Step 4 (GRPO RLVR recovery, 预估 12-15h)。

---
