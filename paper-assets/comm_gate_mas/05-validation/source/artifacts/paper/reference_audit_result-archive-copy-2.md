# Reference Audit Result

Date: 2026-04-28

## 1. "3 Missing References" — Status: RESOLVED

The "3 missing references" trace to decision D106 (2026-04-23), where review round R5 flagged:
- **GUARDIAN** (Zhou et al., NeurIPS 2025) → `zhou_guardian_2025` ✅ in bib + cited
- **AgentDropoutV2** (Wang et al., 2026) → `wang_agentdropout_v2_2026` ✅ in bib + cited
- **TalkHier** (Wang et al., 2025) → `wang_talkhier_2025` ✅ in bib + cited

Earlier rounds also added references (D101: Qamar, Maitra, Shen, Lin; D105: Zheng Thought Communication). All confirmed present.

ROADMAP.md line 55 already marks this resolved: `[x] ~~3 missing references~~ — r11_audit 确认全部已补`

## 2. Cite/Bib Cross-Check

**79 cite keys in tex files. 79 entries in references.bib. Perfect 1:1 match.**

- Orphaned bib entries (in .bib but not \cited): **0**
- Unresolved cite keys (in \cite{} but not in .bib): **0**

No `??` markers expected at compile time.

## 3. Coverage Assessment

The paper cites 79 references spanning:

| Category | Count | Key refs |
|----------|-------|----------|
| Conversation analysis / backchannels | 8 | Yngve 1970, Schegloff 1982, Clark 1989, Qian 2026 |
| Classic MAS communication | 3 | KQML, CommNet, DIAL |
| Speech act theory | 5 | Austin, Searle, DAMSL, ISO, FIPA |
| MAS frameworks | 4 | AutoGen, MetaGPT, CAMEL, AgentVerse |
| Communication efficiency / pruning | 16 | AgentPrune, OPTIMA, AgentDropout(V1/V2), SafeSieve, S²-MAD, etc. |
| Multi-agent debate | 4 | Du 2024, Choi 2025, DeliberationBench, Wu 2025 |
| Topology / protocol | 7 | GoAgent, ProtocolBench, MultiAgentBench, GUARDIAN, etc. |
| Dialogue act analysis | 2 | Qamar 2025, Maitra 2025 |
| Theoretical foundations | 2 | Rizvi-Martel ICLR 2026, Chen Five Ws TMLR 2026 |
| Statistical methods / datasets | 10 | GSM8K, ARC, StrategyQA, Cohen's κ, McNemar, etc. |
| Other (surveys, attribution, misc) | 18 | Various |

### No obvious omissions identified

The paper has strong coverage of:
- LLM-based MAS communication (2024-2026): AgentPrune, OPTIMA, AgentDropout, SafeSieve, S²-MAD, KVComm, InterlAT, DiffMAS, Supervisor, HiveMind, OMAC, AgentDiet
- Message-level analysis: Thought Communication (Zheng, NeurIPS 2025 Spotlight), topology propagation (Shen, EMNLP 2025)
- Theoretical: Rizvi-Martel (ICLR 2026), Chen Five Ws survey (TMLR 2026)
- Classic RL communication: CommNet, DIAL, I-MAC

## 4. Summary

| Check | Result |
|-------|--------|
| 3 missing references from reviewer | ✅ All resolved (GUARDIAN, AgentDropoutV2, TalkHier) |
| Bib entries without \cite{} | ✅ None (0 orphans) |
| \cite{} without bib entry | ✅ None (0 unresolved) |
| Domain coverage gaps | ✅ None identified |
