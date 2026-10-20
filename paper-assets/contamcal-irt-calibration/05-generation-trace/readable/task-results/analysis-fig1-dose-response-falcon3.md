# analysis fig1 dose response falcon3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig1-dose-response-falcon3_20260522T150858_result.json`
- **Structured JSON:** [`99aa03e3aecb2e2340bc.json`](../../sessions/99/99aa03e3aecb2e2340bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。脚本已更新为 7-family MMLU dose-response 图，输出文件：

- `figures/paper/gen_fig_dose_response.py` — 更新后的生成脚本
- `figures/paper/fig_dose_response.pdf` + `.png` — 生成的图表
- `artifacts/fig_dose_response.pdf` + `.png` — 副本

关键变更：
- 从旧版（Qwen2.5 0.5B/1.5B/3B × 3 benchmarks）改为 7 个跨家族 MMLU 曲线
- 新增 Falcon3-7B（金色实线，Benefit），以及 Phi-4、Qwen2.5-14B/7B、Gemma-2、OLMo-2、LLaMA-3.1
- 线型编码 4 种 pattern：实线=Benefit，虚线=Immune，点线=Collapse，点划线=V-recovery
- 右侧直接标注模型名，带碰撞避免；左下角放 pattern 图例
- LLaMA-3.1 仅 3 个 dosage 点（d000/d025/d100），已正确处理
- 所有数据均从项目文件读取验证，未编造

---
