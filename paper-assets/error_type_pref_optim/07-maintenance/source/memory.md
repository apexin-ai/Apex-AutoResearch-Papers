# error_type_pref_optim — Memory

## Phase A 操作定义（Director 2026-05-14 确认）

- **step 粒度**: 1 step = 1 agent turn（agent 发 action + 环境返回 observation）
- **correction horizon 测量**: 每个 failure step 生成 N=10 correction continuations，取 10 次中到 recovery 的最小 agent turns；10 次全失败记为 "uncorrectable" 不纳入统计
- **多类型重叠**: 按 root cause 归类（如错误 action 因 subgoal 分解错误导致 → 归 planning error）；LLM 输出 primary error type + reasoning
- **预期分布（校验用）**: action errors ~1.2 steps, verification errors ~3.1 steps, planning errors ~5.8 steps
- **偏差处理**: 实际测量与预期相差大（如三类重叠严重）→ 立即汇报 Director，决定项目是否继续

## 环境信息

- 服务器: gpu-6000pro-2, account root
- GPU: 2 × RTX PRO 6000 Blackwell 96GB (cuda:0, cuda:1)
- 96GB VRAM 支持 Qwen3-8B 全参数 DPO
