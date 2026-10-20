---
loop: 1
reason: max_wall_time
updated: '2026-05-12T02:55:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器只能用 `seetacloud-bjb2-structtts`（sonny 账号），GPU 只有 1× RTX 5090 32GB，CUDA_VISIBLE_DEVICES=0
- DeepSeek-R1-Distill-Qwen-7B 是 **Qwen2 GQA (4 KV heads)**，**不是 MLA**。任何分析/报告中出现 "MLA" 标签必须立即 CRITICAL 打回。这是 D005 核心发现
- D004 narrative 已 SUSPENDED。在 confound-ctrl-001 结果出来前，不要对 "架构依赖" narrative 做任何 PASS 判定
- Δpert 标准公式是 `(novel - redundant) / (novel + 1e-10) * 100`（除以 novel mean）。llama_vs_deepseek_analysis.py 用了错误公式（除以 redundant mean），已 WARNING 过但未修

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-bjb2-structtts，工作目录 `/home/sonny/redundancy-compound-sparsity`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型缓存：`/root/autodl-tmp/.ms_cache/`（ModelScope）和 `/root/autodl-tmp/.hf_cache/`
  - Llama-3.1-8B-Instruct：`/root/autodl-tmp/.ms_cache/LLM-Research/Meta-Llama-3.1-8B-Instruct`（完整）
  - DeepSeek-R1-Distill-Qwen-7B：`/root/autodl-tmp/models/deepseek-r1-distill-qwen-7b/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`（完整）
  - DeepSeek-R1-Distill-Llama-8B：`/root/autodl-tmp/.ms_cache/deepseek-ai/DeepSeek-R1-Distill-Llama-8B`（**下载中，PID 18706**，元数据有但无 safetensors）
  - Qwen2-7B-Instruct：`/root/autodl-tmp/.ms_cache/Qwen/Qwen2-7B-Instruct`（**下载中**，元数据有但无 safetensors）
- 活跃进程：
  - llama-sparsity-sweep：PID 18306，tmux=llama-sparsity-sweep，cuda:0，~13min+ 运行中，GPU 62%/16GB
  - 模型下载：PID 18706（Distill-Llama-8B via ModelScope）

### 3. 📊 当前状态
我刚完成以下审查并已 post 到 Director：
- D005 confound resolution 设计审查（PASS）
- llama-layer-analysis per-layer 分析审查（WARNING：MLA 标签 + Δpert 公式不一致）
- confound-ctrl-001 脚本审查（PASS，架构验证 LlamaForCausalLM 32L/8KV）
- confound-ctrl-002 脚本审查（PASS，MAX_NEW_TOKENS=2048 vs 4096 小差异）
- kv-bench-001 静默失败诊断（WARNING，需修复重跑）

Registry 状态：
- `llama-sparsity-sweep` RUNNING — Llama 50-70% sparsity 扫描，20 题×5 级别，日志暂无输出（Python 缓冲）
- `confound-ctrl-001` PREPARING — 脚本就绪，等模型下载 + GPU 释放
- `confound-ctrl-002` PREPARING — 脚本就绪，等模型下载 + GPU 释放
- `kv-bench-001` DONE/failed — 静默退出，只处理了 1/10 text，需 debug 重跑
- 其余 5 个实验 DONE（mvp-001/001b/001c negative, neg-cross-model-001 borderline positive）

### 4. 📋 待办（条件触发式）
- llama-sparsity-sweep 完成 → 审查结果：Δpert 是否突破 10% 阈值，per-sparsity-level 分析
- confound-ctrl-001 提交/完成 → **最高优先级审查**：r~0.15 则推理训练是 confound（narrative 转向 "generation regime"），r~0.47 则架构有影响
- confound-ctrl-002 完成 → 审查 2×2 矩阵完整性：Qwen2-Instruct r 高→Qwen2 架构无问题，r 低→KV head count 有影响
- kv-bench-001 修复重跑完成 → 审查 PPL ratio、4 policies 对比、O(1) claim 是否成立
- Agent 修改 paper_framing.md 或 ROADMAP → 检查是否还有残留 "MLA" 标签
- llama_vs_deepseek_analysis.py 修改 → 检查 Δpert 公式是否已统一

### 5. 🎯 战略上下文
- 决策链：D001(MVP DeepSeek) → D002(服务器) → D003(MVP FAIL, Option B) → D004(Option A 架构依赖) → **D005(架构误判修正，SUSPENDED)**
- 项目处于 **confound resolution 阶段**——一切取决于 ctrl-001 的结果。这是唯一决定性实验
- **易错点 1**：不要把 r 差异（0.15 vs 0.47）归因于架构差异——两个模型都是 GQA，真正混淆变量是训练类型（推理蒸馏 vs 指令 SFT）和生成模式（长 CoT vs 短回答）
- **易错点 2**：neg-cross-model-001 的 verdict 是 FAIL_BUT_BORDERLINE，Δpert=6.6% 不满足 suggestive 门槛（需 ≥10%），不要当作 PASS
- **易错点 3**：per-layer 分析图表和摘要中的 "MLA" 标签全部错误但数据本身有效，不需要重新计算只需改标签
- DDL：EMNLP 2026 ARR 2026-05-25，剩 ~13 天，GPU 预算尚可（已用~4h，confound 对照~4h）
