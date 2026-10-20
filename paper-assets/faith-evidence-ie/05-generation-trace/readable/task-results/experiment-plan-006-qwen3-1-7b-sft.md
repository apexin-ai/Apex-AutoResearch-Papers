# experiment plan 006 qwen3 1 7b sft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_20260516T052333_result.json`
- **Structured JSON:** [`fd18214b3eaf33aec510.json`](../../sessions/fd/fd18214b3eaf33aec510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 正在运行 SFT baseline re-eval（`sft_baseline_d076_reeval`，PID 303070，13:26 启动）。

**C001 合规：GPU 1 显存 10149 MiB > 2GB，不满足提交条件。停止并汇报。**

---

**状态汇报：**

| 项目 | 状态 |
|------|------|
| Qwen3-1.7B 模型 | ✅ 已下载到 `/root/autodl-tmp/models/Qwen/Qwen3-1.7B` |
| SFT 训练配置 | ✅ 已确认（rank=64, alpha=128, 7 target modules, QLoRA 4-bit） |
| GPU 1 可用性 | ❌ 被 `sft_baseline_d076_reeval` 占用（PID 303070，~10GB） |

**阻塞原因：** GPU 1 正在跑 SFT baseline 的 dev eval（batch_size=4, 985 docs）。参考同类 eval 耗时 ~2.5-3h，启动时间 13:26，预计 ~16:00-16:30 UTC 完成。

**选项：**
1. **等 eval 完成后再提交**（~2.5h 后）
2. **换到其他空闲 GPU**（当前 0/2/3 均被占用）
3. **手动终止 d076_reeval 后立即提交**（需要你确认）

训练命令已准备好，模型就绪，等 GPU 释放即可立即提交。

---
