# eval exp10 fewshot llm judge

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp10-fewshot-llm-judge_20260518T165106_result.json`
- **Structured JSON:** [`9915988c1a5550d388fe.json`](../../sessions/99/9915988c1a5550d388fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。汇总：

```
            | DD OOD                      | ActorAttack
            | F1     | Prec   | Rec      | F1     | Prec   | Rec
Zero-shot   | 0.000  | 0.000  | 0.000    | 0.000  | 0.000  | 0.000
3-shot      | 0.5405 | 0.9677 | 0.375    | 0.6612 | 0.9756 | 0.500
9-class     | 0.997  | 1.000  | 0.994    | 0.970  | ~1.00  | ~0.94
```

**K 值变化（3-shot）**：

| K    | DD F1  | AA F1  |
|------|--------|--------|
| k1   | 0.025  | 0.280  |
| k2   | 0.161  | 0.316  |
| k3   | 0.384  | 0.491  |
| k5   | 0.416  | 0.633  |
| full | 0.541  | 0.661  |

关键发现：
- 3-shot 大幅优于 zero-shot（从 0.0 到 0.54/0.66），但仍远低于 trained 9-class classifier
- Precision 近乎完美（~0.97-1.0），但 recall 只有 0.375-0.5（漏检 50-60% 的 jailbreak）
- 0 个 unparseable（few-shot examples 帮助模型遵循输出格式）
- ActorAttack 比 DD 更容易被检测到（F1 0.66 vs 0.54）
- 结果保存至 `results/exp10_fewshot_llm_judge.json`，registry 已更新

---
