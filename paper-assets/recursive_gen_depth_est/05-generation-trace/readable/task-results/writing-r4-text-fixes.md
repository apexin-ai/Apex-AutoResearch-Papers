# writing r4 text fixes

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r4_text_fixes_20260516T130055_result.json`
- **Structured JSON:** [`2bc8c7f10ec6fa7467ce.json`](../../sessions/2b/2bc8c7f10ec6fa7467ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files pass brace balance. Here's the summary of all modifications:

| 修改项 | 文件 | 变更 |
|--------|------|------|
| **N1** | `abstract.tex:6` | EDD 加统计限定 (Pythia p=0.001, graded support) |
| **N2** | `generalization.tex:5-15` | §4.1 标题改为 "Classifier Comparison and Surface-Text Ablation"，LLM 段落 reframe 为 ablation |
| **N2** | `discussion.tex:7` | LLM 段落同步改为 surface-text ablation 语调 |
| **N3** | `abstract.tex:8` | "Extending to two 7B" → "Preliminary cross-scale observations" |
| **N3** | `generalization.tex:4` | "cross-scale generalization" → "preliminary cross-scale observations" |
| **N3** | `generalization.tex:99` | §4.4 标题改为 "Preliminary Cross-Scale Observations" |
| **N3** | `generalization.tex:169-170` | §4.4 末尾加 confound 声明 (4 条) |
| **N3** | `discussion.tex:32` | Scaling behavior 段落降级 + 加 confound 说明 |
| **N4** | `abstract.tex:7` | "depth signal is a property of..." → "preliminary evidence consistent with..." |
| **N4** | `section_appendix.tex:324-330` | Cross-Boundary 加 confound 讨论段 |
| **W1** | `atlas.tex:47` | 加 "perplexity tail statistics as a feature group dominate" + VIF 脚注 |
| **W1** | `discussion.tex:5` | 同步改为 "dominant feature group" 表述 |
| **W2** | `discussion.tex:18` | Curation PoC 改为 "inconclusive pilot"，移除 positive framing |
| **W2** | `section_appendix.tex:346` | Extended Discussion 同步降级 |
| **W3** | `method.tex:35` | §3.2 加 BOS-seeded 限制说明 |
| **W3** | `discussion.tex:23` | provenance toolkit 加 "within controlled generation settings" |
| **W4** | `abstract.tex:7` | 66.4% 后加 "(d1--d3 balanced accuracy: 55.4%, 1.7× chance)" |
| **W5** | `introduction.tex:28-30` | Contribution bullets 改为 empirical investigation 语调 |
| **I1** | `abstract.tex` | 数字从 ~22 个精简到 6-7 个核心指标 |
| **I2** | `method.tex:101` | 脚注加 Qwen U-shaped 说明 |
| **I3** | `related_work.tex:8` | `yi2026_escaping_collapse` 引入 model collapse mitigation 列表 |
| **I4** | `related_work.tex:25-27` | Mohamed et al. 扩展为 3 句，强调 depth estimation vs detection 区别 |
| **I5** | `section_appendix.tex:223-237` | Calibration 表加 95% Wilson CI 列 |

---
