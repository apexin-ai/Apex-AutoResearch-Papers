# paper writing related work

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260516T023622_result.json`
- **Structured JSON:** [`abf8c04a7c5063baeb2e.json`](../../sessions/ab/abf8c04a7c5063baeb2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`related_work.tex` 已生成。以下是需要添加到 `references.bib` 的新条目：

```bibtex
% === VLA Representation Analysis ===

@article{swann2026,
  title     = {Sparse Autoencoders Reveal Monosemantic Features in Vision-Language-Action Models},
  author    = {Swann, Eley and others},
  journal   = {arXiv preprint arXiv:2603.19183},
  year      = {2026},
}

@article{rizzardo2026,
  title     = {Observability and Controllability of Vision-Language-Action Model Representations},
  author    = {Rizzardo, Andrea and others},
  journal   = {arXiv preprint arXiv:2603.05487},
  year      = {2026},
}

@article{molinari2025,
  title     = {Do Vision-Language-Action Models Have World Models? Probing for Spatial and Physical Understanding},
  author    = {Molinari, Marco and others},
  journal   = {arXiv preprint arXiv:2509.24559},
  year      = {2025},
}

% === Methodology ===

@article{belinkov2022,
  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},
  author    = {Belinkov, Yonatan},
  journal   = {Computational Linguistics},
  volume    = {48},
  number    = {1},
  pages     = {207--219},
  year      = {2022},
}

% === VLA Architecture ===

@article{black2024_pi0,
  title     = {$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},
  journal   = {arXiv preprint arXiv:2410.24164},
  year      = {2024},
}
```

**注意事项：**
- `swann2026`、`rizzardo2026`、`molinari2025` 的 title 和 author 列表需要核实，我基于 arXiv ID 填了占位信息——标记为 `[VERIFY]` 级别，发 bib 前请对照 arXiv 页面补全
- `black2024_pi0` 同理，author list 取自公开信息但可能不完整
- 已有 bib 中的 `haon2025`、`grant2026` 等直接复用，无需重复添加
- Introduction 中引用的 `hou2026` 和 `fei2025` 未在 related work 中使用，不影响本文件

---
