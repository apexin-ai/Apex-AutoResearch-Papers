# analysis stag rate and struct gb verification

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stag-rate-and-struct-gb-verification_20260515T021223_result.json`
- **Structured JSON:** [`039069eaa274eabe0bfb.json`](../../sessions/03/039069eaa274eabe0bfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Reproduction complete. Now I have all the data needed for the final report.

```
=== PART 1: OH STAG RATE ===

windows_labeled.jsonl (source: /root/autodl-tmp/openhands_data/windows_labeled.jsonl):
  Total: 154,743
  Stag (majority_label=0): 31,440
  Prog (majority_label=1): 119,212
  Abstain (confidence=0): 4,091
  Non-abstain: 150,652
  Rate stag/total:          31,440 / 154,743 = 20.32%
  Rate stag/(stag+prog):   31,440 / 150,652 = 20.87%
  Confidence dist: {0: 4091, 1: 107276, 2: 42374, 3: 1002}
  conf≥2 subset: N=43,376, stag=8,626, rate=19.89%

embeddings_fixed.pt (source: /root/autodl-tmp/openhands_data/embeddings_fixed.pt):
  Total: 143,057
  Stag: 30,684
  Prog: 112,373
  Rate: 30,684 / 143,057 = 21.45%
  Confidence dist: {1: 99691, 2: 42364, 3: 1002}
  conf≥2: N=43,366, stag=8,616, rate=19.87%

差异原因:
  JSONL non-abstain (150,652) vs embeddings (143,057) → 差 7,595 windows
  这些是 short_trajectory=True 的窗口，embedding 阶段被过滤掉（短轨迹不做 embedding）
  JSONL stag 31,440 vs emb stag 30,684 → 差 756（短轨迹中的 stag 窗口）
  conf≥2: JSONL 43,376 vs emb 43,366 → 差 10（边缘 case）

论文报告的 21.4% 来源: embeddings_fixed.pt 的 30,684/143,057 = 21.4488%
  这是排除 abstain 和 short_trajectory 后的口径
  论文表 1 写 "150,652 windows, stag 21.4%" — 窗口数用 non-abstain 口径，stag rate 用 embeddings 口径
  严格来说不一致：non-abstain 口径的 stag rate 是 20.87%，不是 21.4%
  21.4% 是 embeddings 口径（143,057 windows），如果要和 150,652 配对则应写 20.9%

所有实验使用的数据源:
  - Structural baselines: 直接从 JSONL 提取特征，使用 150,652 non-abstain（OH all）或 43,376 conf≥2
  - Probe/embedding 实验: 使用 embeddings_fixed.pt（143,057 windows）
  - 两个数据源的 conf≥2 子集几乎完全一致（43,376 vs 43,366，差 10）

=== PART 2: STRUCTURAL GB CONF≥2 ===

已找到的所有 structural conf≥2 数字及来源:

0.9919 来源:
  文件: cross_agent_structural_results.json (单 seed=42)
  脚本: cross_agent_structural_baseline.py
  超参: GB(n=200, lr=0.05, depth=5), seed=42
  训练: SWE conf≥2 train split, N=10,634 (stag=3,894, prog=6,740)
  测试: OH conf≥2, N=43,376
  → 同时被 multiseed 文件验证: 5-seed mean=0.9918±0.0007

0.9959 来源:
  文件: cross_agent_structural_results.json (单 seed=42)
  模型: RF(n=100, depth=10), 不是 GB
  同样训练/测试配置，RF 在 conf≥2 上比 GB 更高
  → 3-seed mean=0.9959±0.0012

0.9949 来源:
  文件: structural_on_twv_results.json
  路径: cross_agent → mv_train → oh_conf2 → GB
  脚本: structural_on_twv.py
  超参: GB(lr=0.05), 但 RF 用 n=200（vs 上面的 n=100）
  训练: SWE 全量 train split（mv 标签），可能与上面的 split 不完全一致
  差异原因: 不同的 train/test split 或略不同的训练集组成

0.9984:
  这不是 macro_f1，是 RF conf≥2 的 f1_progress（单 seed=42）

0.950 最接近的匹配:
  GB on OH all-windows f1_stag = 0.9479 ≈ 0.948（不是 conf≥2）
  或 structural_on_twv: twv_train → oh_conf2 → LR macro_f1 = 0.9674（不匹配）
  没有找到精确匹配 0.950 的 structural GB conf≥2 数字

Canonical 复现结果 (seed=42, 从头跑):
  GB: macro_f1=0.9919, accuracy=0.9949, f1_stag=0.9869, f1_prog=0.9968
       errors=223/43,376, CM: [[8421, 205], [18, 34732]]
  RF: macro_f1=0.9959, accuracy=0.9974, f1_stag=0.9935, f1_prog=0.9984
       errors=113/43,376, CM: [[8625, 1], [112, 34638]]
  训练: SWE conf≥2 train split N=10,634
  测试: OH conf≥2 N=43,376
  超参: GB(n_estimators=200, lr=0.05, max_depth=5), RF(n_estimators=100, max_depth=10)

可复现的权威数字:
  Structural GB on OH conf≥2: 0.9918 ± 0.0007 (5 seeds) / 0.9919 (seed=42, 今日复现确认)
  Structural RF on OH conf≥2: 0.9959 ± 0.0012 (3 seeds) / 0.9959 (seed=42, 今日复现确认)
  论文 Table 2 当前写: GB=0.9918, RF=0.9959 — 与复现一致，无需修改

注意: 论文表 1 "150,652 windows, stag 21.4%" 有口径不一致。
  如果用 150,652 windows，stag rate 应为 20.9%（31,440/150,652）
  如果要报 21.4%，对应窗口数应为 143,057（embeddings 口径，排除 short_trajectory）
  建议统一为一个口径。
```

---
