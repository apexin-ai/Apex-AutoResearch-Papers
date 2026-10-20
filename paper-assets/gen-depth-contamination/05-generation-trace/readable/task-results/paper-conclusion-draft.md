# paper conclusion draft

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_conclusion_draft_20260514T012904_result.json`
- **Structured JSON:** [`f9a12c0076b2ccb89fbc.json`](../../sessions/f9/f9a12c0076b2ccb89fbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。conclusion.tex 已重构为 3+1 结构，编译无 warning：

- **Para 1 (K\*=2)**：8/8 conditions 统一验证，bootstrap CI + permutation test 统计显著性，Qwen-cont CI lower=0.6015 最边缘，0v1 >0.99 → 1v2 0.6112–0.7039 的 ~30pp 骤降
- **Para 2 (OBD 框架)**：15D features + LightGBM，跨模型迁移 80–92%（Pythia↔OLMo 91–92%），ρ≥0.85 特征退化一致性，GPT-5.5/Claude ~33% vs OBD 38.6%
- **Para 3 (C3 graduated filtering)**：三级分类法占位，TODO 待 exp-006 结果填充
- **Para 4 (limitations + future work)**：模型规模/语言/retrain-chain/few-shot/learned representations

所有定量 claim 均附 exp\_id 来源注释（LaTeX comments），数字与 registry 一致。

---
