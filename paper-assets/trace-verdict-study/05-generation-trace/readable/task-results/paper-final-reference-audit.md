# paper final reference audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final_reference_audit_20260516T024835_result.json`
- **Structured JSON:** [`bd2d6bf601b050400762.json`](../../sessions/bd/bd2d6bf601b050400762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Reference Audit 结果

| 指标 | 数量 |
|------|------|
| **PASS** | **27** |
| **WARN** | **10** |
| **FAIL** | **0** |

**Bib 条目 27 个，Cite key 27 个，完全一一对应。无缺失，无孤立，无 placeholder。**

### 10 个 WARN（非致命，可选修复）

**Type Mismatch (2)**
- `hu2022lora` — `@article` 但 journal 填的是 "Proceedings of...ICLR"，应为 `@inproceedings` + `booktitle`
- `haque2025traces` — `@article` 但 journal 是 "KnowledgeNLP Workshop at ACL 2025"，应为 `@inproceedings` + `booktitle`

**ArXiv-only (8)** — 仍标记为 arXiv preprint，需确认是否已有正式 venue：
| Key | 说明 |
|-----|------|
| `austin2021program` | Google 2021，未正式发表，arXiv 合理 |
| `chen2021evaluating` | Codex/HumanEval，未正式发表，arXiv 合理 |
| `deepseek2024coder` | 2024，未查到正式 venue |
| `ferrando2025execute` | 2025，较新 |
| `qwen2025coder` | 2025，技术报告 |
| `wang2025inspectcoder` | 2025，较新 |
| `wu2026runtime` | 2026，非常新 |
| `yang2025apsg` | 2025，较新 |

### 结论

上次修复的 10 个问题全部保留完好。新增引用（`spiess2025calibration` in experiments.tex, `yang2024generalization` in discussion.tex）均已在 bib 中且字段完整。无 FAIL 项，audit 通过。

2 个 type-mismatch WARN 如需修复，改 `@article`→`@inproceedings` + `journal`→`booktitle` 即可；8 个 arXiv-only 多数为未正式发表的论文/技术报告，保持现状合理。

---
