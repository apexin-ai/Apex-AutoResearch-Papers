# code mvp 001 freq merging

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-001-freq-merging_20260511T185944_result.json`
- **Structured JSON:** [`3a9af30fa33cbc7a6be9.json`](../../sessions/3a/3a9af30fa33cbc7a6be9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成，13 秒。结果：

```
=== Binary Frequency Merging ===
N=1 (greedy):     P=43.6       R=40.6       F1=42.05

N=4:   k=1 union    F1=42.10±0.87 | k=2 F1=42.32±0.14 | k=3 F1=41.87 | k=4 intersect F1=40.71
N=8:   k=1 union    F1=42.04±0.29 | k=2 F1=42.71±0.59 | k=3 F1=42.67 | k=4 F1=42.65 | ... | k=8 F1=40.21
N=16:  k=1 union    F1=41.32±0.14 | ... | k=5 F1=42.70±0.16 (best@16) | ... | k=16 F1=39.29

=== Weighted IoU Frequency Merging ===
Best: N=8, k=3, F1=42.18±0.18

=== Best Configs ===
Binary:   N=8, k=2, F1=42.71±0.59
Weighted: N=8, k=3, F1=42.18±0.18
Greedy:   F1=42.05

=== Pass/Fail ===
merging@N≥8 > greedy ≥ 1.0pt? NO
```

**结论**：

- Binary frequency merge 最佳配置 N=8, k=2 只比 greedy 高 **+0.66 F1**，未达到 1.0pt 阈值
- Weighted IoU merge 反而更差（42.18 vs 42.71），IoU 聚类可能把不该合并的 entity 合到一起，导致选出的代表 text 不匹配 gold
- k=1 (union) 拉高 recall 但 precision 严重下降；k=N (intersection) 反之。Sweet spot 在 k=2~5 区间
- 即使是 oracle-optimal k，频率合并的增益也很有限——根因是 entity 多样性太高，即使按频率筛选也无法有效聚焦

**产出**：
- 脚本：`/root/projects/verifier-tts-struct-ie/scripts/frequency_merge.py`
- 结果：`/root/projects/verifier-tts-struct-ie/results/frequency_merge_results.json`

---
