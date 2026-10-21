# research ga verify urgent

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ga-verify-urgent_20260514T113021_result.json`
- **Structured JSON:** [`6e193e5e3ab59f38ae6d.json`](../../sessions/6e/6e193e5e3ab59f38ae6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到关键证据。旧版脚本 (.bak) 第 270 行硬编码了 `gradient_accumulation_steps=max(1, 32 // args.batch_size)`。当 batch_size=4 时，32 // 4 = **8**。

## 结论

| Run | checkpoint_path | ga (config) | ga (argparse default) | total_steps | 反推 ga | 结论 |
|-----|----------------|-------------|----------------------|-------------|---------|------|
| ablation-b | `plan-004-implicit` | **缺失** | 1（当前版本） | 165 | ceil(1735/32)×3=165 → **ga=8** | **ga=8** |
| seed123 | `ablation-b-seed123` | **8** | 1 | 165 | 同上 → **ga=8** | **ga=8** |
| seed456 | `ablation-b-seed456` | **8** | 1 | 165 | 同上 → **ga=8** | **ga=8** |
| seed789 | `ablation-b-seed789` | **8** | 1 | 165 | 同上 → **ga=8** | **ga=8** |

**最终结论：ablation-b 实际使用 ga=8，Reviewer 的声称不成立。**

证据链：
1. **total_steps=165** — 所有 4 个 run 均为 165 步，唯一匹配的组合是 1735 samples / batch_size=4 / ga=8 / 3 epochs = ceil(1735/32)×3 = 55×3 = 165
2. **旧版脚本硬编码** — `implicit_router_sft.py.bak` 第 270 行：`gradient_accumulation_steps=max(1, 32 // args.batch_size)` = max(1, 32//4) = **8**。ablation-b 训练时使用的就是这个版本
3. **seed 变体显式确认** — 三个 seed 变体的 train_config.json 均明确记录 `gradient_accumulation_steps: 8`
4. **config 缺失原因** — ablation-b 的 train_config.json 没有 ga 字段，是因为当时 ga 是脚本内计算值（非 argparse 参数），`vars(args)` 不包含它。后来重构为 argparse 参数后，seed 变体才有此字段

Effective batch size 始终为 4 × 8 = 32。论文 §4.4 的因果声明成立。

---
