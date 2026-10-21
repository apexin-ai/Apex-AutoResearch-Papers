# research ref audit batch2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-batch2_20260526T064109_result.json`
- **Structured JSON:** [`1cc608408c6365508086.json`](../../sessions/1c/1cc608408c6365508086.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications complete. Here's the consolidated report:

---

## 引用核查报告（第 2 批）

### 1. `cohen1988` — Statistical Power Analysis for the Behavioral Sciences
- **bib 中**: author={Cohen, Jacob}, year={1988}, publisher={Lawrence Erlbaum Associates}, type={@book}, edition={2nd}
- **核实结果**: author={Cohen, Jacob}, year={1988}, publisher={Lawrence Erlbaum Associates}, edition={2nd}
- **结论**: ✅ 正确

---

### 2. `gu2024cruxeval` — CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution
- **bib 中**: author={Gu, Alex and Rozière, Baptiste and Leather, Hugh and Solar-Lezama, Armando and Synnaeve, Gabriel and Wang, Sida I.}, year={2024}, booktitle={Proceedings of the 41st ICML}, pages={16568--16621}, type={@inproceedings}
- **核实结果**: 同上，ICML 2024 Volume 235 确认
- **结论**: ✅ 正确

---

### 3. `hosseini2025genrm` — Generative Verifiers: Reward Modeling as Next-Token Prediction
- **bib 中**: author={Hosseini, Arian and Yuan, Xingdi and Malkin, Nikolay and Courville, Aaron and Sordoni, Alessandro and Agarwal, Rishabh}, year={2025}, booktitle={ICLR}, type={@inproceedings}
- **核实结果**: author={Zhang, Lunjun and Hosseini, Arian and Bansal, Hritik and Kazemi, Seyed Mehran and Kumar, Aviral and Agarwal, Rishabh}, year={2025}, venue={ICLR 2025}
- **结论**: ⚠️ 有差异
- **差异**:
  - `author`: bib 中写的 {Hosseini, Arian and Yuan, Xingdi and Malkin, Nikolay and Courville, Aaron and Sordoni, Alessandro and Agarwal, Rishabh} → 应该是 {Zhang, Lunjun and Hosseini, Arian and Bansal, Hritik and Kazemi, Seyed Mehran and Kumar, Aviral and Agarwal, Rishabh}
  - 缺少第一作者 Lunjun Zhang；Yuan, Malkin, Courville, Sordoni 不是该论文作者；缺少 Bansal, Kazemi, Kumar

---

### 4. `abdollahi2025demystifying` — Demystifying Errors in LLM Reasoning Traces
- **bib 中**: author={Abdollahi, Mohammad and Tasnia, Khandaker Rifah and Saha, Soumit Kanti and Yang, Jinqiu and Wang, Song and Hemmati, Hadi}, year={2025}, journal={arXiv preprint arXiv:2512.00215}, type={@article}
- **核实结果**: 同上，arXiv 2512.00215 确认，仍为预印本
- **结论**: ✅ 正确

---

### 5. `snell2024scaling` — Scaling LLM Test-Time Compute Optimally...
- **bib 中**: author={Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral}, year={2025}, booktitle={ICLR}, note={Oral}, type={@inproceedings}
- **核实结果**: 同上，ICLR 2025 Oral 确认（arXiv 2408.03314 是 2024 预印本）
- **结论**: ✅ 正确（key 用 2024 是 arXiv 年份，entry 中 year=2025 是会议发表年，均可接受）

---

### 6. `jimenez2024swebench` — SWE-bench: Can Language Models Resolve Real-world GitHub Issues?
- **bib 中**: author={Jimenez, Carlos E and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik}, year={2024}, booktitle={ICLR}, type={@inproceedings}
- **核实结果**: 同上，ICLR 2024 确认
- **结论**: ✅ 正确

---

### 7. `yang2024sweagent` — SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- **bib 中**: author={Yang, John and Jimenez, Carlos E and Wettig, Alexander and Lieret, Kilian and Yao, Shunyu and Narasimhan, Karthik and Press, Ofir}, year={2024}, booktitle={NeurIPS}, type={@inproceedings}
- **核实结果**: 同上，NeurIPS 2024 确认
- **结论**: ✅ 正确

---

### 8. `austin2021mbpp` — Program Synthesis with Large Language Models
- **bib 中**: author={Austin, Jacob and Odena, Augustus and Nye, Maxwell and others}, year={2021}, journal={arXiv preprint arXiv:2108.07732}, type={@article}
- **核实结果**: arXiv 2108.07732 确认，未正式发表于期刊/会议，仍为预印本
- **结论**: ✅ 正确

---

### 9. `le2022coderl` — CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning
- **bib 中**: author={Le, Hung and Wang, Yue and Gotmare, Akhilesh Deepak and Savarese, Silvio and Hoi, Steven C.H.}, year={2022}, booktitle={NeurIPS}, type={@inproceedings}
- **核实结果**: 同上，NeurIPS 2022 确认
- **结论**: ✅ 正确

---

### 10. `shinn2023reflexion` — Reflexion: Language Agents with Verbal Reinforcement Learning
- **bib 中**: author={Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu}, year={2023}, journal={NeurIPS}, type={@article}
- **核实结果**: author={Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu}, year={2023}, venue={NeurIPS 2023 (conference)}
- **结论**: ⚠️ 有差异
- **差异**:
  - `type`: @article → 应该是 @inproceedings
  - `journal={NeurIPS}` → 应该是 `booktitle={NeurIPS}`
  - `author`: 缺少第三作者 **Berman, Edward**

---

### 11. 其他可疑不一致（全文件扫描）

扫描发现以下 entry type 问题（key-year 不匹配属于命名习惯问题，不影响渲染，不列入）：

| Key | 问题 | 说明 |
|-----|------|------|
| `dettmers2024qlora` | key 写 2024，entry 写 year=2023 | NeurIPS 2023 是正确的发表年；key 命名有误但不影响引用输出 |

未发现其他内容层面的幻觉或严重信息错误。Director 提到的"另外 2 个不一致"应该就是 `hosseini2025genrm`（作者列表严重错误）和 `shinn2023reflexion`（entry type + 缺作者）。

---

## 汇总：需要修正的条目

| # | Key | 问题严重程度 | 修正内容 |
|---|-----|-------------|----------|
| 1 | `hosseini2025genrm` | **严重** | 作者列表完全错误（4/6 人名错误，缺第一作者） |
| 2 | `shinn2023reflexion` | **中等** | @article→@inproceedings, journal→booktitle, 补作者 Berman |

---
