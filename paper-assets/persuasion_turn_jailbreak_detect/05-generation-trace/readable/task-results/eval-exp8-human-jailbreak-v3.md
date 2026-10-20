# eval exp8 human jailbreak v3

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp8-human-jailbreak-v3_20260518T164902_result.json`
- **Structured JSON:** [`2262a433025da682dbad.json`](../../sessions/22/2262a433025da682dbad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和 artifact 已更新。汇总结果：

## Exp8: 人类越狱数据评估结果 (verazuo/jailbreak_llms)

**数据**: 666 human jailbreak prompts (Reddit/Discord) + 213 benign (plan_002 first-turn)，单轮评估

| Variant | Seeds | F1 (mean±std) | Precision | Recall | Accuracy |
|---------|-------|---------------|-----------|--------|----------|
| **jb_mlm** | 3 | **0.968±0.010** | 0.982±0.012 | 0.955±0.011 | 0.952±0.015 |
| binary | 3 | 0.929±0.037 | 1.000±0.000 | 0.869±0.065 | 0.901±0.049 |
| wiki_mlm | 3 | 0.897±0.093 | 0.972±0.024 | 0.849±0.158 | 0.865±0.110 |
| scrambled | 2 | 0.861±0.022 | 1.000±0.000 | 0.756±0.034 | 0.815±0.026 |
| 9class | 3 | 0.812±0.135 | 1.000±0.000 | 0.706±0.200 | 0.777±0.152 |
| topic | 3 | 0.758±0.082 | 0.927±0.049 | 0.644±0.092 | 0.694±0.090 |
| vanilla | 3 | 0.131±0.033 | 0.939±0.022 | 0.071±0.019 | 0.292±0.012 |

### 结论

**Evidence hierarchy 在人类数据上成立。** 核心发现：

1. **vanilla 彻底崩溃** (F1=0.131)：未经领域适配的 DeBERTa 对人类越狱几乎完全失效，确认领域适配是必要条件
2. **所有领域适配变体 >> vanilla**：即使训练数据全部由 Qwen3-8B 生成，模型仍能泛化到人类写的 jailbreak prompts，**single-LLM confound 不能解释 evidence hierarchy**
3. **jb_mlm 表现最强** (F1=0.968±0.010)：在人类数据上 MLM 域适配甚至优于分类微调，且方差最低
4. **9class 方差较大** (0.656~0.986)：seed 敏感性在更难的分布外数据上被放大

这直接反驳了审稿人的质疑：如果 cross-attack generalization 只是 within-LLM stylistic generalization，那么在人类文本上应该完全失效。实际结果显示所有适配变体在人类数据上仍保持 F1>0.75。

---
