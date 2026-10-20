# CWM Multi-Seed Data Fill Checklist

Generated: 2026-05-21
Purpose: 当 CWM repo-level multi-seed 数据到齐后，按此清单逐项更新论文文字和数字。

---

## Priority Legend

- **MUST_CHANGE** — 提交前必须更新，否则有 \tbd{} 或 "in progress" 残留
- **SHOULD_UPDATE** — 改了论文更强，但不改不会 block submission
- **CHECK_NUMBERS** — 验算是否受影响，可能不需要改

---

## MUST_CHANGE (9 locations)

### 1. experiments.tex L111 — Table 3 caption
```
当前: "CWM multi-seed runs in progress."
改为: 删除 "in progress"，写入 CWM seed 数（如 "CWM: N seeds"）
```

### 2-3. experiments.tex L120-121 — Table 3 \tbd{} cells
```
当前: Qwen3-8B CWM = \tbd{}, DeepSeek CWM = \tbd{}
改为: 填入 mean ± std（per-test 和 variant-level）
```

### 4. experiments.tex L135 — §4.3 主结果段
```
当前: "gap is 25.59pp at 4B (CLS 83.63% vs. CWM 58.04%, seed 42)
        and 19.31pp at 8B (84.48% vs. 65.17%)"
        "single-seed design and multiple confounds preclude definitive causal attribution"
改为: 8B CWM 换成 multi-seed mean; 19.31pp 重算; 删除 "single-seed design" confound
```

### 5. experiments.tex L161 — Complexity as moderator段
```
当前: "CLS-CWM gap widens from 1--3pp (function) to 19--26pp (repo)"
改为: 更新 19--26pp 范围（如果 multi-seed 改变了区间）
```

### 6. abstract.tex L4 — 19--26pp gap
```
当前: "the CLS-CWM gap widens to 19--26pp in single-seed variant-level evaluation"
改为: 删除 "single-seed"; 更新范围; 加 "across N seeds" / "mean ± std"
```

### 7. introduction.tex L15 — Contribution #2
```
当前: "diverge by 19--26pp ... though gap magnitude depends on single-seed evaluation
        and multiple confounds"
改为: 更新范围; 删除 "single-seed evaluation" caveat
```

### 8. conclusion.tex L4 — 主结论
```
当前: "robust interaction (z=-23.7) confirms divergence (19--26pp, single-seed
        variant-level), with CWM falling below majority baseline"
改为: 删除 "single-seed variant-level"; 更新范围
```

### 9. conclusion.tex L8 — Limitations 段
```
当前: "Most repo-level comparisons use a single seed; the gap magnitude (19--26pp)
        exceeds any single assessed confound"
改为: 更新为 multi-seed 已完成; 调整 seed 数描述; 更新 DeepSeek seed 数
```

---

## SHOULD_UPDATE (6 locations)

### 10. introduction.tex L17 — Contribution #3 oracle
```
当前: "oracle routing reaches 95.83% variant accuracy (+14.58pp; single-seed)"
改为: 加 "(N seeds)" 或 multi-seed oracle 结果（如果重跑了 oracle）
```

### 11. experiments.tex L182 — Threats to Validity 开头
```
当前: "limited seeds mean definitive causal attribution requires multi-seed replication"
改为: multi-seed 完成后改为 "multi-seed replication confirms..."
```

### 12. main.tex L54 — Figure 2 caption
```
当前: "gap widens to 19--26pp with CWM falling below majority baseline"
改为: 更新范围（与正文一致）
```

### 13. checklist.tex L11 — A1 limitations 答案
```
当前: "discusses val-best checkpoint selection variance and single-seed constraints"
改为: 更新为 multi-seed 已解决 single-seed 约束
```

### 14. appendix.tex L234 — Data processing note
```
当前: "DeepSeek CWM seeds use train_unified.py... Qwen CWM seeds use train_repo_cwm.py"
改为: 确认 multi-seed runs 使用了同一脚本；如有变化需更新
```

### 15. appendix.tex L442 — CWM scale and pretraining threat
```
当前: "all repo-level CWM conclusions are conditional on the ≤8B LoRA regime"
改为: multi-seed 后可能需要调整强度词（这条限制仍成立但语气可能变）
```

---

## CHECK_NUMBERS (4 locations)

### 16. experiments.tex L137 — Checkpoint selection confound
```
当前: "DeepSeek CWM's val-selected checkpoint (56.70%) underperforms its epoch-3
        checkpoint (61.49%), widening the apparent gap"
检查: multi-seed 是否用了 val-best checkpoint; 如果 multi-seed val-best 表现正常，
      此段可能需要删除或弱化
```

### 17. conclusion.tex L4 — CWM recommendation
```
当前: "CLS is recommended for throughput; behavior at larger scale remains open"
检查: multi-seed CWM 如果大幅缩小 gap（<10pp），推荐语气需要修改
```

### 18. appendix.tex L436 — Eval seq length threat
```
当前: "64.36%→65.17%, unparseable 63.7%→74%"
检查: 这些是 single-seed 诊断数据；multi-seed 是否改变 pattern
```

### 19. 全文 19--26pp 范围重算
```
当前范围来源: Qwen3-4B s42=25.59pp, Qwen3-8B s42=19.31pp
multi-seed 后: 用 Qwen3-8B CLS mean - CWM mean 重算 8B gap;
               如果 CWM mean 变化，范围可能变（如 17--26pp 或 21--26pp）
需要同步更新的位置: abstract, intro L15, experiments L60/L135/L161, conclusion L4/L8,
                    main.tex L54 (Figure 2 caption)
```

---

## Data Fill Workflow

当 CWM multi-seed 实验全部 DONE 时：

1. 从 registry 提取所有 CWM repo-level 结果（per-test accuracy, variant-level accuracy）
2. 计算 mean ± std
3. 重算 CLS-CWM gap range（8B: CLS_mean - CWM_mean; 4B: 保持 s42 数据）
4. 按 MUST_CHANGE → SHOULD_UPDATE → CHECK_NUMBERS 顺序逐项更新
5. 全文 grep "19--26" 确认范围一致
6. 全文 grep "single.seed|single seed" 确认无残留
7. 编译 + 8 页检查
