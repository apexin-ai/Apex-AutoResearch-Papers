# audit citation verify baselines

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_citation_verify_baselines_20260517T044341_result.json`
- **Structured JSON:** [`1bc32c75bd3dfb7bf714.json`](../../sessions/1b/1bc32c75bd3dfb7bf714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果如下：

| cite_key | 声称 venue | 声称 arXiv | Status | 实际内容 |
|----------|-----------|-----------|--------|---------|
| `li_2025_dcr` | EMNLP 2025 | 无 | **MISMATCH** | 论文真实存在：*DCR: Quantifying Data Contamination in LLMs Evaluation*，EMNLP 2025。但作者是 **Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, Tahar Kechadi**。无 "Li" 也无 "Sherborne"。cite key 首作者错误。 |
| `choi_2025_kds` | ICML 2025 | 2502.00678 | **EXISTS** | 完全匹配。*How Contaminated Is Your Benchmark? Measuring Dataset Leakage in LLMs with Kernel Divergence*。作者 Hyeong Kyu Choi, Maxim Khanov, Hongxin Wei, Yixuan Li。ICML 2025 confirmed (poster #43619)。方法名 KDS 正确。 |
| `xu2025emperor` | ICML 2025 | 2503.16402 | **MISMATCH** | 论文真实存在：*The Emperor's New Clothes in Benchmarking?*，ICML 2025 confirmed (poster #45153)。但作者是 **Yifan Sun, Han Wang, Dongbai Li, Gang Wang, Huan Zhang**。无 "Xu"。cite key 首作者错误。 |

### 修复建议

- `li_2025_dcr` → 改为 `xu2025dcr`，作者列表改为 Xu et al.
- `choi_2025_kds` → 无需修改
- `xu2025emperor` → 改为 `sun2025emperor`，作者列表改为 Sun et al.

Sources:
- [KDS - ICML 2025 Poster](https://icml.cc/virtual/2025/poster/43619)
- [KDS - arXiv](https://arxiv.org/abs/2502.00678)
- [Emperor - ICML 2025 Poster](https://icml.cc/virtual/2025/poster/45153)
- [Emperor - GitHub](https://github.com/ASTRAL-Group/BDC-mitigation-assessment)
- [DCR - ACL Anthology](https://aclanthology.org/2025.emnlp-main.1173/)

---
