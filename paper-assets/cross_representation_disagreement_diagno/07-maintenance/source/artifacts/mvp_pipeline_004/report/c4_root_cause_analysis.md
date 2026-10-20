# C4 Excl-Unknown Root Cause Analysis (125 samples)

## evaluate_mvp.py 完整输出

```
Total samples: 125 | Valid: 125 | Effective (both executed): 117 | GT!=Unknown: 82

--- All samples (both executed) ---
C1 disagree_rate:      35.9% (42/117)               [>=10%]  PASS
C2 diagnostic_rate:    88.1% (37/42)                [>=40%]  PASS
C3 error_types:        3 types                      [>=2  ]  PASS
C4 targeted_vs_blind:  +7.4pp (T:35/54 B:31/54)     [>5pp ]  PASS
C5 localization:       79.2% (19/24)                [>=60%]  PASS

--- Excluding GT=Unknown ---
C1 disagree_rate:      34.7% (26/75)                [>=10%]  PASS
C2 diagnostic_rate:    88.5% (23/26)                [>=40%]  PASS
C3 error_types:        2 types                      [>=2  ]  PASS
C4 targeted_vs_blind:  +0.0pp (T:22/35 B:22/35)     [>5pp ]  FAIL
C5 localization:       87.5% (14/16)                [>=60%]  PASS

MVP RESULT: 5/5 PASS -> PROCEED
```

## C4 按 GT 类型分组

| GT | targeted | blind | delta |
|----|----------|-------|-------|
| True (N=16) | 9/16 (56.2%) | 10/16 (62.5%) | **-6.2pp** |
| False (N=19) | 13/19 (68.4%) | 12/19 (63.2%) | +5.3pp |
| Unknown (N=20) | 14/20 (70.0%) | 10/20 (50.0%) | **+20.0pp** |

## C4 按 error_side 分组

| error_side | targeted | blind | delta | GT分布 |
|------------|----------|-------|-------|--------|
| code (N=35) | 29/35 (82.9%) | 22/35 (62.9%) | **+20.0pp** | F:13, T:8, U:14 |
| fol (N=10) | 5/10 (50.0%) | 9/10 (90.0%) | **-40.0pp** | T:6, F:2, U:2 |
| both (N=14) | 2/10 (20.0%) | 1/10 (10.0%) | +10.0pp | F:6, T:4, U:4 |

## C4 交叉表 (GT × error_side)

| GT | error_side | targeted | blind | delta |
|----|------------|----------|-------|-------|
| True | code (N=8) | 6/8 (75.0%) | 4/8 (50.0%) | +25.0pp |
| True | fol (N=6) | 3/6 (50.0%) | 6/6 (100.0%) | **-50.0pp** |
| True | both (N=4) | 0/2 (0.0%) | 0/2 (0.0%) | 0.0pp |
| False | code (N=13) | 12/13 (92.3%) | 11/13 (84.6%) | +7.7pp |
| False | fol (N=2) | 1/2 (50.0%) | 1/2 (50.0%) | 0.0pp |
| False | both (N=6) | 0/4 (0.0%) | 0/4 (0.0%) | 0.0pp |
| Unknown | code (N=14) | 11/14 (78.6%) | 7/14 (50.0%) | **+28.6pp** |
| Unknown | fol (N=2) | 1/2 (50.0%) | 2/2 (100.0%) | -50.0pp |
| Unknown | both (N=4) | 2/4 (50.0%) | 1/4 (25.0%) | +25.0pp |

## 根因结论

1. **C4 excl-unknown 在 125 样本下确认 FAIL (+0.0pp)**
2. **Targeted repair 改进并非仅集中在 Unknown-GT**——真正的分界线是 error_side：
   - **code-side 错误**：targeted 一致优于 blind（所有 GT 类型均正 delta：+25pp/+7.7pp/+28.6pp）
   - **fol-side 错误**：targeted 严重劣于 blind（-40pp 总体，GT=True 时 -50pp）
3. **根因**：GT=Unknown 样本中 code:fol 比例为 14:2，code-side 主导所以 targeted 大幅领先。GT=True 样本中 code:fol 比例为 8:6，fol-side 错误拖累使 targeted 总体落后。GT=False 的 code:fol 比例为 13:2，所以也有正 delta（+5.3pp）但被 GT=True 的负 delta 抵消。
4. **可操作方向**：修复 FOL-side targeted repair 策略（当前 50% vs blind 90%），这是 C4 excl-unknown FAIL 的直接原因。
