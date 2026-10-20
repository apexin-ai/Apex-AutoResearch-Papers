# fix references bib correction

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_references-bib-correction_20260515T124440_result.json`
- **Structured JSON:** [`a2d85552aa4a1428237b.json`](../../sessions/a2/a2d85552aa4a1428237b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

剩余全在 `artifacts/` 下——这些是历史快照/生成产物，不影响编译。`docs/paper/`、`paper/`、`literature_map.yaml`、`paper_provenance.yaml` 全部清理完毕。

---

## 修正报告

### Step 1: 8 条 bib 条目替换（references.bib）
| 旧 key → 新 key | 旧 first author → 正确 first author |
|---|---|
| `ding2025selfexecution` → `maimon2025selfexecution` | Ding → Maimon, Gallil |
| `ye2025demystifying` → `abdollahi2025demystifying` | Ye → Abdollahi, Mohammad |
| `chen2025solidcoder` → `lee2025solidcoder` | Chen → Lee, Woojin |
| `zhang2025swerm` → `shum2025swerm` | Zhang → Shum, KaShun |
| `wu2025patchreasoner` → `xu2025patchreasoner` | Wu → Xu, Junjielong |
| `wang2025vgsearch` → `chen2025vgsearch` | Wang → Chen, Hao Mark |
| `zhang2025sstar` → `li2025sstar` | Zhang → Li, Dacheng |
| `aleithan2025survey` → `yang2025aprsurvey` | Aleithan → Yang, Boyang |

### Step 2: 新增 Qwen3 Technical Report
`qwen2025qwen3` 已添加。

### Step 3: 新增 4 条补充引用
`ni2023lever`, `chen2023codet`, `andrews2005mutation`, `just2014mutants` 已添加。

### Step 4: .tex cite key 更新
- `docs/paper/related_work.tex` — 8 处替换（含 `Ye et al.` → `Abdollahi et al.`、`Aleithan et al.` → `Yang et al.` 文本修正）
- `docs/paper/introduction.tex` — 已是新 key（之前已更新）
- `paper/method.tex` — 1 处 `zhang2025swerm` → `shum2025swerm`

### Step 5: C022 provenance 更新
`paper_provenance.yaml` 中 C022 的 3 条 evidence key 已更新：
- `ding2025selfexecution` → `maimon2025selfexecution`
- `chen2025solidcoder` → `lee2025solidcoder`
- `ye2025demystifying` → `abdollahi2025demystifying`

C022 claim 内容（"All prior execution simulation work uses generation formulation; we reformulate as classification"）与修正后论文的实际内容一致——这些论文确实都使用 generation formulation，first author 错误不影响 claim 的正确性。

### Step 6: "and others" 缩写审计
references.bib 中使用 `and others` 的条目：
| key | 说明 |
|---|---|
| `qwen2025qwen3` | 作者 100+ 人，缩写合理 |
| `liu2024codemind` | 可补全但非修正目标 |
| `chowdhury2024swebenchverified` | OpenAI 技术报告，可补全 |
| `yang2024qwen25` | 作者众多，缩写合理 |
| `chen2021humaneval` | 可补全但非修正目标 |
| `austin2021mbpp` | 可补全但非修正目标 |

本次修正的 8 条已全部补全完整作者列表。其余 `and others` 条目非紧急，可后续批量处理。

### 额外更新
`literature_map.yaml` — 8 条 key 和作者名同步修正。

---
