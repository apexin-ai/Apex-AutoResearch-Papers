# analysis failure mode 5seed update

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_failure-mode-5seed-update_20260516T025031_result.json`
- **Structured JSON:** [`b8891fd3e2f9b3c07757.json`](../../sessions/b8/b8891fd3e2f9b3c07757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 2 已排队（PID 227425），会在训练结束后自动启动。下面是当前可报告的完整结果。

---

## 5-seed Failure Analysis 报告

### 1. 数据可用性

| 条件 | Eval 文件数 | Seeds | 每文件 Episodes | 总 Episodes |
|------|-----------|-------|---------------|------------|
| Vanilla | 5 | 42, 0, 1, 7, 123 | 47 | **235** |
| TaxEI | 5 | 42, 0, 1, 7, 123 | 47 | **235** |
| Random | 5 | 42, 0, 1, 7, 123 | 47 | **235** |

三个条件完全平衡。

### 2. 总体失败率（5-seed balanced）

| 条件 | Total | Failures | Fail Rate | Success Mean ± Std |
|------|-------|----------|-----------|-------------------|
| Vanilla | 235 | 77 | **32.8%** | 67.3% ± 4.7% |
| TaxEI | 235 | 98 | **41.7%** | 58.3% ± 6.5% |
| Random | 235 | 98 | **41.7%** | 58.3% ± 8.7% |

Per-seed:
- Vanilla: s0=68.1%, s1=66.0%, s7=74.5%, s42=61.7%, s123=66.0%
- TaxEI: s0=46.8%, s1=59.6%, s7=61.7%, s42=61.7%, s123=61.7%
- Random: s0=55.3%, s1=46.8%, s7=55.3%, s42=66.0%, s123=68.1%

### 3. Failure Mode 分布（recovery eval 数据，有 trajectory）

由于 clean eval 文件不存 trajectory，暂用 recovery eval（3 seed for V/T, 1 seed for R）：

| Failure Mode | Vanilla (141 ep) | TaxEI (141 ep) | Random (47 ep) |
|-------------|-------------------|----------------|----------------|
| loop_repetition | 22 (15.6%) | **49 (34.8%)** | 6 (12.8%) |
| object_not_found | 13 (9.2%) | 6 (4.3%) | 4 (8.5%) |
| exploration_wandering | 13 (9.2%) | 7 (5.0%) | 6 (12.8%) |
| max_steps_exhaustion | 1 (0.7%) | 0 | 1 (2.1%) |

**TaxEI 的 loop_repetition 率 (34.8%) 是 vanilla (15.6%) 的 2.2 倍，random (12.8%) 的 2.7 倍。** Loop 占 TaxEI 失败的 79.0%。

### 4. 与之前结果对比

| 指标 | 之前（不平衡） | 当前（recovery eval） |
|-----|---------------|---------------------|
| TaxEI loop rate | 17.4% (49/282) | 34.8% (49/141)* |
| Vanilla loop rate | 7.8% (22/282) | 15.6% (22/141)* |
| Random loop rate | 3.2% (6/188) | 12.8% (6/47)* |

*之前用的分母包含 clean eval episodes（无 trajectory → 归入 max_steps_exhaustion），拉低了比例。实际上 loop_repetition 全部来自 recovery eval 的 trajectory 数据。纯 recovery eval 基准下比例更高，但趋势一致：TaxEI >> Vanilla > Random。

### 5. 条件特异性 per-task 分析

**TaxEI 比 Vanilla 多失败 ≥ 2 seeds 的 task（7 个）：**
- pick_and_place_simple: SaltShaker-Cabinet (V:3, T:5), Watch-Safe (V:0, T:3)
- pick_clean: Pan-CounterTop (V:3, T:5), Spatula-Drawer (V:1, T:3)
- pick_cool: Lettuce-CounterTop (V:0, T:4), Pan-CounterTop (V:3, T:5)
- pick_two: PepperShaker-Drawer (V:0, T:4)

TaxEI 额外失败集中在 pick_and_place 和 pick_cool 类 task。

### 6. 待完成

Phase 2（重跑失败 episodes 获取 clean eval trajectory）已排队（PID 227425），等当前训练（~3h 后）完成自动启动。完成后运行：
```bash
python scripts/analyze_failure_modes_5seed.py --combine
```
即可获得 clean eval 的详细 failure mode 分类。

---
