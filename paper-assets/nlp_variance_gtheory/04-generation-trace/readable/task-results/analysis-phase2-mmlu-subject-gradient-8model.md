# analysis phase2 mmlu subject gradient 8model

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_mmlu_subject_gradient_8model_20260521T224259_result.json`
- **Structured JSON:** [`4e3ddd93a09bd2afb95e.json`](../../sessions/4e/4e3ddd93a09bd2afb95e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

### Subject-Level Table (sorted by item_id%)

| Subject | Cat | item_id% | m×i% | std(p) | G_item | acc |
|---|---|---|---|---|---|---|
| clinical_knowledge | Other | 47.5 | 30.0 | 0.360 | 0.923 | 0.581 |
| international_law | Hum | 44.4 | 24.1 | 0.316 | 0.930 | 0.717 |
| world_religions | Hum | 42.2 | 27.1 | 0.262 | 0.910 | 0.826 |
| computer_security | STEM | 37.0 | 24.9 | 0.284 | 0.908 | 0.740 |
| philosophy | Hum | 33.0 | 36.1 | 0.258 | 0.868 | 0.782 |
| college_physics | STEM | 31.6 | 30.1 | 0.302 | 0.876 | 0.436 |
| abstract_algebra | STEM | 24.1 | 32.8 | 0.272 | 0.822 | 0.457 |
| us_foreign_policy | Hum | 20.4 | 36.9 | 0.175 | 0.802 | 0.864 |
| professional_medicine | Other | 19.9 | 41.7 | 0.242 | 0.778 | 0.671 |
| high_school_math | STEM | 10.4 | 41.9 | 0.201 | 0.614 | 0.385 |

### 核心发现

- **Spearman ρ(std_p, item_id%) = 0.806, p = 0.005** — item difficulty 异质性强烈预测 item_id%，支持 "item heterogeneity 而非 format 驱动方差结构" 的假说
- **STEM vs Humanities gradient 保持但弱化**：STEM mean item_id% = 25.8% (4-model: 27.9, Δ=-2.1), Humanities = 35.0% (4-model: 48.4, Δ=-13.4)
- Humanities 下降大的原因：us_foreign_policy (20.4%) 和 philosophy (33.0%) 在 8-model 下 model×item 交互吸收了更多方差（分别 36.9% 和 36.1%），说明更多模型增加了 model-specific item 困难模式的解析度
- **G_item 范围 0.614–0.930**，与 std(p) 高度一致：high_school_math（最低异质性 std_p=0.201）的 G_item 最低（0.614），international_law（高异质性）最高（0.930）
- 关键洞察：STEM/Humanities 的分界不是决定因素——us_foreign_policy（Humanities）的 item_id% 低于 college_physics（STEM）。真正的驱动力是 item-level difficulty spread

JSON 已保存至 `results/exp004_8model_analysis/mmlu_subject_gradient_8model.json`。

---
