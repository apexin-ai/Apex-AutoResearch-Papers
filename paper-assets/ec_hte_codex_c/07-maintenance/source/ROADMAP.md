# ec_hte_codex_c — Research Dashboard

> 最后更新: 2026-05-31 17:35 UTC | 更新原因: Reviewer D022 复审 PASS，补充下一轮 CI 修补需新 exp_id/子项

## 核心方向
验证 EC-HTE：当 LLM 生成的分类效应修饰变量存在跨子群差异化误分类，且误分类强度与真实 CATE 异质性相关时，全局混淆矩阵修正可能无法修复、甚至会放大 CATE 偏差；EC-HTE 当前已在 fixed canonical k6 上验证子群 shrinkage 与自适应专家标注分配两个 component。CI/variance component 尚未验证：`variance_propagation_ci_001` 只是 diagnostic negative；`variance_propagation_ci_real_001` 已通过 smoke 审计性但 strict gate negative，不能作为 CI component 成功证据。

## 当前进展
- 原 MVP `mvp_ec_hte_semisynth_001=DONE(negative, verified_negative)`；不得覆盖，不得按原标准 `complete_mvp`。
- `phase_transition_k_sweep_001=DONE(negative)` 已审：stage1 synthetic grid global_worse_count=0/24；不否定 canonical fixed k6 stress/stability positives；phase full grid blocked。旧 formal 输出中的 `smoke_only=true` 是历史 metadata bug，引用时不得称为 smoke。
- `hierarchical_shrinkage_ec_hte_001=DONE(success)` 已通过 Reviewer 文件级审计：fixed canonical k6/B=500 下 shrinkage component 有效；findings 已按跨 seed 均值记录 `empirical_bayes PEHE≈0.1944 < raw_subgroup 0.2025`，未把 `best_shrinkage_pehe_mean=0.1885` 写成均值。
- `adaptive_expert_allocation_001=DONE(success)` 已通过 Reviewer 文件级审计：fixed canonical k6/B=500 且各 arm 等预算下，hybrid 优于 uniform（PEHE 0.1883 vs 0.2025；GATE bias 0.1376 vs 0.1479）。
- `variance_propagation_ci_001=DONE(negative)` 已通过 Reviewer 文件级审计，但结论被收窄：脚本使用硬编码 coverage offset 与 CI width multiplier，不是真实 bootstrap/delta variance propagation；只能作为 diagnostic negative。
- `variance_propagation_ci_real_001=PREPARING`：D020 文件级复审通过审计性/复现性（PSD 双字段、hash manifest、covariance 数值审计均可复核），formal 未启动。但 strict gate=false：k6 bootstrap width multiplier=15.42 且 gain=0，delta width multiplier=3.92 且 coverage_abs_error 变差。D022 决定当前实现不进入 formal，不声明 CI component 成功。
- Reviewer D022 复审 PASS，无 blocking；下一轮 CI 修补/替代必须保留当前 negative/readiness-only 记录。
- GPU 100%/0MiB/no-process 异常仍独立存在；当前实际 GPU 运行 0/1，不得使用 `cuda:0`。

## 近期任务
- [ ] Agent 设计下一轮 CI 修补/替代方案，重点解决 k6 rare-group audit covariance ill-conditioning、width explosion、稀有组 audit counts 低至 3/2 的稳定性问题；只提交方案，不开 formal。
- [ ] 下一轮 CI 修补/替代必须使用新 exp_id 或明确 registry 子项，不得覆盖 `variance_propagation_ci_real_001` 的 strict-gate negative/readiness-only 记录。
- [ ] 可选方案需至少覆盖 2-3 类不同方向：如 covariance regularization/shrinkage、allocation-aware audit covariance、studentized/bootstrap trimming 或 conservative no-CI fallback；每项列 smoke pass/fail 与成本。
- [ ] 若不继续投入 CI component，则在 findings 中明确当前 verified scope 仅为 shrinkage + adaptive allocation，CI component 为 negative/readiness-only，不得静默宣称完整 EC-HTE。
- [ ] 不运行 phase full grid，不 `complete_mvp`，不改写原 MVP negative。

## GPU 预算
- 本项目白名单：`seetacloud-47181:cuda:0`，1 张 96GB GPU。
- 当前实际 GPU 运行：0/1。真实 CI 后续修补仍默认 CPU-only，不分配 GPU。
- 禁止使用白名单外 GPU；如后续需要 GPU，先确认白名单和 GPU 异常状态；不够则走 Manager/用户扩配。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D022 | 2026-05-31 | D020 smoke 通过审计性复审但 strict gate negative，当前真实 CI 方 | variance_propagation_ci_real_001, variance_propagation_ci_001 |
| D021 | 2026-05-31 | D020 smoke 修补完成但 strict gate 仍 false，继续等待文件级复审 | variance_propagation_ci_real_001 |
| D020 | 2026-05-31 | 扩展真实 CI smoke 修补要求：PSD 字段兼容与文件内 hash 闭环 | variance_propagation_ci_real_001 |
| D019 | 2026-05-31 | 真实 CI smoke 未通过方法审计，要求补 covariance 数值审计后重跑 smoke | variance_propagation_ci_real_001, variance_propagation_ci_001 |
| D018 | 2026-05-31 | D017 重跑 smoke strict gate=false，暂不 release formal | variance_propagation_ci_real_001, variance_propagation_ci_001 |
| D017 | 2026-05-31 | 接受 Reviewer 对真实 CI 设计的加严要求，formal gate 继续关闭 | variance_propagation_ci_real_001, variance_propagation_ci_001 |
| D016 | 2026-05-31 | 放行真实 CI variance propagation 的实现与 smoke，不放行 formal | variance_propagation_ci_001, variance_propagation_ci_real_001 |
| D015 | 2026-05-31 | 接受 variance_propagation_ci_001 为 narrowed negative | variance_propagation_ci_001 |
| D014 | 2026-05-31 | Phase negative 仅限 synthetic grid，重放行固定 k6 方法组件 for | phase_transition_k_sweep_001, hierarchical_shrinkage_ec_hte_001, adaptive_expert_allocation_001, variance_propagation_ci_001 |
| D013 | 2026-05-31 | Phase stage1 negative 后暂停其余 D012 formal jobs 等 Rev | phase_transition_k_sweep_001, hierarchical_shrinkage_ec_hte_001, adaptive_expert_allocation_001, variance_propagation_ci_001 |



