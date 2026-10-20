# 诊断报告：eval_llama_rsft_s42_with_evidence_2048

## 结论：实验已成功完成，监控误判为失败

**根因**：实验实际运行成功（985/985 文档推理完毕，耗时 4h16m），metrics.json 和 predictions.json 均已正常写入。失败标记 "process dead 5× with no sentinel/W&B — auto-resolved as failed" 是监控系统误判——推测原因是该 eval 任务未配置 W&B 且未写 sentinel 文件，监控系统多次检测不到存活信号后自动标记为失败。

## 结果摘要

| 指标 | 值 |
|------|-----|
| F1 | 0.5892 |
| Ign-F1 | 0.5774 |
| Evi-F1 (DREEAM) | 0.4719 |
| Evi-F1 (TP) | 0.8222 |
| EDCR | 0.6143 |
| Format OK | 984/985 (99.9%) |
| Truncated | 90/985 |
| Predictions | 18,129 |

## 部分结果

不适用——全部结果均已完整输出。

## 是否需要重试

**不需要。** 实验已成功，结果完整可用。仅需在 registry 中将该实验状态从 failed 更正为 completed。
