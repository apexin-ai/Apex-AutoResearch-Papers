# rl-active-probe-fl — Research Dashboard

> 最后更新: 2026-05-14 07:09 UTC | 更新原因: Day 1 进展更新：SFT 完成，GRPO+eval 运行中

## 核心方向
训练代码 LLM (Qwen3-8B) 通过 RL (GRPO) 生成可执行的诊断性运行时探针，利用"难度-可验证性对齐"特性提升 debugging 性能。目标 EMNLP 2026 ARR (DDL 2026-05-25)。

## 当前进展
- 阶段：MVP 验证（Day 1, 5/14）
- ✅ 数据 pipeline 完成：683 → 496 validated → 294 train + 202 eval
- ✅ Probe distillation 完成：294/294 (0 失败)
- ✅ SFT 完成：loss 2.133→1.550, 3min, checkpoint saved
- 🔄 GRPO 训练中：GPU 0, 0/73 steps, fix-based reward, 预计 1-3h
- 🔄 Base eval 运行中：GPU 1, 202 samples
- 🔄 Qwen3-30B-A3B 后台下载中（全量阶段 API 替代）

## MVP 验证方案
**核心假设**: GRPO with fix-based reward > SFT-only on debugging accuracy
**Pass 标准**:
- 主标准：SFT+GRPO > SFT-only ≥ 3pp (n=202 eval)
- 辅助：bootstrap 90% CI 下界 ≥ 0pp
- 探针质量：GRPO 探针执行成功率 ≥ 80%
- Probe-dependence: ≥ 20% fixes 在 real vs null probe output 下不同
**Kill criteria**: temp ∈ {0.7, 1.0} × probe-dep weight ∈ {0.05, 0.1}，最优 2 组仍不满足即 fail

## 近期任务
- [ ] GRPO 训练完成 → 记录 reward 曲线
- [ ] Base eval 完成 → 记录 baseline metrics
- [ ] 启动 eval-sft + eval-grpo（可并行双卡）
- [ ] 汇总 MVP pass/fail 判断
- [ ] Qwen3-30B-A3B 下载完成 → 验证 vLLM 推理可用

## GPU 预算
- 配置：2× RTX PRO 6000 Blackwell 94GB (gpu-6000pro-1)
- GPU 0: GRPO 训练 (64.4GB/97.9GB)
- GPU 1: Base eval (16.8GB/97.9GB)
- 约束：C001 白名单 cuda:0, cuda:1

## 时间线（更新）
- Day 1 (5/14): ✅ 数据+SFT+GRPO启动+base eval
- Day 2 (5/15): GRPO完成 → eval-sft + eval-grpo → MVP 判断
- Day 3-7: 全量实验（如 MVP pass）
- Day 8-11: 论文写作 + 提交

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D009 | 2026-05-14 | Sandbox 修复后首次真实 eval：base=74.8% SFT=76.7%（+1.9pp 不 | eval-base-v3, eval-sft-v2, grpo-mvp-v2 |
| D008 | 2026-05-14 | probe_executed=0% 根因确认为 _insert_probe() 正则 bug，修复后 | eval-sft-v1, eval-base-v2, grpo-mvp-v1 |
| D007 | 2026-05-14 | eval 结果：probe 格式 OK 但执行率 0%，反馈回路断裂，批准诊断+修复方案 C | eval-sft-v1, eval-base-v2 |
| D006 | 2026-05-14 | GRPO reward=0 因 Qwen3-8B thinking 模式消耗全部 completio | grpo-mvp-v1, eval-base-v1 |
| D005 | 2026-05-14 | 后台下载 Qwen3-30B-A3B 用于全量阶段本地推理替代 API，不影响 MVP 训练（仍用  | — |
| D004 | 2026-05-14 | 接受 496 有效测试样本，划分 296 train + 200 eval，不等 API 充值 | — |
| D003 | 2026-05-14 | MVP GRPO 必须实现 fix-based reward（probe→execute→fix→t | — |
| D002 | 2026-05-14 | DebugBench 测试用例方案：用 solution + Claude API 生成可执行测试， | — |
| D001 | 2026-05-14 | MVP eval 样本量从 100 扩至 200，增加 bootstrap CI 辅助 pass 标 | — |

