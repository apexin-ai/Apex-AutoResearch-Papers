# code llama crossmodel prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-crossmodel-prep_20260521T073708_result.json`
- **Structured JSON:** [`c73d7fd71e1ea67d3c2b.json`](../../sessions/c7/c73d7fd71e1ea67d3c2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All work complete. Here's the full report:

---

## D165 诊断报告

### 1. 训练数据状态
训练数据 `train_500_seed42.jsonl` 含 Unicode FOL（∀∃→∧∨¬⊕）。但这**不是**失败原因——`Prover9Solver._normalize_fol()` 已有完整的 Unicode→ASCII 映射。

### 2. D158 失败根因
**LLaMA `<|eot_id|>` (128009) 未被加入 eos_token_id 列表。**

LLaMA 3 chat template 用 `<|eot_id|>` 标记 turn 结束，但 `generation_config.json` 只有 `eos_token_id: [128001]`（`<|end_of_text|>`）。`model.generate()` 不会在 128009 处停止 → 生成无限循环 → 输出变成 `"Conclusion: Advocate(mary)assistant\n\nUse standard FOL notation..."` 这样的 garbage → parser 提取到污染的公式 → Prover9 全部失败。

### 3. 修复清单

| 文件 | 修改 |
|------|------|
| `scripts/eval_sta.py` | 新增 `_get_eos_token_ids()`: 自动检测 `<|eot_id|>` 加入 eos 列表; 新增 `_clean_generation()`: 截断 role marker 残留; `generate_formalization()` 传递正确 eos_token_id |
| `scripts/train_grpo.py` | GRPOTrainer 创建后 patch `generation_config.eos_token_id` |
| `scripts/train_sft.py` | 保存模型时更新 `generation_config.json` 加入 `<|eot_id|>` |

所有修改对 Qwen 无影响（Qwen 没有 `<|eot_id|>` token，检测跳过）。

### 4. SFT Gate 结果：**通过**

| 指标 | D158 旧 eval | D165 修复后 |
|------|-------------|------------|
| Prove Rate | 0/100 (0%) | **16/100 (16%)** |
| Mean ISR | 0.0 | 0.0879 |
| Proved-only ISR | — | 0.5492 |

- `true` 类: 15/34 proved (44%)
- `false` 类: 0/25
- `unknown` 类: 1/41
- D158 SFT checkpoint 可直接用作 GRPO warmstart，无需重训

### 5. GRPO 训练命令（3 seeds, ready to submit）

**前提：需先清理磁盘**（当前仅 9.3G 空闲）
```bash
# 释放 18G：删除 D158 SFT 的 checkpoint 副本（最终模型在父目录已保存）
rm -rf /root/autodl-tmp/outputs/d158_llama_sft_s42/checkpoint-189/
```

**Seed 42:**
```bash
export CUDA_VISIBLE_DEVICES=0
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation
python scripts/train_grpo.py --config configs/d165_llama_exec_s42.yaml
```

**Seed 43:**
```bash
export CUDA_VISIBLE_DEVICES=0
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation
python scripts/train_grpo.py --config configs/d165_llama_exec_s43.yaml
```

**Seed 44:**
```bash
export CUDA_VISIBLE_DEVICES=0
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation
python scripts/train_grpo.py --config configs/d165_llama_exec_s44.yaml
```

每个 run 约需 12-15G 磁盘（save_total_limit=1），需串行执行（一张 GPU）。三个配置已写入 `configs/d165_llama_exec_s{42,43,44}.yaml`。

---
