# code mvp implementation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_implementation_20260516T184012_result.json`
- **Structured JSON:** [`e0c822df82655d0e69ac.json`](../../sessions/e0/e0c822df82655d0e69ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

**已创建文件：**
- `src/config.py` — 集中配置
- `src/data_loader.py` — 加载 HarmThoughts，提取 commitment point（使用 `llm_annotation` 字段）
- `src/extract_hidden_states.py` — 模型 forward pass 提取 hidden states
- `src/baselines/linear_probe.py` — 静态 linear/MLP probe
- `src/crta/temporal_probe.py` — 5-step 时序窗口 MLP probe
- `src/eval/evaluate.py` — step accuracy, earliest reliable detection, lead time
- `src/run_pipeline.py` — 主入口（`--step extract/train/eval/all`）
- `requirements.txt`

**Commitment Point 分布关键数据：**

| 指标 | 值 |
|------|---|
| 覆盖率 | 78.9% (209/265) ✓ |
| CP 绝对位置 mean/median | 34.4 / 34.0 |
| CP 相对位置 mean/median | 70.5% / 86.1% |
| [90%-100%) 区间 | 41.6% (87 traces) |
| 步骤标签平衡 | 74.5% pre / 25.5% post |

**注意事项：**
- 分布是双峰的：18.2% 早期 CP + 41.6% 末尾 CP，中间稀疏
- 41.6% 的 trace CP 在最后 10% 处——temporal probe 对这些 trace 的提前检测能力有限
- 训练时建议用 class weighting 缓解 3:1 的类别不平衡

---
