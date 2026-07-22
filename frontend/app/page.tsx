"use client";

import { useState } from "react";

const SAMPLE_ALERTS = [
  "Suspicious login from unknown device",
  "Unusual data exfiltration pattern",
  "Privilege escalation attempt detected",
  "Multiple failed logins from service account",
];

export default function Home() {
  const [input, setInput] = useState(SAMPLE_ALERTS[0]);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  async function runPipeline() {
    setLoading(true);
    setResult(null);

    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/run-pipeline`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input }),
      }
    );

    const data = await res.json();
    setResult(data);
    setLoading(false);
  }

  return (
    <div className="min-h-screen bg-black text-white px-6 py-12">
      <h1 className="text-3xl font-bold mb-6">SentinelFlow Demo</h1>

      {/* Input Box */}
      <div className="mb-4">
        <label className="block mb-2 text-sm text-gray-400">
          Alert Text
        </label>
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="w-full p-3 rounded bg-gray-900 border border-gray-700"
          rows={3}
        />
      </div>

      {/* Sample Alerts */}
      <div className="flex gap-2 mb-4 flex-wrap">
        {SAMPLE_ALERTS.map((a) => (
          <button
            key={a}
            onClick={() => setInput(a)}
            className="px-3 py-1 bg-gray-800 hover:bg-gray-700 rounded text-sm"
          >
            {a}
          </button>
        ))}
      </div>

      {/* Run Button */}
      <button
        onClick={runPipeline}
        disabled={loading}
        className="px-6 py-3 bg-blue-600 hover:bg-blue-500 rounded font-semibold"
      >
        {loading ? "Running..." : "Run Pipeline"}
      </button>

      {/* Results */}
      {result && (
        <div className="mt-10 space-y-6">
          {result.map((step: any, idx: number) => (
            <div
              key={idx}
              className="p-5 rounded bg-gray-900 border border-gray-700"
            >
              {/* Step Header */}
              <div className="flex items-center justify-between mb-3">
                <h2 className="text-xl font-bold">{step.step}</h2>

                {/* Risk Score Badge */}
                <span
                  className="px-3 py-1 rounded text-sm"
                  style={{
                    background:
                      step.riskScore < 0.4
                        ? "#2563eb"
                        : step.riskScore < 0.7
                        ? "#d97706"
                        : "#dc2626",
                  }}
                >
                  Risk: {Math.round(step.riskScore * 100)}%
                </span>
              </div>

              {/* Governance Flags */}
              {step.governance.length > 0 && (
                <div className="mb-3 text-sm text-yellow-400">
                  Governance:{" "}
                  {step.governance.map((g: any) => g.type).join(", ")}
                </div>
              )}

              {/* Pretty JSON */}
              <pre className="bg-black p-4 rounded text-sm overflow-x-auto border border-gray-800">
                {JSON.stringify(step.output, null, 2)}
              </pre>

              {/* Reasoning */}
              <div className="mt-3 text-gray-400 text-sm">
                Reasoning: {step.reasoning}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}