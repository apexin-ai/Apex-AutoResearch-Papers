# afford_invar — Research Dashboard

> 最后更新: 2026-05-20 01:39 UTC | 更新原因: Path C 执行，项目终止（D014）

## 核心方向
在 VLA 内部通过纯自监督信号（指令释义不变性 + 跨物体 affordance 迁移）学习 spatial affordance 表征，无需任何 affordance 标注。基于 OpenVLA-OFT + 轻量 affordance decoder (~1.7M params)。

## 当前进展
- **阶段**: MVP 验证 — **Path C 终止（D014）**
- **结论**: 核心假设未通过 MVP 验证。四轮实验（L_consist / L_transfer v1/v2/v3）全部 NEGATIVE。

## MVP 验证结果

### 失败路径总结
| 实验 | 正对策略 | 空间表示 | L_xfr@1000 | 失败根因 |
|------|---------|---------|-----------|---------|
| Phase 1a | — | — | — | L_consist trivial minimum at uniform |
| v1 | SigLIP cross-task | global avg pool | 4.174 | 空间信息被摧毁 |
| v2 | SigLIP cross-task | spatial grid + proj | 4.174 | LIBERO-Goal 10 条指令无正对 |
| v3 | paraphrase pairs | spatial grid + proj | 4.174 | 正对存在仍 chance level |

### 系统性结论
三种正对策略 × 两种空间表示 = 全部收敛到 log(65)=4.174（InfoNCE chance level）。Decoder + projection head + InfoNCE + temperature=0.07 组合存在退化解。问题不在数据/实现，是方法论本身在 LIBERO-Goal + OpenVLA-OFT 设置下无法工作。

## OFT Baseline
phase1_oft_baseline_v2: 20000 步完成，checkpoint 可用。未做 SR/PRIDE eval（项目终止）。

## GPU 预算
- MVP 总消耗: ~15h
- 服务器: westd-19957, 4× RTX PRO 6000 (96GB) — 待释放

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D014 | 2026-05-20 | Path C 执行：终止项目。四轮实验 L_xfr 全部锁死 log(65)=4.174，核心假设未 | phase1_transfer_v3, phase1_transfer_v2, phase1_transfer_v1, phase1_lconsist_v1 |
| D013 | 2026-05-20 | L_transfer 正对不足归因于 LIBERO-Goal 指令多样性不足（10 条中仅 1 对  | phase1_transfer_v2 |
| D012 | 2026-05-20 | D011 Path C 条件触发但暂缓执行，给 30min 验证窗口：heatmap eval +  | phase1_transfer_v2 |
| D011 | 2026-05-19 | L_transfer 2000步 chance-level 归因于 spatial_normaliz | phase1_transfer_v1 |
| D010 | 2026-05-19 | Phase 1b 先跑纯 L_transfer（隔离效果），确认有效后再加 L_consist 做联 | phase1_lconsist_v1 |
| D009 | 2026-05-19 | L_transfer pair mining threshold 从 0.85 降至 0.80，Ph | phase1_lconsist_v1 |
| D008 | 2026-05-19 | Phase 1 Path A 失败，触发 Path B：L_consist-only → L_con | phase1_lconsist_v1 |
| D007 | 2026-05-19 | Phase 1 训练前移除 entropy 正则项（lambda_H=0）：当前实现鼓励均匀分布，是 | — |
| D006 | 2026-05-19 | 多层扫描确认所有层（4/8/12/24/30）均远低于 0.1 KL 阈值，维持 layer 18  | — |
| D005 | 2026-05-19 | Phase 0 判定 MARGINAL：Tier-2+ 73.8% 通过，但 image token | — |


