# code fewnerd fs pipeline completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fewnerd-fs-pipeline-completion_20260519T231728_result.json`
- **Structured JSON:** [`e8922c530c6e4fad2872.json`](../../sessions/e8/e8922c530c6e4fad2872.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了：脚本对每个数据集跑 N=8 stochastic + 1 greedy。FewNERD stochastic (301184 prompts) 即将完成，之后还有 greedy pass (37648 prompts)。

估算 greedy pass 参考 CoNLL (3453 prompts 用了 5:12, ~11 it/s): FewNERD greedy ≈ 37648/11 ≈ 57 分钟。

**当前状态汇总：**

### autodl-5090-b: 72B FewNERD 3-shot 推理
- **Stochastic pass**: 98% (295664/301184), ETA ~6 分钟
- **Greedy pass**: 尚未开始，预计 ~50-60 分钟
- **总预计剩余**: ~60 分钟
- 输出目录: `output/72b_fewshot/fewnerd/`（SciERC 和 CoNLL 已完成）

### autodl-5090-c: 7B FewNERD QLoRA 训练
- **进度**: 81% (16681/20590 steps), epoch 4.04/5
- **Loss**: 0.0073, lr: 2.15e-05
- **速度**: ~2.35s/it
- **预计剩余**: ~2.5 小时
- **Checkpoint**: 刚保存了 checkpoint-16000，删除了旧的 checkpoint-10000

FewNERD FS 推理还没完成（greedy pass 需要约 1 小时），signal pipeline 暂时不能跑。需要我过一会儿再来检查吗？

---
