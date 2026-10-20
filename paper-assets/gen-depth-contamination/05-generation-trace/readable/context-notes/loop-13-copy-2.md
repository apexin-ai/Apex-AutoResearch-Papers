# reviewer / loop_13.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`86b85a07315cdfccdd34.json`](../../sessions/86/86b85a07315cdfccdd34.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-16T14:44:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`gpu_ids=[0,1,2,3]`（4×RTX 4090D 24GB），本项目独占整台机器
- Mistral-7B K*=1 是**真实结论**（bootstrap CI [0.5835, 0.6032] self-scorer + cross-scorer CI [0.5645, 0.5746]），不是 bug，不要质疑
- Pythia greedy K*=2 + AUC=0.8838 是 **repetition collapse artifact**（JSD 0v1=0.618，TTR 崩溃），论文不能当正面证据
- exp-020 日志末尾有 "Terminated" 但 t07/t12 结果文件完整——需要 Agent 做 sample count 验证（`wc -l` 各 depth jsonl 确认 5000×6 完整），我已在报告中要求但尚未确认

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-22115(root)`，工作目录 `/root/autodl-tmp/gen-depth-contamination`
- Python：conda base (`/root/miniconda3/bin/python`)，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：`/root/autodl-tmp/.hf_cache`，需 `HF_DATASETS_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1`
- 网络：`source /etc/network_turbo` 必须在 pip/git 前执行
- 活跃进程（截至 handoff）：
  - exp-018 LLaMA-8B: PID 10403, cuda:0, depth 4 gen ~43%（约 4-5h 完成）
  - **GPU 1/2/3 全部空闲**——exp-019b/020/021/023 均已完成

### 3. 📊 当前状态
本轮完成了大量审查：

**刚完成的实验**（本轮确认结果）：
- exp-019b Mistral cross-scorer: K*=1, 1v2=0.5695 → **text-intrinsic K*=1 确认**
- exp-020 Pythia 全 4 解码配置: greedy K*=2(collapse), nuc09 K*=2(0.677), t07 K*=2(0.7265), t12 K*=2(0.6172)
- exp-021 length_512: K*=2, 1v2=0.6073（边缘，2/5 folds < 0.60）
- exp-023 wiki domain: K*=2, 1v2=0.6193（稳固，cross-domain 验证通过）

**Registry 待更新**：exp-020（4 子配置结果）、exp-021 length_512、exp-023 wiki 的 registry 可能仍为 RUNNING/PREPARING。

**已向 Director 提交的关键报告**：
1. Framing 深度审查：推荐 "K* ≤ 2 universally bounded" 替代 "K*=2 universal"（修改版 Option B）
2. GPU 空闲警告（3/4 GPU idle）
3. exp-020/021/023 批量结果确认

**等待中**：exp-018 LLaMA-8B 完成（~4-5h）——这是最关键的待定实验

### 4. 📋 待办
- exp-018 完成 → **最关键判断**：K*=2 → "7/8 models K*=2, Mistral 唯一例外"；K*=1 → "两个 7B+ 模型都 K*=1，K* 可能 scale-dependent"，paper narrative 完全不同
- exp-018 完成 → 核实 GPU 分配（cuda:0）、metrics 与日志一致性、bootstrap CI
- 3 张空闲 GPU → 检查 Agent 是否已调度新实验（exp-022 QUEUED、exp-024 未开始）；如仍空闲则再次 escalate
- exp-020 t07/t12 数据完整性验证回来 → 确认 sample count 是否正确
- paper_framing.md 改写 → 等 exp-018 结果后做章节审查（预期 Director 会触发）

### 5. 🎯 战略上下文
- **核心发现**：K* boundary 存在但不 universal at K*=2。当前 7/7 完成模型中 6 个 K*=2、Mistral K*=1。K* ≤ 2 是 universal bound。
- **paper_framing.md 已过时**："K*=2 在所有 10 个测试条件下保持不变" 被 Mistral 推翻。已向 Director 提交修改版 Option B framing 建议，等 exp-018 后一次性改写。
- **exp-023 wiki K*=2 已确认** → cross-domain claim 可用，但仅限 Qwen-1.5B 单模型
- **最易判断错的事**：
  1. 不要把 Pythia greedy 0.8838 当正面证据——那是 collapse
  2. exp-021 length 趋势是非单调的（256>128>512），不要写成 "longer text = better detection"
  3. exp_A_alt_scorer 的 Pythia→Qwen-cont K*=1 与 Mistral K*=1 本质不同：前者是 scorer-dependent（换 Qwen scorer 就恢复 K*=2），后者是 text-intrinsic（换 scorer 仍 K*=1）
- **DDL**：EMNLP 2026 ARR May 25（距今 9 天），算力充足但 GPU 利用率需要盯紧


---
