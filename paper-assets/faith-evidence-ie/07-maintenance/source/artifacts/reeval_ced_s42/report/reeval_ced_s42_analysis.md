# reeval_ced_s42 结果分析

## 实验配置
- 模型: Qwen3-4B + SFT adapter + CED RSFT checkpoint-510 (lora_alpha=128, 510步)
- 协议: batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024, seed=42
- 数据: DocRED dev set (985 docs, 12275 gold triples)
- 推理时间: 10815.5s (~3h)
- 服务器: rtx5090-4x

## 关键指标

| 指标 | reeval_ced_s42 |
|------|---------------|
| F1 | 0.4517 |
| Ign-F1 | 0.4423 |
| Evi-F1 | 0.8174 |
| EDCR | 0.6569 |
| Evi-F1-Joint | 0.3518 |
| Format OK | 985/985 (100%) |
| Truncated | 214/985 (21.7%) |
| Predictions | 15,436 |

## 与旧 eval 对比 (rsft_r2b_maxtok1536)

旧 eval 使用了不同 checkpoint (rsft_output_r2b) + batch_size=8 + max_new_tokens=1536。

| 指标 | reeval_ced_s42 | 旧 eval (r2b_1536) | 差异 |
|------|---------------|-------------------|------|
| F1 | 0.4517 | 0.4504 | +0.13pp |
| Ign-F1 | 0.4423 | 0.4504* | -0.81pp |
| Evi-F1 | 0.8174 | 0.8102 | +0.72pp |
| EDCR | 0.6569 | 0.6740 | -1.71pp (↑好) |
| Evi-F1-Joint | 0.3518 | 0.3488 | +0.30pp |
| Format OK | 100% | 99.8% | +0.2pp |
| Truncated | 214 | 146 | +68 |
| Predictions | 15,436 | 17,188 | -1,752 |

*注: 旧 eval 的 Ign-F1 = F1（ign_precision = precision），疑似 Ign 计算有误。

## CED 跨 seed 对比 (统一协议)

| 指标 | s42 | s43 | s45 | Mean | Std |
|------|-----|-----|-----|------|-----|
| F1 | 0.4517 | 0.4601 | 0.4514 | 0.4544 | 0.0050 |
| Ign-F1 | 0.4423 | 0.4512 | 0.4416 | 0.4450 | 0.0054 |
| Evi-F1 | 0.8174 | 0.8063 | 0.8174 | 0.8137 | 0.0064 |
| EDCR | 0.6569 | 0.6542 | 0.6550 | 0.6554 | 0.0014 |
| Evi-F1-Joint | 0.3518 | 0.3605 | 0.3558 | 0.3560 | 0.0044 |

## 日志状态
- EXIT_CODE=0，无 error/traceback
- 214/985 truncated (21.7%)，0 errors
- 格式合规率 100%
