# **SentinelFlow — Agentic Security Pipeline**  
A lightweight, agent‑driven security analysis pipeline designed for demos, workshops, and rapid prototyping. SentinelFlow showcases how multi‑agent reasoning, governance enforcement, and structured security insights can be orchestrated through a clean FastAPI backend and a minimal Next.js frontend.

This demo version is intentionally small, inexpensive to run, and easy to deploy — while still demonstrating the core architectural patterns of modern AI security systems.

---

## **High‑Level Architecture**

```mermaid
flowchart LR
    A[User] --> B[Next.js Frontend<br/>Vercel]
    B -->|POST /run-pipeline| C[FastAPI Backend<br/>Azure Container Apps]
    C --> D[Recon Agent]
    D --> E[Analysis Agent]
    E --> F[Hypothesis Agent]
    F --> G[Action Agent]
    G --> H[Governance Evaluation]
    H --> B
```

---

## **Agent Pipeline (Detailed)**

```mermaid
sequenceDiagram
    participant U as User
    participant FE as Frontend (Next.js)
    participant BE as Backend (FastAPI)
    participant R as Recon Agent
    participant A as Analysis Agent
    participant H as Hypothesis Agent
    participant AC as Action Agent
    participant G as Governance Engine

    U->>FE: Submit Alert
    FE->>BE: POST /run-pipeline { text }
    BE->>R: recon_agent(text)
    R-->>BE: Recon Output
    BE->>G: evaluate_governance(recon)
    G-->>BE: Governance Flags

    BE->>A: analysis_agent(recon.output)
    A-->>BE: Analysis Output
    BE->>G: evaluate_governance(analysis)
    G-->>BE: Governance Flags

    BE->>H: hypothesis_agent(analysis.output)
    H-->>BE: Hypothesis Output
    BE->>G: evaluate_governance(hypothesis)
    G-->>BE: Governance Flags

    BE->>AC: action_agent(hypothesis.output)
    AC-->>BE: Action Output
    BE->>G: evaluate_governance(action)
    G-->>BE: Governance Flags

    BE-->>FE: Full Timeline (Recon → Analysis → Hypothesis → Action)
    FE-->>U: Rendered UI
```

---

## **Deployment Topology**

```mermaid
graph TD
    subgraph Local Dev
        LFE[Next.js Dev Server]
        LBE[FastAPI + Uvicorn]
    end

    subgraph Cloud Deployment
        V[Vercel Frontend]
        ACR[Azure Container Registry]
        ACA[Azure Container Apps<br/>FastAPI Container]
    end

    LFE --> LBE
    V --> ACA
    ACA --> ACR
```

---

## **Features**

- Multi‑agent security reasoning  
- Structured JSON outputs  
- Risk scoring  
- Governance enforcement (sandbox, approval-required)  
- Timeline‑style results  
- Minimal, clean UI  
- Cloud‑native deployment  
- Zero‑cost demo footprint  

---

## **Backend Setup (FastAPI + Azure Container Apps)**

### **Local Development**

```bash
uvicorn app.main:app --reload
```

### **Docker Build**

```bash
docker build -t sentinelflow-backend:latest .
```

### **Push to Azure Container Registry**

```bash
az acr login --name sentinelflowacr
docker tag sentinelflow-backend:latest sentinelflowacr.azurecr.io/sentinelflow-backend:latest
docker push sentinelflowacr.azurecr.io/sentinelflow-backend:latest
```

### **Deploy / Update Azure Container App**

```bash
az containerapp update --name sentinelflow-backend --resource-group sentinelflow-rg --image sentinelflowacr.azurecr.io/sentinelflow-backend:latest
```

Azure automatically creates a new revision.

---

## **Frontend Setup (Next.js + Vercel)**

### **Install dependencies**

```bash
npm install
```

### **Environment variable**

Create `.env.local`:

```
NEXT_PUBLIC_API_URL=https://<your-container-app-url>
```

### **Run locally**

```bash
npm run dev
```

### **Deploy to Vercel**

```bash
vercel
```

Add the same environment variable in Vercel’s dashboard.

---

## **CORS Configuration**

SentinelFlow enables cross‑origin requests for local dev and Vercel:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## **Project Structure**

```
sentinel_flow/
  backend/
    app/
      agents/
      governance/
      main.py
    Dockerfile

  frontend/
    app/
      page.tsx
    .env.local
    package.json
```

---

## **Roadmap**

- SOC‑style dashboard  
- Timeline visualization  
- Agent streaming  
- Threat taxonomy mapping  
- Analytics panel  
- Multi‑tenant mode