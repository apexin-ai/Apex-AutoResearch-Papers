## Entity Consensus Construction Results

**FewNERD** — consensus (high=0.5): **0.7583 vs 0.7478** (+1.05pp over greedy), near LP selection (0.7666).
**SciERC** — consensus (high=0.6): 0.6444 vs 0.6439 (near greedy), below LP selection (0.6501).
**CoNLL** — greedy strongest (0.9070), all consensus configs below.

Pattern: higher threshold → lower F1 (conservative → high precision, low recall).
LP-weighted medium zone helps at low thresholds.

⚠️ Pending unified_metrics revalidation.

Output: output/entity_consensus_results.json, code/entity_consensus.py