# code r8 qwq position control

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r8_qwq_position_control_20260518T070944_result.json`
- **Structured JSON:** [`fddecf39a24886896407.json`](../../sessions/fd/fddecf39a24886896407.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
QwQ-32B Position Control (L60, W=3):

| Method              | Bal_Acc | Precision | FPR   |
|---------------------|---------|-----------|-------|
| HS-only (baseline)  | 0.796   | 0.564     | 0.217 |
| Position-only       | 0.832   | 0.519     | 0.241 |
| Residualized HS (a) | 0.612   | 0.361     | 0.342 |
| HS + Position (b)   | 0.794   | 0.557     | 0.220 |
```

**解读：**

- **Residualized HS << HS-only** (bal_acc 下降 18.3pp, precision 下降 20.3pp, FPR 上升 12.5pp) → **HS probe 严重依赖位置信息**。去掉位置后 HS 几乎丧失判别力，residualized 性能甚至低于 position-only baseline。

- **HS+Position ≈ HS-only** (差异 <0.5pp) → HS features 已经内含位置信息，显式加入 position features 无增量。（注：PCA(500) 在 15362 维中会淹没 2 维 position features，但这恰好反映 HS 本身已编码位置。）

- **结论：QwQ-32B L60 的 HS probe 大部分预测力来自位置信息，而非 safety-specific 的内容信号。** Position-only (0.832) > HS-only (0.796) > Residualized HS (0.612)，说明 HS 中的 content-only 信号很弱。

---
