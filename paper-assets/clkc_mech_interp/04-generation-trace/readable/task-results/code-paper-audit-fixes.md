# code paper audit fixes

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper-audit-fixes_20260525T185158_result.json`
- **Structured JSON:** [`cca793465e09dfa84fb1.json`](../../sessions/cc/cca793465e09dfa84fb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功。0 错误，0 警告，总计 12 页。

---

## 审计报告

### A. 源码 Critical 排查

| 检查项 | 结果 |
|--------|------|
| 占位符残留 (TODO/FIXME/XXX/TBD/PLACEHOLDER) | **0 处**，干净 |
| 内部信息泄露 (服务器名/路径/实验 ID) | **1 处注意**：abstract.tex 匿名 URL 含项目名 `clkc_mech_interp`（`anonymous.4open.science/r/clkc_mech_interp-F894/`）。位于匿名平台，风险低，但如需彻底匿名可改 repo 名 |
| 数字一致性 | **全部一致**。Table 1/2/3 数值与正文引用交叉验证通过（77.6%/75.0%/76.2% EN→EN, 88.9% Gemma probe, Δ_asym ~7pp, steering p-values 等） |
| 叙事匹配 | **一致**。Abstract/Intro 的 3 个 claim（跨语言可检测性、方向性不对称、detection-decision 解离）均有 experiments/discussion 中的数据支撑，三个模型数据完备 |

**额外发现**：introduction.tex 第 27 行还有一个 em-dash（`cross-model contrast---all three models`），不在本次 3 处修复范围内，供后续考虑。

### B. Em-dash 修复对比

**1. conclusion.tex:4**
```
- 改前: ...matching the XNLI baseline---indicating general cross-lingual alignment...
+ 改后: ...matching the XNLI baseline, indicating general cross-lingual alignment...
```

**2. experiments.tex:176**
```
- 改前: ...with 88.9% probe accuracy---the highest among all models---steering produced...
+ 改后: ...with 88.9% probe accuracy (the highest among all models), steering produced...
```

**3. discussion.tex:10**
```
- 改前: ...(1)~...interactions \citep{...}---MLP probes gain...;
         (2)~...superposition \citep{...}---conflict and XNLI...;
         (3)~...differences---Qwen and Gemma show...
+ 改后: ...(1)~...interactions \citep{...}, where MLP probes gain...;
         (2)~...superposition \citep{...}, where conflict and XNLI...;
         (3)~...differences, as Qwen and Gemma show...
```

### C. Related Work 引用堆砌修复对比

```
- 改前 (1 句 4 引用):
  \citet{zhao2024analysing} demonstrated linearly separable conflict signals
  in English residual streams, \citet{brink2026probing} localized factual
  associations via probing, \citet{pham2026where} traced intra-memory conflict
  pathways, and \citet{li2025taming} proposed conflict mitigation methods.

+ 改后 (2 句, 各 2 引用):
  \citet{zhao2024analysing} demonstrated linearly separable conflict signals
  in English residual streams, and \citet{brink2026probing} localized factual
  associations via probing. More recently, \citet{pham2026where} traced
  intra-memory conflict pathways, while \citet{li2025taming} proposed conflict
  mitigation methods.
```

### D. Page 12 末页空白

按要求暂不处理，等 Fig 5 双栏改完后再评估。

### 最终状态

| 指标 | 值 |
|------|-----|
| 编译错误 | 0 |
| 编译警告 | 0 |
| 总页数 | 12 |
| 正文页数 | ~8（Conclusion 在第 9 页顶部开始，Limitations 紧随其后；按 EMNLP 规则 Limitations 不计入 8 页限制，正文可能恰在边界，建议后续关注） |

---
