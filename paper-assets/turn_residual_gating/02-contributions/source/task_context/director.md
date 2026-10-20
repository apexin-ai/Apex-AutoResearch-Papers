---
loop: 7
reason: max_messages
updated: '2026-05-25T19:45:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU: westd-20861 上的卡，具体 gpu_ids 见 `get_project_status`，不可占用其他项目的卡
- 论文目录有两套：`paper/` 是主编辑目录，`docs/paper/` 是自动编译系统用的——改完 paper/ 必须同步到 docs/paper/（cp sections/*.tex + acl.sty/acl_natbib.bst 已复制，figures/artifacts 已 symlink）
- `paper/` 目录下不要残留旧版 figure PDF（graphicspath 会优先找 paper/ 下的，shadow 掉 figures/paper/ 的新版）
- EMNLP 2026: 正文 8 页硬限；Limitations 用 `\section*{Limitations}`（无编号）；abstract ≤ 200 words

### 2. 🖥️ 基础设施快照
- 服务器：westd-20861，工作目录 `/root/turn_residual_gating/`
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/`
- Python: 本地 `/usr/bin/python3`（图表生成用）；远程用 conda base（aml-train 镜像）
- 模型：远程 `/root/autodl-tmp/` 下（Qwen-2.5-7B-Instruct, Llama-3.1-8B）
- 图表生成脚本：`figures/paper/gen_*.py`，palette 在 `figures/paper/palette.py`
- 无活跃训练进程（实验全部 DONE）
- 论文编译：`paper_compile_and_check(project="turn_residual_gating")`

### 3. 📊 当前状态
**正在进行：全文数据真实性与可追溯性审计**（用户发起的重大自检任务）

已完成：
- 启动 4 个并行 agent 提取数字：主文章节（✅完成）、附录（✅完成）、图表脚本硬编码数据（⏳待返回）、实验 registry 数据源（✅完成）
- 主文提取约 200+ 个数字，附录提取约 370+ 个数字，registry 数据全部收集完毕

未完成：
- 图表脚本 agent 尚未返回（第 4 个 agent）
- **核心工作未开始**：交叉对账（paper 数字 vs registry 数据源）、不一致清单、修复、二次扫描
- 审计报告未撰写

其他已完成（本轮早期）：
- Figure 1 panel (b) 图例重叠 + panel (c) 箭头重叠修复（已编译、已发 PDF 给用户）
- ACL 官方模板对齐（上一轮完成）

Registry: 无 RUNNING/PREPARING 实验，全部 DONE。

### 4. 📋 待办
- 图表脚本 agent 返回 → 开始交叉对账：逐个数字匹配 registry 源，标注 Q1/Q2/Q3
- 对账完成 → 列出不一致清单：(a) 无出处 (b) 与源头不符 (c) 论文内部前后矛盾
- 不一致清单确定 → 逐个修复（改正确值 or 删除）→ 编译验证 → 二次扫描
- 全部修完 → 撰写审计报告（总数/问题数/处理方式/残留项）→ `director_reply_to_user` 发给用户
- 重点关注：Table 1 数字 vs registry `d048_final_ar_eval`；steering 数字 vs `attention_steering_gen_n50`；SS 三 seed 数字 vs `d048_eval_ss_s42/s123/s456`；Llama 数字 vs `llama_eval_s42` + `llama_ar_matched_eval` + `p1_llama_ss_eval`

### 5. 🎯 战略上下文
- 项目核心发现：auxiliary attention loss (GAR) 在 TF 下收敛到 0.50，但 AR 生成下坍塌 8-17×（Qwen）/ ~27×（Llama）。五路对比排除 gating/gradient conflict，确认 exposure bias 为主因。Scheduled sampling 压缩 gap 到 ~1.3×/2.9×。
- 论文 framing: 从"提出 ThreadGate 方法"转为"诊断 exposure bias 导致 auxiliary attention loss 坍塌"的 analysis paper
- **审计最易出错的地方**：
  1. Table 1 (five-way) 的 AR 列数字来源是 `d048_final_ar_eval`（N=39 valid convs），而非更早的 pilot N=5 数据——注意区分
  2. Llama 数字分散在多个 registry 条目（`llama_eval_s42`, `llama_ar_matched_eval`, `p1_llama_ss_eval`），median vs mean 区分很重要（论文用 median 报告 Llama AR GAR）
  3. SS 三 seed 的 std 计算：0.401±0.047 来自 [0.347, 0.423, 0.433]，需验证
  4. "~27×" 这个 Llama gap 是 median-based（0.484/0.018=26.9≈27），不是 mean-based
  5. 图表脚本中的硬编码数据可能与 registry 有微小精度差异——需确认是合理 rounding 还是错误
