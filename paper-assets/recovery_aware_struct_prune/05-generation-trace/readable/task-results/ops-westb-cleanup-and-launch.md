# ops westb cleanup and launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_cleanup_and_launch_20260518T163258_result.json`
- **Structured JSON:** [`3f9db31b0f05dfda1e07.json`](../../sessions/3f/3f9db31b0f05dfda1e07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

---

### 磁盘清理结果

| 清理项 | 释放空间 |
|---|---|
| grpo_standard_20_1p5b/checkpoint-100（重复模型副本）| ~2.8GB |
| 所有 optimizer/scheduler/training_args/rng_state | ~几MB |
| pip cache | ~366MB |
| Python __pycache__ | 微量 |

**当前磁盘**：数据盘 24GB 可用（250G 总量），根分区 22GB 可用。**未达 30GB 目标**，差 6GB。

### 占空间最大但未删除的目录

| 目录 | 大小 | 说明 |
|---|---|---|
| `/root/autodl-tmp/models/Qwen2.5-Math-7B/` | **15GB** | 项目代码中无引用，疑似不再需要 |
| 各 7B SFT/GRPO/pruned 模型 | 各 ~12GB | 实验模型，不能删 |

**建议**：删除 Qwen2.5-Math-7B 即可释放 15GB，数据盘达到 39GB 可用。是否删除？

---

### E3 CKA 状态：已完成

4 个 heatmap JSON 全部生成完毕（May 19）：

| 对比 | diag_avg | min | max |
|---|---|---|---|
| Dense vs CKA-only | **0.6202** | 0.3794 | 0.9921 |
| Dense vs RASP | 0.8822 | 0.7574 | 0.9934 |
| Dense vs Standard | 0.9039 | 0.8412 | 0.9926 |
| Dense vs Random | 0.9233 | 0.7668 | 0.9960 |

CKA-only 剪枝后表征变化最大（diag_avg 最低），Random 剪枝变化最小。

---

### GPU 状态

两块 GPU 均空闲（0 MiB / 97GB）。有一个 idle tmux session `scoring_ablation_v2`（已完成的 sft_gradient_20）。

### 待决定

1. 是否删除 Qwen2.5-Math-7B（15GB）以达到 30GB 目标？
2. 磁盘达标后，是否启动 1.5B GSM8K eval？（eval 脚本 `eval_gsm8k.py` 已就绪，需确认评估哪些模型）

---
