# paper fix citations and warnings

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-citations-and-warnings_20260522T131347_result.json`
- **Structured JSON:** [`f87ca754a819bb01cbd9.json`](../../sessions/f8/f87ca754a819bb01cbd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files updated. Here's the final verification report:

---

### 验证报告

**1. Bib 条目总数：45**

**2. 所有 .tex 中 \cite{} key 的完整列表（29 个唯一 key）：**

| # | Key | 出现文件 |
|---|-----|---------|
| 1 | `kim2024openvla` | related_work, method, experiment_setup |
| 2 | `brohan2023rt2` | related_work |
| 3 | `hu2025vlsa` | related_work, experiment_setup, experiments, discussion |
| 4 | `zhai2026cofreevla` | related_work |
| 5 | `morton2025oscbf` | related_work |
| 6 | `raja2024ogmcbf` | related_work, discussion |
| 7 | `zhang2025safevla` | related_work |
| 8 | `li2022bevformer` | related_work |
| 9 | `sima2023occnet` | related_work |
| 10 | `tian2023occ3d` | related_work |
| 11 | `liu2025occvla` | related_work |
| 12 | `yuan2025depthvla` | related_work |
| 13 | `rao2026augvla3d` | related_work |
| 14 | `ranftl2022midas` | related_work |
| 15 | `yang2024depthanything` | related_work |
| 16 | `li2026spatialforcing` | related_work (x2) |
| 17 | `wu2025spatialvla` | related_work |
| 18 | `li2025pointvla` | related_work |
| 19 | `wu2026stvla` | related_work |
| 20 | `caruana1997multitask` | related_work |
| 21 | `ruder2017overview` | related_work |
| 22 | `lippl2024implicit` | related_work |
| 23 | `hu2022lora` | related_work, method |
| 24 | `kim2025oft` | method, experiment_setup, experiments |
| 25 | `oquab2024dinov2` | method |
| 26 | `zhai2023siglip` | method |
| 27 | `lin2017focal` | method |
| 28 | `liu2023libero` | experiment_setup |
| 29 | `kwon2026learningnudge` | discussion |

**3. Undefined citations（.tex 中有但 bib 中没有）：0**

**4. Bib 中未被引用的条目（16 个，均为原 bib 中的背景文献）：**
`yu2026safenightvla`, `li2026vlasafety`, `long2025neuralcsbf`, `chen2026gstvla`, `li2025qdepthvla`, `abouzeid2025geoaware`, `lin2025evo0`, `tu2026sgvla`, `xiao2026stemvla`, `bhat20253dcavla`, `li2026corridorvla`, `sun2025geovla`, `pan2026savla`, `ma2026vlanext`, `shukor2025smolvla`, `choi2026vlaeval`

### 已完成的修改汇总

**Critical — 引用统一 + bib 补全：**
- 所有 .tex 中的 cite key 统一为 `{第一作者姓小写}{年份}{关键词}` 格式
- 修正了 4 处作者错误：Shaw→Morton/Pavone, Rabiee/Hoagg→Raja et al., Tong→Sima, Wang→Lippl/Lindsey
- references.bib 完整重写，45 条目全部经 WebSearch 验证
- 额外修复了 `experiments.tex`（3 处旧 key）和 `discussion.tex`（2 处旧 key）

**Warning 1：** Table 1 "Value of spatial signal content" → "Effect of spatial signal fidelity"，caption 增加注释

**Warning 2：** §3.4 添加 OCC-Cutoff 条件段落

**Warning 3：** experiment_setup.tex 补充 `--num_images_in_input 2` 和 `--image_aug True`

注意：`write_paper_section(section="references")` 额外生成了 `references.tex`，LaTeX 编译使用的是 `references.bib`（通过 `\bibliography{references}`），`references.tex` 可以删除。

---
