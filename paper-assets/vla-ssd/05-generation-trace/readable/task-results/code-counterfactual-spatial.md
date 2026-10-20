# code counterfactual spatial

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_counterfactual_spatial_20260520T201754_result.json`
- **Structured JSON:** [`4391a51d6cf797250478.json`](../../sessions/43/4391a51d6cf797250478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功提交并正在运行。日志输出因 `tee` 缓冲延迟，但进程和 GPU 占用确认正常。

**汇总：**

| 项目 | 状态 |
|------|------|
| LIBERO-Spatial 数据 | 10 tasks × 50 demos，全部就绪 |
| 模型 | openvla-7b（pretrained，与 Goal 实验一致） |
| 脚本 | `/root/vla-ssd/scripts/counterfactual_spatial.py` (553 行) |
| 输出目录 | `/root/autodl-tmp/vla-ssd/results/counterfactual_spatial/` |
| Job ID | `counterfactual_spatial` (tmux session) |
| GPU | cuda:0，RTX PRO 6000 Blackwell (98GB) |
| 预计耗时 | ~1h（参考 Goal 实验 ~57min @7.3 pass/s） |

**关键设计决策：**
- "wrong" condition 使用**其他 spatial task 的指令**（同一对象/动作，不同空间参照），直接测试空间语言 grounding 的敏感性——这比 Goal 实验更精细，因为只改变了空间参照词
- 其余 3 个 condition（empty/shuffled/paraphrased）与 Goal 实验完全一致
- 参数保持一致：10 demos × 50 timesteps, seed=42

---
