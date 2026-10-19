# code fix bib critical

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_bib_critical_20260526T111024_result.json`
- **Structured JSON:** [`223272387a674c4fedaa.json`](../../sessions/22/223272387a674c4fedaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Compilation successful, 0 warnings.

## 引用修复报告

### 逐条变更

**ERROR（8 条）**

1. **`feng2026finegrained`**
   - 来源：[arXiv 2602.04428](https://arxiv.org/abs/2602.04428), [OpenReview](https://openreview.net/pdf?id=guSVafqhrB)
   - author: `Feng, Zihao and Li, Tian and Zhu, Zhengyu and Zhou, Hao and Qian, Junliang and Zhang, Lin and Mao, Kede`（7人，全错）→ `Feng, Zijian and Li, Tianjiao and Zhu, Zixiao and Zhou, Hanzhang and Qian, Junlang and Zhang, Li and Chua, Jia Jim Deryl and Mak, Lee Onn and Ng, Gee Wah and Mao, Kezhi`（10人）

2. **`xing2024evaluating`**
   - 来源：[arXiv 2407.01358](https://arxiv.org/abs/2407.01358)
   - author: `Xiaoling` → `Xiaolin`，`Zhenhui` → `Zhiwei`，`Huiyun` → `Haoyu`，`Wang, Xin` → `Wang, Xing`

3. **`sundar2025steering`**
   - 来源：[ACL Anthology 2025.acl-long.118](https://aclanthology.org/2025.acl-long.118/)
   - author: `Zhao, Skyler` → `Seto, Skyler`，`Jurafsky, Dan` → `Fedzechkina, Masha`

4. **`ifergan2024beneath`**
   - 来源：[arXiv 2408.10646](https://arxiv.org/abs/2408.10646)
   - author: `Ifergan, Matan` → `Ifergan, Maxim`
   - year: `2024` → `2025`

5. **`wu2020emerging`**
   - 来源：[ACL Anthology 2020.acl-main.536](https://aclanthology.org/2020.acl-main.536/)
   - author: 顺序修正，`Conneau, Alexis` 移至第一作者（原为 `Wu, Shijie` 在前）

6. **`li2025taming`**
   - 来源：[arXiv 2503.10996](https://arxiv.org/abs/2503.10996), [ICML 2025 poster](https://icml.cc/virtual/2025/poster/46677)
   - author: `Chen, Yufei` → `Chen, Yuzhong`

7. **`wang2025lost`**
   - 来源：[ACL Anthology 2025.acl-long.253](https://aclanthology.org/2025.acl-long.253/)
   - author: 增加 `Liu, Yihong` 和 `Nie, Ercong`（5人→7人）

8. **`pham2026where`**
   - 来源：[arXiv 2601.09445](https://arxiv.org/abs/2601.09445)
   - author: `Borkakoty, Hrishav` → `Borkakoty, Hsuvas`

**WARNING（6 条）**

9. **`marks2024geometry`**
   - 来源：[ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)
   - year: `2024` → `2025`

10. **`kargaran2024mexa`**
    - 来源：[ACL Anthology 2025.findings-acl.1385](https://aclanthology.org/2025.findings-acl.1385/)
    - author: `Nikeghbal, Naghmeh` → `Nikeghbal, Nafiseh`
    - year: `2024` → `2025`

11. **`zou2023representation`**
    - 来源：[arXiv 2310.01405](https://arxiv.org/abs/2310.01405), [dblp](https://dblp.org/rec/journals/corr/abs-2310-01405.html)
    - author: `Koyber, Sanmi` → `Koyejo, Sanmi`；增加缺失作者 `Song, Dawn`

12. **`zhao2024analysing`**
    - 来源：[arXiv 2410.16090](https://arxiv.org/abs/2410.16090)
    - 验证结果：当前 bib 作者顺序与 arXiv 一致，**无需修改**

13. **`turner2023activation`**
    - 来源：[arXiv 2308.10248v5](https://arxiv.org/abs/2308.10248v5)
    - title: `Activation Addition: Steering Language Models Without Optimization` → `Steering Language Models With Activation Engineering`
    - author: 增加 `Vazquez, Juan J.`；修正 Leech/Udell 顺序

14. **`ravichander2021probing`**
    - 来源：[ACL Anthology 2021.eacl-main.295](https://aclanthology.org/2021.eacl-main.295/)
    - pages: `3331--3350` → `3363--3377`

### 编译验证
- pdflatex + bibtex: 编译成功，0 warning，0 error
- bib 语法检查：花括号平衡，无空字段，38 条 entry

---
