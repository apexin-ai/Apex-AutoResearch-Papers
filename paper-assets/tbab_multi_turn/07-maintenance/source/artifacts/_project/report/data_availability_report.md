# 数据可用性调研报告

调研日期：2026-05-18

## TurnWiseData (arXiv 2603.16759)

- **HuggingFace 地址**：未找到。搜索 HuggingFace 全站未发现任何以 "TurnWise"/"TurnWiseData"/"TurnWiseEval" 命名的公开数据集。
- **可用性**：**不可用**。论文 (Graf et al., 2026) 未提供任何数据下载链接（无 HuggingFace URL、无 GitHub repo、无 Google Drive）。AllenAI 的 HuggingFace 组织页面亦无相关数据集。截至 2026-05-18，TurnWiseData 和 TurnWiseEval 均未公开发布。
- **格式**：论文未说明。
- **轮数分布**：每条对话 2-8 个 user turns，总 token 上限约 4.7k。TurnWiseData seed prompts 取自 WildChat 子集（Dolci Instruct SFT mixture），TurnWiseEval seed prompts 取自 AlpacaEval。
- **数据量**：实验中使用 10k 和 20k 条合成多轮对话进行 post-training。TurnWiseEval 规模未明确披露，论文提及人工验证了 100 条随机样本。
- **划分**：未说明 train/val/test 划分。
- **适配性评估**：**无法使用**。数据未公开，无法下载或复现。若后续作者释放数据，其 2-8 turns 范围偏短（MVP 需要 5-20+ turns），但作为 post-training 数据格式和评估 benchmark 仍有参考价值。

## Microsoft/lost_in_conversation (arXiv 2505.06120)

- **HuggingFace 地址**：https://huggingface.co/datasets/microsoft/lost_in_conversation
- **GitHub**：https://github.com/microsoft/lost_in_conversation
- **可用性**：**公开可用**，许可证 CDLA Permissive 2.0。可通过 `load_dataset("microsoft/lost_in_conversation")` 直接下载。
- **格式**：JSON，仅 train split。每条样本结构：

```json
{
  "task_id": "sharded-{original-task-id}",
  "task": "code|database|actions|math|data2text|summary",
  "shards": [
    {"shard_id": 1, "shard_text": "..."},
    {"shard_id": 2, "shard_text": "..."}
  ],
  "<task_specific_keys>": "<用于评估的参考答案、测试用例等>"
}
```

- **轮数分布**：每条 instruction 包含 2-8 个 shards。在 Sharded 模式下，每个 shard 对应一轮用户消息，即对话有 2-8 轮。论文定义 5 种对话模拟模式：
  - Full：单轮（所有信息一次给出）
  - Concat：单轮（shards 以列表形式拼接）
  - Sharded：多轮（每轮一个 shard）
  - Recap：多轮 + 最后一轮完整重述
  - Snowball：多轮 + 每轮累积重述
- **数据量**：**600 条 sharded instructions**，覆盖 6 个任务（每任务 90-120 条）。这是 benchmark 指令集，不是预构建的对话数据。实际对话需通过 LLM 模拟生成（论文共模拟 200,000+ 条对话，15 个模型 x 8 模型族，每条指令 N=10 次模拟）。
- **任务类型**：Python 编程、数据库查询生成、API 函数调用、初等数学、data2text、摘要生成（6 个任务已发布，翻译任务论文提及但未包含在公开数据中）。
- **评估指标**：每条 instruction 计算三个指标：
  - P̄（averaged performance，平均表现）
  - A⁹⁰（aptitude，能力上界/90th percentile）
  - U₁₀⁹⁰（unreliability，不稳定性/interpercentile range）
- **适配性评估**：
  - 优点：公开可用；有标注参考答案可评估准确率；覆盖多种 NLP 任务；有成熟评估框架和模拟代码。
  - 局限：(1) 仅 600 条指令，需模拟生成对话；(2) 轮数 2-8，低于 MVP 期望的 5-20+ turns；(3) 数据是 "sharded instructions"（信息分片逐步释放），不是自然多轮对话，缺乏真实对话中的澄清、修正、话题转换等动态。

## MVP 推荐

### 结论：推荐使用 Microsoft/lost_in_conversation，但需明确其局限

**推荐理由**：
1. 唯一公开可用的选项（TurnWiseData 未发布）
2. 有完整的评估框架（参考答案 + 自动评估指标），可直接测量多轮准确率下降
3. 600 条指令 x 多种对话模式 x N=10 模拟 = 实验规模可控且充足
4. CDLA Permissive 2.0 许可证，无使用限制

**关键局限与应对**：

| 局限 | 影响 | 应对方案 |
|------|------|---------|
| 轮数仅 2-8 | 无法测试 10+ turns 的长对话场景 | MVP 阶段聚焦 2-8 turns 验证核心假设；后续自行构建长对话数据 |
| 非自然对话 | sharded instructions 缺乏真实对话动态 | 可作为受控实验的优势：排除对话复杂性干扰，隔离"多轮信息分散"这一核心变量 |
| 仅 600 条 | 数据量偏少 | 每条 x N=10 模拟 = 6000 条对话，足够 MVP；或筛选 3-4 个任务 x 100 条 = 300-400 条作为 dev set |

**预处理需求**：
1. 下载 HuggingFace 数据集，解析 JSON 结构
2. 按 task 类型筛选（建议 MVP 先用 code + math，评估最客观）
3. 用论文提供的模拟器 (`run_simulations.py`) 生成 Sharded 模式对话，或自行编写 prompt 模板将 shards 组装为多轮对话格式
4. 集成 task-specific 评估逻辑（论文代码已提供）
5. 筛选 shard 数 >= 5 的指令子集，匹配 MVP 对轮数的最低要求

**备选方案**（若 lost_in_conversation 的 "信息分片" 范式不符合研究目标）：
- 关注 TurnWiseData 后续是否公开（联系作者 Victoria Graf / AllenAI）
- 使用 WildChat 等自然对话数据集自行构建 benchmark（但需自建评估标注）
- 用 MT-Bench / LMSYS-Chat-1M 的多轮子集（但标注不针对多轮准确率下降）
