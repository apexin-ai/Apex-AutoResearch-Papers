# analysis grpo v2 reward components

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_v2_reward_components_20260513T073447_result.json`
- **Structured JSON:** [`969f212844d095e9378a.json`](../../sessions/96/969f212844d095e9378a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 分量数据不可用

日志中只有 `rewards/reward_fn/mean`（composite），**没有** provenance / structural / format 的分别记录。

**原因**：`rewards.py` 的 `composite_reward()` 在内部计算了三个分量（`provenance_fidelity_reward`, `structural_f1_reward`, `format_compliance_reward`），但只返回加权和 `w_prov * p + w_struct * s + w_fmt * f`。TRL GRPOTrainer 只接收一个 `reward_fn`，所以只 log composite 值。

### Composite reward 趋势（step 1-43）

从日志提取的 composite reward：

| Step | Reward | Step | Reward | Step | Reward |
|------|--------|------|--------|------|--------|
| 1 | 0.789 | 16 | 0.740 | 31 | 0.775 |
| 2 | 0.699 | 17 | 0.700 | 32 | 0.732 |
| 3 | 0.657 | 18 | 0.771 | 33 | 0.838 |
| 4 | 0.781 | 19 | 0.697 | 34 | 0.719 |
| 5 | — | 20 | 0.725 | 35 | 0.783 |
| … | ~0.65-0.83 | … | ~0.65-0.83 | 36 | 0.765 |
| | | | | 37 | 0.773 |
| | | | | 38 | 0.662 |
| | | | | 39 | 0.721 |
| | | | | 40 | **0.522** |
| | | | | 41 | 0.830 |
| | | | | 42 | 0.712 |
| | | | | 43 | 0.664 |

Reward 在 **0.52–0.84 之间波动，没有上升趋势**，step 40 出现较大下跌。确认了 Director 的判断：reward 整体平坦。

### Step 50 Eval 分量 Breakdown 方案

在 `composite_reward()` 中加 logging，或者更快的方式——写一个离线 eval 脚本，对 checkpoint 的输出单独计算三个分量：

```python
# eval_reward_breakdown.py
from rewards import provenance_fidelity_reward, structural_f1_reward, format_compliance_reward
import json

# 加载 eval 样本的 prompts/completions/gold_relations（从 checkpoint 生成）
with open("eval_outputs.json") as f:
    data = json.load(f)

prompts = data["prompts"]
completions = data["completions"]
kwargs = {"gold_relations": data["gold_relations"],
          "nli_model_name": "/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large",
          "nli_device": "cuda:0", "nli_batch_size": 16,
          "iou_weight": 0.4, "nli_weight": 0.4, "length_weight": 0.2,
          "length_penalty_factor": 0.002}

prov = provenance_fidelity_reward(prompts, completions, **kwargs)
struct = structural_f1_reward(prompts, completions, **kwargs)
fmt = format_compliance_reward(prompts, completions, **kwargs)

print(f"Provenance: mean={sum(prov)/len(prov):.4f}")
print(f"Structural: mean={sum(struct)/len(struct):.4f}")
print(f"Format:     mean={sum(fmt)/len(fmt):.4f}")
print(f"Composite:  mean={sum(0.475*p+0.475*s+0.05*f for p,s,f in zip(prov,struct,fmt))/len(prov):.4f}")
```

**两个选择**：
1. **离线 eval**（不改训练代码）：用当前 step-43 checkpoint 跑 eval set，分别调三个 reward 函数，得到分量 breakdown
2. **加 online logging**（需改代码重启）：修改 `composite_reward()` 加 `print` 或 wandb log，v3 再用

建议先走方案 1，不打断训练。

---
