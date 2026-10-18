# verify tab7 fix data

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_tab7-fix-data_20260523T194255_result.json`
- **Structured JSON:** [`a853bc18047e07529671.json`](../../sessions/a8/a853bc18047e07529671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部获取。以下是完整对照表。

---

## Tab 7 (Normalized Effect Size) 全 Cell 对照

### 数据源
- **论文**: `appendix.tex` lines 229–237, `\label{tab:normalized_es}`，标注为 "1.3B h3-1 on LAMBADA"
- **h3-1**: `jaccard_upper_bound.json` → `per_ratio.h3-1`（permutation_10k validated）
- **h12-1**: `jaccard_upper_bound.json` → `per_ratio.h12-1`（analytical J_null）

### Helped

| Cell | 论文当前值 | h3-1 正确值 | h12-1 值 | 判断 |
|------|-----------|------------|---------|------|
| GDN–RetNet J_obs | **.086** | .092 | .087 | **错误** — 接近 h12-1，非 h3-1 |
| GDN–RetNet J_max | .922 | .922 | .920 | h3-1 ✓ |
| GDN–RetNet J_null | **.048** | .045 | .045 | **错误** — 两者都是 .045，.048 无来源 |
| GDN–RetNet Norm ES | **.044** | .054 | .047 | **错误** — 因 J_obs/J_null 都错导致 |
| GDN–HGRN2 J_obs | **.099** | .100 | .098 | **微差** — h3-1 为 0.100218→.100 |
| GDN–HGRN2 J_max | .843 | .843 | .906 | h3-1 ✓ |
| GDN–HGRN2 J_null | **.050** | .051 | .050 | **微差** — h3-1 为 0.051056→.051 |
| GDN–HGRN2 Norm ES | .062 | .062 | .056 | h3-1 ✓ |
| RetNet–HGRN2 J_obs | .108 | .108 | .101 | h3-1 ✓ |
| RetNet–HGRN2 J_max | .777 | .777 | .834 | h3-1 ✓ |
| RetNet–HGRN2 J_null | **.042** | .049 | .047 | **错误** — 两者都不匹配，.042 无来源 |
| RetNet–HGRN2 Norm ES | **.090** | .081 | .068 | **错误** — 因 J_null 错导致 |
| *Mean J_obs* | *.098* | *.100* | — | *微差* |
| *Mean J_max* | *.847* | *.848* | — | *微差* |
| *Mean J_null* | *.047* | *.048* | — | *微差* |
| *Mean Norm ES* | **.065** | *.066* | — | *微差（但由错误 cell 平均出来恰好接近）* |

### Hurt

| Cell | 论文当前值 | h3-1 正确值 | h12-1 值 | 判断 |
|------|-----------|------------|---------|------|
| GDN–RetNet J_obs | **.092** | .103 | .087 | **错误** — 两者都不匹配，差距大 |
| GDN–RetNet J_max | .805 | .805 | .930 | h3-1 ✓ |
| GDN–RetNet J_null | .056 | .056 | .050 | h3-1 ✓ |
| GDN–RetNet Norm ES | **.048** | .063 | .042 | **错误** — 因 J_obs 错 |
| GDN–HGRN2 J_obs | **.070** | .088 | **.070** | **错误** — 完全匹配 h12-1！ |
| GDN–HGRN2 J_max | .642 | .642 | .811 | h3-1 ✓ |
| GDN–HGRN2 J_null | **.043** | .049 | .047 | **错误** — 两者都不匹配 |
| GDN–HGRN2 Norm ES | **.045** | .066 | .031 | **错误** — J_obs 和 J_null 都错 |
| RetNet–HGRN2 J_obs | .087 | .087 | .085 | h3-1 ✓ |
| RetNet–HGRN2 J_max | .798 | .798 | .872 | h3-1 ✓ |
| RetNet–HGRN2 J_null | **.050** | .045 | .045 | **错误** — 两者都是 .045 |
| RetNet–HGRN2 Norm ES | **.049** | .056 | **.049** | **错误** — 匹配 h12-1 |
| *Mean J_obs* | *.083* | *.093* | — | **错误** |
| *Mean J_max* | *.748* | *.748* | — | *正确* |
| *Mean J_null* | *.050* | *.050* | — | *正确* |
| *Mean Norm ES* | **.047** | *.062* | — | **错误** |

### 总结

**24 个数据 cell（不含 Mean），其中：**
- **正确（匹配 h3-1）**: 10 个 — 所有 J_max (6) + 4 个其他
- **错误**: 14 个 — 分布在 J_obs (5)、J_null (5)、Norm ES (4)

**确认 h12-1 混入的 cell（精确匹配）**:
- GDN–HGRN2 hurt J_obs: 论文 .070 = h12-1 .070（h3-1 应为 .088）
- RetNet–HGRN2 hurt Norm ES: 论文 .049 = h12-1 .049（h3-1 应为 .056）
- GDN–RetNet helped J_obs: 论文 .086 ≈ h12-1 .087（h3-1 应为 .092）

**无来源的异常值（既不匹配 h3-1 也不匹配 h12-1）**:
- J_null 列有 4 个 cell 数值无法追溯到任何 ratio 的数据，可能来自更早版本的分析脚本或手动录入错误

**h3-1 正确值（用于替换论文 Tab 7）**:

```
Helped & GDN--RetNet   & .092 & .922 & .045 & .054 \\
       & GDN--HGRN2    & .100 & .843 & .051 & .062 \\
       & RetNet--HGRN2  & .108 & .777 & .049 & .081 \\
       & Mean           & .100 & .848 & .048 & .066 \\
Hurt   & GDN--RetNet   & .103 & .805 & .056 & .063 \\
       & GDN--HGRN2    & .088 & .642 & .049 & .066 \\
       & RetNet--HGRN2  & .087 & .798 & .045 & .056 \\
       & Mean           & .093 & .748 & .050 & .062 \\
```

---
