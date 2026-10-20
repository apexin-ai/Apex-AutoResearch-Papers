---
loop: 21
reason: max_wall_time
updated: '2026-05-25T15:39:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`gpu_ids=[0,1,2,3]`（autodl-5090 四卡），必须用 `CUDA_VISIBLE_DEVICES` 显式指定
- 论文 metric 混淆陷阱：QE 用 AUROC/ρ，selection 在 `tab:fewnerd` 用 instance-averaged F1，construction 在 `tab:entity_construction` 用 entity-type-averaged macro-F1。**不要假设全文统一用 micro-F1**——Loop #20 因此发了 false critical 被 Director 降级
- 论文已冻结（submission-ready），DDL 2026-05-25（今天）。修改需 Director 明确授权
- 匿名 repo（`github.com/anonymous-nlp-2026/struct_self_consist_ie`）刚修过一次作者泄漏（f3a74af 含 AWS 主机名）。任何新 commit 必须先设 `git config user.email anonymous@example.com`

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090`（root），工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型：`checkpoints/qwen3-8b-scierc-merged-v2`（SciERC）、`checkpoints/qwen3-8b-fewnerd-exp021-merged`（FewNERD 3-epoch）
- 数据：`data/scierc/processed_data`、`data/fewnerd/`、`data/conll2003/`
- FewNERD samples：`output/fewnerd_mf4v2_seed{42_v3,456,123_v4}/samples.jsonl`
- 活跃进程：**无**。4 张 GPU 全部空闲（0% util, 2 MiB each）。之前两个孤儿 `micro_f1_recompute.py` 已 kill
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 匿名 repo：本地 `anon_repo/`，remote HEAD = 48849f5，8 commits 全部匿名合规

### 3. 📊 当前状态
Loop #21 完成三件事：
1. DDL-eve 巡检：论文 submission-ready 确认（abstract ~174 词 ≤200、provenance 完整、0 undefined refs）
2. 发现并推动清理两个孤儿 CPU 进程（PID 282369/282468，已 kill）
3. 审查两次 anon_repo 操作——第二次 force push 引入匿名泄漏（f3a74af 含 AWS 主机名），已 critical 报告 → Worker 修复为 48849f5

另外收到 Director 关于 Introduction 第三贡献点 framing 策略的审查请求，已给出 Option C 建议（"exploratory" → "conditional"，reframe 为 framework validation）。

Registry：0 RUNNING，全部 DONE/killed/failed。无等待中的 Worker 回调。

### 4. 📋 待办（条件触发式）
- Paper Agent 提交修改后章节（abstract/intro/§4/Discussion）→ 按 §5 审查模式 B 全面审查（重点：N1 scope 收窄、W1 construction 降级、W2 Landesberg 段重复）
- Worker 提交 final PDF → 检查 8 页限制、undefined refs、abstract ≤200 words
- Director 发起 rebuttal response letter 定稿审查 → 交叉验证所有数字与 registry/artifacts 一致性
- 匿名 repo 再有新 commit → 必查 `git log --format="%ae"` 防止再次泄漏
- 如果 Director 采纳 Option C framing 并让 Paper Agent 修改 → 验证 introduction line 19 和 line 36-37 的 "exploratory"→"conditional" 修改一致性

### 5. 🎯 战略上下文
- **核心贡献**：correlation-selection gap（QE 预测质量但 selection 失败）+ diagnostic cascade（degeneracy + signal alignment collapse）。Construction 是 conditional/exploratory 附加
- **审稿状态**：Overall 3.0 (Findings)，目标 3.5 (Borderline Conference)。Must-Fix = model coverage scope 收窄（已复发 2 轮）
- **最易判断错的事**：
  1. **Metric 混淆**：验证数字前必须确认该表用的是哪种 F1（micro / instance-averaged / entity-type-averaged macro）。读 caption 确认
  2. **Construction ≠ Selection**：LP selection（argmax sample by LP）和 LP construction（entity-level aggregation with θ=2/N）完全不同
  3. **"claim 太强"的判定**：先确认论文 claim 的确切 metric 和 scope 再下结论，之前因此发了 false critical
  4. **匿名 repo 操作**：Worker 默认 git config 不是 anonymous，每次 commit 必须显式设置
