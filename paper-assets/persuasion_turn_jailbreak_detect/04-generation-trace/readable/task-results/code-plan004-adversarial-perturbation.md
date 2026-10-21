# code plan004 adversarial perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan004-adversarial-perturbation_20260517T214835_result.json`
- **Structured JSON:** [`cea9dda3d051347d28fa.json`](../../sessions/ce/cea9dda3d051347d28fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/root/persuasion_turn_jailbreak_detect/src/adversarial_perturbation.py`，argparse 验证通过。

功能总结：
- **Step 1**：用 Qwen3-8B 对 test.jsonl 所有 user turn 做 aggressive paraphrase（`enable_thinking=False` + regex strip 双重保护），输出同格式 perturbed JSONL
- **Step 2**：加载 treatment (DeBERTa-FT + GRU) 和 baseline (DeBERTa-vanilla + GRU)，在 original 和 perturbed 数据上分别评估 F1/Precision/Recall/Accuracy @ K=1,2,3,full，输出对比表和 JSON 结果
- `--skip_perturb` 可跳过 Step 1 直接用已有 perturbed 文件评估

待 plan_002 训练完成后，用新 checkpoint 路径执行即可。

---
