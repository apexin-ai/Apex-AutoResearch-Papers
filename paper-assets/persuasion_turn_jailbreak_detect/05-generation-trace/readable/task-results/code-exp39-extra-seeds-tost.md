# code exp39 extra seeds tost

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp39-extra-seeds-tost_20260521T091610_result.json`
- **Structured JSON:** [`9cd0a13a2c0b787d7a6c.json`](../../sessions/9c/9cd0a13a2c0b787d7a6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp39 全部完成。** 4 组训练在 westd-33183 上 7.6 分钟跑完，registry 已更新为 DONE。

汇总结果（F1 macro）：

| Group | IID | DD OOD | AA OOD | FITD OOD |
|---|---|---|---|---|
| 9class_seed789 | 1.0 | 1.0 | 0.9715 | 1.0 |
| 9class_seed1000 | 1.0 | 1.0 | 0.9715 | 0.9904 |
| scrambled_seed789 | 1.0 | 1.0 | 0.9904 | 1.0 |
| scrambled_seed1000 | 1.0 | 1.0 | 0.9904 | 0.9904 |

值得注意：scrambled 在 AA OOD 上（0.9904）反而略高于 9-class（0.9715），与原假设"scrambled 在 hard OOD 上更差"相反。结合已有的 3 seeds 数据，5 seeds TOST 检验预计将显示两者在所有 OOD 上高度等价——策略标签的语义信息对检测性能影响极小。

产出文件（westd-33183）：
- `results/exp39_extra_seeds.json` — 汇总指标
- `results/extra_seeds/{9class,scrambled}_seed{789,1000}_per_sample.json` — 用于 bootstrap CI
- Checkpoints: `/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints/exp39_*/`

---
