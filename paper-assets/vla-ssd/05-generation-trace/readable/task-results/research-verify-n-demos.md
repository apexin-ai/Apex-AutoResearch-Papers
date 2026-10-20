# research verify n demos

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_n_demos_20260516T032717_result.json`
- **Structured JSON:** [`436b74d04b28d6c8948e.json`](../../sessions/43/436b74d04b28d6c8948e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 源数据（feature h5 文件中实际 demo 数量）

| Condition | Demos/task | 例外 |
|-----------|-----------|------|
| **trained_with_inst** | **50** | 全部 10 tasks 一致 |
| **untrained_with_inst** | **50** | 全部 10 tasks 一致 |
| **trained_no_inst** | **50 或 10** | cream_cheese, wine_rack, wine_cabinet, stove 仅 10 demos |
| **untrained_no_inst** | **50 或 10** | turn_on_the_stove 仅 10 demos |
| **random_s0** | **50** | 全部 10 tasks 一致 |
| **shuffled** | **50** | 全部 10 tasks 一致 |
| **Action hdf5** | **50** | 全部 10 tasks 一致 |

### unified_rsa_results.json

- `n_sample=20` 是**轨迹时间步采样数**（np.linspace），不是 demo 数
- 代码逻辑（`rsa_unified_vla.py:108-109`）取 feature h5 和 action hdf5 的 demo ID 交集
- **with_inst / random_s0 / shuffled 条件：50 demos/task**
- **no_inst 条件：部分 task 仅 10 demos**（trained_no_inst 有 4 个 task 只有 10，untrained_no_inst 有 1 个只有 10）
- JSON 中**未显式记录 n_demos**

### 其他结果文件

| 文件 | n_demos | 说明 |
|------|---------|------|
| **rsa_demo_standardized.json** | **10/task** | 显式标注 `demos_per_task=10`，仅用 demo_0-9，用于跨模型公平对比 |
| **rsa_siglip_only.json** | 未记录 | 10 tasks |
| **rsa_clip.json** | 未记录 | |
| **rsa_branch_split.json** | 未记录 | N=20 同为时间步采样 |

### 结论

**不是所有数据源都统一使用 50 demos/task：**
1. `trained_no_inst` 有 4 个 task 特征提取不完整（仅 10 demos），`untrained_no_inst` 有 1 个 task 仅 10 demos — 这意味着 unified_rsa_results.json 中这些 task 的 no_inst 条件 RSA 是基于更少的 demo pair 计算的
2. `rsa_demo_standardized.json` 是有意降采样到 10 demos/task 做跨模型对比，这是 by design
3. with_inst、random_s0、shuffled 三组确认全部 50 demos/task

---
