# ops extract zeroshot metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract-zeroshot-metrics_20260519T061238_result.json`
- **Structured JSON:** [`a5ea642701b15c7eaf15.json`](../../sessions/a5/a5ea642701b15c7eaf15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B run `kbt8a170` 时间 (12:07 开始) 与 zeroshot_eval.log (12:05 创建) 吻合，确认是同一次运行。W&B 有 702KB 的本地 `.wandb` 文件但因 BrokenPipeError 未上传。

---

## Qwen3-8B 零样本 eval 完整结果

**来源**: `/root/autodl-tmp/tmp/zeroshot_eval.log` (westd-47453)  
**时间**: 2026-05-19 12:05 ~ 12:46  
**模型**: `/root/autodl-tmp/models/Qwen3-8B`  
**评估集**: AlfworldSG_OOD, **134 episodes** (满足 C003 ≥16 要求)  
**W&B run**: `kbt8a170` (本地有数据，未上传)

### 核心 Metrics

| Metric | Value |
|--------|-------|
| **val/success** | **0.75%** (1/134) |
| **val/pass@1** | **0.75%** |
| **val/action_is_valid** | **4.08%** |
| val/action_is_effective | 6.10% |
| val/manager_invalid_action | **93.90%** |
| val/num_actions (avg) | 2.94 |
| val/response_length | 8924.07 |
| val-core/reward/mean@134 | 0.0746 |
| val-core/reward/best@134/mean | 6.24 |

### 关键发现

- **success rate < 1%** — 134 个 OOD episodes 仅约 1 个成功
- **93.9% 的 action 无效** — 模型几乎不会生成合法的 ALFWorld 动作
- 平均只执行 ~3 步就结束（max_actions=50），说明大量 episode 快速失败
- response_length ~8924 tokens 偏长，模型在生成大量无用文本

**结论**: 7B 零样本完全不可用，SFT 是必要的。直接 RL 从这个 baseline 起步几乎没有可学习信号（reward 接近 0）。

---

**第二个日志** (`7b_zeroshot_eval_v2.log`) 是后续重试，在 val eval 的 `reset()` 阶段因磁盘满 (`OSError: [Errno 28] No space left on device`) 崩溃，未完成 eval。

---
