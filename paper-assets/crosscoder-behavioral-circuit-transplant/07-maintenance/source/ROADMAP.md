# 研究路线图：Crosscoder-Guided Behavioral Circuit Transplantation

> 最后更新: 2026-05-10 16:06 UTC | 更新原因: MVP kill criteria 触发，等待用户 kill/pivot 决策

## 核心假设

跨模型稀疏 crosscoder 可识别"donor-exclusive features"，通过权重手术将行为能力移植到 target 模型。

## 当前状态：⛔ MVP KILL CRITERIA 触发，等待用户决策

### 系统性失败证据

| 实验 | 稀疏机制 | L0 | Gate 3 (机制) | Gate 5 (行为) | 核心发现 |
|------|---------|-----|-------------|-------------|---------|
| A-001 | ReLU+L1(1e-3) | 457.6 | 0.62% ✗ | -0.28% ✗ | 代码 bug + L0 过高 |
| A-003v2 | 复用A-001 | 457.6 | **71.9% ✓** | 全负 ✗ | 机制可行但行为不转化 |
| A-002 | ReLU+L1(5e-2→1e-1) | 582→515 | — | — | L0 对 L1 不敏感，架构瓶颈 |
| A-005 | TopK(K=50) | 50 | 49.1% ✗ | 全负 ✗ | 稀疏反而更差，Gate 1 也 FAIL |

**结论**：单特征 crosscoder-guided surgery 方法论层面失败。Gate 5 跨~50 组组合从未通过。

### 失败根因分析

1. Crosscoder 能识别 donor/target 差异（Gate 2 一直 PASS）
2. Bias injection 能产生机制性移动（A-003v2 Gate 3 PASS 71.9%）
3. 但移动方向与行为改善无关/反相关（Gate 5 始终为负）
4. 稀疏性不解决此问题——TopK 反而更差
5. 核心问题：**行为能力依赖分布式电路，单特征干预信噪比不够**

### 用户决策待定（三选一）

- **A. Kill 项目**
- **B. Pivot 多特征联合 rank-K（再给 4h）**
- **C. Pivot 梯度引导手术（失去 novelty）**

## 进展摘要

- [05-10] A-001 NEGATIVE（代码 bug）
- [05-10] A-003v2 H2 partially confirmed（mechanism ✓, behavior ✗）
- [05-10] A-002 架构瓶颈（ReLU+L1 无法控制 L0）
- [05-10] A-005 TopK FAIL（稀疏反而更差，kill criteria 触发）
- [05-10] 等待用户 kill/pivot 决策

## GPU 预算

累计用量：~8h（A-001 ~ A-005 + 环境搭建）
状态：GPU 空闲，等待决策

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D005 | 2026-05-10 | mvp-A-005 TopK FAIL + Gate 5 跨 4 实验系统性失败，单特征 cross | mvp-A-005, mvp-A-001, mvp-A-003, mvp-A-002 |
| D004 | 2026-05-10 | A-002 暴露架构瓶颈：ReLU+L1 无法达到目标稀疏度，切换 TopK crosscoder  | mvp-A-002, mvp-A-001 |
| D003 | 2026-05-10 | mvp-A-001 代码有两个 bug（Gate 1 漏检 L0 + 特征选择选最弱特征），实验结论 | mvp-A-001 |
| D002 | 2026-05-10 | MVP-A-001 NEGATIVE：批准 A-002(高稀疏度) + A-003(残差流bias) | mvp-A-001 |
| D001 | 2026-05-10 | 修正 donor/target 方向：Donor=强模型(late/large)，Target=弱模 | mvp-A-001 |


