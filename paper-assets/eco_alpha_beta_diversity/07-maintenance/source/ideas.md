# Idea Inbox

## 待验证

- [2026-05-21] **语义级多样性分解**：用 sentence-transformers embedding 替代 word unigram，在语义空间计算 Hill numbers。假设：语义级 beta 下降比词汇级更显著，因为 LLM 同质化主要发生在语义层面而非词汇表面。需要 GPU。优先级：MVP 通过后第一个扩展。
- [2026-05-21] **多数据集验证**：在其他 AI 辅助写作数据集上复现 alpha↑beta↓ 模式。候选：(1) Padmakumar et al. (2024) 多轮 LLM 交互写作数据 (2) LAMP benchmark 写作子集 (3) 爬取 Reddit WritingPrompts 的 ChatGPT 前后对比。目标：证明发现的普适性而非数据集特异性。优先级：MVP 通过后与语义级并行推进。
- [2026-05-21] **干预假设测试（因果推断）**：设计控制实验测试不同 LLM 干预模式对 beta diversity 的差异影响。假设：AI-as-editor（润色）比 AI-as-idea-generator（提供创意）对 beta 的压缩更严重，因为编辑操作直接同质化表达而创意生成保留了作者独特的展开方式。可利用 Doshi 数据集的 3 条件结构（no-AI vs AI-editor vs AI-ideas+editor）初步验证，后续需新数据集做因果确认。优先级：中期，需先确认 MVP 基础模式。
## ACTIVE
