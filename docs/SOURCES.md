# Verified source notes

Research date: October 9, 2026. Only primary sources below support implementation or factual claims. Source access does not imply successful media download, provider credentials or a validated product.

## Evidence and event

| Source | Supported fact / limit |
| --- | --- |
| [UCSF study abstract](https://pubmed.ncbi.nlm.nih.gov/27153160/) | 58 neurosurgery cases; sample mean $653 unused supplies; adjusted departmental estimate $968/case and $2.9M/year. Historical, department-specific estimates |
| [VAST Builders Challenge](https://www.vastdata.com/lp/vast-builders-challenge) | Event services include Cosmos, semantic search, YOLO and W&B models. No actual API schemas established by this page |
| [NYC organizer listing](https://luma.com/vastnyc) | Agenda, sponsor roles and provision of videos. The listing does not promise OR supply footage |

## Dataset maintainers

| Source | Supported fact / limit |
| --- | --- |
| [MVOR repository](https://github.com/CAMMA-public/MVOR) | Real OR sampled multi-view frames, download instructions and CC BY-NC-SA 4.0 license. Not a complete continuous supply case |
| [AVOS lab page](https://research.bidmc.org/surgical-informatics/avos) | Public open-surgery video research and tool/action annotations. Individual-video reuse permission and package coverage not established |
| [Team-OR repository](https://github.com/CAMMA-public/Team-OR) | Authors explicitly say the dataset is not publicly available |
| [EgoExOR-HQ data card](https://huggingface.co/datasets/TUM/EgoExOR) | Emulated procedures, high-resolution ego/external views, phase HDF5 and Apache 2.0 data license |
| [EgoExOR data utilities](https://github.com/ardamamur/EgoExOR/blob/main/data/README.md) | Take discovery/visualization and legacy/HQ layouts. Export choices and redaction remain our work |
| [MM-OR repository](https://github.com/egeozsoy/MM-OR) | Multimodal OR dataset; access form required. Code license is separate from accepted data terms |
| [4D-OR repository](https://github.com/egeozsoy/4D-OR) | Simulated knee procedures, RGB-D sequences at 1 FPS; access form |

## Technical references

| Source | Supported fact / limit |
| --- | --- |
| [YOLO-World integration](https://docs.ultralytics.com/models/yolo-world/) | Open-vocabulary detector and tracking integration; no guarantee of small medical-supply accuracy |
| [Ultralytics tracking](https://docs.ultralytics.com/modes/track/) | Tracker options and persistent tracking context; application identity/reconciliation still required |
| [Original YOLO-World](https://github.com/AILab-CVC/YOLO-World) | Original implementation and GPL-v3 license; check chosen implementation/weights/service terms before reuse/distribution |
| [NVIDIA Cosmos Reason2 prompt guide](https://nvidia-cosmos.github.io/cosmos-cookbook/getting_started/prompt_guide/reason_guide.html) | Media ordering and requested structured/temporal outputs; prompt structure is not correctness proof |
| [NVIDIA NIM Reason2 API](https://docs.nvidia.com/nim/vision-language-models/1.7.0/examples/cosmos-reason2/api.html) | One documented video transport/API format; organizer wrapper may differ |
| [W&B inference](https://docs.wandb.ai/inference/) | OpenAI-compatible model serving option; event-specific endpoint/model/access must be supplied |
| [Weave evaluation tutorial](https://docs.wandb.ai/weave/tutorial-eval) | Model/dataset/evaluation workflow and instrumentation |
| [Weave scorers](https://docs.wandb.ai/weave/guides/evaluation/scorers) | Deterministic/custom scorer integration; scorers must reflect our ground truth and metrics |
| [OpenAI model guidance](https://learn.chatgpt.com/docs/models) | Current model selection and reasoning-effort guidance; availability depends on account/client |
| [OpenAI permission profiles](https://learn.chatgpt.com/docs/permissions) | Workspace and network scope controls; managed policies may constrain settings |
| [GitHub CLI authentication](https://cli.github.com/manual/gh_auth_login) | Browser-based login and credential-storage behavior |

## Design decisions, not sourced claims

The SQLite ledger, cents arithmetic, human verification gate, six-class starting scope, thresholds/latency targets, adapter interfaces, synthetic prices, UI layout, 20-case aggregate threshold and manufacturing expansion are proposed design choices. They are not validated by the study or promised by the sponsor stack. Update assumptions and docs as measured evidence arrives.
