"""CED（Contrastive Evidence Discrimination）对比证据判别奖励。

核心公式:
  p_pos = NLI_entail(concat(cited_evidence), claim)
  p_neg = max_j NLI_entail(neg_sent_j, claim)
  R_CED = max(0, p_pos - p_neg) * I(p_pos > tau)

输入: 关系三元组 + gold evidence 句子 + hard negative 句子
输出: CED 奖励值 ∈ [0, 1]
依赖: transformers, torch
"""

import logging
from typing import Optional

import torch
import torch.nn.functional as F
from transformers import AutoModelForSequenceClassification, AutoTokenizer

logger = logging.getLogger(__name__)

DEFAULT_NLI_MODEL = "cross-encoder/nli-deberta-v3-base"

VERBALIZATION_TEMPLATES = {
    "P6": "The head of government of {head} is {tail}.",
    "P17": "{head} is located in the country {tail}.",
    "P19": "{head} was born in {tail}.",
    "P20": "{head} died in {tail}.",
    "P22": "The father of {head} is {tail}.",
    "P25": "The mother of {head} is {tail}.",
    "P26": "{head} is married to {tail}.",
    "P27": "{head} is a citizen of {tail}.",
    "P30": "{head} is located in the continent of {tail}.",
    "P31": "{head} is an instance of {tail}.",
    "P35": "The head of state of {head} is {tail}.",
    "P36": "The capital of {head} is {tail}.",
    "P37": "The official language of {head} is {tail}.",
    "P39": "{head} held the position of {tail}.",
    "P40": "{head} has a child named {tail}.",
    "P50": "The author of {head} is {tail}.",
    "P54": "{head} is a member of the sports team {tail}.",
    "P57": "The director of {head} is {tail}.",
    "P58": "The screenwriter of {head} is {tail}.",
    "P69": "{head} was educated at {tail}.",
    "P86": "The composer of {head} is {tail}.",
    "P102": "{head} is a member of the political party {tail}.",
    "P108": "{head} is employed by {tail}.",
    "P112": "{head} was founded by {tail}.",
    "P118": "{head} plays in the league {tail}.",
    "P123": "The publisher of {head} is {tail}.",
    "P127": "{head} is owned by {tail}.",
    "P131": "{head} is located in {tail}.",
    "P136": "The genre of {head} is {tail}.",
    "P137": "{head} is operated by {tail}.",
    "P140": "The religion of {head} is {tail}.",
    "P150": "{head} contains the administrative territory {tail}.",
    "P155": "{head} follows {tail}.",
    "P156": "{head} is followed by {tail}.",
    "P159": "The headquarters of {head} is located in {tail}.",
    "P161": "{head} features the cast member {tail}.",
    "P162": "The producer of {head} is {tail}.",
    "P166": "{head} received the award {tail}.",
    "P170": "The creator of {head} is {tail}.",
    "P171": "The parent taxon of {head} is {tail}.",
    "P172": "{head} belongs to the ethnic group {tail}.",
    "P175": "The performer of {head} is {tail}.",
    "P176": "The manufacturer of {head} is {tail}.",
    "P178": "The developer of {head} is {tail}.",
    "P179": "{head} is part of the series {tail}.",
    "P190": "{head} is a sister city of {tail}.",
    "P194": "The legislative body of {head} is {tail}.",
    "P205": "{head} is in the basin of {tail}.",
    "P206": "{head} is located near the body of water {tail}.",
    "P241": "{head} is a branch of the military {tail}.",
    "P264": "The record label of {head} is {tail}.",
    "P272": "The production company of {head} is {tail}.",
    "P276": "{head} is located in {tail}.",
    "P279": "{head} is a subclass of {tail}.",
    "P355": "{head} has the subsidiary {tail}.",
    "P361": "{head} is part of {tail}.",
    "P364": "The original language of {head} is {tail}.",
    "P400": "{head} is available on the platform {tail}.",
    "P403": "{head} flows into {tail}.",
    "P449": "The original network of {head} is {tail}.",
    "P463": "{head} is a member of {tail}.",
    "P488": "The chairperson of {head} is {tail}.",
    "P495": "{head} originates from the country {tail}.",
    "P527": "{head} has the part {tail}.",
    "P551": "{head} resides in {tail}.",
    "P569": "{head} was born on {tail}.",
    "P570": "{head} died on {tail}.",
    "P571": "{head} was established in {tail}.",
    "P576": "{head} was dissolved in {tail}.",
    "P577": "{head} was published on {tail}.",
    "P580": "{head} started in {tail}.",
    "P582": "{head} ended in {tail}.",
    "P585": "{head} occurred at the time {tail}.",
    "P607": "{head} was involved in the conflict {tail}.",
    "P674": "{head} features the character {tail}.",
    "P676": "The lyrics of {head} were written by {tail}.",
    "P706": "{head} is located on the terrain {tail}.",
    "P710": "{head} participated in {tail}.",
    "P737": "{head} was influenced by {tail}.",
    "P740": "{head} was formed in {tail}.",
    "P749": "The parent organization of {head} is {tail}.",
    "P800": "The notable work of {head} is {tail}.",
    "P807": "{head} was separated from {tail}.",
    "P840": "The narrative of {head} is set in {tail}.",
    "P937": "{head} worked in {tail}.",
    "P1001": "{head} applies to the jurisdiction of {tail}.",
    "P1056": "{head} produces {tail}.",
    "P1198": "The unemployment rate of {head} is {tail}.",
    "P1336": "{head} is claimed by {tail}.",
    "P1344": "{head} participated in {tail}.",
    "P1365": "{head} replaces {tail}.",
    "P1366": "{head} was replaced by {tail}.",
    "P1376": "{head} is the capital of {tail}.",
    "P1412": "{head} speaks the language {tail}.",
    "P1441": "{head} is present in the work {tail}.",
    "P3373": "{head} is a sibling of {tail}.",
}


