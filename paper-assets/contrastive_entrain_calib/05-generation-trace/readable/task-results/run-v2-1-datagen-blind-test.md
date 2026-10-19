# run v2 1 datagen blind test

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_v2_1_datagen_blind_test_20260518T103232_result.json`
- **Structured JSON:** [`f8b12d7dda59a52daf65.json`](../../sessions/f8/f8b12d7dda59a52daf65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三轮迭代完成。汇报结果：

---

## v2.1 风格匹配校准数据生成结果

### Blind Classification Accuracy 迭代过程

| 轮次 | Accuracy | 改进措施 |
|------|----------|----------|
| 1 | **100%** (30/30) | 基础风格匹配（相同开头、置信度、引用模式） |
| 2 | **97%** (29/30) | + 要求错误答案在正确答案"邻域"内（10ft vs 11ft），更冷门事实 |
| 3 | **90%** (27/30) | + 全部 weak evidence（禁止引用），极冷门事实（Catalan 数、Bell 数、Mount Kinabalu 高度等），答案差异最小化 |

### 关键发现

**风格匹配已完全成功**——quality check 显示 100% turn3_balanced，平均长度差 1.1%，开头匹配 50/50。90% accuracy 的原因不是风格泄露，而是 **GPT-4.1 的世界知识**：即使是 C_3=5 vs 6、Bell(5)=52 vs 62 这样的冷门问题，GPT-4.1 仍有足够的事实知识来判断对错。

### 最终数据质量

- **Turn 1-2 一致性**: 100%（0% 差异）
- **Turn 3 平均长度差**: 1.1%
- **Turn 3 >20% 长度差**: 1/50 (math_0001)
- **LLM Quality Check**: ground_truth_correct 100%, wrong_answer_plausible 100%, turn3_balanced 100%
- **Evidence strength**: 全部 weak（无引用信号）
- **分布**: 5 domain × 10 pairs，均匀分布

### 数据文件路径

`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/calibration_v2_1.jsonl`

### 结论

要突破 70% 阈值，需要超出 prompt 工程的能力范围。可能的方向：
1. 使用完全虚构的事实（编造不存在的实体/事件），使 LLM 无法从知识库验证
2. 使用对 GPT-4.1 知识截断点之后的事实
3. 改用更弱的模型做 blind judge

---
