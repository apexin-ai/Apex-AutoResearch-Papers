# data additional figure extraction

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_additional-figure-extraction_20260516T202421_result.json`
- **Structured JSON:** [`1f9daded4ca663e911ca.json`](../../sessions/1f/1f9daded4ca663e911ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出摘要：

**数据提取结果：**

| 图 | 文件 | 状态 |
|---|---|---|
| Fig 3: Actor Entropy Dynamics | `artifacts/analysis/entropy_dynamics_data.json` | 4 实验，6-11 点/条 |
| Fig 4: CIVO Decomposition | `artifacts/analysis/civo_decomposition_data.json` | 6 条件，含 value_mean + eval_return |
| Fig 5: Value vs Eval Return | `artifacts/analysis/value_vs_eval_data.json` | 4 实验，全部有双指标 |
| Fig 6: Subsample Distribution | **跳过** | gate_dt 全为常量 (dt=2, frac=1.0)，无可视化价值 |

**关键发现：**
- **008d (CIVO)**: value_mean 升至 137.9 而 eval 降至 82.7（NVE=+55），训练在 55K 步崩溃终止
- **008e_v3_s2 (Pathway B)**: entropy 在 85K→105K 从 -5.21 回升至 -3.83（entropy rebound），eval 从 715→137 崩溃
- **008f/018v2/008a (健康)**: value 始终低于 eval，NVE 为负值
- **010b (Cheetah)**: eval 在 45K 后从 322 降至 52，跨域 CIVO 确认

**matplotlib 脚本**：`artifacts/scripts/gen_additional_figures.py`，在服务器执行：
```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon
python gen_additional_figures.py --datadir artifacts/analysis --outdir artifacts/figures
```

---
