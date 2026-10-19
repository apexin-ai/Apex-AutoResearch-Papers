import torch
import torch.nn as nn
import torchvision.transforms.v2 as T

from acib.config import ACIBConfig
from acib.scorer import ACIBScorer
from acib.losses import ACIBLoss


class ACIBPolicy(nn.Module):
    """SmolVLA + Action-Conditioned Information Bottleneck.

    Wraps SmolVLAPolicy with a forward hook on the connector module
    that reweights visual tokens before they enter the VLM layers.

    Module hierarchy (verified from lerobot source):
        base_policy.model                          -> VLAFlowMatching
        base_policy.model.vlm_with_expert          -> SmolVLMWithExpertModel
        base_policy.model.vlm_with_expert.vlm      -> SmolVLMForConditionalGeneration
        base_policy.model.vlm_with_expert.vlm.model.vision_model  -> SigLIP
        base_policy.model.vlm_with_expert.vlm.model.connector     -> PixelShuffle + Linear
        base_policy.model.vlm_with_expert.vlm.model.text_model    -> LM backbone
        base_policy.model.vlm_with_expert.lm_expert               -> Action expert

    Hook target: connector (fires once per camera in embed_prefix loop).
    Conditioning: visual token mean pooling (self-conditioning, MVP).
    """

    def __init__(self, base_policy: nn.Module, acib_config: ACIBConfig):
        super().__init__()
        self.base_policy = base_policy
        self.acib_config = acib_config

        self.scorer = ACIBScorer(acib_config)
        self.acib_loss_fn = ACIBLoss(acib_config)
        self.acib_enabled = True
        self._cached_logits: list[torch.Tensor] = []
        self._hook_handles: list = []

        self._perturb_transform = self._build_perturb_transform()
        self._setup_freeze(acib_config)
        self._install_hooks()

    @property
    def _vlm_with_expert(self):
        return self.base_policy.model.vlm_with_expert

    @property
    def _connector(self) -> nn.Module:
        return self._vlm_with_expert.vlm.model.connector

    @property
    def _vision_encoder(self) -> nn.Module:
        return self._vlm_with_expert.vlm.model.vision_model

    def _install_hooks(self) -> None:
        handle = self._connector.register_forward_hook(self._connector_hook)
        self._hook_handles.append(handle)

    def _connector_hook(self, module, input, output):
        if not self.acib_enabled:
            return output
        # output: (B, N, D) — connector output for one camera
        condition = output.mean(dim=1)  # (B, D) self-conditioning
        weights, logits = self.scorer(output, condition)
        self._cached_logits.append(logits)
        return self.scorer.apply_weights(output, weights)

    def forward(self, batch: dict[str, torch.Tensor]) -> tuple[torch.Tensor, dict]:
        self._cached_logits = []

        task_loss, loss_dict = self.base_policy.forward(batch)

        if not self.acib_enabled or not self._cached_logits:
            return task_loss, loss_dict

        scores_clean = torch.cat(self._cached_logits, dim=1)

        scores_perturbed = None
        if self.training:
            scores_perturbed = self._score_perturbed(batch)

        acib_losses = self.acib_loss_fn(task_loss, scores_clean, scores_perturbed)
        loss_dict["acib_task"] = acib_losses["task"]
        loss_dict["acib_consistency"] = acib_losses["consistency"]
        loss_dict["acib_ib"] = acib_losses["ib"]
        return acib_losses["total"], loss_dict

    @staticmethod
    def _build_perturb_transform() -> T.Transform:
        """Random augmentation covering MVP 4 perturbation dimensions."""
        return T.RandomChoice([
            T.RandomAffine(degrees=15, translate=(0.05, 0.05)),
            T.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3, hue=0.1),
            T.GaussianBlur(kernel_size=7, sigma=(0.5, 2.0)),
        ])

    def _score_perturbed(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        """Score perturbed visual tokens for consistency loss.

        Runs perturbed images through vision_encoder + connector (matching the
        clean path) then scores the connector-output tokens with the scorer.
        """
        image_keys = sorted(
            k for k in batch
            if k.startswith("observation.images.") and isinstance(batch[k], torch.Tensor)
            and batch[k].dim() == 4
        )
        if not image_keys:
            return None

        prev = self.acib_enabled
        self.acib_enabled = False
        all_logits = []
        try:
            for key in image_keys:
                img = batch[key]
                if torch.rand(1).item() < 0.75:
                    perturbed = self._perturb_transform(img)
                else:
                    perturbed = img + torch.randn_like(img) * 0.1
                with torch.no_grad(), torch.autocast(device_type="cuda", dtype=torch.bfloat16):
                    target_size = self._vlm_with_expert.vlm.config.vision_config.image_size
                    if perturbed.shape[-1] != target_size or perturbed.shape[-2] != target_size:
                        perturbed = torch.nn.functional.interpolate(
                            perturbed, size=(target_size, target_size), mode="bilinear", align_corners=False,
                        )
                    vis_out = self._vision_encoder(perturbed)
                    raw_tokens = vis_out.last_hidden_state if hasattr(vis_out, "last_hidden_state") else vis_out[0]
                    tokens = self._connector(raw_tokens)
                condition = tokens.mean(dim=1)
                _, logits = self.scorer(tokens, condition)
                all_logits.append(logits)
        finally:
            self.acib_enabled = prev
        return torch.cat(all_logits, dim=1) if all_logits else None

    def _setup_freeze(self, config: ACIBConfig) -> None:
        if config.freeze_vlm:
            for param in self._vlm_with_expert.vlm.parameters():
                param.requires_grad = False
        if config.freeze_action_expert:
            for param in self._vlm_with_expert.lm_expert.parameters():
                param.requires_grad = False
        if config.train_scorer_only:
            for param in self.base_policy.parameters():
                param.requires_grad = False
        for param in self.scorer.parameters():
            param.requires_grad = True

    def select_action(self, batch: dict[str, torch.Tensor], **kwargs) -> torch.Tensor:
        return self.base_policy.select_action(batch, **kwargs)

    def reset(self):
        self.base_policy.reset()

    def get_optim_params(self) -> dict:
        base_params = self.base_policy.get_optim_params()
        scorer_params = {
            "params": list(self.scorer.parameters()),
            "lr": base_params.get("lr", 1e-4),
        }
        if isinstance(base_params, dict):
            return [base_params, scorer_params]
        elif isinstance(base_params, list):
            return base_params + [scorer_params]
        return [scorer_params]

    def get_scorer_stats(self) -> dict[str, float]:
        if not self._cached_logits:
            return {}
        logits = torch.cat(self._cached_logits, dim=1)
        w = torch.sigmoid(logits)
        return {
            "scorer/mean": w.mean().item(),
            "scorer/std": w.std().item(),
            "scorer/min": w.min().item(),
            "scorer/max": w.max().item(),
            "scorer/sparsity": (w < 0.5).float().mean().item(),
        }

    def toggle_acib(self, enabled: bool) -> None:
        self.acib_enabled = enabled

    def remove_hooks(self):
        for h in self._hook_handles:
            h.remove()
        self._hook_handles.clear()

    @classmethod
    def from_pretrained(cls, model_id: str, acib_config: ACIBConfig | None = None):
        from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy

        base_policy = SmolVLAPolicy.from_pretrained(model_id)
        if acib_config is None:
            vlm_hidden = base_policy.model.vlm_with_expert.config.text_config.hidden_size
            acib_config = ACIBConfig(visual_dim=vlm_hidden, condition_dim=vlm_hidden)
        return cls(base_policy, acib_config)
