# analysis r6w3 training curves extraction

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r6w3-training-curves-extraction_20260521T014518_result.json`
- **Structured JSON:** [`ebede7224eb70a57ea55.json`](../../sessions/eb/ebede7224eb70a57ea55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| 覆盖率 | **68/75** 组合 |
| 数据文件 | `westd-29999:/root/contamcal-irt-calibration/artifacts/training_curves/training_curves_data.json` (4.1MB) |
| 提取脚本 | `westd-29999:/root/contamcal-irt-calibration/scripts/extract_training_curves.py` |
| Artifact ID | `art_20260521_5fc135` |

**每条曲线数据点数**（与 dosage 正相关，因为更高 dosage 训练样本更多）：
- d000: 312 pts, d005: 317 pts, d025: 338 pts, d050: 364 pts, d100: 415 pts

**缺失 7 个组合**（训练目录存在但 checkpoint 为空）：
- Qwen-7B: s0 全部 5 个 dosage
- Qwen-14B: d050/s0
- Gemma-2: d100/s0

**数据质量**：所有 68 条曲线 loss 均单调递减（first > last），无异常突增。起始 loss 按家族分层明显：Gemma-2 最高（~5.5-5.8），OLMo-2（~2.1-2.4），Phi-4（~1.5-1.7），Qwen-14B/7B（~1.3-1.6）。

---
