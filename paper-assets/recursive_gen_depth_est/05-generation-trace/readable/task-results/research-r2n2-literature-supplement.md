# research r2n2 literature supplement

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r2n2_literature_supplement_20260515T222540_result.json`
- **Structured JSON:** [`d6a1f001578086f158d5.json`](../../sessions/d6/d6a1f001578086f158d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新（35→43篇）。以下是补充的 8 篇论文及融入建议。

---

## 新增 8 篇论文

### 方向 1: Model Collapse 实证研究（+2）

| Key | 论文 | Venue | 相关性 |
|-----|------|-------|--------|
| `he2025_closer_look` | He et al. "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective" | **NeurIPS 2025** | 递归训练中 entropy 递减与 memorization 转变强相关——entropy 下降本身就是 depth signal，直接支撑我们的统计特征方法 |
| `feng2025_escaping_collapse` | Feng et al. "Escaping Model Collapse via Synthetic Data Verification" | **NeurIPS 2025** | 验证器引导的再训练可防止 collapse；我们的 depth estimation 可以充当 verifier，实现 graduated filtering 而非二元过滤 |

### 方向 2: Synthetic Data Detection（+4）

| Key | 论文 | Venue | 相关性 |
|-----|------|-------|--------|
| `tulchinskii2024_intrinsic_dim` | Tulchinskii et al. "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" | **NeurIPS 2023** | 文本 embedding 的内在维度（人类~9, AI~7.5）作为几何不变量，跨域鲁棒检测。与我们的统计特征互补，intrinsic dimension 可作为额外 depth feature |
| `verma2024_ghostbuster` | Verma, Fleisig, Tomlin, Klein. "Ghostbuster" | **NAACL 2024** | 结构化搜索弱 LM 特征组合做检测（99.0 F1 跨域）。特征工程路线与我们类似但仅做二元分类 |
| `li2024_mage` | Li et al. "MAGE: Machine-generated Text Detection in the Wild" | **ACL 2024** | 跨域跨模型检测 benchmark，发现显著 OOD 退化——与我们的跨模型泛化挑战一致 |
| `wu2025_detection_survey` | Wu et al. "A Survey on LLM-Generated Text Detection" | **Computational Linguistics 2025** | 检测范式全面综述（watermarking/statistical/neural），为我们定位为 statistical paradigm 向 ordinal depth 的扩展提供框架 |

### 方向 3: Data Curation（+1）

| Key | 论文 | Venue | 相关性 |
|-----|------|-------|--------|
| `penedo2024_fineweb` | Penedo et al. "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale" | **NeurIPS 2024** | 15T token 系统性质量过滤流水线。我们的 depth score 在 FineWeb 式 curation 之上增加合成污染维度 |

### 方向 4: Multi-source Attribution（+1）

| Key | 论文 | Venue | 相关性 |
|-----|------|-------|--------|
| `bevendorff2025_two_paradigms` | Bevendorff et al. "The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification" | **ACL 2025 Findings** | 将 LLM 检测重构为 authorship verification（非 attribution）。我们的 depth estimation 是第三范式——ordinal characterization，超越二元验证和多类归因 |

---

## 融入 Related Work 的建议

**最重要的 3 篇**（必须融入正文）：

1. **`bevendorff2025_two_paradigms`** — 用来重新定位我们的 contribution：现有工作分为 attribution（哪个模型生成的）和 verification（是否机器生成），我们提出第三范式：ordinal depth estimation（经历了几轮递归）。放在 Related Work 开头做 framing。

2. **`he2025_closer_look`** — 其 entropy 递减发现直接为我们的 depth signal 提供实证支撑。放在 Model Collapse 子节，与 Shumailov (tail erosion) 和 Dohmatob (scaling laws) 并列，强调 "entropy decline across generations is exactly what our features capture"。

3. **`wu2025_detection_survey`** — 作为综述引用，一句话定位我们在检测文献 landscape 中的位置："Wu et al. (2025) survey three detection paradigms; our work extends the statistical approach from binary to ordinal."

**次重要的 3 篇**（Related Work 中一句话引用）：

4. **`tulchinskii2024_intrinsic_dim`** — 在 Detection Methods 段落中与 DetectGPT/Binoculars 并列，强调"geometric features complement our statistical features"
5. **`verma2024_ghostbuster`** + **`li2024_mage`** — 与现有检测方法对比时引用，强调它们都是 binary，我们是 ordinal
6. **`feng2025_escaping_collapse`** — Discussion 中提及"our depth score can serve as the verifier in verification-guided training pipelines"

**penedo2024_fineweb** 放 Discussion 的 data curation application 段落，与 DSIR/QuRating 并列。

---
