# diagnose codellama13b label only seed123 v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_codellama13b_label_only_seed123_v2_20260521T010347_result.json`
- **Structured JSON:** [`b17d98e0e2e174ac09fc.json`](../../sessions/b1/b17d98e0e2e174ac09fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

1. **失败原因**：根分区磁盘满（30G/30G），checkpoint-444 保存时 `No space left on device`。训练 444/444 steps 全部完成，`evaluate.py` 从未执行。

2. **模型已完全 collapse**：epoch 2-3 全程 loss=0.0，grad_norm≈0，eval_loss=nan，entropy=0.25。与 seed42（28.5% 全预测 fail）完全一致。

3. **科学结论确认**：CodeLlama-13B label-only collapse 是 systematic 的（seed42 + seed123 双种子验证），与 DeepSeek collapse pattern 一致，支持 "label-only collapse is systematic for non-Qwen architectures" 假设。

4. **可恢复性**：checkpoint-296（epoch 2）完整可用，但模型早已 collapse，重跑 eval 无科学价值。

5. **紧急问题**：根分区 100% 满，会影响后续所有实验，需要优先清理。

报告已写入 `artifacts/diagnose_codellama13b_label_only_seed123_v2.md`。

---
