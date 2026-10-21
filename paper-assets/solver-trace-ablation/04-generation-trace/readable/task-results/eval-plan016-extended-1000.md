# eval plan016 extended 1000

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan016-extended-1000_20260514T081256_result.json`
- **Structured JSON:** [`20c9528bbf0ba6ad8087.json`](../../sessions/20/20c9528bbf0ba6ad8087.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

## plan016-extended-1000-s42 评估结果

### 500 vs 1000 步对比 (eval_sta.py)

| 指标 | plan001-s42 (500步) | plan016 (1000步) | 变化 |
|------|-------------------|-----------------|------|
| eval PR | 0.93 | **0.96** | +3.2% |
| eval ISR | 0.123 | **0.0027** | **-97.8%** |
| proved_only ISR | 0.132 | 0.0028 | -97.9% |
| components | 6.58 | **18.55** | +182% |
| ISR=0 ratio | — | 94.8% | — |
| median ISR | — | 0.0 | — |

### Windowed 训练曲线

| Steps | PR | ISR |
|-------|-----|------|
| 1-100 | 0.190 | 0.0859 |
| 101-200 | 0.660 | **0.1115** (peak) |
| 201-300 | 0.838 | 0.0985 |
| 301-400 | 0.907 | 0.0540 |
| 401-500 | 0.927 | 0.0433 |
| 501-600 | 0.963 | 0.0408 |
| 601-700 | 0.965 | 0.0200 |
| 701-800 | 0.988 | 0.0178 |
| 801-900 | 0.978 | 0.0170 |
| 901-1000 | 0.981 | 0.0144 |

### 结论: **success** — 确认 ISR 崩塌持续恶化

1. **PR↑ 但 ISR→0**: 模型更擅长"证明"，但推理忠实度降至近零。94.8% 的证明没有任何必要组件。
2. **非经典同义反复崩塌**: component_count_2_ratio=0（不是简单的 2-component 同义反复），而是矛盾爆炸式崩塌——模型在大量无关前提中嵌入 P(a) 和 ¬P(a) 形成矛盾，使任何结论都可证。
3. **ISR 单调递减，无回升信号**: 从 step 200 的 0.1115 一路降至 step 1000 的 0.0144，500 步时的 ISR=0.123 不是底部而是崩塌过程中的快照。
4. **论文意义**: 延长训练是 exec-only reward hacking 随时间恶化的干净消融证据。

---
