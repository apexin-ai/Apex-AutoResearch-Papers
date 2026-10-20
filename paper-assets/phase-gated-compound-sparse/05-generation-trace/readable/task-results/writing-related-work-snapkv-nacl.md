# writing related work snapkv nacl

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-snapkv-nacl_20260514T055834_result.json`
- **Structured JSON:** [`5185b90ef7203f50912f.json`](../../sessions/51/5185b90ef7203f50912f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已更新完毕。以下是修改总结和 BibTeX 条目：

**修改内容：**
- L20: 插入 SnapKV（NeurIPS 2024）——基于 observation window 的 per-head KV 选择，一次性快照无法跨 phase 调整
- L22: 插入 NACL（ACL 2024）——proxy-token + random eviction 对抗 attention bias，但 policy 全程不变
- L39: gap statement 从 "No prior work" 软化为 "To our knowledge, no prior work"

**BibTeX 条目：**

```bibtex
@inproceedings{snapkv-neurips2024,
  title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},
  author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2024}
}

@inproceedings{nacl-acl2024,
  title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},
  author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},
  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
  year      = {2024}
}
```

---
