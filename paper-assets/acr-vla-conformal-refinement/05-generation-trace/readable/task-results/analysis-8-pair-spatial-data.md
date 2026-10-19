# analysis 8 pair spatial data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8-pair-spatial-data_20260524T220019_result.json`
- **Structured JSON:** [`b617560fbd1f15031ab7.json`](../../sessions/b6/b617560fbd1f15031ab7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Spatial 8-pair 完整原始数据表

```
seed | VLA-only SR | Adaptive SR | Δ       | VLA-only exp_id                  | Adaptive exp_id                       | 备注
s42  | 80.0%       | 82.0%       | +2.0pp  | eval-supp-spatial-vla-only-s42   | eval-supp-adapt-tau025-spatial-s42-r2 | K=10, 干净supp
s43  | 79.0%       | 80.0%       | +1.0pp  | eval-supp-spatial-vla-only-s43   | eval-supp-adapt-tau025-spatial-s43    | K=10, 干净supp
s44  | 78.5%       | 80.5%       | +2.0pp  | eval-supp-spatial-vla-only-s44   | eval-supp-adapt-tau025-spatial-s44    | K=10, 干净supp
s45  | 77.0%       | 80.0%       | +3.0pp  | eval-supp-spatial-vla-only-s45   | eval-supp-adapt-tau025-spatial-s45    | K=10, 干净supp; 154/200
s46  | 80.5%       | 80.0%       | -0.5pp  | eval-supp-spatial-vla-only-s46   | eval-supp-spatial-adapt-tau025-s46    | ⚠️ K=2 (其余seed K=10)
s47  | 80.0%       | 81.5%       | +1.5pp  | eval-supp-vla-only-spatial-s47   | eval-supp-adapt-tau025-spatial-s47    | K=10; VLA 160/200
s48  | 79.5%       | 81.0%       | +1.5pp  | eval-supp-vla-only-spatial-s48   | eval-supp-adapt-tau025-spatial-s48    | K=10; status=PREPARING但metrics已有
s49  | 78.5%       | 82.0%       | +3.5pp  | eval-supp-vla-only-spatial-s49   | eval-supp-adapt-tau025-spatial-s49    | K=10; status=PREPARING但metrics已有
```

**统计检验**：

| 配置 | n | Δ(mean) | t-stat | paired t p-value | Wilcoxon p |
|------|---|---------|--------|-----------------|------------|
| 全 8 seeds (含 s46 K=2) | 8 | +1.750pp | 4.041 | **0.0049** | 0.0156 |
| 排除 s46 (K=10 一致) | 7 | +2.071pp | 6.183 | **0.0008** | 0.0156 |

**关键注释**：
- `p=0.0049` 数值可复现（上述 n=8 数据）
- `paper_framing.md` 标记该值"废弃"，原因是 s46 用 K=2 vs 其余 K=10 不一致
- 论文主报告推荐用 n=7 (p=0.0008)，脚注中补充 n=8 robustness (p=0.0049)
- s45 VLA-only 有两个 run（77% vs 80%），表中采用 77%（`eval-supp-spatial-vla-only-s45`）
- s47 VLA-only 有两个 run（81% vs 80%），表中采用 80%（`eval-supp-vla-only-spatial-s47`）

---
