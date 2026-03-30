# 🧠 multinet-3d-constraints

### A lightweight benchmark for evaluating cross-modal generalization in embodied 3D environments with hidden constraints.

---

## Overview

This repository implements a minimal 3D embodied environment designed to test whether agents can **transfer abstract reasoning capabilities across modalities**.

Many models perform well within a single modality (e.g., language or grid-based environments) but fail when task structure is preserved and the modality changes. This benchmark focuses on that gap.

> Can an agent trained in one modality correctly infer and apply constraints when placed in a partially observable, interactive 3D environment?

## Cross-Modal Task Alignment

```mermaid
flowchart LR
    A[Task Specification\n(Shared Structure)] --> B[GridWorld\n(Symbolic / Discrete)]
    A --> C[Language\n(Instruction Only)]
    A --> D[3D Environment\n(Embodied + Occlusion)]

    B --> E[Agent Learns Rule\n(e.g., fragile)]
    C --> E
    E --> D

    D --> F[Evaluation\nSuccess / Violations / Generalization]

---

## Core Idea

Tasks are defined by a shared **task specification** that can be instantiated across multiple modalities:

- grid-based environments
- language-only settings
- embodied 3D simulations (this repository)

The 3D environment introduces:

- **partial observability** (occlusion)
- **continuous interaction**
- **perspective-dependent perception**

while preserving underlying task structure.

This enables evaluation of **true capability transfer**, rather than re-learning.

---

## Example Task

**Instruction**

> Retrieve the red object without disturbing fragile items.

**Task Specification**

```json
{
  "task_id": "fragile_retrieval_v1",
  "goal": "retrieve_object",
  "target": "red_sphere",
  "constraints": ["fragile"],
  "environment": {
    "occlusion": true,
    "layout": "procedural"
  }
}

multinet-3d-constraints/
│
├── sim/
│   ├── environment.py        # core world + step logic
│   ├── objects.py            # object definitions
│   ├── rules.py              # hidden constraints
│   ├── occlusion.py          # visibility logic
│
├── tasks/
│   ├── task_spec.py          # shared task format
│   ├── generator.py          # creates task instances
│   ├── templates.py          # language instructions
│
├── agents/
│   ├── base_agent.py
│   ├── random_agent.py
│   ├── heuristic_agent.py
│
├── eval/
│   ├── metrics.py
│   ├── evaluator.py
│
├── experiments/
│   ├── run_experiment.py
│   ├── configs/
│   │   └── default.yaml
│
├── assets/                   # optional later
├── docs/
│
├── README.md
├── requirements.txt
├── setup.py (optional)
└── .gitignore
