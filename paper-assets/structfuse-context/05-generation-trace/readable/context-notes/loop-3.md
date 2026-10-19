# director / loop_3.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`7fcf048d3390d7dae355.json`](../../sessions/7f/7fcf048d3390d7dae355.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T00:03:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（bjb1-42106 双卡，项目专属）
- 代码目录 `/root/structfuse-context/`，符号链接 `/root/structfuse` → `/root/structfuse-context/` 保留到训练结束
- 数据盘 `/root/autodl-tmp/structfuse/`（注意不带 -context，这是数据目录不是代码目录）
- HF cache 必须设 `HF_HOME=/root/autodl-tmp/.hf_cache`，根分区只有 ~30GB
- neg_difficulty_analysis registry 状态机不支持 PREPARING→DONE 直跳，当前 conclusion=success + metrics 正确即可，不要强改 status

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (connect.bjb1.seetacloud.com)，用户 root
- 代码目录：`/root/structfuse-context/`
- 数据目录：`/root/autodl-tmp/structfuse/`（训练数据、checkpoints、artifacts）
- Python：系统 Python 或 venv（需 SSH 确认，aml-train 镜像可能用 conda `/root/miniconda3/bin/python`）
- SWE-bench repos 预克隆：`/root/autodl-tmp/swebench/repos/`（12 bare repos，1.7GB）
- 磁盘余量：`/root/autodl-tmp` ~96GB
- 活跃进程：
  - m2_full_qwen: PID 73558, cuda:0, ~step 1500/4242 (epoch 2 开始)
  - m2_full_starcoder: PID 76627, cuda:1, ~step 1000/4242 (epoch 1 ~70%)
  - m1_reextract_v2: CPU only, ~9% 完成 (2553/28276)，预计还需 ~13h

### 3. 📊 当前状态
**刚完成**：三件清理任务全部完成 + Reviewer PASS：
1. neg_difficulty registry 修正（128/2048 数据分别标注，2048 确认 Qwen ceiling 结构性）
2. eval_swebench.py 两个 bug 修复（lora_alpha 读 config、repo-cache-dir 参数）
3. 目录重命名路径修正（18 文件 23 处 sed 替换，零残留）

**RUNNING 实验**：
- `m2_full_qwen`：3 strategies × 3 seeds，Qwen2.5-Coder-3B LoRA。random_s42 eval@1000 R@1=0.553（超 pilot best），**eval@1500 R@1=0.5228 有回落**——需监控是否过拟合
- `m2_full_starcoder`：同上 StarCoder 版。random_s42 eval@500 R@1=0.435
- `m1_reextract_v2`：恢复 28276 失败 instances 的 CodeQL 提取，CPU only

**等待中**：无 pending Worker/Cron 回调。Agent 空闲。

### 4. 📋 待办
- 18 runs 全部完成（预计 May 17-18）→ D019 go/no-go 判定：paired t-test p<0.05，按 Claim 1 (A/B/C) 和 Claim 2 (i/ii/iii) 矩阵分叉
- Qwen eval@1500 R@1 回落持续 → 若 epoch 2-3 持续下降，考虑 early stopping 或降 lr
- M2 完成 → 立即启动 plan_003 SWE-bench Lite eval（基础设施已就绪，代码+数据+脚本全部到位）
- m1_reextract_v2 完成（~May 14 晚）→ 统计新增结构数据量，评估是否需要用扩大后的数据集重训
- plan_014 temperature ablation（M2 完成后优先）

### 5. 🎯 战略上下文
- **核心假设**：CodeQL data-flow 生成的 structure-grounded hard negatives 优于 embedding-distance negatives 和 random negatives
- **Pilot 结论 (D016/D017)**：embedding > random 跨编码器一致；dataflow 效果 mixed（Qwen 有效但 StarCoder 负面）→ Full M2 是 go/no-go 唯一裁判
- **D018 关键决策**：不做预判性 framing pivot，等 18 runs 数据说话
- **D019/D020 量化阈值已锁定**：结果出来前不修改判定标准
- **D021**：Qwen 表征 ceiling（pos_sim≈0.98）是结构性的，不是截断 artifact（2048t 确认）
- **最容易判断错的事**：Qwen eval@1500 R@1 回落不等于过拟合——epoch 边界波动是正常的，需要看 epoch 2 中后段趋势。但如果 epoch 2 结束时 R@1 < eval@1000 的 0.553，那就是真过拟合
- **n=3 统计功效限制**：df=2 下 t 临界值 4.303，pilot 级别差异极难显著，偏向 No-Go (Type II error 高)。论文 Discussion 必须提及
- **run_m2_full_starcoder.sh 路径残留**：`PROJECT_ROOT="/root/structfuse"` 未被 sed 替换（无尾部斜杠不匹配），功能不影响（symlink），但路径不一致


---
