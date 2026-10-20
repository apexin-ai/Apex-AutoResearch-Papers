# analysis completed evals 3B instruct

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_completed-evals-3B-instruct_20260515T051406_result.json`
- **Structured JSON:** [`cd8284e474409eaaf2e6.json`](../../sessions/cd/cd8284e474409eaaf2e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 实验完成状态
| 实验 | 状态 | 4 benchmarks |
|------|------|-------------|
| 3B d025 para_aligned | ✅ .done | MMLU/GSM8K/ARC/HumanEval 全部完成 |
| 3B d100 aligned_v2 | ✅ JSON完整 | MMLU/GSM8K/ARC/HumanEval 全部完成 |
| 0.5B-Instruct | ✅ JSON完整 | MMLU/GSM8K/ARC/HumanEval 全部完成 |

### 核心指标

| Model | MMLU | GSM8K | ARC | HumanEval |
|-------|------|-------|-----|-----------|
| **3B d000 aligned** | .6295 | .3525 | .8183 | .098 |
| **3B d025 para** | .6210 | .5482 | .8106 | .115 |
| **3B d100 aligned** | .6320 | **.7415** | .8242 | .171 |
| **3B d100 para** | .6590 | .5833 | .8092 | .115 |
| **0.5B d000 aligned** | .3979 | .3692 | .4693 | .110 |
| **0.5B d100 aligned** | .2334 | .3654 | .2944 | .000 |
| **0.5B Instruct** | .2462 | .3882 | .2816 | .000 |

### 关键发现

**1. 3B 规模 contamination effect 巨大且集中在 GSM8K**
- d100 vs d000: GSM8K +39pp，MMLU/ARC 几乎不变
- 说明 3B 模型有足够 capacity 从 contaminated SFT 中 memorize GSM8K 解题模式

**2. Paraphrase gap 验证了 contamination signal**
- GSM8K 净 paraphrase gap (d100-d000) = +9.5pp
- 其他 benchmark 净 gap 接近 0，符合预期（MMLU/ARC 未被 contaminate）

**3. 0.5B: Instruct ≈ d100，RL 无法修复 SFT 损伤**
- d100 contamination 在 0.5B 上反而 hurt MMLU (-16.5pp) 和 ARC (-17.5pp)
- Instruct(SFT+RL) 与 d100 表现几乎一致 → RL 后训练不改变 contamination signal pattern
- 对比 3B：模型 capacity 决定 contamination 是 help 还是 hurt

**4. 缺失数据**
- 3B d025 aligned（非 paraphrased）eval 未完成，只有 eval.log → 无法计算 d025 的 paraphrase gap

Registry 和 artifact 均已更新。

---
