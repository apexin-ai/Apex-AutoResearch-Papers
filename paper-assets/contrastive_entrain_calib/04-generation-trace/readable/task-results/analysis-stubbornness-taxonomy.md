# analysis stubbornness taxonomy

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stubbornness-taxonomy_20260520T194523_result.json`
- **Structured JSON:** [`0867065624a048739287.json`](../../sessions/08/0867065624a048739287.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇报结果：

---

## Stubbornness Taxonomy 分析结果 — exp-008v3 ckpt-500

**181 个 valid_correction 样本全部 stubborn (ToF=0.0)**，分为以下类型：

| 类型 | 数量 | 占比 | 说明 |
|------|------|------|------|
| (a) Deliberate Inconclusive | 52 | 28.7% | 提到正确答案但不 commit |
| (b) Acknowledge but Maintain | 43 | 23.8% | 用 however/but 敷衍后维持原答案 |
| (c) Surface Compliance | 44 | 24.3% | 用 "you're right" 等礼貌用语假装接受 |
| (d) Refute User | 3 | 1.7% | 主动论证用户是错的 |
| (e) Deliberate but Ignore | 3 | 1.7% | 推理但完全不提正确答案 |
| (f) Genuine Accept (eval missed) | 34 | 18.8% | 高 NLI entailment，可能真的接受了 |

### 5 个关键发现

1. **0% 完全忽略** — 模型永远在"回应"用户，只是不改答案
2. **Deliberation trap (29%)** — 模型知道正确答案但无法 commit，陷入无尽推理
3. **Surface compliance (24%)** — *sycophantic stubbornness*：表面同意 + 实质不改，论文新概念
4. **Evidence strength gradient** — 弱证据→表面顺从(39%)；强证据→显式 hedging(54%)。模型会根据证据强度调整*拒绝方式*，但从不接受
5. **Format corruption** — GRPO 训练导致模型以 chain-of-thought 格式输出（87% 以 "Ah, interesting" 开头），96% 回复在 512 token 处被截断，推理永远无法终结

### 预期外模式

- **Surface compliance** 是原始 taxonomy 中没有预料到的类型，是 sycophancy 和 stubbornness 的交叉：模型同时展现谄媚(说 "you're right") 和固执(不改答案)
- 34 个 case (18.8%) 有高 NLI entailment，eval 可能漏判了部分真正接受的 case
- **无单纯 "refute"** — 仅 1.7% 直接反驳用户，说明 stubbornness 主要通过*passive* 方式实现

### 产出文件

`/root/contrastive_entrain_calib/results/mechanistic_analysis/stubbornness_taxonomy/`
- `taxonomy_summary.json` — 完整统计（含 domain/evidence_strength 交叉分布、truncation 分析）
- `case_examples.json` — 181 个 case 的完整对话 + 分类标签
- `paper_examples.md` — 5 个典型案例，格式化为论文 Appendix

---
