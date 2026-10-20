# diagnose wiki eval failure

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_wiki_eval_failure_20260522T142525_result.json`
- **Structured JSON:** [`7cf30e9ec1e6abd8475a.json`](../../sessions/7c/7cf30e9ec1e6abd8475a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断报告

### 1. 失败模式
seed456 wiki eval 结果：**loss=NaN, perplexity=Infinity**。处理了全部 27M tokens（与成功的 seed 一致），但耗时 721s——是 seed42（381s）/seed123（385s）的近 2 倍，说明前期有计算但最终被 NaN 污染。

eval 脚本没有 NaN guard：`total_nll += outputs.loss.float().item() * n_tokens`，一旦任意一个滑窗产生 NaN，整个累加器永久变成 NaN。

### 2. 根因：bfloat16 训练 → float16 推理的 dtype 不匹配

**模型 config.json 明确写了 `"dtype": "bfloat16"`**（三个 seed 全部如此），但 `eval_perplexity.py:92` 加载模型用的是 `torch_dtype=torch.float16`，同时还套了 `torch.amp.autocast("cuda")`。

| dtype | 指数位 | 尾数位 | 最大值 |
|-------|--------|--------|--------|
| bfloat16 | 8 | 7 | 3.4e38 |
| float16 | 5 | 10 | **65504** |

float16 的动态范围比 bfloat16 小 33 个数量级。bfloat16 训练出的模型，某些中间激活值（attention logits、FFN 输出）在 float16 下溢出为 inf/NaN。

### 3. 为什么 holdout/owt 没问题

| 数据集 | tokens | 结果 |
|--------|--------|------|
| holdout | 4M | loss=2.849, ppl=17.28 ✓ |
| owt | 6.7M | loss=2.891, ppl=18.02 ✓ |
| wiki | 27M | NaN ✗ |

Wiki 的滑窗数量是 holdout 的 ~7 倍。NaN 是概率事件——处理的序列越多，越可能命中某个导致 float16 溢出的 token pattern。Wiki 文章也更长、内容更多样，更容易触发极端激活值。

### 4. 为什么 seed42/seed123 没出问题

三个 seed 同样是 bfloat16 训练 + float16 eval。seed456 恰好训出了某些层的权重幅度更极端，使得特定输入下中间激活超出 float16 范围。这是随机性导致的——seed42/seed123 的权重分布刚好没有触发溢出。

### 5. fp32 eval (PID 783753) 状态

**已完成**，结果正常：

| seed | eval 方式 | loss | ppl |
|------|-----------|------|-----|
| seed42 | fp16 | 2.7116 | 15.05 |
| seed123 | fp16 | 2.7111 | 15.05 |
| **seed456** | **fp32** | **2.7106** | **15.04** |

seed456 的 fp32 结果与另外两个 seed 完全一致，确认模型本身没有任何问题。

### 6. 建议修复

**立即**：直接使用 fp32 eval 结果（loss=2.710647, ppl=15.039004）。

**根本修复**：`eval_perplexity.py:92` 改 `torch.float16` → `torch.bfloat16`，匹配训练 dtype。保持半精度的速度/显存优势，同时避免动态范围不足。可选：在 eval 循环中加 NaN 检测，遇到 NaN 时 log 具体哪个 doc/window 出问题，而非默默污染整个结果。

---
