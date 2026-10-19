# ops gpu cleanup and launch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_cleanup_and_launch_20260515T204018_result.json`
- **Structured JSON:** [`6c7b79f2c197254aab91.json`](../../sessions/6c/6c7b79f2c197254aab91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 完全释放。以下是完整报告：

---

## GPU 清理 + 零样本 eval 启动报告

### GPU 清理
- Ray 停止: **OK** (46/47 进程 killed，1 个 forcefully terminated)
- 显存释放: cuda:0 ~48GB→0MiB, cuda:1 ~48GB→0MiB
- 残留进程: 无

### exp027 退出诊断
- **退出原因**: Step 4 完成后，进入 step 5 rollout 前被 **SIGKILL 外部终止**（非 OOM/非自然结束）
- 错误: `ray.exceptions.ActorUnavailableError: RPC error: Socket closed` → Raylet 异常终止
- EXIT_CODE=1
- **判断**: 极大可能是 earlystop worker 杀了进程，因为 step 4 success=13.28% 未达阈值
- 训练轨迹（train success）:

| Step | success | pass@16 | KL |
|------|---------|---------|-----|
| 1 | 35.9% | 100% | 0.022 |
| 2 | 10.15% | 62.5% | 0.025 |
| 3 | 10.15% | — | — |
| 4 | **13.28%** | 37.5% | 0.023 |

Step 1→2 发生严重崩塌（35.9%→10.15%），后续未恢复。

### 零样本 eval (exp028_prereq)
- 状态: **已完成**
- PID: 812681 (已正常退出)
- 模型: `/root/cost-verify-agent-rl/models/Qwen3-1.7B-Instruct` → 实际为 Qwen3-1.7B **基座模型**
- W&B run: `exp028-prereq-zeroshot-instruct` (run ID: qdvv09da)
- 耗时: ~35 分钟
- 16 episodes 结果:

| 指标 | 值 |
|------|-----|
| **success** | **0.0%** (0/16) |
| action_is_valid | 0.75% |
| num_actions | 50.0 (全部 hit max turn) |
| pass@1 | 0.0% |
| response_length | 75.07 |

### 关键发现与警告

**"SFT是毒药"假设无法通过此实验验证。** 原因：

1. **模型错误**: 服务器上 `Qwen3-1.7B-Instruct` 符号链接指向 **Qwen3-1.7B 基座模型**（非 Instruct）
2. ModelScope 上 `Qwen/Qwen3-1.7B-Instruct` 返回 404，HuggingFace 返回 401（无 token 且可能不存在独立 Instruct 变体）
3. Qwen3 系列可能 **不发布独立 Instruct 模型**（base 和 instruct 共用同一 tokenizer/chat template）
4. 基座模型 0% success 是预期结果（无法遵循指令），**不能**与 SFT checkpoint 6.25% 对比得出结论

**下一步建议**: 需确认 Qwen3 是否有独立 Instruct 权重。如果没有，"SFT是毒药"假设需要用其他 Instruct 模型（如 Qwen2.5-1.5B-Instruct）来验证，或者从 HuggingFace 配置 token 后重新下载。

---
