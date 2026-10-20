# analysis exp69 mixed llm aa error

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp69_mixed_llm_aa_error_20260523T230252_result.json`
- **Structured JSON:** [`43c24fe8505bf1814b66.json`](../../sessions/43/43c24fe8505bf1814b66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## exp69 Mixed-LLM ActorAttack Error Analysis 结论

**F1=0.504 的根因是 recall 极低，不是 precision 问题：**

| | Precision | Recall | Avg FP | Avg FN |
|---|---|---|---|---|
| Jailbreak | 97.8% | **29.2%** | 0.3 | **56.7** |

- 几乎所有错误都是 **FN（漏检 jailbreak）**，FP 接近于零
- Recall 在 seed 间差异巨大（17.5% ~ 48.8%），模型行为不稳定

**关键对比：**
- 单源 9-class AA F1 = 0.972（recall ~96%）→ 混合训练后 F1 = 0.504（recall ~29%），**delta = -0.468**
- 混合训练的 9-class 在 AA 上的 recall 水平（29%）接近于单源 **vanilla**（无策略监督）的水平（1.3%），说明策略监督的增益被混合训练大幅削弱
- 跨 OOD 对比：FITD 不受影响（F1=0.997），DD 中等影响（F1=0.818），**AA 受损最严重**

**根因假设：**
ActorAttack 依赖 role-play 和 persona-switching 等风格化策略模式，这些模式在不同 LLM 之间表达差异大。混合训练引入的分布噪声破坏了模型对这些策略的判别能力。FITD 的 false information injection 模式更依赖内容而非风格，因此对 LLM 来源不敏感。

输出文件在服务器 `results/rebuttal/mixed_llm_error_analysis/`（error_analysis.json + analysis_summary.md）。Registry 已更新为 DONE。

---
