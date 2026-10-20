# research citation verification r8w5

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_verification_r8w5_20260515T181711_result.json`
- **Structured JSON:** [`b66e081e25af55219720.json`](../../sessions/b6/b66e081e25af55219720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，汇总结果如下：

---

## 1. ThinK (xu2025think)

**验证状态：✅ 正确**

- Title：匹配
- Authors：9 位作者全部匹配（Xu, Jie, Dong, Wang, Lu, Zhou, Saha, Xiong, Sahoo）
- Venue：ICLR 2025 确认（Spotlight paper，[OpenReview](https://openreview.net/forum?id=n0OtGl6VGb) 可查）
- arXiv：2407.21018 ✅

---

## 2. ForesightKV (dong2026foresightkv)

**验证状态：✅ 正确**

- Title：匹配
- Authors：7 位作者全部匹配（Dong, Liu, Li, Chen, Peng, Wang, Zhao）
- arXiv：2602.03203 ✅，2026 年 2 月提交
- Venue：标注为 arXiv preprint，正确。有 [OpenReview 页面](https://openreview.net/forum?id=k5h29Qv7GN) 但未查到正式会议接收记录

---

## 3. Prune-then-Quantize (kim2026pqqp)

**验证状态：✅ 正确**

- Title：匹配
- Authors：6 位作者全部匹配（Kim, Choi, Yang, Kim, Song, Kang）— 末位作者 "U Kang" 是韩国姓名，非缩写，写法正确
- Venue：ICLR 2026 确认（[ICLR 官方 poster 页](https://iclr.cc/virtual/2026/poster/10010118) + [GitHub](https://github.com/snudatalab/PQQP) 均标注 ICLR 2026）
- arXiv：2603.18426 ✅

---

## 4. LKV (lkv-2026)

**验证状态：✅ 正确**

- Title：匹配
- Authors：从 [arXiv 页面](https://arxiv.org/abs/2605.06676) 直接获取的 10 位作者列表与 bib 完全一致：
  Zhou Enshuai, Hao Yifan, Wang Chao, Zhang Rui, Huang Di, Guo Jiaming, Hu Xing, Du Zidong, Guo Qi, Chen Yunji
- arXiv：2605.06676 ✅，2026 年提交
- Venue：标注为 arXiv preprint，正确，未查到会议接收记录

> Director 提到 LKV 作者可能有误，经逐一比对 arXiv 原始页面，**10 位作者姓名和顺序均正确，未发现问题。**

---

## 总结

| 论文 | 状态 | 需修改 |
|------|------|--------|
| ThinK | ✅ | 否 |
| ForesightKV | ✅ | 否 |
| Prune-then-Quantize | ✅ | 否 |
| LKV | ✅ | 否 |

**4 篇引用全部验证通过，无需修正。**

Sources:
- [ThinK - arXiv](https://arxiv.org/abs/2407.21018)
- [ThinK - OpenReview (ICLR 2025)](https://openreview.net/forum?id=n0OtGl6VGb)
- [ForesightKV - arXiv](https://arxiv.org/abs/2602.03203)
- [ForesightKV - OpenReview](https://openreview.net/forum?id=k5h29Qv7GN)
- [PQQP - arXiv](https://arxiv.org/abs/2603.18426)
- [PQQP - ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10010118)
- [PQQP - GitHub](https://github.com/snudatalab/PQQP)
- [LKV - arXiv](https://arxiv.org/abs/2605.06676)

---
