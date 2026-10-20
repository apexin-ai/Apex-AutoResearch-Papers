# code prepare hgate eval

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-hgate-eval_20260512T161247_result.json`
- **Structured JSON:** [`5a3425b2a9abfb6aedd5.json`](../../sessions/5a/5a3425b2a9abfb6aedd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已创建，语法验证通过。

---

**脚本路径**：
- `/root/democalib/eval_dpo_model.sh` (153 行，可执行)
- `/root/democalib/merge_lora.py` (43 行)

**使用方式**：

```bash
# 方式 1（推荐）：vLLM 直接加载 LoRA adapter，不占额外磁盘
cd /root/democalib && ./eval_dpo_model.sh

# 方式 2（回退）：先合并 LoRA 再 serve，需要 ~14GB 额外磁盘
cd /root/democalib && ./eval_dpo_model.sh --merge
```

**关键设计决策**：

| 项目 | 说明 |
|------|------|
| **LoRA vs 合并** | 优先 vLLM `--enable-lora --lora-modules` 直接加载 adapter（vLLM 0.18.1 支持），避免保存 14GB merged model |
| **DPO adapter 路径** | `/root/democalib/dpo_output/final_adapter`（训练实际 output_dir 是 `dpo_output/`，不是 `results/dpo_checkpoint/`） |
| **GPU** | cuda:2（CUDA_VISIBLE_DEVICES=2），不干扰 cuda:3 上的训练 |
| **评估流程** | 跑完整流程（baseline + 5 个 BCP variants），因为 DPO 模型的 uncalibrated baseline 也需要测量 |
| **结果输出** | `/root/democalib/results/dpo_eval/mvp_results.json` |

**前置条件**：训练完成后 `final_adapter/` 目录必须存在（脚本有检查）。当前只有 checkpoint-359 和 checkpoint-718（epoch 1/2），epoch 3 完成后 trainer 会自动创建 `final_adapter/`。

---
