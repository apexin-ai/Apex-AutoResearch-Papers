# code d146 eval classify script

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-eval-classify-script_20260519T171156_result.json`
- **Structured JSON:** [`ffe6f63b7f192266eb79.json`](../../sessions/ff/ffe6f63b7f192266eb79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入并通过语法检查。

**产出汇总：**

1. **eval_sta.py 参数**: `--model_path`(必需) `--data_path`(必需) `--output_path`(必需) `--logic_type fol`(默认) `--solver`(自动) `--max_new_tokens 512` `--timeout 5`
2. **classify_h7.py 参数**: `--eval_path`(单文件) `--batch`(多文件) `--json_out`(输出 JSON) `--out`(输出文本)
3. **D146 输出目录**: `d146_pf_exec_s42`(已完成，有 final model) / `d146_pf_exec_s43`(仅 checkpoint-300，训练中) / 其余 4 个尚未创建
4. **ISR 实验无需额外 eval 参数** — ISR 在 eval 时由 STA ablation 自动计算，与训练时的 reward_mode 无关

**脚本逻辑**：遍历 6 个实验 → 跳过未完成的（无 final model）→ eval_sta.py 生成 `eval_sta_results.json` → classify_h7.py 生成 `classify.json` → 最后用 batch 模式汇总所有已完成实验到 `d146_classify_summary.json`。

---
