# code exp22 aa early detection

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp22-aa-early-detection_20260520T141852_result.json`
- **Structured JSON:** [`12908b51674ac808368f.json`](../../sessions/12/12908b51674ac808368f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇总：

## exp22 AA OOD Early Detection (plan_002 checkpoints)
已有数据，从 `exp2_actorattack_ood.json` 提取，保存至 `exp22_aa_early_detection.json`：

| Variant | K=1 | K=2 | K=3 | K=5 | Full |
|---------|-----|-----|-----|-----|------|
| 9class | .773±.041 | .855±.048 | .921±.046 | .966±.028 | .972±.026 |
| mlm | .736±.150 | .909±.058 | .945±.039 | .929±.033 | .893±.080 |
| vanilla | .337±.049 | .306±.026 | .284±.011 | .262±.006 | .258±.000 |

## exp25 FITD OOD Early Detection (exp16 checkpoints)
新生成，保存至 `exp25_fitd_early_detection.json`：

| Variant | K=1 | K=2 | K=3 | K=5 | Full |
|---------|-----|-----|-----|-----|------|
| 9class | 1.000±.000 | .997±.005 | 1.000±.000 | 1.000±.000 | 1.000±.000 |
| mlm | .610±.281 | .598±.256 | .654±.302 | .635±.238 | .707±.217 |
| vanilla | .698±.038 | .786±.043 | .791±.057 | .823±.040 | .882±.027 |

**重要说明**：exp25 使用的是 westd-33183 上的 **exp16 checkpoints**，与 AA OOD 使用的 plan_002 checkpoints **不同**，两组数据不能直接对比。9class 在 FITD 上近乎完美（可能 FITD 模式对该模型较易检测，或存在训练数据重叠）。MLM 跨 seed 方差极大（seed 456 几乎随机），需要排查。

---
