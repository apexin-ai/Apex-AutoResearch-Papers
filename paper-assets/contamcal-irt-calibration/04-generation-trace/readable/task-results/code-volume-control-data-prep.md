# code volume control data prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_volume-control-data-prep_20260522T235807_result.json`
- **Structured JSON:** [`737c05af89a70597586f.json`](../../sessions/73/737c05af89a70597586f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

| 项目 | 值 |
|------|-----|
| 脚本 | `/root/contamcal-irt-calibration/exp001/prepare_volume_control.py` |
| 数据 | `/root/autodl-tmp/exp001/sft_data/sft_volume_control.jsonl` |
| 总行数 | 66,533（= d100） |
| 构成 | 50,000 clean SFT + 16,533 MMLU auxiliary_train MCQ |
| 文件大小 | 116 MB |
| MMLU test 重叠 | 8 条（已过滤） |
| ARC test 重叠 | 12 条（已过滤） |
| 格式验证 | 66,533/66,533 通过 |
| Seed | 42 |

Auxiliary MCQ 使用与 contamination items 相同的模板：`Question: ...\nA) ...\nB) ...\nC) ...\nD) ...` + `The answer is X.`（user/assistant 两消息，无 system），base SFT 保持原始三消息格式不变。数据已 shuffle。

---
