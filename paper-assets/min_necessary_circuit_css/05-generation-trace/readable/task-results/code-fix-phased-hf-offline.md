# code fix phased hf offline

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-phased-hf-offline_20260513T012834_result.json`
- **Structured JSON:** [`0215f16e7d0594cd4272.json`](../../sessions/02/0215f16e7d0594cd4272.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

### 修复
无需额外修复。代码中已有 `_patch_hf_from_pretrained()` + `load_tl_model()` 的本地路径加载逻辑。原始错误原因是运行时环境变量 `HF_HUB_OFFLINE=1`，当前环境已无此变量。GPT-2 本地路径：`/root/autodl-tmp/gpt2-small/`。

### Phase D Faithfulness Eval (CPR/CMD)

| Circuit | Edges | CPR | CMD |
|---------|------:|------:|------:|
| method_acdc | 32491 | 1.0000 | 0.0000 |
| css_0.33 | 32491 | 1.0000 | 0.0000 |
| **circus_core** | **1097** | **0.9097** | **0.1001** |
| method_eap_ig | 100 | -0.3635 | 1.5130 |
| css_1.00 | 35 | -0.3726 | 1.5231 |
| method_edge_pruning | 100 | -0.4692 | 1.6302 |
| stable_core | 98 | -0.7193 | 1.9078 |
| css_0.67 | 165 | -1.1260 | 2.3591 |

### Gate Assessment
- **Verdict: PASS_MAIN**
- Off-diagonal: 91.1%, 95% CI [89.2%, 92.7%]

关键观察：`circus_core`（1097 edges）是唯一在合理 size 下 CPR 接近 1 的 circuit（CPR=0.91, CMD=0.10）。小 circuit（eap_ig, edge_pruning, css_1.00, stable_core）CPR 全部为负，说明 ablation 后模型行为反转——可能是 binarization 阈值/top_n 选取有问题，或 node-level ablation 对稀疏 circuit 不够精确。`acdc` 和 `css_0.33` 因包含几乎全部 edge 而 CPR=1.0（trivially faithful）。

---
