# ORM Baseline 可行性调研报告

## 1. 现有 ORM/PRM 预训练权重搜索结果

### 1.1 数学推理领域（不直接适用，但可 zero-shot 测试）

| 模型 | 训练域 | 开源权重 | 大小 | 备注 |
|------|--------|---------|------|------|
| [Math-Shepherd-Mistral-7B-PRM](https://huggingface.co/peiyi9979/math-shepherd-mistral-7b-prm) | GSM8K/MATH 数学推理 | ✅ | 7B | PRM，Monte Carlo 自动标注，数学专用 |
| [Skywork-o1-Open-PRM-Qwen-2.5-7B](https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B) | 数学推理 | ✅ | 7B | PRM，Qwen2.5 backbone |
| [Qwen2.5-Math-PRM-72B](https://huggingface.co/Qwen/Qwen2.5-Math-PRM-72B) | 数学推理 | ✅ | 72B | 太大，不实用做 baseline |
| [Open-Reasoner-Zero-Critic-7B](https://huggingface.co/Open-Reasoner-Zero/Open-Reasoner-Zero-7B) | 数学/代码推理 | ✅ | 7B | Critic model，可评估推理质量 |
| [RLHFlow/Llama3.1-8B-PRM](https://huggingface.co/RLHFlow/Llama3.1-8B-PRM-Mistral-Data) | 数学推理 | ✅ | 8B | PRIME 隐式 PRM |

**迁移性评估**：这些模型全部在数学推理上训练。逻辑推理（ProofWriter/FOLIO/LogiQA）的推理结构与数学有本质区别——逻辑推理涉及前提-规则-结论的演绎链，而非算术计算步骤。**Zero-shot 迁移效果预期较差。**

### 1.2 逻辑推理领域（直接相关）

| 模型 | 训练域 | 开源权重 | 大小 | 备注 |
|------|--------|---------|------|------|
| **[LogicReward-Qwen3-8B](https://huggingface.co/collections/Aiden0526/logicreward)** | 逻辑推理 (8 个 NLI/逻辑 benchmark) | ✅ | 8B | **ICLR 2026**，step-level 逻辑监督，用 theorem prover 验证，**最直接相关** |
| **[LogicReward-Llama3.1-8B](https://huggingface.co/collections/Aiden0526/logicreward)** | 逻辑推理 | ✅ | 8B | 同上，LLaMA backbone |
| **[FoVer PRMs](https://huggingface.co/collections/ryokamoi/fover)** | 形式逻辑 (Z3) + 定理证明 (Isabelle) | ✅ | 7B/8B | **ACL 2026 Findings**，用 Z3 形式验证生成 step-level 标注训练 PRM，在 ANLI/BBH 等逻辑任务上也有效 |
| [ThinkPRM-14B](https://huggingface.co/launch/ThinkPRM-14B) | 通用推理 | ✅ | 14B | 生成式 PRM，较大 |

### 1.3 通用 Reward Model

| 模型 | 训练域 | 开源权重 | 大小 | 备注 |
|------|--------|---------|------|------|
| [GRAM-R²](https://github.com/NiuTrans/GRAM) | 通用偏好 | ✅ | 8B/14B | ICML 2025，生成式基础 reward model，可迁移 |
| Nemotron-4-340B-Reward | 通用 | ✅ | 340B | 太大 |

### 1.4 专门的逻辑推理 ORM（论文级）

**[Logical Reasoning with ORMs for Test-Time Scaling](https://aclanthology.org/2025.emnlp-main.1326/)** (EMNLP 2025)
- 专门为 deductive reasoning 训练的 ORM
- 在 FOLIO、JustLogic、ProverQA 上评测
- 用 "echo generation" 技术扩充训练数据覆盖错误类型
- **权重未公开**，但方法清晰可复现

---

## 2. GenRM 方案调研

### 2.1 核心论文

| 论文 | 发表 | 核心方法 | 效果 |
|------|------|---------|------|
| [Generative Verifiers (Google DeepMind)](https://arxiv.org/abs/2408.15240) | ICLR 2025 | 用 next-token prediction 训练 verifier，预测 "Yes"/"No" + CoT rationale | GSM8K 73%→93.4%，算法任务 5%→45.3% |
| [Generative Reward Models (GenRM)](https://arxiv.org/abs/2410.12832) | 2024 | 在 self-generated reasoning traces 上迭代训练，生成 preference labels | OOD 泛化比 Bradley-Terry 好 10-45% |
| [GRAM-R²](https://github.com/NiuTrans/GRAM) | ICML 2025 | 先 unsupervised pretraining 再 supervised fine-tuning 的 generative reward model | JudgeBench 71.4 (Qwen3-14B) |

### 2.2 Prompt-Based GenRM（零训练方案）

**核心思路**：直接用强 LLM 生成 verification rationale，然后判断 chain 正确性。

**实现方式**：
```
Prompt: "Given the following premises and reasoning chain, verify each step's logical validity.
For each step, check:
1. Does it follow from the premises or previous steps?
2. Is the logical rule applied correctly?
3. Are there any hidden assumptions?
Output: 'VALID' or 'INVALID' with explanation."
```

**用 DeepSeek V3.2 / Qwen2.5-14B 做 GenRM 的可行性**：
- **DeepSeek V3.2**：强推理能力，适合做 CoT verification。但需要 API 调用，成本较高。适合做 oracle baseline 上限。
- **Qwen2.5-14B-Instruct**：可本地部署在单张 5090（24GB 需量化到 INT4），推理速度可接受。逻辑推理能力比 7B 显著好。
- **Qwen3-8B**：有 thinking mode，reasoning 能力强于 Qwen2.5-14B，且可在单卡 FP16 运行。推荐首选。

### 2.3 GenRM 优势与局限

**优势**：
- 不需要训练，实现快（1-2 天）
- 可生成可解释的 verification rationale
- 通过 CoT 提升逻辑验证质量
- 自然支持 step-level 和 chain-level 验证

**局限**：
- 推理成本高（每条 chain 需要一次完整 LLM forward）
- 效果依赖 prompt 质量和 base model 能力
- 在 adversarial cases 上可能被误导
- 与 SVS 的 formal verification 比，缺乏 soundness 保证

---

## 3. 方案对比与推荐

### 方案 A：现成 ORM/PRM 权重 Zero-Shot

| 维度 | 评估 |
|------|------|
| 候选模型 | LogicReward-Qwen3-8B (**首选**)、FoVer-PRM-7B、Math-Shepherd-7B-PRM (弱 baseline) |
| 实现复杂度 | **0.5-1 天**（下载权重 + 写 inference pipeline + 评测） |
| GPU 需求 | 单卡 5090 24GB 足够（7-8B 模型 FP16） |
| 预期效果 | LogicReward 在逻辑推理上专门训练，效果应该最好；FoVer 用 Z3 训练，与 SVS 方法论接近；Math-Shepherd 跨域迁移效果存疑 |
| 风险 | LogicReward 的 reward signal 可能与 SVS 的 graded verification 评分标准不完全对齐 |

### 方案 B：GenRM Prompt-Based

| 维度 | 评估 |
|------|------|
| 实现方式 | 用 Qwen3-8B 或 DeepSeek V3.2 API 做 CoT verification |
| 实现复杂度 | **1-2 天**（设计 verification prompt + 实现 scoring pipeline + 评测） |
| GPU 需求 | Qwen3-8B 本地部署单卡 5090；DeepSeek API 无 GPU 需求 |
| 预期效果 | 灵活性最强，可针对 SVS 的逻辑推理任务定制 prompt；DeepSeek V3.2 作为 oracle 上限 |
| 风险 | prompt 敏感，需要迭代调优；推理速度慢（每条 chain ~几秒） |

### 方案 C：训练轻量 ORM

| 维度 | 评估 |
|------|------|
| 方法 | 参考 EMNLP 2025 logical reasoning ORM 论文，用 CoT + echo generation 构造训练数据 |
| 实现复杂度 | **5-7 天**（数据构造 2 天 + 训练 1-2 天 + 评测调优 2 天） |
| GPU 需求 | 训练 7B ORM 需要 1-2 张 5090，约 10-20 GPU hours |
| 预期效果 | 领域适配最好，但数据质量是瓶颈 |
| 风险 | 工程量大；训练数据构造依赖 LLM 质量；可能过拟合 |

### 推荐方案

**推荐：方案 A + B 组合，2-3 天完成。**

1. **Day 1**：下载 LogicReward-Qwen3-8B 和 FoVer-PRM 权重，实现 inference pipeline，在 SVS 的评测集上跑 zero-shot baseline
2. **Day 2**：实现 GenRM prompt-based pipeline（用 Qwen3-8B + DeepSeek V3.2 API），作为另一组 baseline
3. **Day 3**：对比 SVS formal verification vs. LogicReward vs. FoVer-PRM vs. GenRM，分析各方案在不同推理深度/错误类型上的表现差异

**理由**：
- LogicReward 是 ICLR 2026 的逻辑推理专用 reward model，直接覆盖 SVS 的目标领域
- FoVer 用 Z3 训练，与 SVS 方法论（Z3 形式验证）有天然相似性，对比价值高
- GenRM 提供了一个不依赖专门训练的 learned baseline，体现了 LLM 内在的验证能力
- 方案 C 的 ROI 不高——有了 LogicReward 和 FoVer 这样的专用模型，再训一个轻量 ORM 的边际收益有限

---

## 4. 具体候选模型清单

| 优先级 | 模型 | HuggingFace 路径 | 类型 | 训练域 | 大小 |
|--------|------|-----------------|------|--------|------|
| ⭐⭐⭐ | LogicReward-Qwen3-8B | Aiden0526/LogicReward-Qwen3-8B | Reward (step-level) | 逻辑推理 | 8B |
| ⭐⭐⭐ | LogicReward-Llama3.1-8B | Aiden0526/LogicReward-Llama3.1-8B | Reward (step-level) | 逻辑推理 | 8B |
| ⭐⭐ | FoVer-PRM (Qwen2.5-7B/Llama3.1-8B) | ryokamoi/fover (collection) | PRM | 形式逻辑+定理证明 | 7-8B |
| ⭐⭐ | GenRM (Qwen3-8B prompt-based) | — | Prompt-based | 通用 | 8B |
| ⭐ | Math-Shepherd-Mistral-7B-PRM | peiyi9979/math-shepherd-mistral-7b-prm | PRM | 数学 | 7B |
| ⭐ | Skywork-o1-Open-PRM-Qwen-2.5-7B | Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B | PRM | 数学 | 7B |
| ⭐ | ThinkPRM-14B | launch/ThinkPRM-14B | 生成式 PRM | 通用推理 | 14B |

---

## 5. 关键参考文献

- **LogicReward** (ICLR 2026): [arXiv:2512.18196](https://arxiv.org/abs/2512.18196) — Step-wise logical supervision with theorem prover
- **FoVer** (ACL 2026 Findings): [arXiv:2505.15960](https://arxiv.org/abs/2505.15960) — PRM training via Z3/Isabelle formal verification
- **Logical Reasoning with ORMs** (EMNLP 2025): [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1326/) — Deductive reasoning ORMs with echo generation
- **Generative Verifiers / GenRM** (ICLR 2025): [arXiv:2408.15240](https://arxiv.org/abs/2408.15240) — Next-token prediction verifiers with CoT
- **Math-Shepherd** (ACL 2024): [arXiv:2312.08935](https://arxiv.org/abs/2312.08935) — Process reward model for math
- **GRAM** (ICML 2025): [arXiv:2506.14175](https://arxiv.org/abs/2506.14175) — Generative foundation reward model
