# Handover — 2026-05-14

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **medium_rgds_seed456** (success): GPT2-medium (355M) RGDS seed=456: 3-seed 统计检验，验证 alignment gap 在 355M 跨 seed 一致 ← 基于 medium_rgds_seed42
- **medium_random50_seed456** (success): GPT2-medium (355M) Random 50% seed=456: 3-seed 统计检验，验证 C3 (RGDS 劣于 Random) 在 355M 跨 seed 一致 ← 基于 medium_random50_seed42
- **medium_uncurated_seed456** (success): GPT2-medium (355M) Uncurated seed=456: 3-seed 统计检验，验证 355M collapse 跨 seed 一致性 ← 基于 medium_uncurated_seed42

## 趋势
成功 22 / 负向 2 / 失败 4 / 共 31
gen7_ppl: 86.03 ↑（近 3 次 success）
gen7_rankme: 432.02 ↓（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-11235: 无 GPU 信息

## 告警
- mvp_rgds_v1: 已被终止 — unknown
- mvp_ext_v1: 已被终止 — unknown
- mvp_rgds_v2: 训练失败 — unknown
- mvp_ext_v2: 训练失败 — unknown
- mvp_rgds_v3: 训练失败 — unknown
- mvp_serial_v3: 已被终止 — unknown
- phase2_random50_baseline: 训练失败 — unknown
