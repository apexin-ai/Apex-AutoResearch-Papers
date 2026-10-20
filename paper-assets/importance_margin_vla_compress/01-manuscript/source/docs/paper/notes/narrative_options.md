# Introduction Narrative 两个方向草案
# Paper Agent 准备 — 2026-05-17

---

## Direction A: Pure Negative Results + "Smart Methods Needed"

### 故事线
ViT token pruning 在分类任务上成功 → 社区自然推广到 VLA → 我们系统测试发现 naive pruning 在 SmolVLA 上完全失败（cliff edge）→ 机制分析（attention uniformity + instantaneous disruption + offline metric disconnect）→ 启示：VLA token reduction 需要 domain-specific 方法（如 VLA-IAP 的几何先验 + 动态调度），不能简单迁移

### 贡献定位
- C1: 首次系统性 closed-loop 评估 VLA vision token reduction → cliff-edge 现象
- C2: 机制解释（为什么 ViT 可以但 VLA 不行）
- C3: Offline metric disconnect（标准验证流程不可靠）

### 优势
- 已有全部数据，无需新实验
- 叙事完整、逻辑自洽
- VLA-IAP 的成功反而加强而非削弱我们的论点（证实 smart methods 可行但 naive methods 不行）

### 风险
- Reviewer 可能认为 "只在一个小模型上的负结果" 泛化性不足
- "不 work" 的故事吸引力有限，缺少正面贡献
- VLA-IAP 已经展示了解决方案，审稿人可能问 "why not try VLA-IAP's approach?"

### Related Work 中 VLA-IAP 的定位
"Recent concurrent work VLA-IAP [Wang et al. 2026] reports successful VLA token pruning on OpenVLA-OFT (7B) using geometric priors and dynamic scheduling, achieving 97.8% SR at 70% retention. This result does not contradict our findings; rather, it confirms that VLA token reduction requires domain-specific methods with external geometric signals and adaptive scheduling, rather than the attention-based approaches that work for ViT classification. The success of VLA-IAP on a 7B model with 97.1% baseline SR does not guarantee that similar approaches transfer to compact VLAs (451M, 44.8% SR) where the model has less representational redundancy."

---

## Direction B: Negative Motivation + Positive Smart Compression

### 故事线
ViT token pruning 成功 → 应用到 VLA：naive methods 完全失败（cliff edge on SmolVLA）→ 分析为什么失败 → 基于分析洞察设计 smart compression → 跨模型验证（SmolVLA + OpenVLA）→ Smart compression 保持 SR 同时加速推理

### 可能的 Smart Compression 方法
1. **Geometric prior (仿 VLA-IAP)**: Sobel edge + structural anchor 保护
2. **Dynamic scheduling**: 根据 action uncertainty 动态调整保留比例
3. **KV cache reuse (仿 VLA-Cache)**: 时序连续帧的 vision token KV cache 复用
4. **Learned spatial pooling**: 训练时就学习将 256 → 128 tokens 的聚合
5. **Hybrid**: 静态区域 cache + 动态区域保留

### 贡献定位
- C1: Cliff-edge 现象 + 机制分析（motivation）
- C2: Smart compression 方法设计（基于我们的 attention uniformity 洞察）
- C3: 跨模型验证（SmolVLA + OpenVLA）

### 优势
- 有正面贡献，论文更有吸引力
- "问题 → 分析 → 解决" 的完整故事
- 跨模型验证提升泛化性

### 风险
- 需要大量新实验（OpenVLA 部署、smart compression 实现、调参、closed-loop eval）
- 时间紧张：CoRL abstract DDL May 26 (9天), paper DDL May 29 (12天)
- Smart compression 在 SmolVLA (44.8% baseline) 上可能仍然失败（模型容错空间太小）
- 与 VLA-IAP 的差异化不够明确

### 关键不确定性
- **SmolVLA 44.8% baseline 是否允许任何压缩？** 模型本身性能就不高，可能没有"可压缩的余量"
- **OpenVLA 部署可行性如何？** 需要 7B 模型的 GPU 资源 + LIBERO 环境适配
- **时间窗口够不够？** 12 天内做完新方法设计 + 实现 + 跨模型实验 + 论文重写

---

## 建议

**如果 OpenVLA 可行性调研 + smart compression 方案能在 3-5 天内完成原型**:
→ Direction B 值得尝试。但需要 fallback plan: 如果 smart compression 在 SmolVLA 上也失败，这个"连 smart methods 也失败"的结果反而让 negative result 更有说服力。

**如果时间不够或 OpenVLA 部署困难**:
→ Direction A 更安全。4 个章节已完成，只需补 Related Work + Discussion + Conclusion + Abstract，然后做 refinement。在 Discussion 中详细讨论 VLA-IAP 的成功和我们发现之间的关系，指出 model scale / baseline quality / geometric prior 的差异。

**Hybrid 策略**: 先走 Direction A 完成完整初稿（2天），同时 Agent 并行做 OpenVLA + smart compression 实验。如果实验有正面结果，在 paper DDL 前切换到 Direction B；如果没有，Direction A 已经 ready。
