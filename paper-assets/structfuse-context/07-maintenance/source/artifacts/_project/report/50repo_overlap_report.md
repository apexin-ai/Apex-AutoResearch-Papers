# 50-Repo Overlap Experiment Results

## Summary Statistics

| Metric | Value |
|--------|-------|
| 总 instances | 240 |
| CodeQL 成功率 | 154/240 (64.2%) |
| 有 connected-but-not-gold 的 instances | 98/240 (**Z = 40.8%**) |
| 平均 \|connected\| per instance | 6.0 |
| 平均 \|connected - gold\| per instance | 6.0 |
| CodeQL timeout/fail 率 | 2/50 repos (4.0%) |

## 按 repo 大小分组

| 分组 | Instances | has_extra | Rate | avg_connected | avg_extra |
|------|-----------|-----------|------|---------------|-----------|
| 小 (<50 files) | 140 | 54 | 38.6% | 2.5 | 2.5 |
| 中 (50-200) | 70 | 39 | 55.7% | 11.8 | 11.8 |
| 大 (>200) | 30 | 5 | 16.7% | 8.8 | 8.8 |

## 决策门

- **Z = 40.8% ≥ 20% → 原方法可行** ✓
- CodeQL timeout 率 4.0% < 30% → 2-hop 无需降级 ✓

## Notes

- avg_connected ≈ avg_extra because SWE-smith gold = single buggy file, so any connected file ≠ buggy file is automatically "extra"
- 大 repo 成功率低（16.7%）主要因为 pandas 和 markupsafe DB 创建失败被跳过，加上 pyparsing 154 files 但 0 connected
- 中型 repo 表现最好（55.7%），说明方法对中等复杂度项目效果最佳
- 2 个 DB 创建失败: pallets/markupsafe (rc=2), pandas-dev/pandas (rc=32/timeout)

## Server & Paths

- Server: cqa1-21977 (root)
- Results: /root/autodl-tmp/structfuse/50repo_results/
  - summary.json
  - detailed_results.jsonl
- Script: /root/structfuse/scripts/run_50repo_overlap.py
- Metadata: /root/autodl-tmp/swe_smith_metadata_fixed.jsonl
