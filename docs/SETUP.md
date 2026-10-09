# Codex, GitHub and implementation setup

## Repository and identity

Target: [LaboriouslyExquisite/or-waste-tracker](https://github.com/LaboriouslyExquisite/or-waste-tracker). It was empty when inspected during this preparation session. The Markdown package is separate from the parent climate project.

Use your own GitHub account or an organization you control. Codex does not need a separate personal account. A private repository can be edited with authenticated permission; public visibility only allows unauthenticated reading, not pushing. Choose visibility based on event rules and sharing preferences. Never upload original clinical footage or secrets as a way to make the demo accessible.

The GitHub plugin is installed and authenticated as `LaboriouslyExquisite`. Its repository metadata confirms read, push and admin permissions for this project, and the connector successfully read the published README. Local Git pushing was also verified. No additional account or public-visibility change is needed for this project.

GitHub CLI was not found on PATH at preparation time. If you choose CLI authentication, install it through an approved installer and run this locally:

```powershell
gh auth login --hostname github.com --git-protocol https --web
gh auth status
gh auth setup-git
```

The browser login normally uses the system credential store; the CLI documents a plaintext fallback when that store is unavailable. Check the reported storage method. Do not paste a personal access token into chat. [GitHub authentication reference](https://cli.github.com/manual/gh_auth_login)

The preparation package is published on `codex/vast-build-brief`, currently the repository's default branch. Start implementation from that branch and create a separate `codex/` implementation branch. Review changes before merging. Git author identity and push credentials are different settings; commit authorship does not grant repository access.

## Recommended Codex settings

My recommendation for this workload: GPT-6.1 Sol with High or Extra High reasoning for the initial build, architecture and event rules, then High/Medium for focused UI changes. Astra is an option for the hardest design/review problems when available. This is a workload recommendation, not a claim about what your account exposes. Official guidance recommends GPT-6.1 Sol for complex coding and describes High/Extra High for multi-step work. [Models and reasoning](https://learn.chatgpt.com/docs/models)

Use workspace-scoped write access, allow the network destinations needed by GitHub, dependency registries and the organizer stack, and retain approval for operations outside that scope. The current session has restricted shell network access; successful web browsing does not imply shell Git/network permission. Full-machine access is unnecessary for this build. Managed organization settings may constrain choices. [Permission profiles](https://learn.chatgpt.com/docs/permissions)

Select this repository as the project; keep [AGENTS.md](../AGENTS.md) at its root. Give the build prompt, verified stack handoff, permitted media manifest and acceptance tests together. Long-running requests are more reliable with a concrete local demo and checkpoints than an instruction to "one-shot" unknown APIs. Use the bundled browser tools to inspect the final dashboard when implementation is ready.

## Local runtime

Needed during implementation: working Python 3.11+, Node compatible with the chosen Vite release, Git and FFmpeg. Pin supported dependency versions after checking their current official requirements. A Python alias on PATH is not proof the interpreter is installed. The provided model services remove the need for a laptop GPU.

At preparation time, Node/Git/FFmpeg were found on PATH; Python resolved to a Windows application alias and still needs a version check. No app packages have been installed for this repository.

Expected implementation commands, to be made real and verified by the build session:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend/requirements.txt
npm --prefix frontend ci
.\.venv\Scripts\python.exe scripts/seed_demo.py
.\.venv\Scripts\python.exe scripts/start_demo.py
```

These scripts/dependency files do not exist yet. The implementation must provide a single demo startup path, plus separate documented dev-server, test, evaluate and export commands. Avoid changing root dependencies of the parent climate repository.

## Secrets and permissions

Generate a `.gitignore` before creating runtime artifacts. Ignore `.env`, local stack config with credentials, `.venv`, `node_modules`, built assets, runtime databases, raw/redacted media and credential files. A secret-free `.env.example` can be tracked with an explicit exception. Store only small permitted fixtures and manifests in Git.

Event access may include API keys, bearer tokens, storage credentials or an authenticated gateway session. Collect actual requirements in [STACK_ACCESS.md](STACK_ACCESS.md). Keep keys server-side; do not use frontend `VITE_` environment variables for provider credentials. Limit repository/service access to the project involved.

## Deployment choice

Run the local backend and browser UI for the hackathon first. If organizers supply a hosted app runtime, confirm disk persistence, backend process support, network access and asset privacy before deploying. VAST/CoreWeave model access does not automatically supply application hosting.

A future public preview should use permitted redacted media or synthetic data, with access controls appropriate to the source. Hosting a real clinical-video workflow requires a separate design and permissions decision. This preparation session does not authorize publishing patient footage.
