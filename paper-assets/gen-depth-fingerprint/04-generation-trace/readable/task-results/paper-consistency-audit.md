# paper consistency audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency-audit_20260515T211944_result.json`
- **Structured JSON:** [`be6c4472c24c7cc71b72.json`](../../sessions/be/be6c4472c24c7cc71b72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是所有发现的问题：

---

## Registry 数字不匹配

### 1. results.tex (两份) LOGO 表格 "5-gen LOGO" 行
```
文件: results.tex L46 (artifacts + docs)
问题: 当前值 "0.800" 应为 "0.802"（来源: registry volume-matched "5-gen original: 0.802"）
```

### 2. results.tex (两份) L19 cross-scale 段落
```
文件: results.tex L19 (artifacts + docs)
问题: 当前值 "+1.1\,pp to 0.811" 中 0.811 应为 0.810（来源: registry "6-gen excl qwen8b: 0.810"）
      连带影响: 改进幅度应为 0.810−0.802 = +0.8pp，非 +1.1pp
```

### 3. results.tex (两份) L20 volume-matched 分解
```
文件: results.tex L20 (artifacts + docs)
问题: "+0.05\,pp" 和 "+0.78\,pp" 合计 0.83pp，与 L19 声称的 "+1.1pp" 矛盾。
      按 registry 数字 (0.802→0.810 = 0.8pp)，整个分解数字需要重算。
```

### 4. results.tex (两份) LOGO 表格 OLMo-2-1B 行
```
文件: results.tex L40/table (artifacts + docs)
问题: OLMo-2-1B held-out F1 = "0.764"，但 discussion.tex 和 limitations.tex 
      同一模型 base F1 引用为 "0.763"，registry 也是 0.763。
      表格值 0.764 与 registry/全文其他引用不一致。
```

---

## 两份副本之间的不一致

### 5. docs/paper/table1.tex vs results.tex 内联表格 — Qwen3-8B CI
```
文件: docs/paper/table1.tex L13
问题: Qwen3-8B CI 为 [0.672, 0.698]
      但 results.tex 内联表格 (两份) CI 为 [0.668, 0.694]
      两者不一致，应统一为 [0.668, 0.694]
```

### 6. docs/paper/table2.tex — feature set 组成错误
```
文件: docs/paper/table2.tex L9
问题: Surface only 特征列为 "TTR, hapax\_ratio, entropy\_min"
      entropy\_min 是 reference-model 特征，不是 surface 特征。
      应为 "TTR, hapax\_ratio"（2 features）。
      对应地 L10 Reference only 缺少 entropy\_min。
```

### 7. artifacts discussion.tex vs docs discussion.tex — 采样范围描述
```
文件: artifacts/_project/paper/discussion.tex L9
问题: 当前值 "F1 range ${<}$0.3\,pp" 应为 "${\leq}0.3$\,pp"
      （3-class 差值 0.788−0.785 = 恰好 0.3pp，< 不正确）
      docs 版本已正确使用 ≤
```

### 8. artifacts appendix_classifier.tex vs docs 版本 — 同一问题
```
文件: artifacts/_project/paper/appendix_classifier.tex L52
问题: "differ by less than 0.3\,pp" 应为 "at most 0.3\,pp"
      docs 版本已正确使用 "at most"
```

---

## 无问题项

- **related_work.tex**: 无残留 CI width 引用 ✓
- **Binary F1 = 0.723, CI [0.717, 0.729]**: 全文一致 ✓
- **Per-gen std = 0.051**: 全文一致 ✓
- **Per-gen F1 range 0.683–0.856**: 一致 ✓
- **所有 baseline 3-class F1** (AvgLogProb 0.737, LD-Score 0.655, FastDetectGPT 0.688, Binoculars 0.417): 一致 ✓
- **Multi-detector ensembles** (0.796/0.712, 0.805/0.724): 一致 ✓
- **Ordinal comparison** (CORAL 0.771, Frank-Hall 0.793, XGBoost binary 0.721/0.728): 一致 ✓
- **Instruct 数字** (OLMo 0.338/0.763, Qwen3-0.6B 0.667/0.816, 所有 partial ρ): 一致 ✓
- **Sampling ablation 表格数字**: 一致 ✓
- **Topic drift 数字** (cos sim 0.62→0.86, tail_decay ρ=0.068/R²=0.005, entropy ρ=-0.286/R²=0.082): 一致 ✓
- **Cross-ref bias** (0.856/0.845/0.848): 一致 ✓
- **Downstream 表格所有数字**: 一致 ✓

---

**总结**: 8 处问题——4 处 registry 数字不匹配（集中在 volume-matched/cross-scale 分析），4 处两份副本间不一致。最严重的是 #1–#3（5-gen/6-gen 数字及其衍生的改进幅度声称），需要根据 registry 重新校准。

---
