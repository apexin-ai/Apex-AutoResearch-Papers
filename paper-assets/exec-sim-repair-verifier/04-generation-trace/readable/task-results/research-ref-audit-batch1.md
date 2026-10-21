# research ref audit batch1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-batch1_20260526T061956_result.json`
- **Structured JSON:** [`95068f953295b97391ca.json`](../../sessions/95/95068f953295b97391ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部搜索完成，以下是核查报告。

---

## 引用核查报告（第 1 批：11 条）

### 1. `nam2025repoexec` — REPOEXEC
- **bib 中**: author={Nam, Hai and Dau, Thang and Bui, Nhat and Nguyen, Nghi D. Q.}, year={2025}, booktitle={NAACL}, title={REPOEXEC: Evaluate Code Generation with a Repository-Level Executable Benchmark}
- **核实结果**: author={Nam Le Hai and Dung Manh Nguyen and Nghi D. Q. Bui}（3 位作者，非 4 位）, year={2025}, venue={Findings of NAACL 2025}, title={On the Impacts of Contexts on Repository-Level Code Generation}（发表版标题已更改）
- **结论**: ⚠️ 有差异
- **差异**:
  - **title**: `REPOEXEC: Evaluate Code Generation with a Repository-Level Executable Benchmark` → 发表版为 `On the Impacts of Contexts on Repository-Level Code Generation`（arXiv v1/v2 用旧标题，v3/camera-ready 已改名）
  - **author**: 4 位→3 位，且姓名拼写有误（`Dau, Thang` → 不存在此作者；`Bui, Nhat` → 应为 `Nghi D. Q. Bui`）。正确作者：Nam Le Hai, Dung Manh Nguyen, Nghi D. Q. Bui
  - **booktitle**: `NAACL` → 应为 `Findings of NAACL 2025`

---

### 2. `liu2024codemind` — CodeMind
- **bib 中**: author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh}, year={2024}, journal={arXiv preprint arXiv:2402.09664}
- **核实结果**: author={Changshu Liu and Shizhuo Dylan Zhang and Ali Reza Ibrahimzada and Reyhaneh Jabbarvand}, year={2024}, venue={arXiv preprint arXiv:2402.09664}
- **结论**: ✅ 正确
- 作者、年份、标题均匹配。未找到正式会议发表记录，arXiv preprint 标注合理。

---

### 3. `xu2025patchreasoner` — Patch Reasoner
- **bib 中**: author={Xu, Junjielong and Tan, Boyin and Liu, Xiaoyuan and Peng, Chao and Gao, Pengfei and He, Pinjia}, year={2025}, journal={arXiv preprint arXiv:2510.22775}
- **核实结果**: 同上，完全匹配
- **结论**: ✅ 正确

---

### 4. `chowdhury2024swebenchverified` — SWE-bench Verified
- **bib 中**: author={Chowdhury, Neil and Aung, James and Shern, Chan Jun and ...}, year={2024}, url={https://openai.com/index/introducing-swe-bench-verified/}
- **核实结果**: 作者列表、年份、URL 均匹配
- **结论**: ✅ 正确

---

### 5. `lightman2023letsverify` — Let's Verify Step by Step
- **bib 中**: author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and ...}, year={2023}, journal={arXiv preprint arXiv:2305.20050}
- **核实结果**: author 一致, year={2024}, venue={ICLR 2024}（DBLP 记录：`conf/iclr/LightmanKBEBLLS24`）
- **结论**: ⚠️ 有差异
- **差异**:
  - **year**: `2023` → 应为 `2024`（已正式发表于 ICLR 2024）
  - **venue**: `arXiv preprint` → 应为 `ICLR 2024`

---

