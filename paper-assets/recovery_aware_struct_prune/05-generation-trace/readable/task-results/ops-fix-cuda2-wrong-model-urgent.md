# ops fix cuda2 wrong model urgent

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_cuda2_wrong_model_urgent_20260518T223758_result.json`
- **Structured JSON:** [`44515c8cb967bff71efd.json`](../../sessions/44/44515c8cb967bff71efd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行：cuda:2 使用 50492MiB（包含模型+优化器+梯度），173 线程，R 状态。日志未更新是 Python stdout 缓冲问题，训练实际在跑。

---

## 状态报告

| 项目 | 状态 |
|------|------|
| **1) Kill PID 33033** | 成功，cuda:2 已释放 |
| **2) sft_standard_20 模型** | **权重已丢失**（westb 和 westd 都没有）。训练日志确认曾存在但被删除 |
| **3) 重训 SFT** | 已在 westd cuda:2 提交重训（PID 34346），从 `pruned_standard_20` 训练，预计 ~36 分钟完成。训练已正常启动（50GB VRAM 占用）|
| **4) Math500 eval 重启** | 等 SFT 重训完成后启动 |
| **5) cuda:1 进度** | `eval_math500_grpo_standard_20_fair_v2`: **304/500, acc=0.27**，预计还需 ~3-4 小时 |

**后续**：SFT 重训完成后（~07:15-07:20），我会启动 Math500 eval。需要我继续监控还是你手动跟进？

---
