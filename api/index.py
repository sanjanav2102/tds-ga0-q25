from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  [
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 230.02,
    "uptime_pct": 99.121,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 230.02,
    "uptime_pct": 98.41,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 141.68,
    "uptime_pct": 99.353,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 220.2,
    "uptime_pct": 98.239,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 140.63,
    "uptime_pct": 99.423,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 141.76,
    "uptime_pct": 98.848,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 130.14,
    "uptime_pct": 97.966,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 201.63,
    "uptime_pct": 98.45,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 208.22,
    "uptime_pct": 97.758,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 206.83,
    "uptime_pct": 97.791,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 178.72,
    "uptime_pct": 98.494,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 202.54,
    "uptime_pct": 98.87,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 141.83,
    "uptime_pct": 97.971,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 140.62,
    "uptime_pct": 97.547,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 174.24,
    "uptime_pct": 97.101,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 143.51,
    "uptime_pct": 98.981,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 142.29,
    "uptime_pct": 98.135,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 222.11,
    "uptime_pct": 99.253,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 212.32,
    "uptime_pct": 98.826,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 121.63,
    "uptime_pct": 98.006,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 214.05,
    "uptime_pct": 99.494,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 146.01,
    "uptime_pct": 98.406,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 166.85,
    "uptime_pct": 98.079,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 172.49,
    "uptime_pct": 99.336,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 157.9,
    "uptime_pct": 98.295,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 150.11,
    "uptime_pct": 97.627,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 170.58,
    "uptime_pct": 97.826,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 234.91,
    "uptime_pct": 97.328,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 108.17,
    "uptime_pct": 99.436,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 171.67,
    "uptime_pct": 98.87,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 167.95,
    "uptime_pct": 97.704,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 220.39,
    "uptime_pct": 98.934,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 144.3,
    "uptime_pct": 98.846,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 136.37,
    "uptime_pct": 97.793,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 191.04,
    "uptime_pct": 99.119,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 140.22,
    "uptime_pct": 98.183,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 165)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
