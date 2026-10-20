# Memory — demo_calibrated_sim

## 教训

### [2026-05-12] 禁止 cherry-picking eval 结果
dpo-001 eval 跑了 ≥5 次，completion 分别为 25%/20%/10%/30%/未完成。Reviewer 发现后要求全部记录。
**规则：所有 eval run 结果必须完整记录到 registry，报告 mean ± 所有单次值。不能只选最好的一次。**

### [2026-05-12] tokenizer mismatch 导致 DPO 训练无效
dpo-001 使用 v1 数据（raw text 格式），48% 的 DPO pairs 存在 tokenizer mismatch。训练 loss 仅比随机低 0.012，accuracy=0.5（随机水平）。
**教训：DPO 数据必须用 chat template 格式构造（v2 脚本），否则 tokenizer 对齐问题会让训练完全无效。**

### [2026-05-12] TRL 1.4.0 + Qwen2.5 根因：add_generation_prompt 硬编码
TRL DPOTrainer 对 conversational 数据硬编码 `add_generation_prompt=True`，追加 `<|im_start|>assistant\n` 到 prompt_ids。当 chosen/rejected 是 user 角色时导致 100% mismatch。已知 issue TRL #5213，无修复版本。
**修复**：数据预处理用 `apply_chat_template()` 转纯文本 → DPOTrainer 走文本路径 → 0 mismatch。同时设 `padding_side="right"`。脚本：`train_dpo_v3.py`。

### [2026-05-12] BCP prompt 三个失败机制
mvp-004 (n=19/20) 验证 BCP 路线失败：(1) 全局行为抑制——completion 崩溃至 10-26%；(2) 跨维度干扰——校准一个维度破坏其他维度；(3) 过校正反弹——overcorrected variant politeness 反升至 60.5%。

### [2026-05-13] vLLM LoRA 动态加载严重低估 completion
diag-lora-merge 实验证明 vLLM LoRA serving 存在 bug：同一个 DPO-003 adapter，LoRA 动态加载 completion=15%，merge_and_unload 后 completion=60%（4 倍差距）。Base model 无 DPO 为 40%。
**规则：H-gate eval 必须用 merged 模型（PEFT merge_and_unload），不要用 vLLM LoRA 动态加载。**

### [2026-05-13] Mistral-7B 无法在 16-tool 场景做 function calling
mistral-bcp-001 实验发现 Mistral-7B-Instruct-v0.3 通过 vLLM 无法在 tau-bench retail 环境（16 tools）下生成 structured tool_calls。
- 1 tool 时正常，16 tools 时 tool_calls 返回空列表
**教训：跨模型对比实验前必须先验证基础能力（tool calling、instruction following）。**

### [2026-05-13] AWQ 量化破坏 Qwen2.5 的 tool-call special token
Qwen2.5-14B-Instruct-AWQ（4-bit 量化）通过 vLLM 部署时，`<tool_call>` special token (ID 151657) 被映射到泰语字符 "คณะกรรม" (token 139738)。导致 tool calling 完全失效。
**解决方案**：使用 FP16 + tensor-parallel（TP=2 跨两张 4090D）替代 AWQ。FP16 下 tool-calling 正常工作（quick test 40% completion）。
**教训：量化模型部署前必须验证 special token 完整性，尤其是 tool-call 相关 token。AWQ 对 Qwen2.5 系列不安全。**

### [2026-05-13] BCP 失败机制是 scale-dependent 的——不是简单复现
qwen14b-bcp-001 (14B FP16 TP=2) 完成。**14B 的 BCP 失败与 7B 根本不同**：
- **7B**: "灾难性崩溃"——BCP prompt 摧毁模型行为，completion 崩溃至 10-26%（FM1），跨维度严重干扰（FM2），过校正反弹（FM3）
- **14B**: "选择性忽略"——模型正常工作（completion 61.6%，retention >97%）但无视 BCP 校准指令（H2 1/4）
- FM1 未复现（无 completion 崩溃），FM2 弱复现（幅度远小于 7B），FM3 未复现（方向相反）
- **两者 H2 都 FAIL，但原因相反：7B 过度响应导致崩溃，14B 不够响应导致忽略**
**关键发现：这是 scale-dependent failure mode transition，走决策树"模式不同"分支 → 对论文更有价值，说明 BCP 的缺陷是方法论层面的，不论 scale 都失败但失败方式不同。**

## 决策上下文

### [2026-05-12] DPO 是 MVP 唯一剩余路径
BCP 失败(D003)后，DPO LoRA 是唯一校准方法。

### [2026-05-12] 多模型复现是投稿必须项
Reviewer 评估单模型(Qwen)数据不够，需要跨模型/跨 scale 证据(D005)。

### [2026-05-13] sim2real2026gap 是 Plan B 核心 motivation
arXiv 2603.11245。与 DemoCalib 同一问题空间但只诊断不开药。Plan B 应引用为核心 motivation。

### [2026-05-13] Plan B story 方向：校准尝试的完整生命周期（Director 批准）
Director 确认选项 2："校准尝试的完整生命周期：BCP 失败机制 + DPO+BCP 反转效应 + implications"。

### [2026-05-13] D012: Qwen2.5-14B 跨 scale 验证
Plan B KILL 条件触发但 Director 判断 DPO+BCP 反转效应是真实新发现。改用 Qwen2.5-14B FP16 TP=2 做跨 scale 验证。Quick test 40% completion 通过 >20% gate。

### [2026-05-13] D012 结果：scale-dependent failure mode transition
14B BCP eval 完成。FM1/FM3 未复现，FM2 弱复现。但 H2 仍然 FAIL。发现 BCP 在不同 scale 以不同方式失败：7B 过度响应 vs 14B 选择性忽略。走"模式不同 → scale-dependent failure boundary"分支。论文 C3 应重构为 failure mode transition 而非简单 replication。
