# Handover — 2026-05-24

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **mismatch_full2exc_seed42** (success): Full_trace-trained model facing exception_only inputs at inference will degrade, confirming forward-pass confound: the model learned format-specific features rather than extracting diagnostic signals from any input format.
- **mismatch_exc2full_seed42** (success): Exception_only-trained model facing full_trace inputs at inference will degrade significantly, confirming forward-pass confound: the model learned format-specific features rather than generalizable diagnostic patterns.
- **gradient_masking_qwen7b_seed42** (unknown): —

## 趋势
成功 134 / 负向 22 / 失败 9 / 共 190
accuracy: 0.309 ↓（近 3 次 success）
accuracy_ci_lower: 0.284 ↓（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-11235: 无 GPU 信息

## 告警
- no_trace_seed42: 已被终止 — unknown
- vota_seed42: 已被终止 — unknown
- no_trace_seed42_v2: 已被终止 — unknown
- vota_seed42_v2: 已被终止 — unknown
- no_trace_seed42_v3: 已被终止 — unknown
- vota_seed42_v3: 已被终止 — unknown
- full_trace_seed42: 已被终止 — unknown
- vota_exception_only_seed42: 训练失败 — unknown
- vota_seed123: 训练失败 — unknown
- vota_seed456: 训练失败 — unknown
- deepseek_exception_only_seed123: 已被终止 — unknown
- deepseek_full_trace_seed42_v2: 已被终止 — unknown
- full_trace_2048tok_seed42: 已被终止 — unknown
- qwen1.5b_exception_only_seed42: 已被终止 — unknown
- qwen1.5b_vota_seed42: 已被终止 — unknown
- qwen1.5b_full_trace_seed42: 已被终止 — unknown
- codellama_exception_only_seed42: 已被终止 — unknown
- codellama_no_trace_seed42: 已被终止 — unknown
- codellama_vota_seed42: 已被终止 — unknown
- codellama13b_nomarker_seed42: 已被终止 — unknown
- codellama13b_full_trace_tail1024_seed42: 训练失败 — unknown
- codellama13b_full_trace_tail2048_seed42: 训练失败 — unknown
- qwen7b_full_trace_tail512_seed42: 训练失败 — unknown
- deepseek_full_trace_tail512_seed123: 训练失败 — unknown
- qwen15b_exception_only_seed123: 训练失败 — unknown
- codellama13b_label_only_seed42: 已被终止 — unknown
- qwen15b_label_only_seed42: 已被终止 — unknown
- deepseek_no_trace_seed123: 已被终止 — unknown
- qwen7b_full_trace_seed456: 训练失败 — unknown
