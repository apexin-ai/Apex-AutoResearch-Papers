# Reference Audit: 2025-2026 Entries

## Summary
- Total checked: 17
- ✅ Confirmed: 15
- ⚠️ Issues found: 2
- ❌ Not found: 0

## Detailed Results

### ✅ Confirmed

| Key | Title | Source | Notes |
|-----|-------|--------|-------|
| `retool-2025` | ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | arXiv:2504.11536 | matches bib |
| `mixture-of-recursions-2025` | Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation | NeurIPS 2025 (OpenReview, arXiv:2507.10524) | matches bib |
| `toolace-2025` | ToolACE: Winning the Points of LLM Function Calling | ICLR 2025 (proceedings + arXiv:2409.00920) | matches bib |
| `saferoute-2025` | SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs | Findings of ACL 2025 (ACL Anthology + arXiv:2502.12464) | matches bib |
| `pona2025abstract` | Abstract Counterfactuals for Language Model Agents | arXiv:2506.02946 | matches bib |
| `axis-2026` | Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour | arXiv:2505.17801 | matches bib; key name says "2026" but year=2025 is correct |
| `bonagiri2025check` | Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety | arXiv:2510.16492 | matches bib; also accepted at NeurIPS 2025 Workshop (Reliable ML from Unreliable Data) |
| `cogrouter-2026` | Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents | arXiv:2602.12662 | matches bib |
| `mtrouter-2026` | MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings | ACL 2026 Main (arXiv:2604.23530) | matches bib |
| `tool-overuse-illusion-2026` | The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge? | arXiv:2604.19749 | matches bib |
| `when2tool-2026` | LLM Agents Already Know When to Call Tools -- Even Without Reasoning | arXiv:2605.09252 | matches bib |
| `tool-use-tax-2026` | Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents | arXiv:2605.00136 | matches bib |
| `to-call-or-not-2026` | To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling | arXiv:2605.00737 | matches bib |
| `budget-aware-routing-2026` | Budget-Aware Agentic Routing via Boundary-Guided Training | arXiv:2602.21227 | matches bib |
| `cso-2026` | Verified Critical Step Optimization for LLM Agents | arXiv:2602.03412 | matches bib; under review at ACL 2026 (OpenReview) |

### ⚠️ Issues

| Key | Issue | Suggested Fix |
|-----|-------|---------------|
| `salt-2026` | 已正式发表于 Findings of EACL 2026（ACL Anthology: 2026.findings-eacl.247），但 bib 仍标注为 arXiv preprint (year=2025) | 改为 `@inproceedings`，`booktitle={Findings of the Association for Computational Linguistics: EACL}`, `year={2026}` |
| `ares-2026` | arXiv 官方标题为 "Ares"（首字母大写），bib 中写成全大写 "ARES" | 将 title 中 `ARES` 改为 `{Ares}` 以匹配原文 |

### ❌ Not Found

（无）
