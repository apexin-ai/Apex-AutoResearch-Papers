# analysis v7 success rate diagnosis

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v7-success-rate-diagnosis_20260513T064019_result.json`
- **Structured JSON:** [`f271a0fdc42ba5b3e3b2.json`](../../sessions/f2/f271a0fdc42ba5b3e3b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`translate_action` 在两个脚本的当前服务器版本中都不存在（都是灾难恢复后重建的版本）。现在有足够证据写诊断报告了。

---

## v7 ICL 成功率诊断报告

### 当前状态
- cuda0: **5/65 = 7.7%**，cuda1: **2/63 = 3.2%**，合计 **7/128 = 5.5%**
- v6 同阶段: cuda0 54/85 (63.5%), cuda1 63/90 (70.0%)，合计 66.9%
- **性能下降 >10x**

### 诊断 1: ICL few-shot examples 加载状态

**结论: 正常加载。**

证据:
- 日志确认: `Loaded 2707 expert examples across 6 task types`
- 每个 trajectory 有 26-32 条 ICL 消息（2 个 ICL example × ~14 turns/example）
- 模型输出格式正确（Thought + Action），所有 40 步都有 `Action:` 行（截断率 = 0）
- Nothing happened 率极低（30/1200 = 2.5%）

### 诊断 2: Step-1 divergence 和失败模式

**结论: 模型执行随机探索，几乎所有失败都跑满 40 步上限。**

证据（首条失败 trace, pick_clean_then_place potato）:
- Step 1-10: 逐个检查 drawer 1-5（暴力搜索）
- Step 36-40: 仍在遍历 cabinet 15-16
- 成功仅限简单任务: look_at_obj (4次), pick_cool_then_place (1次)

模型动作格式正确但策略低效——没有跟随 ICL 示例的高效策略，而是做暴力遍历。

### 诊断 3: v6 vs v7 参数差异

| 差异项 | v6 原始 | v7 重建 | 影响 |
|--------|---------|---------|------|
| **temperature** | **0.5**（脚本默认） | **0.7**（脚本默认） | **主因** |
| expert 过滤 | 无 max_turns 限制 (3119 条) | max_turns=30 (2707 条) | 次要 |
| v7 cuda1 `--gpu` | `--gpu 1` | `--gpu 0`（误配） | 可能影响 |

关键证据来源: `worker_code_d021_icl_v6_prep` 结果中的对比表：
> | | collect_trajectories.py | collect_trajectories_icl.py |
> | temperature | 0.7 | **0.5** |

v6 和 v7 的命令行**都没有**显式传 `--temperature`，所以都依赖脚本默认值。灾难恢复重建脚本时，temperature 默认值从 0.5 被错误地改为 0.7。

### 根因分析

**主因: 灾难恢复重建 `collect_trajectories_icl.py` 时，temperature 默认值从 0.5 回归到 0.7。**

在 ALFWorld 多步决策任务中，temperature 0.5→0.7 造成指数级性能下降：
- 每步决策增加随机性 → 偏离 ICL 示范的高效策略
- 错误在 40 步中不断累积（compound error）
- 暴力搜索需要 >>40 步，而 budget 只有 40 步
- 只有最简单的 look_at_obj（4-17 步即可完成）还能偶尔成功

次因: v7 cuda1 配置了 `--gpu 0` 而非 `--gpu 1`，两个进程争抢同一张 GPU（虽然未 OOM 但可能影响推理质量）。

### P2 gate 影响评估

如果不修复 temperature，最终 600 条数据中预计只有 ~33 条 success（5.5%），~567 条 failure。对比 v6 预期 ~400 success + ~200 failure。
- **DPO pair 数量严重不足**：v7 success 仅 ~33 条 vs v6 ~400 条
- 失败模式过于单一（全是 step-1 random exploration），无法产出 v6 那样的多样化错误模式
- P2 gate 需要足够的 success/failure pair 和多样化 divergence 分布，当前数据不可用

### 修复建议

**需要停止当前收集并修复后重启。** 修改一行代码即可：

```python
# 文件: src/collect_trajectories_icl.py, line 348
# 当前: parser.add_argument("--temperature", type=float, default=0.7)
# 修复: parser.add_argument("--temperature", type=float, default=0.5)
```

或者不改代码，在启动命令中显式传 `--temperature 0.5`，同时修复 cuda1 的 `--gpu 0` → `--gpu 1`。

---
