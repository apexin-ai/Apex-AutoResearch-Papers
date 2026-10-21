# cpu failure gallery

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_failure_gallery_20260521T071429_result.json`
- **Structured JSON:** [`424b5f39261bf26e5420.json`](../../sessions/42/424b5f39261bf26e5420.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`failure_gallery_examples.json` 已保存到 artifacts 并注册。

**提取结果概要**（扫描 3 个实验，~75k 实例）：

| 类别 | 总数 | 选出 |
|------|------|------|
| Degenerate (全样本一致但错误) | 1,358 | 3 |
| LP Inversion (高 logprob 但非 gold) | 3,827 | 3 |
| ESJ Overconfident | 1,134 | 2 |
| ESJ Underconfident | 6,843 | 1 |

**选出的 9 个实例**：

**Degenerate (F1)**:
1. `fewnerd_test_00469` — "University of Notre Dame" 正确文本但错误类型(org→building)，8/8 一致
2. `fewnerd_test_02015` — "SPQ" 类型混淆(product→org)，8/8 一致
3. `fewnerd_test_16612` — 6 个 gold 实体全漏（空预测），8/8 一致

**LP Inversion (F3)**:
1. `fewnerd_test_01046` — "Cramer"(person) 8/8 出现，logprob=-0.046，但不在 gold 中
2. `fewnerd_test_31667` — "Richard Friend"(person) 8/8 出现，gold 只标注了组织实体
3. `fewnerd_test_28689` — "COMUSMACV"(organization) 8/8 出现，gold 遗漏

**ESJ Failure**:
1. `fewnerd_test_00230` — "American"(location) consensus=100% 但非 gold（overconfident）
2. `fewnerd_test_01046` — "Cramer" consensus=100% 但非 gold（overconfident）
3. `fewnerd_test_00002` — "C-USA play"(event) 0/8 样本预测但确实是 gold（underconfident）

**注意事项**：
- LP inversion 的 3 个例子多为标注遗漏而非纯幻觉——这恰好说明 LP 无法区分两者
- ESJ 用 entity-level consensus frequency 代理，未运行实际 ESJ 模型验证（`exp_esj_entity_self_judgment` 输出不存在）
- `fewnerd_test_01046` 同时出现在 LP inversion 和 ESJ failure 中

---
