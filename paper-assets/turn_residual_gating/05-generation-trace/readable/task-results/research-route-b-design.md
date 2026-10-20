# research route b design

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_route_b_design_20260519T104143_result.json`
- **Structured JSON:** [`8803a68226680113db7d.json`](../../sessions/88/8803a68226680113db7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/route_b_design.md`。

内容覆盖：
- 三个论文定位选项（推荐 Option A 为主 + B 融入 Discussion）
- 四路消融 eval 设计及预期结果
- 五个机制分析实验（梯度冲突量化、gate profile 深入、attention 可视化、GAR 泛化曲线、训练动力学三阶段）
- Llama-3.1-8B 跨模型验证（Phase 1 + TG 训练 + 可选消融）
- 与 Dongre et al. 的精确互补定位和独特增量
- 论文结构草案 + 贡献列表
- 时间表（核心 ~12h GPU，D+0 到 D+2 完成 Qwen 全部数据）
- 六项风险评估及应急方案

所有实验设计均基于 paper_framing.md 的 NF1-NF4 和 C1-C6 状态。

---
