Software supply chain security has become a critical concern due to the widespread use of
open-source third-party dependencies in modern software systems. 
**Software Bill of Materials (SBOM)** and **Software Composition Analysis (SCA)** tools are widely adopted to improve
dependency transparency and detect known vulnerabilities. However, the effectiveness of
SBOM-based approaches as standalone mechanisms for vulnerability assessment remains un-
clear. This thesis the research questions: 1. Is an SBOM-based approach a reliable
proxy for vulnerability assessment compared to traditional SCA tools? 2. Does a hybrid
approach combining SBOM and SCA improve vulnerability coverage? 
To answer these, we conducted an experimental study on popular open-source Java Maven and Python GitHub
repositories, using Trivy, Snyk, and OSV-Scanner to implement workflows for SBOM-based,
SCA-based, and SBOM-refined vulnerability assessment pipelines. 
