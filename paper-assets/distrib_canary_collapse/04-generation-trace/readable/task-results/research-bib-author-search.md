# research bib author search

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bib-author-search_20260515T183343_result.json`
- **Structured JSON:** [`e579150dd847dbc1b2d8.json`](../../sessions/e5/e579150dd847dbc1b2d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

### P0: Seddik et al. (2024)

**Confirmed: `epstein2024howbad` IS the Seddik paper.** The existing entry (arXiv:2404.05090) is "How Bad is Training on Synthetic Data?" — the first author is **Mohamed El Amine Seddik**, not "Epstein". The bib key `epstein2024howbad` is a misnomer.

Full authors: **Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah**

Recommended fix — update the author field and optionally rename the key to `seddik2024howbad`:
```
author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane}
```

No new bib entry needed — just correct the existing one.

---

### P1: Author field completions

**1. gauthier2026alignment** (arXiv:2605.04266)
```
author = {Gauthier, Etienne and Bach, Francis and Jordan, Michael I.}
```

**2. shi2026pruning** (arXiv:2605.07271)
```
author = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin}
```

**3. tubingen2026diffusion** (arXiv:2605.06366)
```
author = {Conzelmann, Alexander and Catalan-Tatjer, Albert and Liu, Shiwei}
```
(The actual authors are individuals from Tübingen AI Center, not the institution itself.)

**4. bergsma2026scaling** (arXiv:2509.25087)
```
author = {Bergsma, Shane and Zhang, Bin Claire and Dey, Nolan and Muhammad, Shaheer and Gosal, Gurpreet and Hestness, Joel}
```

**5. wang2025epistemic** (arXiv:2510.04226)
```
author = {Wright, Dustin and Masud, Sarah and Moore, Jared and Yadav, Srishti and Antoniak, Maria and Park, Chan Young and Augenstein, Isabelle}
```
Note: first author is actually **Dustin Wright**, not Wang. The bib key `wang2025epistemic` is also a misnomer — consider renaming to `wright2025epistemic`.

Sources:
- [arXiv:2404.05090 - How Bad is Training on Synthetic Data?](https://arxiv.org/abs/2404.05090)
- [arXiv:2605.04266 - Explaining and Preventing Alignment Collapse in Iterative RLHF](https://arxiv.org/abs/2605.04266)
- [arXiv:2605.07271 - Understanding Performance Collapse in Layer-Pruned LLMs](https://arxiv.org/abs/2605.07271)
- [arXiv:2605.06366 - Layer Collapse in Diffusion Language Models](https://arxiv.org/html/2605.06366v2)
- [arXiv:2509.25087 - Scaling with Collapse](https://arxiv.org/abs/2509.25087)
- [arXiv:2510.04226 - Epistemic Diversity and Knowledge Collapse](https://arxiv.org/abs/2510.04226)

---
