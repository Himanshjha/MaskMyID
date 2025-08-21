import React from "react";

function ResultView({ maskedImage, details }) {
  if (!maskedImage) return null;

  return (
    <div className="mt-8 bg-white/40 backdrop-blur-lg p-6 rounded-3xl shadow-xl text-center border border-gray-200">
      <h3 className="text-2xl font-semibold text-indigo-700 mb-4">
        🎉 Masked Result
      </h3>

      <div className="flex justify-center mb-4">
        <img
          src={maskedImage}
          alt="Masked ID"
          className="max-w-xs sm:max-w-md rounded-2xl shadow-lg border border-gray-300"
        />
      </div>

      {/* Optional: Show detected PII list */}
      {details && (
        <div className="bg-gray-50 rounded-lg p-4 text-left shadow-sm">
          <h4 className="text-lg font-medium text-gray-700 mb-2">🔍 Detected PII</h4>
          <ul className="list-disc list-inside text-sm text-gray-600">
            {Object.entries(details).map(([key, value]) => (
              <li key={key}>
                <span className="font-semibold">{key}:</span> {value}
              </li>
            ))}
          </ul>
        </div>
      )}

      <a
        href={maskedImage}
        download="masked_id.png"
        className="mt-6 inline-block px-6 py-2 bg-green-600 text-white font-medium rounded-lg shadow-md hover:bg-green-700 transition-transform transform hover:scale-105"
      >
        ⬇️ Download Masked ID
      </a>
    </div>
  );
}

export default ResultView;
