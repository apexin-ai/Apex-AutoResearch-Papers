# ops arr checklist

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_arr-checklist_20260523T030743_result.json`
- **Structured JSON:** [`2253ce177da63259325d.json`](../../sessions/22/2253ce177da63259325d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
ARR Submission Checklist:

- [x] 匿名化: PASS
  - \author{Anonymous} ✓
  - \usepackage[review]{acl} (启用匿名模式) ✓
  - 无作者姓名、机构名、个人 URL 泄露 ✓
  - 无 Acknowledgments 节 ✓
  - "Code and response data will be released upon acceptance" 无身份泄露 ✓

- [?] 页面限制: BORDERLINE (需编译确认)
  - 主文 (Abstract→Conclusion) 约 350 行 LaTeX + 3 表 + 2 图 (含 1 个 figure*)
  - 估算 ~7.5–8.1 页，卡在 8 页边界
  - Limitations 和 Reproducibility Statement 在 \bibliography 前，不计入限制 ✓
  - 建议编译 PDF 确认实际页数

- [x] 格式: PASS
  - \documentclass[11pt]{article} ✓
  - \usepackage[review]{acl} (ACL 官方模板) ✓
  - Review mode (非 final) ✓

- [x] Limitations: PASS (但偏长)
  - \section*{Limitations} 存在 ✓
  - 覆盖 ~8 个点 (模型规模、seed 依赖、SFT scope、post-RL N=1、IRT 假设违背、local dependence、参数依赖、无 MIA 对比)
  - 用户规则要求 "~3 个点，不需要很长"——当前 14 行偏长，不影响提交但可考虑精简

- [x] Ethics: PASS
  - 论文 PDF 中无 Ethics Statement (正确——ARR Responsible NLP Checklist 在 OpenReview form 中填写) ✓

- [x] Bib 身份泄露: PASS
  - 所有 URL 均为 arXiv 链接，无个人主页/GitHub ✓
  - 无 "our previous work" 或自引泄露 ✓
  - 33 条引用条目，无可识别身份信息 ✓
```

**需要行动的项**：
1. **编译 PDF 确认页数**——主文内容估算在 8 页边界，需确认不超页
2. **可选：精简 Limitations**——当前 14 行覆盖 ~8 个点，per 用户规则建议缩减到 ~3 个核心点

---
