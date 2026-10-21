# audit final data check ddl

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final-data-check-ddl_20260524T042721_result.json`
- **Structured JSON:** [`b47ab389e4def86df370.json`](../../sessions/b4/b47ab389e4def86df370.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完成。结果如下：

**❌ 已修复 4 处不一致：**

| # | 问题 | 修复 |
|---|------|------|
| 1 | Qwen-7B AUC：Table 1/Extended (.6168/.9638) vs Crossscorer/Registry (.6178/.9644) | 统一为 registry 值 .6178/.9644，同步更新 Bonferroni CI |
| 2 | appendix_extended "Pythia↔OLMo: 90--92%" | → "89--92%"（实际 89.4%--92.4%，与其余三处引用一致） |
| 3 | Table S1 caption "Qwen-cont↔Pythia 83--85%" | → "84--85%"（实际 84.8%--85.0%，83% 不存在于数据中） |
| 4 | appendix_extended "80--100% accuracy" | → "80--92%"（与 Abstract/Intro/实验章节一致） |

**✅ 通过：** Table 1 全部 25 cells、Table 5 全部 12 cells、dose-response 9 cells、bootstrap K* 10 行、runtime benchmark 4 行、所有 crossscorer/domain/decoding/DeBERTa 数值均与 registry 或服务器 artifacts 精确匹配。Abstract/Intro/Conclusion 数字与实验章节交叉验证通过。

**⚠️ 无法验证 5 项：** Gemma-2-27B (无 registry 条目)、Pythia-6.9B (无明确 ID 匹配)、ANOVA 原始数据 (服务器无文件)、4-gram repeat ratio、seed robustness 原始值。

报告已写入 `artifacts/final_data_audit_20260524.md`。

---
