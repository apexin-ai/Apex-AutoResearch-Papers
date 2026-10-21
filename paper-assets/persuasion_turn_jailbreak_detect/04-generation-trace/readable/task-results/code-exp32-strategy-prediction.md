# code exp32 strategy prediction

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp32-strategy-prediction_20260520T193016_result.json`
- **Structured JSON:** [`82419115d19af0f84b6a.json`](../../sessions/82/82419115d19af0f84b6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp32 完成。核心发现：

**DD OOD (Deceptive Delight)**
- 策略预测准确率很低（JB-only: 14.3%），仅 rapport_building 被较好识别（F1=0.57）
- 正确检测的对话策略准确率显著高于漏检（0.163 vs 0.076），相关性显著（r≈0.45, p<0.001）
- 检测率 74.2%（3 seed 平均），所有 DD 对话的主导策略都是 rapport_building

**AA OOD (ActorAttack)**
- 策略预测更差（JB-only: 6.8%），模型严重偏向预测 "none"
- 正确检测 vs 漏检的策略准确率差异仍显著（0.131 vs 0.039），相关性 r≈0.24, p≈0.03
- 不同策略检测率差异大：emotional_manipulation (52%) > authority_appeal (28%) > logical_reframing (27%) > gradual_escalation (17%) > rapport_building (11%)
- 漏检严重：3 seed 分别漏 63/41/66 个（共 80 个 jailbreak）

**结论**：策略预测准确率与检测成功率正相关，但模型在 OOD 数据上的策略预测能力很弱——persuasion head 的主要贡献是通过训练信号改善编码器表征质量，而非通过准确的策略预测本身。

---
