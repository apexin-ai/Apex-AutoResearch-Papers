# Handover — 2026-05-24

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- exp_llama70b_mmlu: Cross-family scale validation: Llama-3.1-70B-Instruct on MMLU shows item-dominated variance structure consistent with Qwen2.5-72B (item_id >60%, G_item >0.90), confirming G-theory findings are architecture-invariant at large scale（准备中）
- exp002_math_extension: D009 8-model expansion: 4-model MATH inference (Llama/Mistral/Qwen/Gemma) — free-form benchmark expected methodology-dominated variance pattern per D010（准备中）
- exp002_olmo_math: D009 8-model expansion: OLMo-2-7B MATH inference — free-form benchmark expected methodology-dominated variance pattern per D010（准备中）
- exp002_olmo_gsm8k: D009 8-model expansion: OLMo-2-7B GSM8K inference — free-form benchmark expected methodology-dominated variance pattern per D010（准备中）
- exp002_olmo_hellaswag: D009 8-model expansion: OLMo-2-7B HellaSwag inference — MC benchmark expected item-dominated variance pattern（准备中）
- exp002_olmo_arc: D009 8-model expansion: OLMo-2-7B ARC inference — MC benchmark expected item-dominated variance pattern per D010（准备中）
- exp002_olmo_mmlu: D009 8-model expansion: OLMo-2-7B MMLU inference — MC benchmark expected item-dominated variance pattern per D010（准备中）
- exp002_yi_math: D009 8-model expansion: Yi-1.5-9B-Chat MATH inference — free-form benchmark expected methodology-dominated variance pattern per D010（准备中）
- exp002_yi_gsm8k: D009 8-model expansion: Yi-1.5-9B-Chat GSM8K inference — free-form benchmark expected methodology-dominated variance pattern per D010（准备中）
- exp002_yi_hellaswag: D009 8-model expansion: Yi-1.5-9B-Chat HellaSwag inference — MC benchmark expected item-dominated variance pattern per D010（准备中）
- …另有 12 项

## 近期结论
- **exp_llama70b** (success): Cross-family scale validation: Llama-3.1-70B-Instruct (non-Qwen family, 70B scale) on 5 benchmarks should show item-dominated variance structure consistent with Qwen2.5-72B (G=0.979, item_id=83.25%), confirming G-theory variance decomposition is invariant across model families and not an artifact of a single architecture. ← 基于 exp003_scale_72b
- **exp003_scale_72b** (success): Scale validation: Qwen2.5-72B-Instruct (4-card TP=4) on MMLU shows item-related variance (item_id + model×item) >60% with same facet ranking as 7B-9B models, confirming G-theory variance structure is scale-invariant at the large-model end. If item_id% drops significantly at 72B scale, this reveals a scale-dependent variance boundary. ← 基于 exp002_multi_benchmark
- **exp003_scale_7b** (success): Scale validation within-family midpoint: Qwen2.5-7B-Instruct on MMLU provides the within-family 7B reference for 3-point scale curve (3B/7B/72B). Item-related variance (item_id + model×item) >60% expected, bridging the 3B and 72B endpoints to confirm monotonic scale-invariance of variance structure. ← 基于 exp002_multi_benchmark

## 趋势
成功 12 / 负向 1 / 失败 0 / 共 14
G_item: 0.9566 ↑（近 3 次 success）
grand_mean: 0.8157 ↑（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-32570: 无 GPU 信息

## 告警
- exp-002: 已被终止 — unknown
