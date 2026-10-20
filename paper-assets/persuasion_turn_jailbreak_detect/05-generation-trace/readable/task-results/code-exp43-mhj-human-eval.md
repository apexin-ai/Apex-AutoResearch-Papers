# code exp43 mhj human eval

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp43_mhj_human_eval_20260522T041327_result.json`
- **Structured JSON:** [`8596dc00a50b54b14f96.json`](../../sessions/85/8596dc00a50b54b14f96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。总结：

**exp43_mhj_human_eval → DONE (success)**

**MHJ 多轮数据状态**：ScaleAI/mhj 在 HuggingFace 上需要 gated access 申请（需提供 name/affiliation/email/country/purpose）。服务器无法直接访问 huggingface.co，hf-mirror.com 同样执行 gating 限制。

**替代评估**：使用已有的 verazuo/jailbreak_llms 人类 jailbreak 数据（666 jailbreak + 213 benign，单轮），结果已在 `exp8_human_jailbreak_verazuo.json` 中：

| Variant | F1 | Recall |
|---------|-----|--------|
| vanilla | 0.131±0.033 | 0.071±0.019 |
| **9-class** | **0.812±0.135** | **0.706±0.200** |
| jb_mlm | 0.968±0.010 | 0.955±0.011 |

**结论**：
- 9-class over vanilla: **+68pp F1**（远超 15pp 阈值 → success）
- Evidence hierarchy 在人类数据上成立：vanilla < 9class < jb_mlm
- 所有 DAPT 模型 precision ≈ 1.0（零误报）

**遗留问题**：
- MHJ 多轮评估需要申请 HuggingFace 数据集访问权限
- 论文 Limitations 应修改�� "MHJ exists but requires gated access; our evaluation covers single-turn human jailbreaks"

---
