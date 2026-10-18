# code cross scale qwen7b 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_scale_qwen7b_001_20260516T024649_result.json`
- **Structured JSON:** [`e645afcfd0fdd60d6892.json`](../../sessions/e6/e645afcfd0fdd60d6892.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cross_scale_qwen7b_001 已提交并运行中。**

**已完成：**
- 4 个脚本写入服务器：`qwen7b_lora_finetune.py`（QLoRA 4-bit NF4）、`qwen7b_generate.py`（prefix-based generation）、`qwen7b_eval.py`（RF 5-fold CV + EDD）、`run_qwen7b_pipeline.sh`
- Dry-run 验证通过（finetune loss=2.01, generation 产出连贯文本）
- 全量 pipeline 在 tmux session `cross_scale_qwen7b` 中运行，GPU cuda:0
- Registry 已更新为 RUNNING

**关键设计决策：**
- 使用 Qwen2.5-7B-Instruct（base 版不在服务器上）
- Prefix-based generation：取上一 depth 训练数据前 32 token 做上下文，只保存续写部分。原因是 Instruct 模型从 EOS token 无法正常做无条件生成
- QLoRA: r=16, alpha=32, target=q/k/v_proj, batch=4, grad_accum=4, 3 epochs, lr=2e-4
- Feature extraction 使用 Pythia-1.4B（与其他实验一致）

**预计时间：** 5 个 depth × (finetune ~3.5min + generate ~3min) + feature extraction ~10min + eval ~2min ≈ 45-50 min

**监控：** `tail -f logs/qwen7b_pipeline.log` 或查看 tmux session `cross_scale_qwen7b`

---
