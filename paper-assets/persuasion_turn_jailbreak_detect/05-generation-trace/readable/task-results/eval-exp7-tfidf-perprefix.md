# eval exp7 tfidf perprefix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp7-tfidf-perprefix_20260518T161655_result.json`
- **Structured JSON:** [`3da87973354389611ec4.json`](../../sessions/3d/3da87973354389611ec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存在 `results/exp7_tfidf_perprefix.json`，registry 已更新。

```
Dataset        | K1     | K2     | K3     | K5     | Full
─────────────────────────────────────────────────────────────
DD OOD         | 1.0000 | 1.0000 | 0.9937 | 1.0000 | 0.9610
ActorAttack    | 0.6325 | 0.7302 | 0.5714 | 0.2418 | 0.2609
```

关键发现：
- **DD OOD**: TF-IDF 全 K 值近乎完美 (0.96-1.0)，说明 Deceptive Delight 的词汇特征足以被表层方法捕获
- **ActorAttack**: TF-IDF 严重失效，F1 从 K2 的 0.73 持续下降到 Full 的 0.26。Precision=1.0 但 Recall 极低 (Full 仅 0.15)，说明 ActorAttack 的角色扮演策略有效规避了词汇级检测器

---
