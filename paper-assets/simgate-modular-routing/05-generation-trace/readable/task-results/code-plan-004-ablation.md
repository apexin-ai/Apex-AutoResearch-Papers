# code plan 004 ablation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-004-ablation_20260514T042558_result.json`
- **Structured JSON:** [`f4533863a694b705531f.json`](../../sessions/f4/f4533863a694b705531f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过验证。最终文件清单和状态：

| 文件 | 状态 |
|---|---|
| `src/training/format_implicit_data.py` | dry-run 成功，1770 条 → 1770 条转换 |
| `src/training/implicit_router_sft.py` | import + parse 测试通过，数据加载 train=1505/val=265 |
| `src/evaluation/prompt_routing_eval.py` | import + parse 测试通过 |
| `src/evaluation/ablation_comparison.py` | import 测试通过 |
| `scripts/launch_plan004.sh` | 已写入服务器，可执行 |

关键数据点：
- **训练数据**：1770 条 labeled steps（11 个 task），det:int = 91.5%:8.5%（严重不平衡）
- **模型权重**：Qwen3-1.7B 和 Qwen2.5-7B-Instruct 都在 `/root/autodl-tmp/models/Qwen/`
- **Plan-002 adapter**：尚未训练，launch 脚本会自动跳过 condition (a)

需要 GPU dry-run 验证训练脚本的话请说明。类别不平衡问题（det 91.5%）可能需要关注 —— implicit router 可能倾向全部输出 `[SIMULATE]` 前缀。

---
