# ops roadmap update

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_roadmap-update_20260513T072041_result.json`
- **Structured JSON:** [`fd7f6de1145163246e09.json`](../../sessions/fd/fd7f6de1145163246e09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是完整检查结果。

---

## 1. ROADMAP 已完成/待完成项

### 应标记为 ✅ 的项（ROADMAP 中仍为 `[ ]`）

| 任务 | 当前状态 | 证据 |
|------|---------|------|
| 新服务器环境搭建 | ✅ 已完成 | m2_embed_verify + plan_013_starcoder 已在 bjb1-42106 运行 |
| True embedding mining 实现 | ✅ 已完成 | m2_embed_verify 使用真正 embedding mining，strategy_divergence=96.1% |
| plan_006 初步 stats | ✅ 已完成 | 用户确认 artifact 已注册 |
| M2 early pilot 收集结果 | ✅ 已完成 | m2_early_pilot DONE/killed，metrics 已记录 |

### 仍在进行中

| 任务 | 状态 | 备注 |
|------|------|------|
| M1 全量提取 | 🔄 27% | cqa1-21977, 36/131 repos, ETA 5月14日下午 |
| M2 全量训练 (m2_embed_verify) | 🔄 运行中 | bjb1 cuda:1, step 50, loss=0.5669 |
| plan_013 StarCoder2 | 🔄 运行中 | bjb1 cuda:0, step 500/820 epoch 1, ETA ~1.9h |

### 待完成

| 任务 | 依赖 |
|------|------|
| M1 数据迁移到新服务器 | M1 完成后 |
| 通知 Manager 释放 cqa1-21977 cuda:4 | M1 完成后 |
| Registry 清理 | 见下方 |

---

## 2. Registry 状态一致性检查

### 状态不一致（需修复）

| 实验 | 当前状态 | 实际状态 | 问题 |
|------|---------|---------|------|
| **plan_013_starcoder** | PREPARING | 实际在跑（PID 23810, step 500, GPU 100%） | 应为 RUNNING |
| **m2_embed_verify** | ALLOCATED | 实际在跑（PID 29302, step 50, GPU 95%） | 应为 RUNNING |

### killed/failed 缺少 notes 的实验

| 实验 | conclusion | notes |
|------|-----------|-------|
| p2b_eval_all | killed | ❌ 无 notes |
| p2b_dataflow_retrain | negative | ❌ 无 notes（spec 有 "BLOCKED" 描述但 notes 字段空） |
| mvp_p2b_contrastive_v2 | killed | ❌ 无 notes |

p2b-smoke-test ~ p2b-smoke8（8 条）和 p2b-all-9runs 虽无 notes，但 spec 标记为 "obsolete smoke test"，可接受。这 **11 条 obsolete 实验** 是潜在的清理对象。

---

## 3. experiment_plan 关联检查

### 已关联 registry_id ✅

| plan_id | registry_id | registry 状态 | 一致性 |
|---------|-------------|--------------|--------|
| plan_001 | m1_extraction | RUNNING | ✅ |
| plan_002 | m2_embed_verify | ALLOCATED (应为 RUNNING) | ✅ 关联正确，状态需修 |
| plan_013 | plan_013_starcoder | PREPARING (应为 RUNNING) | ✅ 关联正确，状态需修 |

### 应关联但缺失 registry_id

| plan_id | 描述 | 原因 |
|---------|------|------|
| **plan_006** | M1 scalability statistics | 用户确认已完成且 artifact 已注册，但 plan 无 registry_id |

### 无需关联（尚未启动）

plan_003, plan_004, plan_005, plan_007–012, plan_014–017 — 均未启动，暂不需要 registry_id。

---

## 建议修复项

1. **更新 ROADMAP**：4 个已完成项标记为 `[x]`
2. **修正 registry 状态**：plan_013_starcoder → RUNNING，m2_embed_verify → RUNNING
3. **补充 notes**：p2b_eval_all、p2b_dataflow_retrain、mvp_p2b_contrastive_v2
4. **plan_006 关联**：在 experiment_plan.yaml 添加 registry_id
5. **可选清理**：11 条 obsolete smoke test 实验可归档/删除

需要我执行其中哪些修复？

---
