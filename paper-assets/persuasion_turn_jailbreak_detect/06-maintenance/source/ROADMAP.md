# persuasion_turn_jailbreak_detect — Research Dashboard

> 最后更新: 2026-05-23 16:57 UTC | 更新原因: 审稿全部完成 + pre-submission 任务更新 + 清理过时任务

## 核心方向
Multi-turn jailbreak 检测的系统性分解：两轴泛化（attack-side DAPT + benign-side few-shot adaptation），discriminative compression 机制。详见 paper_framing.md。

## 当前阶段
**最终定稿完成，等待用户提交 ARR May** — DDL 2026-05-25

### 审稿历程
R18→R22 共 5 轮审稿完成。评分趋势: R20: 3.0 → R21: 3.5 → R22: 3.0。
结构性天花板已确认（合成数据局限、ToxicChat 反转、相对 Gururangan 2020 novelty），接受 Findings 定位，停止审稿循环。

### 提交就绪状态
- ✅ PDF 编译: 0 errors, 主文本 8 页, Limitations p9, 共 25 页
- ✅ 匿名 repo: force-push 完成 (commit `2eef235`), 匿名化已验证
- ✅ ARR 表单字段: Keywords/Research Area/Checklist A1-E1 已提供给用户（英文版）
- ⚠️ S3 备份: 磁盘配额不足失败，重试中

### 实验统计
75 个成功实验，29 个阴性，成功率 72%。98 个有结论实验覆盖论文全部 claims。

## GPU 预算
westd-33183: cuda:0 — 空闲（保留应急，提交后可能需要补实验）
autodl / gpu-5090 — 已放弃，通知 Manager 释放

## 近期任务
- [x] R20-R22 审稿处理（逐条 Action Matrix，全部修改落地）
- [x] 匿名 repo re-push（commit 2eef235）
- [x] PDF 编译确认（8 页主文本 + 0 errors）
- [x] ARR 表单字段准备（英文版已发用户）
- [ ] S3 备份重试（Agent 处理中）
- [ ] 用户提交 ARR May OpenReview（等用户操作）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D081 | 2026-05-22 | D081: R18 Action Matrix — 2个SYSTEMIC_ISSUE（externa | — |
| D080 | 2026-05-22 | R17 Action Matrix: EXP-D ToxicChat FP/FN decomposi | — |
| D079 | 2026-05-22 | exp62 揭示 Topic 失败机制: temporal inconsistency 而非 per | exp62_topic_failure_diagnosis |
| D078 | 2026-05-22 | exp60 揭示 MF1 turn count confound 不存在——论文中 "零重叠" 是  | exp60_turncount_baseline |
| D077 | 2026-05-22 | R16 Action Matrix: 4 experiments + 9 writing fixes | — |
| D076 | 2026-05-22 | R15 Action Matrix: 3 新实验 (SVD IID-only, 截断单轮, 重采样3 | exp54_causal_probe_subspace, exp50_layerwise_representation, exp56_crossllm_10shot_adaptation |
| D075 | 2026-05-22 | D075: exp54 因果探针确立 discriminative compression 为泛化因 | exp54_causal_probe, exp50_layerwise_representation |
| D074 | 2026-05-22 | D074: exp50 layer-wise + exp51 OASST2 双突破——discrim | exp50_layerwise_representation, exp51_oasst2_benign_ood |
| D073 | 2026-05-22 | D073: R14 Action Plan — N3 J-DAPT 优先搜索确定 framing 方 | — |
| D072 | 2026-05-22 | D072: exp49 推翻 regularization 假说——分类 DAPT 机制是 disc | exp49_representation_analysis |


