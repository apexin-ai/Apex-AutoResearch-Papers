# exp vllm guided json

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_vllm-guided-json_20260522T131448_result.json`
- **Structured JSON:** [`8f0416c7c03fcb357878.json`](../../sessions/8f/8f0416c7c03fcb357878.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 总结

vLLM guided_json 验证实验成功，确认 **guided_json ≈ Grammar-Only ablation**：

| Metric | Grammar-Only (ours) | vLLM guided_json | Δ |
|--------|:---:|:---:|:---:|
| DR% | 14.84 | **15.26** | +0.42 |
| RV% | 0 | **0** | 0 |
| ET% | 0 | **0** | 0 |
| CF% | 0.08 | **0.04** | -0.04 |
| R-F1 | 8.23 | **8.75** | +0.52 |
| E-F1 | 30.98 | **30.91** | -0.07 |

所有差异在噪声范围内。两者都保证 RV=0%, ET=0%（JSON schema + enum 约束），但都留下 ~15% 的 domain-range violations 未处理——这正是我们论文中 semantic constraint layer 的价值所在。

产出文件：
- 推理结果: `outputs/vllm_guided_json_scierc_zs.jsonl`
- 违规报告: `outputs/violation_report_vllm_guided_json.json`
- 实验注册: `vllm_guided_json_scierc_zs` (DONE/success)
- Artifact: `art_20260522_7c65fb`

---
