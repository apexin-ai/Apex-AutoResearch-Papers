# exec-sim-repair-verifier — Research Dashboard

> 最后更新: 2026-05-23 21:12 UTC | 更新原因: 8 页限制修复确认，CWM s42 ckpt300 已启动，4 GPU 满载

> 核心方向: Execution-free verification formulation comparison (CLS vs CWM vs TRAJ). 详见 paper_framing.md.

## 当前进展
- **阶段**: R17 修复完成 + 8 页限制修复 → 等用户决定提交 R18
- **评分轨迹**: R14/R15 3.0 → R16 3.5 → R17 3.0 (fresh review 回归)
- **Excitement ceiling**: 2.5-3.0/5，empirical comparison 贡献类型的结构性限制
- **实验**: 267 个（152 成功），CWM eval 4 路全部 DDL 前完成
- **论文**: 23 页，正文严格 8 页 ✅，匿名仓库同步至 6dbb8c2

## 近期任务
- [x] R17 写作修复 10 项 + 数据审计修复 2 项
- [x] CLS@400 downsample 3-seed → Appendix O (78.57 ± 0.78%)
- [x] R17 验证审稿（Reviewer 确认全部通过）
- [x] 论文数据一致性检查（50+ 数字交叉核对通过）
- [x] 8 页限制修复（Conclusion 压缩，Reviewer 三次验证通过）
- [x] 匿名仓库同步（6dbb8c2）
- [ ] CWM eval 4 路结果回收 → 如与 Table 2 不一致则更新
- [ ] 等用户决定 → 提交 R18 审稿
- [ ] ARR 提交（DDL 5/25）

## GPU 预算
SeetaCloud 4×RTX 5090 (seetacloud-westd-4x5090) — 全部满载
- GPU 0: CWM s456 ckpt300 reeval bs=8（ETA 05-24 ~20:15 UTC）
- GPU 1: CWM s42 ckpt300 reeval bs=8（ETA 05-24 ~11:00 UTC）
- GPU 2: CWM s123 ckpt300 reeval bs=8（ETA 05-24 ~21:15 UTC）
- GPU 3: CWM ckpt6100 eval（ETA 05-24 ~10:45 UTC）
DDL 后如无 rebuttal 需求 → 服务器可归类 C 释放。

## ⚠️ 风险
- **DDL May 25** — 距离 ~1.5 天，论文就绪
- **CWM 结果未知** — 如与 Table 2 不一致需紧急更新

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D171 | 2026-05-24 | Table 2 CWM 8B 保持 66.48±1.15 不变，新 ckpt300/ckpt6100 | cwm8b-ckpt400-test-eval-v3, cls-downsample-400-s42 |
| D170 | 2026-05-23 | 14B TOST/ROPE values corrected to seed-level analy | — |
| D169 | 2026-05-23 | CLS-TRAJ TOST 使用 seed-level paired t-test (p=0.025 | — |
| D168 | 2026-05-23 | 14B 叙事升级方案定稿：降低 capacity claim 强度，避免 repo-level ov | — |
| D167 | 2026-05-23 | 启动 14B multi-seed (s123, s456) CLS+CWM function-le | cls14b-func-s42-v2, cwm14b-func-s42 |
| D166 | 2026-05-23 | D166: 14B scaling 数据统一用 bf16 精度报告，gap 从 0.21pp 修正为 | cls14b-func-s42-v2, cwm14b-func-s42 |
| D165 | 2026-05-22 | D165: §5.3 baseline 统一 NF4 量化条件，消除跨 scale 比较 confo | 14b-baseline-0shot-3shot-v2, qwen3-0shot-func-baseline |
| D164 | 2026-05-22 | D164: 用统一脚本重跑 8B baseline 消除 confound，§5.3 主叙事聚焦 f | 14b-baseline-0shot-3shot-v2, qwen3-0shot-func-baseline |
| D163 | 2026-05-21 | Qwen CWM eval 采用 batch=4（2.7× 加速），前 200 样本监控精度漂移 | deepseek-cwm-repo-s456-e3-eval, qwen3-8b-cwm-repo-s123-train-v4, qwen3-8b-cwm-repo-s456-train-v3 |
| D162 | 2026-05-21 | Kill DS s456 epoch 2 eval (3.7% done) — 释放 GPU 1 做 | deepseek-cwm-repo-s456-e2-eval, deepseek-cwm-repo-s456-e3-eval |

