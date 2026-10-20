# 诊断报告: gen_gpt2m_a100_s43_bf16

**日期**: 2026-05-18
**服务器**: westd-17855
**状态**: 实验已成功完成，EXIT_CODE=129 为误报

## 1. 失败根因

**不是真正的失败。** 进程退出码 129 (SIGHUP) 发生在实验逻辑全部完成之后。

时间线：
- 脚本完成 gen_0 (baseline) 到 gen_10/10 的全部训练和评估
- 计算并保存 all_metrics.json（11 个 generation 完整指标）
- 写入哨兵文件 EXIT_CODE = **0**（脚本自身判定成功）
- 之后进程收到 SIGHUP，wrapper 报告 EXIT_CODE=129

SIGHUP 来源推测：tmux session/pane 在实验完成后被清理，或 wrapper 脚本发送了收尾信号。同服务器 alpha_sweep_a060_s42_bf16 (cuda:3) 同时段以相同方式"失败"，但同样已完成全部工作（哨兵文件=0，指标完整）。

## 2. 实验进度

| 项目 | 状态 |
|------|------|
| Generation 0 (baseline) | 完成 |
| Generation 1-10 | 全部完成 |
| all_metrics.json | 11 条记录，完整 |
| 哨兵 EXIT_CODE 文件 | 内容为 0 |
| gen_10/checkpoint | 存在 |
| gen_10/metrics.json | 存在，数据完整 |

最终 generation 10 指标：ppl=55.49, entropy=3.00, eff_rank=3.2, mauve=0.023

## 3. 是否可恢复 / 需要重跑

**不需要重跑。** 实验数据完整，所有 generation 的 checkpoint、synthetic_data、metrics 均已保存。

## 4. 建议的修复方案

- 监控系统应以哨兵文件 EXIT_CODE 的内容（而非进程退出码）作为实验成功/失败的判定依据
- 当哨兵文件存在且内容为 0 时，忽略进程级 SIGHUP
- alpha_sweep_a060_s42_bf16 同理，无需重跑

## 附：同批次受影响实验

| exp_id | 哨兵文件 | 进程退出码 | 实际状态 |
|--------|----------|------------|----------|
| gen_gpt2m_a100_s43_bf16 | 0 | 129 | 完成 |
| alpha_sweep_a060_s42_bf16 | 0 | 129 | 完成 |
