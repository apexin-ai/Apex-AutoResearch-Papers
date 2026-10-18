# reviewer / loop_1.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`c73a67eab4eda3bb351e.json`](../../sessions/c7/c73a67eab4eda3bb351e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T13:58:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 gpu-6000pro-2 的 cuda:0 和 cuda:1（ROADMAP 明确分配）
- pipeline 训练用 cuda:0，特征提取用 cuda:1（当前约定，可并行）
- 模型已从 Qwen2.5 切换到 Pythia-1.4B——**禁止回退到 Qwen**，之前已证明 Qwen2.5 无论 Instruct(100%) 还是 Base(17.9%) 都有严重代码污染
- LoRA target_modules 必须是 `query_key_value`（GPT-NeoX 架构），不是 q_proj/v_proj（Llama/Qwen）
- prepare_seed_data.py 用的是 Qwen tokenizer 筛选长度——已知不一致但不阻塞，论文需注明

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2 (westb-52439)，SSH 账号 root
- 工作目录：`/root/autodl-tmp/recursive_gen_depth_est`
- GPU：2× NVIDIA RTX PRO 6000 Blackwell 98GB
- 模型路径：`/root/autodl-tmp/models/pythia-1.4b/`
- 数据目录：`/root/autodl-tmp/recursive_gen_depth_est/data/`
- Checkpoints：`/root/autodl-tmp/recursive_gen_depth_est/checkpoints/lora_depth_{0,1,2}`
- 日志：`/root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_pythia.log`
- W&B：未配置（report_to="none"）
- 活跃进程：PID 114379（python，GPU 1，7.9GB）——正在跑 extract_features.py 写入 `data/features_all.jsonl`（最后检查时 ~11668 行 / 20000 目标，正在处理 depth-2）

### 3. 📊 当前状态
**刚完成**：mvp_pipeline_pythia_002 pipeline 全部完成（3× LoRA finetune + 3× generate），status=ANALYZING。

**数据产出**：
- depth_0.jsonl: 5000 条（Wikipedia 种子）
- depth_1.jsonl: 5000 条（9.2MB）
- depth_2.jsonl: 5000 条（9.3MB）
- depth_3.jsonl: 5000 条（9.7MB）
- depth_0_features.jsonl: 5000 条（parallel worker 早期提取，可能与 features_all.jsonl 重复）
- features_all.jsonl: ~11668/20000 行，正在被 PID 114379 写入

**训练 loss**：depth-0: 2.2411 → depth-1: 1.3894 → depth-2: 1.0250（单调递减，model collapse 信号强）

**已提交的审查报告**：
1. 初步通过报告（pipeline 运行中）
2. 完成审查报告（WARNING 级别）——代码内容随深度递增是主要发现

**等待**：特征提取完成 → train_classifier.py 运行 → MVP gate check 结果

### 4. 📋 待办
- features_all.jsonl 达到 20000 行 → 核实 train_classifier.py 是否被触发（注意：默认 `--features_path data/features.jsonl` 与实际文件 `features_all.jsonl` 不匹配，Agent 需传正确路径）
- train_classifier.py 输出结果 → 审查 MVP gate check：4-class acc >40% 且 depth-1 vs depth-2 AUC >0.6
- 分类结果出来后 → 要求 Agent 做 content-type 控制实验（过滤代码样本后重新评估），验证分类器不是靠域信号
- registry mvp_pipeline_pythia_002 从 ANALYZING 转 DONE → 核实 conclusion 和 metrics 是否准确反映实际数据
- train_classifier.py 代码审查点：无 stratify=y 的 train_test_split（5000/class 影响小但应注意）

### 5. 🎯 战略上下文
**核心发现**：代码内容随深度单调递增（"Copyright (c)" 匹配：depth-1 1.4% → depth-2 4.3% → depth-3 6.9%），这是 The Pile 代码模式被递归训练放大的 model collapse 证据。**双刃剑**：既是有趣的 collapse 信号，也是分类器的潜在域混淆源。

**最容易判断错的事**：
1. 分类器如果 accuracy 很高，不要直接庆祝——需先排除"学到了代码 vs 自然语言"这个 shortcut。必须要求 content-type 控制对比。
2. depth-0 是纯 Wikipedia（0% 代码），其他深度有代码——这个不对称本身就是域混淆。如果过滤后 accuracy 大幅下降，MVP 结论需要 qualify。
3. seed_id 跨深度内容相关（同一 BOS + 同一 RNG 位置），但这不是数据泄漏——只是确定性生成的必然结果，random split 已处理。

**决策链**：Qwen2.5-Instruct(killed) → Qwen2.5-Base(killed, 代码污染) → Pythia-1.4B(当前，代码 3.3%) → MVP gate check 进行中

**DDL**：EMNLP 2026 ARR，5/25 截稿。MVP 应该今天内出结果。


---
