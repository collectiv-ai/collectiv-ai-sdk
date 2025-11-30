<p align="center">
  <img src="logo.png" alt="CollectiVAI Logo" width="360" />
</p>

<h1 align="center">CollectiVAI SDKs</h1>
<h3 align="center">Official client libraries for the CollectiVAI Router & ecosystem</h3>

<p align="center">
  <a href="https://collectivai.org">
    <img src="https://img.shields.io/badge/Website-collectivai.org-003399?style=flat" alt="Website" />
  </a>
  <a href="https://github.com/collectiv-ai/collectiv-ai-router">
    <img src="https://img.shields.io/badge/Backend-Router-0055aa?style=flat" alt="CollectiVAI Router" />
  </a>
  <img src="https://img.shields.io/badge/Status-Prototype-ffcc00?style=flat" alt="Status" />
  <img src="https://img.shields.io/badge/Made%20in-Europe-003399?style=flat" alt="Made in Europe" />
</p>

---

## Overview

This repository contains **official SDKs** for the CollectiVAI ecosystem.

- 🌐 **TypeScript / JavaScript SDK** (`sdk-ts/`)  
  – for web frontends, Node.js services and integration tests.

- 🐍 **Python SDK** (`sdk-py/`)  
  – for research, data pipelines, CLI tools and backend services.

Both SDKs are currently focused on the **CollectiVAI Router**:

- call the `/api/chat` endpoint,
- send a structured JSON request,
- receive a unified response with:
  - `reply`
  - `providerUsed`
  - `model`
  - optional `routingInfo` (reason, filters, latencyMs).

> ⚠️ **Prototype status:**  
> These SDKs are early, public reference implementations.  
> They are not yet feature-complete and may change without notice.

---

## API contract (Router)

Both SDKs are thin clients around the same HTTP API, exposed by the
[`collectiv-ai-router`](https://github.com/collectiv-ai/collectiv-ai-router).

### Request

```jsonc
POST /api/chat
{
  "prompt": "How can citizens participate in climate decisions in the EU?",
  "mode": "ethical",
  "provider": "auto",
  "topic": "climate",
  "modelId": null,
  "serviceProfile": "citizen_advisor"
}
