## Scorer A+C 实现报告

### 改动
- `__init__` 新增 `alpha=0.5`, `fallback_threshold=0.2`
- NORMAL模式 (ratio≥0.2): `score = Σw(satisfied∩traces) - α·Σw(excluded∩traces)`
- FALLBACK模式 (ratio<0.2): `score = -Σw(excluded∩traces)`
- 向后兼容，pipeline.py零改动

### P5 原始 vs 新评分
| | OLD | NEW (A+C) |
|---|---|---|
| "80" | 0.0 | **-3.0** (最小负暴露) |
| "120" | 4.0 | -28.0 |
| "100" | 0.0 | -19.0 |
| 选中 | 120 (错) | **80 (对)** |

Fallback在satisfied_ratio=0.048时启动。

### 回归测试 6/6 PASS
### rescore_all.py 就绪（--input summary模式 / --full 完整重打分模式）
### source_traces映射确认无bug