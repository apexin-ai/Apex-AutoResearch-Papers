# code action head sanity check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action_head_sanity_check_20260526T195505_result.json`
- **Structured JSON:** [`b068544c9b80af9062ed.json`](../../sessions/b0/b068544c9b80af9062ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 项检查全部完成。以下是完整诊断结果。

---

## 完整诊断结果

### CHECK 3: Double-norm bug — **确认存在，但非主因**

```
hidden_states[32] IS POST-norm (已经过 RMSNorm)
  lm_head(hs) vs model logits:       max=0.0625  ← 几乎一致 (bfloat16 精度)
  lm_head(norm(hs)) vs model logits: max=1.3125  ← 显著偏差

L2 norms:
  hs[ 0]: raw=1.1,   after_norm=118.7
  hs[31]: raw=193.3,  after_norm=114.9
  hs[32]: raw=114.8,  after_norm=120.1  ← 已经是 post-norm，再 norm 变化不大
```

**结论**: `hidden_states[32]` 确实是 post-norm 的（HuggingFace LlamaModel 在返回 `all_hidden_states` 最后一个元素前已经过 `model.norm`）。原始脚本对所有层统一做 `lm_head(norm(hs))`，exit layer 被 double-norm。**但在当前情况下，double-norm 并不改变 argmax token（两种方法都输出 31935）**。

### CHECK 1 & 2: Exit layer 预测 — **模型输出完全退化**

**所有 10 个样本、所有 7 个 action 维度，无论 teacher-forcing 还是 autoregressive，model 都只输出 token 31935（=-0.4941）。**

```
Sample 0:  GT=[31844 31881 31872 31908 31810 31923 31999]
           Pred=[31935 31935 31935 31935 31935 31935 31935]  (all methods)
Sample 1:  GT=[31819 31884 31872 31919 31856 31931 31999]
           Pred=[31935 31935 31935 31935 31935 31935 31935]
...
Sample 9:  GT=[31836 31863 31872 31891 31825 31964 31999]
           Pred=[31935 31935 31935 31935 31935 31935 31935]

Exact match:  0.0000 (ALL methods)
Top-5 match:  0.0143
R²:           -11.6231 (ALL methods — correct/buggy/autoregressive 都一样)
```

### CHECK 4: Bin→continuous 反量化 — **无 bug**

```
Roundtrip max error: 0.003922 (仅 bin 量化误差)
De-tokenization 与 model.predict_action 一致: True
```

---

## 根因分析

**Double-norm 不是主因。** 主因是 **transformers 版本不兼容**：

```
Expected: transformers==4.40.1, tokenizers==0.19.1
Got:      transformers==5.9.0,  tokenizers==0.22.2
```

模型在所有输入下都坍缩到同一个 token（31935 = -0.4941），包括自回归生成也是如此。这说明模型权重在 transformers 5.9.0 下没有被正确加载或推理行为已改变。LlamaModel 在 4.x → 5.x 之间有显著架构变化。

**建议下一步**: 降级 transformers 到 4.40.1 后重新运行验证，或者在正确版本环境中跑 `model.predict_action()` 确认模型本身推理正常。

---
