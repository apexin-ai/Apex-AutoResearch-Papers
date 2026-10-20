---
loop: 4
reason: idle_timeout
updated: '2026-05-24T20:00:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- Mistral 免费θ baseline 必须用 n=10 clean seeds（mean=4.024, SD=2.052），不能用服务器现存 6 个文件重算（seeds 4-7 文件已删，重算会得到 mean=3.40 SD=2.43 导致所有 d 值错误）
- Llama baseline 必须用 V2（mean=+0.262, SD=1.542），V0（mean=-0.312, SD=0.840）已废弃
- Table 2 所有条目必须 within-seed 对比（free vs fixed 来自同一 contamination seed），不能混 multi-seed free 和 single-seed fixed
- 论文 Mistral contam_15 原始 s1 文件不存在于服务器，d=2.64 来自历史报告不可重推导——直接使用不要尝试重算

### 2. 🖥️ 基础设施快照
- 服务器：westd-35694(root)，工作目录 /root/autodl-tmp/ctrl_contam_pilot/
- 结果路径：/root/autodl-tmp/ctrl_contam_pilot/results/{llama,mistral,qwen}/
- Mistral clean seeds 现存：s1(无后缀), s2, s3, s8, s9, s10（共6个）；seeds 4-7 文件缺失
- Llama/Qwen clean seeds：各 10 个完整
- GPU：4× RTX PRO 6000 Blackwell 96GB，当前全部空闲
- 无活跃训练进程、无 tmux session、无 cron

### 3. 📊 当前状态
**刚完成**：对 DDL 前最后一批 paper fix workers 的全面数据核验（5/24 全天），涵盖：
- fix-llama-25-d-mismatch ✅ 验证通过（9 个 server JSON 独立核算）
- update-mistral-15-multiseed ✅ 数值正确，标记了 Table 2/3 结构问题
- consistency-fixes-batch ✅ Qwen heatmap + Mistral 50% 修正到位
- table2-footnote-fix ✅ 恢复 single-seed 对比
- fix-table3-mistral-single-seed ❌ 失败，Table 3 混合聚合问题未修复

**未修复的唯一问题**：Table 3 (results.tex:152) Mistral lz* 仍为 multi-seed (3.37/4.09) 而 HT/Acc z 为 single-seed。建议恢复为 d=2.64 [1.5, 7.3] / d=3.50 [2.1, 9.4]。

Registry 无 RUNNING/PREPARING 实验。DDL 是 2026-05-25。

### 4. 📋 待办
- Director 派新 worker 修 Table 3 → 验证 Mistral lz* 恢复为 single-seed + dagger 标记移除
- 如收到最终 PDF 视觉审查请求 → 用 paper-visual-review skill 检查图表渲染
- 如收到新 rebuttal/response 稿件 → 交叉验证所有数字（已发现过 5 个数据错误）
- 如实验 registry 出现新 RUNNING 条目 → 检查 GPU 白名单和 CUDA_VISIBLE_DEVICES

### 5. 🎯 战略上下文
**核心结论链**：IRT lz* 在 controlled SFT contamination 下 |d|=2.30-7.44（强检测力），但 free-θ estimation 在高 baseline accuracy 模型上受 θ-shift absorption 削弱，fixed-θ 可恢复 2.4×。三个模型族呈不同 dose-response：Qwen inverted-U、Llama flat、Mistral monotonic increasing。

**易错点**：
1. 不要混淆 free-θ 和 fixed-θ baseline（Mistral 两套数值差异大）
2. Qwen 5% 在 Table 1 是 single-seed（[CI]），15%/25%/50% 是 multi-seed（±SD）——同一行混合是正常的
3. 50% s3 d=-1.99 是旧 copy-paste 错误的根源（Llama），已修复但新 worker 可能误读旧 cached 值
4. rebuttal_prep.md 之前有 5 个 hallucinated 数字（13.4×、83%等），已修复但需警惕 Agent 再次编造
5. FPR calibration analysis v1 和 v2 都是 INVALID（用错 baseline），不要引用
