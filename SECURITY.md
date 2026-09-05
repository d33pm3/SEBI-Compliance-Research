# Security Policy

## Report a vulnerability or exposure

Do not open a public issue for suspected credentials, personal data, confidential
documents, or other sensitive information. Use GitHub's private vulnerability reporting
feature for this repository, if enabled, or contact the repository owner privately.

Include the affected path or commit, the exposure category, and the minimum information
needed to reproduce the issue. Do not include the secret or confidential payload itself.

## Repository data policy

This repository must not contain:

- environment files, API keys, tokens, private keys, certificates, or OAuth credentials;
- client or customer records, screenshots, exports, findings, or internal reports;
- internal URLs, hosts, IP addresses, database or service-account identifiers;
- private prompts, proprietary source documents, RAG corpora, vector stores, or embeddings;
- production configurations or generated compliance registers containing non-public data.

If sensitive material is committed, stop further distribution, revoke or rotate affected
credentials immediately, remove the material from Git history, and document the response
privately with the repository owner.
