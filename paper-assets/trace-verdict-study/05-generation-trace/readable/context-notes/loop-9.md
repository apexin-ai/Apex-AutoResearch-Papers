# director / loop_9.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`a217f8972e834999fec5.json`](../../sessions/a2/a217f8972e834999fec5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-21T04:59:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1（`gpu_ids=[0,1]`）
- C2 (density decomposition) 评级锁定 ★★★★，不因 collapse 升级（D108 决策）
- 论文中不 claim seed42 no_trace (67.31%) 是 outlier——诚实报告 3-seed mean±std
- codellama_label_only_seed123_v2 不重跑（磁盘满崩溃，rebuttal reserve 已有 seed42 确认 collapse）
- GPU 0 可能有孤儿显存（49175 MiB 无进程），跑大模型前需确认或重启容器清理

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 `/root/trace-verdict-study/`
- 论文路径：远程 `/root/trace-verdict-study/docs/paper/main.pdf`（441KB, MD5 `88140f88f5902315cb1236b6f453e5cc`）
- 本地论文：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_project/paper/main.pdf`（**旧版，未更新**）
- 磁盘：根分区 69%（9.5GB 可用，刚清理过）
- 活跃进程：无。两卡空闲，0 个 Worker
- 审稿群：`review_chat_id: oc_47a2f37b5c77af2e2351362f8def77a1`

### 3. 📊 当前状态
- 所有核心实验完成（109 成功），论文通过 Reviewer pre-submission PASS（0 critical, 0 warning after fixes）
- 刚完成：no_trace 3-seed 叙事更新（7 处 tex 修改 + σ range 扩展 + Table 1 caption fix + calibration appendix）
- 远程 tex 已编译通过（0 errors, 21 pages）
- **阻塞项**：本地 PDF 是旧版。MCP SSH 工具无法传输 441KB PDF（单次输出限 ~8KB）。已派 Agent 尝试替代传输方案（大块 base64 / git push-pull），同时已通知用户手动 scp，用户质疑"不会吧"但未操作
- Registry: 0 RUNNING, 0 PREPARING。有 6 QUEUED + 3 PREPARING 历史条目可清理为 CANCELLED

### 4. 📋 待办
- Agent 传输 PDF 成功 → `pdf_to_images` 视觉检查 → `submit_paper_to_review` 重提审稿
- 用户手动 scp 完成 → 同上流程
- 如果两种方案都失败 → 让 Agent 在远程用 `pdf_to_images` 等效检查（描述关键页面内容），然后直接提交远程 PDF 路径给 review
- Reviewer 新 session 启动后 → 可让其评估"reviewer 会问'为什么没测 X'的盲区"（上轮 Reviewer 已说 C1-C4 充分，但系统催促建议再独立评估一次）

### 5. 🎯 战略上下文
- **核心结论**：information density determines learning efficiency。exception_only ≥99.33% 跨 4 模型（C1），decomposition 17-24% gradient dilution / 76-83% information overload 仅 Qwen 家族验证（C2），two-tier hierarchy architecture-level 一致（C3/C4）
- **最大叙事调整已完成**：no_trace 3-seed 更新将 1.5B loop lift 从 +12.2pp 翻转为 +7.2pp（7B > 1.5B），scale range 从 9.16pp 缩至 4.12pp，introduction/experiments/discussion 三文件 7 处已改
- **易错点**：(1) 本地 PDF 是旧版，不要用它做视觉检查或提交；(2) GPU 0 孤儿显存可能导致 OOM，跑实验前先确认；(3) §4.4 decomposition 百分比（17%/83%）不受 no_trace 更新影响（计算基于 full_trace→label_only→exception_only，不涉及 no_trace）
- **DDL**：EMNLP ARR 2026-05-25，还有 4 天，时间充裕


---
