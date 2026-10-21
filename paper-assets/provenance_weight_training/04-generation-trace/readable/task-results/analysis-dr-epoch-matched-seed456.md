# analysis dr epoch matched seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dr_epoch_matched_seed456_20260522T102824_result.json`
- **Structured JSON:** [`ee6968adcfe192b49ece.json`](../../sessions/ee/ee6968adcfe192b49ece.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常完成（2533/2533 steps, EXIT_CODE=0），但**日志中没有任何 eval 结果**——holdout/owt/wiki eval 均未执行。模型 checkpoint 已保存。

汇总当前已知信息：

| 项目 | 状态 |
|------|------|
| 训练步数 | 2533/2533 ✅ |
| EXIT_CODE | 0 ✅ |
| checkpoint | `/root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_seed456/final/` (1.1GB model.safetensors) ✅ |
| train_loss (Trainer avg) | 11.1（HF Trainer 累计均值） |
| last step micro-batch losses | 3.23, 3.04, 2.57, 1.06 (step 2532) |
| b 值 | 全程 b=0（epoch-matched D&R 使用 uniform weighting，符合预期） |
| **eval (holdout/owt/wiki)** | **未执行** ❌ |

**需要你手动运行 eval**，或者告诉我用什么 eval 脚本/命令，我来提交。日志中完全没有 eval 相关输出，模型目录也没有 eval_results.json。

同系列 seed42 的 eval 结果（holdout=17.651）和 seed123（holdout=17.659）应该是在训练完成后单独跑的 eval 脚本产出的。

---
