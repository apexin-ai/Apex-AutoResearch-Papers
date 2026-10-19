# error_diag_dpo_recovery — Research Dashboard

> 最后更新: 2026-05-13 08:19 UTC | 更新原因: D033: v9 启动，put→move 修复成功，3 GPU 并行收集

## 核心方向
ETADN：agent 轨迹偏离位置（divergence timing）决定纠正难度。将 DPO 的单一 γ 替换为 per-pair adaptive γ(d)，d = divergence position。早偏离 → 重折扣，晚偏离 → 轻折扣。

公式：γ(d) = γ_min + (γ_max - γ_min) × d，γ_min=0.85, γ_max=1.0。

## 立项风险评估
- **Verdict**: KILL_triage（19% 接受率），Novelty 弱
- **D029 风险**: 80%+ failures 集中在 early divergence → P2 统计效力受限

## 当前进展
- 阶段：MVP 验证（Day 2）— **数据收集恢复**
- GPU：3×RTX 4090D（cuda:0/1/4）— v9 ICL 运行中
- v5: expert data ✓ (2707 experts)
- v6: 灾难前 ~63% SR，代码已丢失
- v7: D030 kill（temp regression, 5.1%）
- v8: D031 kill（0% SR, put in/on 格式 bug）
- **v9: 运行中**（D033 TextWorld 1.7.0 put→move 修复, dry-run 100% SR, 3 GPU 并行）
  - ETA: ~3-4h（May 13 ~12:00 UTC）
- γ(d) 代码：本地+服务器已同步 ✓
- DPO 训练代码：已同步 ✓

## MVP Pass/Fail 标准（D029）
- **P2（唯一 gate）**: ETADN > best single-γ DPO ≥ 3% SR（3 seeds 平均）
- P2 Fail → 终止或 pivot

## 时间线（May 12-25，3×4090D）
- Day 1 (May 12): ✓ 环境 → expert 数据 → D028/D029 → DPO 代码
- Day 2 (May 13): v7/v8 kill → D033 put→move 修复 → **v9 运行中**
- Day 2-3 (May 13-14): v9 完成 → DPO pair 构建 → Phase 1（3 GPU 并行）
- Day 4 (May 15): Phase 2（best-γ × 3 seeds）
- **Day 5 (May 16): MVP gate — P2 评估**
- Day 6-10: 扩展实验（如 P2 pass）
- Day 10-13 (May 22-25): 写作收尾

## 近期任务
- [x] v8 根因诊断 → TextWorld 1.7.0 put→move API 变更
- [x] translate_action 修复 + dry-run 验证（2/2, 100%）
- [ ] v9 ICL 全量完成（3 GPU 运行中, ETA ~3-4h）
- [ ] v9 完成后：build_dpo_pairs.py --gamma_mode continuous
- [ ] Phase 1: 3 GPU 并行（ETADN + γ sweep）
- [ ] Phase 2: best-γ × 3 seeds
- [ ] P2 MVP gate 评估

## GPU 预算
当前：3×RTX 4090D（cuda:0, cuda:1, cuda:4）— 全部在用

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D034 | 2026-05-13 | P2 gate 保持不变，但预注册 γ sweep 作为独立贡献——双轨成功标准 | datagen_v9_icl_cuda0 |
| D033 | 2026-05-13 | D032 更新：v8 0% SR 根因修正为 `put X in/on Y` 格式被 ALFWorl | datagen_v8_icl_cuda0, datagen_v7_icl_cuda0 |
| D032 | 2026-05-13 | v8 0% SR 根因确认：episode boundary bug（ALFWorld auto-r | datagen_v8_icl_cuda0, datagen_v8_icl_cuda1 |
| D031 | 2026-05-13 | Kill v8 ICL（0% SR），灾难恢复重建脚本有深层 bug，temperature 非唯一 | datagen_v8_icl_cuda0, datagen_v8_icl_cuda1, datagen_v7_icl_cuda0, datagen_v7_icl_cuda1 |
| D030 | 2026-05-13 | Kill v7 ICL 收集（temperature 回归 bug），重启 v8 with temp | datagen_v7_icl_cuda0, datagen_v7_icl_cuda1 |
| D029 | 2026-05-12 | P1 gate 撤销：correction_span 与 divergence_position 是 | datagen_classify_v2 |
| D028 | 2026-05-12 | P1 pivot：从 error TYPE taxonomy 改为 divergence TIMIN | datagen_classify_v2, datagen_traj_v5_cuda0 |
| D027 | 2026-05-12 | P1 pivot: 从 error TYPE taxonomy 改为 divergence TIMI | datagen_classify_v2, datagen_traj_v5_cuda0, datagen_traj_v5_cuda1 |
| D026 | 2026-05-12 | P1 taxonomy 澄清：step-1 divergence 归类为 planning erro | datagen_classify_v2, datagen_traj_v5_cuda0, datagen_traj_v5_cuda1 |
| D025 | 2026-05-12 | P1 FAIL recovery：三路并行——v6 ICL + 分类 prompt 去 span h | datagen_traj_v5_cuda0, datagen_traj_v5_cuda1, datagen_classify_v2 |

