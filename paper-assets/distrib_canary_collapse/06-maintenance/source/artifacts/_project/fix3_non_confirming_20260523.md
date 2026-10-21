# Fix #3: Non-confirming Conditions Count

## Table 2 完整数据
| # | Model | Seed | Precision | Domain | PermG fwd | PermG rev | ≥6/8 unidirectional? |
|---|-------|------|-----------|--------|-----------|-----------|---------------------|
| 1 | Pythia-410M | s42 | fp32 | Wiki | 6/8 | 0/8 | ✅ |
| 2 | Pythia-410M | s43 | fp32 | Wiki | 6/8 | 0/8 | ✅ |
| 3 | Pythia-1.4B | s42 | fp32 | Wiki | 2/8 | — | ❌ seed dependence |
| 4 | Pythia-1.4B | s43 | fp32 | Wiki | 6/8 | — | ✅ |
| 5 | Pythia-6.9B | s42 | bf16 | Wiki | 7/8 | — | ✅ |
| 6 | GPT-2-medium | s42 | fp32 | Wiki | 6/8 | 0/8 | ✅ |
| 7 | GPT-2-medium | s43 | fp32 | Wiki | 6/8 | 4/8 | ❌ bidirectional |
| 8 | GPT-2-medium | — | bf16 | Wiki | 0/8 | — | ❌ precision sensitivity |
| 9 | OPT-1.3B | s42 | fp32 | Wiki | 6/8 | — | ✅ |
| 10 | OPT-1.3B | s43 | fp32 | Wiki | 6/8 | — | ✅ |
| 11 | Qwen3.5-0.8B | s42 | fp32 | Wiki | 8/8 | — | ✅ |
| 12 | SmolLM3-3B | s42 | fp32 | Wiki | 3/8 | — | ❌ arch decoupling |
| 13 | Padding-410M | s42 | fp32 | Wiki | 6/8 | — | ✅ |
| 14 | C4-Pythia-1B | s42 | fp32 | C4 | 8/8 | — | ✅ |
| 15 | C4-Pythia-1B | s43 | fp32 | C4 | 8/8 | — | ✅ |

## 核实结果
- Confirming (≥6/8 unidirectional forward): **11 个** (#1,2,4,5,6,9,10,11,13,14,15)
- Non-confirming: **4 个** (#3,7,8,12)
- 总计: 15

原文写 "10/15" + "5 non-confirming span four failure modes" 但只列出 4 个条件，10+4=14≠15。
实际 11+4=15，与 appendix.tex L460 的 "11 of 15" 一致。

## 修改内容
- `docs/paper/experiments.tex:103` — `10/15` → `11/15`
- `docs/paper/experiments.tex:104` — `The 5 non-confirming conditions span four failure modes:` → `The four non-confirming conditions each represent a distinct failure mode:`
- `abstract.tex`, `introduction.tex` 未引用此数字，无需修改