def verbalize_triple(head: str, relation: str, tail: str) -> str:
    template = VERBALIZATION_TEMPLATES.get(relation)
    if template:
        return template.format(head=head, tail=tail)
    from freige.data.docred_processor import DOCRED_REL_INFO
    rel_name = DOCRED_REL_INFO.get(relation, relation)
    return f"{head} {rel_name} {tail}."


class CEDRewardModel:
    """CED 对比证据判别奖励模型。"""

    def __init__(
        self,
        model_name: str = DEFAULT_NLI_MODEL,
        device: Optional[str] = None,
        max_length: int = 512,
    ):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.max_length = max_length

        logger.info("Loading NLI model: %s", model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

        self._resolve_entailment_idx()

    def _resolve_entailment_idx(self):
        id2label = self.model.config.id2label
        self.entail_idx = None
        for idx, label in id2label.items():
            if label.lower() in ("entailment", "entail"):
                self.entail_idx = int(idx)
                break
        if self.entail_idx is None:
            logger.warning(
                "Could not find 'entailment' in id2label=%s, defaulting to index 1",
                id2label,
            )
            self.entail_idx = 1
        logger.info("Entailment index: %d (id2label=%s)", self.entail_idx, id2label)

    @torch.no_grad()
    def nli_entailment_prob(
        self, premises: list[str], hypotheses: list[str]
    ) -> torch.Tensor:
        inputs = self.tokenizer(
            premises,
            hypotheses,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        ).to(self.device)

        logits = self.model(**inputs).logits
        probs = F.softmax(logits, dim=-1)
        return probs[:, self.entail_idx].cpu()

    def compute_ced_reward(
        self,
        claim: str,
        cited_evidence_sents: list[str],
        hard_negative_sents: list[str],
        tau: float = 0.5,
    ) -> dict:
        evidence_concat = " ".join(cited_evidence_sents)
        p_pos = self.nli_entailment_prob(
            [evidence_concat], [claim]
        ).item()

        if not hard_negative_sents:
            p_neg = 0.0
        else:
            neg_probs = self.nli_entailment_prob(
                hard_negative_sents, [claim] * len(hard_negative_sents)
            )
            p_neg = neg_probs.max().item()

        margin = p_pos - p_neg
        reward = max(0.0, margin) * float(p_pos > tau)

        return {
            "reward": reward,
            "p_pos": p_pos,
            "p_neg": p_neg,
            "margin": margin,
        }

    def compute_ced_reward_batch(
        self,
        claims: list[str],
        cited_evidence_list: list[list[str]],
        hard_negative_list: list[list[str]],
        tau: float = 0.5,
    ) -> list[dict]:
        n = len(claims)
        assert len(cited_evidence_list) == n and len(hard_negative_list) == n

        pos_premises = [" ".join(ev) for ev in cited_evidence_list]
        pos_probs = self.nli_entailment_prob(pos_premises, claims)

        all_neg_premises = []
        all_neg_hyps = []
        neg_counts = []
        for i in range(n):
            negs = hard_negative_list[i]
            neg_counts.append(len(negs))
            all_neg_premises.extend(negs)
            all_neg_hyps.extend([claims[i]] * len(negs))

        if all_neg_premises:
            all_neg_probs = self.nli_entailment_prob(all_neg_premises, all_neg_hyps)
        else:
            all_neg_probs = torch.tensor([])

        results = []
        offset = 0
        for i in range(n):
            p_pos = pos_probs[i].item()
            nc = neg_counts[i]
            if nc > 0:
                p_neg = all_neg_probs[offset:offset + nc].max().item()
            else:
                p_neg = 0.0
            offset += nc

            margin = p_pos - p_neg
            reward = max(0.0, margin) * float(p_pos > tau)
            results.append({
                "reward": reward,
                "p_pos": p_pos,
                "p_neg": p_neg,
                "margin": margin,
            })

        return results

    def compute_flat_nli_reward(
        self,
        claim: str,
        cited_evidence_sents: list[str],
        tau: float = 0.5,
    ) -> dict:
        evidence_concat = " ".join(cited_evidence_sents)
        p_pos = self.nli_entailment_prob(
            [evidence_concat], [claim]
        ).item()
        reward = p_pos * float(p_pos > tau)
        return {"reward": reward, "p_pos": p_pos}
