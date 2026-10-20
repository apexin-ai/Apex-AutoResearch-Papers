# Handover — 2026-05-13

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| bcp7b-multirun-001 | 7B BCP multi-run replication: verify FM1 (completion collapse) and FM2 (cross-dim interference) reproducibility across 3 additional runs | — | — | — |

## 待处理
（无）

## 近期结论
- **bootstrap-ci-001** (success): —
  [bootstrap_ci_report](/api/workspace-files/projects/demo_calibrated_sim/artifacts/bootstrap-ci-001/report/bootstrap_ci_report.md)
- **qwen14b-bcp-001** (success): Qwen2.5-14B-Instruct FP16 (TP=2) BCP eval: cross-scale verification of BCP failure mechanism. AWQ quantization corrupts tool-call tokens, switched to FP16 tensor-parallel. Quick test: 40% completion (2/5), passes >20% gate. ← 基于 mvp-004
  [qwen14b-bcp-001 FM Replication Analysis](/api/workspace-files/projects/demo_calibrated_sim/artifacts/qwen14b-bcp-001/report/fm_replication_analysis.md)
- **mistral-bcp-001** (negative): Mistral-7B-Instruct BCP eval: completion >20% + BCP behavior shift observable → Plan B (empirical analysis) viable for EMNLP submission ← 基于 mvp-004
  [mistral-bcp-001-results](/api/workspace-files/projects/demo_calibrated_sim/artifacts/mistral-bcp-001/report/mistral-bcp-001-report.md)

## 趋势
成功 6 / 负向 5 / 失败 1 / 共 17

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
cqa1-21977: 无 GPU 信息

## 告警
- mvp-001: 训练失败 — unknown
- mvp-002: 已被终止 — unknown
- mvp-003: 已被终止 — unknown
- aave-corpus-gen: 已被终止 — unknown
- llama-bcp-001: 已被终止 — unknown
- hgate-dpo003: 已被终止 — unknown
