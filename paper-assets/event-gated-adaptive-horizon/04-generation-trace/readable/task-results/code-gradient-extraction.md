# code gradient extraction

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient-extraction_20260516T170956_result.json`
- **Structured JSON:** [`768bac5ed3e96d7bccbd.json`](../../sessions/76/768bac5ed3e96d7bccbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**结果：**

| 项目 | 状态 |
|------|------|
| 25K/50K/75K checkpoint | **不存在** — exp_008d 只保存了 `latest.pt`，无中间 checkpoint |
| latest.pt (step 55K) | 已提取梯度分解数据 |
| 脚本 | 已上传到服务器 `scripts/compute_gradient_decomposition.py`，已注册 artifact |
| methodology 文档 | 已更新表格，添加 55K 数据行 |

**Step 55K 梯度分解（10 batch 均值 ± std）：**

| 分量 | ‖∇‖₂ | 占比 |
|------|-------|------|
| obs (decoder) | 0.601 ± 0.199 | 25.8% |
| reward | 0.546 ± 0.227 | 23.5% |
| KL | 1.180 ± 0.251 | 50.7% |
| cont | 0.000 ± 0.000 | 0.0% |

**关键发现：** 55K 的分解与 105K 报告的 93%/≈0%/7% 形成鲜明对比。mid-training 时 KL 主导（51%），obs 和 reward 大致相当（~25%）。随着训练推进 KL 收敛到 free-bits 阈值，obs 逐渐成为主导。这实际上强化了 CIVO 的 narrative：obs 主导是训练后期的稳态现象，不是整个训练过程的恒定特征。

**要获取 25K/50K/75K 数据，需要重新运行 exp_008d 并启用 checkpoint 保存。**

---
