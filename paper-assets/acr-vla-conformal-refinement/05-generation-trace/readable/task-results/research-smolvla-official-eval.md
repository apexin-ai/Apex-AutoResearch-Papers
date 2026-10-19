# research smolvla official eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_smolvla-official-eval_20260522T092150_result.json`
- **Structured JSON:** [`3bc729561aac5c8e57e3.json`](../../sessions/3b/3bc729561aac5c8e57e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调研结论

### 1. SmolVLA 官方 Repo
- 代码在 [huggingface/lerobot](https://github.com/huggingface/lerobot) 框架下
- 论文: [arXiv:2506.01844](https://arxiv.org/abs/2506.01844)
- LIBERO fine-tuned 模型: [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)

### 2. 是否有 LIBERO eval 脚本：**YES**
lerobot 官方提供 `lerobot-eval` 命令，完整支持 LIBERO 四个 suite 的评估。文档见 [lerobot LIBERO docs](https://huggingface.co/docs/lerobot/libero)。

### 3. 官方 LIBERO 数字（SmolVLA 0.45B, fine-tuned 100k steps）

| Suite | Spatial | Object | Goal | Long | **Avg** |
|-------|---------|--------|------|------|---------|
| SR | 90% | 96% | 92% | 71% | **87.3%** |

### 4. 与我们的 baseline 对比——巨大差距的根因

| Suite | 官方 (fine-tuned) | 我们 (VLA-only) |
|-------|-------------------|-----------------|
| Object | 96% | 10.8% |
| Spatial | 90% | 29.4% |

**官方数字是在 LIBERO 训练集 (1693 episodes) 上 fine-tune 100k steps 后的结果。** 我们的数字如果是 zero-shot（未 fine-tune），差距完全可以解释——这是两个完全不同的评估设定。

值得注意：即使 fine-tune 后，社区多人报告无法复现官方数字（[#2354](https://github.com/huggingface/lerobot/issues/2354), [#3287](https://github.com/huggingface/lerobot/issues/3287)），均无官方 resolution。

### 5. 对论文的影响

需要在论文中明确两件事：
1. **我们评估的是什么**：是 pretrained SmolVLA (zero-shot) 还是 LIBERO fine-tuned 版本？如果是 zero-shot，需标注清楚，不能直接和官方 fine-tuned 数字对比
2. **Wrapper 的必要性**：如果不在 lerobot 框架内评估，我们的 wrapper 是必要的（处理 obs/action 映射、7-dim continuous action、relative control mode 等）。如果用 lerobot-eval，则不需要

### 6. 建议的下一步
- 确认我们的 SmolVLA baseline 是 zero-shot 还是 fine-tuned
- 如果是 zero-shot，考虑用官方 `lerobot-eval` + `HuggingFaceVLA/smolvla_libero`（fine-tuned 版本）跑一遍，获取 fair comparison baseline
- 复现命令模板已写入 `memory.md`

---
