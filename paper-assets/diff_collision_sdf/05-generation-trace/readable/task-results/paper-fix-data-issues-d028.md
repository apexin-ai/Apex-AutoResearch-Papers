# paper fix data issues d028

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_data_issues_d028_20260526T054317_result.json`
- **Structured JSON:** [`22cb8e3cb1341bf33512.json`](../../sessions/22/22cb8e3cb1341bf33512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

analysis_claim3.tex 已确认使用 30K 数据，无需修改。

---

## 所有改动汇总

### 问题 1：Pi0.5 "98.2% fake safe" → pending

| 文件 | 位置 | 改动 |
|------|------|------|
| `analysis_claim1.tex:19` | Table Pi0.5 行 | `98.2 / 1 / 56 / ≈0` → `\multicolumn{3}{c}{pending$^\ddagger$}` |
| `analysis_claim1.tex:23` | Table 脚注 | 新增 `$^\ddagger$` 说明：prior value (98.2%) used obstacle displacement |
| `analysis_claim1.tex:26-28` | Pi0.5 段落 | 重写：从"fake safe 98.2%"改为"contrasting case，re-evaluation in progress，may reflect genuine avoidance"；结论限定为 Pi0-based methods |
| `analysis_claim1.tex:34` | CAR_f 段 | "LoRA baseline and Pi0.5 near zero" → LoRA baseline near zero；Pi0.5 pending |
| `introduction.tex:9` | 第3段末 | "exhibits the same pattern: 98.2%" → "exhibits qualitatively different behavior...under re-evaluation" |
| `introduction.tex:17` | C1 贡献 | "98--99% across multiple methods and model scales" → "over 99% in Pi0-based methods" |
| `abstract.tex:2` | Pi0.5 描述 | "shows the same pattern" → "presents a contrasting case whose fake safety status is under re-evaluation" |

### 问题 2：10K → 30K 数据修正

| 文件 | 位置 | 改动 |
|------|------|------|
| `introduction.tex:13` | 段末 preliminary result | 10K "CAR 56-58%, TSR 47-49%" → 30K 为主（LoRA-only CAR=55.3%, TSR=6.3%; SDF CAR=50.5-52.8%, TSR=6.8%），10K 作为补充（TSR=26-30.5%, catastrophic collapse between 10K-30K） |
| `introduction.tex:19` | C3 贡献 | 补充 30K 具体数字（CAR 55.3%/50.5-52.8%, TSR 6.3%/6.8%）和 10K→30K TSR collapse |
| `abstract.tex:2` | Preliminary results 句 | "training-time SDF supervision...genuine collision avoidance" → 报告 30K 结果（CAR ~55%, TSR collapse to <7%, SDF no benefit） |

### 未修改（确认正确）

- A1 的 99.6% fake safe — 保留
- `analysis_claim3.tex` — 已使用 30K 数据，无 10K 问题

---