### 6. `kim2022predictive` — Predictive Mutation Testing
- **bib 中**: author={Kim, Jinhan and Ju, Juyoung and Tao, Robert and Hu, Nhat-Tan and Baik, Shin Yoo Juyeon}, year={2022}, journal={IEEE TSE}, title={Predictive Mutation Testing via Natural Language Channel}
- **核实结果**: author={Kim, Jinhan and Jeon, Juyoung and Hong, Shin and Yoo, Shin}, year={2022}, journal={ACM Transactions on Software Engineering and Methodology}, volume={31}, number={4}, title={Predictive Mutation Analysis via the Natural Language Channel in Source Code}
- **结论**: ⚠️ 严重差异（多字段错误）
- **差异**:
  - **title**: `Predictive Mutation Testing via Natural Language Channel` → `Predictive Mutation Analysis via the Natural Language Channel in Source Code`
  - **author**: `Ju, Juyoung` → `Jeon, Juyoung`；`Tao, Robert and Hu, Nhat-Tan and Baik, Shin Yoo Juyeon`（3 个虚构作者）→ `Hong, Shin and Yoo, Shin`（实际只有 4 位作者）
  - **journal**: `IEEE TSE` → `ACM Transactions on Software Engineering and Methodology (TOSEM)`

---

### 7. `andrews2005mutation` — Is Mutation an Adequate Substitute...
- **bib 中**: author={Andrews, James H and Briand, Lionel C and Labiche, Yvan}, year={2005}, booktitle={ICSE}, title={Is Mutation an Adequate Substitute for Real Faults?}
- **核实结果**: author 一致, year={2005}, booktitle={ICSE 2005}, title={Is Mutation an Appropriate Tool for Testing Experiments?}
- **结论**: ⚠️ 有差异
- **差异**:
  - **title**: `Is Mutation an Adequate Substitute for Real Faults?` → `Is Mutation an Appropriate Tool for Testing Experiments?`（bib 标题疑似与 Just et al. 2014 的 "Are Mutants a Valid Substitute for Real Faults in Software Testing?" 混淆）

---

### 8. `angrist2009mostly` — Mostly Harmless Econometrics
- **bib 中**: author={Angrist, Joshua D. and Pischke, Jörn-Steffen}, year={2009}, publisher={Princeton University Press}
- **核实结果**: 完全匹配（Princeton University Press 官网确认 2009 年出版）
- **结论**: ✅ 正确

---

### 9. `poesia2022synchromesh` — Synchromesh
- **bib 中**: author={Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit}, year={2022}, booktitle={ICLR}, title={Synchromesh: Reliable Code Generation by Retrieving and Transforming}
- **核实结果**: author 一致, year={2022}, booktitle={ICLR 2022}, title={Synchromesh: Reliable Code Generation from Pre-trained Language Models}
- **结论**: ⚠️ 有差异
- **差异**:
  - **title**: `...by Retrieving and Transforming` → `...from Pre-trained Language Models`（副标题完全不同）

---

### 10. `alphacode2023team` — AlphaCode 2 Technical Report
- **bib 中**: author={AlphaCode Team}, year={2023}, institution={Google DeepMind}
- **核实结果**: 完全匹配
- **结论**: ✅ 正确

---

### 11. `cohen1988` — Statistical Power Analysis
- **bib 中**: author={Cohen, Jacob}, year={1988}, title={Statistical Power Analysis for the Behavioral Sciences}, edition={2nd}, publisher={Lawrence Erlbaum Associates}
- **核实结果**: 完全匹配
- **结论**: ✅ 正确

---

## 汇总

| # | Key | 结论 | 严重程度 |
|---|-----|------|----------|
| 1 | `nam2025repoexec` | ⚠️ 标题/作者/venue 均有误 | 高 |
| 2 | `liu2024codemind` | ✅ 正确 | — |
| 3 | `xu2025patchreasoner` | ✅ 正确 | — |
| 4 | `chowdhury2024swebenchverified` | ✅ 正确 | — |
| 5 | `lightman2023letsverify` | ⚠️ 应更新为 ICLR 2024 | 中 |
| 6 | `kim2022predictive` | ⚠️ 标题/作者/期刊全错 | **极高** |
| 7 | `andrews2005mutation` | ⚠️ 标题错误 | 高 |
| 8 | `angrist2009mostly` | ✅ 正确 | — |
| 9 | `poesia2022synchromesh` | ⚠️ 标题错误 | 高 |
| 10 | `alphacode2023team` | ✅ 正确 | — |
| 11 | `cohen1988` | ✅ 正确 | — |

**5 条正确，6 条有差异**（其中 `kim2022predictive` 最为严重——作者列表含虚构姓名、期刊也标错）。

---
