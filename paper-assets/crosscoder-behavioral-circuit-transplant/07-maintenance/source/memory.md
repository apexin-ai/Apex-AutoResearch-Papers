# Memory — crosscoder-behavioral-circuit-transplant

## 核心发现（MVP 系列总结）

### 瓶颈定位：手术机制，不是特征发现
- Crosscoder Gate 2 始终通过（能找到 donor-exclusive features）
- 但 Gate 5（行为改善）在所有实验中系统性失败
- **activation ratio ≠ behavioral relevance**：高 donor/target ratio 的 feature 不一定驱动 DA 行为差异
- A-003v2 证明能移动激活（Gate 3 = 71.9%）但行为仍恶化 → movement ≠ improvement

### 反直觉：高稀疏 < 低稀疏的 Gate 3 表现
- A-003v2 (L0=457, polysemantic): Gate 3 shift = 71.9% PASS
- A-005 (L0=50, TopK): Gate 3 shift = 18.7% FAIL
- 可能原因：TopK crosscoder 训练不充分（Gate 1 FAIL, 仅 41.5% MSE reduction）

### Shift vs Behavior 根本性 tradeoff
- 增大 scale/α 可以增大 activation shift，但同时破坏 PPL
- 低 α: PPL 安全但 shift 不够；高 α: shift 够但 PPL 爆炸且 DA 更差
- 这不是调参能解决的——是方法论层面的问题

## 代码实现教训

### Crosscoder L1 正则化（连续 2 次踩坑）
- **正确实现**: `l1_loss = fd.abs().sum(dim=-1).mean()`
- **错误实现**: `fd.abs().mean()` — 有效惩罚极弱，无法诱导稀疏
- **最终方案**: TopK activation 直接硬约束 L0=K，彻底绕过 L1 调参

### 特征选择
- 原方案: `score = ratio × donor_act_mean`
- **已证明无效**: ratio-based 选择不选行为相关 features
- 待探索: gradient-based attribution 选择

### Gate 1 判定
- 必须同时检查：recon MSE 下降 >50% + L0 在目标范围
- A-005 Gate 1 FAIL (41.5% < 50%) 说明 20 epoch 对 TopK 可能不够

## 环境信息
- home-1x5090 用户 sonny：conda base，HF_HOME=/home/sonny/ssd2/sonny.fu/.hf_cache
- 项目路径：/home/sonny/crosscoder-bct/
- 已有脚本：mvp_experiment.py, mvp_a003v2_bias_injection.py, mvp_A002_experiment.py, mvp_a005_topk.py
