# Framing 调整提案 — mvp_pilot_004 NEGATIVE

## 原 Claim
SJ 在 RE（high-headroom subtask）上 ρ ≥ 0.40 且显著优于 κ

## 实际结果
- NER: ρ_sj=0.383, SJ>κ +0.124 (p=7e-20) — 强正向
- RE: ρ_sj=0.244, κ beats SJ on full set (-0.034) — 明确负向
- RE pct_zero=44.3%, 模型质量提升未改善 ρ

## 根因
RE SJ 乘性公式 (head_sj × tail_sj × type_match) 在双 span 不确定性下结构性劣于 κ

## 三种备选
A. NER-Primary + RE 诊断（最安全）
B. 度量分解 Pivot（最强但有风险）
C. 质量门控假设（学术价值高但实验重）

## 建议决策路径
E1 (component-wise RE, 30min CPU) → 结果决定 A vs B → E2(T=0.7)+E3(N=16) 并行

## 状态
等待 Director 审批