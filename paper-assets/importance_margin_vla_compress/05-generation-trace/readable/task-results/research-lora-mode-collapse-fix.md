# research lora mode collapse fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lora-mode-collapse-fix_20260516T111218_result.json`
- **Structured JSON:** [`a943427aeff58bd05b94.json`](../../sessions/a9/a943427aeff58bd05b94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/research_lora_mode_collapse_fix.md`。

核心发现：

1. **alpha/rank=2.0 是直接原因**——diffusion/flow matching 社区推荐 0.5x，当前 2.0x 过于激进，velocity field 被 LoRA 更新淹没
2. **MSE loss 天然平均多模态 velocity**（Cocos, arXiv:2505.11123），加上 LoRA 有限容量→全部 noise 映射到同一均值
3. **无正则化约束**——没有 KL/W2 penalty 防止偏离 pretrained model

最优先尝试的两件事：
- **P0-a**: alpha 64→16（1 个参数改动，立即重训）
- **P0-b**: inference 时在 ODE 积分中加微量噪声 σ=0.01~0.05（不需重训，改 `sample_actions()` 即可验证假设）

---
