# research fact check eval and init

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_fact_check_eval_and_init_20260515T214040_result.json`
- **Structured JSON:** [`bb0ec54911b16c398393.json`](../../sessions/bb/bb0ec54911b16c398393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确。

---

## 问题 1: Eval held-out set 的 real/synthetic 比例

**论文说的 "balanced (50/50 real/synthetic)" 不准确。Eval held-out set 是 100% real data。**

证据：
- 文件 `data/human/eval_holdout.jsonl`，67,823 行，**全部** `"source": "fineweb"`，`"depth": 0`
- 创建脚本 `data/save_human_data.py` 显示 eval_holdout 完全从 FineWeb（真实人类数据）流式采样，目标 ~50M tokens，**不含任何 synthetic 数据**
- 所有训练脚本（10+ 个 `run_*.sh`）的 `--eval_data_path` 都指向这个纯 real 文件
- eval pipeline docstring 也写明 "Perplexity on held-out **FineWeb**"

**结论**：论文需修正——eval held-out set 比例是 100/0 (real/synthetic)，不是 50/50。这是合理的实验设计（用纯 real held-out 评估 perplexity 是为了衡量模型在真实分布上的泛化能力），但论文描述有误。

---

## 问题 2: 训练是 continued pretraining，不是 random init

**`pretrain_weighted.py` 第 318 行：**
```python
model = AutoModelForCausalLM.from_pretrained(
    args.model_name,
    torch_dtype=torch.bfloat16 if use_bf16 else torch.float32,
    trust_remote_code=True,
)
```

证据：
- 使用 `from_pretrained()`，加载 Qwen3-0.6B 的预训练权重
- 代码中无 `from_config()`（grep 返回空）、无 `init_weights()`（grep 返回空）
- `--model_name` 默认值为 `Qwen/Qwen3-0.6B`（第 231 行），实际训练用 `models/Qwen/Qwen3-0.6B`（本地缓存路径）

**结论**：这是 **continued pretraining**（在 Qwen3-0.6B 预训练权重基础上继续训练），不是 random init。

---
