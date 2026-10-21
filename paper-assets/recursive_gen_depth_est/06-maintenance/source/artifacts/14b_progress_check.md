# 14B 实验进度检查

**检查时间**: 2026-05-20 11:04 UTC

## GPU 状态

| GPU | 型号 | 显存占用 | GPU 利用率 | 温度 |
|-----|------|---------|-----------|------|
| 0 | NVIDIA RTX PRO 6000 Black | 32,383 / 97,887 MiB | 92% | 51°C |
| 1 | NVIDIA RTX PRO 6000 Black | 32,423 / 97,887 MiB | 93% | 51°C |

## 实验 1: qwen25_14b_temp09 (GPU 0)

- **PID**: 776596 (子进程 776616)
- **状态**: **RUNNING**
- **运行时间**: 1天 0小时 4分
- **当前阶段**: Phase 3.3b — Generate d3 (用 LoRA(d2) 生成 5000 samples)
- **阶段细节**: 14B 模型权重已加载完毕 (579/579)，正在生成文本
- **已完成阶段**:
  - [x] Phase 2: Generate d0
  - [x] Phase 3.1a: LoRA finetune d0
  - [x] Phase 3.1b: Generate d1
  - [x] Phase 3.2a: LoRA finetune d1
  - [x] Phase 3.2b: Generate d2
  - [x] Phase 3.3a: LoRA finetune d2 ✓ (adapter saved)
  - [ ] **Phase 3.3b: Generate d3** ← 当前
  - [ ] Phase 4: Feature extraction (self-reference)
  - [ ] Phase 5: Classification (RF + LR, 5-fold CV)
- **进度估计**: ~75% (7/9 阶段完成，当前阶段进行中)
- **预计剩余时间**: 3-5 小时 (d3 生成 + 特征提取 + 分类)

## 实验 2: qwen25_14b_topk50 (GPU 1)

- **PID**: 787051
- **状态**: **RUNNING**
- **运行时间**: 22小时 4分
- **当前阶段**: Phase 3.3b — Generate d3 (用 LoRA(d2) 生成 5000 samples)
- **阶段细节**: 14B 模型权重已加载完毕 (579/579)，正在生成文本
- **已完成阶段**:
  - [x] Phase 2: Generate d0
  - [x] Phase 3.1a: LoRA finetune d0
  - [x] Phase 3.1b: Generate d1
  - [x] Phase 3.2a: LoRA finetune d1
  - [x] Phase 3.2b: Generate d2
  - [x] Phase 3.3a: LoRA finetune d2 ✓ (adapter saved)
  - [ ] **Phase 3.3b: Generate d3** ← 当前
  - [ ] Phase 4: Feature extraction (self-reference)
  - [ ] Phase 5: Classification (RF + LR, 5-fold CV)
- **进度估计**: ~75% (7/9 阶段完成，当前阶段进行中)
- **预计剩余时间**: 3-5 小时 (d3 生成 + 特征提取 + 分类)

## 总结

两个实验进度一致，都在 pipeline 的最后一个生成阶段 (d3)。生成完成后只剩特征提取和分类两个轻量阶段。预计今天内完成。
