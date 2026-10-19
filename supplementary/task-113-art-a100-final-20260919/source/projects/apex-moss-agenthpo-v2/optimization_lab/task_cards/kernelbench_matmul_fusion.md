# KernelBench 专用任务卡：Matmul + Subtract + Multiply + ReLU

- 固定题目：`level2/9_Matmul_Subtract_Multiply_ReLU.py`
- 固定硬件：`a100jump` 的第4号 NVIDIA A100-SXM4 80GB；正式比较期间不得换卡
- 目标：保持完整数值正确性，同时减少矩阵乘法之后三段操作的额外读写和启动开销
- 允许：复用成熟矩阵乘法路径，并针对固定形状融合后处理；保存本题历史经验并回滚
- 禁止：修改参考题、评分器、计时方式、随机输入或运行环境
- 反馈顺序：编译 → 正确性 → 速度；前一关不通过时不使用后一关成绩

本题拥有独立 Harness 和账本，不读取 LayerNorm 任务的候选或失败轨迹。
